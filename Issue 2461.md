# Issue 2461: vector norms should have a reasonable default

archive/issues_002461.json:
```json
{
    "body": "Assignee: somebody\n\nv.norm() should work without any arguments, returning the (standard) Euclidean norm. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2461\n\n",
    "created_at": "2008-03-10T18:05:31Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "vector norms should have a reasonable default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2461",
    "user": "@robertwb"
}
```
Assignee: somebody

v.norm() should work without any arguments, returning the (standard) Euclidean norm. 

Issue created by migration from https://trac.sagemath.org/ticket/2461





---

archive/issue_comments_016678.json:
```json
{
    "body": "Attachment [vector-norms.patch](tarball://root/attachments/some-uuid/ticket2461/vector-norms.patch) by @robertwb created at 2008-03-10 18:05:42",
    "created_at": "2008-03-10T18:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16678",
    "user": "@robertwb"
}
```

Attachment [vector-norms.patch](tarball://root/attachments/some-uuid/ticket2461/vector-norms.patch) by @robertwb created at 2008-03-10 18:05:42



---

archive/issue_comments_016679.json:
```json
{
    "body": "I was in the process of refereeing this, and realized that Robert's changes to the doctests uncovered a fairly serious bug in the code for norm():\n\n\n```\nsage: v = vector([1, 2, -3])\nsage: v.norm(Infinity)\n2\nsage: v.norm(1)\n0\n```\n\n\nBoth of these are wrong, due to the fact that whoever wrote the norm() function (I think it was me, actually) forgot to take absolute values of the entries of the vector before computing the norm.\n\nI fixed this and put up a new patch that incorporates both this fix and Robert's improvements.",
    "created_at": "2008-03-11T02:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16679",
    "user": "@aghitza"
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

archive/issue_comments_016680.json:
```json
{
    "body": "Attachment [vector-norms_replace.patch](tarball://root/attachments/some-uuid/ticket2461/vector-norms_replace.patch) by @rlmill created at 2008-03-12 05:19:23",
    "created_at": "2008-03-12T05:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16680",
    "user": "@rlmill"
}
```

Attachment [vector-norms_replace.patch](tarball://root/attachments/some-uuid/ticket2461/vector-norms_replace.patch) by @rlmill created at 2008-03-12 05:19:23



---

archive/issue_comments_016681.json:
```json
{
    "body": "Looks good, testall passes.\n\nApply vector-norms_replace.patch; when writing release notes, note that this patch combines work by robertwb and `AlexGhitza`.",
    "created_at": "2008-03-14T01:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16681",
    "user": "cwitty"
}
```

Looks good, testall passes.

Apply vector-norms_replace.patch; when writing release notes, note that this patch combines work by robertwb and `AlexGhitza`.



---

archive/issue_comments_016682.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T02:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16682",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016683.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T02:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2461#issuecomment-16683",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
