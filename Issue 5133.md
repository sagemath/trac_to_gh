# Issue 5133: improve the coverage of ext/multi_modular.pyx from an abysmal 0% to something more respectable

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-30 01:10:20

Assignee: was


```
wstein`@`sage:~/build/sage-3.2.3/devel/sage/sage/ext$ sage -coverage multi_modular.pyx
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

wstein`@`sage:~/build/sage-3.2.3/devel/sage/sage/ext$ 
```



---

Comment by burcin created at 2009-06-27 14:32:50

add doctests and fix memory management in sage.ext.multi_modular


---

Comment by burcin created at 2009-06-27 14:37:21

Changing assignee from was to burcin.


---

Comment by burcin created at 2009-06-27 14:37:21

Changing status from new to assigned.


---

Attachment

attachment:trac_5133-multi_modular_tests.patch adds doctests and fixes some possible segfaults by reorganizing the memory allocations in `sage.ext.multi_modular`. Changes introduced by the patch are:

 * 100% coverage
 * refactor memory management
 * use random primes
 * set upper/lower bounds for moduli on initialization


---

Comment by malb created at 2009-07-16 12:46:57

*Review*

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

Comment by burcin created at 2009-07-18 15:48:45

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

Attachment

second try, apply only this one


---

Comment by malb created at 2009-07-19 22:30:50

all tests pass, issues were addressed.


---

Comment by mvngu created at 2009-07-20 14:20:44

rebased to depend on #6529


---

Attachment

I got a hunk failure when applying `trac_5133-multi_modular_tests-take2.patch`:

```
[mvngu`@`sage sage-exp]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5133/trac_5133-multi_modular_tests-take2.patch
adding trac_5133-multi_modular_tests-take2.patch to series file
[mvngu`@`sage sage-exp]$ hg qpush -a
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
`@``@` -915,6 +915,9 `@``@`
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

Comment by mvngu created at 2009-07-20 14:26:33

Oops... can I get someone to do a quick review of the rebased patch?


---

Comment by burcin created at 2009-07-20 16:39:15

changed error message in rebased patch


---

Attachment

I changed the error message `random_prime()` gives when `lower_bound` is `< n`.

Positive review for the rebased patch.


---

Comment by mvngu created at 2009-07-20 17:10:59

Resolution: fixed


---

Comment by mvngu created at 2009-07-20 17:36:28

Changing status from closed to reopened.


---

Comment by mvngu created at 2009-07-20 17:36:28

This will have to wait for Sage 4.1.1.alpha1. Apparently, I accidentally closed this as being merged in 4.1.1.alpha0.


---

Comment by mvngu created at 2009-07-20 17:36:28

Resolution changed from fixed to 


---

Comment by mvngu created at 2009-07-23 02:47:59

Merged `trac_5133-take2-rebased2.patch`.


---

Comment by mvngu created at 2009-07-23 02:47:59

Resolution: fixed
