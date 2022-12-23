# Issue 5495: type: "A mysterious error (perphaps a memory error?)"   *PERP*HAPS!!!

archive/issues_005495.json:
```json
{
    "body": "Assignee: cwitty\n\nThere is a typo in the error message below (not a \"perp\"haps):\n\n\n```\nwstein@debian32:/space/wstein/farm/sage-3.4/devel/sage/sage/matrix$ sage -t matrix2.pyx\nsage -t  \"devel/sage-main/sage/matrix/matrix2.pyx\"          \n*** glibc detected *** double free or corruption (fasttop): 0x0a41a380 ***\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\t [2.4 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5495\n\n",
    "created_at": "2009-03-12T02:38:25Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "type: \"A mysterious error (perphaps a memory error?)\"   *PERP*HAPS!!!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5495",
    "user": "was"
}
```
Assignee: cwitty

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

archive/issue_comments_042674.json:
```json
{
    "body": "Trivial patch.",
    "created_at": "2009-03-22T22:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42674",
    "user": "jhpalmieri"
}
```

Trivial patch.



---

archive/issue_comments_042675.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-22T22:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42675",
    "user": "jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042676.json:
```json
{
    "body": "Changing assignee from cwitty to jhpalmieri.",
    "created_at": "2009-03-22T22:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42676",
    "user": "jhpalmieri"
}
```

Changing assignee from cwitty to jhpalmieri.



---

archive/issue_comments_042677.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-22T22:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42677",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_042678.json:
```json
{
    "body": "The patch **5495.patch** fails to apply at all against Sage 3.4:\n\n```\nsage: hg_sage.apply(\"/home/mvngu/patch/5495/5495.patch\")\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg status\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg status\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg import   \"/home/mvngu/patch/5495/5495.patch\"\napplying /home/mvngu/patch/5495/5495.patch\nunable to find 'sage-doctest' for patching\n1 out of 1 hunks FAILED -- saving rejects to file sage-doctest.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2009-03-24T08:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42678",
    "user": "mvngu"
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

archive/issue_comments_042679.json:
```json
{
    "body": "Try using \"hg_scripts\" instead of \"hg_sage\".",
    "created_at": "2009-03-24T15:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42679",
    "user": "jhpalmieri"
}
```

Try using "hg_scripts" instead of "hg_sage".



---

archive/issue_comments_042680.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> Try using \"hg_scripts\" instead of \"hg_sage\".\n\n\nYep, it now applies OK against Sage 3.4. Looks good, and I doctested `sage/matrix/matrix2.pyx` hoping to get a similar error as reported above. But no \"mysterious error\" popped up. Anyway, positive review for the typo fix.",
    "created_at": "2009-03-26T07:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42680",
    "user": "mvngu"
}
```

Replying to [comment:4 jhpalmieri]:
> Try using "hg_scripts" instead of "hg_sage".


Yep, it now applies OK against Sage 3.4. Looks good, and I doctested `sage/matrix/matrix2.pyx` hoping to get a similar error as reported above. But no "mysterious error" popped up. Anyway, positive review for the typo fix.



---

archive/issue_comments_042681.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T23:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42681",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_042682.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-26T23:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5495#issuecomment-42682",
    "user": "mabshoff"
}
```

Resolution: fixed
