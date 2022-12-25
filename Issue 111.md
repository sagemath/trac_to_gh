# Issue 111: def copy -- they should all be def __copy__

archive/issues_000111.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb @mwhansen\n\nThere are many instances of copy methods in SAGE.  They should all be __copy__, which\nis what gets called by the standard copy module (part of the standard Python library). \n\n\n```\nsage: search_sage('def copy')\n\nmatrix/sparse_matrix.py:    def copy(self):\nmodules/free_module_element.py:    def copy(self):\nplot/graph.py:    def copy(self, name):\nrings/finite_field_element.py:    def copy(self):\nrings/fraction_field_element.py:    def copy(self):\nrings/laurent_series_ring_element.py:    def copy(self):\nrings/padic.py:    def copy(self):\nrings/polynomial_element.py:    def copy(self):\nrings/polynomial_element.py:    def copy(self):\nrings/polynomial_element.py:    def copy(self):\nrings/polynomial_element.py:    def copy(self):\nrings/power_series_ring_element.py:    def copy(self):\nrings/power_series_ring_element.py:    def copy(self):\nrings/quotient_ring_element.py:    def copy(self):\nlibs/pari/functional.py:def copy(self): return pari(self).copy()\nmodular/modsym/manin_symbols.py:    def copy(self):\nserver/server1/server1.py:    def copyfile(self, source, outputfile): \nmatrix/dense_matrix_pyx.pyx:    def copy(self):\nmatrix/matrix_generic.pyx:    def copy(self):\nmatrix/matrix_integer_dense.pyx:    def copy(self):\nmatrix/matrix_modn_dense.pyx:    def copy(Matrix_modn_dense self):\nmatrix/matrix_modn_sparse.pyx:    def copy(self):\nmatrix/matrix_rational_dense.pyx:    def copy(self):\nmatrix/sparse_matrix_pyx.pyx:    def copy(self):\nmatrix/sparse_matrix_pyx.pyx:    def copy(self):\nmatrix/sparse_matrix_pyx.pyx:    def copy(self):\nrings/integer.pyx:    def copy(self):\nrings/integer_mod.pyx:    def copy(IntegerMod_gmp self):\nrings/integer_mod.pyx:    def copy(IntegerMod_int self):\nrings/integer_mod.pyx:    def copy(IntegerMod_int64 self):\nrings/mpc.pyx:    def copy(self):\nrings/polynomial_pyx.pyx:    def copy(self):\nrings/polynomial_pyx.pyx:    def copy(self):\nrings/rational.pyx:    def copy(self):\nrings/real_double.pyx:    def copy(self):\nrings/real_mpfr.pyx:    def copy(self):\nrings/sparse_poly.pyx:    def copy(self):\nrings/sparse_poly.pyx:    def copy(self):\nlibs/linbox/finite_field_givaro.pyx:    def copy(self):\nlibs/ntl/ntl.pyx:    def copy(self):\nlibs/ntl/ntl.pyx:    def copy(self):\nlibs/ntl/ntl.pyx:    def copy(ntl_GF2E self):\nlibs/pari/_py_pari_orig.pyx:    def copy(gen self):\nlibs/pari/gen.pyx:    def copy(gen self):\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/111\n\n",
    "created_at": "2006-10-05T06:24:07Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "def copy -- they should all be def __copy__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/111",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @robertwb @mwhansen

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


Issue created by migration from https://trac.sagemath.org/ticket/111





---

archive/issue_events_000115.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2006-10-05T08:07:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/111#event-115"
}
```



---

archive/issue_comments_000515.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-05T08:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-515",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000516.json:
```json
{
    "body": "Fixed for sage-1.4",
    "created_at": "2006-10-05T08:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-516",
    "user": "https://github.com/williamstein"
}
```

Fixed for sage-1.4



---

archive/issue_comments_000517.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2006-10-05T08:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-517",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_000518.json:
```json
{
    "body": "I reverted my changes in my local copy -- there were some nontrivial issues with make such a global change.",
    "created_at": "2006-10-05T08:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-518",
    "user": "https://github.com/williamstein"
}
```

