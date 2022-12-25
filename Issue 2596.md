# Issue 2596: Sage 2.11.alpha0: sage/plot/plot.py doctest failure

archive/issues_002596.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nsage -t -long devel/sage/sage/plot/plot.py\n----------------------------------------------------------------------\nTotal time for all tests: 965.6 seconds\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha0$ ./sage -t -long devel/sage/sage/plot/plot.py\nsage -t -long devel/sage-main/sage/plot/plot.py\n**********************************************************************\nFile \"plot.py\", line 3860:\n    sage: networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=0)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_118[17]>\", line 1, in <module>\n        networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=Integer(0))###line 3860:\n    sage: networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=0)\n    AttributeError: 'Graph' object has no attribute '_nxg'\n**********************************************************************\n1 items had failures:\n   1 of  18 in __main__.example_118\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_plot.py\n         [68.5 s]\nexit code: 256\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2596\n\n",
    "created_at": "2008-03-19T13:31:01Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Sage 2.11.alpha0: sage/plot/plot.py doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2596",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_events_002785.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-22T22:19:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2596#event-2785"
}
```



---

archive/issue_comments_017721.json:
```json
{
    "body": "Mmh, somehow I opened the same ticket twice. This is a dupe of #2583.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T22:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17721",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mmh, somehow I opened the same ticket twice. This is a dupe of #2583.

Cheers,

Michael



---

archive/issue_comments_017722.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-22T22:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17722",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_017723.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2008-03-22T22:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17723",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_017724.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-22T22:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17724",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_002786.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-22T22:27:52Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2596#event-2786"
}
```



---

archive/issue_comments_017725.json:
```json
{
    "body": "Ooops, I ended up pasting the wrong doctest failure into the description. Since it now has the corrected version I am reopening this.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T22:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17725",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ooops, I ended up pasting the wrong doctest failure into the description. Since it now has the corrected version I am reopening this.

Cheers,

Michael



---

archive/issue_comments_017726.json:
```json
{
    "body": "The returned output is correct, so it should be included in the doctest.\n\n\"99 points\" should be replaced with \"...\", I think, since sometimes it will be \"100 points\" (due to random shifts in the points).  We could just set randomize=False, but that would make for a more confusing example, I think.",
    "created_at": "2008-03-24T14:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17726",
    "user": "https://github.com/jasongrout"
}
```

The returned output is correct, so it should be included in the doctest.

"99 points" should be replaced with "...", I think, since sometimes it will be "100 points" (due to random shifts in the points).  We could just set randomize=False, but that would make for a more confusing example, I think.



---

archive/issue_comments_017727.json:
```json
{
    "body": "Attachment [sage-2596.patch](tarball://root/attachments/some-uuid/ticket2596/sage-2596.patch) by @williamstein created at 2008-03-28 05:17:44",
    "created_at": "2008-03-28T05:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17727",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2596.patch](tarball://root/attachments/some-uuid/ticket2596/sage-2596.patch) by @williamstein created at 2008-03-28 05:17:44



---

archive/issue_comments_017728.json:
```json
{
    "body": "Patch looks good to me. Positive review.",
    "created_at": "2008-03-28T07:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17728",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. Positive review.



---

archive/issue_events_002787.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-28T07:25:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2596#event-2787"
}
```



---

archive/issue_comments_017729.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T07:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17729",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017730.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-28T07:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2596#issuecomment-17730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha2
