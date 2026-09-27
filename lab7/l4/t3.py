#25341a05l1 vinay

students = [("Ravi", 78), ("Sita", 92), ("Amit", 65)]

sorted_students = sorted(students, key=lambda s: s[1], reverse=True)

print("Students sorted by marks:")
for student in sorted_students:
    print(student)

words = ["Python", "Java", "C", "Programming"]

sorted_words = sorted(words, key=lambda x: len(x))

print("Words sorted by length:")
for word in sorted_words:
    print(word)

'''output :
Students sorted by marks:
('Sita', 92)
('Ravi', 78)
('Amit', 65)

Words sorted by length:
C
Java
Python
Programming
'''