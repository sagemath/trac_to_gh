# Issue 9759: Possible numerical noise doctest failure in sage/matrix/matrix2.pyx on t2

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-08-17 23:46:36

Assignee: drkirkby

CC:  jhpalmieri

Reported by John Palmieri on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/67feb1b840ff2710/90a82acffe8f10de#90a82acffe8f10de):

```
On t2, I'm getting a failure:

sage -t  -long devel/sage/sage/matrix/matrix2.pyx
**********************************************************************
File "/home/palmieri/t2/sage-4.5.3.alpha1/devel/sage-main/sage/matrix/
matrix2.pyx", line 6406:
    sage: all(imag(e) < 1e-15 for e in eigs)
Expected:
    True
Got:
    False

This looks like numerical noise: if I replace 1e-15 by 1e-14, it passes.  Has anyone else seen this?  Could it possibly be dependent on ATLAS (e.g., the load on the system when it's tuning itself)? 
```




---

Comment by drkirkby created at 2010-08-18 00:21:39

I expect ATLAS would be used for this test, but has that been 100% confirmed? 

It's very puzzling. I guess its possible that ATLAS may give slightly different results if it's tuned differently.

I suspect John built this with the ATLAS changes at #9508. Since he normally used a version of ATLAS he built before to save time, I suspect he tuned ATLAS this time. 

John reported on #9508 that the ATLAS changes has been tested on t2. Does this mean the doctests passed for John once, but failed on a second build? 

I can power up my SPARC tomorrow and see if I can reproduce this. Since my processors are reconised by ATLAS, it does not go through the lenghty tuning process needed on 't2', and so the tuning parameters will not change from one build to another. 

Can John try removing ATLAS, then using his old ATLAS file (or they are in /ATLAS on t2). 

It's possible that the additional shared libraries from #9508 mean something in Sage that previously linked with a static library, would now link with a shared one. 

I suspect slight differences in tuning parameters might be the cause though. Does the criteria need to be  changed by a factor of 10 to get htis to pass, or would a maller change be acceptable,


---

Comment by mpatel created at 2010-08-18 01:22:20

For the example starting around line 6393 of `sage/matrix/matrix2.pyx`, I get this on t2:

```python
sage: set_random_seed(0)
sage: r = MatrixSpace(ComplexField(100), 6, 6).random_element()
sage: m = r * r.conjugate().transpose()
sage: m.change_ring(CDF);
sage: eigs = m.change_ring(CDF).eigenvalues()
sage: from sage.misc.citation import get_systems
sage: get_systems('eigs = m.change_ring(CDF).eigenvalues()')
['numpy', 'scipy']
sage: [imag(e) for e in eigs]
[-3.08834127609e-16, 1.137042931e-16, 1.50426489494e-16, 1.64867945474e-16, -4.61662881292e-16, 1.74964827139e-16]
sage: all(imag(e) < 1e-15 for e in eigs)
True
```

On sage.math, I get

```python
[...]
sage: [imag(e) for e in eigs]
[-4.98835989975e-16, -5.05298436852e-16, 5.59670199836e-17, 4.34508443713e-17, -5.75358699674e-17, 5.1816322259e-16]
sage: sage: all(imag(e) < 1e-15 for e in eigs)
True
```

(The real parts of the eigenvalues agree.)  I suppose that these are double-precision computations and that we cannot take the returned imaginary parts as other than "small"?


---

Comment by mpatel created at 2010-08-18 01:26:04

To clarify:  "...and that we cannot take the returned imaginary parts *here* as other than "small"?"


---

Comment by jhpalmieri created at 2010-08-18 01:32:02

Replying to [comment:1 drkirkby]:
> I expect ATLAS would be used for this test, but has that been 100% confirmed? 
> 
> It's very puzzling. I guess its possible that ATLAS may give slightly different results if it's tuned differently.
> 
> I suspect John built this with the ATLAS changes at #9508. Since he normally used a version of ATLAS he built before to save time, I suspect he tuned ATLAS this time. 

