

input=open("Input.txt","r")
lines=input.readlines()
print(len(lines))
#get rid of /n

x=0
y=0

treecounter=0
notreecounter=0
for line in lines:
      if lines[x][y] == '#':
         treecounter+=1
      else:
         notreecounter+=1
      y=(y+3) % (len(lines[0])-1)
   #31 is len. modulo working.
      x=(x+1) % (len(lines))
   #use modulo operator to get a circle in x & y

print(treecounter)
print(notreecounter)

#answer is 230

print(230*104*83)
