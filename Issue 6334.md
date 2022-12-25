# Issue 6334: optional doctest failure -- broken finance doctest failures

archive/issues_006334.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @cswiercz\n\n\n```\nsage -t -long --optional devel/sage/sage/finance/stock.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/finance/stock.py\", line 180:\n    sage: finance.Stock('vmw').google()[:5]   # optional -- internet\nExpected:\n    [\n     28-Nov-07 80.57 88.49 80.57 87.69    7496000,\n     29-Nov-07 90.91 93.20 89.50 90.85    5497600,\n     30-Nov-07 95.39 95.60 89.85 91.37    4750200,\n      3-Dec-07 89.87 96.00 88.70 94.97    4401100,\n      4-Dec-07 92.26 97.10 92.05 95.08    2896600\n    ]\nGot:\n    [\n     16-Jun-08 66.00 67.50 65.60 67.47    1742000,\n     17-Jun-08 67.84 67.84 66.03 67.00    1196900,\n     18-Jun-08 66.50 66.56 64.76 66.19    1186400,\n     19-Jun-08 65.92 66.50 64.69 65.72     549200,\n     20-Jun-08 65.72 65.72 63.12 63.86    1242300\n    ]\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_9\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6334\n\n",
    "created_at": "2009-06-16T15:16:52Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optional doctest failure -- broken finance doctest failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6334",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @cswiercz


```
sage -t -long --optional devel/sage/sage/finance/stock.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/finance/stock.py", line 180:
    sage: finance.Stock('vmw').google()[:5]   # optional -- internet
Expected:
    [
     28-Nov-07 80.57 88.49 80.57 87.69    7496000,
     29-Nov-07 90.91 93.20 89.50 90.85    5497600,
     30-Nov-07 95.39 95.60 89.85 91.37    4750200,
      3-Dec-07 89.87 96.00 88.70 94.97    4401100,
      4-Dec-07 92.26 97.10 92.05 95.08    2896600
    ]
Got:
    [
     16-Jun-08 66.00 67.50 65.60 67.47    1742000,
     17-Jun-08 67.84 67.84 66.03 67.00    1196900,
     18-Jun-08 66.50 66.56 64.76 66.19    1186400,
     19-Jun-08 65.92 66.50 64.69 65.72     549200,
     20-Jun-08 65.72 65.72 63.12 63.86    1242300
    ]
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_9
***Test Failed*** 1 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/6334





---

archive/issue_comments_050459.json:
```json
{
    "body": "Changing assignee from tbd to @cswiercz.",
    "created_at": "2009-06-16T15:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6334#issuecomment-50459",
    "user": "https://github.com/cswiercz"
}
```

Changing assignee from tbd to @cswiercz.



---

archive/issue_comments_050460.json:
```json
{
    "body": "Attachment [sage-6334.patch](tarball://root/attachments/some-uuid/ticket6334/sage-6334.patch) by @cswiercz created at 2009-06-16 22:18:20\n\nI also updated stock.py's documentation for Sphinx formatting.",
    "created_at": "2009-06-16T22:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6334#issuecomment-50460",
    "user": "https://github.com/cswiercz"
}
```

Attachment [sage-6334.patch](tarball://root/attachments/some-uuid/ticket6334/sage-6334.patch) by @cswiercz created at 2009-06-16 22:18:20

I also updated stock.py's documentation for Sphinx formatting.



---

archive/issue_comments_050461.json:
```json
{
    "body": "Changing keywords from \"\" to \"finance, stock\".",
    "created_at": "2009-06-16T22:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6334#issuecomment-50461",
    "user": "https://github.com/cswiercz"
}
```

Changing keywords from "" to "finance, stock".



---

archive/issue_comments_050462.json:
```json
{
    "body": "1.  I still get 12 optional doctest failures, it looks like the requested dates are not being honored, but I haven't deduced a pattern to it.  Full output in attached text file.\n\n2.  Documentation can be built with a lot fewer blank lines, especially inbetween list elements.  Reviewer patch illustrates this and corrects one misspelled word.\n\n3.  I couldn't test the documentation since it doesn't seem to get pulled into the reference manual.  Should it be included?  If not, how should it be tested?",
    "created_at": "2009-07-17T04:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6334#issuecomment-50462",
    "user": "https://github.com/rbeezer"
}
```

1.  I still get 12 optional doctest failures, it looks like the requested dates are not being honored, but I haven't deduced a pattern to it.  Full output in attached text file.

2.  Documentation can be built with a lot fewer blank lines, especially inbetween list elements.  Reviewer patch illustrates this and corrects one misspelled word.

3.  I couldn't test the documentation since it doesn't seem to get pulled into the reference manual.  Should it be included?  If not, how should it be tested?



---

archive/issue_comments_050463.json:
```json
{
    "body": "sage -t -optional   output on  stock.py",
    "created_at": "2009-07-17T04:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6334#issuecomment-50463",
    "user": "https://github.com/rbeezer"
}
```

sage -t -optional   output on  stock.py



---

archive/issue_comments_050464.json:
```json
{
    "body": "Attachment [stock-tests.txt](tarball://root/attachments/some-uuid/ticket6334/stock-tests.txt) by @rbeezer created at 2009-07-17 04:02:12",
    "created_at": "2009-07-17T04:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6334#issuecomment-50464",
    "user": "https://github.com/rbeezer"
}
```

Attachment [stock-tests.txt](tarball://root/attachments/some-uuid/ticket6334/stock-tests.txt) by @rbeezer created at 2009-07-17 04:02:12



---

archive/issue_comments_050465.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-11T11:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6334#issuecomment-50465",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050466.json:
```json
{
    "body": "Attachment [trac_6334_reviewer_edits.patch](tarball://root/attachments/some-uuid/ticket6334/trac_6334_reviewer_edits.patch) by @burcin created at 2013-01-11 11:05:51\n\nIt looks like Minh fixed the documentation in `sage/finance` with [attachment:trac_9218-reviewer.patch:ticket:9218].\n\nThere is also #13884 to fix the optional doctests, where Karl-Dieter posted a patch.\n\nShall we close this ticket as duplicate?",
    "created_at": "2013-01-11T11:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6334#issuecomment-50466",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6334_reviewer_edits.patch](tarball://root/attachments/some-uuid/ticket6334/trac_6334_reviewer_edits.patch) by @burcin created at 2013-01-11 11:05:51

It looks like Minh fixed the documentation in `sage/finance` with [attachment:trac_9218-reviewer.patch:ticket:9218].

There is also #13884 to fix the optional doctests, where Karl-Dieter posted a patch.

Shall we close this ticket as duplicate?



---

archive/issue_comments_050467.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2013-12-25T13:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6334#issuecomment-50467",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_050468.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2013-12-25T13:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6334#issuecomment-50468",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_events_006579.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-01-04T04:23:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6334#event-6579"
}
```



---

archive/issue_comments_050469.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-01-04T04:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6334",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6334#issuecomment-50469",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate
