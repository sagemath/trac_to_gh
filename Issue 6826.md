# Issue 6826: [with patch, needs review] magma_free interface is broken

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-08-26 01:16:34

Assignee: was

CC:  was

Keywords: magma free internet interface

The magma free interface has changed slightly.  The attached patch updates the interface.


---

Attachment


---

Comment by mhansen created at 2009-09-01 22:40:57

It looks like it is still "input" rather than "commands" when looking at the source for http://magma.maths.usyd.edu.au/calc/.


---

Comment by ncalexan created at 2009-09-02 16:49:42

Replying to [comment:1 mhansen]:
> It looks like it is still "input" rather than "commands" when looking at the source for http://magma.maths.usyd.edu.au/calc/.

Yep, it did to me too.  All I know is that it didn't work before the patch, and it now works with the patch.  That's the important part -- is that the same for you?


---

Comment by mhansen created at 2009-09-02 19:41:17

It works both before and after for me.  Maybe the test input that I'm using is too simple.


---

Comment by robertwb created at 2009-09-22 22:37:59

It's id="input" name="commands". 

It still works for me too, but this should probably be fixed for consistencies sake.


---

Comment by mvngu created at 2009-09-24 06:18:21

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:54:11

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
