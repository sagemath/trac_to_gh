# Issue 3855: point3d size default is too small to see

Issue created by migration from https://trac.sagemath.org/ticket/3855

Original creator: rlm

Original creation time: 2008-08-14 19:31:44

Assignee: was


```
point3d((0,0,0))
```

versus

```
point3d((0,0,0), size=10)
```


Easy to fix...


---

Comment by anakha created at 2008-09-21 19:47:09

Changing assignee from was to anakha.


---

Attachment

Yes, easy.


---

Comment by anakha created at 2008-09-21 19:47:19

Changing status from new to assigned.


---

Comment by aginiewicz created at 2008-09-21 22:56:20

5 looks good - so it's easy positive review


---

Comment by mabshoff created at 2008-09-23 00:35:31

Merged in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-23 00:35:31

Resolution: fixed
