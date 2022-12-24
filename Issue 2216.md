# Issue 2216: Creating an order in a number field --> infinite loop?

archive/issues_002216.json:
```json
{
    "body": "Assignee: @williamstein\n\nSo I just tried the following:\n\n\n```\nsage: F.<alpha> = NumberField(x**4+3)\nsage: F.order([alpha**2], allow_subfield=True)\n```\n\n\nand it seemed to go into an infinite loop. (Maybe I'm impatient, but it doesn't seem like it should take more than 2 seconds to do this, nevermind the minute I waited.) I haven't looked to see what the problem is at all.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2216\n\n",
    "created_at": "2008-02-20T01:57:12Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "Creating an order in a number field --> infinite loop?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2216",
    "user": "@craigcitro"
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

archive/issue_comments_014652.json:
```json
{
    "body": "It was indeed an infinite loop in absolute_order_from_module_generators().  See the attached patch.",
    "created_at": "2008-04-25T01:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14652",
    "user": "@aghitza"
}
```

It was indeed an infinite loop in absolute_order_from_module_generators().  See the attached patch.



---

archive/issue_comments_014653.json:
```json
{
    "body": "Looks good, with one trivial change: I think we should take out the line that says \"This shows that trac #2216 has been fixed.\" This is useful to people editing the code, but not to the user -- and that's who the docstring **should** be for ...",
    "created_at": "2008-04-26T11:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14653",
    "user": "@craigcitro"
}
```

Looks good, with one trivial change: I think we should take out the line that says "This shows that trac #2216 has been fixed." This is useful to people editing the code, but not to the user -- and that's who the docstring **should** be for ...



---

archive/issue_comments_014654.json:
```json
{
    "body": "revised patch",
    "created_at": "2008-04-26T13:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14654",
    "user": "@aghitza"
}
```

revised patch



---

archive/issue_comments_014655.json:
```json
{
    "body": "Attachment [2216-order_bug.patch](tarball://root/attachments/some-uuid/ticket2216/2216-order_bug.patch) by @aghitza created at 2008-04-26 13:42:30\n\nI've replaced the patch with one in which \"trac #2216 has been fixed\" is changed into something more informative for the user (\"an order in a subfield\").",
    "created_at": "2008-04-26T13:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14655",
    "user": "@aghitza"
}
```

Attachment [2216-order_bug.patch](tarball://root/attachments/some-uuid/ticket2216/2216-order_bug.patch) by @aghitza created at 2008-04-26 13:42:30

I've replaced the patch with one in which "trac #2216 has been fixed" is changed into something more informative for the user ("an order in a subfield").



---

archive/issue_comments_014656.json:
```json
{
    "body": "I still think that mentioning the trac ticket when adding a specific doctest is a good thing. So combining both, i.e. a description that is useful for the user as well as (fixes #2216) in a good compromise.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T22:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14656",
    "user": "mabshoff"
}
```

I still think that mentioning the trac ticket when adding a specific doctest is a good thing. So combining both, i.e. a description that is useful for the user as well as (fixes #2216) in a good compromise.

Cheers,

Michael



---

archive/issue_comments_014657.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T22:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14657",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014658.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-26T22:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2216#issuecomment-14658",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha0
