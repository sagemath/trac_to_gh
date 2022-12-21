# Issue 3188: add 64 bit OSX build support to mpfi

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-13 14:20:00

Assignee: mabshoff

spkg coming up

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-13 14:20:05

Changing status from new to assigned.


---

Attachment

An updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha1/mpfi-1.3.4-cvs20071125.p7.spkg

Cheers,

Michael


---

Comment by was created at 2008-05-19 04:22:10

Positive review -- pending asking Jason Martin about his mysterious:

```
# Added by Jason Martin, to avoid conflict with global libraries.  
CFLAGS="-Z "$CFLAGS
```



---

Comment by mabshoff created at 2008-05-19 04:33:07

Resolution: fixed


---

Comment by mabshoff created at 2008-05-19 04:33:07

Merged in Sage 3.0.2.alpha1
