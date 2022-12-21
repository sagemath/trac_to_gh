# Issue 3626: Graph.set_boundary only takes lists

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-07-09 18:49:36

Assignee: boothby

CC:  rlm


```
sage: G = Graph("George")
sage: G.set_boundary(set([1,2,3]))
sage: G.get_boundary()
[]
```


... which makes sense, given the code...


```
    def set_boundary(self, boundary):
        ...
        if isinstance(boundary,list):
            self._boundary = boundary

    def set_embedding(self, embedding):
        ...
```




---

Attachment


---

Comment by rlm created at 2008-07-12 16:51:26

+1


---

Comment by mabshoff created at 2008-07-16 00:42:12

Resolution: fixed


---

Comment by mabshoff created at 2008-07-16 00:42:12

Merged in Sage 3.0.6.alpha0
