# Issue 4114: [with patch, needs review] hang in lisp.py on OS X 10.5

archive/issues_004114.json:
```json
{
    "body": "Assignee: was\n\n\n```\nOne *major* issue that remains is that the lisp.py doctest hangs forever\non OS X ppc 10.5:\n\nsage -t -long devel/sage/sage/interfaces/lie.py\n        [5.5 s]\nsage -t -long devel/sage/sage/interfaces/lisp.py\n\n^Z [[10 hours later!]]\n[1]+  Stopped                 ./bb\nclement-pernets-imac-g5:~ was$\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4114\n\n",
    "created_at": "2008-09-14T06:45:11Z",
    "labels": [
        "interfaces",
        "blocker",
        "bug"
    ],
    "title": "[with patch, needs review] hang in lisp.py on OS X 10.5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4114",
    "user": "mhansen"
}
```
Assignee: was


```
One *major* issue that remains is that the lisp.py doctest hangs forever
on OS X ppc 10.5:

sage -t -long devel/sage/sage/interfaces/lie.py
        [5.5 s]
sage -t -long devel/sage/sage/interfaces/lisp.py

^Z [[10 hours later!]]
[1]+  Stopped                 ./bb
clement-pernets-imac-g5:~ was$
```


Issue created by migration from https://trac.sagemath.org/ticket/4114





---

archive/issue_comments_029789.json:
```json
{
    "body": "Attachment\n\nOn an OSX 10.4 PPC box this patch fixes the issue:\n\n```\nvarro:~/sage-3.1.2.rc2 mabshoff$ ./sage -t devel/sage/sage/interfaces/lisp.py\nsage -t  devel/sage/sage/interfaces/lisp.py                 \n         [19.8 s]\n \n----------------------------------------------------------------------\nAll tests passed!\n```\n\nBut I am mystified why it did work on OSX Intel boxen. \n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T07:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4114#issuecomment-29789",
    "user": "mabshoff"
}
```

Attachment

On an OSX 10.4 PPC box this patch fixes the issue:

```
varro:~/sage-3.1.2.rc2 mabshoff$ ./sage -t devel/sage/sage/interfaces/lisp.py
sage -t  devel/sage/sage/interfaces/lisp.py                 
         [19.8 s]
 
----------------------------------------------------------------------
All tests passed!
```

But I am mystified why it did work on OSX Intel boxen. 

Cheers,

Michael



---

archive/issue_comments_029790.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc3",
    "created_at": "2008-09-14T09:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4114#issuecomment-29790",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc3



---

archive/issue_comments_029791.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-14T09:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4114#issuecomment-29791",
    "user": "mabshoff"
}
```

Resolution: fixed
