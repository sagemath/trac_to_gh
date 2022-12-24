# Issue 7842: Let attrcall objects accept further arguments

archive/issues_007842.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat\n\nKeywords: attrcall\n\nThe attached patch allows for the following:\n\n\n```\n            sage: xseries = attrcall('series', x)\n            sage: xseries(sin(x), 4)\n            1*x + (-1/6)*x^3 + Order(x^4)\n```\n\n\nThis is used in #7753\n\nIssue created by migration from https://trac.sagemath.org/ticket/7842\n\n",
    "created_at": "2010-01-04T15:27:08Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "title": "Let attrcall objects accept further arguments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7842",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat

Keywords: attrcall

The attached patch allows for the following:


```
            sage: xseries = attrcall('series', x)
            sage: xseries(sin(x), 4)
            1*x + (-1/6)*x^3 + Order(x^4)
```


This is used in #7753

Issue created by migration from https://trac.sagemath.org/ticket/7842





---

archive/issue_comments_067929.json:
```json
{
    "body": "Attachment [trac_7842-attrcall-nt.patch](tarball://root/attachments/some-uuid/ticket7842/trac_7842-attrcall-nt.patch) by nthiery created at 2010-01-04 15:28:23",
    "created_at": "2010-01-04T15:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7842#issuecomment-67929",
    "user": "nthiery"
}
```

Attachment [trac_7842-attrcall-nt.patch](tarball://root/attachments/some-uuid/ticket7842/trac_7842-attrcall-nt.patch) by nthiery created at 2010-01-04 15:28:23



---

archive/issue_comments_067930.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-04T15:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7842#issuecomment-67930",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067931.json:
```json
{
    "body": "Another nice thing to have now that I think about it would be this syntax:\n\n\n```\nsage: xseries = attrcall.series(x)\nsage: xseries(sin(x), 4)\n1*x + (-1/6)*x^3 + Order(x^4)\n```\n\n\nI'll make a new ticket for this so that that it'll backward-compatible with the old version.",
    "created_at": "2010-01-04T17:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7842#issuecomment-67931",
    "user": "mhansen"
}
```

Another nice thing to have now that I think about it would be this syntax:


```
sage: xseries = attrcall.series(x)
sage: xseries(sin(x), 4)
1*x + (-1/6)*x^3 + Order(x^4)
```


I'll make a new ticket for this so that that it'll backward-compatible with the old version.



---

archive/issue_comments_067932.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> Another nice thing to have now that I think about it would be this syntax:\n> \n> {{{\n> sage: xseries = attrcall.series(x)\n> sage: xseries(sin(x), 4)\n> 1*x + (-1/6)*x^3 + Order(x^4)\n> }}}\n\nYour point is that this syntax gives a better visual hint about this being about method calls, right? So here, attrcall would be some sort of dummy object placeholder? Why not. Though I am a bit reluctant with having two syntaxes.\n\n> I'll make a new ticket for this so that that it'll backward-compatible with the old version.\n\nDo you mind reviewing this first, so that we can get #7753 in?\n\nI'll review your patch in return :-)",
    "created_at": "2010-01-04T18:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7842#issuecomment-67932",
    "user": "nthiery"
}
```

Replying to [comment:2 mhansen]:
> Another nice thing to have now that I think about it would be this syntax:
> 
> {{{
> sage: xseries = attrcall.series(x)
> sage: xseries(sin(x), 4)
> 1*x + (-1/6)*x^3 + Order(x^4)
> }}}

Your point is that this syntax gives a better visual hint about this being about method calls, right? So here, attrcall would be some sort of dummy object placeholder? Why not. Though I am a bit reluctant with having two syntaxes.

> I'll make a new ticket for this so that that it'll backward-compatible with the old version.

Do you mind reviewing this first, so that we can get #7753 in?

I'll review your patch in return :-)



---

archive/issue_comments_067933.json:
```json
{
    "body": "This patch looks good to me.\n\nWe should also maybe allow putting keywords in too at the \"second stage\".",
    "created_at": "2010-01-04T18:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7842#issuecomment-67933",
    "user": "mhansen"
}
```

This patch looks good to me.

We should also maybe allow putting keywords in too at the "second stage".



---

archive/issue_comments_067934.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-04T18:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7842#issuecomment-67934",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067935.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T07:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7842#issuecomment-67935",
    "user": "rlm"
}
```

Resolution: fixed
