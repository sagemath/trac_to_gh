# Issue 3962: Error in converting vector to SR

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-08-26 21:08:18

Assignee: was


```
sage: a=(QQ^3).subspace([This is the Trac macro *1,0,1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,0,1-macro))
sage: b=a.basis()[0]
sage: b.change_ring(SR)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/modules/<ipython console> in <module>()

/home/grout/sage/devel/sage-main/sage/modules/free_module_element.pyx in sage.modules.free_module_element.FreeModuleElement.change_ring (sage/modules/free_module_element.c:3583)()
    407         if P.base_ring() is R:
    408             return self
--> 409         return P.change_ring(R)(self)
    410
    411     def additive_order(self):

/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in change_ring(self, R)
   4406             return M.span_of_basis(B)
   4407         else:
-> 4408             return M.span(B)
   4409
   4410     def coordinate_vector(self, v, check=True):

/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in span(self, gens, base_ring, check, already_echelonized)
   2571         if base_ring is None or base_ring == self.base_ring():
   2572             return FreeModule_submodule_field(
-> 2573                 self.ambient_module(), gens=gens, check=check, already_echelonized=already_echelonized)
   2574         else:
   2575             try:

/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in __init__(self, ambient, gens, check, already_echelonized)
   4857             raise TypeError, "Argument gens (= %s) must be a list, tuple, or sequence."%gens
   4858         FreeModule_submodule_with_basis_field.__init__(self, ambient, basis=gens, check=check,
-> 4859             echelonize=not already_echelonized, already_echelonized=already_echelonized)
   4860
   4861     def _repr_(self):

/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in __init__(self, ambient, basis, check, echelonize, echelonized_basis, already_echelonized)
   4683         FreeModule_submodule_with_basis_pid.__init__(
   4684             self, ambient, basis=basis, check=check, echelonize=echelonize,
-> 4685             echelonized_basis=echelonized_basis, already_echelonized=already_echelonized)
   4686
   4687     def _repr_(self):

/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in __init__(self, ambient, basis, check, echelonize, echelonized_basis, already_echelonized)
   3745
   3746         if echelonize and not already_echelonized:
-> 3747             basis = self._echelonized_basis(ambient, basis)
   3748
   3749         FreeModule_generic.__init__(self, R, rank=len(basis), degree=ambient.degree(), sparse=ambient.is_sparse())

/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in _echelonized_basis(self, ambient, basis)
   4794         E = A.echelon_form()
   4795         # Return the first rank rows (i.e., the nonzero rows).
-> 4796         return E.rows()[:E.rank()]
   4797
   4798     def is_ambient(self):

TypeError: slice indices must be integers or None or have an __index__ method
```


Attached patch fixes this problem


---

Comment by mhansen created at 2008-08-29 01:28:22

I've attached a patch which replaces the first one and fixes the problem by adding an __index__ method for SymbolicConstants.


---

Comment by jason created at 2008-08-29 04:30:28

mhansen's patch does indeed correct the issue and is much more general, so positive review for his patch.  Doctests in the freemodule directory pass.


---

Comment by mabshoff created at 2008-08-29 06:28:47

This patch causes a doctest failure:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2$ ./sage -t -long devel/sage/sage/structure/element.pyx
sage -t -long devel/sage/sage/structure/element.pyx         
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/tmp/element.py", line 1458:
    sage: 2r**(SR(2)-1-1r)
Expected:
    Traceback (most recent call last):
    ...
    NotImplementedError: non-integral exponents not supported
Got:
    1
**********************************************************************
1 items had failures:
   1 of  15 in __main__.example_60
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/tmp/.doctest_element.py
         [6.1 s]
exit code: 1024
```



---

Comment by jason created at 2008-10-02 02:48:52

huh, this means that something that used to not work (but should have) now works, so a doctest passes where it used to give an error.

I'd say this is a sign of the success of this patch.  Change the doctest so that the result is what it should be!


---

Comment by jason created at 2008-10-02 02:49:48

With the doctest fixed, giving this a positive review.


---

Comment by jason created at 2008-10-02 02:50:26

So the last two patches should be applied.  I haven't tested the last patch, but it's a simple doctest fix, so what could go wrong? :)


---

Comment by mabshoff created at 2008-10-02 02:59:10

Replying to [comment:7 jason]:
> So the last two patches should be applied.  I haven't tested the last patch, but it's a simple doctest fix, so what could go wrong? :)

Mike Hansen had some reservations, so let's wait until he signs off on it.

Cheers,

Michael


---

Comment by jason created at 2008-10-02 03:32:53

Okay, there is a problem.  Since __index__ just converts self to an int, it rounds 1/2 to zero, etc.  So we get 2^(SR(1/2)) = 1.

Changing the __index__ method to return int(Integer(self)) fixes the problem.


---

Attachment

Apply trac_3962-3.patch only.  It incorporates both an updated __index__ method and the necessary doctest fixes and additions.


---

Comment by robertwb created at 2008-10-14 17:50:16

Adding the `__index__` method is the right thing to do. Works well and applies cleanly to 3.1.3.


---

Comment by mabshoff created at 2008-10-18 15:11:05

Resolution: fixed


---

Comment by mabshoff created at 2008-10-18 15:11:05

Merged trac_3962-3.patch in Sage 3.2.alpha0
