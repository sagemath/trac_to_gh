# Issue 1499: fix import issues related to ATLAS BLAS

archive/issues_001499.json:
```json
{
    "body": "Assignee: mabshoff\n\nAt least on sage.math Sage fails to start up when doing import all. The following doctest failure illustrates the problem:\n\n```\nmabshoff@sage:/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7$ ./sage -t  devel/sage-main/sage/numerical/test.py\nsage -t  devel/sage-main/sage/numerical/test.py             Traceback (most recent call last):\n  File \".doctest_test.py\", line 1, in <module>\n    from sage.all_cmdline import *;\n  File \"/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7/local/lib/python2.5/site-packages/sage/all_cmdline.py\", line 1\n4, in <module>\n    from sage.all import *\n  File \"/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7/local/lib/python2.5/site-packages/sage/all.py\", line 53, in <m\nodule>\n    from sage.misc.all       import *         # takes a while\n  File \"/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7/local/lib/python2.5/site-packages/sage/misc/all.py\", line 67,\nin <module>\n    from functional import (additive_order,\n  File \"/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7/local/lib/python2.5/site-packages/sage/misc/functional.py\", li\nne 33, in <module>\n    from sage.rings.complex_double import CDF\nImportError: /tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7/local/lib/libcblas.so: undefined symbol: ATL_ctbmv\n\n         [0.3 s]\nexit code: 256\n```\n\nThe attached patch fixes that, but not in a very clean way. I tried various \"clean\" approaches, but non of them got past Cython and always lead to link errors.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1499\n\n",
    "created_at": "2007-12-14T00:01:46Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "fix import issues related to ATLAS BLAS",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1499",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

At least on sage.math Sage fails to start up when doing import all. The following doctest failure illustrates the problem:

```
mabshoff@sage:/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7$ ./sage -t  devel/sage-main/sage/numerical/test.py
sage -t  devel/sage-main/sage/numerical/test.py             Traceback (most recent call last):
  File ".doctest_test.py", line 1, in <module>
    from sage.all_cmdline import *;
  File "/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7/local/lib/python2.5/site-packages/sage/all_cmdline.py", line 1
4, in <module>
    from sage.all import *
  File "/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7/local/lib/python2.5/site-packages/sage/all.py", line 53, in <m
odule>
    from sage.misc.all       import *         # takes a while
  File "/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7/local/lib/python2.5/site-packages/sage/misc/all.py", line 67,
in <module>
    from functional import (additive_order,
  File "/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7/local/lib/python2.5/site-packages/sage/misc/functional.py", li
ne 33, in <module>
    from sage.rings.complex_double import CDF
ImportError: /tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha7/local/lib/libcblas.so: undefined symbol: ATL_ctbmv

         [0.3 s]
exit code: 256
```

The attached patch fixes that, but not in a very clean way. I tried various "clean" approaches, but non of them got past Cython and always lead to link errors.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1499





---

archive/issue_comments_009592.json:
```json
{
    "body": "Attachment [Sage-2.9.alpha7-fix-ATLAS-linking.patch](tarball://root/attachments/some-uuid/ticket1499/Sage-2.9.alpha7-fix-ATLAS-linking.patch) by mabshoff created at 2007-12-14 00:52:31\n\nThe patch passes a `sage -ba` and a `testall` on OSX 10.5\n\nCheers,\n\nMichael",
    "created_at": "2007-12-14T00:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1499#issuecomment-9592",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.9.alpha7-fix-ATLAS-linking.patch](tarball://root/attachments/some-uuid/ticket1499/Sage-2.9.alpha7-fix-ATLAS-linking.patch) by mabshoff created at 2007-12-14 00:52:31

The patch passes a `sage -ba` and a `testall` on OSX 10.5

Cheers,

Michael



---

archive/issue_comments_009593.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-14T02:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1499#issuecomment-9593",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003806.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-14T02:19:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1499",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1499#event-3806"
}
```



---

archive/issue_comments_009594.json:
```json
{
    "body": "Merged in 2.9.alpha7.",
    "created_at": "2007-12-14T02:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1499#issuecomment-9594",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha7.
