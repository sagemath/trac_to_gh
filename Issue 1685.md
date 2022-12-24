# Issue 1685: restructuring symmetric functions and misc. combinatorics updates.

archive/issues_001685.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1685\n\n",
    "created_at": "2008-01-04T23:35:55Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "restructuring symmetric functions and misc. combinatorics updates.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1685",
    "user": "mhansen"
}
```
Assignee: mhansen

CC:  sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/1685





---

archive/issue_comments_010702.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-04T23:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1685#issuecomment-10702",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010703.json:
```json
{
    "body": "The following files need to be deleted:\n\ncombinat/sfa.py\ncombinat/kfpoly.py\ncombinat/hall_littlewood.py\ncombinat/hall_polynomial.py",
    "created_at": "2008-01-05T00:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1685#issuecomment-10703",
    "user": "mhansen"
}
```

The following files need to be deleted:

combinat/sfa.py
combinat/kfpoly.py
combinat/hall_littlewood.py
combinat/hall_polynomial.py



---

archive/issue_comments_010704.json:
```json
{
    "body": "Attachment [1685.patch](tarball://root/attachments/some-uuid/ticket1685/1685.patch) by mhansen created at 2008-01-05 00:08:40",
    "created_at": "2008-01-05T00:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1685#issuecomment-10704",
    "user": "mhansen"
}
```

Attachment [1685.patch](tarball://root/attachments/some-uuid/ticket1685/1685.patch) by mhansen created at 2008-01-05 00:08:40



---

archive/issue_comments_010705.json:
```json
{
    "body": "Attachment [1685-2.patch](tarball://root/attachments/some-uuid/ticket1685/1685-2.patch) by mhansen created at 2008-01-05 00:09:24",
    "created_at": "2008-01-05T00:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1685#issuecomment-10705",
    "user": "mhansen"
}
```

Attachment [1685-2.patch](tarball://root/attachments/some-uuid/ticket1685/1685-2.patch) by mhansen created at 2008-01-05 00:09:24



---

archive/issue_comments_010706.json:
```json
{
    "body": "Attachment [Sage-2.10.alpha2-revert-hunk-from-ticket-1685.patch](tarball://root/attachments/some-uuid/ticket1685/Sage-2.10.alpha2-revert-hunk-from-ticket-1685.patch) by mabshoff created at 2008-01-11 16:15:49",
    "created_at": "2008-01-11T16:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1685#issuecomment-10706",
    "user": "mabshoff"
}
```

Attachment [Sage-2.10.alpha2-revert-hunk-from-ticket-1685.patch](tarball://root/attachments/some-uuid/ticket1685/Sage-2.10.alpha2-revert-hunk-from-ticket-1685.patch) by mabshoff created at 2008-01-11 16:15:49



---

archive/issue_comments_010707.json:
```json
{
    "body": "Hi Mike, \n\nI needed to revert one hunk from the first patch in order to pass doctests. It seems not to belong in the patch logically and calculus.py already has a similar `_polynomial_` method. I merged the patch in alpha2, but I am leaving this open for now because I might still have to revert this.\n\nOtherwise I like the patch, it seems to be have plenty of doctests, but I am no expert of the mathematics involved. Let me know what you think.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-11T16:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1685#issuecomment-10707",
    "user": "mabshoff"
}
```

Hi Mike, 

I needed to revert one hunk from the first patch in order to pass doctests. It seems not to belong in the patch logically and calculus.py already has a similar `_polynomial_` method. I merged the patch in alpha2, but I am leaving this open for now because I might still have to revert this.

Otherwise I like the patch, it seems to be have plenty of doctests, but I am no expert of the mathematics involved. Let me know what you think.

Cheers,

Michael



---

archive/issue_comments_010708.json:
```json
{
    "body": "Hi Mike, \n\nunfortunately when moving around stuff not all issues get fixed and something assumes the old places of the file or classes. You should be able to fix this much more quickly:\n\n```\n        sage -t  devel/sage-main/sage/libs/symmetrica/schur.pxi\n        sage -t  devel/sage-main/sage/libs/symmetrica/sc.pxi\n        sage -t  devel/sage-main/sage/libs/symmetrica/kostka.pxi\n        sage -t  devel/sage-main/sage/combinat/partition.py\n        sage -t  devel/sage-main/sage/combinat/sf/sfa.py\n        sage -t  devel/sage-main/sage/combinat/sf/elementary.py\n        sage -t  devel/sage-main/sage/combinat/sf/dual.py\n        sage -t  devel/sage-main/sage/combinat/sf/hall_littlewood.py\n        sage -t  devel/sage-main/sage/combinat/sf/schur.py\n        sage -t  devel/sage-main/sage/combinat/sf/monomial.py\n        sage -t  devel/sage-main/sage/combinat/sf/homogeneous.py\n        sage -t  devel/sage-main/sage/combinat/sf/classical.py\n        sage -t  devel/sage-main/sage/combinat/combinatorial_algebra.py\n        sage -t  devel/sage-main/sage/combinat/schubert_polynomial.py\n        sage -t  devel/sage-main/sage/combinat/tableau.py\n```\n\nGood that I didn't close this ticket yet ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-01-12T00:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1685#issuecomment-10708",
    "user": "mabshoff"
}
```

Hi Mike, 

unfortunately when moving around stuff not all issues get fixed and something assumes the old places of the file or classes. You should be able to fix this much more quickly:

```
        sage -t  devel/sage-main/sage/libs/symmetrica/schur.pxi
        sage -t  devel/sage-main/sage/libs/symmetrica/sc.pxi
        sage -t  devel/sage-main/sage/libs/symmetrica/kostka.pxi
        sage -t  devel/sage-main/sage/combinat/partition.py
        sage -t  devel/sage-main/sage/combinat/sf/sfa.py
        sage -t  devel/sage-main/sage/combinat/sf/elementary.py
        sage -t  devel/sage-main/sage/combinat/sf/dual.py
        sage -t  devel/sage-main/sage/combinat/sf/hall_littlewood.py
        sage -t  devel/sage-main/sage/combinat/sf/schur.py
        sage -t  devel/sage-main/sage/combinat/sf/monomial.py
        sage -t  devel/sage-main/sage/combinat/sf/homogeneous.py
        sage -t  devel/sage-main/sage/combinat/sf/classical.py
        sage -t  devel/sage-main/sage/combinat/combinatorial_algebra.py
        sage -t  devel/sage-main/sage/combinat/schubert_polynomial.py
        sage -t  devel/sage-main/sage/combinat/tableau.py
```

Good that I didn't close this ticket yet ;)

Cheers,

Michael



---

archive/issue_comments_010709.json:
```json
{
    "body": "Some of the doctest failures:\n\n```\nsage -t  devel/sage-main/sage/libs/symmetrica/schur.pxi     ****************************************************************\n******\nFile \"schur.py\", line 341:\n    sage: symmetrica.part_part_skewschur([3,2,1],[2,1])\nException raised:\n    Traceback (most recent call last):\n      File \"/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[0]>\", line 1, in <module>\n        symmetrica.part_part_skewschur([Integer(3),Integer(2),Integer(1)],[Integer(2),Integer(1)])###line 341:\n    sage: symmetrica.part_part_skewschur([3,2,1],[2,1])\n      File \"schur.pxi\", line 131, in sage.libs.symmetrica.symmetrica.part_part_skewschur_symmetrica\n        res = _py(cresult)\n      File \"symmetrica.pxi\", line 471, in sage.libs.symmetrica.symmetrica._py\n        return _py_schur(a)\n      File \"symmetrica.pxi\", line 768, in sage.libs.symmetrica.symmetrica._py_schur\n        s = SymmetricFunctionAlgebra(R, basis='s')\n    TypeError: 'NoneType' object is not callable\n**********************************************************************\n1 items had failures:\n   1 of   1 in __main__.example_10\n***Test Failed*** 1 failures.\n```\n\nAnd:\n\n```\nsage -t  devel/sage-main/sage/libs/symmetrica/sc.pxi        Exception exceptions.ImportError: 'No module named sfa' in 'sage\n.libs.symmetrica.symmetrica.late_import' ignored\n\n         [1.7 s]\nsage -t  devel/sage-main/sage/libs/symmetrica/kostka.pxi    Exception exceptions.ImportError: 'No module named sfa' in 'sage\n.libs.symmetrica.symmetrica.late_import' ignored\n```\n\nAnd:\n\n```\nsage -t  devel/sage-main/sage/combinat/partition.py   \n**********************************************************************\nFile \"partition.py\", line 1147:\n    sage: h( s(part) )\nException raised:\n    Traceback (most recent call last):\n      File \"/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_47[4]>\", line 1, in <module>\n        h( s(part) )###line 1147:\n    sage: h( s(part) )\n      File \"/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/sf/classical.p\ny\", line 146, in __call__\n        xmprime = t( {part:Integer(1)} ).monomial_coefficients()\n      File \"schur.pxi\", line 423, in sage.libs.symmetrica.symmetrica.t_SCHUR_HOMSYM_symmetrica\n      File \"symmetrica.pxi\", line 473, in sage.libs.symmetrica.symmetrica._py\n      File \"symmetrica.pxi\", line 846, in sage.libs.symmetrica.symmetrica._py_homsym\n    TypeError: 'NoneType' object is not callable\n**********************************************************************\nFile \"partition.py\", line 1174:\n    sage: Partition([1]).character_polynomial()\nException raised:\n    Traceback (most recent call last):\n      File \"/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_48[0]>\", line 1, in <module>\n        Partition([Integer(1)]).character_polynomial()###line 1174:\n    sage: Partition([1]).character_polynomial()\n      File \"/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/partition.py\",\n line 1191, in character_polynomial\n        ps_mu = p(s(self))\n      File \"/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/sf/classical.p\ny\", line 146, in __call__\n        xmprime = t( {part:Integer(1)} ).monomial_coefficients()\n      File \"schur.pxi\", line 464, in sage.libs.symmetrica.symmetrica.t_SCHUR_POWSYM_symmetrica\n      File \"symmetrica.pxi\", line 475, in sage.libs.symmetrica.symmetrica._py\n      File \"symmetrica.pxi\", line 804, in sage.libs.symmetrica.symmetrica._py_powsym\n    TypeError: 'NoneType' object is not callable\n**********************************************************************\n```\n\nand so on.\n\n```\n         [3.5 s]\nsage -t  devel/sage-main/sage/combinat/sf/sfa.py\n**********************************************************************\nFile \"sfa.py\", line 11:\n    : f2 = e(f1)\nException raised:\n    Traceback (most recent call last):\n      File \"/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[4]>\", line 1, in <module>\n        f2 = e(f1)###line 11:\n    : f2 = e(f1)\n      File \"/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/sf/classical.p\ny\", line 146, in __call__\n        xmprime = t( {part:Integer(1)} ).monomial_coefficients()\n      File \"schur.pxi\", line 443, in sage.libs.symmetrica.symmetrica.t_SCHUR_ELMSYM_symmetrica\n      File \"symmetrica.pxi\", line 477, in sage.libs.symmetrica.symmetrica._py\n      File \"symmetrica.pxi\", line 825, in sage.libs.symmetrica.symmetrica._py_elmsym\n    TypeError: 'NoneType' object is not callable\n**********************************************************************\n```\n\nand so on.\n\n```\nsage -t  devel/sage-main/sage/combinat/sf/elementary.py\n**********************************************************************\nFile \"elementary.py\", line 62:\n    sage: a.frobenius()\nException raised:\n    Traceback (most recent call last):\n      File \"/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[2]>\", line 1, in <module>\n        a.frobenius()###line 62:\n    sage: a.frobenius()\n      File \"/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/sf/elementary.\npy\", line 76, in frobenius\n        return self.parent()(res)\n      File \"/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/sf/classical.p\ny\", line 146, in __call__\n        xmprime = t( {part:Integer(1)} ).monomial_coefficients()\n      File \"schur.pxi\", line 788, in sage.libs.symmetrica.symmetrica.t_HOMSYM_ELMSYM_symmetrica\n      File \"symmetrica.pxi\", line 477, in sage.libs.symmetrica.symmetrica._py\n      File \"symmetrica.pxi\", line 825, in sage.libs.symmetrica.symmetrica._py_elmsym\n    TypeError: 'NoneType' object is not callable\n*********************************************************************\n```\n\nand so on.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-13T11:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1685#issuecomment-10709",
    "user": "mabshoff"
}
```

Some of the doctest failures:

```
sage -t  devel/sage-main/sage/libs/symmetrica/schur.pxi     ****************************************************************
******
File "schur.py", line 341:
    sage: symmetrica.part_part_skewschur([3,2,1],[2,1])
