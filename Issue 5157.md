# Issue 5157: if the mwrank interface is interrupted from the notebook (!) it stays broken for the rest of the sage session

archive/issues_005157.json:
```json
{
    "body": "Assignee: was\n\nThis has been driving me nuts for a while.  If you do \n\n```\nsage: EllipticCurve(997).gens(use_database=False)\n[[press control-c]]\nsage: EllipticCurve([1,3]).gens(use_database=False)\nTraceback (most recent call last):\n...\nRuntimeError: [Errno 9] Bad file descriptor\nError evaluating [0, 0, 0, 1, 3] in Mwrank\n```\n\n\nThis is from the notebook.  The same sequence works correctly from the command line (no bad file descriptor). \n\nI think the problem is that the notebook sends multiple control-c's and ends up killing sage properly restarting mwrank.  On the command line one has:\n\n\n```\nsage: EllipticCurve(997).gens(use_database=False)\n...\nKeyboardInterrupt: Restarting Mwrank (WARNING: all variables defined in previous session are now invalid)\nsage: EllipticCurve([1,3]).gens(use_database=False)\n[(-1 : 1 : 1)]\n```\n\n\nBUT, if you hit control-c twice in rapid succession, then mwrank gets broken even on the command line (I just verified this).\n\nThe fix is to make it so the mwrank interface recovers automatically if it gets left in this state. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5157\n\n",
    "created_at": "2009-02-02T06:09:32Z",
    "labels": [
        "algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "if the mwrank interface is interrupted from the notebook (!) it stays broken for the rest of the sage session",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5157",
    "user": "was"
}
```
Assignee: was

This has been driving me nuts for a while.  If you do 

```
sage: EllipticCurve(997).gens(use_database=False)
[[press control-c]]
sage: EllipticCurve([1,3]).gens(use_database=False)
Traceback (most recent call last):
...
RuntimeError: [Errno 9] Bad file descriptor
Error evaluating [0, 0, 0, 1, 3] in Mwrank
```


This is from the notebook.  The same sequence works correctly from the command line (no bad file descriptor). 

I think the problem is that the notebook sends multiple control-c's and ends up killing sage properly restarting mwrank.  On the command line one has:


```
sage: EllipticCurve(997).gens(use_database=False)
...
KeyboardInterrupt: Restarting Mwrank (WARNING: all variables defined in previous session are now invalid)
sage: EllipticCurve([1,3]).gens(use_database=False)
[(-1 : 1 : 1)]
```


BUT, if you hit control-c twice in rapid succession, then mwrank gets broken even on the command line (I just verified this).

The fix is to make it so the mwrank interface recovers automatically if it gets left in this state. 


Issue created by migration from https://trac.sagemath.org/ticket/5157





---

archive/issue_comments_039507.json:
```json
{
    "body": "It seems to be okay, but do we really want the \"print '*'*1000\" in there?",
    "created_at": "2009-02-02T06:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5157#issuecomment-39507",
    "user": "mhansen"
}
```

It seems to be okay, but do we really want the "print '*'*1000" in there?



---

archive/issue_comments_039508.json:
```json
{
    "body": "Attachment [trac_5157.patch](tarball://root/attachments/some-uuid/ticket5157/trac_5157.patch) by was created at 2009-02-02 07:31:03",
    "created_at": "2009-02-02T07:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5157#issuecomment-39508",
    "user": "was"
}
```

Attachment [trac_5157.patch](tarball://root/attachments/some-uuid/ticket5157/trac_5157.patch) by was created at 2009-02-02 07:31:03



---

archive/issue_comments_039509.json:
```json
{
    "body": "This should be refereed by someone who knows pexpect!",
    "created_at": "2009-02-02T09:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5157#issuecomment-39509",
    "user": "cremona"
}
```

This should be refereed by someone who knows pexpect!



---

archive/issue_comments_039510.json:
```json
{
    "body": "> It seems to be okay, but do we really want the \"print '*'*1000\" in there? \n\nThat's debugging code -- I updated the patch to not have it. \n\n> This should be refereed by someone who knows pexpect! \n\nMhansen does, and he said \"it seems to be okay\".",
    "created_at": "2009-02-02T10:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5157#issuecomment-39510",
    "user": "was"
}
```

> It seems to be okay, but do we really want the "print '*'*1000" in there? 

That's debugging code -- I updated the patch to not have it. 

> This should be refereed by someone who knows pexpect! 

Mhansen does, and he said "it seems to be okay".



---

archive/issue_comments_039511.json:
```json
{
    "body": "Since Mike gave this the heads up and William removed the debug print statement I am changing this to a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T18:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5157#issuecomment-39511",
    "user": "mabshoff"
}
```

Since Mike gave this the heads up and William removed the debug print statement I am changing this to a positive review.

Cheers,

Michael



---

archive/issue_comments_039512.json:
```json
{
    "body": "Merged in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T18:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5157#issuecomment-39512",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha4.

Cheers,

Michael



---

archive/issue_comments_039513.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T18:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5157#issuecomment-39513",
    "user": "mabshoff"
}
```

Resolution: fixed
