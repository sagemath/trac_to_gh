# Issue 5503: "cmp" method failing on objects in the pickle jar

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2009-03-12 20:23:26

Assignee: cwitty

CC:  jakobkroeker

Keywords: universal comparison, transitivity, coercion

The following piece of code loads the pickle jar and tries to compare each pair of members. In my 3.4, it currently segfaults.

If sage is to have universal comparison, these comparisons should all occur without error. The next step would be to ensure that results are consistent with transitivity.


```
L=[]
M=[]
#change this location to point to your own pickle jar
path="/usr/local/sage/default/tmp/pickle_jar-3.4"

for n in sorted(os.listdir(path)):
  if n.endswith(".sobj") and not(n in M):
    print n
    L.append(load(path+"/"+n))

for i in [1..len(L)-1]:
    for j in range(i):
        try:
            _=cmp(L[i],L[j])
        except:
            print [i,j]
```



---

Comment by jdemeyer created at 2017-03-08 13:19:48

Duplicate of #16311.


---

Comment by jdemeyer created at 2017-03-08 13:19:48

Resolution: duplicate
