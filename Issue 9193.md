# Issue 9193: Proveable computation of L-functions

archive/issues_009193.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @rishikesha @jbalakrishnan\n\nThis is related to #4475.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9193\n\n",
    "created_at": "2010-06-09T05:42:19Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Proveable computation of L-functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9193",
    "user": "@robertwb"
}
```
Assignee: @williamstein

CC:  @rishikesha @jbalakrishnan

This is related to #4475.

Issue created by migration from https://trac.sagemath.org/ticket/9193





---

archive/issue_comments_086009.json:
```json
{
    "body": "Attachment [9193-part1-lfunc.patch](tarball://root/attachments/some-uuid/ticket9193/9193-part1-lfunc.patch) by @robertwb created at 2010-06-09 06:13:46",
    "created_at": "2010-06-09T06:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86009",
    "user": "@robertwb"
}
```

Attachment [9193-part1-lfunc.patch](tarball://root/attachments/some-uuid/ticket9193/9193-part1-lfunc.patch) by @robertwb created at 2010-06-09 06:13:46



---

archive/issue_comments_086010.json:
```json
{
    "body": "Attachment [9193-part2-incomplete-gamma.patch](tarball://root/attachments/some-uuid/ticket9193/9193-part2-incomplete-gamma.patch) by @robertwb created at 2010-06-09 06:14:39",
    "created_at": "2010-06-09T06:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86010",
    "user": "@robertwb"
}
```

Attachment [9193-part2-incomplete-gamma.patch](tarball://root/attachments/some-uuid/ticket9193/9193-part2-incomplete-gamma.patch) by @robertwb created at 2010-06-09 06:14:39



---

archive/issue_comments_086011.json:
```json
{
    "body": "Attachment [9193-part3-prec.patch](tarball://root/attachments/some-uuid/ticket9193/9193-part3-prec.patch) by @robertwb created at 2010-06-09 06:14:50",
    "created_at": "2010-06-09T06:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86011",
    "user": "@robertwb"
}
```

Attachment [9193-part3-prec.patch](tarball://root/attachments/some-uuid/ticket9193/9193-part3-prec.patch) by @robertwb created at 2010-06-09 06:14:50



---

archive/issue_comments_086012.json:
```json
{
    "body": "Depends on #9165, #9184, #9180.",
    "created_at": "2010-06-09T06:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86012",
    "user": "@robertwb"
}
```

Depends on #9165, #9184, #9180.



---

archive/issue_comments_086013.json:
```json
{
    "body": "Why do you write above that this \"Depends on #9165\"?  There is no code there, and that is related to the Cygwin port?",
    "created_at": "2010-07-08T14:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86013",
    "user": "@williamstein"
}
```

Why do you write above that this "Depends on #9165"?  There is no code there, and that is related to the Cygwin port?



---

archive/issue_comments_086014.json:
```json
{
    "body": "The dependency should have been #9156 (which is a tiny, now merged, ticket) rather than #9165. \n\nThis still needs work in two ways. Firstly, it needs more doctests/documentation (though most of the important/tricky functions are already done), and there is also a bug in computing the tail of the G-function summation that I'm still tracking down. I did some work towards this during Sage Days 22, and even thought about it a touch this week, but haven't quite gotten to the bottom of it. \n\n\n```\n$ sage -coverage sage/lfunctions/lfunction.py \n----------------------------------------------------------------------\nsage/lfunctions/lfunction.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE sage/lfunctions/lfunction.py: 61% (19 of 31)\n\n$ sage -coverage sage/lfunctions/G_function.py \n----------------------------------------------------------------------\nsage/lfunctions/G_function.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE sage/lfunctions/G_function.py: 59% (13 of 22)\n```\n",
    "created_at": "2010-07-08T16:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86014",
    "user": "@robertwb"
}
```

The dependency should have been #9156 (which is a tiny, now merged, ticket) rather than #9165. 

This still needs work in two ways. Firstly, it needs more doctests/documentation (though most of the important/tricky functions are already done), and there is also a bug in computing the tail of the G-function summation that I'm still tracking down. I did some work towards this during Sage Days 22, and even thought about it a touch this week, but haven't quite gotten to the bottom of it. 


```
$ sage -coverage sage/lfunctions/lfunction.py 
----------------------------------------------------------------------
sage/lfunctions/lfunction.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE sage/lfunctions/lfunction.py: 61% (19 of 31)

