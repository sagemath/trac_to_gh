# Issue 2827: sage -notebook does not handle options passed to it correctly

archive/issues_002827.json:
```json
{
    "body": "Assignee: boothby\n\nThe code suspect code is the following (which doesn't isn't flexible enough:\n\n\n```\nif len(sys.argv) > 1:\n    notebook(*sys.argv[1:])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2827\n\n",
    "created_at": "2008-04-06T10:05:02Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "sage -notebook does not handle options passed to it correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2827",
    "user": "@mwhansen"
}
```
Assignee: boothby

The code suspect code is the following (which doesn't isn't flexible enough:


```
if len(sys.argv) > 1:
    notebook(*sys.argv[1:])
```


Issue created by migration from https://trac.sagemath.org/ticket/2827





---

archive/issue_comments_019407.json:
```json
{
    "body": "Maybe we should change sage -notebook so that it works like this:\n\n\n```\nsage -notebook \"(secure=True, address='sage.math.washington.edu', accounts=False)\"\n```\n\n\nwhere anything in quotes is valid Python.  What do you think?",
    "created_at": "2008-05-27T01:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2827#issuecomment-19407",
    "user": "@williamstein"
}
```

Maybe we should change sage -notebook so that it works like this:


```
sage -notebook "(secure=True, address='sage.math.washington.edu', accounts=False)"
```


where anything in quotes is valid Python.  What do you think?



---

archive/issue_comments_019408.json:
```json
{
    "body": "Some recent work went in in this area? Can someone still reproduce this or is this ticket invalid?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-12T08:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2827#issuecomment-19408",
    "user": "mabshoff"
}
```

Some recent work went in in this area? Can someone still reproduce this or is this ticket invalid?

Cheers,

Michael



---

archive/issue_comments_019409.json:
```json
{
    "body": "Replying to [comment:2 was]:\n> Maybe we should change sage -notebook so that it works like this:\n> \n> {{{\n> sage -notebook \"(secure=True, address='sage.math.washington.edu', accounts=False)\"\n> }}}\n> \n> where anything in quotes is valid Python.  What do you think?\n\nThis seems quite reasonable to me. I also remember Dr. Kirkby's problem with specifying server_pool using `sage -n`.",
    "created_at": "2010-01-19T22:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2827#issuecomment-19409",
    "user": "@TimDumol"
}
```

Replying to [comment:2 was]:
> Maybe we should change sage -notebook so that it works like this:
> 
> {{{
> sage -notebook "(secure=True, address='sage.math.washington.edu', accounts=False)"
> }}}
> 
> where anything in quotes is valid Python.  What do you think?

This seems quite reasonable to me. I also remember Dr. Kirkby's problem with specifying server_pool using `sage -n`.



---

archive/issue_comments_019410.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2827#issuecomment-19410",
    "user": "boothby"
}
```

Closing deprecated notebook tickets



---

archive/issue_comments_019411.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2827#issuecomment-19411",
    "user": "boothby"
}
```

Resolution: invalid
