

input=open("Input.txt","r")
lines=input.readlines()
#get rid of /n

x=0
y=0

treecounter=0
notreecounter=0
for line in lines:
   y=(y+3) % (len(lines[0])-1)
   #31 is len. modulo working. 
   x=(x+1) % (len(lines))
   #use modulo operator to get a circle in x & y

   if lines[x][y] == '#':
      treecounter+=1
   else:
      notreecounter+=1
      
   
print(treecounter)
print(notreecounter)

#answer is 230

103
83
98
98
print(103*83*98*98)
