# Issue 6253: [with patch, needs review] Constant functions

archive/issues_006253.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @mwhansen @jasongrout\n\nKeywords: constant functions\n\nThis trivial patch adds basic support for constant functions\n\nSuch a function could be written as lambda x: constant, but that's not picklable. Besides, this should eventually be cythoned for speed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6253\n\n",
    "created_at": "2009-06-09T22:08:39Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] Constant functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6253",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat @mwhansen @jasongrout

Keywords: constant functions

This trivial patch adds basic support for constant functions

Such a function could be written as lambda x: constant, but that's not picklable. Besides, this should eventually be cythoned for speed.

Issue created by migration from https://trac.sagemath.org/ticket/6253





---

archive/issue_comments_049847.json:
```json
{
    "body": "Oh, I forgot to mention: let me know if this readily exists somewhere and I missed it.",
    "created_at": "2009-06-09T22:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49847",
    "user": "https://github.com/nthiery"
}
```

Oh, I forgot to mention: let me know if this readily exists somewhere and I missed it.



---

archive/issue_comments_049848.json:
```json
{
    "body": "How is this intended to be used?  What are your typical constants? Are there instances where you'd want a non-constant function to be used in the same place?",
    "created_at": "2009-06-09T22:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49848",
    "user": "https://github.com/mwhansen"
}
```

How is this intended to be used?  What are your typical constants? Are there instances where you'd want a non-constant function to be used in the same place?



---

archive/issue_comments_049849.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> How is this intended to be used?  \n\nOne of my use case looks like:\n\ndef my_objects(<some parameters>, predicate = ConstantFunction(True)):\n    \"\"\"\n    Returns all the objects blah blah blah (as an EnumeratedSet)\n    Optionally, a predicate can be specified to select only those objects satisfying the predicate\n\nAnother one looks like:\n\ndef generating_series(..., weight = ConstantFunction(1)):\n    ...\n\n> What are your typical constants? \n\nSo far, True, 1, Integer(1)\n\nBtw: with UniqueRepresentation, the two first yield the same constant function with the current implementation, thanks to this horror:\n\n    sage: { 1: 'a', True: 'b' }\n    {1: 'b'}\n\nFixed patch in a couple minutes.\n\n> Are there instances where you'd want a non-constant function to be used in the same place? \n\nYes. Actually, that's the case in all the situations I encountered so far",
    "created_at": "2009-06-10T07:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49849",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:2 mhansen]:
> How is this intended to be used?  

One of my use case looks like:

def my_objects(<some parameters>, predicate = ConstantFunction(True)):
    """
    Returns all the objects blah blah blah (as an EnumeratedSet)
    Optionally, a predicate can be specified to select only those objects satisfying the predicate

Another one looks like:

def generating_series(..., weight = ConstantFunction(1)):
    ...

> What are your typical constants? 

So far, True, 1, Integer(1)

Btw: with UniqueRepresentation, the two first yield the same constant function with the current implementation, thanks to this horror:

    sage: { 1: 'a', True: 'b' }
    {1: 'b'}

Fixed patch in a couple minutes.

> Are there instances where you'd want a non-constant function to be used in the same place? 

Yes. Actually, that's the case in all the situations I encountered so far



---

archive/issue_comments_049850.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-10T07:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49850",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049851.json:
```json
{
    "body": "Attachment [trac_6253-constant_function-nt.patch](tarball://root/attachments/some-uuid/ticket6253/trac_6253-constant_function-nt.patch) by @nthiery created at 2009-07-26 23:07:12",
    "created_at": "2009-07-26T23:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49851",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_6253-constant_function-nt.patch](tarball://root/attachments/some-uuid/ticket6253/trac_6253-constant_function-nt.patch) by @nthiery created at 2009-07-26 23:07:12



---

archive/issue_comments_049852.json:
```json
{
    "body": "The updated patch removes two unused imports spotted by Florent. Apply only this one.",
    "created_at": "2009-07-26T23:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49852",
    "user": "https://github.com/nthiery"
}
```

The updated patch removes two unused imports spotted by Florent. Apply only this one.



---

archive/issue_comments_049853.json:
```json
{
    "body": "The patch looks good ! Positive review !\n\nFlorent",
    "created_at": "2009-07-26T23:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49853",
    "user": "https://github.com/hivert"
}
```

The patch looks good ! Positive review !

Florent



---

archive/issue_comments_049854.json:
```json
{
    "body": "reviewer patch",
    "created_at": "2009-08-23T01:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

reviewer patch



---

archive/issue_comments_049855.json:
```json
{
    "body": "Attachment [trac_6253-reviewer.patch](tarball://root/attachments/some-uuid/ticket6253/trac_6253-reviewer.patch) by mvngu created at 2009-08-23 01:54:36\n\nThis is great stuff! So let's put it in the reference manual. The reviewer patch `trac_6253-reviewer.patch` adds the module `sage/misc/constant_function.py` to the reference manual. It also fixes some typos so that the reference manual builds without any warnings. If people are happy with my changes, then patches should be merged in this order:\n\n1. `trac_6253-constant_function-nt.patch`\n2. `trac_6253-reviewer.patch`",
    "created_at": "2009-08-23T01:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49855",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6253-reviewer.patch](tarball://root/attachments/some-uuid/ticket6253/trac_6253-reviewer.patch) by mvngu created at 2009-08-23 01:54:36

This is great stuff! So let's put it in the reference manual. The reviewer patch `trac_6253-reviewer.patch` adds the module `sage/misc/constant_function.py` to the reference manual. It also fixes some typos so that the reference manual builds without any warnings. If people are happy with my changes, then patches should be merged in this order:

1. `trac_6253-constant_function-nt.patch`
2. `trac_6253-reviewer.patch`



---

archive/issue_comments_049856.json:
```json
{
    "body": "Replying to [comment:7 mvngu]:\n> This is great stuff! So let's put it in the reference manual. The reviewer patch `trac_6253-reviewer.patch` adds the module `sage/misc/constant_function.py` to the reference manual. It also fixes some typos so that the reference manual builds without any warnings. If people are happy with my changes, then patches should be merged in this order:\n> \n>  1. `trac_6253-constant_function-nt.patch`\n>  1. `trac_6253-reviewer.patch`\n\nThanks Minh! (again)\n\nPositive review on your reviewer patch.",
    "created_at": "2009-08-23T08:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49856",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:7 mvngu]:
> This is great stuff! So let's put it in the reference manual. The reviewer patch `trac_6253-reviewer.patch` adds the module `sage/misc/constant_function.py` to the reference manual. It also fixes some typos so that the reference manual builds without any warnings. If people are happy with my changes, then patches should be merged in this order:
> 
>  1. `trac_6253-constant_function-nt.patch`
>  1. `trac_6253-reviewer.patch`

Thanks Minh! (again)

Positive review on your reviewer patch.



---

archive/issue_comments_049857.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6253-constant_function-nt.patch`\n2. `trac_6253-reviewer.patch`",
    "created_at": "2009-08-23T09:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49857",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged patches in this order:

1. `trac_6253-constant_function-nt.patch`
2. `trac_6253-reviewer.patch`



---

archive/issue_events_006497.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-23T09:52:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6253#event-6497"
}
```



---

archive/issue_comments_049858.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-23T09:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6253#issuecomment-49858",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
