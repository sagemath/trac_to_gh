# Issue 9941: Fix CHomP-related doctest errors

archive/issues_009941.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nCC:  @qed777\n\nWith the optional CHomP package in 4.5.3 on sage.math, I get some doctest failures:\n\n```python\nsage -t -long -only-optional=chomp \"devel/sage/sage/homology/cell_complex.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/cell_complex.py\", line 470:\n    sage: S2.homology(dim=2, generators=True)  # optional - CHomP\nExpected:\n    (Z, [(0, 1, 2) - (0, 1, 3) + (0, 2, 3) - (1, 2, 3)])\nGot:\n    (Z, [-(0, 1, 2) + (0, 1, 3) - (0, 2, 3) + (1, 2, 3)])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9942\n\n",
    "created_at": "2010-09-18T18:04:01Z",
    "labels": [
        "component: algebraic topology",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Fix CHomP-related doctest errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9941",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

CC:  @qed777

With the optional CHomP package in 4.5.3 on sage.math, I get some doctest failures:

```python
sage -t -long -only-optional=chomp "devel/sage/sage/homology/cell_complex.py"
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/cell_complex.py", line 470:
    sage: S2.homology(dim=2, generators=True)  # optional - CHomP
Expected:
    (Z, [(0, 1, 2) - (0, 1, 3) + (0, 2, 3) - (1, 2, 3)])
Got:
    (Z, [-(0, 1, 2) + (0, 1, 3) - (0, 2, 3) + (1, 2, 3)])