$ sage -coverage sage/lfunctions/G_function.py 
----------------------------------------------------------------------
sage/lfunctions/G_function.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE sage/lfunctions/G_function.py: 59% (13 of 22)
```




---

archive/issue_comments_086015.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-08T16:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86015",
    "user": "@robertwb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_086016.json:
```json
{
    "body": "This is done except for doctests on some functions (though it could use some optimisations too).",
    "created_at": "2011-03-27T05:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86016",
    "user": "@robertwb"
}
```

This is done except for doctests on some functions (though it could use some optimisations too).



---

archive/issue_comments_086017.json:
```json
{
    "body": "(I just rebased this with Robert for sage-4.7.2.alpha2.)",
    "created_at": "2011-08-25T06:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86017",
    "user": "@williamstein"
}
```

(I just rebased this with Robert for sage-4.7.2.alpha2.)



---

archive/issue_comments_086018.json:
```json
{
    "body": "Attachment [9193-part4-proveable.patch](tarball://root/attachments/some-uuid/ticket9193/9193-part4-proveable.patch) by @williamstein created at 2011-08-25 06:58:42\n\nAll patches apply (with a minor rebase) and mostly work.  However, there is one bug. \n\n\n```\nUnfortunately, this is wrong, since the coefficients of 1 and T have\nto be 0.0000?.  However, the output *is* correct to 10 bits of\nprecision, so the correct fix is just to truncate.::\n\n    sage: L = LFunction(EllipticCurve('389a'))\n    sage: L.taylor_series(RealField(10)(1), 3, proof=True)\n    -0.00002125? + 0.00001204?*T + 0.75933?*T^2 - 0.43032?*T^3 + O(T^4)\n```\n",
    "created_at": "2011-08-25T06:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86018",
    "user": "@williamstein"
}
```

Attachment [9193-part4-proveable.patch](tarball://root/attachments/some-uuid/ticket9193/9193-part4-proveable.patch) by @williamstein created at 2011-08-25 06:58:42

All patches apply (with a minor rebase) and mostly work.  However, there is one bug. 


```
Unfortunately, this is wrong, since the coefficients of 1 and T have
to be 0.0000?.  However, the output *is* correct to 10 bits of
precision, so the correct fix is just to truncate.::

    sage: L = LFunction(EllipticCurve('389a'))
    sage: L.taylor_series(RealField(10)(1), 3, proof=True)
    -0.00002125? + 0.00001204?*T + 0.75933?*T^2 - 0.43032?*T^3 + O(T^4)
```




---

archive/issue_comments_086019.json:
```json
{
    "body": "(slightly updated)",
    "created_at": "2011-08-25T07:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86019",
    "user": "@williamstein"
}
```

(slightly updated)



---

archive/issue_comments_086020.json:
```json
{
    "body": "Attachment [9193-part5-docstrings-and-prec-fix.patch](tarball://root/attachments/some-uuid/ticket9193/9193-part5-docstrings-and-prec-fix.patch) by @jdemeyer created at 2013-08-13 15:35:53",
    "created_at": "2013-08-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9193#issuecomment-86020",
    "user": "@jdemeyer"
}
```

Attachment [9193-part5-docstrings-and-prec-fix.patch](tarball://root/attachments/some-uuid/ticket9193/9193-part5-docstrings-and-prec-fix.patch) by @jdemeyer created at 2013-08-13 15:35:53
