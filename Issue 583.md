# Issue 583: major bug in polynomial creation

archive/issues_000583.json:
```json
{
    "body": "Assignee: somebody\n\nFrom J Voight:\n\n```\nsage: cfs = [-64,-147,28,126]\nsage: fQ = QQ['x'](cfs)\nsage: fQ.is_irreducible()\nTrue\nsage:\nsage: # First try with real double field\nsage: fRDF = RDF['x'](cfs)\nsage: fRDF\n126.0*x^3 + 28.0*x^2 - 147.0*x - 64.0\nsage: fRDF.roots()\n[-2.03728436529, -1.12136314957, 0.861772514857]\nsage: [fRDF(r) for r in fRDF.roots()]\n[-713.73585047, -41.6189386015, -89.2466895053]\nsage: # Argh! The computed roots are not zeros!\nsage: # This does not agree with the python/numpy direct call:\nsage: # >>> cfs = array([-64,-147,28,126])\nsage: # >>> roots(cfs)\nsage: # array([-2.03728437, -1.12136315,  0.86177251])\nsage: # >>> f = poly1d(cfs)\nsage: # >>> [f(r) for r in roots(cfs)]\nsage: # [2.8421709430404007e-014, 0.0, -5.6843418860808015e-014]\nsage:\nsage: # Now try precision 40\nsage: fR40 = RealField(40)['x'](cfs)\nsage: fR40\n126.00000000*x^3 + 28.000000000*x^2 - 147.00000000*x - 64.000000000\nsage: fR40.roots()\n[-0.89177176937, -0.49084949408, 1.1603990412]\n[fR40(r) for r in fR40.roots()]\nsage: [fR40(r) for r in fR40.roots()]\n# The roots are totally different!\n[0, 0, -0.00000000023283064365]\nsage: # The roots are totally different!\nsage: # Maybe it's a problem with the order of the coefficients\nsage: cfs.reverse()\nsage: cfs\n[126, 28, -147, -64]\nsage: fRDFrev = RDF['x'](cfs)\nsage: fRDFrev\n-64.0*x^3 - 147.0*x^2 + 28.0*x + 126.0\nsage: fRDFrev.roots()\n[1.16039904123, -0.891771769374, -0.49084949408]\nsage: [fRDFrev(r) for r in fRDFrev.roots()]\n[-139.44861312, 29.5156369585, 84.4077948961]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/583\n\n",
    "created_at": "2007-09-03T17:03:53Z",
    "labels": [
        "component: basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "major bug in polynomial creation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/583",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

From J Voight:

```
sage: cfs = [-64,-147,28,126]
sage: fQ = QQ['x'](cfs)
sage: fQ.is_irreducible()
True
sage:
sage: # First try with real double field
sage: fRDF = RDF['x'](cfs)
sage: fRDF
126.0*x^3 + 28.0*x^2 - 147.0*x - 64.0
sage: fRDF.roots()
[-2.03728436529, -1.12136314957, 0.861772514857]
sage: [fRDF(r) for r in fRDF.roots()]
[-713.73585047, -41.6189386015, -89.2466895053]
sage: # Argh! The computed roots are not zeros!
sage: # This does not agree with the python/numpy direct call:
sage: # >>> cfs = array([-64,-147,28,126])
sage: # >>> roots(cfs)
sage: # array([-2.03728437, -1.12136315,  0.86177251])
sage: # >>> f = poly1d(cfs)
sage: # >>> [f(r) for r in roots(cfs)]
sage: # [2.8421709430404007e-014, 0.0, -5.6843418860808015e-014]
sage:
sage: # Now try precision 40
sage: fR40 = RealField(40)['x'](cfs)
sage: fR40
126.00000000*x^3 + 28.000000000*x^2 - 147.00000000*x - 64.000000000
sage: fR40.roots()
[-0.89177176937, -0.49084949408, 1.1603990412]
[fR40(r) for r in fR40.roots()]
sage: [fR40(r) for r in fR40.roots()]
# The roots are totally different!
[0, 0, -0.00000000023283064365]
sage: # The roots are totally different!
sage: # Maybe it's a problem with the order of the coefficients
sage: cfs.reverse()
sage: cfs
[126, 28, -147, -64]
sage: fRDFrev = RDF['x'](cfs)
sage: fRDFrev
-64.0*x^3 - 147.0*x^2 + 28.0*x + 126.0
sage: fRDFrev.roots()
[1.16039904123, -0.891771769374, -0.49084949408]
sage: [fRDFrev(r) for r in fRDFrev.roots()]
[-139.44861312, 29.5156369585, 84.4077948961]
```


Issue created by migration from https://trac.sagemath.org/ticket/583





---

archive/issue_comments_003000.json:
```json
{
    "body": "fix the bug",
    "created_at": "2007-09-04T02:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/583#issuecomment-3000",
    "user": "https://github.com/williamstein"
}
```

fix the bug



---

archive/issue_comments_003001.json:
```json
{
    "body": "Attachment [trac583.patch](tarball://root/attachments/some-uuid/ticket583/trac583.patch) by @williamstein created at 2007-09-04 02:17:53",
    "created_at": "2007-09-04T02:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/583#issuecomment-3001",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac583.patch](tarball://root/attachments/some-uuid/ticket583/trac583.patch) by @williamstein created at 2007-09-04 02:17:53



---

archive/issue_comments_003002.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-04T02:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/583#issuecomment-3002",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001555.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-04T02:17:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/583",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/583#event-1555"
}
```
