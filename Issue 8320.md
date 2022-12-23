# Issue 8320: Make HTML doc headers and footers more compact

archive/issues_008320.json:
```json
{
    "body": "Assignee: mvngu\n\nWe can use Sphinx's [html_short_title setting](http://sphinx.pocoo.org/config.html#confval-html_short_title) to [try to] keep links from overflowing the header and footer.\n\nFor example, instead of \"Sage Reference Manual v4.3.3,\" we can use \"Reference v4.3.3.\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/8320\n\n",
    "created_at": "2010-02-21T19:59:15Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "Make HTML doc headers and footers more compact",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8320",
    "user": "mpatel"
}
```
Assignee: mvngu

We can use Sphinx's [html_short_title setting](http://sphinx.pocoo.org/config.html#confval-html_short_title) to [try to] keep links from overflowing the header and footer.

For example, instead of "Sage Reference Manual v4.3.3," we can use "Reference v4.3.3."

Issue created by migration from https://trac.sagemath.org/ticket/8320





---

archive/issue_comments_073796.json:
```json
{
    "body": "HTML short titles for selected docs.  sage repo.",
    "created_at": "2010-02-21T21:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73796",
    "user": "mpatel"
}
```

HTML short titles for selected docs.  sage repo.



---

archive/issue_comments_073797.json:
```json
{
    "body": "Attachment\n\nThe patch adds shorter HTML titles, which appear in Sphinx headers and footers, for selected docs: the developer's guide, Bordeaux lectures, numerical primer, and reference manual.  The others' titles overflow only with very large font sizes.  But feel free to make adjustments, e.g., for consistency.",
    "created_at": "2010-02-21T21:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73797",
    "user": "mpatel"
}
```

Attachment

The patch adds shorter HTML titles, which appear in Sphinx headers and footers, for selected docs: the developer's guide, Bordeaux lectures, numerical primer, and reference manual.  The others' titles overflow only with very large font sizes.  But feel free to make adjustments, e.g., for consistency.



---

archive/issue_comments_073798.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2010-02-21T21:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73798",
    "user": "mpatel"
}
```

Changing priority from minor to trivial.



---

archive/issue_comments_073799.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-21T21:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73799",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073800.json:
```json
{
    "body": "Attachment\n\napply on top of previous patch",
    "created_at": "2010-02-26T04:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73800",
    "user": "mvngu"
}
```

Attachment

apply on top of previous patch



---

archive/issue_comments_073801.json:
```json
{
    "body": "The reviewer patch [trac_8320-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-reviewer.patch) shortens the HTML title of these documents:\n\n* A Tour of Sage\n* Sage Installation Guide\n \nI also changed the short title of the reference manual from \"Reference\" to \"Sage Reference\" as an attempt to be consistent with these short titles:\n\n* Sage Tutorial\n* Sage Constructions\n* Sage Tour\n \nOnly my patch needs review by anyone but me.",
    "created_at": "2010-02-26T04:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73801",
    "user": "mvngu"
}
```

The reviewer patch [trac_8320-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-reviewer.patch) shortens the HTML title of these documents:

* A Tour of Sage
* Sage Installation Guide
 
I also changed the short title of the reference manual from "Reference" to "Sage Reference" as an attempt to be consistent with these short titles:

* Sage Tutorial
* Sage Constructions
* Sage Tour
 
Only my patch needs review by anyone but me.



---

archive/issue_comments_073802.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-26T20:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73802",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073803.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T22:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73803",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_073804.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8320-html_short_title.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-html_short_title.patch)\n2. [trac_8320-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-reviewer.patch)",
    "created_at": "2010-03-02T22:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73804",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_8320-html_short_title.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-html_short_title.patch)
2. [trac_8320-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-reviewer.patch)
