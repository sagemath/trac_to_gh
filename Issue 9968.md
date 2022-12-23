# Issue 9968: Update extension code for mpmath-0.16

Issue created by migration from https://trac.sagemath.org/ticket/9969

Original creator: fredrik.johansson

Original creation time: 2010-09-22 13:16:04

Assignee: tbd

The patch adds fast Cython version of some more mpmath functions to sage.libs.mpmath.

This should wait to be merged until mpmath 0.16 gets released (I will do this soon). Right now, it can be tested with an svn trunk checkout of mpmath.

It can be tested with:

```
sage: import mpmath
sage: mpmath.runtests()
sage: mpmath.doctests()
```



---

Attachment

updated mpmath Cython extension code


---

Comment by fredrik.johansson created at 2010-10-30 21:42:49

Here is an spkg: http://sage.math.washington.edu/home/fredrik/mpmath-0.16.spkg

It should work fine together with the patch. Sorry for the very long delay!


---

Comment by fredrik.johansson created at 2010-10-30 21:42:49

Changing status from new to needs_review.


---

Comment by was created at 2010-11-02 22:23:40

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-11-02 22:23:40

REPORT:

* All tests passon sage.math.

*  Your code needs "::\n\n" before any sage sessions for sphinx to format it right.
See the template here and note rightafterwords: http://sagemath.blogspot.com/
right now if somebody introspects one of your functions in the notebook, sphinx will butcher it.

* You define "isqrt" but sage integers already have an isqrt method that is exactly the same.  Clarify in the documentation the distinction.

Bug me again by email or chat when you've posted another patch (or patch on top of the above) that fixes the above two little things.


---

Comment by was created at 2010-11-02 22:25:02

Oh, could you have at least a short comment explaining what every single function does.  E.g.,

```
cdef cy_exp_basecase(mpz_t y, mpz_t x, int prec):
     # <what this function does>
```



---

Attachment


---

Comment by fredrik.johansson created at 2010-11-19 15:01:26

Added second patch with docstring fixes.


---

Comment by fredrik.johansson created at 2010-11-19 15:01:26

Remove assignee tbd.


---

Comment by fredrik.johansson created at 2010-11-19 15:01:51

Changing status from needs_work to needs_review.


---

Comment by fbissey created at 2011-01-27 08:51:18

If I understand correctly you need to apply 14600.patch first, then docstring-fixes.patch?
This goes in sage-on-gentoo tonight for testing.


---

Comment by fbissey created at 2011-01-27 08:55:09

I forgot, for it to go in sage proper a new spkg will be needed. Are you working on that?


---

Comment by fredrik.johansson created at 2011-01-27 09:40:56

Yes, the patches should be applied in that order.

The spkg was linked in a post above: http://sage.math.washington.edu/home/fredrik/mpmath-0.16.spkg


---

Comment by fbissey created at 2011-01-27 10:04:39

I should get a reader since I am obviously blind :)
I say we try to get it formally in 4.7, I rewrite the
description a little bit.


---

Comment by fbissey created at 2011-02-01 22:18:15

I just saw your post about mpmath-0.17 release, are you planing to update this ticket
for mpmath 0.17?


---

Comment by fredrik.johansson created at 2011-02-01 22:22:20

Yes, I'll create an spkg for 0.17 immediately to replace the 0.16 one.

Nothing should have changed in the way of Sage compatibility, so the patches should still be fine.


---

Comment by fredrik.johansson created at 2011-02-01 22:31:11

By the way, I noticed (too late) that there are two failing doctests if you run mpmath.doctests() as per the instructions. These failures a trivial (output formatting) and can be ignored.


---

Comment by fbissey created at 2011-02-01 22:33:24

Replying to [comment:11 fredrik.johansson]:
> Yes, I'll create an spkg for 0.17 immediately to replace the 0.16 one.
> 
> Nothing should have changed in the way of Sage compatibility, so the patches should still be fine.

Good to know, that means I won't have to change anything to support mpmath-0.17 in sage-on-gentoo when 4.6.2 is released.


---

Comment by fredrik.johansson created at 2011-02-17 10:15:29

Fixed patch that should apply in sage-4.6.1


---

Attachment

Patch that fixes some mpmath test failures due to use of the truediv operator


---

Attachment


---

Comment by fbissey created at 2011-02-18 08:45:03

The two new patches together are smaller than the two previous patches. Is docstring-fixes.patch really not needed anymore?


---

Comment by fredrik.johansson created at 2011-02-18 08:51:15

Most of docstring-fixes.patch consisted of reformatting existing docstrings, and there's a lot of air in the diff format, so I think the numbers add up.


---

Comment by fbissey created at 2011-02-18 09:03:06

Replying to [comment:17 fredrik.johansson]:
> Most of docstring-fixes.patch consisted of reformatting existing docstrings, and there's a lot of air in the diff format, so I think the numbers add up.

I thought it could be the case. I will try to review this quickly so we can have it included in 4.7.alpha.


---

