# Issue 5495: [with patch, positive review] fix typo in error: "A mysterious error (perphaps a memory error?)"   *PERP*HAPS!!!

archive/issues_005495.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nThere is a typo in the error message below (not a \"perp\"haps):\n\n```\nwstein@debian32:/space/wstein/farm/sage-3.4/devel/sage/sage/matrix$ sage -t matrix2.pyx\nsage -t  \"devel/sage-main/sage/matrix/matrix2.pyx\"          \n*** glibc detected *** double free or corruption (fasttop): 0x0a41a380 ***\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n [2.4 s]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5495\n\n",
    "closed_at": "2009-03-26T23:02:52Z",
    "created_at": "2009-03-12T02:38:25Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] fix typo in error: \"A mysterious error (perphaps a memory error?)\"   *PERP*HAPS!!!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5495",
    "user": "https://github.com/williamstein"
}
```
Assignee: @jhpalmieri

There is a typo in the error message below (not a "perp"haps):

```
wstein@debian32:/space/wstein/farm/sage-3.4/devel/sage/sage/matrix$ sage -t matrix2.pyx
sage -t  "devel/sage-main/sage/matrix/matrix2.pyx"          
*** glibc detected *** double free or corruption (fasttop): 0x0a41a380 ***
A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
 [2.4 s]
```

Issue created by migration from https://trac.sagemath.org/ticket/5495





---

archive/issue_comments_042591.json:
```json
{
    "body": "Trivial patch.",
    "created_at": "2009-03-22T22:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42591",
    "user": "https://github.com/jhpalmieri"
}
```

Trivial patch.



---

archive/issue_comments_042592.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-22T22:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42592",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042593.json:
```json
{
    "body": "Changing assignee from cwitty to @jhpalmieri.",
    "created_at": "2009-03-22T22:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42593",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from cwitty to @jhpalmieri.



---

archive/issue_comments_042594.json:
```json
{
    "body": "Attachment [5495.patch](tarball://root/attachments/some-uuid/ticket5495/5495.patch) by @jhpalmieri created at 2009-03-22 22:12:33",
    "created_at": "2009-03-22T22:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42594",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [5495.patch](tarball://root/attachments/some-uuid/ticket5495/5495.patch) by @jhpalmieri created at 2009-03-22 22:12:33



---

archive/issue_comments_042595.json:
```json
{
    "body": "The patch **5495.patch** fails to apply at all against Sage 3.4:\n\n```\nsage: hg_sage.apply(\"/home/mvngu/patch/5495/5495.patch\")\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg status\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg status\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg import   \"/home/mvngu/patch/5495/5495.patch\"\napplying /home/mvngu/patch/5495/5495.patch\nunable to find 'sage-doctest' for patching\n1 out of 1 hunks FAILED -- saving rejects to file sage-doctest.rej\nabort: patch failed to apply\n```",
    "created_at": "2009-03-24T08:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42595",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch **5495.patch** fails to apply at all against Sage 3.4:

```
sage: hg_sage.apply("/home/mvngu/patch/5495/5495.patch")
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg import   "/home/mvngu/patch/5495/5495.patch"
applying /home/mvngu/patch/5495/5495.patch
unable to find 'sage-doctest' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage-doctest.rej
abort: patch failed to apply
```



---

archive/issue_comments_042596.json:
```json
{
    "body": "Try using \"hg_scripts\" instead of \"hg_sage\".",
    "created_at": "2009-03-24T15:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42596",
    "user": "https://github.com/jhpalmieri"
}
```

Try using "hg_scripts" instead of "hg_sage".



---

archive/issue_comments_042597.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> Try using \"hg_scripts\" instead of \"hg_sage\".\n\n\n\nYep, it now applies OK against Sage 3.4. Looks good, and I doctested `sage/matrix/matrix2.pyx` hoping to get a similar error as reported above. But no \"mysterious error\" popped up. Anyway, positive review for the typo fix.",
    "created_at": "2009-03-26T07:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42597",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:4 jhpalmieri]:
> Try using "hg_scripts" instead of "hg_sage".



Yep, it now applies OK against Sage 3.4. Looks good, and I doctested `sage/matrix/matrix2.pyx` hoping to get a similar error as reported above. But no "mysterious error" popped up. Anyway, positive review for the typo fix.



---

archive/issue_comments_042598.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T23:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42598",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_042599.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-26T23:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42599",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012860.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-26T23:02:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5495#event-12860"
}
```
