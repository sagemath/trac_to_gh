# Issue 1685: restructuring symmetric functions and misc. combinatorics updates.

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-01-04 23:35:55

Assignee: mhansen

CC:  sage-combinat




---

Comment by mhansen created at 2008-01-04 23:42:20

Changing status from new to assigned.


---

Comment by mhansen created at 2008-01-05 00:00:36

The following files need to be deleted:

combinat/sfa.py
combinat/kfpoly.py
combinat/hall_littlewood.py
combinat/hall_polynomial.py


---

Attachment


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-01-11 16:18:39

Hi Mike, 

I needed to revert one hunk from the first patch in order to pass doctests. It seems not to belong in the patch logically and calculus.py already has a similar `_polynomial_` method. I merged the patch in alpha2, but I am leaving this open for now because I might still have to revert this.

Otherwise I like the patch, it seems to be have plenty of doctests, but I am no expert of the mathematics involved. Let me know what you think.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-12 00:37:45

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

Comment by mabshoff created at 2008-01-13 11:37:15

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

Attachment

Merged in Sage 2.10.alpha2. I applied 1685-doctests.patch and now all combinatorics doctest pass.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-13 12:14:32

Resolution: fixed
