# Issue 5621: doctests for calculus.py

archive/issues_005621.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: doctest, calculus.py\n\nThe objective here is to add more doctests to the file `sage/calculus/calculus.py`, especially documentation for methods/functions that are exposed to readers via the reference manual.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5621\n\n",
    "created_at": "2009-03-28T03:55:27Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "doctests for calculus.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5621",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

Keywords: doctest, calculus.py

The objective here is to add more doctests to the file `sage/calculus/calculus.py`, especially documentation for methods/functions that are exposed to readers via the reference manual.

Issue created by migration from https://trac.sagemath.org/ticket/5621





---

archive/issue_comments_043807.json:
```json
{
    "body": "The patch `trac_5621-doctests-calculus.patch` adds doctests to 6 functions/methods in `sage/calculus/calculus.py`, raising the coverage of that module by 1% to 52%. Interestingly, with the command\n\n```\nsage -coverage\n```\n\nSage doesn't pick up doctests for functions/methods where there's a blank line between the docstring and the function/method. For example, as it now stands with Sage 3.4, the function `desolve_system_strings()` in the module `sage/calculus/desolvers.py` has doctests but Sage doesn't pick that up. Doing a doctest coverage on Sage 3.4 shows that the coverage for `sage/calculus/desolvers.py` is at 75%. But after removing the blank line between the function signature and its docstring, running the doctest coverage again shows that `sage/calculus/desolvers.py` has 87% coverage.",
    "created_at": "2009-03-28T04:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5621#issuecomment-43807",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch `trac_5621-doctests-calculus.patch` adds doctests to 6 functions/methods in `sage/calculus/calculus.py`, raising the coverage of that module by 1% to 52%. Interestingly, with the command

```
sage -coverage
```

Sage doesn't pick up doctests for functions/methods where there's a blank line between the docstring and the function/method. For example, as it now stands with Sage 3.4, the function `desolve_system_strings()` in the module `sage/calculus/desolvers.py` has doctests but Sage doesn't pick that up. Doing a doctest coverage on Sage 3.4 shows that the coverage for `sage/calculus/desolvers.py` is at 75%. But after removing the blank line between the function signature and its docstring, running the doctest coverage again shows that `sage/calculus/desolvers.py` has 87% coverage.



---

archive/issue_comments_043808.json:
```json
{
    "body": "This patch causes a few tiny doctest failures.  Can you fix them and post another patch:\n\n```\nsage -t  devel/sage/sage/calculus/calculus.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/calculus/calculus.py\", line 4921:\n    sage: var(\"x,y,z\");\nExpected nothing\nGot:\n    (x, y, z)\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/calculus/calculus.py\", line 4968:\n    sage: var(\"x,y,z\");\nExpected nothing\nGot:\n    (x, y, z)\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/calculus/calculus.py\", line 5537:\n    sage: var(\"a,b\");\nExpected nothing\nGot:\n    (a, b)\n**********************************************************************\n3 items had failures:\n   1 of   6 in __main__.example_119\n   1 of  12 in __main__.example_121\n   1 of   5 in __main__.example_138\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2-ref2/tmp/.doctest_calculus.py\n         [48.7 s]\n \n----------------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t  devel/sage/sage/calculus/calculus.py # 3 doctests failed\n```\n",
    "created_at": "2009-04-12T06:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5621#issuecomment-43808",
    "user": "https://github.com/williamstein"
}
```

This patch causes a few tiny doctest failures.  Can you fix them and post another patch:

```
sage -t  devel/sage/sage/calculus/calculus.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/calculus/calculus.py", line 4921:
    sage: var("x,y,z");
Expected nothing
Got:
    (x, y, z)
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/calculus/calculus.py", line 4968:
    sage: var("x,y,z");
Expected nothing
Got:
    (x, y, z)
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/calculus/calculus.py", line 5537:
    sage: var("a,b");
Expected nothing
Got:
    (a, b)
**********************************************************************
3 items had failures:
   1 of   6 in __main__.example_119
   1 of  12 in __main__.example_121
   1 of   5 in __main__.example_138
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2-ref2/tmp/.doctest_calculus.py
         [48.7 s]
 
----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage/sage/calculus/calculus.py # 3 doctests failed
```




---

archive/issue_comments_043809.json:
```json
{
    "body": "Attachment [trac_5621-doctests-calculus.patch](tarball://root/attachments/some-uuid/ticket5621/trac_5621-doctests-calculus.patch) by mvngu created at 2009-04-17 03:32:52\n\nbased on sage-3.4.1.rc3",
    "created_at": "2009-04-17T03:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5621#issuecomment-43809",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5621-doctests-calculus.patch](tarball://root/attachments/some-uuid/ticket5621/trac_5621-doctests-calculus.patch) by mvngu created at 2009-04-17 03:32:52

based on sage-3.4.1.rc3



---

archive/issue_comments_043810.json:
```json
{
    "body": "Replying to [comment:2 was]:\n> This patch causes a few tiny doctest failures.  Can you fix them and post another patch:\n\n\nYour wish is my command :-)  Please see the new patch, rebased against sage-3.4.1.rc3.",
    "created_at": "2009-04-17T03:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5621#issuecomment-43810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 was]:
> This patch causes a few tiny doctest failures.  Can you fix them and post another patch:


Your wish is my command :-)  Please see the new patch, rebased against sage-3.4.1.rc3.



---

archive/issue_comments_043811.json:
```json
{
    "body": "Looks good, all tests pass on sage.math.  There is a trivial typo, corrected in the referee's patch.",
    "created_at": "2009-05-10T22:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5621#issuecomment-43811",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good, all tests pass on sage.math.  There is a trivial typo, corrected in the referee's patch.



---

archive/issue_comments_043812.json:
```json
{
    "body": "Attachment [ref_5621.patch](tarball://root/attachments/some-uuid/ticket5621/ref_5621.patch) by mabshoff created at 2009-05-11 08:08:15\n\nGiven the pynac transformation I don't think it is a good idea to merge this now. calculus.py will be more or less gone before the end of the week anyway :).\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T08:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5621#issuecomment-43812",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [ref_5621.patch](tarball://root/attachments/some-uuid/ticket5621/ref_5621.patch) by mabshoff created at 2009-05-11 08:08:15

Given the pynac transformation I don't think it is a good idea to merge this now. calculus.py will be more or less gone before the end of the week anyway :).

Thoughts?

Cheers,

Michael



---

archive/issue_comments_043813.json:
```json
{
    "body": "I talked to Mike Hansen yesterday: The new doctests are going in via new symbolics - no point in creating merge issues when calculus is being more or less completely wiped out :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-13T18:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5621#issuecomment-43813",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I talked to Mike Hansen yesterday: The new doctests are going in via new symbolics - no point in creating merge issues when calculus is being more or less completely wiped out :)

Cheers,

Michael



---

archive/issue_events_013227.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-21T01:28:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5621",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5621#event-13227"
}
```



---

archive/issue_events_013228.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-21T01:28:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5621",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5621#event-13228"
}
```



---

archive/issue_comments_043814.json:
```json
{
    "body": "This has been merged via #5930 into the new symbolics.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T01:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5621#issuecomment-43814",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been merged via #5930 into the new symbolics.

Cheers,

Michael



---

archive/issue_comments_043815.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T01:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5621#issuecomment-43815",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
