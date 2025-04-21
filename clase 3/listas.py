# Introduccion a lista

array = ["futbol", "Pc", 18.6, 18, [6, 7, 10.4], True, False]
print(array)
print(array[1])
print(array[4])
print(array[-1])
print(array[0:3])
print(array[:2])
print(array[2:])

print(len(array))

array.append(66)
print(array)

array.insert(1, 88)
print(array)

array.extend([1, 88, True, 100])
print(array)




array1 = ["futbol", "Pc", 18.6, 18, [6, 7, 10.4], True, False, "Pc"]
array2 = [200, 250, "hola"]
array3 = array1 + array2
print(array3)


print("Pc" in array1)


print(array1.index("Pc"))

print(array1.count("Pc"))


array1.remove("Pc")
print(array1)


print(array1)

array1.reverse()
print(array1)

array4 = [1, 2, 8, -11, 5]
array4.sort()
print(array4)

array4.sort(reverse=True)
print(array4)