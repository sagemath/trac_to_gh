# Issue 1263: change pari C library error handler (instead of overriding exit() with abort())

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-25 06:39:30

Assignee: was

CC:  jdemeyer

This is from Anton Mellit, and basically explains how to do what we
want, maybe. 


```
By the way I put my sources on sourceforge (http://pari-
python.cvs.sourceforge.net/pari-python/pari-python/)
The error handlers are in errors.cpp and errors.h
I use slightly modified version of the pari exception handling which
is implemented using setjmp/longjmp and you use it like this:
CATCH(CATCH_ALL) {
   // if error occures
} TRY {
   // do something
} ENDCATCH
I made similar macros, but I catch exceptions not when they arise in
PARI, but after PARI prints error message and calls
default_exception_handler, which I set as follows:
default_exception_handler = exception_handler,
where exception_handler simply should return 0 if there is a handler
installed. And the actual handler must be installed in GP_DATA->env
using setjmp(GP_DATA->env) (don't forget to store the old handler
somewhere and put it back afterwards)

I've recently worked on it so that it catches SIGINT (Ctrl-C).

First I turned off PARI's own signal handling. Instead of pari_init I
use this:

pari_init_opts(64000000, 500000, INIT_DFTm);

Then I install my own signal handler which simply raises pari
exception. I install the handler at the first CATCH and uninstall it
and return the Python's one on the last ENDCATCH.
- Show quoted text -
```



---

Comment by was created at 2007-11-25 06:39:40

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2010-08-01 15:37:22

It is totally not clear to me what this is all about.  In Sage-4.5.2 the PARI error handling works (a bit ugly, but it works).

I would mark it "duplicate/invalid/wontfix".


---

Comment by jdemeyer created at 2010-09-16 07:43:12

Changing status from new to needs_review.


---

Comment by mariah created at 2011-05-16 18:09:39

Changing status from needs_review to positive_review.


---

Comment by mariah created at 2011-05-16 18:09:39

If this is a sage-duplicate/invalid/wontfix, then I believe that this ticket can be closed.


---

Comment by jdemeyer created at 2011-05-17 15:51:18

Resolution: invalid
