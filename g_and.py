def activastion_(actvation_function_name,weight:list,x1:list,x2:list):
    '''AND, OR, XOR, NOT, NAND, NOR and XNOR.'''
    # w1= False if weight1<1 else True
    # w2= False if weight2<1 else True

    # if actvation_function_name=='AND':
    #     return w1 and w2
    
    
    # if actvation_function_name=='OR':
    #     return w1 or w2
    
    # if actvation_function_name=='XOR':
    #     return w1  != w2
    
    # if actvation_function_name=='XNOR':
    #     return w1 == w2
    
    
    # if actvation_function_name=='NAND':
    #     return not (w1 and w2)
    
    # if actvation_function_name=='NOR':
    #  return not(w1 or w2)
    

    # w1=1
    # w2=1
    
    y = weight[0] * x1 + weight[1] * x2
    if actvation_function_name=='AND':
        return False if  max(y) else True
        return False if y < 1 else True
    
    
    if actvation_function_name=='OR':
        return False if min(y)==0 else True
    
    # if actvation_function_name=='XOR':
    #     return w1  != w2
    
    # if actvation_function_name=='XNOR':
    #     return w1 == w2
    
    
    # if actvation_function_name=='NAND':
    #     return not (w1 and w2)
    
    # if actvation_function_name=='NOR':
    #  return not(w1 or w2)
    
def NOT_gate(weight):
    return not False if weight<1 else True

print(activastion_('AND',1,1))

print(activastion_('OR',-1,-1))
print(activastion_('XOR',1,-1))