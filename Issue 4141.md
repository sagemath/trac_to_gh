# Issue 4141: OS X: R pulls in libraries from fink

Issue created by migration from https://trac.sagemath.org/ticket/4141

Original creator: dphilp

Original creation time: 2008-09-18 00:39:25

Assignee: mabshoff

CC:  georgsweber was

When building sage 3.1.2 without hiding fink,

```
sage-3.1.2/local/lib/R/library/tcltk/libs/tcltk.so links to non-whitelisted file /sw/lib/libtcl8.4.dylib
sage-3.1.2/local/lib/R/library/tcltk/libs/tcltk.so links to non-whitelisted file /sw/lib/libtk8.4.dylib
```



---

Comment by kcrisman created at 2010-05-26 20:28:15

Since we now automatically make Sage barf when /sw is in PATH, is this ticket invalid?  I no longer have that in my PATH, so I can't test this - someone else?


---

Comment by kcrisman created at 2011-04-26 02:50:19

Yeah, we can close this.  I put it back in my PATH (in fact, the very files listed here are available in my /sw folder!) and got

```
***************************************************
***************************************************
Found Fink in  /sw/bin//fink

*********************************************************

Found either MacPorts or Fink in your PATH, which potentially wrecks the Sage build process.
You should make sure MacPorts and Fink cannot be found.  Either:
(1) rename /opt/local and /sw, or
(2) change PATH and DYLD_LIBRARY_PATH
(Once Sage is built, you can restore them.)

*********************************************************

make[1]: *** [installed/prereq-0.8] Error 1

real	0m5.581s
user	0m1.715s
sys	0m1.913s
Error building Sage.
make: *** [build] Error 1
new-host-2:sage-4.7.alpha5-Finktest 
```

So I highly doubt this is possible any more.    We haven't gotten a single report of this other than this one in 3 years.  

Also, the sage-check-libraries.py script that found this on #4140 seems to not work any more!  

Anyway, this should be closed.


---

Comment by kcrisman created at 2011-04-26 02:50:19

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-04-26 02:50:31

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-04-26 03:01:19

> Also, the sage-check-libraries.py script that found this on #4140 seems to not work any more!  

In the meantime I found #4127, which talks about how to correctly use it.  Sadly, the file itself doesn't tell this (e.g., source sage-env first!).


---

Comment by jdemeyer created at 2011-04-26 09:08:36

Resolution: worksforme
