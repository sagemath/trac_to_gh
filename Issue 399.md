# Issue 399: [with patch] PHCpack interface improvement

archive/issues_000399.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: phc, homotopy, polynomial solutions\n\nI have rewritten the PHCpack interface (phc.py in interfaces) to work in blackbox mode and to parse the solutions into a list of dictionaries.  The solutions are given as elements of the ComplexField.\n\nIssue created by migration from https://trac.sagemath.org/ticket/399\n\n",
    "closed_at": "2007-10-19T01:45:09Z",
    "created_at": "2007-07-03T16:57:24Z",
    "labels": [
        "component: numerical",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "[with patch] PHCpack interface improvement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/399",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mhampton

Keywords: phc, homotopy, polynomial solutions

I have rewritten the PHCpack interface (phc.py in interfaces) to work in blackbox mode and to parse the solutions into a list of dictionaries.  The solutions are given as elements of the ComplexField.

Issue created by migration from https://trac.sagemath.org/ticket/399





---

archive/issue_comments_001953.json:
```json
{
    "body": "Attachment [phc.py](tarball://root/attachments/some-uuid/ticket399/phc.py) by mhampton created at 2007-07-03 16:57:38",
    "created_at": "2007-07-03T16:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/399#issuecomment-1953",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [phc.py](tarball://root/attachments/some-uuid/ticket399/phc.py) by mhampton created at 2007-07-03 16:57:38



---

archive/issue_comments_001954.json:
```json
{
    "body": "Attachment [phc.patch](tarball://root/attachments/some-uuid/ticket399/phc.patch) by mabshoff created at 2007-08-24 12:59:08",
    "created_at": "2007-08-24T12:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/399#issuecomment-1954",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [phc.patch](tarball://root/attachments/some-uuid/ticket399/phc.patch) by mabshoff created at 2007-08-24 12:59:08



---

archive/issue_events_000957.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-24T12:59:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/399#event-957"
}
```



---

archive/issue_comments_001955.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2007-09-11T17:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/399#issuecomment-1955",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Resolution: wontfix



---

archive/issue_comments_001956.json:
```json
{
    "body": "The PHCpack developers are working on a slicker interface than mine, so my interface doesn't need to be added.",
    "created_at": "2007-09-11T17:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/399#issuecomment-1956",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

The PHCpack developers are working on a slicker interface than mine, so my interface doesn't need to be added.



---

archive/issue_events_000958.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mhampton",
    "created_at": "2007-09-11T17:09:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/399#event-958"
}
```



---

archive/issue_comments_001957.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-11T22:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/399#issuecomment-1957",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_000959.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-11T22:59:04Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/399#event-959"
}
```



---

archive/issue_comments_001958.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2007-09-11T22:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/399#issuecomment-1958",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from wontfix to 



---

archive/issue_comments_001959.json:
```json
{
    "body": "Are you sure?  What's their timeframe?  I'm not convinced yours shouldn't be added.  They've been\nworking on a Python/SAGE interface for nearly a year now...",
    "created_at": "2007-09-11T22:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/399#issuecomment-1959",
    "user": "https://github.com/williamstein"
}
```

Are you sure?  What's their timeframe?  I'm not convinced yours shouldn't be added.  They've been
working on a Python/SAGE interface for nearly a year now...



---

archive/issue_events_000960.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-18T13:47:47Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/399#event-960"
}
```



---

archive/issue_events_000961.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-18T13:47:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/399#event-961"
}
```



---

archive/issue_comments_001960.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-19T01:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/399#issuecomment-1960",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000962.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-19T01:45:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/399",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/399#event-962"
}
```
