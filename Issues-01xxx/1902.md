# Issue 1902: [with patch, positive review] mistake in the documentation for gens for Finite field givaro

archive/issues_001902.json:
```json
{
    "body": "Assignee: @JohnCremona\n\n```\n> sage: sage.rings.finite_field_givaro.FiniteField_givaro.gen?\n> [...]\n> Docstring:\n> \n>             Return a generator of self. All elements x of self are\n>             expressed as log_{self.gen()}(p) internally. If self is\n>             a prime field this method returns 1.\n> \n> (The sentence \"If self is a prime field...\" is wrong, but the first\n> sentence is correct.)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1902\n\n",
    "closed_at": "2008-03-02T17:12:17Z",
    "created_at": "2008-01-24T00:37:08Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, positive review] mistake in the documentation for gens for Finite field givaro",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1902",
    "user": "https://github.com/williamstein"
}
```
Assignee: @JohnCremona

```
> sage: sage.rings.finite_field_givaro.FiniteField_givaro.gen?
> [...]
> Docstring:
> 
>             Return a generator of self. All elements x of self are
>             expressed as log_{self.gen()}(p) internally. If self is
>             a prime field this method returns 1.
> 
> (The sentence "If self is a prime field..." is wrong, but the first
> sentence is correct.)
```

Issue created by migration from https://trac.sagemath.org/ticket/1902





---

archive/issue_comments_012012.json:
```json
{
    "body": "Attachment [8683.patch](tarball://root/attachments/some-uuid/ticket1902/8683.patch) by @JohnCremona created at 2008-03-01 16:31:24\n\nAttached patch corrects the docstring and adds a new doctest which is relevant,",
    "created_at": "2008-03-01T16:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12012",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [8683.patch](tarball://root/attachments/some-uuid/ticket1902/8683.patch) by @JohnCremona created at 2008-03-01 16:31:24

Attached patch corrects the docstring and adds a new doctest which is relevant,



---

archive/issue_comments_012013.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-01T16:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12013",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012014.json:
```json
{
    "body": "Changing assignee from somebody to @JohnCremona.",
    "created_at": "2008-03-01T16:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12014",
    "user": "https://github.com/JohnCremona"
}
```

Changing assignee from somebody to @JohnCremona.



---

archive/issue_comments_012015.json:
```json
{
    "body": "Attachment [edited-8683.patch](tarball://root/attachments/some-uuid/ticket1902/edited-8683.patch) by cwitty created at 2008-03-01 18:12:33\n\nI hand-edited John's original 8683.patch to create edited-8683.patch: I changed \"primitve\" -> \"primitive\".\n\nWith this revised patch: looks good, the doctest passes.",
    "created_at": "2008-03-01T18:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12015",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [edited-8683.patch](tarball://root/attachments/some-uuid/ticket1902/edited-8683.patch) by cwitty created at 2008-03-01 18:12:33

I hand-edited John's original 8683.patch to create edited-8683.patch: I changed "primitve" -> "primitive".

With this revised patch: looks good, the doctest passes.



---

archive/issue_comments_012016.json:
```json
{
    "body": "Merged edited-8683.patch in Sage 2.10.3.rc1",
    "created_at": "2008-03-02T17:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12016",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged edited-8683.patch in Sage 2.10.3.rc1



---

archive/issue_events_004583.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-02T17:12:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1902#event-4583"
}
```



---

archive/issue_comments_012017.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-02T17:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12017",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
