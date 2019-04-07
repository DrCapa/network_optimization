"""network optimization with pyomo abstract model
   minimum cost flow problem"""

from pyomo.opt import SolverFactory
from pyomo.environ import *
import pandas as pd


input_data = 'input.xlsx'

costs = pd.read_excel(input_data, index_col=0, sheet_name='cost')
capacities = pd.read_excel(input_data, index_col=0, sheet_name='capacity')
sup_dem = pd.read_excel(input_data, index_col=0, sheet_name='sup_dem')

# Feasible solution property
if sup_dem['sup_dem'].sum(axis=0) == 0:
    print('problem is feasible')
else:
    print('problem is infeasible')

# Select solver
opt = SolverFactory('cbc')

# Create model
m = AbstractModel()

# set, variable
m.i = Set(initialize=costs.index)
m.x = Var(m.i, m.i, within=NonNegativeIntegers)


# Objective
def obj_expression(m):
    return sum(costs.loc[i, j]*m.x[i, j]
               for i in m.i
               for j in m.i
               )
m.obj = Objective(rule=obj_expression, sense=minimize)


# node constraints
def node_constraint(m, i, j):
    if costs.loc[i, j] == 0:
        return Constraint.Skip
    else:
        return (sum(m.x[i, j] for j in m.i)-sum(m.x[j, i] for j in m.i) ==
                sup_dem.loc[i, 'sup_dem'])
m.node_constraint = Constraint(m.i, m.i, rule=node_constraint)


# maximale capacity constraint
def max_capacity(m, i, j):
    return m.x[i, j] <= capacities.loc[i, j]
m.max_capacity = Constraint(m.i, m.i, rule=max_capacity)


# Create instanz
instance = m.create_instance()

# Solve the optimization problem
results = opt.solve(instance, symbolic_solver_labels=True,
                    tee=True, load_solutions=True)

for i in instance.i.value:
    for j in instance.i.value:
        if(instance.x[i, j].value != 0):
            print('from ', i, ' to ', j, ': ',
                  instance.x[i, j].value, ' units')
