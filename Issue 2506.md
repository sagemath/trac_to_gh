# Issue 2506: Problem with inequality operator (!=) in graph.py

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2008-03-13 16:56:38

Assignee: rlm


```
sage: g = Graph()
sage: g2 = g.copy()
sage: g == g   # fine
True
sage: g != g   # fine
False
sage: g2 == g  # PROBLEM: either this one
True
sage: g2 != g  # or this one should be false
True
```



---

Comment by rlm created at 2008-03-14 00:45:00

I think this may be a subtlety having to do with Python comparison (although I'm tempted to call it a bug, maybe "subtlety" is more P.C.). The funny thing is if you define the method

```
def __ne__(self, other):
    return (not (self == other))
```

you get the correct behavior. Before making a patch, it might be good to figure out why this is the case...


---

Comment by rlm created at 2008-03-14 00:46:01

The correct behavior is the following:

```
sage: g = Graph()
sage: g2 = g.copy()
sage: g == g
True
sage: g != g
False
sage: g2 == g
True
sage: g2 != g
False
sage: g is g
True
sage: g2 is g
False
```



---

Comment by rlm created at 2008-03-14 13:39:29

Aparently, to have proper behavior, we do have to implement the `__ne__` method:

http://www.voidspace.org.uk/python/articles/comparison.shtml


---

Attachment


---

Comment by mabshoff created at 2008-03-14 14:15:14

Patch looks good to me and fixes the bug.


---

Comment by mabshoff created at 2008-03-14 14:16:29

Merged in Sage 2.10.4.alpha0


---

Comment by mabshoff created at 2008-03-14 14:16:29

Resolution: fixed