That's right.  Although my old version is based on atlas-3.8.3.p12, compared to the current 3.8.3.p14.  I also had to rebuild the shared libraries, and I rebuilt them using exactly the commands from the p14 spkg.  I don't think the ATLAS sources changed from p12 to p14, so the only difference should be in the tuning from one time (several months ago) to another.  When I built Sage using SAGE_ATLAS_LIB pointing to my old version, the tests passed; indeed, if I just copy the p12 files to SAGE_ROOT/local/lib, then tests pass.  If I copy the p14 files back, then tests fail.

> It's possible that the additional shared libraries from #9508 mean something in Sage that previously linked with a static library, would now link with a shared one. 

I don't know if it's that or if it's just different tuning from one build to the next.

> I suspect slight differences in tuning parameters might be the cause though. Does the criteria need to be  changed by a factor of 10 to get htis to pass, or would a maller change be acceptable,

A smaller change would work, at least right now: the largest imaginary part for any eigenvalue is 1.09867961128e-15.  With the p12 files, the largest (in absolute value) is -4.61662881292e-16.  Of course, now I see that the doctest should really be *abs*(imag(e)) < 1e-15...


---

Comment by drkirkby created at 2010-08-18 08:04:16

Replying to [comment:4 jhpalmieri]:
> Replying to [comment:1 drkirkby]:
> > I expect ATLAS would be used for this test, but has that been 100% confirmed? 
> > 
> > It's very puzzling. I guess its possible that ATLAS may give slightly different results if it's tuned differently.
> > 
> > I suspect John built this with the ATLAS changes at #9508. Since he normally used a version of ATLAS he built before to save time, I suspect he tuned ATLAS this time. 
> 
> That's right.  Although my old version is based on atlas-3.8.3.p12, compared to the current 3.8.3.p14.  I also had to rebuild the shared libraries, and I rebuilt them using exactly the commands from the p14 spkg.  I don't think the ATLAS sources changed from p12 to p14,

That is correct - the ATLAS source code has not changed. 

> so the only difference should be in the tuning from one time (several months ago) to another.  When I built Sage using SAGE_ATLAS_LIB pointing to my old version, the tests passed; indeed, if I just copy the p12 files to SAGE_ROOT/local/lib, then tests pass.  If I copy the p14 files back, then tests fail.
>

> > It's possible that the additional shared libraries from #9508 mean something in Sage that previously linked with a static library, would now link with a shared one. 
> 
> I don't know if it's that or if it's just different tuning from one build to the next.

Can you try backing up the additional shared libraries, then see if the tests pass or fail in the same way. It could well totally mess up the build, as if a shared library is missing, it may fail to work. But if it still works, but fails, that means the change in the static library has caused this. 
 
> > I suspect slight differences in tuning parameters might be the cause though. Does the criteria need to be  changed by a factor of 10 to get htis to pass, or would a maller change be acceptable,
> 
> A smaller change would work, at least right now: the largest imaginary part for any eigenvalue is 1.09867961128e-15.  With the p12 files, the largest (in absolute value) is -4.61662881292e-16.  Of course, now I see that the doctest should really be *abs*(imag(e)) < 1e-15...

If I have understood you correctly, to get this to pass, a change from

`abs((imag(e)) < 1e-15` 

to

`abs((imag(e)) < 1.1e-15` 

would be sufficient, which is only a 10% change from the current value. That would seem safe to me. 

I've started to build this on a SPARC where the tuning parameters should not have changed, as ATLAS has them for the UltraSPARC III+ CPUs in my Blade 1000. But it will take the best part of a day before I know the results of that. (I can't use a faster machine as it's in the house and too noisy! The slower one is in the garage. I might change that soon, as I have no need for the faster SPARC in the house any more) 

dave


---

Comment by jhpalmieri created at 2010-08-18 15:15:05

Replying to [comment:5 drkirkby]:

> Can you try backing up the additional shared libraries, then see if the tests pass or fail in the same way. It could well totally mess up the build, as if a shared library is missing, it may fail to work. But if it still works, but fails, that means the change in the static library has caused this. 

I'm not sure what you mean by this. For the tests with the old ATLAS build and the new one, I changed all of the libraries built by ATLAS: libatlas.a, libatlas.so, ... (7 altogether, 4 static and 3 shared, since liblapack.so is not built).  Do you want me to just delete the .so files instead?  Sage doesn't start in that case.

