# Issue 71: Secret transation of .sage to .py causes confusion

Issue created by migration from Trac.

Original creator: Justin Walker (justin@mac.com)

Original creation time: 2006-09-20 21:40:01

Assignee: somebody

When a .sage file is "load"ed or "attach"ed, it gets translated to a .py file before being processed; the result is a file with different structure than the original.  Any errors are described in terms of the .py file, not the .sage file.  I realize this is a kind of Catch-22, but is there a way to (as the C preprocessor does) keep the .sage line numbers?

Of course this requires that Python have that ability, because it reports the errors.

I suppose the proper solution, given this, is to document the issue.

I think this points up an aspect of a fundamental issue: SAGE is a programming language/system; SAGE is a computer system for mathematicians to use.  I'm not sure how good it can be at both.


---

Comment by was created at 2006-09-21 01:27:39

SAGE can embed the original line numbers in the .py file, and even the original
.sage lines (before parsing) in the .sage file.  Then the error messages will
also list the original line number (and line, if you want) in a comment at the end
of the line.   In the notebook, at least, it would be easy to postparse the error
messages so they refer to the original .sage file.


---

Comment by was created at 2007-01-13 02:15:01

Changing type from defect to enhancement.


---

Comment by was created at 2007-01-13 02:15:01

This is not a bug.


---

Comment by davidloeffler created at 2009-06-07 13:16:26

Changing component from basic arithmetic to misc.


---

Comment by davidloeffler created at 2009-06-07 13:16:26

Changing assignee from somebody to cwitty.


---

Comment by kcrisman created at 2013-01-29 20:21:25

Hi.  This is a REALLY old ticket.  Is the documentation at [the programming tutorial](http://www.sagemath.org/doc/tutorial/programming.html) now sufficient, or should we still keep this ticket around?  I love the idea in William's (six-year-old) comment:1, so we could repurpose this ticket to implement this if desired.  Or, one could just improve the documentation a little to mention that errors refer to lines in the .py file.


---

Comment by git created at 2014-11-20 16:50:59

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2014-11-20 20:59:59

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2014-11-20 22:17:42

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2014-11-21 06:21:36

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2014-11-23 10:55:33

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:
