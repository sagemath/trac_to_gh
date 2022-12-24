# Issue 2117: problems with "...?starup_token=..." URL in notebook

archive/issues_002117.json:
```json
{
    "body": "Assignee: boothby\n\nThe following sequence of events leads to a \"Internal Server Error\" page:\n\n* Start up sage to serve a local notebook (sage -notebook)\n[Browser pops up with \"admin\" already logged in, using a \"startup_token\" url]\n* select some worksheets\n* click \"archive\"\n\nThe notebook seems to be in a sane condition afterwards. If I change the URL to \"https://localhost:8001/\" (i.e., remove the \"?startup_token=...\" part) everything seems as it should be. I guess the notebook barfs at this stage on the \"?\" part in the URL?\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2117\n\n",
    "created_at": "2008-02-08T18:47:44Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "problems with \"...?starup_token=...\" URL in notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2117",
    "user": "nbruin"
}
```
Assignee: boothby

The following sequence of events leads to a "Internal Server Error" page:

* Start up sage to serve a local notebook (sage -notebook)
[Browser pops up with "admin" already logged in, using a "startup_token" url]
* select some worksheets
* click "archive"

The notebook seems to be in a sane condition afterwards. If I change the URL to "https://localhost:8001/" (i.e., remove the "?startup_token=..." part) everything seems as it should be. I guess the notebook barfs at this stage on the "?" part in the URL?



Issue created by migration from https://trac.sagemath.org/ticket/2117





---

archive/issue_comments_013879.json:
```json
{
    "body": "As we don't get the URL at the beginning with the startup token, I'm going to mark this as invalid.  I can't reproduce it in 3.2.3.",
    "created_at": "2009-01-23T13:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2117#issuecomment-13879",
    "user": "mhansen"
}
```

As we don't get the URL at the beginning with the startup token, I'm going to mark this as invalid.  I can't reproduce it in 3.2.3.



---

archive/issue_comments_013880.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-23T13:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2117#issuecomment-13880",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_013881.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-01-23T16:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2117#issuecomment-13881",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_013882.json:
```json
{
    "body": "This came up last week on sage-edu with Sage 3.2.3, so there is certainly a bug to be found and fixed here. It was reproducible with a wiped .sage by someone who seemed technically competent enough not to make a dumb mistake. So I am reopening this.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T16:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2117#issuecomment-13882",
    "user": "mabshoff"
}
```

This came up last week on sage-edu with Sage 3.2.3, so there is certainly a bug to be found and fixed here. It was reproducible with a wiped .sage by someone who seemed technically competent enough not to make a dumb mistake. So I am reopening this.

Cheers,

Michael



---

archive/issue_comments_013883.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2009-01-23T16:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2117#issuecomment-13883",
    "user": "mabshoff"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_013884.json:
```json
{
    "body": "This thread ( http://groups.google.com/group/sage-edu/browse_thread/thread/4565115a21b28f5d/9e75206e7fada15b?lnk=gst&q=internal+server+error#9e75206e7fada15b ) is a different issue than the one reported here.",
    "created_at": "2009-01-24T01:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2117#issuecomment-13884",
    "user": "mhansen"
}
```

This thread ( http://groups.google.com/group/sage-edu/browse_thread/thread/4565115a21b28f5d/9e75206e7fada15b?lnk=gst&q=internal+server+error#9e75206e7fada15b ) is a different issue than the one reported here.



---

archive/issue_comments_013885.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-24T01:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2117#issuecomment-13885",
    "user": "mhansen"
}
```

Resolution: invalid
