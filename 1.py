

input=open("Input.txt","r")
lines=input.readlines()

print (lines[1][2])


x=0
y=0

treecounter=0

for line in lines:
   x=+1
   y=+3
   if lines[x][y] == '#':
      treecounter=+1
   else:
      ""
    
print(treecounter)
