# Issue 6034: [with spkg, needs review] update Singular to newest upstream release

Issue created by migration from https://trac.sagemath.org/ticket/6034

Original creator: malb

Original creation time: 2009-05-13 03:00:37

Assignee: malb

CC:  craigcitro

Keywords: singular

Singular 3.1 has many new features which are pretty exciting for Sage (computation over base *rings*, yay!). So we should upgrade.


---

Comment by malb created at 2009-05-13 03:00:57

fixes doctest fallout


---

Attachment

The SPKG can be found here:

   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-2-20090512.spkg

It does not contain the changed LIB location. It basically is a drop-in replacement for the current Singular spkg.


---

Attachment

I've updated sage-env and the spkg to move the `*.lib` files out of the way to `$SAGE_LOCAL/share/singular`.


---

Comment by malb created at 2009-05-17 01:02:48

Note that I updated the SPKG at 

    http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-2-20090512.spkg

to include the fixes for enabling the coefficient rings which are not fields.


---

Comment by malb created at 2009-05-17 01:11:01

The attached patch enables the Singular coefficient rings natively. It passes doctests except:


```
The following tests failed:

        sage -t  devel/sage/sage/rings/polynomial/toy_d_basis.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1049.8 seconds
```


which I reported upstream at 

  http://www.singular.uni-kl.de:8002/trac/ticket/137


---

Comment by malb created at 2009-05-17 01:13:02

Ignore that comment, wrong ticket.


---

Comment by was created at 2009-05-28 07:11:41

This will be a perfect addition for sage-4.0.1.


---

Comment by kedlaya created at 2009-05-30 22:25:30

Could you change singular_env.patch so that it knows where to find sage-env (i.e., in (sage directory)/local/bin)?

Thanks,
Kiran


---

Comment by malb created at 2009-05-31 13:42:22

I am not quite sure what you're asking since singular_env.patch is a HG patch which should be applied via 


```
cd $SAGE_LOCAL/bin
hg import ~/singular_env.patch 
```



---

Comment by kedlaya created at 2009-06-02 16:37:39

That works, yes. I had been trying to run hg from within sage.

With that, the patches apply against 4.0, the spkg builds, and the patch on #6051 applies and does what is expected (with the one known doctest failure caused by upstream). I didn't find any collateral doctest failures either. Positive review; however, in order to get #6051 to pass doctests, we'll need a new version from upstream and hence a new spkg.


---

Comment by malb created at 2009-06-07 12:06:56

Changing type from defect to enhancement.


---

Comment by SimonKing created at 2009-06-08 14:20:04

Sorry, but something is wrong.

I get

```
sage: import os
sage: os.environ['SINGULARPATH']
'/home/king/SAGE/devel/sage-4.0/local/share/singular'
sage: singular.eval('system("SingularLib")')
'/home/king/SAGE/devel/sage-4.0/local/share/singular:/home/king/SAGE/devel/sage-4.0/local/LIB'
```


But the last line is Singular's way of telling where the libs are.


---

Comment by malb created at 2009-06-08 14:26:52

Hi Simon,

why is the last result wrong? It searches in `/home/king/SAGE/devel/sage-4.0/local/share/singular` first, which looks correct to me. What am I missing?


---

Comment by SimonKing created at 2009-06-08 14:31:12

Replying to [comment:13 malb]:
> Hi Simon,
> 
> why is the last result wrong? It searches in `/home/king/SAGE/devel/sage-4.0/local/share/singular` first, which looks correct to me. What am I missing?

Double sorry. I was missing something. Ithought that ``system("SingularLib")`` gives precisely one location in which Singular is looking for libraries. But, as you point out, it may provide multiple search paths.

OK, then back to Kiran's positive review.


---

Comment by ncalexan created at 2009-06-10 05:16:24

This segfaults on startup for me with sage-4.0.1.  I thought the patch at #6051 might help, but it doesn't apply against 4.0.1.  We want to merge this in 4.0.2 so quick movement is appreciated.


---

Comment by SimonKing created at 2009-06-10 06:10:11

Replying to [comment:15 ncalexan]:
> This segfaults on startup for me with sage-4.0.1.  I thought the patch at #6051 might help, but it doesn't apply against 4.0.1.  We want to merge this in 4.0.2 so quick movement is appreciated.

What did you do in order to install the spkg?

You should do:
 1. Either replace the singular-3-0-4 spkg by the new spkg and re-build Sage _from scratch_
 2. Or do the following:
      i. ``sage -i singular-3-1-0...`` (so, install it into an existing sage)
      ii. ``sage -f ntl...`` (so, force a re-installation of the ntl-spkg)
      iii. 
        * Do ``sage -ba``, or 
        * touch all Cython extensions depending on Singular (these are sage.libs.singular.singular, sage.matrix.matrix_mpolynomial_dense, sage.rings.polynomial.multi_polynomial_ideal_libsingular and sage.rings.polynomial.multi_polynomial_libsingular) and do ``sage -b``

This is how I installed the new spkg.

Cheers,
    Simon


---

Comment by ncalexan created at 2009-06-10 07:48:37

> This is how I installed the new spkg.

Thanks Simon, it now builds and runs and I'll get to testing it tomorrow.


---

Comment by ncalexan created at 2009-06-10 17:35:58

Replying to [comment:17 ncalexan]:
> > This is how I installed the new spkg.
> 
> Thanks Simon, it now builds and runs and I'll get to testing it tomorrow.

Just for my own reference:


```
touch sage/libs/singular/* sage/matrix/matrix_mpolynomial_dense* sage/rings/polynomial/multi_polynomial_ideal_libsingular* sage/rings/polynomial/multi_polynomial_libsingular*
```



---

Comment by craigcitro created at 2009-06-10 17:50:22

Replying to [comment:18 ncalexan]:
> Just for my own reference:
> 
> {{{
> touch sage/libs/singular/* sage/matrix/matrix_mpolynomial_dense* sage/rings/polynomial/multi_polynomial_ideal_libsingular* sage/rings/polynomial/multi_polynomial_libsingular*
> }}}

Should we add something involving these dependencies to `module_list.py`?


---

Comment by malb created at 2009-06-10 17:59:26

Replying to [comment:19 craigcitro]:
> Should we add something involving these dependencies to `module_list.py`?

Yes. The right dependencies would be `$SAGE_LOCAL/include/libsingular.h`, strange I thought I did that a while ago.


---

Comment by SimonKing created at 2009-06-11 06:19:01

Replying to [comment:20 malb]:
> Replying to [comment:19 craigcitro]:
> > Should we add something involving these dependencies to `module_list.py`?
> 
> Yes. The right dependencies would be `$SAGE_LOCAL/include/libsingular.h`, strange I thought I did that a while ago.

Aren't these dependencies already in `module_list.py`? Actually this is where I was looking what I had to touch. Or perhaps touching `libsingular.h` would have been enough, who knows...


---

Comment by malb created at 2009-06-11 11:32:42

Indeed the dependencies are already in, Nick must have forgotten to `sage -b` ?


---

Comment by ncalexan created at 2009-06-12 07:43:44

Resolution: fixed
