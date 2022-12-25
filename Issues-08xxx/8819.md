# Issue 8819: warnings in building documentation of Sage 4.4.2.alpha0

archive/issues_008819.json:
```json
{
    "body": "Assignee: mvngu\n\nBuilding the documentation of Sage 4.4.1.alpha2 results in the following warnings in the reference manual:\n\n```\ndocstring of sage.calculus.interpolators.CCSpline.derivative:7: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\ndocstring of sage.calculus.interpolators.CCSpline.value:6: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\ndocstring of sage.calculus.interpolators.PSpline.derivative:7: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\ndocstring of sage.calculus.interpolators.PSpline.value:7: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/lib/python2.6/site-packages/sage/modular/modsym/space.py:docstring of sage.modular.modsym.space.ModularSymbolsSpace.abvarquo_rational_cuspidal_subgroup:13: (WARNING/2) Literal block expected; none found.\n```\n\nThe same warnings also appear when building the reference manual of Sage 4.4.2.alpha0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8819\n\n",
    "closed_at": "2010-05-12T22:46:28Z",
    "created_at": "2010-04-29T08:26:34Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "warnings in building documentation of Sage 4.4.2.alpha0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8819",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

Building the documentation of Sage 4.4.1.alpha2 results in the following warnings in the reference manual:

```
docstring of sage.calculus.interpolators.CCSpline.derivative:7: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
docstring of sage.calculus.interpolators.CCSpline.value:6: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
docstring of sage.calculus.interpolators.PSpline.derivative:7: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
docstring of sage.calculus.interpolators.PSpline.value:7: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/lib/python2.6/site-packages/sage/modular/modsym/space.py:docstring of sage.modular.modsym.space.ModularSymbolsSpace.abvarquo_rational_cuspidal_subgroup:13: (WARNING/2) Literal block expected; none found.
```

The same warnings also appear when building the reference manual of Sage 4.4.2.alpha0.

Issue created by migration from https://trac.sagemath.org/ticket/8819





---

archive/issue_comments_080810.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-29T09:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8819#issuecomment-80810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080811.json:
```json
{
    "body": "Attachment [trac_8819-doc-warnings.patch](tarball://root/attachments/some-uuid/ticket8819/trac_8819-doc-warnings.patch) by mvngu created at 2010-04-30 20:37:19\n\nbased on Sage 4.4.1.alpha2",
    "created_at": "2010-04-30T20:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8819#issuecomment-80811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8819-doc-warnings.patch](tarball://root/attachments/some-uuid/ticket8819/trac_8819-doc-warnings.patch) by mvngu created at 2010-04-30 20:37:19

based on Sage 4.4.1.alpha2



---

archive/issue_comments_080812.json:
```json
{
    "body": "Changing priority from blocker to minor.",
    "created_at": "2010-05-03T00:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8819#issuecomment-80812",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing priority from blocker to minor.



---

archive/issue_comments_080813.json:
```json
{
    "body": "Patch applies fine to 4.4.2.alpha0.  docbuild reference html produced no warnings or errors.  The html files which are changed look ok (not perfect, e.g. some more math markup would be nice, but that is not the issue here).\n\nHence positive review.",
    "created_at": "2010-05-11T15:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8819#issuecomment-80813",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies fine to 4.4.2.alpha0.  docbuild reference html produced no warnings or errors.  The html files which are changed look ok (not perfect, e.g. some more math markup would be nice, but that is not the issue here).

Hence positive review.



---

archive/issue_comments_080814.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-11T15:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8819#issuecomment-80814",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021507.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-12T22:46:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8819",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8819#event-21507"
}
```



---

archive/issue_comments_080815.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-12T22:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8819#issuecomment-80815",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
