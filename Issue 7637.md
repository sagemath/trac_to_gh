# Issue 7637: Default dictionary in MixedIntegerLinearProgram

archive/issues_007637.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @malb\n\nMartin Albrecht requested this functionality for his code, and it would also simplify mine. For short linear programs, of when some global variables do not require the creation of a new dictionary of variables ( from which only one field would be used ), this trick is good enough !\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7637\n\n",
    "closed_at": "2009-12-14T15:51:31Z",
    "created_at": "2009-12-09T12:27:25Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Default dictionary in MixedIntegerLinearProgram",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7637",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jkantor

CC:  @malb

Martin Albrecht requested this functionality for his code, and it would also simplify mine. For short linear programs, of when some global variables do not require the creation of a new dictionary of variables ( from which only one field would be used ), this trick is good enough !

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7637





---

archive/issue_comments_065157.json:
```json
{
    "body": "* `try: foo except AttributeError:` seems to be favoured in the Python community over `hasattr`. It is also faster if the attribute does in fact exist.\n  * Why do you call `__getitem__()` instead of using the normal syntax `[x]`?",
    "created_at": "2009-12-09T15:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65157",
    "user": "https://github.com/malb"
}
```

* `try: foo except AttributeError:` seems to be favoured in the Python community over `hasattr`. It is also faster if the attribute does in fact exist.
  * Why do you call `__getitem__()` instead of using the normal syntax `[x]`?



---

archive/issue_comments_065158.json:
```json
{
    "body": "Done !",
    "created_at": "2009-12-09T17:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65158",
    "user": "https://github.com/nathanncohen"
}
```

Done !



---

archive/issue_comments_065159.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-09T17:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65159",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065160.json:
```json
{
    "body": "Attachment [trac_7637.patch](tarball://root/attachments/some-uuid/ticket7637/trac_7637.patch) by @malb created at 2009-12-09 20:55:55",
    "created_at": "2009-12-09T20:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65160",
    "user": "https://github.com/malb"
}
```

Attachment [trac_7637.patch](tarball://root/attachments/some-uuid/ticket7637/trac_7637.patch) by @malb created at 2009-12-09 20:55:55



---

archive/issue_comments_065161.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T20:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65161",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_018162.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-14T15:51:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7637#event-18162"
}
```



---

archive/issue_comments_065162.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-14T15:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7637#issuecomment-65162",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_018163.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-14T16:40:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7637",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7637#event-18163"
}
```
