# Issue 9506: include libSingular error messages in exceptions

archive/issues_009506.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nLike this:\n\n\n\n\n```\nsage: P.<e,d,c,b,a> = PolynomialRing(QQ,5,order='lex')\nsage: I = sage.rings.ideal.Cyclic(P)\n\nsage: triangL = sage.libs.singular.ff.triang__lib.triangL\nsage: _ = triangL(I)\nTraceback (most recent call last):\n...\nRuntimeError: Error in Singular function call 'triangL':\n The input is no groebner basis.\n leaving triang.lib::triangL\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9506\n\n",
    "created_at": "2010-07-15T12:49:08Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "include libSingular error messages in exceptions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9506",
    "user": "malb"
}
```
Assignee: AlexGhitza

Like this:




```
sage: P.<e,d,c,b,a> = PolynomialRing(QQ,5,order='lex')
sage: I = sage.rings.ideal.Cyclic(P)

sage: triangL = sage.libs.singular.ff.triang__lib.triangL
sage: _ = triangL(I)
Traceback (most recent call last):
...
RuntimeError: Error in Singular function call 'triangL':
 The input is no groebner basis.
 leaving triang.lib::triangL
```


Issue created by migration from https://trac.sagemath.org/ticket/9506





---

archive/issue_comments_091330.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-15T12:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9506#issuecomment-91330",
    "user": "malb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_091331.json:
```json
{
    "body": "The attached patch requires #4499 and a patch to Singular available at http://www.singular.uni-kl.de:8002/trac/ticket/244 which will be available in the next Singular release.",
    "created_at": "2010-07-15T12:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9506#issuecomment-91331",
    "user": "malb"
}
```

The attached patch requires #4499 and a patch to Singular available at http://www.singular.uni-kl.de:8002/trac/ticket/244 which will be available in the next Singular release.



---

archive/issue_comments_091332.json:
```json
{
    "body": "Argh, that's \u00a0#9499 and not#4499.",
    "created_at": "2010-07-15T12:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9506#issuecomment-91332",
    "user": "malb"
}
```

Argh, that's  #9499 and not#4499.



---

archive/issue_comments_091333.json:
```json
{
    "body": "Attachment [trac_9506_error_msg.patch](tarball://root/attachments/some-uuid/ticket9506/trac_9506_error_msg.patch) by malb created at 2010-07-15 17:20:42\n\nThis patch depends on\u00a0#8059.",
    "created_at": "2010-07-15T17:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9506#issuecomment-91333",
    "user": "malb"
}
```

Attachment [trac_9506_error_msg.patch](tarball://root/attachments/some-uuid/ticket9506/trac_9506_error_msg.patch) by malb created at 2010-07-15 17:20:42

This patch depends on #8059.



---

archive/issue_comments_091334.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-20T09:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9506#issuecomment-91334",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091335.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-20T09:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9506#issuecomment-91335",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091336.json:
```json
{
    "body": "Looks good.  And I reviewed this informally before when I stress tested it for my application and found it didn't work (for several iterations).  But I think this is good.",
    "created_at": "2010-07-20T09:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9506#issuecomment-91336",
    "user": "was"
}
```

Looks good.  And I reviewed this informally before when I stress tested it for my application and found it didn't work (for several iterations).  But I think this is good.



---

archive/issue_comments_091337.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-15T08:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9506#issuecomment-91337",
    "user": "mpatel"
}
```

Resolution: fixed
