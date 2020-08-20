mainBoard = ( "      |       |      \n"
              "  1   |   2   |  3   \n"
              "------|-------|------\n"
              "  4   |   5   |  6   \n"
              "------|-------|------\n"
              "  7   |   8   |  9   \n"
              "      |       |       ")
displayBoard = ( "      |       |      \n"
                 "  o   |   x   |  3   \n"
                 "------|-------|------\n"
                 "  o   |   x   |  6   \n"
                 "------|-------|------\n"
                 "  x   |   x   |  9   \n"
                 "      |       |       ")
print(mainBoard)
a=list(mainBoard)
b=list(displayBoard)
z=[]

for i in range(len(a)):
    if a[i].isdigit() == True:
        z.append(i)

print(z)

if displayBoard[z[0]]==displayBoard[z[3]]==displayBoard[z[6]]:
    print('Yes')
elif displayBoard[z[0]]==displayBoard[z[1]]==displayBoard[z[2]]:
    print('Yes')
elif displayBoard[z[0]]==displayBoard[z[4]]==displayBoard[z[5]]:
    print('Yes')
elif displayBoard[z[1]]==displayBoard[z[4]]==displayBoard[z[7]]:
    print('Yes')
elif displayBoard[z[1]]==displayBoard[z[4]]==displayBoard[z[7]]:
    print('Yes')
elif displayBoard[z[2]]==displayBoard[z[5]]==displayBoard[z[8]]:
    print('Yes')
elif displayBoard[z[1]]==displayBoard[z[4]]==displayBoard[z[7]]:
    print('Yes')
elif displayBoard[z[2]]==displayBoard[z[4]]==displayBoard[z[6]]:
    print('Yes')
elif displayBoard[z[3]]==displayBoard[z[4]]==displayBoard[z[5]]:
    print('Yes')
elif displayBoard[z[6]]==displayBoard[z[7]]==displayBoard[z[8]]:
    print('Yes')