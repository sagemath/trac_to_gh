# Issue 7924: Notebook trims trailing underscores from output.

archive/issues_007924.json:
```json
{
    "body": "Assignee: @williamstein\n\nTry\n\n```\nprint \"___x___\"\n```\n\nIn a notebook cell. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7924\n\n",
    "closed_at": "2010-01-19T03:15:53Z",
    "created_at": "2010-01-14T04:16:48Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Notebook trims trailing underscores from output.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7924",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

Try

```
print "___x___"
```

In a notebook cell. 

Issue created by migration from https://trac.sagemath.org/ticket/7924





---

archive/issue_comments_068851.json:
```json
{
    "body": "More data:\n\n```python\nsage: from sagenb.interfaces.expect import WorksheetProcess_ExpectImplementation \nsage: wp = WorksheetProcess_ExpectImplementation() \nsage: wp.execute('print \"___x___\"')\nsage: wp.output_status()\nOutput Status:\n        output: '___x'\n        filenames: []\n        done: True\n```",
    "created_at": "2010-01-15T22:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68851",
    "user": "https://github.com/qed777"
}
```

More data:

```python
sage: from sagenb.interfaces.expect import WorksheetProcess_ExpectImplementation 
sage: wp = WorksheetProcess_ExpectImplementation() 
sage: wp.execute('print "___x___"')
sage: wp.output_status()
Output Status:
        output: '___x'
        filenames: []
        done: True
```



---

archive/issue_comments_068852.json:
```json
{
    "body": "[str.rstrip](http://docs.python.org/library/stdtypes.html#str.rstrip)",
    "created_at": "2010-01-15T22:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68852",
    "user": "https://github.com/qed777"
}
```

[str.rstrip](http://docs.python.org/library/stdtypes.html#str.rstrip)



---

archive/issue_comments_068853.json:
```json
{
    "body": "This may be a duplicate of #7663.",
    "created_at": "2010-01-15T22:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68853",
    "user": "https://github.com/qed777"
}
```

This may be a duplicate of #7663.



---

archive/issue_comments_068854.json:
```json
{
    "body": "The patch at #7663 should fix this.  If it does and that ticket merges, please close this one.",
    "created_at": "2010-01-15T23:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68854",
    "user": "https://github.com/qed777"
}
```

The patch at #7663 should fix this.  If it does and that ticket merges, please close this one.



---

archive/issue_comments_068855.json:
```json
{
    "body": "Works with sagenb-0.6.",
    "created_at": "2010-01-19T03:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68855",
    "user": "https://github.com/TimDumol"
}
```

Works with sagenb-0.6.



---

archive/issue_events_018984.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:15:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7924#event-18984"
}
```



---

archive/issue_comments_068856.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T03:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68856",
    "user": "https://github.com/TimDumol"
}
```

Resolution: duplicate



---

archive/issue_events_018985.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:15:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7924#event-18985"
}
```
