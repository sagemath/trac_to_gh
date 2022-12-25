# Issue 2487: [with patch, positive review] remove unused/broken p-adic morphism.pyx

archive/issues_002487.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nThis file does not compile with cython currently but is in the tree.  It is currently disabled in setup.py and should be removed or fixed.  This is a significant priority as it makes the development of efficient(parallel) build systems problematic and wastes space, especially for files which have not been touched in ages. Code that does not build should not be in the main repository.\n\n```\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\nfrom sage.rings.rational cimport Rational\n\nfrom sage.rings.padics.padic_fixed_mod_element cimport pAdicFixedModElement\nfrom sage.rings.padics.padic_capped_absolute_element cimport pAdicCappedAbsoluteElement\nfrom sage.rings.padics.padic_capped_relative_element cimport pAdicCappedRelativeElement\nfrom sage.rings.padics.eisenstein_fixed_mod_element cimport EisensteinFixedModElement\n^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:13:0: 'sage.rings.padics.eisenstein_fixed_mod_element.pxd' not found\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\nfrom sage.rings.rational cimport Rational\n\nfrom sage.rings.padics.padic_fixed_mod_element cimport pAdicFixedModElement\nfrom sage.rings.padics.padic_capped_absolute_element cimport pAdicCappedAbsoluteElement\nfrom sage.rings.padics.padic_capped_relative_element cimport pAdicCappedRelativeElement\nfrom sage.rings.padics.eisenstein_fixed_mod_element cimport EisensteinFixedModElement\n                                                           ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:13:60: 'EisensteinFixedModElement' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\nfrom sage.rings.padics.padic_fixed_mod_element cimport pAdicFixedModElement\nfrom sage.rings.padics.padic_capped_absolute_element cimport pAdicCappedAbsoluteElement\nfrom sage.rings.padics.padic_capped_relative_element cimport pAdicCappedRelativeElement\nfrom sage.rings.padics.eisenstein_fixed_mod_element cimport EisensteinFixedModElement\nfrom sage.rings.padics.unramified_fixed_mod_element cimport UnramifiedFixedModElement\n^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:14:0: 'sage.rings.padics.unramified_fixed_mod_element.pxd' not found\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\nfrom sage.rings.padics.padic_fixed_mod_element cimport pAdicFixedModElement\nfrom sage.rings.padics.padic_capped_absolute_element cimport pAdicCappedAbsoluteElement\nfrom sage.rings.padics.padic_capped_relative_element cimport pAdicCappedRelativeElement\nfrom sage.rings.padics.eisenstein_fixed_mod_element cimport EisensteinFixedModElement\nfrom sage.rings.padics.unramified_fixed_mod_element cimport UnramifiedFixedModElement\n                                                           ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:14:60: 'UnramifiedFixedModElement' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\nfrom sage.rings.padics.padic_capped_relative_element cimport pAdicCappedRelativeElement\nfrom sage.rings.padics.eisenstein_fixed_mod_element cimport EisensteinFixedModElement\nfrom sage.rings.padics.unramified_fixed_mod_element cimport UnramifiedFixedModElement\n\nfrom sage.rings.padics.pow_computer cimport PowComputer_class\nfrom sage.rings.padics.pow_computer_ext cimport PowComputer_ZZ_pX\n                                               ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:17:48: 'PowComputer_ZZ_pX' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans._parent = parent\n    ans.prime_pow = <PowComputer_class>parent.prime_pow\n    mpz_init(ans.unit)\n    return ans\n\ncdef EisensteinFixedModElement make_new_EisFM(parent):\n    ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:49:5: 'EisensteinFixedModElement' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans._parent = parent\n    ans.prime_pow = <PowComputer_class>parent.prime_pow\n    mpz_init(ans.unit)\n    return ans\n\ncdef EisensteinFixedModElement make_new_EisFM(parent):\n    ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:49:5: 'EisensteinFixedModElement' is not a type identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans._parent = parent\n    ans.prime_pow = ppow\n    ZZ_pX_construct(&ans.value)\n    return ans\n\ncdef UnramifiedFixedModElement make_new_UnrFM(parent):\n    ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:58:5: 'UnramifiedFixedModElement' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans._parent = parent\n    ans.prime_pow = ppow\n    ZZ_pX_construct(&ans.value)\n    return ans\n\ncdef UnramifiedFixedModElement make_new_UnrFM(parent):\n    ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:58:5: 'UnramifiedFixedModElement' is not a type identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans.prime_pow = <PowComputer_class>parent.prime_pow\n    mpz_init(ans.unit)\n    return ans\n\ncdef EisensteinFixedModElement make_new_EisFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:50:9: 'PowComputer_ZZ_pX' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans.prime_pow = <PowComputer_class>parent.prime_pow\n    mpz_init(ans.unit)\n    return ans\n\ncdef EisensteinFixedModElement make_new_EisFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:50:9: 'PowComputer_ZZ_pX' is not a type identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    return ans\n\ncdef EisensteinFixedModElement make_new_EisFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n    ppow.restore_top_context()\n    cdef EisensteinFixedModElement ans = PY_NEW(EisensteinFixedModElement)\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:52:9: 'EisensteinFixedModElement' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    return ans\n\ncdef EisensteinFixedModElement make_new_EisFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n    ppow.restore_top_context()\n    cdef EisensteinFixedModElement ans = PY_NEW(EisensteinFixedModElement)\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:52:9: 'EisensteinFixedModElement' is not a type identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans.prime_pow = <PowComputer_class>parent.prime_pow\n    mpz_init(ans.unit)\n    return ans\n\ncdef EisensteinFixedModElement make_new_EisFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n                                  ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:50:35: 'PowComputer_ZZ_pX' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans.prime_pow = <PowComputer_class>parent.prime_pow\n    mpz_init(ans.unit)\n    return ans\n\ncdef EisensteinFixedModElement make_new_EisFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n                                  ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:50:35: 'PowComputer_ZZ_pX' is not a type identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    return ans\n\ncdef EisensteinFixedModElement make_new_EisFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n    ppow.restore_top_context()\n    cdef EisensteinFixedModElement ans = PY_NEW(EisensteinFixedModElement)\n                                                                        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:52:73: undeclared name not builtin: EisensteinFixedModElement\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans.prime_pow = ppow\n    ZZ_pX_construct(&ans.value)\n    return ans\n\ncdef UnramifiedFixedModElement make_new_UnrFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:59:9: 'PowComputer_ZZ_pX' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans.prime_pow = ppow\n    ZZ_pX_construct(&ans.value)\n    return ans\n\ncdef UnramifiedFixedModElement make_new_UnrFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:59:9: 'PowComputer_ZZ_pX' is not a type identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    return ans\n\ncdef UnramifiedFixedModElement make_new_UnrFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n    ppow.restore_top_context()\n    cdef UnramifiedFixedModElement ans = PY_NEW(UnramifiedFixedModElement)\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:61:9: 'UnramifiedFixedModElement' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    return ans\n\ncdef UnramifiedFixedModElement make_new_UnrFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n    ppow.restore_top_context()\n    cdef UnramifiedFixedModElement ans = PY_NEW(UnramifiedFixedModElement)\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:61:9: 'UnramifiedFixedModElement' is not a type identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans.prime_pow = ppow\n    ZZ_pX_construct(&ans.value)\n    return ans\n\ncdef UnramifiedFixedModElement make_new_UnrFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n                                  ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:59:35: 'PowComputer_ZZ_pX' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ans.prime_pow = ppow\n    ZZ_pX_construct(&ans.value)\n    return ans\n\ncdef UnramifiedFixedModElement make_new_UnrFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n                                  ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:59:35: 'PowComputer_ZZ_pX' is not a type identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    return ans\n\ncdef UnramifiedFixedModElement make_new_UnrFM(parent):\n    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow\n    ppow.restore_top_context()\n    cdef UnramifiedFixedModElement ans = PY_NEW(UnramifiedFixedModElement)\n                                                                        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:61:73: undeclared name not builtin: UnramifiedFixedModElement\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\n    cdef Element _call_c_impl(self, Element x):\n        \"\"\"\n        x must be an Integer.\n        \"\"\"\n        cdef EisensteinFixedModElement ans = make_new_EisFM(self._codomain)\n            ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:365:13: 'EisensteinFixedModElement' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\n    cdef Element _call_c_impl(self, Element x):\n        \"\"\"\n        x must be an Integer.\n        \"\"\"\n        cdef EisensteinFixedModElement ans = make_new_EisFM(self._codomain)\n            ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:365:13: 'EisensteinFixedModElement' is not a type identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\n    cdef Element _call_c_impl(self, Element x):\n        \"\"\"\n        x must be an Integer.\n        \"\"\"\n        cdef UnramifiedFixedModElement ans = make_new_UnrFM(self._codomain)\n            ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:379:13: 'UnramifiedFixedModElement' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\n    cdef Element _call_c_impl(self, Element x):\n        \"\"\"\n        x must be an Integer.\n        \"\"\"\n        cdef UnramifiedFixedModElement ans = make_new_UnrFM(self._codomain)\n            ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:379:13: 'UnramifiedFixedModElement' is not a type identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\n    cdef Element _call_c_impl(self, Element x):\n        \"\"\"\n        x must be a pAdicFixedModElement\n        \"\"\"\n        cdef EisensteinFixedModElement ans = make_new_EisFM(self._codomain)\n            ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:395:13: 'EisensteinFixedModElement' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\n    cdef Element _call_c_impl(self, Element x):\n        \"\"\"\n        x must be a pAdicFixedModElement\n        \"\"\"\n        cdef EisensteinFixedModElement ans = make_new_EisFM(self._codomain)\n            ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:395:13: 'EisensteinFixedModElement' is not a type identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\n    cdef Element _call_c_impl(self, Element x):\n        \"\"\"\n        x must be a pAdicFixedModElement\n        \"\"\"\n        cdef EisensteinFixedModElement ans = make_new_UnrFM(self._codomain)\n            ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:411:13: 'EisensteinFixedModElement' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\n    cdef Element _call_c_impl(self, Element x):\n        \"\"\"\n        x must be a pAdicFixedModElement\n        \"\"\"\n        cdef EisensteinFixedModElement ans = make_new_UnrFM(self._codomain)\n            ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:411:13: 'EisensteinFixedModElement' is not a type identifier\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o morphism.c morphism.pyx\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2487\n\n",
    "closed_at": "2008-03-14T22:34:53Z",
    "created_at": "2008-03-12T09:30:51Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, positive review] remove unused/broken p-adic morphism.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2487",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

This file does not compile with cython currently but is in the tree.  It is currently disabled in setup.py and should be removed or fixed.  This is a significant priority as it makes the development of efficient(parallel) build systems problematic and wastes space, especially for files which have not been touched in ages. Code that does not build should not be in the main repository.

```
Error converting Pyrex file to C:
------------------------------------------------------------
...
from sage.rings.rational cimport Rational

