# Issue 365: very serious infinite loop in coercion somewhere

archive/issues_000365.json:
```json
{
    "body": "Assignee: somebody\n\n```\nOn 5/17/07, Prof. J. E. Cremona <john.cremona@nottingham.ac.uk> wrote:\n> \n> Problem:  when executing the following, the last line takes forever and\n> had to be killed:\n> \n> R = PolynomialRing(QQ, ['a','b','c','d','e'], 5)\n> K = R.fraction_field()\n> a,b,c,d,e = K.gens()\n> \n> ig = 12*a*e-3*b*d+c^2\n> jg = 72*a*c*e+9*b*c*d-27*a*d^2-27*e*b^2-2*c^3\n> hg = 8*a*c-3*b^2\n> deltag = 4*ig^3-jg^2\n> \n> Ky.<y> = PolynomialRing(K,'y')\n> phipoly = y^3-3*ig*y+jg\n> \n> What am I missing?\n\nNothing --  You have found a subtle bug in SAGE's coercion code.  \nIf you make the coercion that is going on in the last line very explicit,\nthen the above line works, e.g., this works (note that I've used some\nmore compact notation at the beginning, but it's equivalent to\nwhat you wrote):\n\n{{{\nR.<a,b,c,d,e> = QQ[]\nK = R.fraction_field()\na,b,c,d,e = K.gens()\nig = 12*a*e-3*b*d+c^2\njg = 72*a*c*e+9*b*c*d-27*a*d^2-27*e*b^2-2*c^3\nhg = 8*a*c-3*b^2\ndeltag = 4*ig^3-jg^2\n}}}\n\n{{{\nKy.<y> = PolynomialRing(K,'y')\nphipoly = y^3-3*ig*y+Ky([jg])\nphipoly\n///\ny^3 + (-3*c^2 + 9*b*d - 36*a*e)*y + -2*c^3 + 9*b*c*d - 27*b^2*e - 27*a*d^2 + 72*a*c*e\n}}}\n\nThe difference is that I put Ky([jg]) explicitly instead of jg.  \n\nWhatever is causing this is a serious bug, and I hope somebody fixes\nit soon (or that I do).  It's trac #\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/365\n\n",
    "created_at": "2007-05-17T15:47:05Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "very serious infinite loop in coercion somewhere",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/365",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

```
On 5/17/07, Prof. J. E. Cremona <john.cremona@nottingham.ac.uk> wrote:
> 
> Problem:  when executing the following, the last line takes forever and
> had to be killed:
> 
> R = PolynomialRing(QQ, ['a','b','c','d','e'], 5)
> K = R.fraction_field()
> a,b,c,d,e = K.gens()
> 
> ig = 12*a*e-3*b*d+c^2
> jg = 72*a*c*e+9*b*c*d-27*a*d^2-27*e*b^2-2*c^3
> hg = 8*a*c-3*b^2
> deltag = 4*ig^3-jg^2
> 
> Ky.<y> = PolynomialRing(K,'y')
> phipoly = y^3-3*ig*y+jg
> 
> What am I missing?

Nothing --  You have found a subtle bug in SAGE's coercion code.  
If you make the coercion that is going on in the last line very explicit,
then the above line works, e.g., this works (note that I've used some
more compact notation at the beginning, but it's equivalent to
what you wrote):

{{{
R.<a,b,c,d,e> = QQ[]
K = R.fraction_field()
a,b,c,d,e = K.gens()
ig = 12*a*e-3*b*d+c^2
jg = 72*a*c*e+9*b*c*d-27*a*d^2-27*e*b^2-2*c^3
hg = 8*a*c-3*b^2
deltag = 4*ig^3-jg^2
}}}

{{{
Ky.<y> = PolynomialRing(K,'y')
phipoly = y^3-3*ig*y+Ky([jg])
phipoly
///
y^3 + (-3*c^2 + 9*b*d - 36*a*e)*y + -2*c^3 + 9*b*c*d - 27*b^2*e - 27*a*d^2 + 72*a*c*e
}}}

The difference is that I put Ky([jg]) explicitly instead of jg.  

Whatever is causing this is a serious bug, and I hope somebody fixes
it soon (or that I do).  It's trac #

```

Issue created by migration from https://trac.sagemath.org/ticket/365





---

archive/issue_comments_001761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-05-18T15:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/365#issuecomment-1761",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_001762.json:
```json
{
    "body": "This is fixed now.  It was a problem in the __call__ method of polynomial ring.\n\n```\n@@ -156,6 +163,8 @@ class PolynomialRing_general(sage.algebr\n         C = self.__polynomial_class\n         if isinstance(x, C) and x.parent() is self:\n             return x\n+        elif is_Element(x) and x.parent() == self.base_ring():\n+            return self([x])\n         elif is_SingularElement(x) and self._has_singular:\n             self._singular_().set_ring()\n             try:\n```",
    "created_at": "2007-05-18T15:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/365#issuecomment-1762",
    "user": "https://github.com/williamstein"
}
```

This is fixed now.  It was a problem in the __call__ method of polynomial ring.

```
@@ -156,6 +163,8 @@ class PolynomialRing_general(sage.algebr
         C = self.__polynomial_class
         if isinstance(x, C) and x.parent() is self:
             return x
+        elif is_Element(x) and x.parent() == self.base_ring():
+            return self([x])
         elif is_SingularElement(x) and self._has_singular:
             self._singular_().set_ring()
             try:
```



---

archive/issue_events_000852.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-05-18T15:46:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/365",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/365#event-852"
}
```
