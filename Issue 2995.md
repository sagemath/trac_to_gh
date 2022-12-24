# Issue 2995: [with patch, needs review] some new functionality and doctests for congruence subgroups

archive/issues_002995.json:
```json
{
    "body": "Assignee: craigcitro\n\nKeywords: congruence subgroup\n\nThe attached patch does the following:\n\n1. allow coercing a 2x2 matrix (or a list of 4 elements) into a congruence subgroup: Gamma0(5)([1,5,1,6]) now works\n\n2. modified G.generators() so that it actually returns a list of elements of the group G instead of just matrices\n\n3. added gens()\n\n4. added a bunch of doctests\n\nRight now, all these changes are for Gamma0 and Gamma1 subgroups; I will do the same with GammaH subgroups as soon as I figure out how these work.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2995\n\n",
    "created_at": "2008-04-22T03:34:36Z",
    "labels": [
        "modular forms",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] some new functionality and doctests for congruence subgroups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2995",
    "user": "AlexGhitza"
}
```
Assignee: craigcitro

Keywords: congruence subgroup

The attached patch does the following:

1. allow coercing a 2x2 matrix (or a list of 4 elements) into a congruence subgroup: Gamma0(5)([1,5,1,6]) now works

2. modified G.generators() so that it actually returns a list of elements of the group G instead of just matrices

3. added gens()

4. added a bunch of doctests

Right now, all these changes are for Gamma0 and Gamma1 subgroups; I will do the same with GammaH subgroups as soon as I figure out how these work.


Issue created by migration from https://trac.sagemath.org/ticket/2995





---

archive/issue_comments_020601.json:
```json
{
    "body": "Attachment [congroup.patch](tarball://root/attachments/some-uuid/ticket2995/congroup.patch) by AlexGhitza created at 2008-04-23 02:06:10\n\nI've replaced the previous patch with one that also has the changes listed above for the groups Gamma_H.",
    "created_at": "2008-04-23T02:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2995#issuecomment-20601",
    "user": "AlexGhitza"
}
```

Attachment [congroup.patch](tarball://root/attachments/some-uuid/ticket2995/congroup.patch) by AlexGhitza created at 2008-04-23 02:06:10

I've replaced the previous patch with one that also has the changes listed above for the groups Gamma_H.



---

archive/issue_comments_020602.json:
```json
{
    "body": "Patch looks good, doctests are good too.\n\nI hate the name `acton` -- it looks like a typoed `action`.  Could we change that to `act_on`?",
    "created_at": "2008-04-25T23:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2995#issuecomment-20602",
    "user": "ncalexan"
}
```

Patch looks good, doctests are good too.

I hate the name `acton` -- it looks like a typoed `action`.  Could we change that to `act_on`?



---

archive/issue_comments_020603.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-26T00:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2995#issuecomment-20603",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha0



---

archive/issue_comments_020604.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T00:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2995#issuecomment-20604",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020605.json:
```json
{
    "body": "Nick: good point about acton().  I am planning to do some more work on congroup.py and friends, and I'll fix this then.",
    "created_at": "2008-04-26T02:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2995#issuecomment-20605",
    "user": "AlexGhitza"
}
```

Nick: good point about acton().  I am planning to do some more work on congroup.py and friends, and I'll fix this then.