from sage.rings.padics.padic_fixed_mod_element cimport pAdicFixedModElement
from sage.rings.padics.padic_capped_absolute_element cimport pAdicCappedAbsoluteElement
from sage.rings.padics.padic_capped_relative_element cimport pAdicCappedRelativeElement
from sage.rings.padics.eisenstein_fixed_mod_element cimport EisensteinFixedModElement
^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:13:0: 'sage.rings.padics.eisenstein_fixed_mod_element.pxd' not found

Error converting Pyrex file to C:
------------------------------------------------------------
...
from sage.rings.rational cimport Rational

from sage.rings.padics.padic_fixed_mod_element cimport pAdicFixedModElement
from sage.rings.padics.padic_capped_absolute_element cimport pAdicCappedAbsoluteElement
from sage.rings.padics.padic_capped_relative_element cimport pAdicCappedRelativeElement
from sage.rings.padics.eisenstein_fixed_mod_element cimport EisensteinFixedModElement
                                                           ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:13:60: 'EisensteinFixedModElement' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...

from sage.rings.padics.padic_fixed_mod_element cimport pAdicFixedModElement
from sage.rings.padics.padic_capped_absolute_element cimport pAdicCappedAbsoluteElement
from sage.rings.padics.padic_capped_relative_element cimport pAdicCappedRelativeElement
from sage.rings.padics.eisenstein_fixed_mod_element cimport EisensteinFixedModElement
from sage.rings.padics.unramified_fixed_mod_element cimport UnramifiedFixedModElement
^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:14:0: 'sage.rings.padics.unramified_fixed_mod_element.pxd' not found

