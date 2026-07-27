#25341a05l1 vinay
# taking number of rows
rows = int(input("Enter rows: "))

# outer loop
for i in range(1, rows + 1):

    # checking condition
    if i > 0:

        # inner loop
        for j in range(i):
            print("*", end="")

    print()

    ''' output 
    Enter rows: 5
*
**
***
****
*****
'''