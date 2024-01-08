def activation_function(gate_type, weight, x1, x2):
    if gate_type == 'AND':
        return False if weight[0]*x1 + weight[1]*x2 < 1 else True
    elif gate_type == 'OR':
        return False if weight[0]*x1 + weight[1]*x2 <= 0 else True
    elif gate_type == 'XOR':
        return False if weight[0]*x1 + weight[1]*x2 == 0 else True
    elif gate_type == 'NAND':
        return not (False if weight[0]*x1 + weight[1]*x2 < 1 else True)
    elif gate_type == 'NOR':
        return not (False if weight[0]*x1 + weight[1]*x2 <= 0 else True)
    elif gate_type == 'ZOR':
        return False if weight[0]*x1 + weight[1]*x2 != 0 else True
    else:
        print("Wrong gate type given")
    
print(activation_function('AND', [1, 1], 1, 1))
# print(activation_function('AND', [0, 1], 1, 1))
print(activation_function('OR', [-1, -1], -1, -1))
print(activation_function('XOR', [1, -1], 1, -1))
print(activation_function('NAND', [1, 1], 1, 1))
print(activation_function('NOR', [-1, -1], -1, -1))
print(activation_function('ZOR', [1, -1], 1, -1))