Error converting Pyrex file to C:
------------------------------------------------------------
...

from sage.rings.padics.padic_fixed_mod_element cimport pAdicFixedModElement
from sage.rings.padics.padic_capped_absolute_element cimport pAdicCappedAbsoluteElement
from sage.rings.padics.padic_capped_relative_element cimport pAdicCappedRelativeElement
from sage.rings.padics.eisenstein_fixed_mod_element cimport EisensteinFixedModElement
from sage.rings.padics.unramified_fixed_mod_element cimport UnramifiedFixedModElement
                                                           ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:14:60: 'UnramifiedFixedModElement' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...
from sage.rings.padics.padic_capped_relative_element cimport pAdicCappedRelativeElement
from sage.rings.padics.eisenstein_fixed_mod_element cimport EisensteinFixedModElement
from sage.rings.padics.unramified_fixed_mod_element cimport UnramifiedFixedModElement

from sage.rings.padics.pow_computer cimport PowComputer_class
from sage.rings.padics.pow_computer_ext cimport PowComputer_ZZ_pX
                                               ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:17:48: 'PowComputer_ZZ_pX' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans._parent = parent
    ans.prime_pow = <PowComputer_class>parent.prime_pow
    mpz_init(ans.unit)
    return ans

cdef EisensteinFixedModElement make_new_EisFM(parent):
    ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:49:5: 'EisensteinFixedModElement' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans._parent = parent
    ans.prime_pow = <PowComputer_class>parent.prime_pow
    mpz_init(ans.unit)
    return ans

