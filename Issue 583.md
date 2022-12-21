# Issue 583: major bug in polynomial creation

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-03 17:03:53

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



---

Comment by was created at 2007-09-04 02:17:01

fix the bug


---

Attachment


---

Comment by was created at 2007-09-04 02:17:53

Resolution: fixed
