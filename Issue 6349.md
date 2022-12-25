# Issue 6349: graphs -- bug in DiGraph constructor

archive/issues_006349.json:
```json
{
    "body": "Assignee: @rlmill\n\n\n```\nsage: DiGraph(matrix(2,[0,0,-1,1]), format=\"incidence_matrix\")\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/Users/wstein/.sage/sage_notebook/worksheets/admin/187/code/29.py\", line 7, in <module>\n    DiGraph(matrix(_sage_const_2 ,[_sage_const_0 ,_sage_const_0 ,-_sage_const_1 ,_sage_const_1 ]), format=\"incidence_matrix\")\n  File \"/Users/wstein/s/local/lib/python2.5/site-packages/Jinja-1.2-py2.5-macosx-10.3-i386.egg/\", line 1, in <module>\n    \n  File \"/Users/wstein/s/local/lib/python2.5/site-packages/sage/graphs/graph.py\", line 9894, in __init__\n    raise ValueError(msg + msg2)\nTypeError: cannot concatenate 'str' and 'exceptions.AssertionError' objects\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6349\n\n",
    "created_at": "2009-06-17T22:27:52Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "graphs -- bug in DiGraph constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6349",
    "user": "https://github.com/williamstein"
}
```
Assignee: @rlmill


```
sage: DiGraph(matrix(2,[0,0,-1,1]), format="incidence_matrix")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/wstein/.sage/sage_notebook/worksheets/admin/187/code/29.py", line 7, in <module>
    DiGraph(matrix(_sage_const_2 ,[_sage_const_0 ,_sage_const_0 ,-_sage_const_1 ,_sage_const_1 ]), format="incidence_matrix")
  File "/Users/wstein/s/local/lib/python2.5/site-packages/Jinja-1.2-py2.5-macosx-10.3-i386.egg/", line 1, in <module>
    
  File "/Users/wstein/s/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 9894, in __init__
    raise ValueError(msg + msg2)
TypeError: cannot concatenate 'str' and 'exceptions.AssertionError' objects
```



Issue created by migration from https://trac.sagemath.org/ticket/6349





---

archive/issue_comments_050678.json:
```json
{
    "body": "Attachment [trac_6349.patch](tarball://root/attachments/some-uuid/ticket6349/trac_6349.patch) by @rlmill created at 2009-06-17 22:53:36",
    "created_at": "2009-06-17T22:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6349#issuecomment-50678",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6349.patch](tarball://root/attachments/some-uuid/ticket6349/trac_6349.patch) by @rlmill created at 2009-06-17 22:53:36



---

archive/issue_comments_050679.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-17T22:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6349#issuecomment-50679",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050680.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6349#issuecomment-50680",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_014940.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-24T10:11:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6349",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6349#event-14940"
}
```
