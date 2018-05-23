a=lambda c,d:c*d
print(a(2,7))
b=lambda x,y:x/y
print(b(12,6))
l=[(lambda x,y : x**y),(lambda u,h : u+h),(lambda c,d : c-d)]
print(l[0](8,2),l[1](20,80),l[2](10,40))
print(l[1](20,80))
print(l[2](10,40))
