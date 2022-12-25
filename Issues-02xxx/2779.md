# Issue 2779: Error message for notebook server already running is misleading

archive/issues_002779.json:
```json
{
    "body": "Assignee: boothby\n\nIf I have a notebook server already running, and I start a new one, I get something like this:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.11, Release Date: 2008-03-30                        |\n| Type notebook() for the GUI, and license() for information.        |\nPlease wait while the SAGE Notebook server starts...\n...\nThe notebook files are stored in: /Users/justin/.sage//sage_notebook\nPort 8000 is already in use.\nTrying next port...\n****************************************************\n*                                                  *\n* Open your web browser to https://localhost:8001  *\n*                                                  *\n****************************************************\nThere is an admin account.  If you do not remember the password,\nquit the notebook and type notebook(reset=True).\nAnother twistd server is running, PID 19662\n\nThis could either be a previously started instance of your application or a\ndifferent application entirely. To start a new one, either run it in some other\ndirectory, or use the --pidfile and --logfile parameters to avoid clashes.\n```\n\nIt's not clear how to use the second suggestion (using the additional parameters), and I sure couldn't get it to work.\n\nUsing an alternate directory does work, but that somehow didn't come through in this error message.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2779\n\n",
    "closed_at": "2010-01-19T03:32:07Z",
    "created_at": "2008-04-02T20:38:45Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Error message for notebook server already running is misleading",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2779",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: boothby

If I have a notebook server already running, and I start a new one, I get something like this:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.11, Release Date: 2008-03-30                        |
| Type notebook() for the GUI, and license() for information.        |
Please wait while the SAGE Notebook server starts...
...
The notebook files are stored in: /Users/justin/.sage//sage_notebook
Port 8000 is already in use.
Trying next port...
****************************************************
*                                                  *
* Open your web browser to https://localhost:8001  *
*                                                  *
****************************************************
There is an admin account.  If you do not remember the password,
quit the notebook and type notebook(reset=True).
Another twistd server is running, PID 19662

This could either be a previously started instance of your application or a
different application entirely. To start a new one, either run it in some other
directory, or use the --pidfile and --logfile parameters to avoid clashes.
```

It's not clear how to use the second suggestion (using the additional parameters), and I sure couldn't get it to work.

Using an alternate directory does work, but that somehow didn't come through in this error message.



Issue created by migration from https://trac.sagemath.org/ticket/2779





---

archive/issue_events_006418.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-02T21:36:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2779#event-6418"
}
```



---

archive/issue_comments_019046.json:
```json
{
    "body": "Could you suggest a specific better error message?  Oh, and post a patch :-)",
    "created_at": "2008-04-02T21:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19046",
    "user": "https://github.com/williamstein"
}
```

Could you suggest a specific better error message?  Oh, and post a patch :-)



---

archive/issue_comments_019047.json:
```json
{
    "body": "This new patch should do it. It outputs the following message instead:\n\n```\nAnother Sage Notebook server is running, PID 13463.\n\nPlease either stop the old server or run the new server in a different directory.\n```",
    "created_at": "2010-01-16T20:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19047",
    "user": "https://github.com/TimDumol"
}
```

This new patch should do it. It outputs the following message instead:

```
Another Sage Notebook server is running, PID 13463.

Please either stop the old server or run the new server in a different directory.
```



---

archive/issue_comments_019048.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T20:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19048",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_019049.json:
```json
{
    "body": "Outputs a clearer error message (see comment)",
    "created_at": "2010-01-16T23:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19049",
    "user": "https://github.com/TimDumol"
}
```

Outputs a clearer error message (see comment)



---

archive/issue_comments_019050.json:
```json
{
    "body": "Attachment [trac_2779-sagenb-error-message.patch](tarball://root/attachments/some-uuid/ticket2779/trac_2779-sagenb-error-message.patch) by @wjp created at 2010-01-17 19:32:13",
    "created_at": "2010-01-17T19:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19050",
    "user": "https://github.com/wjp"
}
```

Attachment [trac_2779-sagenb-error-message.patch](tarball://root/attachments/some-uuid/ticket2779/trac_2779-sagenb-error-message.patch) by @wjp created at 2010-01-17 19:32:13



---

archive/issue_comments_019051.json:
```json
{
    "body": "Attachment [2779_2_banner.patch](tarball://root/attachments/some-uuid/ticket2779/2779_2_banner.patch) by @wjp created at 2010-01-17 19:38:13\n\nPositive review for Tim's patch. It works great for me.\n\nI've added a second minor patch (to be applied after `trac_2779-sagenb-error-message.patch`) that moves displaying the \"Please open your browser\" banner to below the check Tim added.",
    "created_at": "2010-01-17T19:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19051",
    "user": "https://github.com/wjp"
}
```

Attachment [2779_2_banner.patch](tarball://root/attachments/some-uuid/ticket2779/2779_2_banner.patch) by @wjp created at 2010-01-17 19:38:13

Positive review for Tim's patch. It works great for me.

I've added a second minor patch (to be applied after `trac_2779-sagenb-error-message.patch`) that moves displaying the "Please open your browser" banner to below the check Tim added.



---

archive/issue_comments_019052.json:
```json
{
    "body": "Positive review on the reviewer patch. I'll mark this as positive review now.",
    "created_at": "2010-01-17T19:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19052",
    "user": "https://github.com/TimDumol"
}
```

Positive review on the reviewer patch. I'll mark this as positive review now.



---

archive/issue_comments_019053.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T19:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19053",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006419.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:32:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2779#event-6419"
}
```



---

archive/issue_comments_019054.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19054",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed
