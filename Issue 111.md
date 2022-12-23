# Issue 111: def copy -- they should all be def __copy__

Issue created by migration from https://trac.sagemath.org/ticket/111

Original creator: was

Original creation time: 2006-10-05 06:24:07

Assignee: was

CC:  robertwb mhansen

There are many instances of copy methods in SAGE.  They should all be __copy__, which
is what gets called by the standard copy module (part of the standard Python library). 


```
sage: search_sage('def copy')

matrix/sparse_matrix.py:    def copy(self):
modules/free_module_element.py:    def copy(self):
plot/graph.py:    def copy(self, name):
rings/finite_field_element.py:    def copy(self):
rings/fraction_field_element.py:    def copy(self):
rings/laurent_series_ring_element.py:    def copy(self):
rings/padic.py:    def copy(self):
rings/polynomial_element.py:    def copy(self):
rings/polynomial_element.py:    def copy(self):
rings/polynomial_element.py:    def copy(self):
rings/polynomial_element.py:    def copy(self):
rings/power_series_ring_element.py:    def copy(self):
rings/power_series_ring_element.py:    def copy(self):
rings/quotient_ring_element.py:    def copy(self):
libs/pari/functional.py:def copy(self): return pari(self).copy()
modular/modsym/manin_symbols.py:    def copy(self):
server/server1/server1.py:    def copyfile(self, source, outputfile): 
matrix/dense_matrix_pyx.pyx:    def copy(self):
matrix/matrix_generic.pyx:    def copy(self):
matrix/matrix_integer_dense.pyx:    def copy(self):
matrix/matrix_modn_dense.pyx:    def copy(Matrix_modn_dense self):
matrix/matrix_modn_sparse.pyx:    def copy(self):
matrix/matrix_rational_dense.pyx:    def copy(self):
matrix/sparse_matrix_pyx.pyx:    def copy(self):
matrix/sparse_matrix_pyx.pyx:    def copy(self):
matrix/sparse_matrix_pyx.pyx:    def copy(self):
rings/integer.pyx:    def copy(self):
rings/integer_mod.pyx:    def copy(IntegerMod_gmp self):
rings/integer_mod.pyx:    def copy(IntegerMod_int self):
rings/integer_mod.pyx:    def copy(IntegerMod_int64 self):
rings/mpc.pyx:    def copy(self):
rings/polynomial_pyx.pyx:    def copy(self):
rings/polynomial_pyx.pyx:    def copy(self):
rings/rational.pyx:    def copy(self):
rings/real_double.pyx:    def copy(self):
rings/real_mpfr.pyx:    def copy(self):
rings/sparse_poly.pyx:    def copy(self):
rings/sparse_poly.pyx:    def copy(self):
libs/linbox/finite_field_givaro.pyx:    def copy(self):
libs/ntl/ntl.pyx:    def copy(self):
libs/ntl/ntl.pyx:    def copy(self):
libs/ntl/ntl.pyx:    def copy(ntl_GF2E self):
libs/pari/_py_pari_orig.pyx:    def copy(gen self):
libs/pari/gen.pyx:    def copy(gen self):
```



---

Comment by was created at 2006-10-05 08:07:30

Resolution: fixed


---

Comment by was created at 2006-10-05 08:07:30

Fixed for sage-1.4


---

Comment by was created at 2006-10-05 08:45:09

Resolution changed from fixed to 


---

Comment by was created at 2006-10-05 08:45:09

I reverted my changes in my local copy -- there were some nontrivial issues with make such a global change.


---

Comment by was created at 2006-10-05 08:45:09

Changing status from closed to reopened.


---

Comment by was created at 2007-01-13 02:20:07

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-10-31 21:15:48

The number has decreased significantly:

