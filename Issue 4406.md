# Issue 4406: make polynomail truncation cpdef method

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-10-30 20:07:21

Assignee: tbd

CC:  craigcitro

Currently we have _c variants, some of which call one direction, and some which call the other. 


---

Attachment

This wasn't as invasive as I had expected. Apply on top of fix at #2462.


---

Comment by mabshoff created at 2008-10-31 00:06:31

Patch looks good to me, but I will wait on a review #2462 before testing this. Also fixed a spelling mistake in the subject.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 02:51:38

This patch causes the following doctest failures:

```
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 1 doctests failed
	sage -t -long devel/sage/sage/rings/power_series_ring_element.pyx # 2 doctests failed
	sage -t -long devel/sage/sage/rings/power_series_poly.pyx # 2 doctests failed
	sage -t -long devel/sage/sage/modular/modform/theta.py # 1 doctests failed
	sage -t -long devel/sage/sage/modular/modform/j_invariant.py # 1 doctests failed
	sage -t -long devel/sage/sage/crypto/lfsr.py # 5 doctests failed
```

The error seems to always be

```
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_11[3]>", line 8, in <module>
        g = Rx(g, len(g))
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/rings/power_series_ring.py", line 326, in __call__
        return self.__power_series_class(self, f, prec, check=check)
      File "power_series_poly.pyx", line 47, in sage.rings.power_series_poly.PowerSeries_poly.__init__ (sage/rings/power_series_poly.c:2073)
      File "polynomial_element.pyx", line 3928, in sage.rings.polynomial.polynomial_element.Polynomial.truncate (sage/rings/polynomial/polynomial_element.c:25338)
      File "polynomial_gf2x.pyx", line 43, in sage.rings.polynomial.polynomial_gf2x.Polynomial_GF2X.__getitem__ (sage/rings/polynomial/polynomial_gf2x.cpp:6652)
    TypeError: an integer is required
```


Cheers,

Michael


---

Comment by robertwb created at 2008-10-31 18:06:23

Are you sure this is with my patch? I just tried these and they work fine in my branch. Or maybe it's some incompatibility with your alpha.


---

Comment by mabshoff created at 2008-10-31 18:08:47

Replying to [comment:4 robertwb]:
> Are you sure this is with my patch? I just tried these and they work fine in my branch. Or maybe it's some incompatibility with your alpha. 

Yes, I tried with this and the patch at #2462 and initially suspected #2462, but it turns out to be this patch. Reverting this patch only fixed the issue for me. 3.2.alpha2 is coming today, so there should be a binary for sage.math shortly.

Cheers,

Michael


---

Comment by robertwb created at 2008-10-31 18:11:06

OK, I'll look at it there.


---

Comment by robertwb created at 2008-11-01 23:13:55

I tried fixing this on sage.math, but I'm having issues with the unpacked tar. I copied over sage-3.2.alpha2-sage.math-only-x86_64-Linux and extracted it, but when I run ./sage I get


```
sage: sage.all.__file__
 '/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/all.pyc'
```


and I can't figure out how test my changes. However, I'm pretty sure the error is because line 467 of sage/rings/polynomial/polynomial_template.pxi is still def (rather than cpdef). I'm attaching a patch that should fix the problem.


---

Attachment


---

Comment by mabshoff created at 2008-11-01 23:16:27

I will test the patch and see if that fixes it. More than likely you are getting bitten by #4317, so following the instructions there you should be able to fix the problem.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-02 00:45:59

The second patch Robert posted resolves the issue I found. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-02 00:47:58

Merged in Sage 3.2.alpha3


---

Comment by mabshoff created at 2008-11-02 00:47:58

Resolution: fixed
