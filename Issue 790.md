# Issue 790: rational reconstruction failing for p-adics

archive/issues_000790.json:
```json
{
    "body": "Assignee: somebody\n\nIt's not clear to me why the following rational reconstruction is failing. Either there's a bug, or the documentation for `rational_reconstruction()` needs to explain exactly what conditions the rational reconstruction should satisfy.\n\n\n```\nsage: R = Zp(5, 10)\nsage: x = R(8969532)\nsage: x.rational_reconstruction()\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/Users/david/sage-2.8.5/<ipython console> in <module>()\n\n/Users/david/sage-2.8.5/padic_generic_element.pyx in padic_generic_element.pAdicGenericElement.rational_reconstruction()\n\n/Users/david/sage-2.8.5/local/lib/python2.5/site-packages/sage/rings/arith.py in rational_reconstruction(a, m, algorithm)\n   1338     \"\"\"\n   1339     if algorithm == 'fast':\n-> 1340         return integer_ring.ZZ(a).rational_reconstruction(m)\n   1341     elif algorithm == 'python':\n   1342         return _rational_reconstruction_python(a,m)\n\n/Users/david/sage-2.8.5/integer.pyx in integer.Integer.rational_reconstruction()\n\n/Users/david/sage-2.8.5/rational.pyx in rational.pyrex_rational_reconstruction()\n\n/Users/david/sage-2.8.5/gmp.pxi in rational.mpq_rational_reconstruction()\n\n<type 'exceptions.ValueError'>: Rational reconstruction of 8969532 (mod 9765625) does not exist.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/790\n\n",
    "created_at": "2007-10-02T18:26:01Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "rational reconstruction failing for p-adics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/790",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

It's not clear to me why the following rational reconstruction is failing. Either there's a bug, or the documentation for `rational_reconstruction()` needs to explain exactly what conditions the rational reconstruction should satisfy.


```
sage: R = Zp(5, 10)
sage: x = R(8969532)
sage: x.rational_reconstruction()
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/Users/david/sage-2.8.5/<ipython console> in <module>()

/Users/david/sage-2.8.5/padic_generic_element.pyx in padic_generic_element.pAdicGenericElement.rational_reconstruction()

/Users/david/sage-2.8.5/local/lib/python2.5/site-packages/sage/rings/arith.py in rational_reconstruction(a, m, algorithm)
   1338     """
   1339     if algorithm == 'fast':
-> 1340         return integer_ring.ZZ(a).rational_reconstruction(m)
   1341     elif algorithm == 'python':
   1342         return _rational_reconstruction_python(a,m)

/Users/david/sage-2.8.5/integer.pyx in integer.Integer.rational_reconstruction()

/Users/david/sage-2.8.5/rational.pyx in rational.pyrex_rational_reconstruction()

/Users/david/sage-2.8.5/gmp.pxi in rational.mpq_rational_reconstruction()

<type 'exceptions.ValueError'>: Rational reconstruction of 8969532 (mod 9765625) does not exist.
```



Issue created by migration from https://trac.sagemath.org/ticket/790





---

archive/issue_comments_004738.json:
```json
{
    "body": "Attachment [trac790.patch](tarball://root/attachments/some-uuid/ticket790/trac790.patch) by @williamstein created at 2007-11-03 18:38:07",
    "created_at": "2007-11-03T18:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/790#issuecomment-4738",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac790.patch](tarball://root/attachments/some-uuid/ticket790/trac790.patch) by @williamstein created at 2007-11-03 18:38:07



---

archive/issue_comments_004739.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T18:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/790#issuecomment-4739",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000899.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-11-03T18:39:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/790",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/790#event-899"
}
```
