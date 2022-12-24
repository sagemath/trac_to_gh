# Issue 2596: Sage 2.11.alpha0: sage/plot/plot.py doctest failure

archive/issues_002596.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nsage -t -long devel/sage/sage/plot/plot.py\n----------------------------------------------------------------------\nTotal time for all tests: 965.6 seconds\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha0$ ./sage -t -long devel/sage/sage/plot/plot.py\nsage -t -long devel/sage-main/sage/plot/plot.py\n**********************************************************************\nFile \"plot.py\", line 3860:\n    sage: networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=0)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_118[17]>\", line 1, in <module>\n        networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=Integer(0))###line 3860:\n    sage: networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=0)\n    AttributeError: 'Graph' object has no attribute '_nxg'\n**********************************************************************\n1 items had failures:\n   1 of  18 in __main__.example_118\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_plot.py\n         [68.5 s]\nexit code: 256\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2596\n\n",
    "created_at": "2008-03-19T13:31:01Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Sage 2.11.alpha0: sage/plot/plot.py doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2596",
    "user": "mabshoff"
}
```
Assignee: failure


```
sage -t -long devel/sage/sage/plot/plot.py
----------------------------------------------------------------------
Total time for all tests: 965.6 seconds
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha0$ ./sage -t -long devel/sage/sage/plot/plot.py
sage -t -long devel/sage-main/sage/plot/plot.py
**********************************************************************
File "plot.py", line 3860:
    sage: networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=0)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_118[17]>", line 1, in <module>
        networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=Integer(0))###line 3860:
    sage: networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=0)
    AttributeError: 'Graph' object has no attribute '_nxg'
**********************************************************************
1 items had failures:
   1 of  18 in __main__.example_118
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_plot.py
         [68.5 s]
exit code: 256
```


Issue created by migration from https://trac.sagemath.org/ticket/2596





---

archive/issue_comments_017759.json:
```json
{
    "body": "Mmh, somehow I opened the same ticket twice. This is a dupe of #2583.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T22:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17759",
    "user": "mabshoff"
}
```

Mmh, somehow I opened the same ticket twice. This is a dupe of #2583.

Cheers,

Michael



---

archive/issue_comments_017760.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-22T22:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17760",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_017761.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2008-03-22T22:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17761",
    "user": "mabshoff"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_017762.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-22T22:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17762",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_017763.json:
```json
{
    "body": "Ooops, I ended up pasting the wrong doctest failure into the description. Since it now has the corrected version I am reopening this.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T22:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17763",
    "user": "mabshoff"
}
```

Ooops, I ended up pasting the wrong doctest failure into the description. Since it now has the corrected version I am reopening this.

Cheers,

Michael



---

archive/issue_comments_017764.json:
```json
{
    "body": "The returned output is correct, so it should be included in the doctest.\n\n\"99 points\" should be replaced with \"...\", I think, since sometimes it will be \"100 points\" (due to random shifts in the points).  We could just set randomize=False, but that would make for a more confusing example, I think.",
    "created_at": "2008-03-24T14:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17764",
    "user": "jason"
}
```

The returned output is correct, so it should be included in the doctest.

"99 points" should be replaced with "...", I think, since sometimes it will be "100 points" (due to random shifts in the points).  We could just set randomize=False, but that would make for a more confusing example, I think.



---

archive/issue_comments_017765.json:
```json
{
    "body": "Attachment [sage-2596.patch](tarball://root/attachments/some-uuid/ticket2596/sage-2596.patch) by was created at 2008-03-28 05:17:44",
    "created_at": "2008-03-28T05:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17765",
    "user": "was"
}
```

Attachment [sage-2596.patch](tarball://root/attachments/some-uuid/ticket2596/sage-2596.patch) by was created at 2008-03-28 05:17:44



---

archive/issue_comments_017766.json:
```json
{
    "body": "Patch looks good to me. Positive review.",
    "created_at": "2008-03-28T07:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17766",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review.



---

archive/issue_comments_017767.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T07:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17767",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017768.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-28T07:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17768",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2
