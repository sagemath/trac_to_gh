# Issue 8141: Update font stacks, sans-serif and monospace, for SageNB pages

archive/issues_008141.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @TimDumol @williamstein\n\nFont families (typefaces?) on rendered Sage Notebook pages.\n\nSee [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/533afb39f9f8220f).\n\nNote: Server administrators can already save\n\n```\nhttp://server/css/main.css\n```\n\nto\n\n```\nDOT_SAGE/notebook.css\n```\n\nand edit the latter, according to taste.\n\nLinks:\n\n* http://www.codestyle.org/css/font-family/BuildBetterCSSFontStacks.shtml\n* http://safalra.com/web-design/typography/web-safe-fonts-myth/\n* http://unitinteractive.com/blog/2008/06/26/better-css-font-stacks/\n\nIssue created by migration from https://trac.sagemath.org/ticket/8141\n\n",
    "created_at": "2010-02-01T06:23:42Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Update font stacks, sans-serif and monospace, for SageNB pages",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8141",
    "user": "@qed777"
}
```
Assignee: @williamstein

CC:  @TimDumol @williamstein

Font families (typefaces?) on rendered Sage Notebook pages.

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/533afb39f9f8220f).

Note: Server administrators can already save

```
http://server/css/main.css
```

to

```
DOT_SAGE/notebook.css
```

and edit the latter, according to taste.

Links:

* http://www.codestyle.org/css/font-family/BuildBetterCSSFontStacks.shtml
* http://safalra.com/web-design/typography/web-safe-fonts-myth/
* http://unitinteractive.com/blog/2008/06/26/better-css-font-stacks/

Issue created by migration from https://trac.sagemath.org/ticket/8141





---

archive/issue_comments_071582.json:
```json
{
    "body": "Attachment [trac_8141-font_stacks.patch](tarball://root/attachments/some-uuid/ticket8141/trac_8141-font_stacks.patch) by @qed777 created at 2010-02-01 06:26:31\n\nMore consistent use of font stack mixins.  sagenb repository.",
    "created_at": "2010-02-01T06:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8141#issuecomment-71582",
    "user": "@qed777"
}
```

Attachment [trac_8141-font_stacks.patch](tarball://root/attachments/some-uuid/ticket8141/trac_8141-font_stacks.patch) by @qed777 created at 2010-02-01 06:26:31

More consistent use of font stack mixins.  sagenb repository.



---

archive/issue_comments_071583.json:
```json
{
    "body": "The main purpose of the patch is to use the SASS font stack mixins in `sagenb/sass/src/partials/_mixins.sass` throughout the notebook stylesheets.\n\nI've replaced the original sans-serif stack\n\n```\n\"Gill Sans\", \"Gill Sans MT\", \"Myriad Pro\", Myriad, \"Liberation Sans\", \"Nimbus Sans L\", Tahoma, Geneva, \"Helvetica Neue\", Helvetica, Arial, sans-serif\n```\n\nwith\n\n```\n'Arial', 'Helvetica', sans-serif\n```\n\nin an attempt to reproduce the pre-#7786 fonts.  But I don't have a strong opinion on what we should use.  Feel free to use other sets!",
    "created_at": "2010-02-01T06:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8141#issuecomment-71583",
    "user": "@qed777"
}
```

The main purpose of the patch is to use the SASS font stack mixins in `sagenb/sass/src/partials/_mixins.sass` throughout the notebook stylesheets.

I've replaced the original sans-serif stack

```
"Gill Sans", "Gill Sans MT", "Myriad Pro", Myriad, "Liberation Sans", "Nimbus Sans L", Tahoma, Geneva, "Helvetica Neue", Helvetica, Arial, sans-serif
```

with

```
'Arial', 'Helvetica', sans-serif
```

in an attempt to reproduce the pre-#7786 fonts.  But I don't have a strong opinion on what we should use.  Feel free to use other sets!



---

archive/issue_comments_071584.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-05T07:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8141#issuecomment-71584",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071585.json:
```json
{
    "body": "Attachment [trac_8141-font_stacks.2.patch](tarball://root/attachments/some-uuid/ticket8141/trac_8141-font_stacks.2.patch) by @qed777 created at 2010-02-21 00:33:16\n\nDon't override non-compute cells' fonts.  Replaces previous.",
    "created_at": "2010-02-21T00:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8141#issuecomment-71585",
    "user": "@qed777"
}
```

Attachment [trac_8141-font_stacks.2.patch](tarball://root/attachments/some-uuid/ticket8141/trac_8141-font_stacks.2.patch) by @qed777 created at 2010-02-21 00:33:16

Don't override non-compute cells' fonts.  Replaces previous.



---

archive/issue_comments_071586.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-25T21:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8141#issuecomment-71586",
    "user": "mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071587.json:
```json
{
    "body": "This seems to work well in sage-4.3.3.  Checked on firefox and safari and it looks good.  Positive review.",
    "created_at": "2010-02-25T21:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8141#issuecomment-71587",
    "user": "mhampton"
}
```

This seems to work well in sage-4.3.3.  Checked on firefox and safari and it looks good.  Positive review.



---

archive/issue_comments_071588.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-04T22:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8141#issuecomment-71588",
    "user": "@qed777"
}
```

Resolution: fixed
