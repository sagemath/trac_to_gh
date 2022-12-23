# Issue 5313: patch singular so that when it runs out of memory the error message says "singular" in it

Issue created by migration from https://trac.sagemath.org/ticket/5313

Original creator: was

Original creation time: 2009-02-19 19:18:47

Assignee: malb

CC:  leif

When looking at #3760 it took a long long time to see that this had anything whatever to do with singular.  To speed this up, we should patch two files in Singular so that instead of getting


```
error: no more memory
System 5120k:5120k Appl 4638k/481k Malloc 4095k/0k Valloc 1024k/480k Pages 153/103 Regions 2:2

halt 14
```

as an error, one gets


```
SINGULAR error: no more memory
System 5120k:5120k Appl 4638k/481k Malloc 4095k/0k Valloc 1024k/480k Pages 153/103 Regions 2:2
...
and then an exception is raised!
```



---

Comment by was created at 2010-01-18 01:36:31

Changing type from defect to enhancement.


---

Comment by was created at 2010-01-18 01:36:31

This is really an enhancement, not a bug.


---

Comment by was created at 2010-07-14 13:47:51

I'm wrong, this is a *BUG*, since Sage should not exit on memory overflow, but should instead raise an exception. 
Here's a new example to illustrate the problem:

```

sage: n=500
sage: R = PolynomialRing(QQ,n,names='x')
sage: f = sum(R.gens())
sage: g = f*f

error: no more memory
System 212048k:212048k Appl 164440k/2763k Malloc 156k/0k Valloc 167048k/2763k Pages 41762/0 Regions 360:360

halt 14
wstein@sage:~/build/sage-4.4.4/spkg/standard$   
```


I should not be dumped to the command prompt!


---

Comment by was created at 2010-07-14 20:08:40

More complete log on sage.math:

```

wstein@sage:~/build/sage-4.4.4$ ulimit -v 1000000
wstein@sage:~/build/sage-4.4.4$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: n = 1000
sage: R = PolynomialRing(QQ,n,names='x')
sage: f = sum(R.gens())
sage: g = f*f
error: no more memory
System 212080k:212080k Appl 168836k/2090k Malloc 211k/0k Valloc 170716k/2090k Pages 42679/0 Regions 388:388
halt 14
wstein@sage:~/build/sage-4.4.4$ 
| Sage Version 4.4.4.1, Release Date: 2010-06-28                     |
| Type notebook() for the GUI, and license() for information.        |
```



---

Comment by was created at 2010-07-14 20:44:08

I submitted this upstream to Hans Schoenemann


---

Attachment

NOTE to future self:

To work on singular:

  1. sage -f -m singular-x.y.z.spkg
  2. cd spkg/build/singular-x.y.z
  3. Make changes
  4. Type `make install-libsingular`


---

Comment by was created at 2010-07-14 21:05:31

To get rid of the "exit of out sage" issue hackishly:

   1. Modify src/kernel/mminit.cc and put abort() right after the first fprintf in the function void omSingOutOfMemoryFunc().

   2. Edit the file devel/sage/sage/libs/singular/polynomial.pyx  by adding _sig_on/_sig_off around `ret[0] = pp_Mult_qq(p, q, r)` in the function singular_polynomial_mul. 

Then we have:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: n = 1000
sage: sage: R = PolynomialRing(QQ,n,names='x')
sage: sage: f = sum(R.gens())
sage: sage: g = f*f
| Sage Version 4.4.4.1, Release Date: 2010-06-28                     |
| Type notebook() for the GUI, and license() for information.        |
2 - Singular error: no more memory
calling abort
sage: 
```


Note that strangely there is no traceback.  But at least one gets the sage prompt back.

Regarding speed:

WITH the _sig_on/_sig_off stuff:

```

sage: R.<x,y,z> = PolynomialRing(QQ)
sage: f = (x+y+z)^2
sage: timeit('f*(f+1)')
625 loops, best of 3: 12.6 µs per loop
sage: f = (x+y+z)
sage: timeit('f*(f+1)')
625 loops, best of 3: 11.4 µs per loop
sage: f = (x+y+z)^10+1
sage: timeit('f*(f+1)')
625 loops, best of 3: 168 µs per loop
sage: timeit('x*x')
625 loops, best of 3: 410 ns per loop
```

and without it:


```
sage: sage: R.<x,y,z> = PolynomialRing(QQ)
sage: sage: f = (x+y+z)^2
sage:  timeit('f*(f+1)')
625 loops, best of 3: 12.4 µs per loop
sage: sage: f = (x+y+z)
sage: sage: timeit('f*(f+1)')
625 loops, best of 3: 11.2 µs per loop
sage: sage: f = (x+y+z)^10+1
sage: sage: timeit('f*(f+1)')
625 loops, best of 3: 167 µs per loop
sage: timeit('x*x')
625 loops, best of 3: 290 ns per loop
```


This is all on sage.math.


---

Attachment

This makes it so errors during arithmetic can be handled.   This won't do anything though unless the singular library is patched to call abort() before exit, as explained in a comment on this ticket.


---

Attachment

this is a patch to the singular spkg.  It patches a patch file.


---

Comment by was created at 2010-07-14 21:37:22

Changing status from new to needs_review.


---

Comment by malb created at 2010-08-12 13:27:09

This patch http://trac.sagemath.org/sage_trac/attachment/ticket/5313/Singular_error.patch is already included in #8059.


---

Comment by kcrisman created at 2011-06-23 03:36:20

These examples all work for me, no memory issue reported, even.

Anyway, Martin or someone, can you confirm this, put your name as reviewer, and set to positive review (possibly cc:ing jdemeyer)?  Then this can be closed, assuming the previous comment is true.


---

Comment by kcrisman created at 2012-07-05 14:57:29

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-07-05 14:57:29

Okay, I can confirm that the equivalent of [attachment:Singular_error.patch] is in the Singular in Sage, but that nothing like [attachment:singular-spkg_add_abort.patch] is in the current Singular - `abort()` is not called, and can confirm that William's example with the ulimit still fails to raise an exception, although it does now say Singular in the error.  Sorry for not reading more carefully before.

Further, the patch [attachment:trac_5313-sigon_sigoff.patch] to Sage no longer applies.

```
patching file sage/libs/singular/polynomial.pyx
Hunk #4 FAILED at 266
Hunk #5 FAILED at 336
2 out of 5 hunks FAILED -- saving rejects to file sage/libs/singular/polynomial.pyx.rej
abort: patch failed to apply
```


Finally, should we submit a pull request or issue [upstream](https://github.com/Singular/Sources) for the abort issue, or is that truly too hackish to ask them to do?  Putting none of the above for upstream since one thing was completely incorporated while the other they apparently don't even know about.
