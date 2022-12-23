# Issue 5133: improve the coverage of ext/multi_modular.pyx from an abysmal 0% to something more respectable

archive/issues_005133.json:
```json
{
    "body": "Assignee: was\n\n\n```\nwstein@sage:~/build/sage-3.2.3/devel/sage/sage/ext$ sage -coverage multi_modular.pyx\n----------------------------------------------------------------------\nmulti_modular.pyx\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE multi_modular.pyx: 0% (0 of 15)\n\nMissing documentation:\n         * _extend_moduli_to_height(self, height):\n         * _extend_moduli(self, count):\n         * precomputation_list(self):\n         * partial_product(self, n):\n         * prod(self):\n         * list(self):\n         * __len__(self):\n         * __iter__(self):\n         * __getitem__(self, ix):\n         * __repr__(self):\n         * next_prime(self):\n         * replace_prime(self, ix):\n\n\nMissing doctests:\n         * __init__(self, height):\n         * _extend_moduli_to_count(self, int count):\n         * crt(self, b):\n\n----------------------------------------------------------------------\n\nwstein@sage:~/build/sage-3.2.3/devel/sage/sage/ext$ \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5133\n\n",
    "created_at": "2009-01-30T01:10:20Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "improve the coverage of ext/multi_modular.pyx from an abysmal 0% to something more respectable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5133",
    "user": "was"
}
```
Assignee: was


```
wstein@sage:~/build/sage-3.2.3/devel/sage/sage/ext$ sage -coverage multi_modular.pyx
----------------------------------------------------------------------
multi_modular.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE multi_modular.pyx: 0% (0 of 15)

Missing documentation:
         * _extend_moduli_to_height(self, height):
         * _extend_moduli(self, count):
         * precomputation_list(self):
         * partial_product(self, n):
         * prod(self):
         * list(self):
         * __len__(self):
         * __iter__(self):
         * __getitem__(self, ix):
         * __repr__(self):
         * next_prime(self):
         * replace_prime(self, ix):


Missing doctests:
         * __init__(self, height):
         * _extend_moduli_to_count(self, int count):
         * crt(self, b):

----------------------------------------------------------------------