```


Issue created by migration from https://trac.sagemath.org/ticket/9942





---

archive/issue_comments_098826.json:
```json
{
    "body": "On OS X 10.6, cell_complex passes all tests (with the same options as above), but I do get:\n\n\n```\nsage -t -long -only-optional=chomp \"devel/sage/sage/homology/tests.py\"\n**********************************************************************\nFile \"/Volumes/E/sage-4.6.rc0/devel/sage/sage/homology/tests.py\", line 10:\n    sage: test_random_chain_complex(trials=20)  # optional - CHomP\nExpected nothing\nGot:\n    Homology in dimension 20 according to CHomP: Z^16\n    Homology in dimension 20 according to Sage: Z^16\n    Chain complex: {20: 34 x 50 sparse matrix over Integer Ring, 21: []}\n    Random testing has revealed a problem in test_random_chain_complex\n    Please report this bug!  You may be the first\n    person in the world to have seen this problem.\n    Please include this random seed in your bug report:\n    Random seed: 34394830719288133598462639118695428033\n    ValueError()\n**********************************************************************\nFile \"/Volumes/E/sage-4.6.rc0/devel/sage/sage/homology/tests.py\", line 11:\n    sage: test_random_chain_complex(level=2, trials=20)  # optional - CHomP\nExpected nothing\nGot:\n    Homology in dimension -32 according to CHomP: Z^24\n    Homology in dimension -32 according to Sage: Z^24\n    Chain complex: {-32: [-26  -3 724   0   0  -9  -2   1  -1  -5   1   1   0  -2   0   8  15   1  -1   0   2  -1   2  -1 132   1   0]\n    [ -6   2  -1   0 -10  -2   1   1   4   1   0  -1  -3   0 266   5   0  -1  10  -1  -2  -1   1   1  -2   1  -1]\n    [  1   5  -2  -1   2   1   1   1  -7  -1 -12   0  -2  -1   0  -2   1   1  32  -4   0   2   8  -1  -6   1   0], -33: []}\n    Random testing has revealed a problem in test_random_chain_complex\n    Please report this bug!  You may be the first\n    person in the world to have seen this problem.\n    Please include this random seed in your bug report:\n    Random seed: 27072195692990853427961476841312173568\n    ValueError()\n**********************************************************************\nFile \"/Volumes/E/sage-4.6.rc0/devel/sage/sage/homology/tests.py\", line 12:\n    sage: test_random_chain_complex(level=4, trials=20)  # long time # optional - CHomP\nExpected nothing\nGot:\n    Homology in dimension -32 according to CHomP: 0\n    Homology in dimension -32 according to Sage: 0\n    Chain complex: {-32: 0 x 59 dense matrix over Integer Ring, -33: 59 x 108 dense matrix over Integer Ring}\n    Random testing has revealed a problem in test_random_chain_complex\n    Please report this bug!  You may be the first\n    person in the world to have seen this problem.\n    Please include this random seed in your bug report:\n    Random seed: 87149713787488187057113721275525857721\n    ValueError()\n**********************************************************************\nFile \"/Volumes/E/sage-4.6.rc0/devel/sage/sage/homology/tests.py\", line 72:\n    sage: test_random_chain_complex(trials=2)  # optional - CHomP\nExpected nothing\nGot:\n    Homology in dimension 17 according to CHomP: Z^6\n    Homology in dimension 17 according to Sage: Z^6\n    Chain complex: {17: [ -1 -10 -38   6   0   0  -2   3  -1]\n    [ -2   0   2  -1  -1   1  -1   0   1]\n    [ -4  -1   1   8   0  -2  -6   1   2], 18: []}\n    Random testing has revealed a problem in test_random_chain_complex\n    Please report this bug!  You may be the first\n    person in the world to have seen this problem.\n    Please include this random seed in your bug report:\n    Random seed: 133823518449144789725728141987438003198\n    ValueError()\n**********************************************************************\n```",
    "created_at": "2010-10-27T16:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9941#issuecomment-98826",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

On OS X 10.6, cell_complex passes all tests (with the same options as above), but I do get:


```
sage -t -long -only-optional=chomp "devel/sage/sage/homology/tests.py"
**********************************************************************
File "/Volumes/E/sage-4.6.rc0/devel/sage/sage/homology/tests.py", line 10:
    sage: test_random_chain_complex(trials=20)  # optional - CHomP
Expected nothing
Got:
    Homology in dimension 20 according to CHomP: Z^16
    Homology in dimension 20 according to Sage: Z^16
    Chain complex: {20: 34 x 50 sparse matrix over Integer Ring, 21: []}
    Random testing has revealed a problem in test_random_chain_complex
    Please report this bug!  You may be the first
    person in the world to have seen this problem.
    Please include this random seed in your bug report:
    Random seed: 34394830719288133598462639118695428033
    ValueError()
**********************************************************************
File "/Volumes/E/sage-4.6.rc0/devel/sage/sage/homology/tests.py", line 11:
    sage: test_random_chain_complex(level=2, trials=20)  # optional - CHomP
Expected nothing
Got:
    Homology in dimension -32 according to CHomP: Z^24
    Homology in dimension -32 according to Sage: Z^24
    Chain complex: {-32: [-26  -3 724   0   0  -9  -2   1  -1  -5   1   1   0  -2   0   8  15   1  -1   0   2  -1   2  -1 132   1   0]
    [ -6   2  -1   0 -10  -2   1   1   4   1   0  -1  -3   0 266   5   0  -1  10  -1  -2  -1   1   1  -2   1  -1]
    [  1   5  -2  -1   2   1   1   1  -7  -1 -12   0  -2  -1   0  -2   1   1  32  -4   0   2   8  -1  -6   1   0], -33: []}
    Random testing has revealed a problem in test_random_chain_complex
    Please report this bug!  You may be the first
    person in the world to have seen this problem.
    Please include this random seed in your bug report:
    Random seed: 27072195692990853427961476841312173568
    ValueError()
**********************************************************************
File "/Volumes/E/sage-4.6.rc0/devel/sage/sage/homology/tests.py", line 12:
    sage: test_random_chain_complex(level=4, trials=20)  # long time # optional - CHomP
Expected nothing
Got:
    Homology in dimension -32 according to CHomP: 0
    Homology in dimension -32 according to Sage: 0
    Chain complex: {-32: 0 x 59 dense matrix over Integer Ring, -33: 59 x 108 dense matrix over Integer Ring}
    Random testing has revealed a problem in test_random_chain_complex
    Please report this bug!  You may be the first
    person in the world to have seen this problem.
    Please include this random seed in your bug report:
    Random seed: 87149713787488187057113721275525857721
    ValueError()
**********************************************************************
File "/Volumes/E/sage-4.6.rc0/devel/sage/sage/homology/tests.py", line 72:
    sage: test_random_chain_complex(trials=2)  # optional - CHomP
Expected nothing
Got:
    Homology in dimension 17 according to CHomP: Z^6
    Homology in dimension 17 according to Sage: Z^6
    Chain complex: {17: [ -1 -10 -38   6   0   0  -2   3  -1]
    [ -2   0   2  -1  -1   1  -1   0   1]
    [ -4  -1   1   8   0  -2  -6   1   2], 18: []}
    Random testing has revealed a problem in test_random_chain_complex
    Please report this bug!  You may be the first
    person in the world to have seen this problem.
    Please include this random seed in your bug report:
    Random seed: 133823518449144789725728141987438003198
    ValueError()
**********************************************************************
```



---

archive/issue_comments_098827.json:
```json
{
    "body": "Hi Marshall,\n\nI think you're seeing the problem reported on #9940: equality (or inequality?) testing for abelian groups is broken.",
    "created_at": "2010-10-27T17:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9941#issuecomment-98827",
    "user": "https://github.com/jhpalmieri"
}
```

Hi Marshall,

I think you're seeing the problem reported on #9940: equality (or inequality?) testing for abelian groups is broken.



---

archive/issue_comments_098828.json:
```json
{
    "body": "I see this failure on various linux machines (sage.math and the skynet machines eno, flavius, lena, sextus, taurus).  The tests seem to pass on OS X and Solaris (fulvia) and OpenSolaris (hawk).  With the attached patch, it passes on all of these machines.",
    "created_at": "2010-11-20T06:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9941#issuecomment-98828",
    "user": "https://github.com/jhpalmieri"
}
```

I see this failure on various linux machines (sage.math and the skynet machines eno, flavius, lena, sextus, taurus).  The tests seem to pass on OS X and Solaris (fulvia) and OpenSolaris (hawk).  With the attached patch, it passes on all of these machines.



---

archive/issue_comments_098829.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-20T06:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9941#issuecomment-98829",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098830.json:
```json
{
    "body": "> The tests seem to pass on OS X and Solaris (fulvia) and OpenSolaris \n\n\n(By \"seem to pass\", I mean that they pass on all of the machines on which I've tested them, but I can't guarantee that they would pass on all Solaris and/or OpenSolaris boxes.)",
    "created_at": "2010-11-20T06:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9941#issuecomment-98830",
    "user": "https://github.com/jhpalmieri"
}
```

> The tests seem to pass on OS X and Solaris (fulvia) and OpenSolaris 


(By "seem to pass", I mean that they pass on all of the machines on which I've tested them, but I can't guarantee that they would pass on all Solaris and/or OpenSolaris boxes.)



---

archive/issue_comments_098831.json:
```json
{
    "body": "I've been doing some more testing of CHomP-related doctests and have found a few more failures of this same type: on some platforms, one generator is chosen, and other platforms a different (but mathematically valid) generator is chosen.  I've fixed these in the new patch.  Also, the file `sage/homology/tests.py` takes too long to test on some platforms (with `-long -only-optional=chomp`), so I've shortened the tests there.",
    "created_at": "2010-12-15T21:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9941#issuecomment-98831",
    "user": "https://github.com/jhpalmieri"
}
```

I've been doing some more testing of CHomP-related doctests and have found a few more failures of this same type: on some platforms, one generator is chosen, and other platforms a different (but mathematically valid) generator is chosen.  I've fixed these in the new patch.  Also, the file `sage/homology/tests.py` takes too long to test on some platforms (with `-long -only-optional=chomp`), so I've shortened the tests there.



---

archive/issue_comments_098832.json:
```json
{
    "body": "Attachment [trac_9942-chomp.patch](tarball://root/attachments/some-uuid/ticket9942/trac_9942-chomp.patch) by mhampton created at 2011-01-11 00:24:38\n\nLooks good and all tests pass on OS X 10.5, 10.6, and linux (64-bit Ubuntu 10.04, intel i7 860).  So I think I can give this a positive review.",
    "created_at": "2011-01-11T00:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9941#issuecomment-98832",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_9942-chomp.patch](tarball://root/attachments/some-uuid/ticket9942/trac_9942-chomp.patch) by mhampton created at 2011-01-11 00:24:38

Looks good and all tests pass on OS X 10.5, 10.6, and linux (64-bit Ubuntu 10.04, intel i7 860).  So I think I can give this a positive review.



---

archive/issue_comments_098833.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-11T00:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9941#issuecomment-98833",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_025075.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-11T06:02:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9941",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9941#event-25075"
}
```



---

archive/issue_events_025076.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-19T22:22:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9941",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9941#event-25076"
}
```



---

archive/issue_comments_098834.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9941#issuecomment-98834",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