cdef EisensteinFixedModElement make_new_EisFM(parent):
    ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:49:5: 'EisensteinFixedModElement' is not a type identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans._parent = parent
    ans.prime_pow = ppow
    ZZ_pX_construct(&ans.value)
    return ans

cdef UnramifiedFixedModElement make_new_UnrFM(parent):
    ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:58:5: 'UnramifiedFixedModElement' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans._parent = parent
    ans.prime_pow = ppow
    ZZ_pX_construct(&ans.value)
    return ans

cdef UnramifiedFixedModElement make_new_UnrFM(parent):
    ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:58:5: 'UnramifiedFixedModElement' is not a type identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans.prime_pow = <PowComputer_class>parent.prime_pow
    mpz_init(ans.unit)
    return ans

cdef EisensteinFixedModElement make_new_EisFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:50:9: 'PowComputer_ZZ_pX' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans.prime_pow = <PowComputer_class>parent.prime_pow
    mpz_init(ans.unit)
    return ans

cdef EisensteinFixedModElement make_new_EisFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:50:9: 'PowComputer_ZZ_pX' is not a type identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...
    return ans

cdef EisensteinFixedModElement make_new_EisFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
    ppow.restore_top_context()
    cdef EisensteinFixedModElement ans = PY_NEW(EisensteinFixedModElement)
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:52:9: 'EisensteinFixedModElement' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...
    return ans

cdef EisensteinFixedModElement make_new_EisFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
    ppow.restore_top_context()
    cdef EisensteinFixedModElement ans = PY_NEW(EisensteinFixedModElement)
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:52:9: 'EisensteinFixedModElement' is not a type identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans.prime_pow = <PowComputer_class>parent.prime_pow
    mpz_init(ans.unit)
    return ans

cdef EisensteinFixedModElement make_new_EisFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
                                  ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:50:35: 'PowComputer_ZZ_pX' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans.prime_pow = <PowComputer_class>parent.prime_pow
    mpz_init(ans.unit)
    return ans

cdef EisensteinFixedModElement make_new_EisFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
                                  ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:50:35: 'PowComputer_ZZ_pX' is not a type identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...
    return ans

cdef EisensteinFixedModElement make_new_EisFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
    ppow.restore_top_context()
    cdef EisensteinFixedModElement ans = PY_NEW(EisensteinFixedModElement)
                                                                        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:52:73: undeclared name not builtin: EisensteinFixedModElement

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans.prime_pow = ppow
    ZZ_pX_construct(&ans.value)
    return ans

cdef UnramifiedFixedModElement make_new_UnrFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:59:9: 'PowComputer_ZZ_pX' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans.prime_pow = ppow
    ZZ_pX_construct(&ans.value)
    return ans

cdef UnramifiedFixedModElement make_new_UnrFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:59:9: 'PowComputer_ZZ_pX' is not a type identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...
    return ans

cdef UnramifiedFixedModElement make_new_UnrFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
    ppow.restore_top_context()
    cdef UnramifiedFixedModElement ans = PY_NEW(UnramifiedFixedModElement)
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:61:9: 'UnramifiedFixedModElement' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...
    return ans

cdef UnramifiedFixedModElement make_new_UnrFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
    ppow.restore_top_context()
    cdef UnramifiedFixedModElement ans = PY_NEW(UnramifiedFixedModElement)
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:61:9: 'UnramifiedFixedModElement' is not a type identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans.prime_pow = ppow
    ZZ_pX_construct(&ans.value)
    return ans

cdef UnramifiedFixedModElement make_new_UnrFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
                                  ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:59:35: 'PowComputer_ZZ_pX' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ans.prime_pow = ppow
    ZZ_pX_construct(&ans.value)
    return ans

cdef UnramifiedFixedModElement make_new_UnrFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
                                  ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:59:35: 'PowComputer_ZZ_pX' is not a type identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...
    return ans