wstein@sage:~/build/sage-3.2.3/devel/sage/sage/ext$ 
```


Issue created by migration from https://trac.sagemath.org/ticket/5133





---

archive/issue_comments_039244.json:
```json
{
    "body": "add doctests and fix memory management in sage.ext.multi_modular",
    "created_at": "2009-06-27T14:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39244",
    "user": "burcin"
}
```

add doctests and fix memory management in sage.ext.multi_modular



---

archive/issue_comments_039245.json:
```json
{
    "body": "Changing assignee from was to burcin.",
    "created_at": "2009-06-27T14:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39245",
    "user": "burcin"
}
```

Changing assignee from was to burcin.



---

archive/issue_comments_039246.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-27T14:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39246",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039247.json:
```json
{
    "body": "Attachment\n\nattachment:trac_5133-multi_modular_tests.patch adds doctests and fixes some possible segfaults by reorganizing the memory allocations in `sage.ext.multi_modular`. Changes introduced by the patch are:\n\n* 100% coverage\n* refactor memory management\n* use random primes\n* set upper/lower bounds for moduli on initialization",
    "created_at": "2009-06-27T14:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39247",
    "user": "burcin"
}
```

Attachment

attachment:trac_5133-multi_modular_tests.patch adds doctests and fixes some possible segfaults by reorganizing the memory allocations in `sage.ext.multi_modular`. Changes introduced by the patch are:

* 100% coverage
* refactor memory management
* use random primes
* set upper/lower bounds for moduli on initialization



---

archive/issue_comments_039248.json:
```json
{
    "body": "**Review**\n\n* typo: `l_bound` -> `u_bound` in docstring\n* the string representation is quite unusual, not sure if that's desired.\n* `isinstance(val, list)` should allow more types `isinstance(val, (list,tuple,GeneratorType))`\n* Why is it okay to use `proof=False` for random integers, because they are so small anyway? That should be added as a comment.\n* `__cmp__` wants you to return -1,0,1 and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html\n* `INPUT::` -> `INPUT:`, it doesn't get two : because the following block is not literal\n* patch applies cleanly against 4.1\n* doctest failures:\n  {{{\n       sage -t  devel/sage/sage/modular/modsym/heilbronn.pyx # 1 doctests failed\n       sage -t  devel/sage/sage/modular/modsym/subspace.py # 12 doctests failed\n       sage -t  devel/sage/sage/modular/modsym/space.py # 9 doctests failed\n       sage -t  devel/sage/sage/modular/modform/eisenstein_submodule.py # 2 doctests failed\n       sage -t  devel/sage/sage/modular/modform/space.py # 3 doctests failed\n       sage -t  devel/sage/sage/modular/hecke/degenmap.py # 1 doctests failed\n       sage -t  devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 5 doctests failed\n       sage -t  devel/sage/sage/modular/modsym/ambient.py # 3 doctests failed\n       sage -t  devel/sage/sage/modular/hecke/element.py # 1 doctests failed\n       sage -t  devel/sage/sage/modular/hecke/hecke_operator.py # 1 doctests failed\n       sage -t  devel/sage/sage/modular/abvar/homology.py # 4 doctests failed\n       sage -t  devel/sage/sage/modular/abvar/morphism.py # 1 doctests failed\n       sage -t  devel/sage/sage/modular/hecke/module.py # 3 doctests failed\n       sage -t  devel/sage/sage/modular/abvar/torsion_subgroup.py # 4 doctests failed\n       sage -t  devel/sage/sage/modular/hecke/submodule.py # 4 doctests failed\n       sage -t  devel/sage/sage/modular/abvar/abvar.py # 10 doctests failed\n       sage -t  devel/sage/sage/modular/modform/element.py # 1 doctests failed\n       sage -t  devel/sage/sage/modular/abvar/homspace.py # 4 doctests failed\n       sage -t  devel/sage/sage/combinat/symmetric_group_representations.py # 1 doctests failed\n       sage -t  devel/sage/sage/geometry/lattice_polytope.py # 15 doctests failed\n       sage -t  devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 12 doctests failed\n       sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 6 doctests failed\n       sage -t  devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 4 doctests failed\n  }}}",
    "created_at": "2009-07-16T12:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39248",
    "user": "malb"
}
```

**Review**

* typo: `l_bound` -> `u_bound` in docstring
* the string representation is quite unusual, not sure if that's desired.
* `isinstance(val, list)` should allow more types `isinstance(val, (list,tuple,GeneratorType))`
* Why is it okay to use `proof=False` for random integers, because they are so small anyway? That should be added as a comment.
* `__cmp__` wants you to return -1,0,1 and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html
* `INPUT::` -> `INPUT:`, it doesn't get two : because the following block is not literal
* patch applies cleanly against 4.1
* doctest failures:
  {{{
       sage -t  devel/sage/sage/modular/modsym/heilbronn.pyx # 1 doctests failed
       sage -t  devel/sage/sage/modular/modsym/subspace.py # 12 doctests failed
       sage -t  devel/sage/sage/modular/modsym/space.py # 9 doctests failed
       sage -t  devel/sage/sage/modular/modform/eisenstein_submodule.py # 2 doctests failed
       sage -t  devel/sage/sage/modular/modform/space.py # 3 doctests failed
       sage -t  devel/sage/sage/modular/hecke/degenmap.py # 1 doctests failed
       sage -t  devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 5 doctests failed
       sage -t  devel/sage/sage/modular/modsym/ambient.py # 3 doctests failed
       sage -t  devel/sage/sage/modular/hecke/element.py # 1 doctests failed
       sage -t  devel/sage/sage/modular/hecke/hecke_operator.py # 1 doctests failed
       sage -t  devel/sage/sage/modular/abvar/homology.py # 4 doctests failed
       sage -t  devel/sage/sage/modular/abvar/morphism.py # 1 doctests failed
       sage -t  devel/sage/sage/modular/hecke/module.py # 3 doctests failed
       sage -t  devel/sage/sage/modular/abvar/torsion_subgroup.py # 4 doctests failed
       sage -t  devel/sage/sage/modular/hecke/submodule.py # 4 doctests failed
       sage -t  devel/sage/sage/modular/abvar/abvar.py # 10 doctests failed
       sage -t  devel/sage/sage/modular/modform/element.py # 1 doctests failed
       sage -t  devel/sage/sage/modular/abvar/homspace.py # 4 doctests failed
       sage -t  devel/sage/sage/combinat/symmetric_group_representations.py # 1 doctests failed
       sage -t  devel/sage/sage/geometry/lattice_polytope.py # 15 doctests failed
       sage -t  devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 12 doctests failed
       sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 6 doctests failed
       sage -t  devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 4 doctests failed
  }}}



---

archive/issue_comments_039249.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n\n>  * typo: `l_bound` -> `u_bound` in docstring\n\nFixed.\n\n>  * the string representation is quite unusual, not sure if that's desired.\n\nChanged it to:\n\n\n```\nsage: from sage.ext.multi_modular import MultiModularBasis_base\nsage: mm = MultiModularBasis_base([3, 5, 7]); mm\nMultiModularBasis with moduli [3, 5, 7]\n```\n\n\n>  * `isinstance(val, list)` should allow more types `isinstance(val, (list,tuple,GeneratorType))`\n\nDone.\n\n>  * Why is it okay to use `proof=False` for random integers, because they are so small anyway? That should be added as a comment.\n\nI'd forgotten that I put that in. Good catch. I removed that argument, so we use the global flag now.\n\n>  * `__cmp__` wants you to return -1,0,1 and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html\n\nFixed. Who would compare these things anyway? :)\n\n>  * `INPUT::` -> `INPUT:`, it doesn't get two : because the following block is not literal\n\nFixed.\n\n>  * patch applies cleanly against 4.1\n\n>  * doctest failures:\n\nDoh! I only doctested the `sage/matrix` directory. Apparently the only user of `MultiModularBasis`, namely `matrix_integer_dense.pyx` didn't have doctests for it. Now it does.",
    "created_at": "2009-07-18T15:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39249",
    "user": "burcin"
}
```

