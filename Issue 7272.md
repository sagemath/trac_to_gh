# Issue 7272: Upgrade to Cython 0.12

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-10-23 17:04:56

Assignee: mabshoff

Cython 0.12 isn't released yet, but should be shortly, and this ticket is about getting Sage to compile and pass all tests.

Spkg at http://sage.math.washington.edu/home/robertwb/cython/cython-0.12.spkg

Also depends on patch at #7023 (to be applied before the attached patch). 


---

Comment by robertwb created at 2009-10-23 17:10:36

Changing status from new to needs_work.


---

Comment by robertwb created at 2009-10-23 17:10:36

I had to force cdivision=True globally as way to much stuff broke otherwise (and even if all tests passed, it's a bold move that should be taken after looking through the entire library for problems).


---

Comment by robertwb created at 2009-10-23 17:14:41

I've gotten everything working but


```
	sage -t  "sage/modular/modsym/ambient.py"
	sage -t  "sage/modular/modsym/heilbronn.pyx"
```


with 


```
sage -t  "devel/sage-cython2/sage/modular/modsym/heilbronn.pyx"
python(96760) malloc: *** mmap(size=1744830464) failed (error code=12)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
**********************************************************************
File "/Users/robertwb/sage/sage-4.0/devel/sage-cython2/sage/modular/modsym/heilbronn.pyx", line 839:
    sage: sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k(4,1,3,15,6,[1,11,12], R)
Exception raised:
    Traceback (most recent call last):
      File "/Users/robertwb/sage/sage-4.0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/robertwb/sage/sage-4.0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/robertwb/sage/sage-4.0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[4]>", line 1, in <module>
        sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k(Integer(4),Integer(1),Integer(3),Integer(15),Integer(6),[Integer(1),Integer(11),Integer(12)], R)###line 839:
    sage: sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k(4,1,3,15,6,[1,11,12], R)
      File "heilbronn.pyx", line 877, in sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k (sage/modular/modsym/heilbronn.c:7652)
      File "heilbronn.pyx", line 417, in sage.modular.modsym.heilbronn.HeilbronnMerel.__init__ (sage/modular/modsym/heilbronn.c:4561)
    SystemError: NULL result without error in PyObject_Call
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_17
***Test Failed*** 1 failures.
```



---

Comment by robertwb created at 2009-10-30 06:13:43

Above failure due to memory corruption caused by http://trac.cython.org/cython_trac/ticket/442

Sage builds and passes all tests (vanilla 4.2 + attached patch)


---

Attachment


---

Comment by mhansen created at 2009-11-17 11:10:00

Looks good to me.

I went ahead and removed the src/.hg/ repo from the Cython spkg and checked in the modification to spkg-install.  The new spkg can be found at http://sage.math.washington.edu/home/mhansen/cython-0.12.spkg


---

Comment by mhansen created at 2009-11-17 11:10:00

Resolution: fixed


---

Comment by robertwb created at 2009-11-17 20:07:49

Changing status from closed to needs_work.


---

Comment by robertwb created at 2009-11-17 20:07:49

Thanks for doing this, but 0.12 isn't officially out yet. Fortunately, I just updated the spkg to the most recent release candidate a couple of days ago. I see a release happening in the next week, so the only change (that impacts us, there's two windows fixes since then) will be the version number bump (I hope). 

The linked spkg should work fine, but if we release soon (before you do) I'd be nice to actually be synced with upstream.


---

Comment by mhansen created at 2009-11-18 03:51:28

I think 0.12 will be out before 4.3.  I'll include the official 0.12 in the main release.


---

Comment by jason created at 2009-12-03 14:35:51

It looks like 0.12 is out now.  From the Cython webpage:


```
The latest release of Cython is 0.12 (released 2009-11-23).
```


Is the official release in the spkg above, or were there changes since the spkg above?

And congrats on the 0.12 release!  I'm excited about the improvements in it!


---

Comment by robertwb created at 2009-12-03 16:44:57

I'll upload the actual spkg.


---

Comment by robertwb created at 2009-12-05 17:23:39

Spkg at http://sage.math.washington.edu/home/robertwb/cython/cython-0.12.spkg is the 0.12 release (minus repo).


---

Comment by robertwb created at 2009-12-07 19:20:22

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2009-12-07 19:21:30

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2009-12-07 19:21:30

I'm changing this to positive review, as the changes between when this was merged and the official upstream are minimal.


---

Comment by mhansen created at 2009-12-07 23:19:15

I've merged this new spkg in 4.3.rc0