I reverted my changes in my local copy -- there were some nontrivial issues with make such a global change.



---

archive/issue_comments_000519.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2006-10-05T08:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-519",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_000116.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2006-10-05T08:45:09Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/111#event-116"
}
```



---

archive/issue_comments_000520.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-01-13T02:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-520",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000521.json:
```json
{
    "body": "The number has decreased significantly:\n\n```\nlibs/ntl/ntl_ZZX.pyx:    def copy(self):\nlibs/ntl/ntl_ZZ_pEX.pyx:    def copy(self):\nlibs/ntl/ntl_ZZ_pX.pyx:    def copy(self):\nlibs/pari/gen.pyx:    def copy(gen self):\nmatrix/matrix0.pyx:    def copy(self):\nmodules/free_module_element.pyx:    def copy(self):\nrings/padics/padic_ZZ_pX_CA_element.pyx:    def copy(self):\nrings/padics/padic_ZZ_pX_CR_element.pyx:    def copy(self):\nrings/padics/padic_ZZ_pX_FM_element.pyx:    def copy(self):\nrings/padics/padic_capped_absolute_element.pyx:    def copy(pAdicCappedAbsoluteElement self):\nrings/padics/padic_capped_relative_element.pyx:    def copy(self):\nrings/padics/padic_fixed_mod_element.pyx:    def copy(self):\nrings/polynomial/polynomial_pyx.pyx:    def copy(self):\nrings/polynomial/polynomial_pyx.pyx:    def copy(self):\nrings/laurent_series_ring_element.pyx:    def copy(self):\nrings/power_series_poly.pyx:    def copy(self):\nrings/rational.pyx:    def copy(self):\nrings/sparse_poly.pyx:    def copy(self):\nrings/sparse_poly.pyx:    def copy(self):\n```\n\n\nIt would be nice if someone could take an axe to the remaining ones.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T21:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-521",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_000522.json:
```json
{
    "body": "In sage-4.1, I am seeing\n\n\n```\nlibs/pari/gen.pyx:1051:    def copy(gen self):\nlibs/ntl/ntl_ZZ_pEX.pyx:197:    def copy(self):\nlibs/ntl/ntl_ZZ_pX.pyx:189:    def copy(self):\nlibs/ntl/ntl_ZZX.pyx:152:    def copy(self):\ngraphs/graph.py:780:    def copy(self, implementation='networkx', sparse=None):\ncombinat/matrices/latin.py:321:    def copy(self):\nmatrix/matrix0.pyx:115:    def copy(self):\nmodular/modsym/manin_symbols.py:1667:    def copy(self):\nrings/laurent_series_ring_element.pyx:943:    def copy(self):\nrings/finite_field_givaro.pyx:1118:    cdef FiniteField_givaro copy\nrings/finite_field_element.py:396:    def copy(self):\nrings/fraction_field_element.pyx:179:    def copy(self):\nrings/power_series_poly.pyx:575:    def copy(self):\nrings/rational.pyx:558:    def copy(self):\nrings/padics/padic_fixed_mod_element.pyx:661:    def copy(self):\nrings/padics/padic_ZZ_pX_CA_element.pyx:1567:    def copy(self):\nrings/padics/padic_ZZ_pX_CR_element.pyx:2193:    def copy(self):\nrings/padics/padic_ZZ_pX_FM_element.pyx:840:    def copy(self):\nrings/padics/padic_capped_relative_element.pyx:1453:    def copy(self):\nrings/padics/padic_capped_absolute_element.pyx:810:    def copy(pAdicCappedAbsoluteElement self):\nrings/polynomial/polynomial_element_generic.py:866:    def copy(self):\nrings/polynomial/padics/polynomial_padic_capped_relative_dense.py:726:    def copy(self):\ngroups/perm_gps/partn_ref/refinement_python.pyx:145:    def copy(self):\nmodules/free_module_element.pyx:513:    def copy(self):\ndatabases/database.py:575:    def copy(self):\ndatabases/database.py:1003:    def copy(self):\ndatabases/database.py:1546:    def copy(self):\n```\n",
    "created_at": "2009-07-12T01:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-522",
    "user": "https://github.com/aghitza"
}
```

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

archive/issue_comments_000523.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2009-07-13T10:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-523",
    "user": "https://github.com/aghitza"
}
```

Changing status from reopened to new.



---

archive/issue_comments_000524.json:
```json
{
    "body": "Doing all of these in one shot is pretty nasty.  I've attached a patch that fixes most of the instances, and I have opened two follow-up tickets: #6521 for matrix0.pyx and #6522 for graph.py.",
    "created_at": "2009-07-13T10:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-524",
    "user": "https://github.com/aghitza"
}
```

Doing all of these in one shot is pretty nasty.  I've attached a patch that fixes most of the instances, and I have opened two follow-up tickets: #6521 for matrix0.pyx and #6522 for graph.py.



---

archive/issue_comments_000525.json:
```json
{
    "body": "Changing assignee from @williamstein to @aghitza.",
    "created_at": "2009-07-13T10:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-525",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @aghitza.



---

archive/issue_comments_000526.json:
```json
{
    "body": "Attachment [trac_111.patch](tarball://root/attachments/some-uuid/ticket111/trac_111.patch) by @aghitza created at 2009-07-13 10:40:07",
    "created_at": "2009-07-13T10:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-526",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_111.patch](tarball://root/attachments/some-uuid/ticket111/trac_111.patch) by @aghitza created at 2009-07-13 10:40:07



---

archive/issue_comments_000527.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-13T10:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-527",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_000528.json:
```json
{
    "body": "Patch looks fine to me -- I am running doctests at the moment -- but it looks like you missed one in `sage/rings/polynomial/polynomial_element_generic.py`. I'll do a mini-patch and see if that breaks anything :-)",
    "created_at": "2009-07-14T16:59:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-528",
    "user": "https://github.com/loefflerd"
}
```

Patch looks fine to me -- I am running doctests at the moment -- but it looks like you missed one in `sage/rings/polynomial/polynomial_element_generic.py`. I'll do a mini-patch and see if that breaks anything :-)



---

archive/issue_comments_000529.json:
```json
{
    "body": "apply over previous patch",
    "created_at": "2009-07-14T19:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-529",
    "user": "https://github.com/loefflerd"
}
```

apply over previous patch



---

archive/issue_comments_000530.json:
```json
{
    "body": "Attachment [trac_111-reviewer.patch](tarball://root/attachments/some-uuid/ticket111/trac_111-reviewer.patch) by @loefflerd created at 2009-07-14 19:19:29\n\nI have uploaded a one-liner patch to deal with the `def copy` in `polynomial_element_generic` that got missed out. All doctests pass, both on sage.math and on my machine, so let's get this one in.",
    "created_at": "2009-07-14T19:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-530",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_111-reviewer.patch](tarball://root/attachments/some-uuid/ticket111/trac_111-reviewer.patch) by @loefflerd created at 2009-07-14 19:19:29

I have uploaded a one-liner patch to deal with the `def copy` in `polynomial_element_generic` that got missed out. All doctests pass, both on sage.math and on my machine, so let's get this one in.



---

archive/issue_comments_000531.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-18T18:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-531",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_000117.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-18T18:07:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/111#event-117"
}
```



---

archive/issue_comments_000532.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-07-18T18:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-532",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged both patches.



---

archive/issue_comments_000533.json:
```json
{
    "body": "Just an FYI to those involved on this ticket: there may be a new ticket coming to put in deprecation warnings for these.  See the discussion at #6521.",
    "created_at": "2009-09-15T15:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/111#issuecomment-533",
    "user": "https://github.com/kcrisman"
}
```

Just an FYI to those involved on this ticket: there may be a new ticket coming to put in deprecation warnings for these.  See the discussion at #6521.
