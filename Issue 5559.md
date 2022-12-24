# Issue 5559: roots issue on fedora core 32-bit

archive/issues_005559.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  cwitty\n\n\n```\n>> x86-Linux-fc (cicero)\n>>\n>> The following tests failed:\n>>\n>>        sage -t  \"devel/sage/sage/rings/polynomial/complex_roots.py\"\n>\n> Could you send the output of this test failing?\n\nsage -t  \"devel/sage/sage/rings/polynomial/complex_roots.py\"\n**********************************************************************\nFile \"/home/mariah/sage/sage-3.4-x86-Linux-fc/devel/sage/sage/rings/polynomial/c\nomplex_roots.py\", line 271:\n   sage: complex_roots(x^2 + 27*x + 181)\nExpected:\n   [(-14.61803398874990?..., 1), (-12.3819660112501...? + 0.?e-27*I, 1)]\nGot:\n   [(-12.3819660112501?, 1), (-14.61803398874990? + 0.?e-27*I, 1)]\n**********************************************************************\n1 items had failures:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5559\n\n",
    "created_at": "2009-03-18T14:26:39Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "roots issue on fedora core 32-bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5559",
    "user": "@williamstein"
}
```
Assignee: mabshoff

CC:  cwitty


```
>> x86-Linux-fc (cicero)
>>
>> The following tests failed:
>>
>>        sage -t  "devel/sage/sage/rings/polynomial/complex_roots.py"
>
> Could you send the output of this test failing?

sage -t  "devel/sage/sage/rings/polynomial/complex_roots.py"
**********************************************************************
File "/home/mariah/sage/sage-3.4-x86-Linux-fc/devel/sage/sage/rings/polynomial/c
omplex_roots.py", line 271:
   sage: complex_roots(x^2 + 27*x + 181)
Expected:
   [(-14.61803398874990?..., 1), (-12.3819660112501...? + 0.?e-27*I, 1)]
Got:
   [(-12.3819660112501?, 1), (-14.61803398874990? + 0.?e-27*I, 1)]
**********************************************************************
1 items had failures:
```


Issue created by migration from https://trac.sagemath.org/ticket/5559





---

archive/issue_comments_043265.json:
```json
{
    "body": "This is \"only\" a problem with gcc 4.3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-01T02:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5559#issuecomment-43265",
    "user": "mabshoff"
}
```

This is "only" a problem with gcc 4.3.3.

Cheers,

Michael



---

archive/issue_comments_043266.json:
```json
{
    "body": "This is a 3.4.1 blocker if there ever was one :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T18:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5559#issuecomment-43266",
    "user": "mabshoff"
}
```

This is a 3.4.1 blocker if there ever was one :)

Cheers,

Michael



---

archive/issue_comments_043267.json:
```json
{
    "body": "After chatting to cwitty about this problem a couple weeks ago: we can just use another polynomial since the specific choice is irrelevant. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T21:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5559#issuecomment-43267",
    "user": "mabshoff"
}
```

After chatting to cwitty about this problem a couple weeks ago: we can just use another polynomial since the specific choice is irrelevant. 

Cheers,

Michael



---

archive/issue_comments_043268.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-04-18T01:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5559#issuecomment-43268",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_043269.json:
```json
{
    "body": "This is a dupe of #5378.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T01:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5559#issuecomment-43269",
    "user": "mabshoff"
}
```

This is a dupe of #5378.

Cheers,

Michael
