# Issue 2779: Error message for notebook server already running is misleading

archive/issues_002779.json:
```json
{
    "body": "Assignee: boothby\n\nIf I have a notebook server already running, and I start a new one, I get something like this:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.11, Release Date: 2008-03-30                        |\n| Type notebook() for the GUI, and license() for information.        |\nPlease wait while the SAGE Notebook server starts...\n...\nThe notebook files are stored in: /Users/justin/.sage//sage_notebook\nPort 8000 is already in use.\nTrying next port...\n****************************************************\n*                                                  *\n* Open your web browser to https://localhost:8001  *\n*                                                  *\n****************************************************\nThere is an admin account.  If you do not remember the password,\nquit the notebook and type notebook(reset=True).\nAnother twistd server is running, PID 19662\n\nThis could either be a previously started instance of your application or a\ndifferent application entirely. To start a new one, either run it in some other\ndirectory, or use the --pidfile and --logfile parameters to avoid clashes.\n```\n\n\nIt's not clear how to use the second suggestion (using the additional parameters), and I sure couldn't get it to work.\n\nUsing an alternate directory does work, but that somehow didn't come through in this error message.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2779\n\n",
    "created_at": "2008-04-02T20:38:45Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "Error message for notebook server already running is misleading",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2779",
    "user": "justin"
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

archive/issue_comments_019086.json:
```json
{
    "body": "Could you suggest a specific better error message?  Oh, and post a patch :-)",
    "created_at": "2008-04-02T21:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19086",
    "user": "was"
}
```

Could you suggest a specific better error message?  Oh, and post a patch :-)



---

archive/issue_comments_019087.json:
```json
{
    "body": "This new patch should do it. It outputs the following message instead:\n\n\n```\nAnother Sage Notebook server is running, PID 13463.\n\nPlease either stop the old server or run the new server in a different directory.\n```\n",
    "created_at": "2010-01-16T20:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19087",
    "user": "timdumol"
}
```

This new patch should do it. It outputs the following message instead:


```
Another Sage Notebook server is running, PID 13463.

Please either stop the old server or run the new server in a different directory.
```




---

archive/issue_comments_019088.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T20:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19088",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_019089.json:
```json
{
    "body": "Outputs a clearer error message (see comment)",
    "created_at": "2010-01-16T23:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19089",
    "user": "timdumol"
}
```

Outputs a clearer error message (see comment)



---

archive/issue_comments_019090.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-17T19:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19090",
    "user": "wjp"
}
```

Attachment



---

archive/issue_comments_019091.json:
```json
{
    "body": "Attachment\n\nPositive review for Tim's patch. It works great for me.\n\nI've added a second minor patch (to be applied after `trac_2779-sagenb-error-message.patch`) that moves displaying the \"Please open your browser\" banner to below the check Tim added.",
    "created_at": "2010-01-17T19:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19091",
    "user": "wjp"
}
```

Attachment

Positive review for Tim's patch. It works great for me.

I've added a second minor patch (to be applied after `trac_2779-sagenb-error-message.patch`) that moves displaying the "Please open your browser" banner to below the check Tim added.



---

archive/issue_comments_019092.json:
```json
{
    "body": "Positive review on the reviewer patch. I'll mark this as positive review now.",
    "created_at": "2010-01-17T19:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19092",
    "user": "timdumol"
}
```

Positive review on the reviewer patch. I'll mark this as positive review now.



---

archive/issue_comments_019093.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T19:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19093",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_019094.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2779#issuecomment-19094",
    "user": "timdumol"
}
```

Resolution: fixed
