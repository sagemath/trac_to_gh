# Issue 2465: 2.10.3 doctest failure in groebner_fan.py

archive/issues_002465.json:
```json
{
    "body": "Assignee: failure\n\nThe failure is\n\n```\nFile \"groebner_fan.py\", line 42:\n    sage: g.reduced_groebner_bases()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[3]>\", line 1, in <module>\n        g.reduced_groebner_bases()###line 42:\n    sage: g.reduced_groebner_bases()\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 272, in reduced_groebner_bases\n        G0 = self._gfan_reduced_groebner_bases()\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 230, in _gfan_reduced_groebner_bases\n        B = self.gfan()\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 310, in gfan\n        I = self._gfan_ideal()\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 214, in _gfan_ideal\n        J = to_gfan(self.__ideal)\n      File \"morphism.pyx\", line 116, in sage.categories.morphism.Morphism.__call__\n      File \"multi_polynomial_libsingular.pyx\", line 618, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__\n        return self(str(element))\n      File \"multi_polynomial_libsingular.pyx\", line 525, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__\n        element = eval(element, d, {})\n      File \"<string>\", line 1\n         Ideal (x**2 - y**2 + 1) of Multivariate Polynomial Ring in x, y over Rational Field\n                                  ^\n     SyntaxError: invalid syntax\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2465\n\n",
    "created_at": "2008-03-11T01:43:15Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "2.10.3 doctest failure in groebner_fan.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2465",
    "user": "mabshoff"
}
```
Assignee: failure

The failure is

```
File "groebner_fan.py", line 42:
    sage: g.reduced_groebner_bases()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        g.reduced_groebner_bases()###line 42:
    sage: g.reduced_groebner_bases()
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 272, in reduced_groebner_bases
        G0 = self._gfan_reduced_groebner_bases()
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 230, in _gfan_reduced_groebner_bases
        B = self.gfan()
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 310, in gfan
        I = self._gfan_ideal()
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 214, in _gfan_ideal
        J = to_gfan(self.__ideal)
      File "morphism.pyx", line 116, in sage.categories.morphism.Morphism.__call__
      File "multi_polynomial_libsingular.pyx", line 618, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
        return self(str(element))
      File "multi_polynomial_libsingular.pyx", line 525, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
        element = eval(element, d, {})
      File "<string>", line 1
         Ideal (x**2 - y**2 + 1) of Multivariate Polynomial Ring in x, y over Rational Field
                                  ^
     SyntaxError: invalid syntax
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/2465





---

archive/issue_comments_016706.json:
```json
{
    "body": "Changing assignee from failure to @williamstein.",
    "created_at": "2008-03-11T01:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2465#issuecomment-16706",
    "user": "@williamstein"
}
```

Changing assignee from failure to @williamstein.



---

archive/issue_comments_016707.json:
```json
{
    "body": "Attachment [sage-2465.patch](tarball://root/attachments/some-uuid/ticket2465/sage-2465.patch) by @williamstein created at 2008-03-11 02:02:49",
    "created_at": "2008-03-11T02:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2465#issuecomment-16707",
    "user": "@williamstein"
}
```

Attachment [sage-2465.patch](tarball://root/attachments/some-uuid/ticket2465/sage-2465.patch) by @williamstein created at 2008-03-11 02:02:49



---

archive/issue_comments_016708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-11T02:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2465#issuecomment-16708",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_016709.json:
```json
{
    "body": "The patch fixes the doctest failure. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-11T02:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2465#issuecomment-16709",
    "user": "mabshoff"
}
```

The patch fixes the doctest failure. Positive review.

Cheers,

Michael



---

archive/issue_comments_016710.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc5",
    "created_at": "2008-03-11T02:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2465#issuecomment-16710",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc5
