# Issue 9759: Possible numerical noise doctest failure in sage/matrix/matrix2.pyx on t2

archive/issues_009759.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jhpalmieri\n\nReported by John Palmieri on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/67feb1b840ff2710/90a82acffe8f10de#90a82acffe8f10de):\n\n```\nOn t2, I'm getting a failure:\n\nsage -t  -long devel/sage/sage/matrix/matrix2.pyx\n**********************************************************************\nFile \"/home/palmieri/t2/sage-4.5.3.alpha1/devel/sage-main/sage/matrix/\nmatrix2.pyx\", line 6406:\n    sage: all(imag(e) < 1e-15 for e in eigs)\nExpected:\n    True\nGot:\n    False\n\nThis looks like numerical noise: if I replace 1e-15 by 1e-14, it passes.  Has anyone else seen this?  Could it possibly be dependent on ATLAS (e.g., the load on the system when it's tuning itself)? \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9760\n\n",
    "created_at": "2010-08-17T23:46:36Z",
    "labels": [
        "porting: Solaris",
        "blocker",
        "bug"
    ],
    "title": "Possible numerical noise doctest failure in sage/matrix/matrix2.pyx on t2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9759",
    "user": "mpatel"
}
```
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



Issue created by migration from https://trac.sagemath.org/ticket/9760





---

archive/issue_comments_095591.json:
```json
{
    "body": "I expect ATLAS would be used for this test, but has that been 100% confirmed? \n\nIt's very puzzling. I guess its possible that ATLAS may give slightly different results if it's tuned differently.\n\nI suspect John built this with the ATLAS changes at #9508. Since he normally used a version of ATLAS he built before to save time, I suspect he tuned ATLAS this time. \n\nJohn reported on #9508 that the ATLAS changes has been tested on t2. Does this mean the doctests passed for John once, but failed on a second build? \n\nI can power up my SPARC tomorrow and see if I can reproduce this. Since my processors are reconised by ATLAS, it does not go through the lenghty tuning process needed on 't2', and so the tuning parameters will not change from one build to another. \n\nCan John try removing ATLAS, then using his old ATLAS file (or they are in /ATLAS on t2). \n\nIt's possible that the additional shared libraries from #9508 mean something in Sage that previously linked with a static library, would now link with a shared one. \n\nI suspect slight differences in tuning parameters might be the cause though. Does the criteria need to be  changed by a factor of 10 to get htis to pass, or would a maller change be acceptable,",
    "created_at": "2010-08-18T00:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95591",
    "user": "drkirkby"
}
```

I expect ATLAS would be used for this test, but has that been 100% confirmed? 

It's very puzzling. I guess its possible that ATLAS may give slightly different results if it's tuned differently.

I suspect John built this with the ATLAS changes at #9508. Since he normally used a version of ATLAS he built before to save time, I suspect he tuned ATLAS this time. 

John reported on #9508 that the ATLAS changes has been tested on t2. Does this mean the doctests passed for John once, but failed on a second build? 

I can power up my SPARC tomorrow and see if I can reproduce this. Since my processors are reconised by ATLAS, it does not go through the lenghty tuning process needed on 't2', and so the tuning parameters will not change from one build to another. 

Can John try removing ATLAS, then using his old ATLAS file (or they are in /ATLAS on t2). 

It's possible that the additional shared libraries from #9508 mean something in Sage that previously linked with a static library, would now link with a shared one. 

I suspect slight differences in tuning parameters might be the cause though. Does the criteria need to be  changed by a factor of 10 to get htis to pass, or would a maller change be acceptable,



---

archive/issue_comments_095592.json:
```json
{
    "body": "For the example starting around line 6393 of `sage/matrix/matrix2.pyx`, I get this on t2:\n\n```python\nsage: set_random_seed(0)\nsage: r = MatrixSpace(ComplexField(100), 6, 6).random_element()\nsage: m = r * r.conjugate().transpose()\nsage: m.change_ring(CDF);\nsage: eigs = m.change_ring(CDF).eigenvalues()\nsage: from sage.misc.citation import get_systems\nsage: get_systems('eigs = m.change_ring(CDF).eigenvalues()')\n['numpy', 'scipy']\nsage: [imag(e) for e in eigs]\n[-3.08834127609e-16, 1.137042931e-16, 1.50426489494e-16, 1.64867945474e-16, -4.61662881292e-16, 1.74964827139e-16]\nsage: all(imag(e) < 1e-15 for e in eigs)\nTrue\n```\n\nOn sage.math, I get\n\n```python\n[...]\nsage: [imag(e) for e in eigs]\n[-4.98835989975e-16, -5.05298436852e-16, 5.59670199836e-17, 4.34508443713e-17, -5.75358699674e-17, 5.1816322259e-16]\nsage: sage: all(imag(e) < 1e-15 for e in eigs)\nTrue\n```\n\n(The real parts of the eigenvalues agree.)  I suppose that these are double-precision computations and that we cannot take the returned imaginary parts as other than \"small\"?",
    "created_at": "2010-08-18T01:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95592",
    "user": "mpatel"
}
```

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

archive/issue_comments_095593.json:
```json
{
    "body": "To clarify:  \"...and that we cannot take the returned imaginary parts **here** as other than \"small\"?\"",
    "created_at": "2010-08-18T01:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95593",
    "user": "mpatel"
}
```

To clarify:  "...and that we cannot take the returned imaginary parts **here** as other than "small"?"



---

archive/issue_comments_095594.json:
```json
{
    "body": "Replying to [comment:1 drkirkby]:\n> I expect ATLAS would be used for this test, but has that been 100% confirmed? \n> \n> It's very puzzling. I guess its possible that ATLAS may give slightly different results if it's tuned differently.\n> \n> I suspect John built this with the ATLAS changes at #9508. Since he normally used a version of ATLAS he built before to save time, I suspect he tuned ATLAS this time. \n\nThat's right.  Although my old version is based on atlas-3.8.3.p12, compared to the current 3.8.3.p14.  I also had to rebuild the shared libraries, and I rebuilt them using exactly the commands from the p14 spkg.  I don't think the ATLAS sources changed from p12 to p14, so the only difference should be in the tuning from one time (several months ago) to another.  When I built Sage using SAGE_ATLAS_LIB pointing to my old version, the tests passed; indeed, if I just copy the p12 files to SAGE_ROOT/local/lib, then tests pass.  If I copy the p14 files back, then tests fail.\n\n> It's possible that the additional shared libraries from #9508 mean something in Sage that previously linked with a static library, would now link with a shared one. \n\nI don't know if it's that or if it's just different tuning from one build to the next.\n\n> I suspect slight differences in tuning parameters might be the cause though. Does the criteria need to be  changed by a factor of 10 to get htis to pass, or would a maller change be acceptable,\n\nA smaller change would work, at least right now: the largest imaginary part for any eigenvalue is 1.09867961128e-15.  With the p12 files, the largest (in absolute value) is -4.61662881292e-16.  Of course, now I see that the doctest should really be **abs**(imag(e)) < 1e-15...",
    "created_at": "2010-08-18T01:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95594",
    "user": "jhpalmieri"
}
```

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

A smaller change would work, at least right now: the largest imaginary part for any eigenvalue is 1.09867961128e-15.  With the p12 files, the largest (in absolute value) is -4.61662881292e-16.  Of course, now I see that the doctest should really be **abs**(imag(e)) < 1e-15...



---

archive/issue_comments_095595.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> Replying to [comment:1 drkirkby]:\n> > I expect ATLAS would be used for this test, but has that been 100% confirmed? \n> > \n> > It's very puzzling. I guess its possible that ATLAS may give slightly different results if it's tuned differently.\n> > \n> > I suspect John built this with the ATLAS changes at #9508. Since he normally used a version of ATLAS he built before to save time, I suspect he tuned ATLAS this time. \n> \n> That's right.  Although my old version is based on atlas-3.8.3.p12, compared to the current 3.8.3.p14.  I also had to rebuild the shared libraries, and I rebuilt them using exactly the commands from the p14 spkg.  I don't think the ATLAS sources changed from p12 to p14,\n\nThat is correct - the ATLAS source code has not changed. \n\n> so the only difference should be in the tuning from one time (several months ago) to another.  When I built Sage using SAGE_ATLAS_LIB pointing to my old version, the tests passed; indeed, if I just copy the p12 files to SAGE_ROOT/local/lib, then tests pass.  If I copy the p14 files back, then tests fail.\n>\n\n> > It's possible that the additional shared libraries from #9508 mean something in Sage that previously linked with a static library, would now link with a shared one. \n> \n> I don't know if it's that or if it's just different tuning from one build to the next.\n\nCan you try backing up the additional shared libraries, then see if the tests pass or fail in the same way. It could well totally mess up the build, as if a shared library is missing, it may fail to work. But if it still works, but fails, that means the change in the static library has caused this. \n \n> > I suspect slight differences in tuning parameters might be the cause though. Does the criteria need to be  changed by a factor of 10 to get htis to pass, or would a maller change be acceptable,\n> \n> A smaller change would work, at least right now: the largest imaginary part for any eigenvalue is 1.09867961128e-15.  With the p12 files, the largest (in absolute value) is -4.61662881292e-16.  Of course, now I see that the doctest should really be **abs**(imag(e)) < 1e-15...\n\nIf I have understood you correctly, to get this to pass, a change from\n\n`abs((imag(e)) < 1e-15` \n\nto\n\n`abs((imag(e)) < 1.1e-15` \n\nwould be sufficient, which is only a 10% change from the current value. That would seem safe to me. \n\nI've started to build this on a SPARC where the tuning parameters should not have changed, as ATLAS has them for the UltraSPARC III+ CPUs in my Blade 1000. But it will take the best part of a day before I know the results of that. (I can't use a faster machine as it's in the house and too noisy! The slower one is in the garage. I might change that soon, as I have no need for the faster SPARC in the house any more) \n\ndave",
    "created_at": "2010-08-18T08:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95595",
    "user": "drkirkby"
}
```

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
> A smaller change would work, at least right now: the largest imaginary part for any eigenvalue is 1.09867961128e-15.  With the p12 files, the largest (in absolute value) is -4.61662881292e-16.  Of course, now I see that the doctest should really be **abs**(imag(e)) < 1e-15...

If I have understood you correctly, to get this to pass, a change from

`abs((imag(e)) < 1e-15` 

to

`abs((imag(e)) < 1.1e-15` 

would be sufficient, which is only a 10% change from the current value. That would seem safe to me. 

I've started to build this on a SPARC where the tuning parameters should not have changed, as ATLAS has them for the UltraSPARC III+ CPUs in my Blade 1000. But it will take the best part of a day before I know the results of that. (I can't use a faster machine as it's in the house and too noisy! The slower one is in the garage. I might change that soon, as I have no need for the faster SPARC in the house any more) 

dave



---

archive/issue_comments_095596.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n\n> Can you try backing up the additional shared libraries, then see if the tests pass or fail in the same way. It could well totally mess up the build, as if a shared library is missing, it may fail to work. But if it still works, but fails, that means the change in the static library has caused this. \n\nI'm not sure what you mean by this. For the tests with the old ATLAS build and the new one, I changed all of the libraries built by ATLAS: libatlas.a, libatlas.so, ... (7 altogether, 4 static and 3 shared, since liblapack.so is not built).  Do you want me to just delete the .so files instead?  Sage doesn't start in that case.\n\n> If I have understood you correctly, to get this to pass, a change from\n\n```\nabs((imag(e)) < 1e-15\n```\n\n> to\n\n```\nabs((imag(e)) < 1.1e-15\n```\n\n\nRight, except it's actually changing from `imag(e) < 1e-15` (with no \"abs\") to `abs(imag(e)) < 1.1e-15`.  The test does pass with this change.  It would be safest to not add the \"abs\" right now: with that change, it would clearly still pass wherever it worked before.  Adding the \"abs\" changes what the test is actually testing, though, and would require evaluation on lots of platforms: for all we know, there is numerical noise somewhere else which gives a relatively large negative imaginary part for one of the eigenvalues.  Should we make this change on this ticket or elsewhere?",
    "created_at": "2010-08-18T15:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95596",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_095597.json:
```json
{
    "body": "Let's make adding \"abs\" a separate ticket that we can include early in the 4.6 series.",
    "created_at": "2010-08-18T21:56:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95597",
    "user": "mpatel"
}
```

Let's make adding "abs" a separate ticket that we can include early in the 4.6 series.



---

archive/issue_comments_095598.json:
```json
{
    "body": "Okay, here's a patch, replacing 1 by 1.1.",
    "created_at": "2010-08-18T22:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95598",
    "user": "jhpalmieri"
}
```

Okay, here's a patch, replacing 1 by 1.1.



---

archive/issue_comments_095599.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-18T22:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95599",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095600.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-18T22:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95600",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_095601.json:
```json
{
    "body": "See #9765 for the \"abs\" issue.",
    "created_at": "2010-08-18T22:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95601",
    "user": "jhpalmieri"
}
```

See #9765 for the "abs" issue.



---

archive/issue_comments_095602.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-18T22:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95602",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_095603.json:
```json
{
    "body": "Okay, I've now turned at least part of my mind on.  The file \"....pyx\" should be called \"....patch\".  I've attached a properly named file, identical to the first one.",
    "created_at": "2010-08-18T22:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95603",
    "user": "jhpalmieri"
}
```

Okay, I've now turned at least part of my mind on.  The file "....pyx" should be called "....patch".  I've attached a properly named file, identical to the first one.



---

archive/issue_comments_095604.json:
```json
{
    "body": "I was just about to write this below, and when I tried to submit it, you had beaten me to it. I think you have basically confirmed what I thought. \n\n----\nJohn,\n\nI'm not exactly sure what's happening in this Sage code - I don't understand Sage well enough. \n\nBut I'm guessing that the the eigenvalues should be real numbers here - i.e. have zero imaginary component. Any imaginary component present is due to rounding errors. Would that be right? \n\nIf so, I would have thought testing the absolute value was actually the more sensible test. If the imaginary part of the eigenvalue was -1000, then the original test would pass, despite my belief that such a huge negative value would be incorrect. It seems to me the actual test is fundamentally flawed. \n\nHowever, adding the abs() would need testing on lots of platforms, so I'm not suggesting we make that change. \n\nI think in this case, we should change the test to \n\n`imag(e) < 1.1e-15`\n\nand perhaps open another ticket to change the test, to add the `abs()` at a later date. \n\nDoes that seem sensible? \n\nDave",
    "created_at": "2010-08-18T22:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95604",
    "user": "drkirkby"
}
```

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

archive/issue_comments_095605.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-18T22:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95605",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095606.json:
```json
{
    "body": "For the record, I built Sage on a Sun Blade 1000, with 2 GB RAM and two UltraSPARC III+ processors. Unlike the T2 PLUS CPUs in 't2,math', ATLAS has the tuning parameters for these older processors, so does not need to go through the tuning process. Hence I assume (though may be wrong), that ATLAS will build the say way each time I build it. Anyway, all tests finally passed. \n\n\n```\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 25806.8 seconds\n```\n\n\nSo I don't think we have introduced any problems - ATLAS probably just had a bad day on t2!\n\nDave",
    "created_at": "2010-08-19T17:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95606",
    "user": "drkirkby"
}
```

For the record, I built Sage on a Sun Blade 1000, with 2 GB RAM and two UltraSPARC III+ processors. Unlike the T2 PLUS CPUs in 't2,math', ATLAS has the tuning parameters for these older processors, so does not need to go through the tuning process. Hence I assume (though may be wrong), that ATLAS will build the say way each time I build it. Anyway, all tests finally passed. 


```
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 25806.8 seconds
```


So I don't think we have introduced any problems - ATLAS probably just had a bad day on t2!

Dave



---

archive/issue_comments_095607.json:
```json
{
    "body": "Replying to [comment:13 drkirkby]:\n> So I don't think we have introduced any problems - ATLAS probably just had a bad day on t2!\n\nI agree, and having to change the test from `1e-15` to `1.1e-15` is pretty minor.",
    "created_at": "2010-08-19T17:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95607",
    "user": "jhpalmieri"
}
```

Replying to [comment:13 drkirkby]:
> So I don't think we have introduced any problems - ATLAS probably just had a bad day on t2!

I agree, and having to change the test from `1e-15` to `1.1e-15` is pretty minor.



---

archive/issue_comments_095608.json:
```json
{
    "body": "NB although this has a positive review, there;s a problem with it fixed by a oatch at #9765.  Would it not be better to change the patch here?",
    "created_at": "2010-08-22T13:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95608",
    "user": "cremona"
}
```

NB although this has a positive review, there;s a problem with it fixed by a oatch at #9765.  Would it not be better to change the patch here?



---

archive/issue_comments_095609.json:
```json
{
    "body": "Replying to [comment:16 cremona]:\n> NB although this has a positive review, there;s a problem with it fixed by a oatch at #9765.  Would it not be better to change the patch here?\n\nThe point is that this patch is very safe, and will not cause any doctest failures on any machines. It has been marked as a blocker, and the release manager has agreed to merge it in 4.5.3\n\nIn contrast, whilst #9765 should not cause any build failures, we do not know if it will cause any doctest failures.  We might need to adjust the 1.1e-15 up a little. As such, it would be unwise to put it a release candidate without it being tested more fully. \n\n\n\nDave",
    "created_at": "2010-08-22T13:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95609",
    "user": "drkirkby"
}
```

Replying to [comment:16 cremona]:
> NB although this has a positive review, there;s a problem with it fixed by a oatch at #9765.  Would it not be better to change the patch here?

The point is that this patch is very safe, and will not cause any doctest failures on any machines. It has been marked as a blocker, and the release manager has agreed to merge it in 4.5.3

In contrast, whilst #9765 should not cause any build failures, we do not know if it will cause any doctest failures.  We might need to adjust the 1.1e-15 up a little. As such, it would be unwise to put it a release candidate without it being tested more fully. 



Dave



---

archive/issue_comments_095610.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-24T02:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9759#issuecomment-95610",
    "user": "mpatel"
}
```

Resolution: fixed
