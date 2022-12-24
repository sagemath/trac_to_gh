# Issue 8202: Allow raw HTML in jsMath's \hbox{}

archive/issues_008202.json:
```json
{
    "body": "Assignee: was\n\nCC:  rbeezer\n\nWe can do this by setting `safeHBoxes` to 0 in `sagenb/data/sage/js/jsmath.js`.\n\nSee [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/b56eb3ec554642ce).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8202\n\n",
    "created_at": "2010-02-06T19:58:18Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Allow raw HTML in jsMath's \\hbox{}",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8202",
    "user": "mpatel"
}
```
Assignee: was

CC:  rbeezer

We can do this by setting `safeHBoxes` to 0 in `sagenb/data/sage/js/jsmath.js`.

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/b56eb3ec554642ce).

Issue created by migration from https://trac.sagemath.org/ticket/8202





---

archive/issue_comments_072345.json:
```json
{
    "body": "Disable jsMath's `safeHBoxes` option.  sagenb repo.",
    "created_at": "2010-02-06T20:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8202#issuecomment-72345",
    "user": "mpatel"
}
```

Disable jsMath's `safeHBoxes` option.  sagenb repo.



---

archive/issue_comments_072346.json:
```json
{
    "body": "Attachment [trac_8202-jsmath_hboxes.patch](tarball://root/attachments/some-uuid/ticket8202/trac_8202-jsmath_hboxes.patch) by mpatel created at 2010-02-06 20:03:34\n\nI've attached a patch that only disables jsMath's safe `\\hbox{}` setting.  Feel free to ignore it!",
    "created_at": "2010-02-06T20:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8202#issuecomment-72346",
    "user": "mpatel"
}
```

Attachment [trac_8202-jsmath_hboxes.patch](tarball://root/attachments/some-uuid/ticket8202/trac_8202-jsmath_hboxes.patch) by mpatel created at 2010-02-06 20:03:34

I've attached a patch that only disables jsMath's safe `\hbox{}` setting.  Feel free to ignore it!



---

archive/issue_comments_072347.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-06T20:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8202#issuecomment-72347",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072348.json:
```json
{
    "body": "The patch should apply cleanly to SageNB 0.7.4 (cf. #8051), which will be part of Sage 4.3.2.  But it may also work with SageNB 0.6.",
    "created_at": "2010-02-06T20:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8202#issuecomment-72348",
    "user": "mpatel"
}
```

The patch should apply cleanly to SageNB 0.7.4 (cf. #8051), which will be part of Sage 4.3.2.  But it may also work with SageNB 0.6.



---

archive/issue_comments_072349.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-07T04:40:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8202#issuecomment-72349",
    "user": "rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072350.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> The patch should apply cleanly to SageNB 0.7.4 (cf. #8051), which will be part of Sage 4.3.2.  But it may also work with SageNB 0.6.\n\nI've tested this on 4.3.1 with SageNB 0.7.4 (cf. #8051).  It behaves as expected with patch applied (and behavior reverts when I pop it off).  This is a big help with rendering my textbook-conversion experiments.  Thanks for the help.\n\nPositive review.\n\nRob",
    "created_at": "2010-02-07T04:40:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8202#issuecomment-72350",
    "user": "rbeezer"
}
```

Replying to [comment:2 mpatel]:
> The patch should apply cleanly to SageNB 0.7.4 (cf. #8051), which will be part of Sage 4.3.2.  But it may also work with SageNB 0.6.

I've tested this on 4.3.1 with SageNB 0.7.4 (cf. #8051).  It behaves as expected with patch applied (and behavior reverts when I pop it off).  This is a big help with rendering my textbook-conversion experiments.  Thanks for the help.

Positive review.

Rob



---

archive/issue_comments_072351.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-10T18:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8202#issuecomment-72351",
    "user": "mpatel"
}
```

Resolution: fixed
