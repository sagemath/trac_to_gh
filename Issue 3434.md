# Issue 3434: notebook -- implementin MAX_OUTPUT handling in cell.py for interact.

archive/issues_003434.json:
```json
{
    "body": "Assignee: boothby\n\nTry this in the notebook\n\n```\n@interact\ndef test(a=1):\n    print 2^a\n```\n\n\nFor large a it outputs something massive and very very bad. This should not be aloud. \n\nTo fix this:\n\n1. Look at\n\n```\n            self.interact = input[len('%__sage_interact__')+1]\n```\n\nin cell.py\n2. Factor out this code from cell.py:\n\n```\n        if 'notruncate' not in output and 'Output truncated!' not in output and \\\n              (len(output) > MAX_OUTPUT or output.count('\\n') > MAX_OUTPUT_LINES) and \\\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3434\n\n",
    "created_at": "2008-06-15T23:11:35Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "notebook -- implementin MAX_OUTPUT handling in cell.py for interact.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3434",
    "user": "@williamstein"
}
```
Assignee: boothby

Try this in the notebook

```
@interact
def test(a=1):
    print 2^a
```


For large a it outputs something massive and very very bad. This should not be aloud. 

To fix this:

1. Look at

```
            self.interact = input[len('%__sage_interact__')+1]
```

in cell.py
2. Factor out this code from cell.py:

```
        if 'notruncate' not in output and 'Output truncated!' not in output and \
              (len(output) > MAX_OUTPUT or output.count('\n') > MAX_OUTPUT_LINES) and \
```


Issue created by migration from https://trac.sagemath.org/ticket/3434





---

archive/issue_comments_024201.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3434#issuecomment-24201",
    "user": "@aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_024202.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3434#issuecomment-24202",
    "user": "boothby"
}
```

Closing deprecated notebook tickets



---

archive/issue_comments_024203.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3434#issuecomment-24203",
    "user": "boothby"
}
```

Resolution: invalid
