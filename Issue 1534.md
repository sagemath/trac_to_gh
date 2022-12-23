# Issue 1534: Purge java3d from extcode

archive/issues_001534.json:
```json
{
    "body": "Assignee: was\n\nOnce #1533 is done, we need to remove the files from extcode. This should be done is such a way that the history of the (several MB) jar files is purged, I'm still looking for the best way to do this. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1534\n\n",
    "created_at": "2007-12-16T07:24:54Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "Purge java3d from extcode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1534",
    "user": "robertwb"
}
```
Assignee: was

Once #1533 is done, we need to remove the files from extcode. This should be done is such a way that the history of the (several MB) jar files is purged, I'm still looking for the best way to do this. 

Issue created by migration from https://trac.sagemath.org/ticket/1534





---

archive/issue_comments_009791.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2007-12-16T07:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9791",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_009792.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-16T07:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9792",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009793.json:
```json
{
    "body": "See http://www.selenic.com/pipermail/mercurial/2007-May/013256.html for some brief discussion of the question.  The answer seems to be to use \"hg clone -r\" and \"hg transplant\".\n\nBe sure to test \"sage -upgrade\" when you make this change.",
    "created_at": "2007-12-16T19:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9793",
    "user": "cwitty"
}
```

See http://www.selenic.com/pipermail/mercurial/2007-May/013256.html for some brief discussion of the question.  The answer seems to be to use "hg clone -r" and "hg transplant".

Be sure to test "sage -upgrade" when you make this change.



---

archive/issue_comments_009794.json:
```json
{
    "body": "Looks good. We need to make sure that if developers work on extcode they don't merge this stuff back in though.",
    "created_at": "2007-12-17T18:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9794",
    "user": "robertwb"
}
```

Looks good. We need to make sure that if developers work on extcode they don't merge this stuff back in though.



---

archive/issue_comments_009795.json:
```json
{
    "body": "I had lots of problems trying to use hg transplant, which just doesn't work for me.\n\ncwitty remarks: Looks like what we really want is http://www.selenic.com/pipermail/mercurial/2006-June/008878.html ; too bad it seems like nobody's touched it since mid-2006.",
    "created_at": "2008-01-19T18:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9795",
    "user": "was"
}
```

I had lots of problems trying to use hg transplant, which just doesn't work for me.

cwitty remarks: Looks like what we really want is http://www.selenic.com/pipermail/mercurial/2006-June/008878.html ; too bad it seems like nobody's touched it since mid-2006.



---

archive/issue_comments_009796.json:
```json
{
    "body": "Changing type from defect to task.",
    "created_at": "2010-03-17T05:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9796",
    "user": "jason"
}
```

Changing type from defect to task.



---

archive/issue_comments_009797.json:
```json
{
    "body": "There is no java3d in SAGE_EXTCODE.",
    "created_at": "2014-08-19T16:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9797",
    "user": "aapitzsch"
}
```

There is no java3d in SAGE_EXTCODE.



---

archive/issue_comments_009798.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-19T16:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9798",
    "user": "aapitzsch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_009799.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-08-26T19:24:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9799",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_009800.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-08-29T18:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9800",
    "user": "vbraun"
}
```

Resolution: fixed
