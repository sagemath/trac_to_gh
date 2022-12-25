# Issue 1469: sage-doctest should import the namespace of the file

archive/issues_001469.json:
```json
{
    "body": "Assignee: @burcin\n\nThe doctest script sage-doctest should try to import the namespace of the file being tested. It is not very convenient to add\n\n\n```\nfrom sage.foo import bar\n```\n\n\nat the beginning of every doctest in a file.\n\nThis would simplify some of the doctests in ~100 files, removing ~450 lines.\n\nImporting the module might have an impact on the speed of the doctests. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1469\n\n",
    "created_at": "2007-12-12T08:56:24Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "sage-doctest should import the namespace of the file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1469",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

The doctest script sage-doctest should try to import the namespace of the file being tested. It is not very convenient to add


```
from sage.foo import bar
```


at the beginning of every doctest in a file.

This would simplify some of the doctests in ~100 files, removing ~450 lines.

Importing the module might have an impact on the speed of the doctests. 

Issue created by migration from https://trac.sagemath.org/ticket/1469





---

archive/issue_comments_009424.json:
```json
{
    "body": "\n```\n<craigcitro> let's say the user types foo?\n<craigcitro> and gets the docstring for some function\n<craigcitro> then since they don't see this import that you've added\n<craigcitro> they can't actually run those doctests\n<craigcitro> they have to modify them by adding the sage.path.to.file at the beginning\n<craigcitro> which would be confusing if you've never run into it before\n```\n",
    "created_at": "2007-12-12T12:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1469#issuecomment-9424",
    "user": "https://github.com/burcin"
}
```


```
<craigcitro> let's say the user types foo?
<craigcitro> and gets the docstring for some function
<craigcitro> then since they don't see this import that you've added
<craigcitro> they can't actually run those doctests
<craigcitro> they have to modify them by adding the sage.path.to.file at the beginning
<craigcitro> which would be confusing if you've never run into it before
```




---

archive/issue_comments_009425.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2007-12-12T12:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1469#issuecomment-9425",
    "user": "https://github.com/burcin"
}
```

Resolution: wontfix



---

archive/issue_events_003739.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2007-12-12T12:17:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1469",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1469#event-3739"
}
```
