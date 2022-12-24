# Issue 5303: Sage 3.3.rc2: numerical noise in sage/schemes/elliptic_curves/sha_tate.py

archive/issues_005303.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @JohnCremona\n\n\n```\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/sha_tate.py\"\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.3.rc1/devel/sage/sage/schemes/elliptic_curves/sha_tate.py\", line 88:\n    sage: [sha.an_numerical(prec) for prec in xrange(30,100,10)] # long time\nExpected:\n    [1.0000000,\n    1.0000000000,\n    1.0000000000000,\n    1.0000000000000000,\n    1.0000000000000000000,\n    1.0000000000000000000000,\n    1.0000000000000000000000000]\nGot:\n    [0.99999969, 1.0000000000, 1.0000000000000, 1.0000000000000000, 1.0000000000000000000, 1.0000000000000000000000, 1.0000000000000000000000000]\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5303\n\n",
    "created_at": "2009-02-18T11:55:21Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Sage 3.3.rc2: numerical noise in sage/schemes/elliptic_curves/sha_tate.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5303",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  @JohnCremona


```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/sha_tate.py"
**********************************************************************
File "/Users/mabshoff/sage-3.3.rc1/devel/sage/sage/schemes/elliptic_curves/sha_tate.py", line 88:
    sage: [sha.an_numerical(prec) for prec in xrange(30,100,10)] # long time
Expected:
    [1.0000000,
    1.0000000000,
    1.0000000000000,
    1.0000000000000000,
    1.0000000000000000000,
    1.0000000000000000000000,
    1.0000000000000000000000000]
Got:
    [0.99999969, 1.0000000000, 1.0000000000000, 1.0000000000000000, 1.0000000000000000000, 1.0000000000000000000000, 1.0000000000000000000000000]
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/5303





---

archive/issue_comments_040796.json:
```json
{
    "body": "Hi John,\n\nthere are several suggestions on how to fix this:\n\n* start off with 40 bit of precision, but this might hide a bug\n* check if the value is within some eps of 1, the same comment about hiding a bug might apply here\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T10:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5303#issuecomment-40796",
    "user": "mabshoff"
}
```

Hi John,

there are several suggestions on how to fix this:

* start off with 40 bit of precision, but this might hide a bug
* check if the value is within some eps of 1, the same comment about hiding a bug might apply here

Thoughts?

Cheers,

Michael



---

archive/issue_comments_040797.json:
```json
{
    "body": "Attachment [trac_5303.patch](tarball://root/attachments/some-uuid/ticket5303/trac_5303.patch) by mabshoff created at 2009-02-20 18:16:49",
    "created_at": "2009-02-20T18:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5303#issuecomment-40797",
    "user": "mabshoff"
}
```

Attachment [trac_5303.patch](tarball://root/attachments/some-uuid/ticket5303/trac_5303.patch) by mabshoff created at 2009-02-20 18:16:49



---

archive/issue_comments_040798.json:
```json
{
    "body": "This patch avoids the computation for prec=30 and thus gets rid of the numerical problem. This might not be the right long term fix, but it is a good fix for 3.3.\n\nJohn: If you think that this should be reverted and fixed in some other way please open another ticket in case this got merged.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T18:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5303#issuecomment-40798",
    "user": "mabshoff"
}
```

This patch avoids the computation for prec=30 and thus gets rid of the numerical problem. This might not be the right long term fix, but it is a good fix for 3.3.

John: If you think that this should be reverted and fixed in some other way please open another ticket in case this got merged.

Cheers,

Michael



---

archive/issue_comments_040799.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-20T18:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5303#issuecomment-40799",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040800.json:
```json
{
    "body": "Replying to [comment:3 was]:\n\nI was not in time but this seems a reasonable compromise to me!",
    "created_at": "2009-02-20T19:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5303#issuecomment-40800",
    "user": "@JohnCremona"
}
```

Replying to [comment:3 was]:

I was not in time but this seems a reasonable compromise to me!



---

archive/issue_comments_040801.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T20:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5303#issuecomment-40801",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040802.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T20:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5303#issuecomment-40802",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael
