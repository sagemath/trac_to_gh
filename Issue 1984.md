# Issue 1984: make html documentation error

archive/issues_001984.json:
```json
{
    "body": "Assignee: tba\n\nin v2.10, after the build process is complete, change directories to devel/doc and run make html. This gives an emergency stop on \\`@`mathbf when processing ref.toc. In order to successfully generate the HTML documentation I  had to first run \n\nsed -i -e \"s/`@`mathbf/mathbf/g\" ../doc-main/ref/ref.toc\n\nwhich simply removed the unnecessary '`@`' sign before mathbf.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1984\n\n",
    "closed_at": "2009-02-26T17:22:48Z",
    "created_at": "2008-01-30T13:42:31Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "make html documentation error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1984",
    "user": "https://trac.sagemath.org/admin/accounts/users/pgrinber"
}
```
Assignee: tba

in v2.10, after the build process is complete, change directories to devel/doc and run make html. This gives an emergency stop on \`@`mathbf when processing ref.toc. In order to successfully generate the HTML documentation I  had to first run 

sed -i -e "s/`@`mathbf/mathbf/g" ../doc-main/ref/ref.toc

which simply removed the unnecessary '`@`' sign before mathbf.

Issue created by migration from https://trac.sagemath.org/ticket/1984





---

archive/issue_comments_012821.json:
```json
{
    "body": "In my experience, it also suffices to simply remove ref.toc.  Probably we should not be shipping this file at all.",
    "created_at": "2008-01-30T18:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1984#issuecomment-12821",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

In my experience, it also suffices to simply remove ref.toc.  Probably we should not be shipping this file at all.



---

archive/issue_comments_012822.json:
```json
{
    "body": "This will be irrelevant once the Sphinx docs are in so I'm not going to work it.",
    "created_at": "2009-01-22T08:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1984#issuecomment-12822",
    "user": "https://github.com/mwhansen"
}
```

This will be irrelevant once the Sphinx docs are in so I'm not going to work it.



---

archive/issue_comments_012823.json:
```json
{
    "body": "This can be closed now.",
    "created_at": "2009-02-26T17:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1984#issuecomment-12823",
    "user": "https://github.com/jhpalmieri"
}
```

This can be closed now.



---

archive/issue_comments_012824.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-26T17:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1984#issuecomment-12824",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_012825.json:
```json
{
    "body": "Good catch.  Closed due to #5330.",
    "created_at": "2009-02-26T17:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1984#issuecomment-12825",
    "user": "https://github.com/mwhansen"
}
```

Good catch.  Closed due to #5330.



---

archive/issue_events_004789.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-02-26T17:22:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1984",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1984#event-4789"
}
```



---

archive/issue_events_004790.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-02-26T17:22:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1984",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1984#event-4790"
}
```
