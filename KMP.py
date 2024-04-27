pattern=input("Enter the Pattern ")
lp=len(pattern)
pi = []
pi= [0 for i in range(lp)]
j=1
i=0
flag=0
if lp==1:
    pi[0]=0
while j<lp:
    if pattern[i]==pattern[j]:
        pi[j]=i+1
        i=i+1
    else:
        pi[j]=0
        i=0
    j=j+1
print("pi=",pi)
q=-1
file = open('file.txt', 'r')
text=file.read()
for i in range(0,len(text)):
    if q>0 and pattern[(q+1)]!=text[i]:
        q=pi[q]
        print("while q=",q)
    if pattern[q+1]==text[i]:
        q=q+1
        print("same q=",q)
    if q==lp-1:
        flag=1
        print("Pattern has occured at",i-lp+2)
        q=pi[q]

if flag==0:
    print("No pattern found")
