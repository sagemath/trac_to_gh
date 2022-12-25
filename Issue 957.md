# Issue 957: scipy is misbuilt on os x

archive/issues_000957.json:
```json
{
    "body": "Assignee: @williamstein\n\nImporting linsolve breaks on os x right now (I've removed the test\nthat exposes this for sage-2.8.8, but want this fixed. \n\n\n```\nbsd0:~/s was$   sage -t  devel/sage-main/sage/numerical/test.py\nsage -t  devel/sage-main/sage/numerical/test.py             **********************************************************************\nFile \"test.py\", line 9:\n    : from scipy import linsolve\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[5]>\", line 1, in <module>\n        from scipy import linsolve###line 9:\n    : from scipy import linsolve\n      File \"/Users/was/s/local/lib/python2.5/site-packages/scipy/linsolve/__init__.py\", line 5, in <module>\n        import umfpack\n      File \"/Users/was/s/local/lib/python2.5/site-packages/scipy/linsolve/umfpack/__init__.py\", line 3, in <module>\n        from umfpack import *\n      File \"/Users/was/s/local/lib/python2.5/site-packages/scipy/linsolve/umfpack/umfpack.py\", line 11, in <module>\n        import scipy.sparse as sp\n      File \"/Users/was/s/local/lib/python2.5/site-packages/scipy/sparse/__init__.py\", line 5, in <module>\n        from sparse import *\n      File \"/Users/was/s/local/lib/python2.5/site-packages/scipy/sparse/sparse.py\", line 14, in <module>\n        from scipy.sparse.sparsetools import cscmux, csrmux, \\\n    ImportError: cannot import name cscmux\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/957\n\n",
    "created_at": "2007-10-21T05:57:34Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "scipy is misbuilt on os x",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/957",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Importing linsolve breaks on os x right now (I've removed the test
that exposes this for sage-2.8.8, but want this fixed. 


```
bsd0:~/s was$   sage -t  devel/sage-main/sage/numerical/test.py
sage -t  devel/sage-main/sage/numerical/test.py             **********************************************************************
File "test.py", line 9:
    : from scipy import linsolve
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        from scipy import linsolve###line 9:
    : from scipy import linsolve
      File "/Users/was/s/local/lib/python2.5/site-packages/scipy/linsolve/__init__.py", line 5, in <module>
        import umfpack
      File "/Users/was/s/local/lib/python2.5/site-packages/scipy/linsolve/umfpack/__init__.py", line 3, in <module>
        from umfpack import *
      File "/Users/was/s/local/lib/python2.5/site-packages/scipy/linsolve/umfpack/umfpack.py", line 11, in <module>
        import scipy.sparse as sp
      File "/Users/was/s/local/lib/python2.5/site-packages/scipy/sparse/__init__.py", line 5, in <module>
        from sparse import *
      File "/Users/was/s/local/lib/python2.5/site-packages/scipy/sparse/sparse.py", line 14, in <module>
        from scipy.sparse.sparsetools import cscmux, csrmux, \
    ImportError: cannot import name cscmux
```


Issue created by migration from https://trac.sagemath.org/ticket/957





---

archive/issue_comments_005817.json:
```json
{
    "body": "From Josh:\n\n```\nThats odd, I have a sage-2.8.2 on OSX where all the commands in\nnumerical/test.py work fine.\n\nDid something change in the scipy package to make it use umfpack for\nsparse stuff. By default it uses superlu, but it can use umfpack.\n\nOnly think I can think of at the moment, did the order of scipy and cvxopt\nchange, cvxopt builds umfpack, but scipy was building before cvxopt so\nwasn't using cvxopt's umfpack.\n```\n",
    "created_at": "2007-10-21T12:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/957#issuecomment-5817",
    "user": "https://github.com/williamstein"
}
```

From Josh:

```
Thats odd, I have a sage-2.8.2 on OSX where all the commands in
numerical/test.py work fine.

Did something change in the scipy package to make it use umfpack for
sparse stuff. By default it uses superlu, but it can use umfpack.

Only think I can think of at the moment, did the order of scipy and cvxopt
change, cvxopt builds umfpack, but scipy was building before cvxopt so
wasn't using cvxopt's umfpack.
```




---

archive/issue_comments_005818.json:
```json
{
    "body": "What is the current status of this?\n\nCheers,\n\nMichael",
    "created_at": "2007-11-03T12:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/957#issuecomment-5818",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What is the current status of this?

Cheers,

Michael



---

archive/issue_comments_005819.json:
```json
{
    "body": "On a fresh install based on 2.8.13.rc1, I cannot duplicate this bug. Since I never could, could someone else using OSX verify that \n\nfrom scipy import linsolve \nfrom scipy import sparse \n\ndo not raise exceptions so we can close this bug.",
    "created_at": "2007-11-21T02:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/957#issuecomment-5819",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

On a fresh install based on 2.8.13.rc1, I cannot duplicate this bug. Since I never could, could someone else using OSX verify that 

from scipy import linsolve 
from scipy import sparse 

do not raise exceptions so we can close this bug.



---

archive/issue_comments_005820.json:
```json
{
    "body": "it also work for me with 2.8.13.rc2 on a G4 on 10.4, so close this.",
    "created_at": "2007-11-22T23:23:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/957#issuecomment-5820",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

it also work for me with 2.8.13.rc2 on a G4 on 10.4, so close this.



---

archive/issue_events_001079.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-11-22T23:23:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/957",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/957#event-1079"
}
```



---

archive/issue_comments_005821.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-22T23:23:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/957#issuecomment-5821",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
