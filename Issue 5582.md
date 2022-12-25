# Issue 5582: Coercion from float to QQ is missing

archive/issues_005582.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  @jbandlow\n\n\n```\n\tsage: a = float(1.0)\n \tsage: QQ(a)\n \tTypeError: Unable to coerce 1.0 (<type 'float'>) to Rational\n```\n\nNote that the following works:\n\n```\n \tsage: a = float(1.0)\n \tsage: QQ(RR(a))\n \t1\n```\n\n\n> Yes, this conversion is missing. It should be easy to implement.\n> \n> - Robert\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5582\n\n",
    "created_at": "2009-03-21T20:00:18Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Coercion from float to QQ is missing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5582",
    "user": "https://github.com/jbandlow"
}
```
Assignee: @robertwb

CC:  @jbandlow


```
	sage: a = float(1.0)
 	sage: QQ(a)
 	TypeError: Unable to coerce 1.0 (<type 'float'>) to Rational
```

Note that the following works:

```
 	sage: a = float(1.0)
 	sage: QQ(RR(a))
 	1
```


> Yes, this conversion is missing. It should be easy to implement.
> 
> - Robert


Issue created by migration from https://trac.sagemath.org/ticket/5582





---

archive/issue_comments_043427.json:
```json
{
    "body": "Attachment [5582-float-QQ.patch](tarball://root/attachments/some-uuid/ticket5582/5582-float-QQ.patch) by @robertwb created at 2009-03-21 20:20:10",
    "created_at": "2009-03-21T20:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5582#issuecomment-43427",
    "user": "https://github.com/robertwb"
}
```

Attachment [5582-float-QQ.patch](tarball://root/attachments/some-uuid/ticket5582/5582-float-QQ.patch) by @robertwb created at 2009-03-21 20:20:10



---

archive/issue_comments_043428.json:
```json
{
    "body": "Applies cleanly to my sage 3.4, solves the problem and has a doctest.  Positive review. Thanks very much for this, Robert!",
    "created_at": "2009-03-22T16:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5582#issuecomment-43428",
    "user": "https://github.com/jbandlow"
}
```

Applies cleanly to my sage 3.4, solves the problem and has a doctest.  Positive review. Thanks very much for this, Robert!



---

archive/issue_comments_043429.json:
```json
{
    "body": "This patch causes the following failure for me:\n\n```\nsage -t -long \"devel/sage/sage/rings/rational.pyx\"          \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/rings/rational.pyx\", line 1510:\n    sage: float(1.2)**(1/2)\nExpected:\n    1.0954451150103321\nGot:\n    sqrt(6)/sqrt(5)\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T21:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5582#issuecomment-43429",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch causes the following failure for me:

```
sage -t -long "devel/sage/sage/rings/rational.pyx"          
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/rings/rational.pyx", line 1510:
    sage: float(1.2)**(1/2)
Expected:
    1.0954451150103321
Got:
    sqrt(6)/sqrt(5)
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_043430.json:
```json
{
    "body": "Attachment [5582-QQfloat2.patch](tarball://root/attachments/some-uuid/ticket5582/5582-QQfloat2.patch) by @robertwb created at 2009-05-18 22:11:09",
    "created_at": "2009-05-18T22:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5582#issuecomment-43430",
    "user": "https://github.com/robertwb"
}
```

Attachment [5582-QQfloat2.patch](tarball://root/attachments/some-uuid/ticket5582/5582-QQfloat2.patch) by @robertwb created at 2009-05-18 22:11:09



---

archive/issue_comments_043431.json:
```json
{
    "body": "Looks good to me.  Apply both patches.",
    "created_at": "2009-05-19T20:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5582#issuecomment-43431",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  Apply both patches.



---

archive/issue_comments_043432.json:
```json
{
    "body": "These apply with quite some offset, so let's hope for the best:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ patch -p1 < trac_5582-float-QQ.patch\npatching file sage/rings/rational.pyx\nHunk #1 succeeded at 65 (offset 4 lines).\nHunk #2 succeeded at 298 (offset 135 lines).\nHunk #3 succeeded at 492 (offset 151 lines).\nmabshoff@sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ patch -p1 < trac_5582-QQfloat2.patch \npatching file sage/rings/rational.pyx\nHunk #1 succeeded at 1816 (offset 191 lines).\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T01:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5582#issuecomment-43432",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

These apply with quite some offset, so let's hope for the best:

```
mabshoff@sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ patch -p1 < trac_5582-float-QQ.patch
patching file sage/rings/rational.pyx
Hunk #1 succeeded at 65 (offset 4 lines).
Hunk #2 succeeded at 298 (offset 135 lines).
Hunk #3 succeeded at 492 (offset 151 lines).
mabshoff@sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ patch -p1 < trac_5582-QQfloat2.patch 
patching file sage/rings/rational.pyx
Hunk #1 succeeded at 1816 (offset 191 lines).
```


Cheers,

Michael



---

archive/issue_comments_043433.json:
```json
{
    "body": "Merged both patches into Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T01:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5582#issuecomment-43433",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches into Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_events_005827.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-21T01:27:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5582",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5582#event-5827"
}
```



---

archive/issue_comments_043434.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T01:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5582#issuecomment-43434",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
