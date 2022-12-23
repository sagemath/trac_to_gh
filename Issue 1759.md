# Issue 1759: Various files still mention GPL V2 [only]

Issue created by migration from https://trac.sagemath.org/ticket/1759

Original creator: mabshoff

Original creation time: 2008-01-11 19:54:35

Assignee: was

The following files mention/are under GPL V2 implying V2 only:

 * c_lib/src/mpn_pylong.c: License: GPL v2
 * c_lib/src/mpz_pylong.c: License: GPL v2
 * sage/misc/banner.py

This ought to be fixed before 2.10 since we will merge GPL V3 or later packages. IIRC all the copyright holders agreed to GPL V2 or later, but we should be careful with this and double check.

Cheers,

Michael


---

Comment by was created at 2008-01-11 20:12:28

Gonzalo Tornaria whose copyright is at the top of those files *definitely* agreed to GPL "V2 or later".  So we're good.

William


---

Comment by mabshoff created at 2008-01-15 04:08:51

See toward the end of

https://groups.google.com/group/sage-devel/browse_thread/thread/2fac21e76cbcbfa3/21068f934515e4e9

for Gonzalo's statements.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-01-15 04:19:43

I have applied the patch to Sage 2.10.alpha3 due to the following statement from the last post in the thread linked above:

```
> Wait, are you saying that you would not allow your code to be re-licensed
> "GPL v2 or later" for Sage?   Or, are you just saying you don't like it,
> but you would do it.

At this time I'm just saying that I don't like it. 
```


I have also send an email to Gonzalo asking for explicit confirmation - but I do not think that the above line could be misinterpreted to mean anything but an agreement to relicense under "GPL v2 or later". 

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-15 04:19:43

Resolution: fixed


---

Comment by tornaria created at 2008-01-15 05:13:01

For the record, I agree to the relicensing under "GPL v2 or later". Please apply the patch suggested by mabshoff on my behalf.
