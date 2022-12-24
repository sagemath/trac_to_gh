# Issue 9084: Move sage/gsl into libs directory.

archive/issues_009084.json:
```json
{
    "body": "Assignee: jason, jkantor\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9084\n\n",
    "created_at": "2010-05-29T08:46:10Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.5",
    "title": "Move sage/gsl into libs directory.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9084",
    "user": "@robertwb"
}
```
Assignee: jason, jkantor



Issue created by migration from https://trac.sagemath.org/ticket/9084





---

archive/issue_comments_084337.json:
```json
{
    "body": "Bundle of file renaming.",
    "created_at": "2010-05-29T17:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84337",
    "user": "@robertwb"
}
```

Bundle of file renaming.



---

archive/issue_comments_084338.json:
```json
{
    "body": "Attachment [9084-fix-imports.patch](tarball://root/attachments/some-uuid/ticket9084/9084-fix-imports.patch) by @robertwb created at 2010-05-29 17:43:16\n\napply on top of previous",
    "created_at": "2010-05-29T17:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84338",
    "user": "@robertwb"
}
```

Attachment [9084-fix-imports.patch](tarball://root/attachments/some-uuid/ticket9084/9084-fix-imports.patch) by @robertwb created at 2010-05-29 17:43:16

apply on top of previous



---

archive/issue_comments_084339.json:
```json
{
    "body": "Should be an easy review, this just moved stuff around. I took the opportunity to change them from .pxi files to .pxd files, which they really should have been originally, so now they're cimported rather than included. \n\nApply bundle with \"hg pull /path/to/9084-move-gsl.hg\". I've created a bundle to preserve the history across the file moves.",
    "created_at": "2010-05-29T17:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84339",
    "user": "@robertwb"
}
```

Should be an easy review, this just moved stuff around. I took the opportunity to change them from .pxi files to .pxd files, which they really should have been originally, so now they're cimported rather than included. 

Apply bundle with "hg pull /path/to/9084-move-gsl.hg". I've created a bundle to preserve the history across the file moves.



---

archive/issue_comments_084340.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-29T17:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84340",
    "user": "@robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084341.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-01T07:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84341",
    "user": "@kwankyu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084342.json:
```json
{
    "body": "This is unfortunate, but the patch does not apply cleanly for Sage 4.6.2. We missed the right time to review the patch...",
    "created_at": "2011-04-01T07:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84342",
    "user": "@kwankyu"
}
```

This is unfortunate, but the patch does not apply cleanly for Sage 4.6.2. We missed the right time to review the patch...



---

archive/issue_comments_084343.json:
```json
{
    "body": "Changing component from numerical to relocation.",
    "created_at": "2016-11-10T20:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84343",
    "user": "@kwankyu"
}
```

Changing component from numerical to relocation.



---

archive/issue_comments_084344.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2016-11-10T20:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84344",
    "user": "@kwankyu"
}
```

Changing priority from major to minor.



---

archive/issue_comments_084345.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-11-10T20:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84345",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_084346.json:
```json
{
    "body": "I disagree with the premise of this ticket.\n\nI believe that `src/sage/libs` is a place purely for the library interface and nothing more. Making classes and implementing functionality using that library belongs somewhere else.\n\nTo use an example: a Sage `Integer` wraps a GMP/MPIR `mpz_t`. The GMP/MPIR library interface belongs in `src/sage/libs/gmp`, but the `Integer` class does not (because it does a lot more than strictly wrapping the GMP/MPIR library).",
    "created_at": "2016-11-10T20:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84346",
    "user": "@jdemeyer"
}
```

I disagree with the premise of this ticket.

I believe that `src/sage/libs` is a place purely for the library interface and nothing more. Making classes and implementing functionality using that library belongs somewhere else.

To use an example: a Sage `Integer` wraps a GMP/MPIR `mpz_t`. The GMP/MPIR library interface belongs in `src/sage/libs/gmp`, but the `Integer` class does not (because it does a lot more than strictly wrapping the GMP/MPIR library).



---

archive/issue_comments_084347.json:
```json
{
    "body": "Replying to [comment:10 jdemeyer]:\n> I disagree with the premise of this ticket.\n> \n> I believe that `src/sage/libs` is a place purely for the library interface and nothing more. Making classes and implementing functionality using that library belongs somewhere else.\n> \n> To use an example: a Sage `Integer` wraps a GMP/MPIR `mpz_t`. The GMP/MPIR library interface belongs in `src/sage/libs/gmp`, but the `Integer` class does not (because it does a lot more than strictly wrapping the GMP/MPIR library).\n\nI understand that. But on the other hand, don't you agree that `gsl` is too specific to be placed just under `src/sage`, where all other subfolders  correspond to rather big (mathematical) themes?\n\nAnd it seems to me that  there are already files under `src/sage/libs/xxx` that contain classes implementing functionality using the libraries. For example, look into `eclib`. No?\n\nI think that `src/libs/gsl` is not an ideal place but less bad than just under `src/sage`. Could you suggest a better palce?",
    "created_at": "2016-11-11T02:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84347",
    "user": "@kwankyu"
}
```

Replying to [comment:10 jdemeyer]:
> I disagree with the premise of this ticket.
> 
> I believe that `src/sage/libs` is a place purely for the library interface and nothing more. Making classes and implementing functionality using that library belongs somewhere else.
> 
> To use an example: a Sage `Integer` wraps a GMP/MPIR `mpz_t`. The GMP/MPIR library interface belongs in `src/sage/libs/gmp`, but the `Integer` class does not (because it does a lot more than strictly wrapping the GMP/MPIR library).

I understand that. But on the other hand, don't you agree that `gsl` is too specific to be placed just under `src/sage`, where all other subfolders  correspond to rather big (mathematical) themes?

And it seems to me that  there are already files under `src/sage/libs/xxx` that contain classes implementing functionality using the libraries. For example, look into `eclib`. No?

I think that `src/libs/gsl` is not an ideal place but less bad than just under `src/sage`. Could you suggest a better palce?



---

archive/issue_comments_084348.json:
```json
{
    "body": "Replying to [comment:11 klee]:\n> Could you suggest a better palce?\n\nHow about in `src/sage/calculus`?",
    "created_at": "2016-11-11T08:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84348",
    "user": "@jdemeyer"
}
```

Replying to [comment:11 klee]:
> Could you suggest a better palce?

How about in `src/sage/calculus`?



---

archive/issue_comments_084349.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-11-11T17:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84349",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_084350.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-11-12T06:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84350",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_084351.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-11-12T12:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84351",
    "user": "@kwankyu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084352.json:
```json
{
    "body": "I owe a lot from Robert's old code.",
    "created_at": "2016-11-12T12:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84352",
    "user": "@kwankyu"
}
```

I owe a lot from Robert's old code.



---

archive/issue_comments_084353.json:
```json
{
    "body": "I have nothing to do for the patchbot plugin failures.",
    "created_at": "2016-11-14T08:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84353",
    "user": "@kwankyu"
}
```

I have nothing to do for the patchbot plugin failures.



---

archive/issue_comments_084354.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-11-21T00:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84354",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_084355.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-11-21T00:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84355",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_084356.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-12-18T12:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84356",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_084357.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-12-21T02:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84357",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_084358.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-12-27T09:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84358",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084359.json:
```json
{
    "body": "Thank you!",
    "created_at": "2016-12-27T09:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84359",
    "user": "@kwankyu"
}
```

Thank you!



---

archive/issue_comments_084360.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-01-23T22:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9084#issuecomment-84360",
    "user": "@vbraun"
}
```

Resolution: fixed
