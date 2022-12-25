# Issue 5979: Parent: fixes broken (implicit) invariant between ._element_constructor and self._element_init_pass_parent

archive/issues_005979.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: coercion, parents, element_constructor\n\nIn Parent, there is an implicit invariant, namely that\n\n\tself._element_init_pass_parent == guess_pass_parent(between ._element_constructor)\n\nThis invariant was broken when self._element_constructor was set from\nself._element_constructor_ by __call__. This made the parent not to be\npassed properly to _element_constructor.\n\nThe category patch #5891 depends heavily on this one, as this way of\nsetting _element_constructor becomes the default one for simple\nparents.\n\nBy the way, this patch makes a related trivial fix to a line that is\napparently never used in coerce_maps, and adds a comment about it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5979\n\n",
    "created_at": "2009-05-04T16:40:54Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "Parent: fixes broken (implicit) invariant between ._element_constructor and self._element_init_pass_parent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5979",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: coercion, parents, element_constructor

In Parent, there is an implicit invariant, namely that

	self._element_init_pass_parent == guess_pass_parent(between ._element_constructor)

This invariant was broken when self._element_constructor was set from
self._element_constructor_ by __call__. This made the parent not to be
passed properly to _element_constructor.

The category patch #5891 depends heavily on this one, as this way of
setting _element_constructor becomes the default one for simple
parents.

By the way, this patch makes a related trivial fix to a line that is
apparently never used in coerce_maps, and adds a comment about it.

Issue created by migration from https://trac.sagemath.org/ticket/5979





---

archive/issue_comments_047398.json:
```json
{
    "body": "Attachment [parent-element_constructor-fix-5979-submitted.patch](tarball://root/attachments/some-uuid/ticket5979/parent-element_constructor-fix-5979-submitted.patch) by @nthiery created at 2009-05-04 16:52:18",
    "created_at": "2009-05-04T16:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5979#issuecomment-47398",
    "user": "https://github.com/nthiery"
}
```

Attachment [parent-element_constructor-fix-5979-submitted.patch](tarball://root/attachments/some-uuid/ticket5979/parent-element_constructor-fix-5979-submitted.patch) by @nthiery created at 2009-05-04 16:52:18



---

archive/issue_comments_047399.json:
```json
{
    "body": "I should mention that sage -testall passes smoothly with sage-3.4.2-alpha0 (except for a trivial broken test in interfaces.r which also fails before applying the patch).\nHaven't tried it with sage-3.4.2 final (under compilation)",
    "created_at": "2009-05-04T18:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5979#issuecomment-47399",
    "user": "https://github.com/nthiery"
}
```

I should mention that sage -testall passes smoothly with sage-3.4.2-alpha0 (except for a trivial broken test in interfaces.r which also fails before applying the patch).
Haven't tried it with sage-3.4.2 final (under compilation)



---

archive/issue_comments_047400.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T06:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5979#issuecomment-47400",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047401.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T00:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5979#issuecomment-47401",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_047402.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T00:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5979#issuecomment-47402",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.alpha0.
