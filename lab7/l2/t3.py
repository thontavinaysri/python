#25341a05l1 vinay

def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

total, average = total_marks(80, 75, 90)
print("Total =", total)
print("Average =", average)

total, average = total_marks(80, 75, 90, 85, 95)
print("Total =", total)
print("Average =", average)

total, average = total_marks(88)
print("Total =", total)
print("Average =", average)

'''output :
Total = 245
Average = 81.66666666666667
Total = 430
Average = 86.0
Total = 88
Average = 88.0
'''