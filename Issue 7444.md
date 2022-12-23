# Issue 7444: Broken: searching published worksheets after publishing a worksheet for the first time

archive/issues_007444.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was timdumol\n\nFrom Tim Dumol (also [comment:6:ticket:7343 here]):\n\nCreating and publishing a worksheet, and then searching for it on the /pub/ page causes an HTTP 500. Server logs show:\n\n\n```\n[...]\nFile \"/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/twist.py\", line 1652, in render\n            s = render_worksheet_list(ctx.args, pub=True, username=self.username)\n          File \"/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/twist.py\", line 1483, in render_worksheet_list\n            search=search, reverse=reverse)\n          File \"/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/notebook.py\", line 1292, in worksheet_list_for_public\n            W = [x for x in W if x.satisfies_search(search)]\n          File \"/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/worksheet.py\", line 1977, in satisfies_search\n            + open(filename).read().lower())\nexceptions.IOError: [Errno 2] No such file or directory: '/home/timdumol/.sage/sage_notebook.sagenb/home/pub/0/worksheet.html'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7444\n\n",
    "created_at": "2009-11-12T14:02:43Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Broken: searching published worksheets after publishing a worksheet for the first time",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7444",
    "user": "mpatel"
}
```
Assignee: boothby

CC:  was timdumol

From Tim Dumol (also [comment:6:ticket:7343 here]):

Creating and publishing a worksheet, and then searching for it on the /pub/ page causes an HTTP 500. Server logs show:


```
[...]
File "/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/twist.py", line 1652, in render
            s = render_worksheet_list(ctx.args, pub=True, username=self.username)
          File "/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/twist.py", line 1483, in render_worksheet_list
            search=search, reverse=reverse)
          File "/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/notebook.py", line 1292, in worksheet_list_for_public
            W = [x for x in W if x.satisfies_search(search)]
          File "/opt/sage-bin/local/lib/python2.6/site-packages/sagenb/notebook/worksheet.py", line 1977, in satisfies_search
            + open(filename).read().lower())
exceptions.IOError: [Errno 2] No such file or directory: '/home/timdumol/.sage/sage_notebook.sagenb/home/pub/0/worksheet.html'
```


Issue created by migration from https://trac.sagemath.org/ticket/7444





---

archive/issue_comments_062671.json:
```json
{
    "body": "Save a newly initialized worksheet.  Apply to sagenb repo.",
    "created_at": "2009-11-12T14:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7444#issuecomment-62671",
    "user": "mpatel"
}
```

Save a newly initialized worksheet.  Apply to sagenb repo.



---

archive/issue_comments_062672.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-12T14:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7444#issuecomment-62672",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062673.json:
```json
{
    "body": "Attachment\n\nNotes:\n\n* This depends on #7428.\n* I assume it's OK to call `worksheet.save` in `notebook._initialize_worksheet`.\n* `TestWorksheetList.test_searching_for_worksheets` no longer fails --- it now yields an error.",
    "created_at": "2009-11-12T14:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7444#issuecomment-62673",
    "user": "mpatel"
}
```

Attachment

Notes:

* This depends on #7428.
* I assume it's OK to call `worksheet.save` in `notebook._initialize_worksheet`.
* `TestWorksheetList.test_searching_for_worksheets` no longer fails --- it now yields an error.



---

archive/issue_comments_062674.json:
```json
{
    "body": "Patch works. Positive review.\n\nThe error is due to the lack of the javascript libraries on the Log page. This is now #7455.",
    "created_at": "2009-11-13T20:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7444#issuecomment-62674",
    "user": "timdumol"
}
```

Patch works. Positive review.

The error is due to the lack of the javascript libraries on the Log page. This is now #7455.



---

archive/issue_comments_062675.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-13T20:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7444#issuecomment-62675",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062676.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-08T05:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7444#issuecomment-62676",
    "user": "was"
}
```

Resolution: fixed
