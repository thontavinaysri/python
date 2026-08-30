#25341a05l1 vinay
set1 = {10, 20, 30, 40, 50}
set2 = {20, 30, 40}

print("Set 1:", set1)
print("Set 2:", set2)

print("Is Set 2 a subset of Set 1?", set2.issubset(set1))

print("Is Set 1 a superset of Set 2?", set1.issuperset(set2))

'''output
Set 1: {50, 20, 40, 10, 30}
Set 2: {40, 20, 30}
Is Set 2 a subset of Set 1? True
Is Set 1 a superset of Set 2? True
'''