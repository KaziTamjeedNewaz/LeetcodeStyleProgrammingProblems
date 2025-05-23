print ("Enter number of rows: ")
m=int(input())
print ("Enter number of Columns: ")
n=int(input())
matrix=[[0]*n for i in range(m)]
matrixVisited=[[False]*n for i in range(m)]
for row in range(m):
    for column in range(n):
        print("Input Element (", row, "," , column, "): " )
        matrix[row][column]=input()
print("Input Matrix")
for row in matrix:
    print(row)
if ((m==1) and (n==1)):
    result=[matrix[0][0]]
    print("Spiral traversal of this matrix\n", result)
    exit  
elif (m==1):
    result=matrix[0]
    print("Spiral traversal of this matrix\n", result)
    exit
index=matrix[0][0]
indexRow=0
indexColumn=0
startingRowPosition=0
startingColumnPosition=0
#nowhereToGoFlag=False #just in case the logic is wrong anywhere, defensive programming, just change the subsequent while loop condition to True if removed
result=[]
while (True):#used to be while(not nowhereToGoFlag): 
    for column in range (startingColumnPosition, n):
        #print("firstLoop")
        indexColumn=column
        #if not matrixVisited[indexRow][indexColumn]: #if using this line, indent everything below one tab
        #print("firstLoopIf")
        index=matrix[indexRow][indexColumn]
        matrixVisited[indexRow][indexColumn]=True
        result.append(index)
        #else:
            #print("firstLoopElse")
            #nowhereToGoFlag=True
            #break
    startingRowPosition+=1
    if matrixVisited[indexRow+1][indexColumn]:
        #nowhereToGoFlag=True
        break
    for row in range (startingRowPosition, m):
        #print("secondLoop")
        indexRow+=1
        #if not matrixVisited[indexRow][indexColumn]: #if using this line, indent everything below one tab
        #print("secondLoopIf")
        index=matrix[indexRow][indexColumn]
        matrixVisited[indexRow][indexColumn]=True
        result.append(index)
        #else:
            #print("secondLoopElse")
            #nowhereToGoFlag=True
            #break
    n-=1
    if matrixVisited[indexRow][indexColumn-1]:
        nowhereToGoFlag=True
        break

    for column in reversed(range(startingColumnPosition,n)):
        #print("thirdLoop")
        indexColumn=column
        #if not matrixVisited[indexRow][indexColumn]: #if using this line, indent everything below one tab
        #print("thirdLoopIf")
        index=matrix[indexRow][indexColumn]
        matrixVisited[indexRow][indexColumn]=True
        result.append(index)
        #else:
            #print("thirdLoopElse")
            #nowhereToGoFlag=True
            #break
    m-=1
    if matrixVisited[indexRow-1][indexColumn]:
        nowhereToGoFlag=True
        break

    for row in reversed(range (startingRowPosition,m)):
        #print("fourthLoop")
        indexRow-=1
        #if not matrixVisited[indexRow][indexColumn]:
        #print("fourthLoopIf")
        index=matrix[indexRow][indexColumn]
        matrixVisited[indexRow][indexColumn]=True
        result.append(index)
        #else:
            #print("fourthLoopElse")
            #nowhereToGoFlag=True
            #break
    startingColumnPosition+=1
    if matrixVisited[indexRow][indexColumn+1]:
        nowhereToGoFlag=True
        break


print("Spiral traversal of this matrix\n",result)