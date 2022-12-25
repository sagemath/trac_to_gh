# Issue 6909: [with patch, needs review]

archive/issues_006909.json:
```json
{
    "body": "Assignee: @malb\n\nImplement a couple of functions using the new libsingular functions interface (#6628).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6909\n\n",
    "created_at": "2009-09-09T16:36:50Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with patch, needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6909",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

Implement a couple of functions using the new libsingular functions interface (#6628).

Issue created by migration from https://trac.sagemath.org/ticket/6909





---

archive/issue_comments_056965.json:
```json
{
    "body": "Attachment [libsingular_more_functions.patch](tarball://root/attachments/some-uuid/ticket6909/libsingular_more_functions.patch) by @malb created at 2009-09-09 16:40:26\n\nThe attached patch\n* implements a Pythonic interface to the Singular options \n* fixes a bug where local orderings were not used correctly \n* switches `groebner_basis()` and `elimination_ideal()` to libsingular.\n\nFor most functions on multivariate polynomial ideals we first need to wrap libSingular lists since many functions return lists. This would require an updated SPKG.",
    "created_at": "2009-09-09T16:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6909#issuecomment-56965",
    "user": "https://github.com/malb"
}
```

Attachment [libsingular_more_functions.patch](tarball://root/attachments/some-uuid/ticket6909/libsingular_more_functions.patch) by @malb created at 2009-09-09 16:40:26

The attached patch
* implements a Pythonic interface to the Singular options 
* fixes a bug where local orderings were not used correctly 
* switches `groebner_basis()` and `elimination_ideal()` to libsingular.

For most functions on multivariate polynomial ideals we first need to wrap libSingular lists since many functions return lists. This would require an updated SPKG.



---

archive/issue_comments_056966.json:
```json
{
    "body": "Hi,\nI spent 10 minutes reading the code and like it (this is not a formal review).\nCheers,\nMichael",
    "created_at": "2009-10-05T12:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6909#issuecomment-56966",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Hi,
I spent 10 minutes reading the code and like it (this is not a formal review).
Cheers,
Michael



---

archive/issue_comments_056967.json:
```json
{
    "body": "rebased to 4.1.2.rc0",
    "created_at": "2009-10-11T15:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6909#issuecomment-56967",
    "user": "https://github.com/burcin"
}
```

rebased to 4.1.2.rc0



---

archive/issue_comments_056968.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-11T15:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6909#issuecomment-56968",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_016237.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2009-10-11T15:07:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6909",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6909#event-16237"
}
```



---

archive/issue_comments_056969.json:
```json
{
    "body": "Attachment [trac_6909-libsingular_more_functions.patch](tarball://root/attachments/some-uuid/ticket6909/trac_6909-libsingular_more_functions.patch) by @burcin created at 2009-10-11 15:07:46\n\nPositive review.\n\nApply only attachment:trac_6909-libsingular_more_functions.patch, which is a rebase of Martin's patch to 4.1.2.rc0.",
    "created_at": "2009-10-11T15:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6909#issuecomment-56969",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6909-libsingular_more_functions.patch](tarball://root/attachments/some-uuid/ticket6909/trac_6909-libsingular_more_functions.patch) by @burcin created at 2009-10-11 15:07:46

Positive review.

Apply only attachment:trac_6909-libsingular_more_functions.patch, which is a rebase of Martin's patch to 4.1.2.rc0.



---

archive/issue_comments_056970.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-16T04:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6909#issuecomment-56970",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_016238.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-16T04:59:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6909",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6909#event-16238"
}
```
