# Issue 7637: Default dictionary in MixedIntegerLinearProgram

archive/issues_007637.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  malb\n\nMartin Albrecht requested this functionality for his code, and it would also simplify mine. For short linear programs, of when some global variables do not require the creation of a new dictionary of variables ( from which only one field would be used ), this trick is good enough !\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7637\n\n",
    "created_at": "2009-12-09T12:27:25Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "title": "Default dictionary in MixedIntegerLinearProgram",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7637",
    "user": "ncohen"
}
```
Assignee: jkantor

CC:  malb

Martin Albrecht requested this functionality for his code, and it would also simplify mine. For short linear programs, of when some global variables do not require the creation of a new dictionary of variables ( from which only one field would be used ), this trick is good enough !

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7637





---

archive/issue_comments_065273.json:
```json
{
    "body": "* `try: foo except AttributeError:` seems to be favoured in the Python community over `hasattr`. It is also faster if the attribute does in fact exist.\n  * Why do you call `__getitem__()` instead of using the normal syntax `[x]`?",
    "created_at": "2009-12-09T15:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65273",
    "user": "malb"
}
```

* `try: foo except AttributeError:` seems to be favoured in the Python community over `hasattr`. It is also faster if the attribute does in fact exist.
  * Why do you call `__getitem__()` instead of using the normal syntax `[x]`?



---

archive/issue_comments_065274.json:
```json
{
    "body": "Done !",
    "created_at": "2009-12-09T17:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65274",
    "user": "ncohen"
}
```

Done !



---

archive/issue_comments_065275.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-09T17:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65275",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065276.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-09T20:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65276",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_065277.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T20:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65277",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065278.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-14T15:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65278",
    "user": "mhansen"
}
```

Resolution: fixed