> If I have understood you correctly, to get this to pass, a change from

```
abs((imag(e)) < 1e-15
```

> to

```
abs((imag(e)) < 1.1e-15
```


Right, except it's actually changing from `imag(e) < 1e-15` (with no "abs") to `abs(imag(e)) < 1.1e-15`.  The test does pass with this change.  It would be safest to not add the "abs" right now: with that change, it would clearly still pass wherever it worked before.  Adding the "abs" changes what the test is actually testing, though, and would require evaluation on lots of platforms: for all we know, there is numerical noise somewhere else which gives a relatively large negative imaginary part for one of the eigenvalues.  Should we make this change on this ticket or elsewhere?


---

Comment by mpatel created at 2010-08-18 21:56:38

Let's make adding "abs" a separate ticket that we can include early in the 4.6 series.


---

Comment by jhpalmieri created at 2010-08-18 22:11:11

Okay, here's a patch, replacing 1 by 1.1.


---

Comment by jhpalmieri created at 2010-08-18 22:11:11

Changing status from new to needs_review.


---

Attachment


---

Comment by jhpalmieri created at 2010-08-18 22:16:41

See #9765 for the "abs" issue.


---

Attachment


---

Comment by jhpalmieri created at 2010-08-18 22:22:08

Okay, I've now turned at least part of my mind on.  The file "....pyx" should be called "....patch".  I've attached a properly named file, identical to the first one.


---

Comment by drkirkby created at 2010-08-18 22:35:22

I was just about to write this below, and when I tried to submit it, you had beaten me to it. I think you have basically confirmed what I thought. 

----
John,

I'm not exactly sure what's happening in this Sage code - I don't understand Sage well enough. 

But I'm guessing that the the eigenvalues should be real numbers here - i.e. have zero imaginary component. Any imaginary component present is due to rounding errors. Would that be right? 

If so, I would have thought testing the absolute value was actually the more sensible test. If the imaginary part of the eigenvalue was -1000, then the original test would pass, despite my belief that such a huge negative value would be incorrect. It seems to me the actual test is fundamentally flawed. 

However, adding the abs() would need testing on lots of platforms, so I'm not suggesting we make that change. 

I think in this case, we should change the test to 

`imag(e) < 1.1e-15`

and perhaps open another ticket to change the test, to add the `abs()` at a later date. 

Does that seem sensible? 

Dave


---

Comment by drkirkby created at 2010-08-18 22:36:34

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-08-19 17:28:07

For the record, I built Sage on a Sun Blade 1000, with 2 GB RAM and two UltraSPARC III+ processors. Unlike the T2 PLUS CPUs in 't2,math', ATLAS has the tuning parameters for these older processors, so does not need to go through the tuning process. Hence I assume (though may be wrong), that ATLAS will build the say way each time I build it. Anyway, all tests finally passed. 


```
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 25806.8 seconds
```


So I don't think we have introduced any problems - ATLAS probably just had a bad day on t2!

Dave


---

Comment by jhpalmieri created at 2010-08-19 17:51:17

Replying to [comment:13 drkirkby]:
> So I don't think we have introduced any problems - ATLAS probably just had a bad day on t2!

I agree, and having to change the test from `1e-15` to `1.1e-15` is pretty minor.


---

Comment by cremona created at 2010-08-22 13:19:03

NB although this has a positive review, there;s a problem with it fixed by a oatch at #9765.  Would it not be better to change the patch here?


---

Comment by drkirkby created at 2010-08-22 13:34:52

Replying to [comment:16 cremona]:
> NB although this has a positive review, there;s a problem with it fixed by a oatch at #9765.  Would it not be better to change the patch here?

The point is that this patch is very safe, and will not cause any doctest failures on any machines. It has been marked as a blocker, and the release manager has agreed to merge it in 4.5.3

In contrast, whilst #9765 should not cause any build failures, we do not know if it will cause any doctest failures.  We might need to adjust the 1.1e-15 up a little. As such, it would be unwise to put it a release candidate without it being tested more fully. 



Dave


---

Comment by mpatel created at 2010-08-24 02:49:17

Resolution: fixed