Exception raised:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[0]>", line 1, in <module>
        symmetrica.part_part_skewschur([Integer(3),Integer(2),Integer(1)],[Integer(2),Integer(1)])###line 341:
    sage: symmetrica.part_part_skewschur([3,2,1],[2,1])
      File "schur.pxi", line 131, in sage.libs.symmetrica.symmetrica.part_part_skewschur_symmetrica
        res = _py(cresult)
      File "symmetrica.pxi", line 471, in sage.libs.symmetrica.symmetrica._py
        return _py_schur(a)
      File "symmetrica.pxi", line 768, in sage.libs.symmetrica.symmetrica._py_schur
        s = SymmetricFunctionAlgebra(R, basis='s')
    TypeError: 'NoneType' object is not callable
**********************************************************************
1 items had failures:
   1 of   1 in __main__.example_10
***Test Failed*** 1 failures.
```

And:

```
sage -t  devel/sage-main/sage/libs/symmetrica/sc.pxi        Exception exceptions.ImportError: 'No module named sfa' in 'sage
.libs.symmetrica.symmetrica.late_import' ignored

         [1.7 s]
sage -t  devel/sage-main/sage/libs/symmetrica/kostka.pxi    Exception exceptions.ImportError: 'No module named sfa' in 'sage
.libs.symmetrica.symmetrica.late_import' ignored
```

And:

```
sage -t  devel/sage-main/sage/combinat/partition.py   
**********************************************************************
File "partition.py", line 1147:
    sage: h( s(part) )
