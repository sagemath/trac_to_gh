# Issue 4978: [with spkg, positive review] fix NTL tuning issue on Linux/ppc64

archive/issues_004978.json:
```json
{
    "body": "Assignee: mabshoff\n\nspkg-install has the following:\n\n```\n    # Do performance tuning steps.\n    if [ `uname` = \"Linux\" -a `uname -m` = \"ppc64\" ]; then\n        echo \"NTL auto tuning is broken on Linux ppc64.  Please report this to Victor Shoup.  Thanks.\"\n    else\n        do_tune\n    fi\n```\nI cannot imagine the tuning code being broken and even if it is the spkg should still at least build, so fix it.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4978\n\n",
    "closed_at": "2009-01-29T04:06:01Z",
    "created_at": "2009-01-14T22:55:53Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with spkg, positive review] fix NTL tuning issue on Linux/ppc64",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4978",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

spkg-install has the following:

```
    # Do performance tuning steps.
    if [ `uname` = "Linux" -a `uname -m` = "ppc64" ]; then
        echo "NTL auto tuning is broken on Linux ppc64.  Please report this to Victor Shoup.  Thanks."
    else
        do_tune
    fi
```
I cannot imagine the tuning code being broken and even if it is the spkg should still at least build, so fix it.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4978





---

archive/issue_comments_037881.json:
```json
{
    "body": "> I cannot imagine ... being broken ...\n\n\nFamous last words :-)",
    "created_at": "2009-01-15T03:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4978#issuecomment-37881",
    "user": "https://github.com/williamstein"
}
```

> I cannot imagine ... being broken ...


Famous last words :-)



---

archive/issue_comments_037882.json:
```json
{
    "body": "The issue is fixed via the spkg at #5040.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T03:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4978#issuecomment-37882",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue is fixed via the spkg at #5040.

Cheers,

Michael



---

archive/issue_comments_037883.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-29T03:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4978#issuecomment-37883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_011511.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-29T03:32:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4978",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4978#event-11511"
}
```



---

archive/issue_comments_037884.json:
```json
{
    "body": "Indirect positive review by Carl Witty via #5040.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T04:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4978#issuecomment-37884",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Indirect positive review by Carl Witty via #5040.

Cheers,

Michael



---

archive/issue_comments_037885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T04:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4978#issuecomment-37885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011512.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-29T04:06:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4978",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4978#event-11512"
}
```



---

archive/issue_comments_037886.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T04:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4978#issuecomment-37886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
