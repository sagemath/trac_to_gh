# Issue 2729: [with patch] tiny jmol spheres have holes

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-03-30 00:01:21

Assignee: was

CC:  jason

For example, try 


```
sum([sphere((1+r,2,3), r/10, color='red') for r in [1..10]]).show(aspect_ratio=[1,1,1])
```


See http://www.mail-archive.com/jmol-users`@`lists.sourceforge.net/msg07676.html (thanks to jason for this tip)


---

Comment by jason created at 2008-03-30 00:29:45

positive review pending the deletion of the print statement.


---

Attachment

OK, print statement is gone.


---

Comment by jason created at 2008-03-30 00:45:26

looks good.


---

Comment by mabshoff created at 2008-03-31 13:47:06

Merged in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-03-31 13:47:06

Resolution: fixed
