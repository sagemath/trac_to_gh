# Issue 5609: [with patch, needs review] some functions for BooleanPolynomialIdeal

archive/issues_005609.json:
```json
{
    "body": "Assignee: malb\n\nCC:  polybori burcin rpw\n\nKeywords: polybori\n\nAdded `interreduced_basis()` and `__cmp__()` functions to `BooleanPolynomialIdeal`. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5609\n\n",
    "created_at": "2009-03-25T16:00:22Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] some functions for BooleanPolynomialIdeal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5609",
    "user": "malb"
}
```
Assignee: malb

CC:  polybori burcin rpw

Keywords: polybori

Added `interreduced_basis()` and `__cmp__()` functions to `BooleanPolynomialIdeal`. 

Issue created by migration from https://trac.sagemath.org/ticket/5609





---

archive/issue_comments_043783.json:
```json
{
    "body": "the attached patch depends on #5586 and #5576",
    "created_at": "2009-03-25T16:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5609#issuecomment-43783",
    "user": "malb"
}
```

the attached patch depends on #5586 and #5576



---

archive/issue_comments_043784.json:
```json
{
    "body": "Just a question after reading the patch: \n\nWhy do you implement both `__cmp__()` and `__richcmp__()` in `BooleanPolynomialIdeal`? The doctests for these two functions also seem to be the same.",
    "created_at": "2009-03-25T18:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5609#issuecomment-43784",
    "user": "burcin"
}
```

Just a question after reading the patch: 

Why do you implement both `__cmp__()` and `__richcmp__()` in `BooleanPolynomialIdeal`? The doctests for these two functions also seem to be the same.



---

archive/issue_comments_043785.json:
```json
{
    "body": "It is just because I am confused which one I have to implement (it seem Cython changed in that regard?)",
    "created_at": "2009-03-25T18:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5609#issuecomment-43785",
    "user": "malb"
}
```

It is just because I am confused which one I have to implement (it seem Cython changed in that regard?)



---

archive/issue_comments_043786.json:
```json
{
    "body": "I removed the `__richcmp__`, Burcin can you review this new patch?",
    "created_at": "2009-04-27T13:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5609#issuecomment-43786",
    "user": "malb"
}
```

I removed the `__richcmp__`, Burcin can you review this new patch?



---

archive/issue_comments_043787.json:
```json
{
    "body": "rebased to 3.4.2",
    "created_at": "2009-05-12T01:16:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5609#issuecomment-43787",
    "user": "malb"
}
```

rebased to 3.4.2



---

archive/issue_comments_043788.json:
```json
{
    "body": "Attachment [pbori_interred.patch](tarball://root/attachments/some-uuid/ticket5609/pbori_interred.patch) by malb created at 2009-05-12 01:16:24\n\nrebased the attached patch to 3.4.2",
    "created_at": "2009-05-12T01:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5609#issuecomment-43788",
    "user": "malb"
}
```

Attachment [pbori_interred.patch](tarball://root/attachments/some-uuid/ticket5609/pbori_interred.patch) by malb created at 2009-05-12 01:16:24

rebased the attached patch to 3.4.2



---

archive/issue_comments_043789.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-05-12T15:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5609#issuecomment-43789",
    "user": "burcin"
}
```

Looks good to me.



---

archive/issue_comments_043790.json:
```json
{
    "body": "This patch completely moves the docstring of two `__init__` methods to the class. Is that the desired effect, i.e. why not add back minimal doctests? I understand that underscore and double underscore methods aren't in the manual, but this makes a difference for -coverage and ought to be fixed.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T21:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5609#issuecomment-43790",
    "user": "mabshoff"
}
```

This patch completely moves the docstring of two `__init__` methods to the class. Is that the desired effect, i.e. why not add back minimal doctests? I understand that underscore and double underscore methods aren't in the manual, but this makes a difference for -coverage and ought to be fixed.

Cheers,

Michael



---

archive/issue_comments_043791.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T21:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5609#issuecomment-43791",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043792.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T21:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5609#issuecomment-43792",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael
