# Issue 7702: Handle interrupts better in the notebook

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2009-12-16 03:17:24

Assignee: was

Interrupting the notebook is less robust than it used to be.  The attached worksheet is an example where the notebook fails to interrupt.  When this happens, the notebook acts as though it's interrupted.


---

Attachment


---

Comment by was created at 2009-12-16 03:18:59

I have verified this.    It is a *very* bad bug, since it means that one thinks the notebook got interrupted, but it didn't.  This results in a seemingly totally broken worksheet, which must cause massive confusion to everybody, to say the least.


---

Comment by was created at 2009-12-16 03:19:23

(Oh, and it is surely my fault since I rewrote the interrupt code in the notebook separation.)


---

Comment by timdumol created at 2010-01-18 06:55:52

The patch at #5712 should fix the problem.


---

Comment by jdemeyer created at 2011-01-26 14:19:05

Hard to say what's going on here.  My guess would be a bare `except:` somewhere catching the `KeyboardInterrupt`.


---

Comment by jdemeyer created at 2011-05-07 11:26:22

Resolution: duplicate


---

Comment by jdemeyer created at 2011-05-07 11:26:22

I cannot reproduce the problem anymore in recent versions of Sage, so I assume it got fixed by #9678.
