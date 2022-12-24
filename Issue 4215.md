# Issue 4215: [with patch, needs review] Bug in creating sparse vectors using a dictionary

archive/issues_004215.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nI suspect there is a bug in the implementation of the vector function.\nIt seems that when trying to construct a sparse vector by a dictionary\nsage simply ignores the keys. for example:\n\nsage: v = vector({3:1.1 , 5:3.14}); v\n(1.10000000000000, 3.14000000000000)\n\nwhere one would expect the behavior to be similar to matrix:\n\nsage: m = matrix({(0,3):1.1 , (0,5):3.14}); m\n[0.000000000000000 0.000000000000000 0.000000000000000\n1.10000000000000 0.000000000000000  3.14000000000000]\n\nit seems to me that the problem is in prepare_dict (in\nfree_module_element)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4215\n\n",
    "created_at": "2008-09-29T02:35:44Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] Bug in creating sparse vectors using a dictionary",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4215",
    "user": "mhansen"
}
```
Assignee: tbd


```
I suspect there is a bug in the implementation of the vector function.
It seems that when trying to construct a sparse vector by a dictionary
sage simply ignores the keys. for example:

sage: v = vector({3:1.1 , 5:3.14}); v
(1.10000000000000, 3.14000000000000)

where one would expect the behavior to be similar to matrix:

sage: m = matrix({(0,3):1.1 , (0,5):3.14}); m
[0.000000000000000 0.000000000000000 0.000000000000000
1.10000000000000 0.000000000000000  3.14000000000000]

it seems to me that the problem is in prepare_dict (in
free_module_element)
```


Issue created by migration from https://trac.sagemath.org/ticket/4215





---

archive/issue_comments_030631.json:
```json
{
    "body": "Attachment [trac_4215.patch](tarball://root/attachments/some-uuid/ticket4215/trac_4215.patch) by mabshoff created at 2008-09-29 03:11:33\n\nPositive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-29T03:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4215#issuecomment-30631",
    "user": "mabshoff"
}
```

Attachment [trac_4215.patch](tarball://root/attachments/some-uuid/ticket4215/trac_4215.patch) by mabshoff created at 2008-09-29 03:11:33

Positive review.

Cheers,

Michael



---

archive/issue_comments_030632.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-29T04:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4215#issuecomment-30632",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030633.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-29T04:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4215#issuecomment-30633",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2
