# Issue 750: permutation group element (dict method, acting on lists)

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-09-24 23:13:58

Assignee: was

CC:  sage-combinat

It would be nice to get permutation elements as dictionaries as well as lists.  If g is a permutation group element, then something like


```
  sage: g.dict()
{1:2, 2:1}
```


It would also be nice if we could have permutation elements act on lists to switch the order according to the permutation.


```
  sage: g.action(range(3))
[0,2,1]
```


Are these things possible already?



---

Attachment

Added a patch to implement something similar to the second.  With this patch, one may do the following:


```
sage: G = SymmetricGroup(4)
sage: g = G((1,2,3,4))
sage: sage: g('abcd')
'bcda'
sage: sage: g([0,1,2,3])
[1, 2, 3, 0]
sage: sage: g(('foo','bar','baz','what'))
('bar', 'baz', 'what', 'foo')
```


However, I can see absolutely no reason for one to want a dict rather than a list.  Do you have an example of where this might be useful?


---

Comment by boothby created at 2007-10-31 18:02:30

Robert Miller convinced me that there are good reasons to want a dict, so I implemented this, too.


---

Comment by boothby created at 2007-10-31 18:02:30

Changing assignee from was to boothby.


---

Comment by boothby created at 2007-10-31 18:02:30

Changing status from new to assigned.


---

Attachment

Includes .dict() code.


---

Comment by boothby created at 2007-11-01 18:32:24

fixes bugs from previous edition / ready for 2.8.11


---

Attachment


---

Comment by mabshoff created at 2007-11-02 03:19:07

Resolution: fixed
