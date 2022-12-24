# Issue 6989: line3d can modify its argument type

archive/issues_006989.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis issue could well arise in other plotting code, I haven't checked yet.  But at least for line3d:\n\n\n```\nsage: mypoints = [vector([1,2,3]), vector([4,5,6])]\nsage: type(mypoints[0])\n<type 'sage.modules.vector_integer_dense.Vector_integer_dense'>\n```\n\nbut then:\n\n```\nsage: L = line3d(mypoints)\nsage: type(mypoints[0])\n<type 'tuple'>\n```\n\n\nso vectors are changed to tuples.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6989\n\n",
    "created_at": "2009-09-22T17:49:16Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "line3d can modify its argument type",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6989",
    "user": "mhampton"
}
```
Assignee: @williamstein

This issue could well arise in other plotting code, I haven't checked yet.  But at least for line3d:


```
sage: mypoints = [vector([1,2,3]), vector([4,5,6])]
sage: type(mypoints[0])
<type 'sage.modules.vector_integer_dense.Vector_integer_dense'>
```

but then:

```
sage: L = line3d(mypoints)
sage: type(mypoints[0])
<type 'tuple'>
```


so vectors are changed to tuples.

Issue created by migration from https://trac.sagemath.org/ticket/6989





---

archive/issue_comments_057806.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T10:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6989#issuecomment-57806",
    "user": "@jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057807.json:
```json
{
    "body": "Attachment [trac-6989-copy-list.patch](tarball://root/attachments/some-uuid/ticket6989/trac-6989-copy-list.patch) by @jasongrout created at 2010-01-20 10:37:34",
    "created_at": "2010-01-20T10:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6989#issuecomment-57807",
    "user": "@jasongrout"
}
```

Attachment [trac-6989-copy-list.patch](tarball://root/attachments/some-uuid/ticket6989/trac-6989-copy-list.patch) by @jasongrout created at 2010-01-20 10:37:34



---

archive/issue_comments_057808.json:
```json
{
    "body": "Looks good.  Positive review, assuming it passes relevant doctests (currently checking).",
    "created_at": "2010-01-27T15:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6989#issuecomment-57808",
    "user": "@kcrisman"
}
```

Looks good.  Positive review, assuming it passes relevant doctests (currently checking).



---

archive/issue_comments_057809.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-27T15:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6989#issuecomment-57809",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057810.json:
```json
{
    "body": "All is well.  And this does not occur in line2d, as far as I have tested it, because of the grid system.",
    "created_at": "2010-01-27T15:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6989#issuecomment-57810",
    "user": "@kcrisman"
}
```

All is well.  And this does not occur in line2d, as far as I have tested it, because of the grid system.



---

archive/issue_comments_057811.json:
```json
{
    "body": "Jason, please provide a meaningful commit message together with a ticket number. See [this section](http://www.sagemath.org/doc/developer/producing_patches.html#quick-mercurial-tutorial-for-sage) of the Developers' Guide.",
    "created_at": "2010-01-29T22:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6989#issuecomment-57811",
    "user": "mvngu"
}
```

Jason, please provide a meaningful commit message together with a ticket number. See [this section](http://www.sagemath.org/doc/developer/producing_patches.html#quick-mercurial-tutorial-for-sage) of the Developers' Guide.



---

archive/issue_comments_057812.json:
```json
{
    "body": "argh!  I'm always forgetting that.  I'll try to do it soon (in the next two weeks).",
    "created_at": "2010-01-30T00:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6989#issuecomment-57812",
    "user": "@jasongrout"
}
```

argh!  I'm always forgetting that.  I'll try to do it soon (in the next two weeks).



---

archive/issue_comments_057813.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-31T01:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6989#issuecomment-57813",
    "user": "mvngu"
}
```

Resolution: fixed
