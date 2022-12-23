# Issue 6117: graph plotting with show ignores keyword 'talk'

Issue created by migration from https://trac.sagemath.org/ticket/6117

Original creator: ekirkman

Original creation time: 2009-05-21 22:13:58

Assignee: ekirkman

CC:  rlm

Bug pointed out by Fidel Barrera-Cruz.  Entering


```
g = graphs.PetersenGraph()
g.show(talk=True)
```


results in 

```
TypeError: show() got an unexpected keyword argument 'talk'
```



---

Attachment


---

Comment by mabshoff created at 2009-05-22 13:36:50

I don't like the deletion/dotting out of the doctest in `sage/graphs/graph.py`. Is that really needed?

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-22 13:45:00

Resolution: fixed


---

Comment by mabshoff created at 2009-05-22 13:45:00

Merged in Sage 4.0.rc1 since it fixes a real bug, but if my comment above could be addressed I wouldn't be too sad ;)

Cheers,

Michael
