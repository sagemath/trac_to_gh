# Issue 3015: introspecting Cryto.DES using DES?? should throw an error message instead of displaying binary junk

archive/issues_003015.json:
```json
{
    "body": "Assignee: @williamstein\n\nIn sage-3.0 on OSX and linux (sage.math.washington.edu) if you do the following:\n\n```\n  sage: from Crypto.Cipher import DES\n  sage: DES??\n```\nYou get a bunch of binary garbage on your screen. I tried the same thing in vanilla ipython and it correctly told me that it could not open the source file. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3015\n\n",
    "closed_at": "2013-07-22T16:11:46Z",
    "created_at": "2008-04-24T03:54:06Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "introspecting Cryto.DES using DES?? should throw an error message instead of displaying binary junk",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3015",
    "user": "https://github.com/yqiang"
}
```
Assignee: @williamstein

In sage-3.0 on OSX and linux (sage.math.washington.edu) if you do the following:

```
  sage: from Crypto.Cipher import DES
  sage: DES??
```
You get a bunch of binary garbage on your screen. I tried the same thing in vanilla ipython and it correctly told me that it could not open the source file. 

Issue created by migration from https://trac.sagemath.org/ticket/3015





---

archive/issue_comments_020679.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-22T16:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3015#issuecomment-20679",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_006846.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-22T16:11:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3015",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3015#event-6846"
}
```



---

archive/issue_events_006847.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-22T16:11:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3015",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3015#event-6847"
}
```



---

archive/issue_comments_020680.json:
```json
{
    "body": "I get an error now instead of binary junk.  I think this was probably fixed with the new IPython update.",
    "created_at": "2013-07-22T16:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3015#issuecomment-20680",
    "user": "https://github.com/mwhansen"
}
```

I get an error now instead of binary junk.  I think this was probably fixed with the new IPython update.
