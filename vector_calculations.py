vec_a = [2,3,4,5]
vec_b = [3,4,5,6]

def elementwise_multiplication(vec_a, vec_b):
    mult = vec_a[0] * vec_b[0]
    return mult
mult = elementwise_multiplication(vec_a, vec_b)
print('multiplication: ', mult)

def elementwise_addition(vec_a, vec_b):
    add = vec_a[0] + vec_b[0]
    return add
add = elementwise_addition(vec_a, vec_b)
print("Addition: ", add)

def vector_sum(vec_a):
    sum= 0
    for i in range(len(vec_a)):
        sum += int((len, vec_a[i]))
        return sum
sum = vector_sum(vec_a)
print('sum: ', sum)

