# Issue 5577: [with patch, needs review] typo in tutorial

archive/issues_005577.json:
```json
{
    "body": "Assignee: tba\n\nThis is a repeat of #4379, changing one word in the tutorial: the change there was undone, perhaps in the ReST conversion, and this reinstates it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5577\n\n",
    "created_at": "2009-03-20T18:18:20Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] typo in tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5577",
    "user": "jhpalmieri"
}
```
Assignee: tba

This is a repeat of #4379, changing one word in the tutorial: the change there was undone, perhaps in the ReST conversion, and this reinstates it.

Issue created by migration from https://trac.sagemath.org/ticket/5577





---

archive/issue_comments_043488.json:
```json
{
    "body": "Attachment\n\nOh, this might depend on #5500.",
    "created_at": "2009-03-20T18:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43488",
    "user": "jhpalmieri"
}
```

Attachment

Oh, this might depend on #5500.



---

archive/issue_comments_043489.json:
```json
{
    "body": "Changing assignee from tba to jhpalmieri.",
    "created_at": "2009-03-20T20:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43489",
    "user": "jhpalmieri"
}
```

Changing assignee from tba to jhpalmieri.



---

archive/issue_comments_043490.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-20T20:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43490",
    "user": "jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043491.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch **tut-typo.patch** applies against Sage 3.4, but with some fuzz:\n\n```\nsage: hg_sage.apply(\"/home/mvngu/patch/5577/tut-typo.patch\")\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg status\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg status\ncd \"/home/mvngu/scratch/sage-3.4/devel/sage\" && hg import   \"/home/mvngu/patch/5577/tut-typo.patch\"\napplying /home/mvngu/patch/5577/tut-typo.patch\npatching file doc/en/tutorial/tour_help.rst\nHunk #1 succeeded at 120 with fuzz 1 (offset -1 lines).\n```\n\nThat didn't prevent me from (re)building the tutorial in HTML format. Viewing the updated section \"Getting Help\" in the tutorial, I see that the patch fixes the problem it meant to fix. I don't know how significant the above fuzz is, but probably it doesn't matter at all, in which case I'd give a positive review to the patch.",
    "created_at": "2009-03-23T02:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43491",
    "user": "mvngu"
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

archive/issue_comments_043492.json:
```json
{
    "body": "Okay, it definitely depends on #5500.  (Without applying #5500, you see the fuzz.)",
    "created_at": "2009-03-23T04:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43492",
    "user": "jhpalmieri"
}
```

Okay, it definitely depends on #5500.  (Without applying #5500, you see the fuzz.)



---

archive/issue_comments_043493.json:
```json
{
    "body": "Looks good, positive review. So here's the order in which patches should be applied:\n1. First apply patches at #5500.\n2. Then apply **tut-typo.patch**.\nThis ordering should prevent any fuzz.",
    "created_at": "2009-03-23T04:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43493",
    "user": "mvngu"
}
```

Looks good, positive review. So here's the order in which patches should be applied:
1. First apply patches at #5500.
2. Then apply **tut-typo.patch**.
This ordering should prevent any fuzz.



---

archive/issue_comments_043494.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T18:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43494",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043495.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T18:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5577#issuecomment-43495",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
