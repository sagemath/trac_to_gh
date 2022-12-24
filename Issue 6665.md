# Issue 6665: Expanding the 'zero' symmetric function in variables crashes symmetrica

archive/issues_006665.json:
```json
{
    "body": "Assignee: mhansen\n\nKeywords: symmetrica\n\nJerome Lefebvre reported:\n\n```\nBizarre error reporting with symmetric functions;\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: H = SymmetricFunctionAlgebra(QQ, basis='homogeneous')\nsage: f = H(0)\nsage: print f\n0\nsage: g = f.expand(3, alphabet=['x_1','x_2','x_3'])\n| Sage Version 4.1, Release Date: 2009-07-09                         |\n| Type notebook() for the GUI, and license() for information.        |\nThis then gives me;\n\nenter a to abort with core dump, g to go, f to supress\ns to supress further error text, r to retry,  e to explain, else stop\nERROR: s_po_k: not POLYNOM?:\n\n\nSo I entered e (had to do it twice) to get;\n\n\nenter a to abort with core dump, g to go, f to supress\ns to supress further error text, r to retry,  e to explain, else stop\nERROR: s_po_k: not POLYNOM?: e\n\nenter a to abort with core dump, g to go, f to supress\ns to supress further error text, r to retry,  e to explain, else stop\nERROR: s_o_k:object == NULL?: e\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call\nlast)\n\n/Users/jeromelefebvre/.sage/temp/Jerome.local/22022/\n_Users_jeromelefebvre__sage_init_sage_0.py in <module>()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/sf/\nhomogeneous.pyc in expand(self, n, alphabet)\n     95         \"\"\"\n     96         condition = lambda part: False\n---> 97         return self._expand(condition, n, alphabet)\n     98\n     99\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/sf/\nsfa.pyc in _expand(self, condition, n, alphabet)\n   1534         resPR = PolynomialRing(parent.base_ring(), n,\nalphabet)\n   1535         f = lambda part: resPR(0) if condition(part) else resPR\n(e(part, n, alphabet))\n-> 1536         return parent._apply_module_morphism(self, f)\n   1537\n   1538     def scalar(self, x):\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/\nfree_module.pyc in _apply_module_morphism(self, x, f)\n    973         res = 0\n    974         for m, c in x._monomial_coefficients.iteritems():\n--> 975             res += c*f(m)\n    976         return res\n    977\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/sf/\nsfa.pyc in <lambda>(part)\n   1533         e = eval('symmetrica.compute_' + str\n(classical.translate[parent.basis_name()]).lower() + '_with_alphabet')\n   1534         resPR = PolynomialRing(parent.base_ring(), n,\nalphabet)\n-> 1535         f = lambda part: resPR(0) if condition(part) else resPR\n(e(part, n, alphabet))\n   1536         return parent._apply_module_morphism(self, f)\n   1537\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/libs/\nsymmetrica/symmetrica.so in\nsage.libs.symmetrica.symmetrica.compute_homsym_with_alphabet_symmetrica\n(sage/libs/symmetrica/symmetrica.c:15628)()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/libs/\nsymmetrica/symmetrica.so in\nsage.libs.symmetrica.symmetrica._py_polynom_alphabet (sage/libs/\nsymmetrica/symmetrica.c:4777)()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/libs/\nsymmetrica/symmetrica.so in sage.libs.symmetrica.symmetrica._py (sage/\nlibs/symmetrica/symmetrica.c:2203)()\n\nNotImplementedError: -6\nsage:\n```\n\n\nThis is related to #6487, and the fact that symmetrica typically segfaults with input it doesn't expect.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6665\n\n",
    "created_at": "2009-08-02T11:16:36Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Expanding the 'zero' symmetric function in variables crashes symmetrica",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6665",
    "user": "jbandlow"
}
```
Assignee: mhansen

Keywords: symmetrica

Jerome Lefebvre reported:

```
Bizarre error reporting with symmetric functions;

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: H = SymmetricFunctionAlgebra(QQ, basis='homogeneous')
sage: f = H(0)
sage: print f
0
sage: g = f.expand(3, alphabet=['x_1','x_2','x_3'])
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
This then gives me;