Replying to [comment:2 malb]:

>  * typo: `l_bound` -> `u_bound` in docstring

Fixed.

>  * the string representation is quite unusual, not sure if that's desired.

Changed it to:


```
sage: from sage.ext.multi_modular import MultiModularBasis_base
sage: mm = MultiModularBasis_base([3, 5, 7]); mm
MultiModularBasis with moduli [3, 5, 7]
```


>  * `isinstance(val, list)` should allow more types `isinstance(val, (list,tuple,GeneratorType))`

Done.

>  * Why is it okay to use `proof=False` for random integers, because they are so small anyway? That should be added as a comment.

I'd forgotten that I put that in. Good catch. I removed that argument, so we use the global flag now.

>  * `__cmp__` wants you to return -1,0,1 and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html

Fixed. Who would compare these things anyway? :)

>  * `INPUT::` -> `INPUT:`, it doesn't get two : because the following block is not literal

Fixed.

>  * patch applies cleanly against 4.1

>  * doctest failures:

Doh! I only doctested the `sage/matrix` directory. Apparently the only user of `MultiModularBasis`, namely `matrix_integer_dense.pyx` didn't have doctests for it. Now it does.



---

archive/issue_comments_039250.json:
```json
{
    "body": "Attachment\n\nsecond try, apply only this one",
    "created_at": "2009-07-18T15:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39250",
    "user": "burcin"
}
```

Attachment

second try, apply only this one



---

archive/issue_comments_039251.json:
```json
{
    "body": "all tests pass, issues were addressed.",
    "created_at": "2009-07-19T22:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39251",
    "user": "malb"
}
```

all tests pass, issues were addressed.



---

archive/issue_comments_039252.json:
```json
{
    "body": "rebased to depend on #6529",
    "created_at": "2009-07-20T14:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39252",
    "user": "mvngu"
}
```

rebased to depend on #6529



---

archive/issue_comments_039253.json:
```json
{
    "body": "Attachment\n\nI got a hunk failure when applying `trac_5133-multi_modular_tests-take2.patch`:\n\n```\n[mvngu@sage sage-exp]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5133/trac_5133-multi_modular_tests-take2.patch\nadding trac_5133-multi_modular_tests-take2.patch to series file\n[mvngu@sage sage-exp]$ hg qpush -a\napplying trac_5133-multi_modular_tests-take2.patch\npatching file sage/rings/arith.py\nHunk #2 FAILED at 914\n1 out of 4 hunks FAILED -- saving rejects to file sage/rings/arith.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac_5133-multi_modular_tests-take2.patch\n```\n\nHere's the hunk that failed:\n\n```\n--- arith.py                                                                    \n+++ arith.py                                                                    \n@@ -915,6 +915,9 @@\n        the function uses a pseudo-primality test, which is much faster for     \n        really big numbers but does not provide a proof of primality. If        \n        None, uses the global default (see sage.structure.proof)                \n+                                                                               \n+    - ``lbound`` - an integer >= 2                                             \n+      lower bound for the chosen primes                                        \n                                                                                \n                                                                                \n     EXAMPLES::\n```\n\nThis is because I previously applied the patches at #6529. The failure has been manually resolved so the docstring of `random_prime` in `sage/rings/arith.py` now reads:\n\n```\n    Returns a random prime p between `lbound` and n (i.e. `lbound <= p <= n`).  \n    The returned prime is chosen uniformly at random from the set of prime      \n    numbers less than or equal to n.                                            \n                                                                                \n    INPUT:                                                                      \n                                                                                \n                                                                                \n    -  ``n`` - an integer >= 2.                                                 \n                                                                                \n    -  ``proof`` - bool or None (default: None) If False, the function uses a   \n       pseudo-primality test, which is much faster for really big numbers but   \n       does not provide a proof of primality. If None, uses the global default  \n       (see :mod:`sage.structure.proof.proof`)                                  \n                                                                                \n    - ``lbound`` - an integer >= 2                                              \n      lower bound for the chosen primes\n```\n\nThe patch `trac_5133-take2-rebased.patch` is a rebase of `trac_5133-multi_modular_tests-take2.patch` that depends on first applying the patches at #6529.",
    "created_at": "2009-07-20T14:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39253",
    "user": "mvngu"
}
```

Attachment

I got a hunk failure when applying `trac_5133-multi_modular_tests-take2.patch`:

```
[mvngu@sage sage-exp]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5133/trac_5133-multi_modular_tests-take2.patch
adding trac_5133-multi_modular_tests-take2.patch to series file
[mvngu@sage sage-exp]$ hg qpush -a
applying trac_5133-multi_modular_tests-take2.patch
patching file sage/rings/arith.py
Hunk #2 FAILED at 914
1 out of 4 hunks FAILED -- saving rejects to file sage/rings/arith.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_5133-multi_modular_tests-take2.patch
```

Here's the hunk that failed:

```
--- arith.py                                                                    
+++ arith.py                                                                    
@@ -915,6 +915,9 @@
        the function uses a pseudo-primality test, which is much faster for     
        really big numbers but does not provide a proof of primality. If        
        None, uses the global default (see sage.structure.proof)                
