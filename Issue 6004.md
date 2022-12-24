# Issue 6004: [with patch, needs review] add odd_degree_model function to hyperelliptic curves

archive/issues_006004.json:
```json
{
    "body": "Assignee: was\n\nKeywords: odd degree model hyperelliptic curves\n\nPatch says it best.  Very simple but I need this all the time.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6004\n\n",
    "created_at": "2009-05-07T20:37:05Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] add odd_degree_model function to hyperelliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6004",
    "user": "ncalexan"
}
```
Assignee: was

Keywords: odd degree model hyperelliptic curves

Patch says it best.  Very simple but I need this all the time.

Issue created by migration from https://trac.sagemath.org/ticket/6004





---

archive/issue_comments_047764.json:
```json
{
    "body": "Positive review pending patch 2 having \"Return an odd degree model of self, or None if one does not exist over the field of definition. \" changed to something that mentions that a ValueError is raised if no model exists.\n\nWilliam",
    "created_at": "2009-05-07T20:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6004#issuecomment-47764",
    "user": "was"
}
```

Positive review pending patch 2 having "Return an odd degree model of self, or None if one does not exist over the field of definition. " changed to something that mentions that a ValueError is raised if no model exists.

William



---

archive/issue_comments_047765.json:
```json
{
    "body": "ok, genuine positive review.",
    "created_at": "2009-05-07T21:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6004#issuecomment-47765",
    "user": "was"
}
```

ok, genuine positive review.



---

archive/issue_comments_047766.json:
```json
{
    "body": "Attachment [trac_6004-odd-degree-model-5.patch](tarball://root/attachments/some-uuid/ticket6004/trac_6004-odd-degree-model-5.patch) by ncalexan created at 2009-05-07 22:50:02",
    "created_at": "2009-05-07T22:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6004#issuecomment-47766",
    "user": "ncalexan"
}
```

Attachment [trac_6004-odd-degree-model-5.patch](tarball://root/attachments/some-uuid/ticket6004/trac_6004-odd-degree-model-5.patch) by ncalexan created at 2009-05-07 22:50:02



---

archive/issue_comments_047767.json:
```json
{
    "body": "Only apply `trac_6004-odd-degree-model-5.patch`.  All others could be deleted.",
    "created_at": "2009-05-07T22:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6004#issuecomment-47767",
    "user": "ncalexan"
}
```

Only apply `trac_6004-odd-degree-model-5.patch`.  All others could be deleted.



---

archive/issue_comments_047768.json:
```json
{
    "body": "Hmm, this needs a rebase:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-4.0.alpha0/devel/sage$ hg import trac_6004-odd-degree-model-5.patch \napplying trac_6004-odd-degree-model-5.patch\npatching file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py\nHunk #1 FAILED at 62\n1 out of 2 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py.rej\nabort: patch failed to apply\n```\n\nMost likely culprit is another patch by Nick:\n\n```\nchangeset:   12218:684af2b9657e\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Thu May 07 13:37:26 2009 -0700\nsummary:     [mq]: trac_6004-odd-degree-model.patch\n```\n\nMight this code already be in Sage via another patch?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T20:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6004#issuecomment-47768",
    "user": "mabshoff"
}
```

Hmm, this needs a rebase:

```
mabshoff@sage:/scratch/mabshoff/sage-4.0.alpha0/devel/sage$ hg import trac_6004-odd-degree-model-5.patch 
applying trac_6004-odd-degree-model-5.patch
patching file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py
Hunk #1 FAILED at 62
1 out of 2 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py.rej
abort: patch failed to apply
```

Most likely culprit is another patch by Nick:

```
changeset:   12218:684af2b9657e
user:        Nick Alexander <ncalexander@gmail.com>
date:        Thu May 07 13:37:26 2009 -0700
summary:     [mq]: trac_6004-odd-degree-model.patch
```

Might this code already be in Sage via another patch?

Cheers,

Michael



---

archive/issue_comments_047769.json:
```json
{
    "body": "Attachment [trac_6004-odd-degree-model-5.2.patch](tarball://root/attachments/some-uuid/ticket6004/trac_6004-odd-degree-model-5.2.patch) by ncalexan created at 2009-05-12 21:04:59",
    "created_at": "2009-05-12T21:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6004#issuecomment-47769",
    "user": "ncalexan"
}
```

Attachment [trac_6004-odd-degree-model-5.2.patch](tarball://root/attachments/some-uuid/ticket6004/trac_6004-odd-degree-model-5.2.patch) by ncalexan created at 2009-05-12 21:04:59



---

archive/issue_comments_047770.json:
```json
{
    "body": "Apply only second patch.  There were a few lines included in #6010 by accident.",
    "created_at": "2009-05-12T21:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6004#issuecomment-47770",
    "user": "ncalexan"
}
```

Apply only second patch.  There were a few lines included in #6010 by accident.



---

archive/issue_comments_047771.json:
```json
{
    "body": "Merged trac_6004-odd-degree-model-5.2.patch in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T21:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6004#issuecomment-47771",
    "user": "mabshoff"
}
```

Merged trac_6004-odd-degree-model-5.2.patch in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_047772.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T21:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6004#issuecomment-47772",
    "user": "mabshoff"
}
```

Resolution: fixed
