#25341a05l1 vinay

from functools import reduce

employees = [
    {"name": "Vinay", "department": "CSE", "salary": 40000},
    {"name": "Rahul", "department": "ECE", "salary": 35000},
    {"name": "Sita", "department": "CSE", "salary": 45000},
    {"name": "Amit", "department": "EEE", "salary": 30000},
    {"name": "Priya", "department": "CSE", "salary": 50000}
]

department = "CSE"

selected = filter(lambda emp: emp["department"] == department, employees)

hiked = map(
    lambda emp: {
        "name": emp["name"],
        "department": emp["department"],
        "salary": emp["salary"] * 1.10
    },
    selected
)

hiked_employees = list(hiked)

total_salary = reduce(
    lambda total, emp: total + emp["salary"],
    hiked_employees,
    0
)

print("Employees after 10% hike:")
for emp in hiked_employees:
    print(emp)

print("Total salary expenditure =", total_salary)

'''output :
Employees after 10% hike:
{'name': 'Vinay', 'department': 'CSE', 'salary': 44000.00000000001}
{'name': 'Sita', 'department': 'CSE', 'salary': 49500.00000000001}
{'name': 'Priya', 'department': 'CSE', 'salary': 55000.00000000001}
Total salary expenditure = 148500.00000000003
'''