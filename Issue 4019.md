# Issue 4019: [with patch, needs review] numerator and denominator for QQ[x]

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-08-31 09:01:46

Assignee: tbd

QQ[x] should have a numerator and denominator method. 


---

Attachment


---

Comment by AlexGhitza created at 2008-08-31 12:27:02

The code looks fine.  However, I'm getting a doctest failure in finite_field_ntl_gf2e.pyx:


```
File "/opt/sage/tmp/finite_field_ntl_gf2e.py", line 1018:
    sage: e == f
Expected:
    True
Got:
    False
```


I can't tell where this is coming from.


---

Comment by mabshoff created at 2008-09-01 01:27:27

I am changing the subject to "needs work" so that the various report will pick up this ticket.

Cheers,

Michael


---

Comment by robertwb created at 2008-09-01 21:10:51

I have been unable to reproduce this error, are you sure it's from this patch?


---

Comment by mabshoff created at 2008-09-01 21:49:27

Replying to [comment:4 robertwb]:
> I have been unable to reproduce this error, are you sure it's from this patch? 

Robert, Alex,

applying this patch only to my merge tree does not result in any doctest failure, so I am giving this a positive review. Hopefully this will not bit us in the ass down the road ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-01 21:49:42

Resolution: fixed


---

Comment by mabshoff created at 2008-09-01 21:49:42

Merged in Sage 3.1.2.alpha4
