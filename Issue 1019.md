# Issue 1019: strange behavious in notebook with %octave

archive/issues_001019.json:
```json
{
    "body": "Assignee: boothby\n\nThe following was reported by David Galant:\n\n```\nIn the notebook, starting a block with '%octave' does not produce a\nresult.\nThis has been consistent throughout all releases of sage 2.*\nThe behavior is consistent on MacOS and Ubuntu Linux.\nA sample session showing this is:\n \nsage: from math import *\nsage: sin(1)\n0.8414709848078965\nsage: gp.sin(1)\n0.8414709848078965066525023216\nsage: octave.sin(1)\n0.841471\nsage: %gp\nsage: sin(1)\n0.8414709848078965066525023216\nsage: %octave\nsage: sin(1)\n \nsage: 3+2\n5\nsage: quit\nExited sage process\n```\n\n\nSee\n\nIssue created by migration from https://trac.sagemath.org/ticket/1019\n\n",
    "created_at": "2007-10-28T09:41:32Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "strange behavious in notebook with %octave",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1019",
    "user": "mabshoff"
}
```
Assignee: boothby

The following was reported by David Galant:

```
In the notebook, starting a block with '%octave' does not produce a
result.
This has been consistent throughout all releases of sage 2.*
The behavior is consistent on MacOS and Ubuntu Linux.
A sample session showing this is:
 
sage: from math import *
sage: sin(1)
0.8414709848078965
sage: gp.sin(1)
0.8414709848078965066525023216
sage: octave.sin(1)
0.841471
sage: %gp
sage: sin(1)
0.8414709848078965066525023216
sage: %octave
sage: sin(1)
 
sage: 3+2
5
sage: quit
Exited sage process
```


See

Issue created by migration from https://trac.sagemath.org/ticket/1019





---

archive/issue_comments_006246.json:
```json
{
    "body": "This is still an issue with 2.10.1 and when I now switch the Sage notebook at sagenb into octave mode it seems like only every second cell is evaluated.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T22:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1019#issuecomment-6246",
    "user": "mabshoff"
}
```

This is still an issue with 2.10.1 and when I now switch the Sage notebook at sagenb into octave mode it seems like only every second cell is evaluated.

Cheers,

Michael



---

archive/issue_comments_006247.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-02-15T22:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1019#issuecomment-6247",
    "user": "mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_006248.json:
```json
{
    "body": "Changing assignee from boothby to @williamstein.",
    "created_at": "2008-03-05T07:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1019#issuecomment-6248",
    "user": "boothby"
}
```

Changing assignee from boothby to @williamstein.



---

archive/issue_comments_006249.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-09-03T00:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1019#issuecomment-6249",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_006250.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-03T00:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1019#issuecomment-6250",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006251.json:
```json
{
    "body": "Attachment [trac_1019.patch](tarball://root/attachments/some-uuid/ticket1019/trac_1019.patch) by @mwhansen created at 2009-01-22 09:19:40",
    "created_at": "2009-01-22T09:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1019#issuecomment-6251",
    "user": "@mwhansen"
}
```

Attachment [trac_1019.patch](tarball://root/attachments/some-uuid/ticket1019/trac_1019.patch) by @mwhansen created at 2009-01-22 09:19:40



---

archive/issue_comments_006252.json:
```json
{
    "body": "It turns out that this is caused by the chdir command (which is run before each cell is evaluated) screwing up the syncronization.\n\nThis can also be fixed by improving the Octave interface to have better error detection.",
    "created_at": "2009-01-22T09:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1019#issuecomment-6252",
    "user": "@mwhansen"
}
```

It turns out that this is caused by the chdir command (which is run before each cell is evaluated) screwing up the syncronization.

This can also be fixed by improving the Octave interface to have better error detection.



---

archive/issue_comments_006253.json:
```json
{
    "body": "This works for me.  Mike explained the patch and it sounds reasonable.  Positive Review.",
    "created_at": "2009-01-22T17:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1019#issuecomment-6253",
    "user": "@jasongrout"
}
```

This works for me.  Mike explained the patch and it sounds reasonable.  Positive Review.



---

archive/issue_comments_006254.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T08:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1019#issuecomment-6254",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_006255.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1019#issuecomment-6255",
    "user": "mabshoff"
}
```

Resolution: fixed