+                                                                               
+    - ``lbound`` - an integer >= 2                                             
+      lower bound for the chosen primes                                        
                                                                                
                                                                                
     EXAMPLES::
```

This is because I previously applied the patches at #6529. The failure has been manually resolved so the docstring of `random_prime` in `sage/rings/arith.py` now reads:

```
    Returns a random prime p between `lbound` and n (i.e. `lbound <= p <= n`).  
    The returned prime is chosen uniformly at random from the set of prime      
    numbers less than or equal to n.                                            
                                                                                
    INPUT:                                                                      
                                                                                
                                                                                
    -  ``n`` - an integer >= 2.                                                 
                                                                                
    -  ``proof`` - bool or None (default: None) If False, the function uses a   
       pseudo-primality test, which is much faster for really big numbers but   
       does not provide a proof of primality. If None, uses the global default  
       (see :mod:`sage.structure.proof.proof`)                                  
                                                                                
    - ``lbound`` - an integer >= 2                                              
      lower bound for the chosen primes
```

The patch `trac_5133-take2-rebased.patch` is a rebase of `trac_5133-multi_modular_tests-take2.patch` that depends on first applying the patches at #6529.



---

archive/issue_comments_039254.json:
```json
{
    "body": "Oops... can I get someone to do a quick review of the rebased patch?",
    "created_at": "2009-07-20T14:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39254",
    "user": "mvngu"
}
```

Oops... can I get someone to do a quick review of the rebased patch?



---

archive/issue_comments_039255.json:
```json
{
    "body": "changed error message in rebased patch",
    "created_at": "2009-07-20T16:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39255",
    "user": "burcin"
}
```

changed error message in rebased patch



---

archive/issue_comments_039256.json:
```json
{
    "body": "Attachment\n\nI changed the error message `random_prime()` gives when `lower_bound` is `< n`.\n\nPositive review for the rebased patch.",
    "created_at": "2009-07-20T16:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39256",
    "user": "burcin"
}
```

Attachment

I changed the error message `random_prime()` gives when `lower_bound` is `< n`.

Positive review for the rebased patch.



---

archive/issue_comments_039257.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-20T17:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39257",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_039258.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-07-20T17:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39258",
    "user": "mvngu"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_039259.json:
```json
{
    "body": "This will have to wait for Sage 4.1.1.alpha1. Apparently, I accidentally closed this as being merged in 4.1.1.alpha0.",
    "created_at": "2009-07-20T17:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39259",
    "user": "mvngu"
}
```

This will have to wait for Sage 4.1.1.alpha1. Apparently, I accidentally closed this as being merged in 4.1.1.alpha0.



---

archive/issue_comments_039260.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-07-20T17:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39260",
    "user": "mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_039261.json:
```json
{
    "body": "Merged `trac_5133-take2-rebased2.patch`.",
    "created_at": "2009-07-23T02:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39261",
    "user": "mvngu"
}
```

Merged `trac_5133-take2-rebased2.patch`.



---

archive/issue_comments_039262.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T02:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5133#issuecomment-39262",
    "user": "mvngu"
}
```

Resolution: fixed