Exception raised:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_47[4]>", line 1, in <module>
        h( s(part) )###line 1147:
    sage: h( s(part) )
      File "/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/sf/classical.p
y", line 146, in __call__
        xmprime = t( {part:Integer(1)} ).monomial_coefficients()
      File "schur.pxi", line 423, in sage.libs.symmetrica.symmetrica.t_SCHUR_HOMSYM_symmetrica
      File "symmetrica.pxi", line 473, in sage.libs.symmetrica.symmetrica._py
      File "symmetrica.pxi", line 846, in sage.libs.symmetrica.symmetrica._py_homsym
    TypeError: 'NoneType' object is not callable
**********************************************************************
File "partition.py", line 1174:
    sage: Partition([1]).character_polynomial()
Exception raised:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_48[0]>", line 1, in <module>
        Partition([Integer(1)]).character_polynomial()###line 1174:
    sage: Partition([1]).character_polynomial()
      File "/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/partition.py",
 line 1191, in character_polynomial
        ps_mu = p(s(self))
      File "/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/sf/classical.p
y", line 146, in __call__
        xmprime = t( {part:Integer(1)} ).monomial_coefficients()
      File "schur.pxi", line 464, in sage.libs.symmetrica.symmetrica.t_SCHUR_POWSYM_symmetrica
      File "symmetrica.pxi", line 475, in sage.libs.symmetrica.symmetrica._py
      File "symmetrica.pxi", line 804, in sage.libs.symmetrica.symmetrica._py_powsym
    TypeError: 'NoneType' object is not callable
**********************************************************************
```

and so on.

```
         [3.5 s]
sage -t  devel/sage-main/sage/combinat/sf/sfa.py
**********************************************************************
File "sfa.py", line 11:
    : f2 = e(f1)
Exception raised:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[4]>", line 1, in <module>
        f2 = e(f1)###line 11:
    : f2 = e(f1)
      File "/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/sf/classical.p
y", line 146, in __call__
        xmprime = t( {part:Integer(1)} ).monomial_coefficients()
      File "schur.pxi", line 443, in sage.libs.symmetrica.symmetrica.t_SCHUR_ELMSYM_symmetrica
      File "symmetrica.pxi", line 477, in sage.libs.symmetrica.symmetrica._py
      File "symmetrica.pxi", line 825, in sage.libs.symmetrica.symmetrica._py_elmsym
    TypeError: 'NoneType' object is not callable
**********************************************************************
```

and so on.

```
sage -t  devel/sage-main/sage/combinat/sf/elementary.py
**********************************************************************
File "elementary.py", line 62:
    sage: a.frobenius()
Exception raised:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        a.frobenius()###line 62:
    sage: a.frobenius()
      File "/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/sf/elementary.
py", line 76, in frobenius
        return self.parent()(res)
      File "/tmp/Work-mabshoff/release-cycle/sage-2.10.alpha3/local/lib/python2.5/site-packages/sage/combinat/sf/classical.p
y", line 146, in __call__
        xmprime = t( {part:Integer(1)} ).monomial_coefficients()
      File "schur.pxi", line 788, in sage.libs.symmetrica.symmetrica.t_HOMSYM_ELMSYM_symmetrica
      File "symmetrica.pxi", line 477, in sage.libs.symmetrica.symmetrica._py
      File "symmetrica.pxi", line 825, in sage.libs.symmetrica.symmetrica._py_elmsym
    TypeError: 'NoneType' object is not callable
*********************************************************************
```

and so on.

Cheers,

Michael



---

archive/issue_comments_010710.json:
```json
{
    "body": "Attachment [1685-doctests.patch](tarball://root/attachments/some-uuid/ticket1685/1685-doctests.patch) by mabshoff created at 2008-01-13 12:14:32\n\nMerged in Sage 2.10.alpha2. I applied 1685-doctests.patch and now all combinatorics doctest pass.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-13T12:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1685#issuecomment-10710",
    "user": "mabshoff"
}
```

Attachment [1685-doctests.patch](tarball://root/attachments/some-uuid/ticket1685/1685-doctests.patch) by mabshoff created at 2008-01-13 12:14:32

Merged in Sage 2.10.alpha2. I applied 1685-doctests.patch and now all combinatorics doctest pass.

Cheers,

Michael



---

archive/issue_comments_010711.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-13T12:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1685#issuecomment-10711",
    "user": "mabshoff"
}
```

Resolution: fixed
