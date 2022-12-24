# Issue 7871: Mis-specified background color for interacts

archive/issues_007871.json:
```json
{
    "body": "Assignee: was\n\nCC:  kcrisman timdumol\n\nIE 7/8 use a bluish background color for `interact` tables, instead of white.\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/d3feb880dcecfcb6#).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7871\n\n",
    "created_at": "2010-01-08T09:28:36Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "Mis-specified background color for interacts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7871",
    "user": "mpatel"
}
```
Assignee: was

CC:  kcrisman timdumol

IE 7/8 use a bluish background color for `interact` tables, instead of white.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/d3feb880dcecfcb6#).

Issue created by migration from https://trac.sagemath.org/ticket/7871





---

archive/issue_comments_068328.json:
```json
{
    "body": "Attachment [trac_7871-interact_bgcolor.patch](tarball://root/attachments/some-uuid/ticket7871/trac_7871-interact_bgcolor.patch) by mpatel created at 2010-01-08 09:31:15\n\nFix CSS color.  sagenb repo.",
    "created_at": "2010-01-08T09:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7871#issuecomment-68328",
    "user": "mpatel"
}
```

Attachment [trac_7871-interact_bgcolor.patch](tarball://root/attachments/some-uuid/ticket7871/trac_7871-interact_bgcolor.patch) by mpatel created at 2010-01-08 09:31:15

Fix CSS color.  sagenb repo.



---

archive/issue_comments_068329.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-08T09:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7871#issuecomment-68329",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068330.json:
```json
{
    "body": "The patch is minimal, but it seems to work for me in IE8 on Windows XP.  I'll clean up and move `interact` CSS directives to the main stylesheet in a separate ticket.",
    "created_at": "2010-01-08T09:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7871#issuecomment-68330",
    "user": "mpatel"
}
```

The patch is minimal, but it seems to work for me in IE8 on Windows XP.  I'll clean up and move `interact` CSS directives to the main stylesheet in a separate ticket.



---

archive/issue_comments_068331.json:
```json
{
    "body": "Still looks good on FF3.5, Safari 4, and Chrome on a Mac.  At least, I think I changed it - unfortunately, this HTML doesn't show up in View->Source, and I'm not sure where to look for it - what is the relevant CSS file name in the rendered worksheet directory?  Probably someone should check on FF on Windows and Linux, but the one-character change seems fine.",
    "created_at": "2010-01-08T15:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7871#issuecomment-68331",
    "user": "kcrisman"
}
```

Still looks good on FF3.5, Safari 4, and Chrome on a Mac.  At least, I think I changed it - unfortunately, this HTML doesn't show up in View->Source, and I'm not sure where to look for it - what is the relevant CSS file name in the rendered worksheet directory?  Probably someone should check on FF on Windows and Linux, but the one-character change seems fine.



---

archive/issue_comments_068332.json:
```json
{
    "body": "The markup is inserted dynamically.  To view live changes in Safari / Chrome, evaluate an `interact` cell, right-click on the output, and select \"Inspect Element.\"  This should open the \"Web Inspector\" / \"Developer Tools,\" which should also be available under some menu (the location and name depend on the browser, OS, etc.).  Anyway, try browsing to the cell under \"Elements\" (an instantaneous tree-like representation of the page).\n\nOpera and IE8 have similar, built-in tools.  For Firefox, I suggest installing the [Firebug extension](http://getfirebug.com/).",
    "created_at": "2010-01-08T16:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7871#issuecomment-68332",
    "user": "mpatel"
}
```

The markup is inserted dynamically.  To view live changes in Safari / Chrome, evaluate an `interact` cell, right-click on the output, and select "Inspect Element."  This should open the "Web Inspector" / "Developer Tools," which should also be available under some menu (the location and name depend on the browser, OS, etc.).  Anyway, try browsing to the cell under "Elements" (an instantaneous tree-like representation of the page).

Opera and IE8 have similar, built-in tools.  For Firefox, I suggest installing the [Firebug extension](http://getfirebug.com/).



---

archive/issue_comments_068333.json:
```json
{
    "body": "Great, I just needed to check that I actually HAD made the change for real and not just in some file deep in the site-packages directory.   So positive review, modulo someone other than the author of the patch testing it on IE.",
    "created_at": "2010-01-08T16:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7871#issuecomment-68333",
    "user": "kcrisman"
}
```

Great, I just needed to check that I actually HAD made the change for real and not just in some file deep in the site-packages directory.   So positive review, modulo someone other than the author of the patch testing it on IE.



---

archive/issue_comments_068334.json:
```json
{
    "body": "Finally got to test it on IE 7 - great catch!",
    "created_at": "2010-01-11T20:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7871#issuecomment-68334",
    "user": "kcrisman"
}
```

Finally got to test it on IE 7 - great catch!



---

archive/issue_comments_068335.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-11T20:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7871#issuecomment-68335",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068336.json:
```json
{
    "body": "merged into sagenb-0.5.",
    "created_at": "2010-01-12T21:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7871#issuecomment-68336",
    "user": "was"
}
```

merged into sagenb-0.5.



---

archive/issue_comments_068337.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-12T21:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7871#issuecomment-68337",
    "user": "was"
}
```

Resolution: fixed