Comment by fbissey created at 2011-02-18 10:35:11

tests are not looking good to me.

```
Python 2.6.6 (r266:84292, Jan 28 2011, 01:59:55) 
[GCC 4.5.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import mpmath
>>> mpmath.runtests()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib64/python2.6/site-packages/mpmath/__init__.py", line 413, in runtests
    from .tests import runtests as tests
ImportError: No module named tests
```

I get pretty much the same thing from sage. 

By the way that looks more like a procedure to do a spkg-check than a doctest.


---

Comment by fredrik.johansson created at 2011-02-18 10:42:51

Hmm... it doesn't seem like mpmath installed correctly for you.

Is "/usr/lib64/python2.6/site-packages" actually the location of your Sage site-packages library, or is this a standalone installation of mpmath 0.17?


---

Comment by fbissey created at 2011-02-19 08:21:10

sorry for the noise I shouldn't post past 11pm. There is an issue in Gentoo and sage-on-gentoo but there shouldn't be any in a pure sage environment. It may take a little bit of time testing this on various hardware.


---

Comment by fbissey created at 2011-02-19 09:17:15

Something I have noticed in the gentoo ebuild. There is now an option to use matplotlib. Since matplotlib is shipped in sage mpmath may have to depend on it or configured not to use it.

Usually people choose the first option in this case, unless there is major trouble. If you want to do that, the deps file in spkg/standard will need to be updated.


---

Comment by fbissey created at 2011-02-21 08:46:49

