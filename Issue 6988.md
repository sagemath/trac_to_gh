# Issue 6988: [with patch, positive review] error building PDF version of reference manual on Sage 4.1.2.alpha2

archive/issues_006988.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nAs the subject says. I'm making this a blocker as it's critical to have both the HTML and PDF versions of every document in the standard documentation build without errors. We do distribute those documents separately from the source and binary tarballs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6988\n\n",
    "closed_at": "2009-09-22T19:24:40Z",
    "created_at": "2009-09-22T16:52:09Z",
    "labels": [
        "component: documentation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] error building PDF version of reference manual on Sage 4.1.2.alpha2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: @jhpalmieri

As the subject says. I'm making this a blocker as it's critical to have both the HTML and PDF versions of every document in the standard documentation build without errors. We do distribute those documents separately from the source and binary tarballs.

Issue created by migration from https://trac.sagemath.org/ticket/6988





---

archive/issue_comments_057691.json:
```json
{
    "body": "Changing assignee from tba to @jhpalmieri.",
    "created_at": "2009-09-22T18:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6988#issuecomment-57691",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from tba to @jhpalmieri.



---

archive/issue_comments_057692.json:
```json
{
    "body": "The issue is that in LaTeX, lists can only be nested four deep, and the file rings/ring.pyx had 6 levels of nesting.  The attached patch rephrases things so that there are only 4 levels of nesting again.",
    "created_at": "2009-09-22T18:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6988#issuecomment-57692",
    "user": "https://github.com/jhpalmieri"
}
```

The issue is that in LaTeX, lists can only be nested four deep, and the file rings/ring.pyx had 6 levels of nesting.  The attached patch rephrases things so that there are only 4 levels of nesting again.



---

archive/issue_comments_057693.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-22T18:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6988#issuecomment-57693",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_events_016407.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-22T19:24:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6988",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6988#event-16407"
}
```



---

archive/issue_comments_057694.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-22T19:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6988#issuecomment-57694",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057695.json:
```json
{
    "body": "Attachment [trac_6988-unnest.patch](tarball://root/attachments/some-uuid/ticket6988/trac_6988-unnest.patch) by mvngu created at 2009-09-22 19:24:40",
    "created_at": "2009-09-22T19:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6988#issuecomment-57695",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6988-unnest.patch](tarball://root/attachments/some-uuid/ticket6988/trac_6988-unnest.patch) by mvngu created at 2009-09-22 19:24:40



---

archive/issue_comments_057696.json:
```json
{
    "body": "I think #6885 is a duplicate.",
    "created_at": "2009-09-22T20:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6988#issuecomment-57696",
    "user": "https://github.com/qed777"
}
```

I think #6885 is a duplicate.



---

archive/issue_comments_057697.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.",
    "created_at": "2009-09-27T09:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6988#issuecomment-57697",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.
