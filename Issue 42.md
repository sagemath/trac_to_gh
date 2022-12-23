# Issue 42: Calling GAP commands via gap("command") reacts badly sometimes

archive/issues_000042.json:
```json
{
    "body": "Assignee: somebody\n\n* (KiranKedlaya) Calling GAP commands via gap(\"command\") reacts badly when the command does not return a value, e.g., gap('Read(\"myfile.txt\")').\n\nIssue created by migration from https://trac.sagemath.org/ticket/42\n\n",
    "created_at": "2006-09-12T23:32:22Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Calling GAP commands via gap(\"command\") reacts badly sometimes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/42",
    "user": "was"
}
```
Assignee: somebody

* (KiranKedlaya) Calling GAP commands via gap("command") reacts badly when the command does not return a value, e.g., gap('Read("myfile.txt")').

Issue created by migration from https://trac.sagemath.org/ticket/42





---

archive/issue_comments_000261.json:
```json
{
    "body": "Do you mean gap.eval('Read(\"myfile.txt\")') is flaky? If so, can you give an example?",
    "created_at": "2006-09-24T19:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/42",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/42#issuecomment-261",
    "user": "wdj"
}
```

Do you mean gap.eval('Read("myfile.txt")') is flaky? If so, can you give an example?



---

archive/issue_comments_000262.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-12T22:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/42",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/42#issuecomment-262",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000263.json:
```json
{
    "body": "This is a misunderstanding about using gap(s) versus gap.eval(s).  This is not a bug.\ngap(s) is supposed to always create a new gap object.",
    "created_at": "2007-01-12T22:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/42",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/42#issuecomment-263",
    "user": "was"
}
```

This is a misunderstanding about using gap(s) versus gap.eval(s).  This is not a bug.
gap(s) is supposed to always create a new gap object.
