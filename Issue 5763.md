# Issue 5763: [with patch, needs review] pynac -- add _polynomial_ conversion constructor

archive/issues_005763.json:
```json
{
    "body": "CC:  burcin mhansen was\n\nKeywords: pynac symbolics _polynomial_ constructor\n\nThe attached patch adds conversion to polynomial rings.  Two doctests fail at this time; they rely on being able to convert to CDF and ComplexField(100).  I didn't want them to get forgotten so I left them in.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5763\n\n",
    "created_at": "2009-04-11T21:40:01Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] pynac -- add _polynomial_ conversion constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5763",
    "user": "ncalexan"
}
```
CC:  burcin mhansen was

Keywords: pynac symbolics _polynomial_ constructor

The attached patch adds conversion to polynomial rings.  Two doctests fail at this time; they rely on being able to convert to CDF and ComplexField(100).  I didn't want them to get forgotten so I left them in.

Issue created by migration from https://trac.sagemath.org/ticket/5763





---

archive/issue_comments_045046.json:
```json
{
    "body": "Attachment [trac_5763-symbolic-polynomial.patch](tarball://root/attachments/some-uuid/ticket5763/trac_5763-symbolic-polynomial.patch) by burcin created at 2009-04-12 09:25:09\n\nThanks Nick!\n\nThe patch looks great, I am looking at the doctests right now. \n\nNote that #5753 fixes the coercion of constants to pynac, so you can use `is_a_constant` in the .is_constant() function.\n\nI will see what I can do about the doctest failures, and hopefully post a patch fixing them soon.",
    "created_at": "2009-04-12T09:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5763#issuecomment-45046",
    "user": "burcin"
}
```

Attachment [trac_5763-symbolic-polynomial.patch](tarball://root/attachments/some-uuid/ticket5763/trac_5763-symbolic-polynomial.patch) by burcin created at 2009-04-12 09:25:09

Thanks Nick!

The patch looks great, I am looking at the doctests right now. 

Note that #5753 fixes the coercion of constants to pynac, so you can use `is_a_constant` in the .is_constant() function.

I will see what I can do about the doctest failures, and hopefully post a patch fixing them soon.



---

archive/issue_comments_045047.json:
```json
{
    "body": "In fact, you can make the doctest works by changing the if is_constant check to coerce the pyobject in.  It's a one line fix that I haven't posted here, it works well for me in practice.",
    "created_at": "2009-04-12T19:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5763#issuecomment-45047",
    "user": "ncalexan"
}
```

In fact, you can make the doctest works by changing the if is_constant check to coerce the pyobject in.  It's a one line fix that I haven't posted here, it works well for me in practice.



---

archive/issue_comments_045048.json:
```json
{
    "body": "This patch seems to have been forgotten during the \"pynac push.\" I recall that it was briefly mentioned on IRC once.\n\nI suggest closing this issue as wontfix now. Trac doesn't allow me close tickets any more.",
    "created_at": "2009-05-24T16:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5763#issuecomment-45048",
    "user": "burcin"
}
```

This patch seems to have been forgotten during the "pynac push." I recall that it was briefly mentioned on IRC once.

I suggest closing this issue as wontfix now. Trac doesn't allow me close tickets any more.



---

archive/issue_comments_045049.json:
```json
{
    "body": "This isn't critical for 4.0.",
    "created_at": "2009-05-28T06:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5763#issuecomment-45049",
    "user": "was"
}
```

This isn't critical for 4.0.



---

archive/issue_comments_045050.json:
```json
{
    "body": "The docstring should adhere to ReST formatting. Some examples follow this rule, but most don't. I'm merely enforcing proper ReST formatting, not actually reviewing the whole patch.",
    "created_at": "2009-06-08T03:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5763#issuecomment-45050",
    "user": "mvngu"
}
```

The docstring should adhere to ReST formatting. Some examples follow this rule, but most don't. I'm merely enforcing proper ReST formatting, not actually reviewing the whole patch.



---

archive/issue_comments_045051.json:
```json
{
    "body": "This should have been marked as a negative review.",
    "created_at": "2009-07-15T22:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5763#issuecomment-45051",
    "user": "boothby"
}
```

This should have been marked as a negative review.



---

archive/issue_comments_045052.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-22T15:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5763#issuecomment-45052",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_045053.json:
```json
{
    "body": "I think we can close this as invalid as all of the doctests in the patch currenly pass.",
    "created_at": "2013-07-22T15:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5763#issuecomment-45053",
    "user": "mhansen"
}
```

I think we can close this as invalid as all of the doctests in the patch currenly pass.
