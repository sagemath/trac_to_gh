# Issue 1485: wrapper for invariant_ring and invariant_algebra_reynolds in Singular

archive/issues_001485.json:
```json
{
    "body": "Assignee: @malb\n\nWraps Singular's invariant_algebra_reynolds and invariant_ring in finvar.lib, with help from Simon King and Martin Albrecht. Computes generators for the polynomial ring F[x1,...,xn]^G, where G in GL(n,F) is a finite matrix group.\n\nIn the \"good characteristic\" case the polynomials returned form a minimal generating set for the algebra of G-invariant polynomials. In the \"bad\" case, the polynomials returned are primary and secondary invariants, forming a not necessarily minimal generating set for the algebra of G-invariant polynomials.\n\nPatch is at\nhttp://sage.math.washington.edu/home/wdj/patches/matrix_group20071213.hg\nand file is at\nhttp://sage.math.washington.edu/home/wdj/patches/matrix_group.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/1485\n\n",
    "created_at": "2007-12-13T12:30:16Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "wrapper for invariant_ring and invariant_algebra_reynolds in Singular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1485",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @malb

Wraps Singular's invariant_algebra_reynolds and invariant_ring in finvar.lib, with help from Simon King and Martin Albrecht. Computes generators for the polynomial ring F[x1,...,xn]^G, where G in GL(n,F) is a finite matrix group.

In the "good characteristic" case the polynomials returned form a minimal generating set for the algebra of G-invariant polynomials. In the "bad" case, the polynomials returned are primary and secondary invariants, forming a not necessarily minimal generating set for the algebra of G-invariant polynomials.

Patch is at
http://sage.math.washington.edu/home/wdj/patches/matrix_group20071213.hg
and file is at
http://sage.math.washington.edu/home/wdj/patches/matrix_group.py

Issue created by migration from https://trac.sagemath.org/ticket/1485





---

archive/issue_comments_009537.json:
```json
{
    "body": "This is indirectly related to trac ticket http://sagetrac.org/sage_trac/ticket/1274\nbut does not resolve that issue.",
    "created_at": "2007-12-13T12:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9537",
    "user": "https://github.com/wdjoyner"
}
```

This is indirectly related to trac ticket http://sagetrac.org/sage_trac/ticket/1274
but does not resolve that issue.



---

archive/issue_comments_009538.json:
```json
{
    "body": "Attachment [matrix_group20071213.hg](tarball://root/attachments/some-uuid/ticket1485/matrix_group20071213.hg) by @malb created at 2008-01-16 16:34:19\n\nThe patch applies cleanly and the doctests pass. I cannot check the results due to lack of knowledge, though. Good to go in, if you ask me.",
    "created_at": "2008-01-16T16:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9538",
    "user": "https://github.com/malb"
}
```

Attachment [matrix_group20071213.hg](tarball://root/attachments/some-uuid/ticket1485/matrix_group20071213.hg) by @malb created at 2008-01-16 16:34:19

The patch applies cleanly and the doctests pass. I cannot check the results due to lack of knowledge, though. Good to go in, if you ask me.



---

archive/issue_comments_009539.json:
```json
{
    "body": "Merged in Sage 2.10.alpha4",
    "created_at": "2008-01-16T17:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9539",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha4



---

archive/issue_comments_009540.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-16T17:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9540",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001637.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-16T17:24:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1485#event-1637"
}
```



---

archive/issue_comments_009541.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-01-16T22:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9541",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_009542.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-01-16T22:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9542",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001638.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-16T22:12:39Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1485#event-1638"
}
```



---

archive/issue_comments_009543.json:
```json
{
    "body": "The patch causes hangs when doctesting `plot/plot3d/transform.pyx`. The really odd thing is that everything is fine when running that doctest with the `-verbose` flag.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-16T22:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9543",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch causes hangs when doctesting `plot/plot3d/transform.pyx`. The really odd thing is that everything is fine when running that doctest with the `-verbose` flag.

Cheers,

Michael



---

archive/issue_comments_009544.json:
```json
{
    "body": "While somebody is at it: please attach single commit change sets as patch in the future.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-16T22:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9544",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

While somebody is at it: please attach single commit change sets as patch in the future.

Cheers,

Michael



---

archive/issue_comments_009545.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2008-01-18T16:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9545",
    "user": "https://github.com/malb"
}
```

Changing status from reopened to new.



---

archive/issue_comments_009546.json:
```json
{
    "body": "Changing assignee from @malb to @wdjoyner.",
    "created_at": "2008-01-18T16:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9546",
    "user": "https://github.com/malb"
}
```

Changing assignee from @malb to @wdjoyner.



---

archive/issue_comments_009547.json:
```json
{
    "body": "Mercurial is stupid: I applied this patch in alpha4, but reverted it by applying the inverse with patch and committed. But unbundling the bundle again doesn't commit *anything*.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-19T17:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9547",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mercurial is stupid: I applied this patch in alpha4, but reverted it by applying the inverse with patch and committed. But unbundling the bundle again doesn't commit *anything*.

Cheers,

Michael



---

archive/issue_comments_009548.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-19T17:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1485#issuecomment-9548",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001639.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-19T17:08:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1485",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1485#event-1639"
}
```
