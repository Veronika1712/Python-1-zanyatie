x=543
y=130
z=130
k1=x//z
k2=y//z
d=k1*k2
k=((x+y)-z*(k1+k2))/(2**0.5)
if k>z:
    d+=1
print(d) 
