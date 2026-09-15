''''''
desserts = [" cake", " cookies", " ice cream", " Chocolate", "candy", " brownies"]
print(desserts)
desserts.append(" cake")
print(desserts)
desserts.insert(1, " chocolate")
print(desserts)

del desserts[2]
print(desserts)
desserts.pop()
print(desserts)

desserts.remove("candy")
print(desserts)
print(sorted(desserts))
print(desserts)
desserts.reverse()

print(desserts)
print(len(desserts))
desserts.sort()
print(desserts)

desserts.sort(reverse=True)
print(desserts)