enter a to abort with core dump, g to go, f to supress
s to supress further error text, r to retry,  e to explain, else stop
ERROR: s_po_k: not POLYNOM?:


So I entered e (had to do it twice) to get;


enter a to abort with core dump, g to go, f to supress
s to supress further error text, r to retry,  e to explain, else stop
ERROR: s_po_k: not POLYNOM?: e

enter a to abort with core dump, g to go, f to supress
s to supress further error text, r to retry,  e to explain, else stop
ERROR: s_o_k:object == NULL?: e
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call
last)

/Users/jeromelefebvre/.sage/temp/Jerome.local/22022/
_Users_jeromelefebvre__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/sf/
homogeneous.pyc in expand(self, n, alphabet)
     95         """
     96         condition = lambda part: False
---> 97         return self._expand(condition, n, alphabet)
     98
     99

/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/sf/
sfa.pyc in _expand(self, condition, n, alphabet)
   1534         resPR = PolynomialRing(parent.base_ring(), n,
alphabet)
   1535         f = lambda part: resPR(0) if condition(part) else resPR
(e(part, n, alphabet))
-> 1536         return parent._apply_module_morphism(self, f)
   1537
   1538     def scalar(self, x):

/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/
free_module.pyc in _apply_module_morphism(self, x, f)
    973         res = 0
    974         for m, c in x._monomial_coefficients.iteritems():
--> 975             res += c*f(m)
    976         return res
    977

/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/sf/
sfa.pyc in <lambda>(part)
   1533         e = eval('symmetrica.compute_' + str
(classical.translate[parent.basis_name()]).lower() + '_with_alphabet')
   1534         resPR = PolynomialRing(parent.base_ring(), n,
alphabet)
-> 1535         f = lambda part: resPR(0) if condition(part) else resPR
(e(part, n, alphabet))
   1536         return parent._apply_module_morphism(self, f)
   1537

/Applications/sage/local/lib/python2.6/site-packages/sage/libs/
symmetrica/symmetrica.so in
sage.libs.symmetrica.symmetrica.compute_homsym_with_alphabet_symmetrica
(sage/libs/symmetrica/symmetrica.c:15628)()

/Applications/sage/local/lib/python2.6/site-packages/sage/libs/
symmetrica/symmetrica.so in
sage.libs.symmetrica.symmetrica._py_polynom_alphabet (sage/libs/
symmetrica/symmetrica.c:4777)()

/Applications/sage/local/lib/python2.6/site-packages/sage/libs/
symmetrica/symmetrica.so in sage.libs.symmetrica.symmetrica._py (sage/
libs/symmetrica/symmetrica.c:2203)()

NotImplementedError: -6
sage:
```


This is related to #6487, and the fact that symmetrica typically segfaults with input it doesn't expect.

Issue created by migration from https://trac.sagemath.org/ticket/6665





---

archive/issue_comments_054703.json:
```json
{
    "body": "Attachment [trac_6665_zero_plethysm_jb.patch](tarball://root/attachments/some-uuid/ticket6665/trac_6665_zero_plethysm_jb.patch) by jbandlow created at 2010-05-06 15:39:35",
    "created_at": "2010-05-06T15:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6665#issuecomment-54703",
    "user": "jbandlow"
}
```

Attachment [trac_6665_zero_plethysm_jb.patch](tarball://root/attachments/some-uuid/ticket6665/trac_6665_zero_plethysm_jb.patch) by jbandlow created at 2010-05-06 15:39:35



---

archive/issue_comments_054704.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-06T15:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6665#issuecomment-54704",
    "user": "jbandlow"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054705.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-09T16:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6665#issuecomment-54705",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054706.json:
```json
{
    "body": "Applies fines, does it job, nothing to complain about... Thank youuuuu ! :-)\n\nNathann",
    "created_at": "2010-05-09T16:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6665#issuecomment-54706",
    "user": "ncohen"
}
```

Applies fines, does it job, nothing to complain about... Thank youuuuu ! :-)

Nathann



---

archive/issue_comments_054707.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6665#issuecomment-54707",
    "user": "mhansen"
}
```

Resolution: fixed
