# Issue 4277: [with patch, needs review] improve doctest coverage of ell_point.py

archive/issues_004277.json:
```json
{
    "body": "Assignee: was\n\nThe patch improves the doctest coverage of ell_point.py to 100%. However, a test is failing, with _magma_init_(), and I wasn't able to fix it, it seems the _magma_().name() implementation is buggy:\n\n```\nFile \"/usr/local/sage-3.1.2/sage/tmp/ell_point.py\", line 1289:\n    sage: P._magma_init_()\nExpected:\n    'EllipticCurve([GF(17)!1,GF(17)!16])![13,4]'\nGot:\n    '_sage_[2]![_sage_[3],_sage_[4]]'\n```\n\nAlso, I believe ell_padic.py should be removed, since it is said it is deprecated, and it does\nnot seem to be used anywhere.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4277\n\n",
    "created_at": "2008-10-13T19:48:41Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] improve doctest coverage of ell_point.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4277",
    "user": "zimmerma"
}
```
Assignee: was

The patch improves the doctest coverage of ell_point.py to 100%. However, a test is failing, with _magma_init_(), and I wasn't able to fix it, it seems the _magma_().name() implementation is buggy:

```
File "/usr/local/sage-3.1.2/sage/tmp/ell_point.py", line 1289:
    sage: P._magma_init_()
Expected:
    'EllipticCurve([GF(17)!1,GF(17)!16])![13,4]'
Got:
    '_sage_[2]![_sage_[3],_sage_[4]]'
```

Also, I believe ell_padic.py should be removed, since it is said it is deprecated, and it does
not seem to be used anywhere.

Issue created by migration from https://trac.sagemath.org/ticket/4277





---

archive/issue_comments_031271.json:
```json
{
    "body": "Attachment [trac4277.patch](tarball://root/attachments/some-uuid/ticket4277/trac4277.patch) by robertwb created at 2008-10-14 20:51:05",
    "created_at": "2008-10-14T20:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4277#issuecomment-31271",
    "user": "robertwb"
}
```

Attachment [trac4277.patch](tarball://root/attachments/some-uuid/ticket4277/trac4277.patch) by robertwb created at 2008-10-14 20:51:05



---

archive/issue_comments_031272.json:
```json
{
    "body": "I had to rebase this against 3.1.3, which involved removing one typo fix that had been fixed by someone else.",
    "created_at": "2008-10-14T20:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4277#issuecomment-31272",
    "user": "robertwb"
}
```

I had to rebase this against 3.1.3, which involved removing one typo fix that had been fixed by someone else.



---

archive/issue_comments_031273.json:
```json
{
    "body": "Nevermind, I get that same error...",
    "created_at": "2008-10-14T21:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4277#issuecomment-31273",
    "user": "robertwb"
}
```

Nevermind, I get that same error...



---

archive/issue_comments_031274.json:
```json
{
    "body": "This patch depends on #4288",
    "created_at": "2008-10-14T21:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4277#issuecomment-31274",
    "user": "robertwb"
}
```

This patch depends on #4288



---

archive/issue_comments_031275.json:
```json
{
    "body": "Replying to [comment:3 robertwb]:\n> This patch depends on #4288\n\nI assume #4289.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T15:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4277#issuecomment-31275",
    "user": "mabshoff"
}
```

Replying to [comment:3 robertwb]:
> This patch depends on #4288

I assume #4289.

Cheers,

Michael



---

archive/issue_comments_031276.json:
```json
{
    "body": "Replying to [comment:4 mabshoff]:\n> I assume #4289.\n\nI guess Robert wanted to say that the _magma_init_ error\nis now a separate ticket, namely #4288.",
    "created_at": "2008-10-18T15:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4277#issuecomment-31276",
    "user": "zimmerma"
}
```

Replying to [comment:4 mabshoff]:
> I assume #4289.

I guess Robert wanted to say that the _magma_init_ error
is now a separate ticket, namely #4288.



---

archive/issue_comments_031277.json:
```json
{
    "body": "Yes, my intention was that the _magma_init_ error is a separate ticket, and needs to be fixed before this can go in (with all doctests passing). William recently changed how _magma_init_ works in some cases, so I'm going to cc him.",
    "created_at": "2008-10-18T16:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4277#issuecomment-31277",
    "user": "robertwb"
}
```

Yes, my intention was that the _magma_init_ error is a separate ticket, and needs to be fixed before this can go in (with all doctests passing). William recently changed how _magma_init_ works in some cases, so I'm going to cc him.



---

archive/issue_comments_031278.json:
```json
{
    "body": "Replying to [comment:5 zimmerma]:\n> I guess Robert wanted to say that the _magma_init_ error\n> is now a separate ticket, namely #4288.\n\nYep, I found that out, too. Let's hope was or someone else fixes this one soon.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T19:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4277#issuecomment-31278",
    "user": "mabshoff"
}
```

Replying to [comment:5 zimmerma]:
> I guess Robert wanted to say that the _magma_init_ error
> is now a separate ticket, namely #4288.

Yep, I found that out, too. Let's hope was or someone else fixes this one soon.

Cheers,

Michael



---

archive/issue_comments_031279.json:
```json
{
    "body": "Replying to [comment:7 mabshoff]:\n> Replying to [comment:5 zimmerma]:\n> > I guess Robert wanted to say that the _magma_init_ error\n> > is now a separate ticket, namely #4288.\n> \n> Yep, I found that out, too. Let's hope was or someone else fixes this one soon.\n\nIt was someone else ;)\n\nSomeone who looked at this one earlier might like to to try it out along with my patch to #4288 since I think the two together work fine (this one needs to be applied before that one).\n\n> \n> Cheers,\n> \n> Michael",
    "created_at": "2008-10-19T20:25:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4277#issuecomment-31279",
    "user": "cremona"
}
```

Replying to [comment:7 mabshoff]:
> Replying to [comment:5 zimmerma]:
> > I guess Robert wanted to say that the _magma_init_ error
> > is now a separate ticket, namely #4288.
> 
> Yep, I found that out, too. Let's hope was or someone else fixes this one soon.

It was someone else ;)

Someone who looked at this one earlier might like to to try it out along with my patch to #4288 since I think the two together work fine (this one needs to be applied before that one).

> 
> Cheers,
> 
> Michael



---

archive/issue_comments_031280.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-20T14:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4277#issuecomment-31280",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031281.json:
```json
{
    "body": "Merged in Sage 3.2.alpha0",
    "created_at": "2008-10-20T14:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4277#issuecomment-31281",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha0
