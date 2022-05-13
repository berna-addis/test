import os
import sys
import pyomo.environ as pe

__author__ = "Bernardetta Addis"

def create_model():

    model = pe.AbstractModel()
    
    model.components = pe.Set(ordered=True)

    model.pinco = pe.Set(ordered=True)

    model.input_ML = pe.Set(ordered=True)

    """
    model.W1_ML = pe.Param(model.set_mem_type_num_neurons,
                           model.input_ML,
                           mutable=True,default=0.1)
    """

    model.x = pe.Var(model.components, domain=pe.NonNegativeReals)

    def cost_rule(model):

        return sum(model.x[i] for i in model.components)

    model.cost = pe.Objective(rule=cost_rule, sense=pe.minimize)
    

    return model

def main():

    #optsolver = opt_utils.create_solver()

    model = create_model()

    instance = model.create_instance('example.dat')

    instance.pprint()
    #optsolver.solve(instance)


    names = []
    for i in (instance.components - instance.components.last()):
        names.append("x_" + i)

    print(names)    
    #instance.input_ML =pe.Set(initialize=(instance.pinco | (instance.components - instance.components.last())))
    for i in names:
        instance.input_ML.add(i)

    instance.W1_ML = pe.Param(instance.input_ML,
                           mutable=True,default=0.1)

        
    print("------------------\n\n")

    instance.pprint()

   
    
    for i in instance.input_ML:
        print(i, " ", instance.W1_ML[i].value)

    
    #objective = opt_utils.get_objective_value(instance)
    #print("Optimal solution found with value ", objective)

if __name__ == '__main__':

    main()


