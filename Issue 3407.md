# Issue 3407: [with patch, positive review] better error handling for GB calculations

archive/issues_003407.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @JohnCremona wstein @mwhansen\n\nKeywords: editor_malb\n\n* bail out of toy_buchberger if the term ordering is unknown\n* bail out of Singular conversion if number field is relative. Singular supports this, but our conversion not just yet.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3407\n\n",
    "closed_at": "2008-06-25T00:39:36Z",
    "created_at": "2008-06-12T22:42:15Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, positive review] better error handling for GB calculations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3407",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @JohnCremona wstein @mwhansen

Keywords: editor_malb

* bail out of toy_buchberger if the term ordering is unknown
* bail out of Singular conversion if number field is relative. Singular supports this, but our conversion not just yet.

Issue created by migration from https://trac.sagemath.org/ticket/3407





---

archive/issue_comments_023848.json:
```json
{
    "body": "Attachment [gb_errors.patch](tarball://root/attachments/some-uuid/ticket3407/gb_errors.patch) by @craigcitro created at 2008-06-15 21:54:18",
    "created_at": "2008-06-15T21:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23848",
    "user": "https://github.com/craigcitro"
}
```

Attachment [gb_errors.patch](tarball://root/attachments/some-uuid/ticket3407/gb_errors.patch) by @craigcitro created at 2008-06-15 21:54:18



---

archive/issue_comments_023849.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_malb\".",
    "created_at": "2008-06-15T21:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23849",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_malb".



---

archive/issue_comments_023850.json:
```json
{
    "body": "IIRC mhansen wants to review it. mhansen can you confirm or deny.",
    "created_at": "2008-06-16T03:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23850",
    "user": "https://github.com/malb"
}
```

IIRC mhansen wants to review it. mhansen can you confirm or deny.



---

archive/issue_comments_023851.json:
```json
{
    "body": "Yep -- I'll do it in the next hour.",
    "created_at": "2008-06-16T03:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23851",
    "user": "https://github.com/mwhansen"
}
```

Yep -- I'll do it in the next hour.



---

archive/issue_comments_023852.json:
```json
{
    "body": "I am seeing doctest failures:\n\n```\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 13 doctests failed\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 13 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 1 doctests failed\n```\n#3406 shows issue in similar areas.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-23T08:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23852",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am seeing doctest failures:

```
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 13 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 13 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 1 doctests failed
```
#3406 shows issue in similar areas.

Cheers,

Michael



---

archive/issue_events_007684.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-23T08:47:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3407#event-7684"
}
```



---

archive/issue_comments_023853.json:
```json
{
    "body": "After fixing #3406.\n\n```\nsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py\nsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py\nsage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\n----------------------------------------------------------------------\nAll tests passed!\n```\n\nSince this patch depends on #3406 anyway, I'll add the positive review back.",
    "created_at": "2008-06-23T17:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23853",
    "user": "https://github.com/malb"
}
```

After fixing #3406.

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py
sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
----------------------------------------------------------------------
All tests passed!
```

Since this patch depends on #3406 anyway, I'll add the positive review back.



---

archive/issue_events_007685.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-25T00:39:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3407#event-7685"
}
```



---

archive/issue_comments_023854.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T00:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_023855.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T00:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3407#issuecomment-23855",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
