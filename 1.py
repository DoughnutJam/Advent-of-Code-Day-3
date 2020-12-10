

input=open("Input.txt","r")
lines=input.readlines()
#get rid of /n
print (lines[1][2])


x=0
y=0

treecounter=0

for line in lines:
   x=+1
   y=+3 % (len(lines[0])-1)
   #use modulo operator to get a loop in y
   if lines[x][y] == '#':
      treecounter=+1

print(treecounter)
