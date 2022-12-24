# Issue 6205: add __invert__ to number field morphism

archive/issues_006205.json:
```json
{
    "body": "Assignee: was\n\nCC:  craigcitro fwclarke\n\nKeywords: number field morphism invert\n\nThis tiny patch does the linear algebra to invert an endomorphism of a number field.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6205\n\n",
    "created_at": "2009-06-04T03:42:36Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "add __invert__ to number field morphism",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6205",
    "user": "ncalexan"
}
```
Assignee: was

CC:  craigcitro fwclarke

Keywords: number field morphism invert

This tiny patch does the linear algebra to invert an endomorphism of a number field.

Issue created by migration from https://trac.sagemath.org/ticket/6205





---

archive/issue_comments_049575.json:
```json
{
    "body": "Attachment [trac_6205-number_field-morphism-invert.patch](tarball://root/attachments/some-uuid/ticket6205/trac_6205-number_field-morphism-invert.patch) by mhansen created at 2009-06-04 05:35:23",
    "created_at": "2009-06-04T05:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6205#issuecomment-49575",
    "user": "mhansen"
}
```

Attachment [trac_6205-number_field-morphism-invert.patch](tarball://root/attachments/some-uuid/ticket6205/trac_6205-number_field-morphism-invert.patch) by mhansen created at 2009-06-04 05:35:23



---

archive/issue_comments_049576.json:
```json
{
    "body": "I like it. My only minor quibble is that I would add the one line \"Return the inverse of self.\" to the docstring, even though it really adds no value whatsoever. \n\nSo since there were no methods in that class before, and 1 now, does that mean this patch makes number field homomorphisms infniitely more useful? `:)`",
    "created_at": "2009-06-05T05:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6205#issuecomment-49576",
    "user": "craigcitro"
}
```

I like it. My only minor quibble is that I would add the one line "Return the inverse of self." to the docstring, even though it really adds no value whatsoever. 

So since there were no methods in that class before, and 1 now, does that mean this patch makes number field homomorphisms infniitely more useful? `:)`



---

archive/issue_comments_049577.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T20:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6205#issuecomment-49577",
    "user": "ncalexan"
}
```

Resolution: fixed
