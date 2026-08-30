#25341a05l1 vinay
set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}

print("Set 1:", set1)
print("Set 2:", set2)

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference (Set 1 - Set 2):", set1.difference(set2))

# Symmetric Difference
print("Symmetric Difference:", set1.symmetric_difference(set2))

'''output 
Set 1: {50, 20, 40, 10, 30}
Set 2: {80, 50, 70, 40, 60}
Union: {70, 40, 10, 80, 50, 20, 60, 30}
Intersection: {40, 50}
Difference (Set 1 - Set 2): {10, 20, 30}
Symmetric Difference: {80, 20, 70, 10, 60, 30}
'''