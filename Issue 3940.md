# Issue 3940: Add a warnings framework to Sage

archive/issues_003940.json:
```json
{
    "body": "Assignee: cwitty\n\nThe builtin python warnings framework allows filtering on subclasses of warnings.  This would be useful to make a sage warnings framework, with different types of sage-specific warnings.\n\nHere, I've added a directory and a basic file with a NumericalPrecisionWarning class that could be triggered, for example, in the eigenvalue computations.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3940\n\n",
    "created_at": "2008-08-24T00:09:30Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "Add a warnings framework to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3940",
    "user": "jason"
}
```
Assignee: cwitty

The builtin python warnings framework allows filtering on subclasses of warnings.  This would be useful to make a sage warnings framework, with different types of sage-specific warnings.

Here, I've added a directory and a basic file with a NumericalPrecisionWarning class that could be triggered, for example, in the eigenvalue computations.

Issue created by migration from https://trac.sagemath.org/ticket/3940





---

archive/issue_comments_028242.json:
```json
{
    "body": "Attachment [warnings.patch](tarball://root/attachments/some-uuid/ticket3940/warnings.patch) by mabshoff created at 2008-08-25 01:15:17\n\nJason,\n\nnow that #3873 has been merged can you check how much of this patch is still useful/applies?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T01:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28242",
    "user": "mabshoff"
}
```

Attachment [warnings.patch](tarball://root/attachments/some-uuid/ticket3940/warnings.patch) by mabshoff created at 2008-08-25 01:15:17

Jason,

now that #3873 has been merged can you check how much of this patch is still useful/applies?

Cheers,

Michael



---

archive/issue_comments_028243.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-08-25T14:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28243",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_028244.json:
```json
{
    "body": "It is useful and it still applies; the application is still sitting in my queue, though.\n\nBasically, there are some situations where computing eigenvalues/vectors should throw a warning.  Also, the plotting code should throw a warning when some situations come up (when the function can't be evaluated at certain points).  The point of this patch is that: \n\n1. It makes it so that sage-related warnings are always shown by default.\n\n2. It makes it very easy to do something with all sage-related warnings (e.g., throw exceptions or ignore them and don't print them out, etc.)\n\nIf you want to wait until I post a patch that uses this, that's fine.",
    "created_at": "2008-08-25T14:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28244",
    "user": "jason"
}
```

It is useful and it still applies; the application is still sitting in my queue, though.

Basically, there are some situations where computing eigenvalues/vectors should throw a warning.  Also, the plotting code should throw a warning when some situations come up (when the function can't be evaluated at certain points).  The point of this patch is that: 

1. It makes it so that sage-related warnings are always shown by default.

2. It makes it very easy to do something with all sage-related warnings (e.g., throw exceptions or ignore them and don't print them out, etc.)

If you want to wait until I post a patch that uses this, that's fine.



---

archive/issue_comments_028245.json:
```json
{
    "body": "BTW, one question I had was whether to make a warnings directory or to just put this under the misc directory.",
    "created_at": "2008-08-25T14:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28245",
    "user": "jason"
}
```

BTW, one question I had was whether to make a warnings directory or to just put this under the misc directory.



---

archive/issue_comments_028246.json:
```json
{
    "body": "IMHO if the warnings framework is expected to stay as one file, then it should be in the misc directory; if you expect the warnings framework to expand to multiple files then maybe a new directory would be more appropriate.",
    "created_at": "2008-08-25T15:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28246",
    "user": "cwitty"
}
```

IMHO if the warnings framework is expected to stay as one file, then it should be in the misc directory; if you expect the warnings framework to expand to multiple files then maybe a new directory would be more appropriate.



---

archive/issue_comments_028247.json:
```json
{
    "body": "What is the status here? Not having a proper summary subject makes files fall through the cracks. \n\nEither this code is useful in which case it should be applied or not. It seems that cwitty's has some pointers, so what's going on here? :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T21:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28247",
    "user": "mabshoff"
}
```

What is the status here? Not having a proper summary subject makes files fall through the cracks. 

Either this code is useful in which case it should be applied or not. It seems that cwitty's has some pointers, so what's going on here? :)

Cheers,

Michael



---

archive/issue_comments_028248.json:
```json
{
    "body": "I agree with cwitty:\n\nWork that needs to be done on this patch to get it ready for review:\n\n* Make it one file in the misc directory\n\nIf warnings become a more important part of Sage, then later we can break things into a different directory.",
    "created_at": "2009-04-16T22:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28248",
    "user": "jason"
}
```

I agree with cwitty:

Work that needs to be done on this patch to get it ready for review:

* Make it one file in the misc directory

If warnings become a more important part of Sage, then later we can break things into a different directory.



---

archive/issue_comments_028249.json:
```json
{
    "body": "Attachment [sagewarnings.py](tarball://root/attachments/some-uuid/ticket3940/sagewarnings.py) by mraum created at 2010-01-18 21:54:03",
    "created_at": "2010-01-18T21:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28249",
    "user": "mraum"
}
```

Attachment [sagewarnings.py](tarball://root/attachments/some-uuid/ticket3940/sagewarnings.py) by mraum created at 2010-01-18 21:54:03



---

archive/issue_comments_028250.json:
```json
{
    "body": "I uploaded sagewarnings.py which derives from Jason's patch.\nThis extension addresses the lack of use cases by providing some warning classes adapted to particular things I've got in mind. This file is for discussion; See the thread on sage-devel.\n\nI renamed the file warning.py to sagewarnings.py. This seems more consistent with python's warnings module to me.",
    "created_at": "2010-01-18T21:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28250",
    "user": "mraum"
}
```

I uploaded sagewarnings.py which derives from Jason's patch.
This extension addresses the lack of use cases by providing some warning classes adapted to particular things I've got in mind. This file is for discussion; See the thread on sage-devel.

I renamed the file warning.py to sagewarnings.py. This seems more consistent with python's warnings module to me.



---

archive/issue_comments_028251.json:
```json
{
    "body": "outdated, should close",
    "created_at": "2021-08-26T03:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28251",
    "user": "mkoeppe"
}
```

outdated, should close



---

archive/issue_comments_028252.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-08-26T03:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28252",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_028253.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-10-04T22:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28253",
    "user": "mjo"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_028254.json:
```json
{
    "body": "I think the motivation behind this is still valid. But to proceed today, we'd have to look through `git grep 'warn('` and come up with a set of warnings that map nicely to the existing uses in the tree. (And the names themselves are just asking for a bikeshed thread on sage-devel.) The patches on the ticket are far out-of-date in that respect.\n\nThat said, I could sit down for five minutes and easily come up with a hundred \"wishlist\" items that would be nice to have and that would involve a lot of work that no one is willing to do. So I think after so many years, the small benefit of closing a \"dead\" ticket outweighs whatever we'd gain from keeping this on the wishlist.",
    "created_at": "2021-10-04T22:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28254",
    "user": "mjo"
}
```

I think the motivation behind this is still valid. But to proceed today, we'd have to look through `git grep 'warn('` and come up with a set of warnings that map nicely to the existing uses in the tree. (And the names themselves are just asking for a bikeshed thread on sage-devel.) The patches on the ticket are far out-of-date in that respect.

That said, I could sit down for five minutes and easily come up with a hundred "wishlist" items that would be nice to have and that would involve a lot of work that no one is willing to do. So I think after so many years, the small benefit of closing a "dead" ticket outweighs whatever we'd gain from keeping this on the wishlist.



---

archive/issue_comments_028255.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-10-04T23:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28255",
    "user": "mkoeppe"
}
```

Resolution: invalid
