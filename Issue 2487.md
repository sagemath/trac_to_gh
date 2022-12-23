# Issue 2487: unused/broken p-adic morphism.pyx

Issue created by migration from https://trac.sagemath.org/ticket/2487

Original creator: gfurnish

Original creation time: 2008-03-12 09:30:51

Assignee: malb

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



---

Attachment


---

Comment by gfurnish created at 2008-03-13 01:58:30

Changing assignee from malb to gfurnish.


---

Comment by gfurnish created at 2008-03-13 01:58:30

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-13 07:48:50

`sage -ba` and a `-testall -long` works after applying this patch. I would suggest contacting the authors of the various files we remove "just in case".

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-14 22:28:53


```
[23:00] <mabshoff> wstein: you are fine with the code removal by gfurnish?
[23:00] <mabshoff> Then I will apply those patches now. 
[23:00] <wstein> yes
```



---

Comment by mabshoff created at 2008-03-14 22:34:53

Resolution: fixed


---

Comment by mabshoff created at 2008-03-14 22:34:53

Merged in Sage 2.10.4.alpha0
