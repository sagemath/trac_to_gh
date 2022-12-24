# Issue 1029: update flint in sage again

archive/issues_001029.json:
```json
{
    "body": "Assignee: somebody\n\nFrom Bill Hart:\n\n\n```\nHi William,\n\nI've just dug another pile of bugs out of FLINT. All functions in\nfmpz_poly normalise correctly now (or at least they should).\n\nI ran a much more comprehensive set of tests, checking for unusual\ncorner cases. I found a handful of them and removed them.\n\nI've also added a make all to the makefile.\n\nFunctions still may not deal with length zero polynomials correctly\n(though most functions do) and with aliased inputs, so there will\nprobably be more changes over the next few days. But for now, FLINT is\nmuch more bulletproof than it was.\n```\n\n\nMoreover, the svn revision to get it: 1045\n\nIssue created by migration from https://trac.sagemath.org/ticket/1029\n\n",
    "created_at": "2007-10-29T05:39:31Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "update flint in sage again",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1029",
    "user": "@williamstein"
}
```
Assignee: somebody

From Bill Hart:


```
Hi William,

I've just dug another pile of bugs out of FLINT. All functions in
fmpz_poly normalise correctly now (or at least they should).

I ran a much more comprehensive set of tests, checking for unusual
corner cases. I found a handful of them and removed them.

I've also added a make all to the makefile.

Functions still may not deal with length zero polynomials correctly
(though most functions do) and with aliased inputs, so there will
probably be more changes over the next few days. But for now, FLINT is
much more bulletproof than it was.
```


Moreover, the svn revision to get it: 1045

Issue created by migration from https://trac.sagemath.org/ticket/1029





---

archive/issue_comments_006285.json:
```json
{
    "body": "Actually, update to 1047:\n\n```\nAs of revision 1047 all functions now deal correctly with length zero\nfunctions. I have also added some managed functions for scalar\nmultiplication of a polynomial by a scalar. I've also hardened some of\nthe memory management functions so that stupid users who try to\nallocate -1 limbs won't run into unexpected trouble.\n```\n",
    "created_at": "2007-10-29T19:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1029#issuecomment-6285",
    "user": "@williamstein"
}
```

Actually, update to 1047:

```
As of revision 1047 all functions now deal correctly with length zero
functions. I have also added some managed functions for scalar
multiplication of a polynomial by a scalar. I've also hardened some of
the memory management functions so that stupid users who try to
allocate -1 limbs won't run into unexpected trouble.
```




---

archive/issue_comments_006286.json:
```json
{
    "body": "Changing assignee from somebody to @williamstein.",
    "created_at": "2007-11-15T01:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1029#issuecomment-6286",
    "user": "@robertwb"
}
```

Changing assignee from somebody to @williamstein.



---

archive/issue_comments_006287.json:
```json
{
    "body": "Changing component from basic arithmetic to packages.",
    "created_at": "2007-11-15T01:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1029#issuecomment-6287",
    "user": "@robertwb"
}
```

Changing component from basic arithmetic to packages.



---

archive/issue_comments_006288.json:
```json
{
    "body": "New flint spkg and bundle (to apply to sage-main) up at\n\nhttp://sage.math.washington.edu/home/robertwb/flint/",
    "created_at": "2007-11-15T01:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1029#issuecomment-6288",
    "user": "@robertwb"
}
```

New flint spkg and bundle (to apply to sage-main) up at

http://sage.math.washington.edu/home/robertwb/flint/



---

archive/issue_comments_006289.json:
```json
{
    "body": "Ok, this should go into 2.8.13. I will ask for somebody to review this.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-15T15:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1029#issuecomment-6289",
    "user": "mabshoff"
}
```

Ok, this should go into 2.8.13. I will ask for somebody to review this.

Cheers,

Michael



---

archive/issue_comments_006290.json:
```json
{
    "body": "This looks good to me and should be in 2.8.13.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-18T10:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1029#issuecomment-6290",
    "user": "mabshoff"
}
```

This looks good to me and should be in 2.8.13.alpha0.

Cheers,

Michael



---

archive/issue_comments_006291.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-18T14:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1029#issuecomment-6291",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006292.json:
```json
{
    "body": "Merged in 2.8.13.alpha0.",
    "created_at": "2007-11-18T14:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1029#issuecomment-6292",
    "user": "mabshoff"
}
```

Merged in 2.8.13.alpha0.



---

archive/issue_comments_006293.json:
```json
{
    "body": "I fixed a ntl linking issue, so now there is a flint-0.9.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-11-18T21:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1029#issuecomment-6293",
    "user": "mabshoff"
}
```

I fixed a ntl linking issue, so now there is a flint-0.9.p0.spkg

Cheers,

Michael
