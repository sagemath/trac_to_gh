# Issue 5622: complex double fast callable interpreter

Issue created by migration from https://trac.sagemath.org/ticket/5622

Original creator: robertwb

Original creation time: 2009-03-28 10:02:35

Assignee: somebody

CC:  cwitty

After RDF and RR, CDF would be very handy to have too. 


---

Comment by robertwb created at 2009-03-28 10:05:43

I started thinking about this as I was refereeing the original ticket, trying to make sure I understood how it all worked.


---

Attachment

Code looks good, doctests pass.  Positive review, unless Michael complains about the portability issues.

Michael, I see two potential portability issues with the code:

1) it uses C99 complex numbers

2) it adds the compiler argument -std=c99

I'm guessing the latter will only work with gcc (unless other compilers specifically copy gcc command-line arguments).  Does Sage currently build with non-gcc compilers?


---

Comment by mabshoff created at 2009-03-28 17:09:52

Replying to [comment:2 cwitty]:
> Code looks good, doctests pass.  Positive review, unless Michael complains about the portability issues.
> 
> Michael, I see two potential portability issues with the code:
> 
> 1) it uses C99 complex numbers

That is not a problem. FLINT mandates that we use C99 anyway.

> 2) it adds the compiler argument -std=c99

We can work around that.

> I'm guessing the latter will only work with gcc (unless other compilers specifically copy gcc command-line arguments).  Does Sage currently build with non-gcc compilers?

Not at the moment, but there is work under way to support the pathscale compiler for SiCortex. 

Cheers,

Michael


---

Comment by robertwb created at 2009-03-28 18:46:04

Thanks. 

BTW, It compiles fine with gcc without the c99 flag, but I figured I'd put it there to be explicit. (I actually only knew about that flag because of flint.)


---

Comment by mabshoff created at 2009-03-31 06:18:46

Resolution: fixed


---

Comment by mabshoff created at 2009-03-31 06:18:46

Merged in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by jason created at 2009-04-11 11:36:08

The work around for the bug in Cython < 0.11 can be removed because we upgraded to Cython 0.11 in this release of Sage, right?

from patch above:

```
# This is to work around a header ordering bug in Cython < 0.11 
# (Pari is included from sage.rings.complex_double.) 
```

