# Issue 4519: [with patch, needs review] problem with build code

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-11-14 06:26:15

Assignee: craigcitro

There's a problem with the build code that was first introduced by #4377. Here's an example of how to see this: pick your favorite `.pyx` file (I was using `gen.pyx`), and break it -- just make some syntax error, and save. Now do a `sage -br` -- you see that it says there's an error ... but then it still runs sage! Oops.

The underlying problem is that if we pass back a different exit code (in the case I was running into, it was 256), the `python setup.py install` still returns 0. 

The attached patch fixes the trouble. Is there a way to test something like this?


---

Attachment


---

Comment by GeorgSWeber created at 2008-11-14 20:54:41

Hmmm,

it seems to me that somewhere I have read that only the lowest 8 bit of "such" return values would be taken into account. I don't remember a reference however, or in what precise context --- bash? posix? ...

But that "256" suddenly becomes "0" would support this faint memory of mine.

Be it as it be, I just tested (with 3.2.rc0) that this patch does indeed fix the problem described (which is there without the patch); and the nature of the patch is local enough one can be pretty sure that nothing else does break.

Positive review from my side.

The only thing I don't agree with is the original classification as "blocker" --- nothing really bad happens, because the old "gen.so" or "gen.dylib" or whatever compiled python extension from the last successful run is still there, and accessed by the wrongly started Sage session. And the error message is displayed prominently enough.


---

Comment by GeorgSWeber created at 2008-11-14 20:54:41

Changing priority from blocker to major.


---

Comment by mabshoff created at 2008-11-14 20:59:25

This is definitely a blocker plain and simple since one does not check any large compilation, i.e. a `-ba` for errors. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-14 20:59:25

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-11-15 05:03:00

Merged in Sage 3.2.rc1


---

Comment by mabshoff created at 2008-11-15 05:03:00

Resolution: fixed
