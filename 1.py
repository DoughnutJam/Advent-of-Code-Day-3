

input=open("Input.txt","r")
lines=input.readlines()
#get rid of /n
print (lines[0][3])

x=0
y=0

treecounter=0
notreecounter=0
for line in lines:
   y=+3 % (len(lines[0])-1)
   #31 is len. modulo working. 
   x=+1
   #use modulo operator to get a loop in y
   if lines[x][y] == '#':
      treecounter=+1
   else:
      notreecounter=+ 1
      
print(treecounter)
print(notreecounter)

