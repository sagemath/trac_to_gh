# Issue 1276: incorporate willem's doctest timing code into sage

Issue created by migration from https://trac.sagemath.org/ticket/1276

Original creator: was

Original creation time: 2007-11-26 04:18:09

Assignee: failure

CC:  wjp


```
> Send me your doctest timing code :-)  I'm looking forward to playing with it.

Here you go. It's a patch to local/bin/sage-doctest and a file timing.py
that I had put in sage/misc .

It adds a --time option to sage-doctest that makes it append the timings
it generates as a dict indexed by hash to the (cpickled) file
.doctest/timings.sobj .  There's no infrastructure yet to automatically
delete that file when appropriate, though.

I also attached two very basic scripts that show or compare the contents
of timings.sobj files.
```



---

Attachment


---

Comment by was created at 2007-11-26 04:19:12

Changing assignee from failure to was.


---

Comment by mabshoff created at 2007-12-29 17:46:00

This ought to get merged.

Cheers,

Michael


---

Comment by ncalexan created at 2008-01-20 03:38:00

Changing assignee from was to ncalexan.


---

Comment by ncalexan created at 2008-01-20 03:38:00

This code looks good, and I'm working in this area so I'll update it and ready it for merging.


---

Comment by mabshoff created at 2008-04-18 20:28:48

Changing priority from major to blocker.


---

Attachment

rebased & fixed devel repo patch for this.


---

Comment by gfurnish created at 2008-05-24 22:42:54

rebased & fixed scripts repo patch for this.


---

Attachment


---

Comment by gfurnish created at 2008-05-24 22:45:05

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-05-24 22:45:05

Changing assignee from ncalexan to gfurnish.


---

Comment by craigcitro created at 2008-06-15 21:28:59

Changing keywords from "" to "editor_mabshoff".


---

Comment by ncalexan created at 2008-08-12 01:11:02

I think that ticket #3476 does the actual "write time info to file" better than this patch, but the viewing scripts here are useful and should be kept.

I suggest basing this ticket on #3476.


---

Comment by mabshoff created at 2008-09-06 23:14:26

Resolution: wontfix


---

Comment by mabshoff created at 2008-09-06 23:14:26

This superseded by #3476, so let's close this. 

Cheers,

Michael
