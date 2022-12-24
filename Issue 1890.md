# Issue 1890: Sage 2.10.1.alpha2: interfaces/libecm.pyx doctest failure

archive/issues_001890.json:
```json
{
    "body": "Assignee: rlm\n\nI get the following doctest failure on sage.math with 2.10.1.alpha1 plus the libecm patch applied:\n\n```\nsage -t  devel/sage-main/sage/interfaces/libecm.pyx\n**********************************************************************\nFile \"libecm.pyx\", line 18:\n    sage: ecmfactor(999, 0.00, verbose=True)\nExpected:\n    Performing one curve with B1=0\n    Found factor in step 1: 999\n    (True, 999)\nGot:\n    Performing one curve with B1=0\n    Found factor in step 1: 27\n    (True, 27)\n**********************************************************************\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1890\n\n",
    "created_at": "2008-01-23T10:55:01Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 2.10.1.alpha2: interfaces/libecm.pyx doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1890",
    "user": "mabshoff"
}
```
Assignee: rlm

I get the following doctest failure on sage.math with 2.10.1.alpha1 plus the libecm patch applied:

```
sage -t  devel/sage-main/sage/interfaces/libecm.pyx
**********************************************************************
File "libecm.pyx", line 18:
    sage: ecmfactor(999, 0.00, verbose=True)
Expected:
    Performing one curve with B1=0
    Found factor in step 1: 999
    (True, 999)
Got:
    Performing one curve with B1=0
    Found factor in step 1: 27
    (True, 27)
**********************************************************************
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1890





---

archive/issue_comments_011971.json:
```json
{
    "body": "Attachment [1890.patch](tarball://root/attachments/some-uuid/ticket1890/1890.patch) by rlm created at 2008-01-23 23:46:19",
    "created_at": "2008-01-23T23:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1890#issuecomment-11971",
    "user": "rlm"
}
```

Attachment [1890.patch](tarball://root/attachments/some-uuid/ticket1890/1890.patch) by rlm created at 2008-01-23 23:46:19



---

archive/issue_comments_011972.json:
```json
{
    "body": "The patch looks good? I looked at the url provided in the code for ecm and there wasn't really much there. I am also wondering why the output of ecmfactor varies on different platforms. I assume the algorithm depends on some kind of input from an entropy pool?\n\nCheers,\n\nMichael",
    "created_at": "2008-01-24T00:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1890#issuecomment-11972",
    "user": "mabshoff"
}
```

The patch looks good? I looked at the url provided in the code for ecm and there wasn't really much there. I am also wondering why the output of ecmfactor varies on different platforms. I assume the algorithm depends on some kind of input from an entropy pool?

Cheers,

Michael



---

archive/issue_comments_011973.json:
```json
{
    "body": "With positive review since Robert says:\n\n```\nMichael,\n\nIt is not platform dependent: it is not deterministic ;)\n```\n",
    "created_at": "2008-01-24T00:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1890#issuecomment-11973",
    "user": "mabshoff"
}
```

With positive review since Robert says:

```
Michael,

It is not platform dependent: it is not deterministic ;)
```




---

archive/issue_comments_011974.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-24T00:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1890#issuecomment-11974",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2



---

archive/issue_comments_011975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-24T00:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1890#issuecomment-11975",
    "user": "mabshoff"
}
```

Resolution: fixed
