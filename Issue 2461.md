# Issue 2461: vector norms should have a reasonable default

archive/issues_002461.json:
```json
{
    "body": "Assignee: somebody\n\nv.norm() should work without any arguments, returning the (standard) Euclidean norm. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2461\n\n",
    "created_at": "2008-03-10T18:05:31Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "vector norms should have a reasonable default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2461",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

v.norm() should work without any arguments, returning the (standard) Euclidean norm. 

Issue created by migration from https://trac.sagemath.org/ticket/2461





---

archive/issue_comments_016642.json:
```json
{
    "body": "Attachment [vector-norms.patch](tarball://root/attachments/some-uuid/ticket2461/vector-norms.patch) by @robertwb created at 2008-03-10 18:05:42",
    "created_at": "2008-03-10T18:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16642",
    "user": "https://github.com/robertwb"
}
```

Attachment [vector-norms.patch](tarball://root/attachments/some-uuid/ticket2461/vector-norms.patch) by @robertwb created at 2008-03-10 18:05:42



---

archive/issue_comments_016643.json:
```json
{
    "body": "I was in the process of refereeing this, and realized that Robert's changes to the doctests uncovered a fairly serious bug in the code for norm():\n\n\n```\nsage: v = vector([1, 2, -3])\nsage: v.norm(Infinity)\n2\nsage: v.norm(1)\n0\n```\n\n\nBoth of these are wrong, due to the fact that whoever wrote the norm() function (I think it was me, actually) forgot to take absolute values of the entries of the vector before computing the norm.\n\nI fixed this and put up a new patch that incorporates both this fix and Robert's improvements.",
    "created_at": "2008-03-11T02:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16643",
    "user": "https://github.com/aghitza"
}
```

I was in the process of refereeing this, and realized that Robert's changes to the doctests uncovered a fairly serious bug in the code for norm():


```
sage: v = vector([1, 2, -3])
sage: v.norm(Infinity)
2
sage: v.norm(1)
0
```


Both of these are wrong, due to the fact that whoever wrote the norm() function (I think it was me, actually) forgot to take absolute values of the entries of the vector before computing the norm.

I fixed this and put up a new patch that incorporates both this fix and Robert's improvements.



---

archive/issue_comments_016644.json:
```json
{
    "body": "Attachment [vector-norms_replace.patch](tarball://root/attachments/some-uuid/ticket2461/vector-norms_replace.patch) by @rlmill created at 2008-03-12 05:19:23",
    "created_at": "2008-03-12T05:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16644",
    "user": "https://github.com/rlmill"
}
```

Attachment [vector-norms_replace.patch](tarball://root/attachments/some-uuid/ticket2461/vector-norms_replace.patch) by @rlmill created at 2008-03-12 05:19:23



---

archive/issue_comments_016645.json:
```json
{
    "body": "Looks good, testall passes.\n\nApply vector-norms_replace.patch; when writing release notes, note that this patch combines work by robertwb and `AlexGhitza`.",
    "created_at": "2008-03-14T01:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16645",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks good, testall passes.

Apply vector-norms_replace.patch; when writing release notes, note that this patch combines work by robertwb and `AlexGhitza`.



---

archive/issue_comments_016646.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T02:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16646",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016647.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T02:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16647",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
