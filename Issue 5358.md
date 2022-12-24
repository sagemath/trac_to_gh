# Issue 5358: major bug in missing import of escape in twist.py

archive/issues_005358.json:
```json
{
    "body": "Assignee: boothby\n\ntwist.py uses escape but doesnt' import it.  This is a bug introduced in #5258 by bad refereeing. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5358\n\n",
    "created_at": "2009-02-24T14:44:39Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "major bug in missing import of escape in twist.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5358",
    "user": "was"
}
```
Assignee: boothby

twist.py uses escape but doesnt' import it.  This is a bug introduced in #5258 by bad refereeing. 

Issue created by migration from https://trac.sagemath.org/ticket/5358





---

archive/issue_comments_041282.json:
```json
{
    "body": "Attachment [trac_5358.patch](tarball://root/attachments/some-uuid/ticket5358/trac_5358.patch) by was created at 2009-02-24 14:45:31",
    "created_at": "2009-02-24T14:45:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5358#issuecomment-41282",
    "user": "was"
}
```

Attachment [trac_5358.patch](tarball://root/attachments/some-uuid/ticket5358/trac_5358.patch) by was created at 2009-02-24 14:45:31



---

archive/issue_comments_041283.json:
```json
{
    "body": "With all due respect, the bug was introduced by the author of the patch (me), not the reviewer (you).  You take too much credit :).\n\nThis patch looks good, but I haven't applied it or doctested it.  I'm upgrading to 3.3 now to be able to try that.\n\nReally, this should have been caught in a doctest, so another +1 towards getting notebook doctesting working!",
    "created_at": "2009-02-24T15:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5358#issuecomment-41283",
    "user": "jason"
}
```

With all due respect, the bug was introduced by the author of the patch (me), not the reviewer (you).  You take too much credit :).

This patch looks good, but I haven't applied it or doctested it.  I'm upgrading to 3.3 now to be able to try that.

Really, this should have been caught in a doctest, so another +1 towards getting notebook doctesting working!



---

archive/issue_comments_041284.json:
```json
{
    "body": "I caught it by watching the server log on sagenb.org and seeing a traceback.  That's definitely not an ideal way to find something like this ;-)",
    "created_at": "2009-02-24T18:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5358#issuecomment-41284",
    "user": "was"
}
```

I caught it by watching the server log on sagenb.org and seeing a traceback.  That's definitely not an ideal way to find something like this ;-)



---

archive/issue_comments_041285.json:
```json
{
    "body": "The patch applies cleanly and I don't see any errors running the notebook with it applies.  It certainly seems like it would cause errors not to have it applied. Positive review.",
    "created_at": "2009-02-24T22:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5358#issuecomment-41285",
    "user": "jason"
}
```

The patch applies cleanly and I don't see any errors running the notebook with it applies.  It certainly seems like it would cause errors not to have it applied. Positive review.



---

archive/issue_comments_041286.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T15:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5358#issuecomment-41286",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041287.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T15:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5358#issuecomment-41287",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael
