# Issue 1902: mistake in the documentation for gens for Finite field givaro

archive/issues_001902.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n> sage: sage.rings.finite_field_givaro.FiniteField_givaro.gen?\n> [...]\n> Docstring:\n> \n>             Return a generator of self. All elements x of self are\n>             expressed as log_{self.gen()}(p) internally. If self is\n>             a prime field this method returns 1.\n> \n> (The sentence \"If self is a prime field...\" is wrong, but the first\n> sentence is correct.)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1902\n\n",
    "created_at": "2008-01-24T00:37:08Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "mistake in the documentation for gens for Finite field givaro",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1902",
    "user": "was"
}
```
Assignee: somebody


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

archive/issue_comments_012042.json:
```json
{
    "body": "Attachment [8683.patch](tarball://root/attachments/some-uuid/ticket1902/8683.patch) by cremona created at 2008-03-01 16:31:24\n\nAttached patch corrects the docstring and adds a new doctest which is relevant,",
    "created_at": "2008-03-01T16:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12042",
    "user": "cremona"
}
```

Attachment [8683.patch](tarball://root/attachments/some-uuid/ticket1902/8683.patch) by cremona created at 2008-03-01 16:31:24

Attached patch corrects the docstring and adds a new doctest which is relevant,



---

archive/issue_comments_012043.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-01T16:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12043",
    "user": "cremona"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012044.json:
```json
{
    "body": "Changing assignee from somebody to cremona.",
    "created_at": "2008-03-01T16:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12044",
    "user": "cremona"
}
```

Changing assignee from somebody to cremona.



---

archive/issue_comments_012045.json:
```json
{
    "body": "Attachment [edited-8683.patch](tarball://root/attachments/some-uuid/ticket1902/edited-8683.patch) by cwitty created at 2008-03-01 18:12:33\n\nI hand-edited John's original 8683.patch to create edited-8683.patch: I changed \"primitve\" -> \"primitive\".\n\nWith this revised patch: looks good, the doctest passes.",
    "created_at": "2008-03-01T18:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12045",
    "user": "cwitty"
}
```

Attachment [edited-8683.patch](tarball://root/attachments/some-uuid/ticket1902/edited-8683.patch) by cwitty created at 2008-03-01 18:12:33

I hand-edited John's original 8683.patch to create edited-8683.patch: I changed "primitve" -> "primitive".

With this revised patch: looks good, the doctest passes.



---

archive/issue_comments_012046.json:
```json
{
    "body": "Merged edited-8683.patch in Sage 2.10.3.rc1",
    "created_at": "2008-03-02T17:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12046",
    "user": "mabshoff"
}
```

Merged edited-8683.patch in Sage 2.10.3.rc1



---

archive/issue_comments_012047.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-02T17:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1902#issuecomment-12047",
    "user": "mabshoff"
}
```

Resolution: fixed
