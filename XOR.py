#AND GATE
#first we me a line eqn that seperates our inputs to 2 areas 
#ture area from AND that comes from input [1,1] and 
#false area for the last
def NAND(inputs):
    #line parameters
    #w1x1+w2x2+b => as be is interception of y axis
    w1=1
    w2=1
    b=-2
    output_arr=[]
    for i in inputs:
        combination = w1 * i[0] + w2 * i[1] + b
        #here we negated the condition from >=0 to <0 to get NAND gate
        output = int(combination < 0)
        #we append the result of the linear combination to get an array than would be 
        #input for pur XOR
        output_arr.append(output)
    return output_arr 
#OR GATE
def OR(inputs):
    w1=1.5
    w2=1.5
    b=-1
    output_arr=[]
    for i in inputs:
        combination = w1 * i[0] + w2 * i[1] + b
        output = int(combination >= 0)
        output_arr.append(output)
    return output_arr   
#XOR GATE
import numpy as np
def XOR(inp):
    #we make a col stack of outputs from NAND and OR above
    '''
    inputs matrix = [[1 0]
                     [1 1]
                     [1 1]
                     [0 1]]
    '''
    inputs=np.column_stack(( NAND(inp),OR(inp) ))
    #to construct a line that classify the 2 pairs inside as true
    #others to be false
    w1=.9
    w2=.9
    b=-1
    output_arr=[]
    for i in inputs:
        combination = w1 * i[0] + w2 * i[1] + b
        output = int(combination >= 0)
        output_arr.append(output)
    return output_arr    
i = [(0, 0), (0, 1), (1, 0), (1, 1)]
print(XOR(i))    
#here we got the XOR Gate!
#output => [0, 1, 1, 0]
    
    
    
    