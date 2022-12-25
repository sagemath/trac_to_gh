# Issue 9636: Catch output from PARI in Sage

archive/issues_009636.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @nexttime @robertwb\n\nThe output from print() functions in libpari is directly written to stdout and is not caught by Sage.  For example, the following doctest fails:\n\n```\ndef printhello():\n    \"\"\"\n    sage: printhello()\n    hello\n    \"\"\"\n    pari('print(\"hello\")')\n```\n\nIt gives\n\n```\nFile \"/home/jdemeyer/paritest.sage\", line 3:\n    sage: printhello()\nExpected:\n    hello\nGot nothing\n```\n\n\nLuckily, libpari provides ways to redirect the output.  There should a small Cython wrapper to direct the PARI output to sys.stdout.write().\n\nI will try to implement this (using #9343 as starting point). -- Jeroen Demeyer\n\nIssue created by migration from https://trac.sagemath.org/ticket/9636\n\n",
    "created_at": "2010-07-29T07:56:00Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Catch output from PARI in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9636",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: @williamstein

CC:  @nexttime @robertwb

The output from print() functions in libpari is directly written to stdout and is not caught by Sage.  For example, the following doctest fails:

```
def printhello():
    """
    sage: printhello()
    hello
    """
    pari('print("hello")')
```

It gives

```
File "/home/jdemeyer/paritest.sage", line 3:
    sage: printhello()
Expected:
    hello
Got nothing
```


Luckily, libpari provides ways to redirect the output.  There should a small Cython wrapper to direct the PARI output to sys.stdout.write().

I will try to implement this (using #9343 as starting point). -- Jeroen Demeyer

Issue created by migration from https://trac.sagemath.org/ticket/9636





---

archive/issue_comments_093256.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-14T20:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9636#issuecomment-93256",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093257.json:
```json
{
    "body": "Attachment [9636.patch](tarball://root/attachments/some-uuid/ticket9636/9636.patch) by @nexttime created at 2010-09-07 11:18:23\n\n\n```\ncdef extern: \n    PariOUT defaultOut \n    PariOUT defaultErr \n\n```\n\nshould perhaps migrate to `sage/libs/pari/decl.pxi`, too.\n\n**Positive review** from me though. Robert, anything to complain about?\n\n----\n\nI wonder when Cython will support `const`...",
    "created_at": "2010-09-07T11:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9636#issuecomment-93257",
    "user": "https://github.com/nexttime"
}
```

Attachment [9636.patch](tarball://root/attachments/some-uuid/ticket9636/9636.patch) by @nexttime created at 2010-09-07 11:18:23


```
cdef extern: 
    PariOUT defaultOut 
    PariOUT defaultErr 

```

should perhaps migrate to `sage/libs/pari/decl.pxi`, too.

**Positive review** from me though. Robert, anything to complain about?

----

I wonder when Cython will support `const`...



---

archive/issue_comments_093258.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-07T11:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9636#issuecomment-93258",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009775.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-10T10:44:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9636",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9636#event-9775"
}
```



---

archive/issue_comments_093259.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-10T10:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9636#issuecomment-93259",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
