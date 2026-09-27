#25341a05l1 vinay

grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks = [85, 35, 72, 28, 40, 55]

for mark in marks:
    print(mark, ":", grade(mark))

'''output :
85 : Pass
35 : Fail
72 : Pass
28 : Fail
40 : Pass
55 : Pass
'''