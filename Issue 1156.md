# Issue 1156: Functions lost in massive combinatorics reorganization?

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-11-12 20:41:15

Assignee: mhansen

CC:  sage-combinat

See changeset "Initial commit of combinat/ files and bug fixes." from Mike Hansen. 

Some functions lost. bernoulli_polynomial among them. 


---

Attachment


---

Comment by mabshoff created at 2007-11-19 21:07:28


```
[21:57] <mabshoff> Is there any more to #1156 or is that patch all that is missing?
[21:59] <mhansen> I went through a diff with the old version and those three things 
were the only ones I found missing.
```



---

Comment by mabshoff created at 2007-11-19 21:16:32

Resolution: fixed


---

Comment by mabshoff created at 2007-11-19 21:16:32

Merged in 2.8.13.alpha1.

After feedback from Mike Hansen closed.

Cheers,

Michael
