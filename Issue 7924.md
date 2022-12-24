# Issue 7924: Notebook trims trailing underscores from output.

archive/issues_007924.json:
```json
{
    "body": "Assignee: was\n\nTry\n\n\n```\nprint \"___x___\"\n```\n\n\nIn a notebook cell. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7924\n\n",
    "created_at": "2010-01-14T04:16:48Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Notebook trims trailing underscores from output.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7924",
    "user": "robertwb"
}
```
Assignee: was

Try


```
print "___x___"
```


In a notebook cell. 

Issue created by migration from https://trac.sagemath.org/ticket/7924





---

archive/issue_comments_068970.json:
```json
{
    "body": "More data:\n\n```python\nsage: from sagenb.interfaces.expect import WorksheetProcess_ExpectImplementation \nsage: wp = WorksheetProcess_ExpectImplementation() \nsage: wp.execute('print \"___x___\"')\nsage: wp.output_status()\nOutput Status:\n        output: '___x'\n        filenames: []\n        done: True\n```\n",
    "created_at": "2010-01-15T22:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68970",
    "user": "mpatel"
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

archive/issue_comments_068971.json:
```json
{
    "body": "[str.rstrip](http://docs.python.org/library/stdtypes.html#str.rstrip)",
    "created_at": "2010-01-15T22:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68971",
    "user": "mpatel"
}
```

[str.rstrip](http://docs.python.org/library/stdtypes.html#str.rstrip)



---

archive/issue_comments_068972.json:
```json
{
    "body": "This may be a duplicate of #7663.",
    "created_at": "2010-01-15T22:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68972",
    "user": "mpatel"
}
```

This may be a duplicate of #7663.



---

archive/issue_comments_068973.json:
```json
{
    "body": "The patch at #7663 should fix this.  If it does and that ticket merges, please close this one.",
    "created_at": "2010-01-15T23:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68973",
    "user": "mpatel"
}
```

The patch at #7663 should fix this.  If it does and that ticket merges, please close this one.



---

archive/issue_comments_068974.json:
```json
{
    "body": "Works with sagenb-0.6.",
    "created_at": "2010-01-19T03:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68974",
    "user": "timdumol"
}
```

Works with sagenb-0.6.



---

archive/issue_comments_068975.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T03:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7924#issuecomment-68975",
    "user": "timdumol"
}
```

Resolution: duplicate
