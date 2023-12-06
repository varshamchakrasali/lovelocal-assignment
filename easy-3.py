#Given an integer numRows, return the first numRows of Pascal's triangle.In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

def pascalsTriangle(numRows):

    #creating a list which will represent the final Pascal's Triangle
    result = []

    for i in range(numRows):
        #creating ith row consisting of row number of elements, and initializing the row elements with 1
        row = [1] * (i+1)

        for j in range(1,i):
            row[j] = result[i-1][j-1] + result[i-1][j]
        result.append(row)
    return result

rows = int(input("Enter the number of rows: "))                
ptriangle = pascalsTriangle(rows)
for row in ptriangle:
    print(row)