cdef UnramifiedFixedModElement make_new_UnrFM(parent):
    cdef PowComputer_ZZ_pX ppow = <PowComputer_ZZ_pX>parent.prime_pow
    ppow.restore_top_context()
    cdef UnramifiedFixedModElement ans = PY_NEW(UnramifiedFixedModElement)
                                                                        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:61:73: undeclared name not builtin: UnramifiedFixedModElement

Error converting Pyrex file to C:
------------------------------------------------------------
...

    cdef Element _call_c_impl(self, Element x):
        """
        x must be an Integer.
        """
        cdef EisensteinFixedModElement ans = make_new_EisFM(self._codomain)
            ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:365:13: 'EisensteinFixedModElement' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...

    cdef Element _call_c_impl(self, Element x):
        """
        x must be an Integer.
        """
        cdef EisensteinFixedModElement ans = make_new_EisFM(self._codomain)
            ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:365:13: 'EisensteinFixedModElement' is not a type identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...

    cdef Element _call_c_impl(self, Element x):
        """
        x must be an Integer.
        """
        cdef UnramifiedFixedModElement ans = make_new_UnrFM(self._codomain)
            ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:379:13: 'UnramifiedFixedModElement' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...

    cdef Element _call_c_impl(self, Element x):
        """
        x must be an Integer.
        """
        cdef UnramifiedFixedModElement ans = make_new_UnrFM(self._codomain)
            ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:379:13: 'UnramifiedFixedModElement' is not a type identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...

    cdef Element _call_c_impl(self, Element x):
        """
        x must be a pAdicFixedModElement
        """
        cdef EisensteinFixedModElement ans = make_new_EisFM(self._codomain)
            ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:395:13: 'EisensteinFixedModElement' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...

    cdef Element _call_c_impl(self, Element x):
        """
        x must be a pAdicFixedModElement
        """
        cdef EisensteinFixedModElement ans = make_new_EisFM(self._codomain)
            ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:395:13: 'EisensteinFixedModElement' is not a type identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...

    cdef Element _call_c_impl(self, Element x):
        """
        x must be a pAdicFixedModElement
        """
        cdef EisensteinFixedModElement ans = make_new_UnrFM(self._codomain)
            ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:411:13: 'EisensteinFixedModElement' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...

    cdef Element _call_c_impl(self, Element x):
        """
        x must be a pAdicFixedModElement
        """
        cdef EisensteinFixedModElement ans = make_new_UnrFM(self._codomain)
            ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/padics/morphism.pyx:411:13: 'EisensteinFixedModElement' is not a type identifier


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o morphism.c morphism.pyx
```

Issue created by migration from https://trac.sagemath.org/ticket/2487





---

archive/issue_comments_016818.json:
```json
{
    "body": "Attachment [trac_2487.patch](tarball://root/attachments/some-uuid/ticket2487/trac_2487.patch) by @garyfurnish created at 2008-03-13 01:58:05",
    "created_at": "2008-03-13T01:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2487#issuecomment-16818",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_2487.patch](tarball://root/attachments/some-uuid/ticket2487/trac_2487.patch) by @garyfurnish created at 2008-03-13 01:58:05



---

archive/issue_comments_016819.json:
```json
{
    "body": "Changing assignee from @malb to @garyfurnish.",
    "created_at": "2008-03-13T01:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2487#issuecomment-16819",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @malb to @garyfurnish.



---

archive/issue_comments_016820.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-13T01:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2487#issuecomment-16820",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016821.json:
```json
{
    "body": "`sage -ba` and a `-testall -long` works after applying this patch. I would suggest contacting the authors of the various files we remove \"just in case\".\n\nCheers,\n\nMichael",
    "created_at": "2008-03-13T07:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2487#issuecomment-16821",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

`sage -ba` and a `-testall -long` works after applying this patch. I would suggest contacting the authors of the various files we remove "just in case".

Cheers,

Michael



---

archive/issue_comments_016822.json:
```json
{
    "body": "```\n[23:00] <mabshoff> wstein: you are fine with the code removal by gfurnish?\n[23:00] <mabshoff> Then I will apply those patches now. \n[23:00] <wstein> yes\n```",
    "created_at": "2008-03-14T22:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2487#issuecomment-16822",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

```
[23:00] <mabshoff> wstein: you are fine with the code removal by gfurnish?
[23:00] <mabshoff> Then I will apply those patches now. 
[23:00] <wstein> yes
```



---

archive/issue_comments_016823.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T22:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2487#issuecomment-16823",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005865.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-14T22:34:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2487",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2487#event-5865"
}
```



---

archive/issue_comments_016824.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T22:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2487#issuecomment-16824",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
