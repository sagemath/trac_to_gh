# Issue 5820: bug in comparison of ring morphisms

archive/issues_005820.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: morphism ring comparison loads dumps\n\nAs discussed at http://groups.google.com/group/sage-devel/browse_thread/thread/bc99d36058aff638 , the following is wrong:\n\n\n```\nsage: f = ZZ.hom(QQ)\nsage: g = loads(dumps(f))\nsage: f == g\nFalse\n```\n\n\n(It should return True.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5820\n\n",
    "created_at": "2009-04-19T02:54:39Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "bug in comparison of ring morphisms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5820",
    "user": "@aghitza"
}
```
Assignee: tbd

Keywords: morphism ring comparison loads dumps

As discussed at http://groups.google.com/group/sage-devel/browse_thread/thread/bc99d36058aff638 , the following is wrong:


```
sage: f = ZZ.hom(QQ)
sage: g = loads(dumps(f))
sage: f == g
False
```


(It should return True.)


Issue created by migration from https://trac.sagemath.org/ticket/5820





---

archive/issue_comments_045738.json:
```json
{
    "body": "Changing assignee from tbd to @aghitza.",
    "created_at": "2009-04-25T09:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5820#issuecomment-45738",
    "user": "@aghitza"
}
```

Changing assignee from tbd to @aghitza.



---

archive/issue_comments_045739.json:
```json
{
    "body": "Changing keywords from \"morphism ring comparison loads dumps\" to \"ring coercion morphism comparison loads dumps\".",
    "created_at": "2009-04-25T09:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5820#issuecomment-45739",
    "user": "@aghitza"
}
```

Changing keywords from "morphism ring comparison loads dumps" to "ring coercion morphism comparison loads dumps".



---

archive/issue_comments_045740.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-25T09:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5820#issuecomment-45740",
    "user": "@aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045741.json:
```json
{
    "body": "This is actually a problem with ring coercion morphisms, namely that they don't have a comparison method defined.\n\nThe attached patch does this and adds doctests (including `f == loads(dumps(f))`).",
    "created_at": "2009-04-25T09:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5820#issuecomment-45741",
    "user": "@aghitza"
}
```

This is actually a problem with ring coercion morphisms, namely that they don't have a comparison method defined.

The attached patch does this and adds doctests (including `f == loads(dumps(f))`).



---

archive/issue_comments_045742.json:
```json
{
    "body": "Attachment [trac_5820.patch](tarball://root/attachments/some-uuid/ticket5820/trac_5820.patch) by @aghitza created at 2009-04-25 09:46:33",
    "created_at": "2009-04-25T09:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5820#issuecomment-45742",
    "user": "@aghitza"
}
```

Attachment [trac_5820.patch](tarball://root/attachments/some-uuid/ticket5820/trac_5820.patch) by @aghitza created at 2009-04-25 09:46:33



---

archive/issue_comments_045743.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-04-29T18:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5820#issuecomment-45743",
    "user": "@roed314"
}
```

Looks good to me.



---

archive/issue_comments_045744.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T01:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5820#issuecomment-45744",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_045745.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T01:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5820#issuecomment-45745",
    "user": "mabshoff"
}
```

Resolution: fixed
