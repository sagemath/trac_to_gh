# Issue 5577: [with patch, needs review] typo in tutorial

archive/issues_005577.json:
```json
{
    "body": "Assignee: tba\n\nThis is a repeat of #4379, changing one word in the tutorial: the change there was undone, perhaps in the ReST conversion, and this reinstates it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5577\n\n",
    "created_at": "2009-03-20T18:18:20Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] typo in tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5577",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tba

This is a repeat of #4379, changing one word in the tutorial: the change there was undone, perhaps in the ReST conversion, and this reinstates it.

Issue created by migration from https://trac.sagemath.org/ticket/5577





---

archive/issue_comments_043404.json:
```json
{
    "body": "Attachment [tut-typo.patch](tarball://root/attachments/some-uuid/ticket5577/tut-typo.patch) by @jhpalmieri created at 2009-03-20 18:19:48\n\nOh, this might depend on #5500.",
    "created_at": "2009-03-20T18:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43404",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [tut-typo.patch](tarball://root/attachments/some-uuid/ticket5577/tut-typo.patch) by @jhpalmieri created at 2009-03-20 18:19:48

Oh, this might depend on #5500.



---

archive/issue_comments_043405.json:
```json
{
    "body": "Changing assignee from tba to @jhpalmieri.",
    "created_at": "2009-03-20T20:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43405",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from tba to @jhpalmieri.



---

archive/issue_comments_043406.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-20T20:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43406",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043407.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch **tut-typo.patch** applies against Sage 3.4, but with some fuzz:\n\n```\nsage: hg_sage.apply(\"/home/mvngu/patch/5577/tut-typo.patch\")\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg status\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg status\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg import   \"/home/mvngu/patch/5577/tut-typo.patch\"\napplying /home/mvngu/patch/5577/tut-typo.patch\npatching file doc/en/tutorial/tour_help.rst\nHunk #1 succeeded at 120 with fuzz 1 (offset -1 lines).\n```\n\nThat didn't prevent me from (re)building the tutorial in HTML format. Viewing the updated section \"Getting Help\" in the tutorial, I see that the patch fixes the problem it meant to fix. I don't know how significant the above fuzz is, but probably it doesn't matter at all, in which case I'd give a positive review to the patch.",
    "created_at": "2009-03-23T02:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43407",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

REFEREE REPORT



The patch **tut-typo.patch** applies against Sage 3.4, but with some fuzz:

```
sage: hg_sage.apply("/home/mvngu/patch/5577/tut-typo.patch")
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg import   "/home/mvngu/patch/5577/tut-typo.patch"
applying /home/mvngu/patch/5577/tut-typo.patch
patching file doc/en/tutorial/tour_help.rst
Hunk #1 succeeded at 120 with fuzz 1 (offset -1 lines).
```

That didn't prevent me from (re)building the tutorial in HTML format. Viewing the updated section "Getting Help" in the tutorial, I see that the patch fixes the problem it meant to fix. I don't know how significant the above fuzz is, but probably it doesn't matter at all, in which case I'd give a positive review to the patch.



---

archive/issue_comments_043408.json:
```json
{
    "body": "Okay, it definitely depends on #5500.  (Without applying #5500, you see the fuzz.)",
    "created_at": "2009-03-23T04:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43408",
    "user": "https://github.com/jhpalmieri"
}
```

Okay, it definitely depends on #5500.  (Without applying #5500, you see the fuzz.)



---

archive/issue_comments_043409.json:
```json
{
    "body": "Looks good, positive review. So here's the order in which patches should be applied:\n1. First apply patches at #5500.\n2. Then apply **tut-typo.patch**.\nThis ordering should prevent any fuzz.",
    "created_at": "2009-03-23T04:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43409",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Looks good, positive review. So here's the order in which patches should be applied:
1. First apply patches at #5500.
2. Then apply **tut-typo.patch**.
This ordering should prevent any fuzz.



---

archive/issue_comments_043410.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T18:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43410",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043411.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T18:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43411",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
