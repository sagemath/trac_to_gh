# Issue 1403: mwrank: crash upon exit

Issue created by migration from https://trac.sagemath.org/ticket/1403

Original creator: mabshoff

Original creation time: 2007-12-05 11:42:07

Assignee: was

Justin Walker reported:

```
'mwrank' doesn't like it if you just exit (by typing "^D" or, more or  
less equivalently, by "ending a file").

Thus, if you run 'mwrank' and give it a file containing, for example,  
"[0,0,1,-1,0]" and nothing else, it will barf at the end.  If your  
file contains "[0,0,0,0,0]", the program sweetly closes up shop (when  
it reads this) and quits.

The error I get is
   bad ZZ input
   Abort trap

Anyone know why this doesn't show up in the test logs?  Is it worth  
tracking down?

The issue is that the terminating condition for input processing in  
'getcurve()' is a "null curve" (""[0,0,0,0,0]""), rather than EOF.  
An EOF is an error condition, hence the abort(). 
```


See also #1402.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-05 19:00:58

John Cremona wrote:

```
i.e. mwrank crashed rather than stopping cleanly when reachinf EOF on
input.  Should be an easy fix to qrank/getcurve.cc, so I'll do it.
```


Cheers,

Michael


---

Comment by cremona created at 2007-12-05 20:22:13

patch for file qrank/getcurve.cc which fixes the problem


---

Attachment

I have fixed this.  Patch attached.  JEC


---

Comment by cremona created at 2007-12-05 20:23:15

Resolution: fixed


---

Comment by mabshoff created at 2007-12-05 21:13:52

Resolution changed from fixed to 


---

Comment by mabshoff created at 2007-12-05 21:13:52

Hello John,

the release manager usually closes the ticket once the patch has been applied into the current release tree. That way we do not lose fixes.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-05 21:13:52

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-12-06 02:02:55

Merged in 2.9.alpha0.


---

Comment by mabshoff created at 2007-12-06 02:04:17

Resolution: fixed


---

Comment by mabshoff created at 2007-12-06 02:04:17

Merged in 2.9.alpha0.


---

Comment by cremona created at 2007-12-06 09:06:57

Resolution changed from fixed to 


---

Comment by cremona created at 2007-12-06 09:06:57

Changing status from closed to reopened.


---

Attachment

Second patch file reader.h.patch to be applied to qcurves/reader.h will stop the same happening for other binaries (e.g. tate, conductor etc) built in the qcurves directory.


---

Comment by mabshoff created at 2007-12-06 13:13:22

Second patch merged in 2.9.alpha1.


---

Comment by mabshoff created at 2007-12-06 13:13:22

Resolution: fixed
