t=(123,56)
print(t.count(123))
print(t.index(56))

#set
s={1,2,6,8,8,8,9}#1,7,9
s1={2,6,8,8,89,1,9}
#s.add(7)
print(s)
print(s1.difference(s))
print(s)
#s.difference_update(s1)
#print(s)
#s.discard(8)
print(s)
print(s.intersection(s1))
print(s.isdisjoint(s1))

print(s.issubset(s1))
print(s.issuperset(s1))
print(s.pop())
s.remove(6)
print(s)
print(s.symmetric_difference(s1))
print(s.union(s1))
s.update(s1)
print(s)

#dictionary
d={1:"jan",2:"rith",3:"dee"}
print(d)
#d.clear()
print(d)
print(d.get(2))
print(d.items())
print(d.keys())
#print(d.pop(2))
print(d)
#d.popitem()
print(d)
d.update({2:"abc"})
print(d)

s={"sanjay","jana","dharani"}
k="s1"
n=dict.fromkeys(k,s)
print(n)


