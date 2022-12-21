# Issue 3790: limit gets stuck without computing anything

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-08-07 22:07:41

Assignee: gfurnish


```
 I noticed that for some expressions limit() gets stuck and does not
return to the sage prompt.  It does not seem to be computing anything
since the cpu usage is 0.
 For example in Sage 3.0.6 try:
vars('Ax,Bx,By')
t = -Ax*sin(sqrt(Ax^2)/2)/(sqrt(Ax^2)*sqrt(By^2 + Bx^2))
t.limit(Ax=0,dir='above')

 It just sits there.  And you need to ctrl-c to get the prompt back.
If you set t = -Ax*sin(sqrt(Ax^2)/2)/(sqrt(Ax^2)*sqrt(By^2))
Then do t.limit(Ax=0,dir='above'), you get a message asking if By is
zero or nonzero.

```



---

Attachment


---

Comment by mabshoff created at 2008-08-08 02:25:48

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-08 23:43:07

Resolution: fixed


---

Comment by mabshoff created at 2008-08-08 23:43:07

Merged in Sage 3.1.alpha1
