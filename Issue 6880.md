# Issue 6880: docstrings and @cached_method -- if you used cached_method then docstring displays wrong file, etc.

archive/issues_006880.json:
```json
{
    "body": "Assignee: tba\n\nIf you used the ``@`cached_method` decorator when defining a function in the Sage library, then get help about it (either in the notebook or command line), the File: field lis as follows:\n\n\n```\nFile:           /.../local/lib/python2.6/site-packages/sage/misc/cachefunc.py\n```\n\n\nThat's of course technically right, but very wrong/misleading for the user, who maybe wants to know more.  We should add specialized code to IPython and the notebook to correct for this. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6880\n\n",
    "created_at": "2009-09-03T17:22:16Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "docstrings and @cached_method -- if you used cached_method then docstring displays wrong file, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6880",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba

If you used the ``@`cached_method` decorator when defining a function in the Sage library, then get help about it (either in the notebook or command line), the File: field lis as follows:


```
File:           /.../local/lib/python2.6/site-packages/sage/misc/cachefunc.py
```


That's of course technically right, but very wrong/misleading for the user, who maybe wants to know more.  We should add specialized code to IPython and the notebook to correct for this. 

Issue created by migration from https://trac.sagemath.org/ticket/6880





---

archive/issue_comments_056684.json:
```json
{
    "body": "This problem has already been fixed (by some work in sage.misc.sageinspect - sorry, I am too lazy to look up the ticket number). For example:\n\n```\nsage: P.<x,y> = QQ[]\nsage: I = P*[x,y]\nsage: I.groebner_basis?\nType:           CachedMethodCaller\nBase Class:     <type 'sage.misc.cachefunc.CachedMethodCaller'>\nString Form:    Cached version of <function groebner_basis at 0x1507b18>\nNamespace:      Interactive\nLoaded File:    /home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/misc/cachefunc.so\nSource File:    /home/simon/SAGE/sage-5.0/devel/sage/sage/misc/cachefunc.so\nDefinition:     I.groebner_basis(self, algorithm='', deg_bound=None, mult_bound=None, prot=False, *args, **kwds)\nDocstring:\n    File: sage/rings/polynomial/multi_polynomial_ideal.py (starting at line 3476)\n...\n```\n\n\nHence, we can close this.",
    "created_at": "2012-06-25T09:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6880#issuecomment-56684",
    "user": "https://github.com/simon-king-jena"
}
```

This problem has already been fixed (by some work in sage.misc.sageinspect - sorry, I am too lazy to look up the ticket number). For example:

```
sage: P.<x,y> = QQ[]
sage: I = P*[x,y]
sage: I.groebner_basis?
Type:           CachedMethodCaller
Base Class:     <type 'sage.misc.cachefunc.CachedMethodCaller'>
String Form:    Cached version of <function groebner_basis at 0x1507b18>
Namespace:      Interactive
Loaded File:    /home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/misc/cachefunc.so
Source File:    /home/simon/SAGE/sage-5.0/devel/sage/sage/misc/cachefunc.so
Definition:     I.groebner_basis(self, algorithm='', deg_bound=None, mult_bound=None, prot=False, *args, **kwds)
Docstring:
    File: sage/rings/polynomial/multi_polynomial_ideal.py (starting at line 3476)
...
```


Hence, we can close this.



---

archive/issue_comments_056685.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-25T09:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6880#issuecomment-56685",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056686.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-25T09:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6880#issuecomment-56686",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_016178.json:
```json
{
    "actor": "https://github.com/simon-king-jena",
    "created_at": "2012-06-25T09:09:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6880",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6880#event-16178"
}
```



---

archive/issue_events_016179.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-07-04T07:17:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6880",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6880#event-16179"
}
```



---

archive/issue_comments_056687.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-07-04T07:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6880#issuecomment-56687",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
