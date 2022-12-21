# Issue 717: sage -t timeout stuff works poorly

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-20 20:07:28

Assignee: failure

Issues:
  1. I can't actually find anywhere in sage-doctest right now where the two alarm codes are actually used, so SAGE should never timeout.  Weird.
  2. It should be easy for users to adjust the timeout, e.g., on slow systems.
  3. "sage --long" should automatically have a much longer timeout.


---

Comment by mabshoff created at 2007-12-04 14:17:27

This has annoyed me on regular occasions, so let's fix this.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 04:31:22

The third part of the ticket, i.e. 'sage --long" should automatically have a much longer timeout' is  now now #2029.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-05 05:20:54

FYI, but this is probably orthogonal to the doctesting and more has to do with signal delivery.

Cheers,

Michael


---

Attachment

This code enables timeouts.


---

Comment by gfurnish created at 2008-12-05 06:24:56

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-12-05 06:24:56

Changing assignee from failure to gfurnish.


---

Comment by mabshoff created at 2008-12-05 06:33:47

Patch looks with one tiny exception:

```
[10:25pm] mab|ds9: one suggestions: raise the sleep period to 1 second: time.sleep(.1)
[10:25pm] gfurnish: feel free to make the modification
[10:25pm] mab|ds9: I think we can live with that.
[10:25pm] mab|ds9: mk
```

I will move item (2) to its own ticket since it is not addressed here.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-05 07:38:35

This works very nicely. Positive review. 

(2) has been moved to #4712.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-05 07:38:52

Merged in Sage 3.2.2.alpha0


---

Comment by mabshoff created at 2008-12-05 07:38:52

Resolution: fixed