I got a number of failing mpmath.doctests on my x86 box. A formatting issue really. Does any of the code interacts with ecl or maxima? The install I tested it on is based on 4.6.2.alpha4 with ecl-11.1.1 (#10766) and maxima-5.23.2 (#10773) and a couple of other patch that should be orthogonal (ppl #10039 and associated patches).

```
almosteq 0.004
findroot **********************************************************************
File "/home/francois/Work/sandbox/sage-4.6.2.alpha4/local/lib/python2.6/site-packages/mpmath/calculus/optimization.py", line 835, in NoName
Failed example:
    findroot(f, -10, solver='anewton', verbose=True)
Expected:
    x:     -9.88888888888888888889
    error: 0.111111111111111111111
    converging slowly
    x:     -9.77890011223344556678
    error: 0.10998877665544332211
    converging slowly
    x:     -9.67002233332199662166
    error: 0.108877778911448945119
    converging slowly
    accelerating convergence
    x:     -9.5622443299551077669
    error: 0.107778003366888854764
    converging slowly
    x:     0.99999999999999999214
    error: 10.562244329955107759
    x:     1.0
    error: 7.8598304758094664213e-18
    1.0
Got:
    ('x:    ', -9.88888888888888888889)
    ('error:', 0.111111111111111111111)
    converging slowly
    ('x:    ', -9.77890011223344556678)
    ('error:', 0.10998877665544332211)
    converging slowly
    ('x:    ', -9.67002233332199662166)
    ('error:', 0.108877778911448945119)
    converging slowly
    accelerating convergence
    ('x:    ', -9.5622443299551077669)
    ('error:', 0.107778003366888854764)
    converging slowly
    ('x:    ', 0.99999999999999999214)
    ('error:', 10.562244329955107759)
    ('x:    ', 1.0)
    ('error:', 7.8598304758094664213e-18)
    1.0
0.132
__name__ 0.001
```

and

```
superfac 0.05
secondzeta **********************************************************************
File "/home/francois/Work/sandbox/sage-4.6.2.alpha4/local/lib/python2.6/site-packages/mpmath/functions/zeta.py", line 983, in NoName
Failed example:
    secondzeta(0.5 + 40j, error=True, verbose=True)
Expected:
    main term = (-30190318549.138656312556 - 13964804384.624622876523j)
        computed using 19 zeros of zeta
    prime term = (132717176.89212754625045 + 188980555.17563978290601j)
        computed using 9 values of the von Mangoldt function
    exponential term = (542447428666.07179812536 + 362434922978.80192435203j)
    singular term = (512124392939.98154322355 + 348281138038.65531023921j)
    ((0.059471043 + 0.3463514534j), 1.455191523e-11)
Got:
    ('main term =', (-30190318549.138656312556 - 13964804384.624622876523j))
    ('    computed using', 19, 'zeros of zeta')
    ('prime term =', (132717176.89212754625045 + 188980555.17563978290601j))
    ('    computed using', 9, 'values of the von Mangoldt function')
    ('exponential term =', (542447428666.07179812536 + 362434922978.80192435203j))
    ('singular term =', (512124392939.98154322355 + 348281138038.65531023921j))
    ((0.059471043 + 0.3463514534j), 1.455191523e-11)
**********************************************************************
File "/home/francois/Work/sandbox/sage-4.6.2.alpha4/local/lib/python2.6/site-packages/mpmath/functions/zeta.py", line 992, in NoName
Failed example:
    secondzeta(0.5 + 40j, a=0.04, error=True, verbose=True)
Expected:
    main term = (-151962888.19606243907725 - 217930683.90210294051982j)
        computed using 9 zeros of zeta
    prime term = (2476659342.3038722372461 + 28711581821.921627163136j)
        computed using 37 values of the von Mangoldt function
    exponential term = (178506047114.7838188264 + 819674143244.45677330576j)
    singular term = (175877424884.22441310708 + 790744630738.28669174871j)
    ((0.059471043 + 0.3463514534j), 1.455191523e-11)
Got:
    ('main term =', (-151962888.19606243907725 - 217930683.90210294051982j))
    ('    computed using', 9, 'zeros of zeta')
    ('prime term =', (2476659342.3038722372461 + 28711581821.921627163136j))
    ('    computed using', 37, 'values of the von Mangoldt function')
    ('exponential term =', (178506047114.7838188264 + 819674143244.45677330576j))
    ('singular term =', (175877424884.22441310708 + 790744630738.28669174871j))
    ((0.059471043 + 0.3463514534j), 1.455191523e-11)
34.812
inf 0.002
```

I am preparing a run on amd64 with a fresh 4.6.2.rc0 without any patches.


---

Comment by fredrik.johansson created at 2011-02-21 09:52:03

These two failures were noted in a previous comment. They can safely be ignored.


---

Comment by fbissey created at 2011-02-21 09:57:14

Replying to [comment:24 fredrik.johansson]:
> These two failures were noted in a previous comment. They can safely be ignored.

I didn't realise they were the same one. I guess I expected they were fixed but that would require a new version of mpmath, not just sage patch I imagine.
Once I have tested this at least on amd64 I can give a positive review.


---

Comment by fbissey created at 2011-02-21 21:12:55

OK so I tested this on linux-amd64 and OS X (10.5). and the tests perform ok.
Although there is some noise on OS X because the wrong version of freetype is detected. I am not sure that the spkg fault or not.

```
test_visualization
    axes                      dyld: Library not loaded: /usr/X11/lib/libfreetype.6.dylib
  Referenced from: /usr/X11/bin/fc-list
  Reason: Incompatible library version: fc-list requires version 13.0.0 or later, but libfreetype.6.dylib provides version 10.0.0
dyld: Library not loaded: /usr/X11/lib/libfreetype.6.dylib
  Referenced from: /usr/X11/bin/fc-list
  Reason: Incompatible library version: fc-list requires version 13.0.0 or later, but libfreetype.6.dylib provides version 10.0.0
ok        6.5380421 s

finished tests in 17.99 seconds
```

On further inspection this test is run because matplotlib is present and I assume that this message originates from matplotlib. So the problem is probably in matplotlib.

The last thing is whether we make matplotlib a dependency of mpmath or not.
I will post a patch making this the default. Voice any opposition then.


---

Attachment

patch to deps to make mpmath depend on matplotlib


---

Comment by fbissey created at 2011-03-13 22:57:03

Fredrik, a question about mpmath behavior with regards to matplotlib. Is mpmath detecting matplotlib at compilation time or its presence at runtime?


---

Comment by fredrik.johansson created at 2011-03-13 23:29:46

Runtime. In fact, it only attempts to import matplotlib from inside the plotting functions (which are pure Python).


---

Comment by fbissey created at 2011-03-14 00:29:43

Thanks, that means we don't need to depend on it. I am giving this a positive review. Hopefully it will be picked up for 4.7.


---

Comment by fbissey created at 2011-03-14 00:29:43

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-03-27 13:51:48

Please change the commit message (using `hg qrefresh -e`) such that the ticket number appears on the first line.


---

Comment by jdemeyer created at 2011-03-27 13:51:48

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-04-11 13:47:24

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-04-11 19:16:07

Resolution: fixed


---

Comment by fbissey created at 2011-04-13 02:49:33

Sorry I meant to do the refresh but I was unable to get it working.


---

Comment by jdemeyer created at 2011-05-04 09:47:49

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2011-05-04 09:47:49

The files `SPKG.txt` and `spkg-install` should be put under hg control.  Also, SPKG.txt should not be executable.  Please fix these trivial issues.


---

Comment by jdemeyer created at 2011-05-04 09:47:49

Changing status from closed to new.


---

Comment by jdemeyer created at 2011-05-04 09:48:31

Changing priority from major to blocker.


---

Comment by fredrik.johansson created at 2011-05-04 09:54:32

I can fix the permissions in the spkg. What is involved to put SPKG.txt and spkg-install under hg control?


---

Comment by jdemeyer created at 2011-05-04 12:19:36

Replying to [comment:38 fredrik.johansson]:
> I can fix the permissions in the spkg. What is involved to put SPKG.txt and spkg-install under hg control?

Never mind.  I did it myself: [http://boxen.math.washington.edu/home/jdemeyer/spkg/mpmath-0.17.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/mpmath-0.17.spkg)


---

Comment by jdemeyer created at 2011-05-04 12:19:36

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2011-05-06 07:19:20

Resolution: fixed
