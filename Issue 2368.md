# Issue 2368: Compiling Atlas on Powerbook G4, Tuning Information

Issue created by migration from https://trac.sagemath.org/ticket/2368

Original creator: rishi

Original creation time: 2008-03-02 15:49:12

Assignee: mabshoff

Compiling Atlas takes forever on Powerbook G4 running debian lenny. Please make the tuning information a part of sage distribution.


---

Comment by mabshoff created at 2008-03-02 15:57:26

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-15 23:27:23

I did fix the detection on the last G4 iBook build by Apple. I also created tuning info that will be integrated into the upcoming ATLAS 3.8.1.spkg (see #2269).

The G4 tuning info can be found at

http://sage.math.washington.edu/home/mabshoff/ATLAS-tune/PPCG432.tgz

Cheers,

Michael


---

Attachment

I will also post this patch to the ATLAS tracker to get it merged upstream


---

Comment by mabshoff created at 2008-03-20 10:56:47

Resolution: fixed


---

Comment by mabshoff created at 2008-03-20 10:56:47

Merged in Sage 2.11.alpha0 via #2260.
