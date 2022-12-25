# Issue 2216: Creating an order in a number field --> infinite loop?

archive/issues_002216.json:
```json
{
    "body": "Assignee: @williamstein\n\nSo I just tried the following:\n\n\n```\nsage: F.<alpha> = NumberField(x**4+3)\nsage: F.order([alpha**2], allow_subfield=True)\n```\n\n\nand it seemed to go into an infinite loop. (Maybe I'm impatient, but it doesn't seem like it should take more than 2 seconds to do this, nevermind the minute I waited.) I haven't looked to see what the problem is at all.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2216\n\n",
    "created_at": "2008-02-20T01:57:12Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "Creating an order in a number field --> infinite loop?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2216",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @williamstein

So I just tried the following:


```
sage: F.<alpha> = NumberField(x**4+3)
sage: F.order([alpha**2], allow_subfield=True)
```


and it seemed to go into an infinite loop. (Maybe I'm impatient, but it doesn't seem like it should take more than 2 seconds to do this, nevermind the minute I waited.) I haven't looked to see what the problem is at all.

Issue created by migration from https://trac.sagemath.org/ticket/2216





---

archive/issue_comments_014621.json:
```json
{
    "body": "It was indeed an infinite loop in absolute_order_from_module_generators().  See the attached patch.",
    "created_at": "2008-04-25T01:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14621",
    "user": "https://github.com/aghitza"
}
```

It was indeed an infinite loop in absolute_order_from_module_generators().  See the attached patch.



---

archive/issue_comments_014622.json:
```json
{
    "body": "Looks good, with one trivial change: I think we should take out the line that says \"This shows that trac #2216 has been fixed.\" This is useful to people editing the code, but not to the user -- and that's who the docstring **should** be for ...",
    "created_at": "2008-04-26T11:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14622",
    "user": "https://github.com/craigcitro"
}
```

Looks good, with one trivial change: I think we should take out the line that says "This shows that trac #2216 has been fixed." This is useful to people editing the code, but not to the user -- and that's who the docstring **should** be for ...



---

archive/issue_comments_014623.json:
```json
{
    "body": "revised patch",
    "created_at": "2008-04-26T13:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14623",
    "user": "https://github.com/aghitza"
}
```

revised patch



---

archive/issue_comments_014624.json:
```json
{
    "body": "Attachment [2216-order_bug.patch](tarball://root/attachments/some-uuid/ticket2216/2216-order_bug.patch) by @aghitza created at 2008-04-26 13:42:30\n\nI've replaced the patch with one in which \"trac #2216 has been fixed\" is changed into something more informative for the user (\"an order in a subfield\").",
    "created_at": "2008-04-26T13:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14624",
    "user": "https://github.com/aghitza"
}
```

Attachment [2216-order_bug.patch](tarball://root/attachments/some-uuid/ticket2216/2216-order_bug.patch) by @aghitza created at 2008-04-26 13:42:30

I've replaced the patch with one in which "trac #2216 has been fixed" is changed into something more informative for the user ("an order in a subfield").



---

archive/issue_comments_014625.json:
```json
{
    "body": "I still think that mentioning the trac ticket when adding a specific doctest is a good thing. So combining both, i.e. a description that is useful for the user as well as (fixes #2216) in a good compromise.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T22:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14625",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I still think that mentioning the trac ticket when adding a specific doctest is a good thing. So combining both, i.e. a description that is useful for the user as well as (fixes #2216) in a good compromise.

Cheers,

Michael



---

archive/issue_comments_014626.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T22:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14626",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014627.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-26T22:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14627",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha0
