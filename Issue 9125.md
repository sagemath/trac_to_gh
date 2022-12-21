# Issue 9125: more examples of simplicial complexes: RP^n, CP^2, etc.

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-06-03 04:13:48

Assignee: jhpalmieri

This patch adds more examples of simplicial complexes: real projective spaces (that is, RP<sup>d</sup> for any positive d), CP<sup>2</sup>, and the Poincare homology sphere.  Some of these are the minimal triangulations, some are not; see the documentation.

These are important test cases for homology and other computations which I hope will be implemented soon -- see tickets #6102 and #6103, for instance.


---

Attachment


---

Comment by jhpalmieri created at 2010-06-03 04:14:27

Changing status from new to needs_review.


---

Comment by robert_goss created at 2010-11-10 22:54:05

Changing status from needs_review to positive_review.


---

Comment by robert_goss created at 2010-11-10 22:54:05

A very useful patch the documentation is very good.

The doc tests all run and the functionality seems correct.


I have been working on a function to generate simplicial complexes for the lens spaces. Although the implimentation is naive would it be something which would be useful to put in this patch?

Robert


---

Comment by jhpalmieri created at 2010-11-10 23:01:53

Replying to [comment:2 robert_goss]:
> I have been working on a function to generate simplicial complexes for the lens spaces. Although the implimentation is naive would it be something which would be useful to put in this patch?

I think having lens spaces would be very nice, although maybe it could go on another ticket so that the current patch can get merged.  If you post something, I'll almost certainly review it.   A naive approach would be fine, but you might also look at some of the papers referenced in the current patch.  In particular, 

 - Basudeb Datta, "Minimal triangulations of manifolds", J. Indian Inst. Sci. 87 (2007), no. 4, 429-449. 

 - Frank H. Lutz, "Triangulated Manifolds with Few Vertices: Combinatorial Manifolds", preprint (2005), 484	arXiv:math/0506372. 

are both expository papers which might include some discussion of lens spaces, or might give references.  (I think I've seen discussions of triangulations of lens spaces somewhere, but I don't remember where.  You might also try searching the web.)


---

Comment by jdemeyer created at 2010-11-14 10:59:38

robert_goss: please add your real name to [Account Names mapped to Real Names](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames) and also add it on this ticket as Reviewer.


---

Comment by robert_goss created at 2010-11-14 17:34:09

Replying to [comment:4 jdemeyer]:
> robert_goss: please add your real name to [Account Names mapped to Real Names](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames) and also add it on this ticket as Reviewer.


Hi thank you jdemeyer this is my first time contributing directly to sage and I am not sure of all the procedures.

Is there anything else I should do?


---

Comment by jdemeyer created at 2010-11-15 23:41:36

Resolution: fixed


---

Comment by drkirkby created at 2010-11-18 01:05:13

See the notes from  François Bissey

https://groups.google.com/group/sage-devel/browse_thread/thread/9e4cef8c8558150?hl=en

that this may be the cause of some timeouts seen on sage-gentoo. 

Dave


---

Comment by jdemeyer created at 2010-11-18 08:13:20

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2010-11-18 08:13:20

The tests take way too long time.  This is on a 32-bit Linux Pentium 4 system:

```
sage: P5 = simplicial_complexes.RealProjectiveSpace(Integer(5))
sage: time P5.homology()
CPU times: user 4083.68 s, sys: 0.63 s, total: 4084.31 s
Wall time: 4084.50 s
{0: 0, 1: C2, 2: 0, 3: C2, 4: 0, 5: Z}
```



---

Comment by jdemeyer created at 2010-11-18 08:13:20

Changing status from closed to new.


---

Comment by jdemeyer created at 2010-11-18 08:13:39

Changing status from new to needs_work.


---

Comment by jhpalmieri created at 2010-11-18 15:55:35

Apply this patch on top of the other one.  This way the doctest will only run if you give it a command like `sage -t -long -only-optional=chomp`.  Since the test finishes in about a second when using CHomP, as opposed to around half an hour (sometimes causing timeouts, since 1800 seconds is the cutoff for long doctests) without CHomP, this seems like the right solution.


---

Comment by jhpalmieri created at 2010-11-18 15:55:35

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-11-18 19:16:30

On the same Pentium 4 system, the following test

```
sage:P4 = simplicial_complexes.RealProjectiveSpace(4)
```

takes almost 4 seconds, so that should also be # long time (and hence also the following tests involving P4).


---

Comment by jhpalmieri created at 2010-11-18 22:46:28

Replying to [comment:11 jdemeyer]:
> On the same Pentium 4 system, the following test takes almost 4 seconds, so that should also be # long time (and hence also the following tests involving P4).

I'll do that, but are you using specific guidelines about what constitutes "long"?  On a 2-year-old iMac, it takes about 10 seconds to doctest the whole file ("sage -t examples.py", not "sage -t -long").  That doesn't seem excessively long to me, especially since the machine isn't new, and it wasn't a top-of-the line machine even when it was new.


---

Comment by jdemeyer created at 2010-11-19 07:18:29

The guideline is that 1 second is the bound for # long time.  In the Sage developer manual, there is the following example:

```
sage: E = EllipticCurve([0, 0, 1, -1, 0])
sage: E.regulator()              # long time (1 second)
0.0511114082399688
```



---

Comment by jhpalmieri created at 2010-12-15 19:03:00

apply on top of other patch


---

Attachment

Can this get reviewed soon?  The original patch was reviewed positively already, so I think only "trac_9125-doctest-fix.patch" needs to be reviewed.  That one just marks some doctests as being "long time" or "optional - CHomP", so I think it should be easy to review.


---

Comment by mhampton created at 2011-03-28 11:47:23

Looks like you missed one "long time" addition, so there is a doctest failure.  



```
**********************************************************************
File "/Users/mh/sagestuff/sage-4.7.alpha2/devel/sage-t1/sage/homology/examples.py", line 518:
    sage: P4.dimension()
Exception raised:
    Traceback (most recent call last):
      File "/Users/mh/sagestuff/sage-4.7.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mh/sagestuff/sage-4.7.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mh/sagestuff/sage-4.7.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[7]>", line 1, in <module>
        P4.dimension()###line 518:
    sage: P4.dimension()
    NameError: name 'P4' is not defined
**********************************************************************

```


I am attaching a cumulative patch that fixes that.


---

Comment by mhampton created at 2011-03-28 11:49:23

Use instead of previous doctest patch


---

Attachment

Oops, I forgot to fold so my patch is only cumulative with respect to trac_9125-doctest-fix.patch.


---

Comment by mhampton created at 2011-03-28 11:56:10

Looks good, passes all tests in sage/homology without chomp and everything passes -long -optional with chomp installed.

John, I think this can have a positive review but you should just double-check my patch.  (Its a tiny change.)  If its OK then you can change to positive review.


---

Comment by jhpalmieri created at 2011-03-28 20:03:36

Thanks, Marshall, looks good.  Tests failed with just my two patches, but they pass with yours.


---

Comment by jhpalmieri created at 2011-03-28 20:03:36

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-07 19:55:46

Resolution: fixed
