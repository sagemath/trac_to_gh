# Issue 4591: magma -- EllipticCurve('37a').three_selmer_rank() fails in Magma 2.14

archive/issues_004591.json:
```json
{
    "body": "Assignee: was\n\nIn Magma 2.13 this works:\n\n```\nEllipticCurve('37a').three_selmer_rank()\n```\n\nbut in Magma 2.14 it doesn't (tested on osx and linux):\n\n```\nsage: EllipticCurve('37a').three_selmer_rank()\n```\n\n\nThis is implemented by a script I ship that is a modified versin of a magma script.\nI thus need to fix this.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/4591\n\n",
    "created_at": "2008-11-23T04:22:13Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "magma -- EllipticCurve('37a').three_selmer_rank() fails in Magma 2.14",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4591",
    "user": "was"
}
```
Assignee: was

In Magma 2.13 this works:

```
EllipticCurve('37a').three_selmer_rank()
```

but in Magma 2.14 it doesn't (tested on osx and linux):

```
sage: EllipticCurve('37a').three_selmer_rank()
```


This is implemented by a script I ship that is a modified versin of a magma script.
I thus need to fix this.  

Issue created by migration from https://trac.sagemath.org/ticket/4591





---

archive/issue_comments_034431.json:
```json
{
    "body": "this totally fixes the problem, and is much simpler and better doctested code.  it also is much faster and works with both magma 2.13 and 2.14.",
    "created_at": "2008-11-23T07:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4591#issuecomment-34431",
    "user": "was"
}
```

this totally fixes the problem, and is much simpler and better doctested code.  it also is much faster and works with both magma 2.13 and 2.14.



---

archive/issue_comments_034432.json:
```json
{
    "body": "Attachment [sage-4591.patch](tarball://root/attachments/some-uuid/ticket4591/sage-4591.patch) by was created at 2008-11-23 07:34:38",
    "created_at": "2008-11-23T07:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4591#issuecomment-34432",
    "user": "was"
}
```

Attachment [sage-4591.patch](tarball://root/attachments/some-uuid/ticket4591/sage-4591.patch) by was created at 2008-11-23 07:34:38



---

archive/issue_comments_034433.json:
```json
{
    "body": "it is very important to delete the whole directory data/extcode/magma/stoll, even if hg doesn't do that.  check it!",
    "created_at": "2008-11-23T07:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4591#issuecomment-34433",
    "user": "was"
}
```

it is very important to delete the whole directory data/extcode/magma/stoll, even if hg doesn't do that.  check it!



---

archive/issue_comments_034434.json:
```json
{
    "body": "Attachment [extcode-4591.patch](tarball://root/attachments/some-uuid/ticket4591/extcode-4591.patch) by mabshoff created at 2008-11-23 07:55:24\n\nPositive review. wstein explained the reasons behind the switch to Magma code in detail, so I am happy.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T07:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4591#issuecomment-34434",
    "user": "mabshoff"
}
```

Attachment [extcode-4591.patch](tarball://root/attachments/some-uuid/ticket4591/extcode-4591.patch) by mabshoff created at 2008-11-23 07:55:24

Positive review. wstein explained the reasons behind the switch to Magma code in detail, so I am happy.

Cheers,

Michael



---

archive/issue_comments_034435.json:
```json
{
    "body": "Unfortunately there are slight reject issues:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage$ patch -p1 --dry-run < trac_4591_sage-4591.patch \npatching file sage/interfaces/magma.py\nHunk #1 FAILED at 744.\n1 out of 1 hunk FAILED -- saving rejects to file sage/interfaces/magma.py.rej\npatching file sage/schemes/elliptic_curves/ell_rational_field.py\npatching file sage/schemes/elliptic_curves/magma_3descent.py\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T08:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4591#issuecomment-34435",
    "user": "mabshoff"
}
```

Unfortunately there are slight reject issues:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage$ patch -p1 --dry-run < trac_4591_sage-4591.patch 
patching file sage/interfaces/magma.py
Hunk #1 FAILED at 744.
1 out of 1 hunk FAILED -- saving rejects to file sage/interfaces/magma.py.rej
patching file sage/schemes/elliptic_curves/ell_rational_field.py
patching file sage/schemes/elliptic_curves/magma_3descent.py
```


Cheers,

Michael



---

archive/issue_comments_034436.json:
```json
{
    "body": "Attachment [sage-4591.2.patch](tarball://root/attachments/some-uuid/ticket4591/sage-4591.2.patch) by was created at 2008-11-23 08:16:06\n\nrebased version.",
    "created_at": "2008-11-23T08:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4591#issuecomment-34436",
    "user": "was"
}
```

Attachment [sage-4591.2.patch](tarball://root/attachments/some-uuid/ticket4591/sage-4591.2.patch) by was created at 2008-11-23 08:16:06

rebased version.



---

archive/issue_comments_034437.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-23T08:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4591#issuecomment-34437",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034438.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-23T08:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4591#issuecomment-34438",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha0
