# Issue 5525: fix bug in intersection of ZZ-modules

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-15 07:37:43

Assignee: malb


```
sage: A = (QQ^1).span([This is the Trac macro *1/3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1/3-macro),ZZ); A
Free module of degree 1 and rank 1 over Integer Ring
Echelon basis matrix:
[1/3]
sage: B = (QQ^1).span([This is the Trac macro *1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1-macro),ZZ); B
Free module of degree 1 and rank 1 over Integer Ring
Echelon basis matrix:
[1]
sage: A.intersection(B)
Free module of degree 1 and rank 1 over Integer Ring
Echelon basis matrix:
[1/3]
```



---

Attachment


---

Comment by mabshoff created at 2009-03-23 18:57:42

This patch causes a massive number of failures:

```
The following tests failed:

        sage -t -long devel/sage/sage/modular/abvar/homspace.py # 49 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar.py # 292 doctests failed
        sage -t -long devel/sage/sage/matrix/matrix_integer_dense.pyx # 2 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 7 doctests failed
        sage -t -long devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 3 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 22 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 12 doctests failed
        sage -t -long devel/sage/sage/modular/modform/element.py # 29 doctests failed
        sage -t -long devel/sage/sage/modular/modsym/space.py # 41 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/morphism.py # 86 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/torsion_subgroup.py # 22 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/finite_subgroup.py # 99 doctests failed
        sage -t -long devel/sage/sage/modular/modsym/subspace.py # 10 doctests failed
        sage -t -long devel/sage/sage/modular/modform/space.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/modsym/ambient.py # 18 doctests failed
        sage -t -long devel/sage/sage/modular/modsym/tests.py # 3 doctests failed
        sage -t -long devel/sage/doc/en/bordeaux_2008/modabvar.rst # 11 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar_ambient_jacobian.py # 13 doctests failed
        sage -t -long devel/sage/sage/modular/hecke/submodule.py # 20 doctests failed
        sage -t -long devel/sage/sage/modular/hecke/module.py # 26 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 2 doctests failed
        sage -t -long devel/sage/doc/fr/tutorial/tour_advanced.rst # 1 doctests failed
        sage -t -long devel/sage/doc/en/tutorial/tour_advanced.rst # 1 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar_newform.py # 8 doctests failed
        sage -t -long devel/sage/sage/tests/book_stein_modform.py # 7 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/cuspidal_subgroup.py # 38 doctests failed
        sage -t -long devel/sage/sage/modular/dims.py # 3 doctests failed
        sage -t -long devel/sage/sage/modular/modform/constructor.py # 1 doctests failed
        sage -t -long devel/sage/sage/server/notebook/twist.py # 2 doctests failed
        sage -t -long devel/sage/sage/structure/coerce.pyx # 5 doctests failed
        sage -t -long devel/sage/sage/modular/hecke/ambient_module.py # 12 doctests failed
        sage -t -long devel/sage/sage/structure/factorization.py # 5 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 1 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/lseries.py # 22 doctests failed
        sage -t -long devel/sage/doc/en/bordeaux_2008/modular_symbols.rst # 1 doctests failed
        sage -t -long devel/sage/sage/modular/hecke/hecke_operator.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/hecke/degenmap.py # 10 doctests failed
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 08:45:39

This has been fixed via the patch at #5520.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 08:45:39

Resolution: fixed
