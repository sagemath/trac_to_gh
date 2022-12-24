# Issue 7985: fix doctest in base.pyx

archive/issues_007985.json:
```json
{
    "body": "Assignee: was\n\nThe following doctest from line 757 of base.pyx:\n\n```\nsage: G = tetrahedron(color='red') + tetrahedron(color='yellow') + tetrahedron(color='red', opacity=0.5)\nsage: G.texture_set()\nset([Texture(texture..., red, ff0000), Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])\n```\n\nwill fail sometimes because the order of the elements of the set is not fixed. The attached patch fixes this by outputting first the two red textures, and then the yellow texture.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7985\n\n",
    "created_at": "2010-01-19T00:10:01Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "fix doctest in base.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7985",
    "user": "wcauchois"
}
```
Assignee: was

The following doctest from line 757 of base.pyx:

```
sage: G = tetrahedron(color='red') + tetrahedron(color='yellow') + tetrahedron(color='red', opacity=0.5)
sage: G.texture_set()
set([Texture(texture..., red, ff0000), Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])
```

will fail sometimes because the order of the elements of the set is not fixed. The attached patch fixes this by outputting first the two red textures, and then the yellow texture.

Issue created by migration from https://trac.sagemath.org/ticket/7985





---

archive/issue_comments_069739.json:
```json
{
    "body": "based on sage 4.3.1.rc0",
    "created_at": "2010-01-19T00:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7985#issuecomment-69739",
    "user": "wcauchois"
}
```

based on sage 4.3.1.rc0



---

archive/issue_comments_069740.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T04:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7985#issuecomment-69740",
    "user": "wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069741.json:
```json
{
    "body": "Attachment [fix-annoying-doctest.patch](tarball://root/attachments/some-uuid/ticket7985/fix-annoying-doctest.patch) by wjp created at 2010-01-19 04:39:07",
    "created_at": "2010-01-19T04:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7985#issuecomment-69741",
    "user": "wjp"
}
```

Attachment [fix-annoying-doctest.patch](tarball://root/attachments/some-uuid/ticket7985/fix-annoying-doctest.patch) by wjp created at 2010-01-19 04:39:07



---

archive/issue_comments_069742.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-01-19T04:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7985#issuecomment-69742",
    "user": "wjp"
}
```

Looks good.



---

archive/issue_comments_069743.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T04:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7985#issuecomment-69743",
    "user": "wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069744.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T05:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7985#issuecomment-69744",
    "user": "rlm"
}
```

Resolution: fixed
