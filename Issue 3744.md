# Issue 3744: Coercion between isomorphic parents should result in an element of the left operand's parent

archive/issues_003744.json:
```json
{
    "body": "Assignee: robertwb\n\nThis is in accordance with the programming guide. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3744\n\n",
    "created_at": "2008-07-30T05:00:58Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "title": "Coercion between isomorphic parents should result in an element of the left operand's parent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3744",
    "user": "robertwb"
}
```
Assignee: robertwb

This is in accordance with the programming guide. 

Issue created by migration from https://trac.sagemath.org/ticket/3744





---

archive/issue_comments_026587.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-30T05:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26587",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_026588.json:
```json
{
    "body": "This patch does not apply cleanly to 3.1.alpha0:\n\n```\nsage: hg_sage.apply (\"/home/john/3744-coercion-left.patch\")\ncd \"/home/john/tmp/sage-3.1.alpha0/devel/sage\" && hg status\ncd \"/home/john/tmp/sage-3.1.alpha0/devel/sage\" && hg status\ncd \"/home/john/tmp/sage-3.1.alpha0/devel/sage\" && hg import   \"/home/john/3744-coercion-left.patch\"\napplying /home/john/3744-coercion-left.patch\npatching file sage/structure/coerce.pyx\nHunk #1 FAILED at 737\nHunk #2 FAILED at 754\n2 out of 2 hunks FAILED -- saving rejects to file sage/structure/coerce.pyx.rej\nabort: patch failed to apply\n```\n\n\nI'm not sure how it fits in with the main coercion model patches though.",
    "created_at": "2008-08-10T10:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26588",
    "user": "cremona"
}
```

This patch does not apply cleanly to 3.1.alpha0:

```
sage: hg_sage.apply ("/home/john/3744-coercion-left.patch")
cd "/home/john/tmp/sage-3.1.alpha0/devel/sage" && hg status
cd "/home/john/tmp/sage-3.1.alpha0/devel/sage" && hg status
cd "/home/john/tmp/sage-3.1.alpha0/devel/sage" && hg import   "/home/john/3744-coercion-left.patch"
applying /home/john/3744-coercion-left.patch
patching file sage/structure/coerce.pyx
Hunk #1 FAILED at 737
Hunk #2 FAILED at 754
2 out of 2 hunks FAILED -- saving rejects to file sage/structure/coerce.pyx.rej
abort: patch failed to apply
```


I'm not sure how it fits in with the main coercion model patches though.



---

archive/issue_comments_026589.json:
```json
{
    "body": "Let's wait until #3738 gets in.",
    "created_at": "2008-08-11T16:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26589",
    "user": "robertwb"
}
```

Let's wait until #3738 gets in.



---

archive/issue_comments_026590.json:
```json
{
    "body": "Still does not apply cleanly to 3.1.alpha2:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: 3744\nsage: hg_sage.apply(\"/home/john/3744-coercion-left.patch\")\ncd \"/home/john/sage-3.1.alpha2/devel/sage\" && hg status\ncd \"/home/john/sage-3.1.alpha2/devel/sage\" && hg status\ncd \"/home/john/sage-3.1.alpha2/devel/sage\" && hg import   \"/home/john/3744-coercion-left.patch\"\napplying /home/john/3744-coercion-left.patch\npatching file sage/structure/coerce.pyx\nHunk #1 succeeded at 845 with fuzz 2 (offset 105 lines).\nHunk #2 FAILED at 780\n1 out of 2 hunks FAILED -- saving rejects to file sage/structure/coerce.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2008-08-14T20:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26590",
    "user": "cremona"
}
```

Still does not apply cleanly to 3.1.alpha2:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: 3744
sage: hg_sage.apply("/home/john/3744-coercion-left.patch")
cd "/home/john/sage-3.1.alpha2/devel/sage" && hg status
cd "/home/john/sage-3.1.alpha2/devel/sage" && hg status
cd "/home/john/sage-3.1.alpha2/devel/sage" && hg import   "/home/john/3744-coercion-left.patch"
applying /home/john/3744-coercion-left.patch
patching file sage/structure/coerce.pyx
Hunk #1 succeeded at 845 with fuzz 2 (offset 105 lines).
Hunk #2 FAILED at 780
1 out of 2 hunks FAILED -- saving rejects to file sage/structure/coerce.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_026591.json:
```json
{
    "body": "This is actually in 3.1.alpha2 and has been reviewed via #3738, so I am giving this a positive reivew.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-14T23:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26591",
    "user": "mabshoff"
}
```

This is actually in 3.1.alpha2 and has been reviewed via #3738, so I am giving this a positive reivew.

Cheers,

Michael



---

archive/issue_comments_026592.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-14T23:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26592",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026593.json:
```json
{
    "body": "Merged in Sage 3.1.alpha2",
    "created_at": "2008-08-14T23:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26593",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha2



---

archive/issue_comments_026594.json:
```json
{
    "body": "Well, I really ought to change the subject, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-14T23:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26594",
    "user": "mabshoff"
}
```

Well, I really ought to change the subject, too.

Cheers,

Michael