```
libs/ntl/ntl_ZZX.pyx:    def copy(self):
libs/ntl/ntl_ZZ_pEX.pyx:    def copy(self):
libs/ntl/ntl_ZZ_pX.pyx:    def copy(self):
libs/pari/gen.pyx:    def copy(gen self):
matrix/matrix0.pyx:    def copy(self):
modules/free_module_element.pyx:    def copy(self):
rings/padics/padic_ZZ_pX_CA_element.pyx:    def copy(self):
rings/padics/padic_ZZ_pX_CR_element.pyx:    def copy(self):
rings/padics/padic_ZZ_pX_FM_element.pyx:    def copy(self):
rings/padics/padic_capped_absolute_element.pyx:    def copy(pAdicCappedAbsoluteElement self):
rings/padics/padic_capped_relative_element.pyx:    def copy(self):
rings/padics/padic_fixed_mod_element.pyx:    def copy(self):
rings/polynomial/polynomial_pyx.pyx:    def copy(self):
rings/polynomial/polynomial_pyx.pyx:    def copy(self):
rings/laurent_series_ring_element.pyx:    def copy(self):
rings/power_series_poly.pyx:    def copy(self):
rings/rational.pyx:    def copy(self):
rings/sparse_poly.pyx:    def copy(self):
rings/sparse_poly.pyx:    def copy(self):
```


It would be nice if someone could take an axe to the remaining ones.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-07-12 01:44:03

In sage-4.1, I am seeing


```
libs/pari/gen.pyx:1051:    def copy(gen self):
libs/ntl/ntl_ZZ_pEX.pyx:197:    def copy(self):
libs/ntl/ntl_ZZ_pX.pyx:189:    def copy(self):
libs/ntl/ntl_ZZX.pyx:152:    def copy(self):
graphs/graph.py:780:    def copy(self, implementation='networkx', sparse=None):
combinat/matrices/latin.py:321:    def copy(self):
matrix/matrix0.pyx:115:    def copy(self):
modular/modsym/manin_symbols.py:1667:    def copy(self):
rings/laurent_series_ring_element.pyx:943:    def copy(self):
rings/finite_field_givaro.pyx:1118:    cdef FiniteField_givaro copy
rings/finite_field_element.py:396:    def copy(self):
rings/fraction_field_element.pyx:179:    def copy(self):
rings/power_series_poly.pyx:575:    def copy(self):
rings/rational.pyx:558:    def copy(self):
rings/padics/padic_fixed_mod_element.pyx:661:    def copy(self):
rings/padics/padic_ZZ_pX_CA_element.pyx:1567:    def copy(self):
rings/padics/padic_ZZ_pX_CR_element.pyx:2193:    def copy(self):
rings/padics/padic_ZZ_pX_FM_element.pyx:840:    def copy(self):
rings/padics/padic_capped_relative_element.pyx:1453:    def copy(self):
rings/padics/padic_capped_absolute_element.pyx:810:    def copy(pAdicCappedAbsoluteElement self):
rings/polynomial/polynomial_element_generic.py:866:    def copy(self):
rings/polynomial/padics/polynomial_padic_capped_relative_dense.py:726:    def copy(self):
groups/perm_gps/partn_ref/refinement_python.pyx:145:    def copy(self):
modules/free_module_element.pyx:513:    def copy(self):
databases/database.py:575:    def copy(self):
databases/database.py:1003:    def copy(self):
databases/database.py:1546:    def copy(self):
```



---

Comment by AlexGhitza created at 2009-07-13 10:39:10

Changing status from reopened to new.


---

Comment by AlexGhitza created at 2009-07-13 10:39:10

Doing all of these in one shot is pretty nasty.  I've attached a patch that fixes most of the instances, and I have opened two follow-up tickets: #6521 for matrix0.pyx and #6522 for graph.py.


---

Comment by AlexGhitza created at 2009-07-13 10:39:10

Changing assignee from was to AlexGhitza.


---

Attachment


---

Comment by AlexGhitza created at 2009-07-13 10:40:15

Changing status from new to assigned.


---

Comment by davidloeffler created at 2009-07-14 16:59:09

Patch looks fine to me -- I am running doctests at the moment -- but it looks like you missed one in `sage/rings/polynomial/polynomial_element_generic.py`. I'll do a mini-patch and see if that breaks anything :-)


---

Comment by davidloeffler created at 2009-07-14 19:17:51

apply over previous patch


---

Attachment

I have uploaded a one-liner patch to deal with the `def copy` in `polynomial_element_generic` that got missed out. All doctests pass, both on sage.math and on my machine, so let's get this one in.


---

Comment by mvngu created at 2009-07-18 18:07:49

Resolution: fixed


---

Comment by mvngu created at 2009-07-18 18:07:49

Merged both patches.


---

Comment by kcrisman created at 2009-09-15 15:20:48

Just an FYI to those involved on this ticket: there may be a new ticket coming to put in deprecation warnings for these.  See the discussion at #6521.
