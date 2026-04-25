# Identity operator (is and is not)
x = ["Barca","Real"]
y = ["Barca","Real"]
z = x

print("x is z: ", x is z) # is check both are same objects or not.
print("x is z: ", x == z) # == check same value or not.

print("x is y: ", x is y) #False, because not same object although same values.
print("x is y: ", x == y) #true, because same value.

print("x is y: ", x is not y) #True, because both are not same objects.
print("x is y: ", x != y) #False, because same value.


m1 = ~45
print(m1)

a = 8
b = 5
print (a & b)
print(a | b)
print(a ^ b)


y = 10 << 2
print("Left shift:", y) # Binary 10: 1010 and add two 00 right side.

x = 10 >> 2
print("Right shift:", x)