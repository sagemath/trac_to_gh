# Issue 5452: Graph broken on a input of type dict of dicts

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2009-03-07 17:15:45

Assignee: slabbe

In sage-3.2.3 the code below was fine, but it is broken in sage-3.3 and sage-3.4.rc0 :


```
sage: a,b,c,d,e,f=sorted(SymmetricGroup(3))
sage: Graph({b:{d:'c',e:'p'}, c:{d:'p',e:'c'}})

...

/sage/graphs/graph.pyc in __init__(self, data, pos, loops, format, boundary, weighted, implementation, sparse, vertex_labels, **kwds)
   8261                     if v not in verts: verts.append(v)
   8262                     if hash(u) > hash(v):
-> 8263                         if u in data[v]:
   8264                             if data[u][v] != data[v][u]:
   8265                                 raise ValueError("Dict does not agree on edge (%s,%s)"%(u,v))

KeyError: (1,2,3)
```






---

Comment by slabbe created at 2009-03-07 17:17:44

Against sage-3.4.rc0


---

Comment by slabbe created at 2009-03-07 17:18:36

Changing status from new to assigned.


---

Attachment


---

Comment by slabbe created at 2009-03-07 17:27:03

Must apply trac_5452.patch first.


---

Attachment

Haven't tried testing since I'm about to get on a plane, but this patch looks straightforward enough to me.

+1


---

Comment by mabshoff created at 2009-03-20 20:23:31

Merged both patches in Sage 3.4.1.alpha0. Doctests do pass.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-20 20:23:31

Resolution: fixed
