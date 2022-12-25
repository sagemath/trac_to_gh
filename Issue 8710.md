# Issue 8710: eigenmatrix_right returns inconsistent results for eigenvectors

archive/issues_008710.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @jhpalmieri alexghitza\n\nDoctests introduced in #4756 return the negative of certain eigenvectors on certain hardware.\n\nSee initital discussion at \n\nhttp://groups.google.com/group/sage-release/browse_thread/thread/9136569bd1c67f6\n\nIssue created by migration from https://trac.sagemath.org/ticket/8710\n\n",
    "created_at": "2010-04-18T03:30:23Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "eigenmatrix_right returns inconsistent results for eigenvectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8710",
    "user": "https://github.com/rbeezer"
}
```
Assignee: jason, was

CC:  @jhpalmieri alexghitza

Doctests introduced in #4756 return the negative of certain eigenvectors on certain hardware.

See initital discussion at 

http://groups.google.com/group/sage-release/browse_thread/thread/9136569bd1c67f6

Issue created by migration from https://trac.sagemath.org/ticket/8710





---

archive/issue_comments_079346.json:
```json
{
    "body": "Attachment [trac_8710-eigenvector-doctest.patch](tarball://root/attachments/some-uuid/ticket8710/trac_8710-eigenvector-doctest.patch) by @rbeezer created at 2010-04-19 04:48:19",
    "created_at": "2010-04-19T04:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8710#issuecomment-79346",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_8710-eigenvector-doctest.patch](tarball://root/attachments/some-uuid/ticket8710/trac_8710-eigenvector-doctest.patch) by @rbeezer created at 2010-04-19 04:48:19



---

archive/issue_comments_079347.json:
```json
{
    "body": "This patch massages the doctests that were causing failures for 4.4.alpha0 on the Skynet machine, sextus.  Its not pretty, but I hope the results are now hardware-neutral.\n\nAlex - you reviewed the original ticket (#4756), so maybe this would be an easy review for you?\n\nJohn - I don't know if it is easy for you to test this on sextus in advance of merging it?  Sounds like it will be a while before I have that kind of access.\n\nRob",
    "created_at": "2010-04-19T04:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8710#issuecomment-79347",
    "user": "https://github.com/rbeezer"
}
```

This patch massages the doctests that were causing failures for 4.4.alpha0 on the Skynet machine, sextus.  Its not pretty, but I hope the results are now hardware-neutral.

Alex - you reviewed the original ticket (#4756), so maybe this would be an easy review for you?

John - I don't know if it is easy for you to test this on sextus in advance of merging it?  Sounds like it will be a while before I have that kind of access.

Rob



---

archive/issue_comments_079348.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-19T04:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8710#issuecomment-79348",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079349.json:
```json
{
    "body": "1. John will have to test, since he has the build on sextus. \n\n2. The doctests actually look much nicer normalized to have first entry 1! \n\n(I would give this a positive review if this works.)",
    "created_at": "2010-04-19T05:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8710#issuecomment-79349",
    "user": "https://github.com/williamstein"
}
```

1. John will have to test, since he has the build on sextus. 

2. The doctests actually look much nicer normalized to have first entry 1! 

(I would give this a positive review if this works.)



---

archive/issue_comments_079350.json:
```json
{
    "body": "Replying to [comment:3 was]:\n> 2. The doctests actually look much nicer normalized to have first entry 1! \n\nThe output looks nicer because this matrix is out of my textbook and was *designed* to have nice-looking answers.  I don't like the hard-to-decipher code that gets you there, but that's the way it goes.  Thanks for having a look and for the advice on getting this squared away.\n\nRob",
    "created_at": "2010-04-19T05:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8710#issuecomment-79350",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:3 was]:
> 2. The doctests actually look much nicer normalized to have first entry 1! 

The output looks nicer because this matrix is out of my textbook and was *designed* to have nice-looking answers.  I don't like the hard-to-decipher code that gets you there, but that's the way it goes.  Thanks for having a look and for the advice on getting this squared away.

Rob



---

archive/issue_comments_079351.json:
```json
{
    "body": "Tests pass on sextus.  I'll test it on a few more machines, and if it works, I'll give it a positive review and merge it into 4.4.alpha1.",
    "created_at": "2010-04-19T05:35:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8710#issuecomment-79351",
    "user": "https://github.com/jhpalmieri"
}
```

Tests pass on sextus.  I'll test it on a few more machines, and if it works, I'll give it a positive review and merge it into 4.4.alpha1.



---

archive/issue_comments_079352.json:
```json
{
    "body": "Hi John,\n\nDid this eventually past muster on skynet, or does it need more testing?\n\nI still haven't done the `SciPy` tests I'd like to do skynet yet, but hope to get to that soon.\n\nRob",
    "created_at": "2010-04-27T05:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8710#issuecomment-79352",
    "user": "https://github.com/rbeezer"
}
```

Hi John,

Did this eventually past muster on skynet, or does it need more testing?

I still haven't done the `SciPy` tests I'd like to do skynet yet, but hope to get to that soon.

Rob



---

archive/issue_comments_079353.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-27T05:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8710#issuecomment-79353",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_021144.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-27T05:59:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8710",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8710#event-21144"
}
```



---

archive/issue_comments_079354.json:
```json
{
    "body": "Sorry, Rob.  This was actually merged in 4.4.alpha1 but I forgot to mark it as closed.  (So it didn't get recorded in the release notes, either.)",
    "created_at": "2010-04-27T05:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8710#issuecomment-79354",
    "user": "https://github.com/jhpalmieri"
}
```

Sorry, Rob.  This was actually merged in 4.4.alpha1 but I forgot to mark it as closed.  (So it didn't get recorded in the release notes, either.)



---

archive/issue_events_021145.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-04-27T12:58:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8710",
    "milestone": "sage-4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8710#event-21145"
}
```
