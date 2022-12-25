# Issue 6742: Stylesheets are not always loaded in Chrome

archive/issues_006742.json:
```json
{
    "body": "Assignee: boothby\n\nStart a local Sage notebook server and open a worksheet list or any worksheet in Chrome.  The HTML is rendered strangely, as if `main.css` has not been retrieved.  In particular, \"Searching for Sage server...\" is always visible at the top of a worksheet, as are the slide controls.\n\nHowever, the \"Edit,\" \"Text,\" \"Undo,\" \"Share,\" and \"Publish\" pages, say, are rendered properly.\n\nThis happens in Chrome 2 on Windows XP when connecting to a Fedora 10 Linux Sage notebook server on the same subnet.\n\n[This](http://code.google.com/p/chromium/issues/detail?id=4181) might be relevant.\n\nCuriously, this **does not** happen with worksheets at `sagenb.org`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6742\n\n",
    "created_at": "2009-08-14T05:26:01Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Stylesheets are not always loaded in Chrome",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6742",
    "user": "https://github.com/qed777"
}
```
Assignee: boothby

Start a local Sage notebook server and open a worksheet list or any worksheet in Chrome.  The HTML is rendered strangely, as if `main.css` has not been retrieved.  In particular, "Searching for Sage server..." is always visible at the top of a worksheet, as are the slide controls.

However, the "Edit," "Text," "Undo," "Share," and "Publish" pages, say, are rendered properly.

This happens in Chrome 2 on Windows XP when connecting to a Fedora 10 Linux Sage notebook server on the same subnet.

[This](http://code.google.com/p/chromium/issues/detail?id=4181) might be relevant.

Curiously, this **does not** happen with worksheets at `sagenb.org`.

Issue created by migration from https://trac.sagemath.org/ticket/6742





---

archive/issue_comments_055143.json:
```json
{
    "body": "Attachment [trac_6742-chrome_css.patch](tarball://root/attachments/some-uuid/ticket6742/trac_6742-chrome_css.patch) by @qed777 created at 2009-08-14 06:40:21\n\nServe main.css with MIME type text/css.",
    "created_at": "2009-08-14T06:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6742#issuecomment-55143",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6742-chrome_css.patch](tarball://root/attachments/some-uuid/ticket6742/trac_6742-chrome_css.patch) by @qed777 created at 2009-08-14 06:40:21

Serve main.css with MIME type text/css.



---

archive/issue_comments_055144.json:
```json
{
    "body": "With the attached patch, the notebook server now serves `main.css` with the MIME type `text/css`.  This placates Chrome, which now renders worksheets and the worksheet list properly.\n\nIn particular, the Web Inspector's console no longer contains the line\n\n```\nResource interpreted as stylesheet but transferred with MIME type text/plain.\n```\nabout `main.css`.  There are a similar messages\n\n```\nResource interpreted as script but transferred with MIME type text/plain.\nResource interpreted as other but transferred with MIME type text/x-javascript.\n```\nfor `main.js` and the jsMath extensions.  It seems that WebKit / Chrome lets this pass, for now.",
    "created_at": "2009-08-14T06:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6742#issuecomment-55144",
    "user": "https://github.com/qed777"
}
```

With the attached patch, the notebook server now serves `main.css` with the MIME type `text/css`.  This placates Chrome, which now renders worksheets and the worksheet list properly.

In particular, the Web Inspector's console no longer contains the line

```
Resource interpreted as stylesheet but transferred with MIME type text/plain.
```
about `main.css`.  There are a similar messages

```
Resource interpreted as script but transferred with MIME type text/plain.
Resource interpreted as other but transferred with MIME type text/x-javascript.
```
for `main.js` and the jsMath extensions.  It seems that WebKit / Chrome lets this pass, for now.



---

archive/issue_comments_055145.json:
```json
{
    "body": "Looks good to me.  Yep, this should also be done for the javascript code that is served up by twisted.",
    "created_at": "2009-09-01T22:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6742#issuecomment-55145",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  Yep, this should also be done for the javascript code that is served up by twisted.



---

archive/issue_events_015905.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-02T05:15:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6742",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6742#event-15905"
}
```



---

archive/issue_events_015906.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-02T05:15:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6742",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6742#event-15906"
}
```



---

archive/issue_comments_055146.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T05:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6742#issuecomment-55146",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
