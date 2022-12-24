# Issue 7418: %maxima cells are partially broken

archive/issues_007418.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @TimDumol\n\nIn the new sage notebook maxima cells do not work anymore for inputs\nstarting with '%'.\n\n\n```\n%maxima\n%pi\n\nTraceback (click to the left for traceback)\n...\nAttributeError: 'sage.symbolic.expression.Expression' object has no\nattribute 'eval'\n```\n\n\nor:\n\n\n```\n%maxima\n%e^(%i * %pi)\n\nSyntax Error:\n    %e^(%i * %pi)\n```\n\n\nThis used to work with older Sage versions.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7418\n\n",
    "created_at": "2009-11-09T16:47:10Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "%maxima cells are partially broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7418",
    "user": "whuss"
}
```
Assignee: boothby

CC:  @williamstein @TimDumol

In the new sage notebook maxima cells do not work anymore for inputs
starting with '%'.


```
%maxima
%pi

Traceback (click to the left for traceback)
...
AttributeError: 'sage.symbolic.expression.Expression' object has no
attribute 'eval'
```


or:


```
%maxima
%e^(%i * %pi)

Syntax Error:
    %e^(%i * %pi)
```


This used to work with older Sage versions.

Issue created by migration from https://trac.sagemath.org/ticket/7418





---

archive/issue_comments_062415.json:
```json
{
    "body": "I think the best fix for this is to break from processing the percent directives once a system directive has been reached.  It should be easy to detect this as the system directives are the \"unknown\" one has been reached.",
    "created_at": "2009-11-09T18:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62415",
    "user": "@mwhansen"
}
```

I think the best fix for this is to break from processing the percent directives once a system directive has been reached.  It should be easy to detect this as the system directives are the "unknown" one has been reached.



---

archive/issue_comments_062416.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T04:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62416",
    "user": "@mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062417.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-17T06:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62417",
    "user": "@TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062418.json:
```json
{
    "body": "Applying the patch on the latest version off the repository (sagenb-0.5.0 + #7843 + #7844 + #7846 + #7871) causes the system directives to display (%html, %maxima, etc. are visible on output).",
    "created_at": "2010-01-17T06:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62418",
    "user": "@TimDumol"
}
```

Applying the patch on the latest version off the repository (sagenb-0.5.0 + #7843 + #7844 + #7846 + #7871) causes the system directives to display (%html, %maxima, etc. are visible on output).



---

archive/issue_comments_062419.json:
```json
{
    "body": "Sorry about that.  I put up a new patch which should fix it.  I opted for duplicating the directives.append line instead of having some sort of check to see if the system was set as it makes the flow a little cleaner.",
    "created_at": "2010-01-17T22:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62419",
    "user": "@mwhansen"
}
```

Sorry about that.  I put up a new patch which should fix it.  I opted for duplicating the directives.append line instead of having some sort of check to see if the system was set as it makes the flow a little cleaner.



---

archive/issue_comments_062420.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-17T22:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62420",
    "user": "@mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062421.json:
```json
{
    "body": "Same problem still here (sagenb-0.6)",
    "created_at": "2010-01-19T08:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62421",
    "user": "@TimDumol"
}
```

Same problem still here (sagenb-0.6)



---

archive/issue_comments_062422.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-19T08:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62422",
    "user": "@TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062423.json:
```json
{
    "body": "Add one.  Rebased for queue in comment.  Replaces previous.",
    "created_at": "2010-01-25T08:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62423",
    "user": "@qed777"
}
```

Add one.  Rebased for queue in comment.  Replaces previous.



---

archive/issue_comments_062424.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-25T08:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62424",
    "user": "@qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062425.json:
```json
{
    "body": "Attachment [trac_7418-maxima_cells.2.patch](tarball://root/attachments/some-uuid/ticket7418/trac_7418-maxima_cells.2.patch) by @qed777 created at 2010-01-25 08:07:53\n\nV2 adds one --- I hope it's in the right place.  The queue:\n\n```\nSageNB 0.7 / #8051\ntrac_7784-hgignore_update.patch\ntrac_5712-interrupt-notification.5.patch\ntrac_6069-missing_pub_ws.2.patch\ntrac_8038-email_plus_addressing_v2.patch\ntrac_7506-notebook_object-documentation.2.patch\ntrac_693-spawn_notebook.3.patch\ntrac_5177-delete-cell-dirs.2.patch\ntrac_7418-maxima_cells.2.patch\n```\n\nThe patch version numbers may be off by one or so.\n\nPositive review, but someone should review my change.",
    "created_at": "2010-01-25T08:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62425",
    "user": "@qed777"
}
```

Attachment [trac_7418-maxima_cells.2.patch](tarball://root/attachments/some-uuid/ticket7418/trac_7418-maxima_cells.2.patch) by @qed777 created at 2010-01-25 08:07:53

V2 adds one --- I hope it's in the right place.  The queue:

```
SageNB 0.7 / #8051
trac_7784-hgignore_update.patch
trac_5712-interrupt-notification.5.patch
trac_6069-missing_pub_ws.2.patch
trac_8038-email_plus_addressing_v2.patch
trac_7506-notebook_object-documentation.2.patch
trac_693-spawn_notebook.3.patch
trac_5177-delete-cell-dirs.2.patch
trac_7418-maxima_cells.2.patch
```

The patch version numbers may be off by one or so.

Positive review, but someone should review my change.



---

archive/issue_comments_062426.json:
```json
{
    "body": "LGTM. Positive review.",
    "created_at": "2010-04-21T20:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62426",
    "user": "@TimDumol"
}
```

LGTM. Positive review.



---

archive/issue_comments_062427.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-21T20:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62427",
    "user": "@TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062428.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-11T06:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7418#issuecomment-62428",
    "user": "@TimDumol"
}
```

Resolution: fixed
