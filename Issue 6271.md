# Issue 6271: upgrade to mpir-1.3.0

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-12 18:49:57

Assignee: tbd

CC:  craigcitro

packages are on sage.math, Craig knows where.


---

Comment by craigcitro created at 2009-06-14 08:50:00

This looks good, with the same caveat that we need to remember to remove the `spkg-check` before we release. (Is there an obvious reason there isn't just a flag for these we set somewhere in the sage build process?)


---

Comment by was created at 2009-06-14 09:46:42

> (Is there an obvious reason there isn't just a flag for these we set somewhere in the sage build process?) 

There is such a flag.  It's SAGE_CHECK.  See http://trac.sagemath.org/sage_trac/ticket/6282.  It's just not documented, so nobody seems to know about it.


---

Comment by craigcitro created at 2009-06-14 22:31:18

Resolution: fixed
