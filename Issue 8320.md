# Issue 8320: Make HTML doc headers and footers more compact

archive/issues_008320.json:
```json
{
    "body": "Assignee: mvngu\n\nWe can use Sphinx's [html_short_title setting](http://sphinx.pocoo.org/config.html#confval-html_short_title) to [try to] keep links from overflowing the header and footer.\n\nThis could be useful for devices with small-screen or large fonts (e.g., for accessibility).\n\nFor example, instead of \"Sage Reference Manual v4.3.3,\" we can use \"Reference v4.3.3,\" which should help for deeply nested pages.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8320\n\n",
    "closed_at": "2010-03-02T22:19:42Z",
    "created_at": "2010-02-21T19:59:15Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Make HTML doc headers and footers more compact",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8320",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

We can use Sphinx's [html_short_title setting](http://sphinx.pocoo.org/config.html#confval-html_short_title) to [try to] keep links from overflowing the header and footer.

This could be useful for devices with small-screen or large fonts (e.g., for accessibility).

For example, instead of "Sage Reference Manual v4.3.3," we can use "Reference v4.3.3," which should help for deeply nested pages.

Issue created by migration from https://trac.sagemath.org/ticket/8320





---

archive/issue_comments_073672.json:
```json
{
    "body": "HTML short titles for selected docs.  sage repo.",
    "created_at": "2010-02-21T21:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73672",
    "user": "https://github.com/qed777"
}
```

HTML short titles for selected docs.  sage repo.



---

archive/issue_comments_073673.json:
```json
{
    "body": "Attachment [trac_8320-html_short_title.patch](tarball://root/attachments/some-uuid/ticket8320/trac_8320-html_short_title.patch) by @qed777 created at 2010-02-21 21:57:54\n\nThe patch adds shorter HTML titles, which appear in Sphinx headers and footers, for selected docs: the developer's guide, Bordeaux lectures, numerical primer, and reference manual.  The others' titles overflow only with very large font sizes.  But feel free to make adjustments, e.g., for consistency.",
    "created_at": "2010-02-21T21:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73673",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8320-html_short_title.patch](tarball://root/attachments/some-uuid/ticket8320/trac_8320-html_short_title.patch) by @qed777 created at 2010-02-21 21:57:54

The patch adds shorter HTML titles, which appear in Sphinx headers and footers, for selected docs: the developer's guide, Bordeaux lectures, numerical primer, and reference manual.  The others' titles overflow only with very large font sizes.  But feel free to make adjustments, e.g., for consistency.



---

archive/issue_comments_073674.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2010-02-21T21:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73674",
    "user": "https://github.com/qed777"
}
```

Changing priority from minor to trivial.



---

archive/issue_comments_073675.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-21T21:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73675",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_events_019909.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-21T21:57:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "milestone": "sage-4.3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8320#event-19909"
}
```



---

archive/issue_comments_073676.json:
```json
{
    "body": "Attachment [trac_8320-reviewer.patch](tarball://root/attachments/some-uuid/ticket8320/trac_8320-reviewer.patch) by mvngu created at 2010-02-26 04:36:01\n\napply on top of previous patch",
    "created_at": "2010-02-26T04:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73676",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8320-reviewer.patch](tarball://root/attachments/some-uuid/ticket8320/trac_8320-reviewer.patch) by mvngu created at 2010-02-26 04:36:01

apply on top of previous patch



---

archive/issue_comments_073677.json:
```json
{
    "body": "The reviewer patch [trac_8320-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-reviewer.patch) shortens the HTML title of these documents:\n\n* A Tour of Sage\n* Sage Installation Guide\n \nI also changed the short title of the reference manual from \"Reference\" to \"Sage Reference\" as an attempt to be consistent with these short titles:\n\n* Sage Tutorial\n* Sage Constructions\n* Sage Tour\n \nOnly my patch needs review by anyone but me.",
    "created_at": "2010-02-26T04:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73677",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
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

archive/issue_comments_073678.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-26T20:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73678",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019910.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T22:19:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8320#event-19910"
}
```



---

archive/issue_comments_073679.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T22:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73679",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_073680.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8320-html_short_title.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-html_short_title.patch)\n2. [trac_8320-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-reviewer.patch)",
    "created_at": "2010-03-02T22:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8320#issuecomment-73680",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac_8320-html_short_title.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-html_short_title.patch)
2. [trac_8320-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-reviewer.patch)
