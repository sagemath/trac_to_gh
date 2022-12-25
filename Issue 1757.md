# Issue 1757: implement Coppersmith's method for finding small roots of univariate polynomials modulo an integer

archive/issues_001757.json:
```json
{
    "body": "Assignee: somebody\n\nFrom the MAGMA 2.14 changelog: \"Coppersmith's method for finding small roots of univariate polynomials modulo an integer has been implemented. This implementation uses the new fpLLL package of Damien Stehl\u00e9.\" ( http://magma.maths.usyd.edu.au/magma/htmlhelp/rel/node2.htm )\n\nIssue created by migration from https://trac.sagemath.org/ticket/1757\n\n",
    "created_at": "2008-01-11T18:36:46Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "implement Coppersmith's method for finding small roots of univariate polynomials modulo an integer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1757",
    "user": "https://github.com/malb"
}
```
Assignee: somebody

From the MAGMA 2.14 changelog: "Coppersmith's method for finding small roots of univariate polynomials modulo an integer has been implemented. This implementation uses the new fpLLL package of Damien Stehlé." ( http://magma.maths.usyd.edu.au/magma/htmlhelp/rel/node2.htm )

Issue created by migration from https://trac.sagemath.org/ticket/1757





---

archive/issue_comments_011059.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-03-03T22:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1757#issuecomment-11059",
    "user": "https://github.com/malb"
}
```

Changing priority from major to minor.



---

archive/issue_comments_011060.json:
```json
{
    "body": "The MAGMA documentation for this function is here `SmallRoots`:\n\n  http://magma.maths.usyd.edu.au/magma/htmlhelp/text300.htm\n\nCoppersmith's algorithm is described and discussed in Alexander May's PhD thesis:\n\n  http://www.informatik.tu-darmstadt.de/KP/publications/03/bp.ps\n\nA first naive implementation would look like this:\n\n```\ndef small_roots(f, X=None):\n  d = f.degree()\n  K = f.base_ring()\n  M = K.characteristic()\n  f.change_ring(ZZ)\n  if X is None:\n    X =  M.nth_root(d*(d+1)/2)\n  A = Matrix(ZZ,d+1,d+1)\n  for i in range(d):\n    A[i,i] = M*X^i\n  for i in range(d+1):\n    A[d,i] = ZZ(f[i])*X^i\n  A = A.LLL()\n  x = ZZ['x'].gen(0)\n  g = 0\n  for i in range(d+1):\n    g+= A[0,i]/X^i * x^i\n  return map(lambda (x,y):(K(x),y), g.roots())\n```\n\nWe can do slightly better though.",
    "created_at": "2008-03-03T22:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1757#issuecomment-11060",
    "user": "https://github.com/malb"
}
```

The MAGMA documentation for this function is here `SmallRoots`:

  http://magma.maths.usyd.edu.au/magma/htmlhelp/text300.htm

Coppersmith's algorithm is described and discussed in Alexander May's PhD thesis:

  http://www.informatik.tu-darmstadt.de/KP/publications/03/bp.ps

A first naive implementation would look like this:

```
def small_roots(f, X=None):
  d = f.degree()
  K = f.base_ring()
  M = K.characteristic()
  f.change_ring(ZZ)
  if X is None:
    X =  M.nth_root(d*(d+1)/2)
  A = Matrix(ZZ,d+1,d+1)
  for i in range(d):
    A[i,i] = M*X^i
  for i in range(d+1):
    A[d,i] = ZZ(f[i])*X^i
  A = A.LLL()
  x = ZZ['x'].gen(0)
  g = 0
  for i in range(d+1):
    g+= A[0,i]/X^i * x^i
  return map(lambda (x,y):(K(x),y), g.roots())
```

We can do slightly better though.



---

archive/issue_comments_011061.json:
```json
{
    "body": "duplicate of #2424",
    "created_at": "2008-03-20T14:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1757#issuecomment-11061",
    "user": "https://github.com/malb"
}
```

duplicate of #2424



---

archive/issue_comments_011062.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-20T14:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1757#issuecomment-11062",
    "user": "https://github.com/malb"
}
```

Resolution: duplicate



---

archive/issue_events_004259.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2008-03-20T14:11:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1757",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1757#event-4259"
}
```



---

archive/issue_events_004260.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-20T21:39:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1757",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1757#event-4260"
}
```
