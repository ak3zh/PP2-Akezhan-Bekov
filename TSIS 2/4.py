thistuple = ("apple", "banana", "cherry")
print(thistuple)


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


fruits = ("apple", "banana", "cherry")


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
