# Issue 3168: Source introspection does not work for outside Cython extensions

archive/issues_003168.json:
```json
{
    "body": "Assignee: cwitty\n\nIf you take a simple Cython extension module and install it in into SAGE via\n\n```\nsage -python setup.py install\n```\n\nsource introspection will not work.   \n\nThis appears to caused by two things\n\n1) cython is invoked without the \"-p\" option\n\n2) the relevant *pyx files are not put somewhere that the Sage interpreter can find them.\n\nAttached is a minimal Cython module illustrating the problem.   Source introspection can be made to work via\n\n\n```\nsage -cython -p introtest.pyx\nsage -python setup.py install\ncp introtest.pyx $SAGEROOT/devel/sage/\n}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/3168\n\n",
    "created_at": "2008-05-12T19:34:17Z",
    "labels": [
        "misc",
        "trivial",
        "bug"
    ],
    "title": "Source introspection does not work for outside Cython extensions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3168",
    "user": "dunfield"
}
```
Assignee: cwitty

If you take a simple Cython extension module and install it in into SAGE via

```
sage -python setup.py install
```

source introspection will not work.   

This appears to caused by two things

1) cython is invoked without the "-p" option

2) the relevant *pyx files are not put somewhere that the Sage interpreter can find them.

Attached is a minimal Cython module illustrating the problem.   Source introspection can be made to work via


```
sage -cython -p introtest.pyx
sage -python setup.py install
cp introtest.pyx $SAGEROOT/devel/sage/
}}

Issue created by migration from https://trac.sagemath.org/ticket/3168





---

archive/issue_comments_021954.json:
```json
{
    "body": "Attachment\n\nMinimal example",
    "created_at": "2008-05-12T19:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3168#issuecomment-21954",
    "user": "dunfield"
}
```

Attachment

Minimal example



---

archive/issue_comments_021955.json:
```json
{
    "body": "Minimal example",
    "created_at": "2008-05-12T19:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3168#issuecomment-21955",
    "user": "dunfield"
}
```

Minimal example



---

archive/issue_comments_021956.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-12T19:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3168#issuecomment-21956",
    "user": "dunfield"
}
```

Attachment



---

archive/issue_comments_021957.json:
```json
{
    "body": "Changing priority from trivial to minor.",
    "created_at": "2008-05-12T19:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3168#issuecomment-21957",
    "user": "dunfield"
}
```

Changing priority from trivial to minor.



---

archive/issue_comments_021958.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:46:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3168#issuecomment-21958",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.
