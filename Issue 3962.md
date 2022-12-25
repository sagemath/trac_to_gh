# Issue 3962: Error in converting vector to SR

archive/issues_003962.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: a=(QQ^3).subspace([[1,0,1]])\nsage: b=a.basis()[0]\nsage: b.change_ring(SR)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/grout/sage/devel/sage-main/sage/modules/<ipython console> in <module>()\n\n/home/grout/sage/devel/sage-main/sage/modules/free_module_element.pyx in sage.modules.free_module_element.FreeModuleElement.change_ring (sage/modules/free_module_element.c:3583)()\n    407         if P.base_ring() is R:\n    408             return self\n--> 409         return P.change_ring(R)(self)\n    410\n    411     def additive_order(self):\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in change_ring(self, R)\n   4406             return M.span_of_basis(B)\n   4407         else:\n-> 4408             return M.span(B)\n   4409\n   4410     def coordinate_vector(self, v, check=True):\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in span(self, gens, base_ring, check, already_echelonized)\n   2571         if base_ring is None or base_ring == self.base_ring():\n   2572             return FreeModule_submodule_field(\n-> 2573                 self.ambient_module(), gens=gens, check=check, already_echelonized=already_echelonized)\n   2574         else:\n   2575             try:\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in __init__(self, ambient, gens, check, already_echelonized)\n   4857             raise TypeError, \"Argument gens (= %s) must be a list, tuple, or sequence.\"%gens\n   4858         FreeModule_submodule_with_basis_field.__init__(self, ambient, basis=gens, check=check,\n-> 4859             echelonize=not already_echelonized, already_echelonized=already_echelonized)\n   4860\n   4861     def _repr_(self):\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in __init__(self, ambient, basis, check, echelonize, echelonized_basis, already_echelonized)\n   4683         FreeModule_submodule_with_basis_pid.__init__(\n   4684             self, ambient, basis=basis, check=check, echelonize=echelonize,\n-> 4685             echelonized_basis=echelonized_basis, already_echelonized=already_echelonized)\n   4686\n   4687     def _repr_(self):\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in __init__(self, ambient, basis, check, echelonize, echelonized_basis, already_echelonized)\n   3745\n   3746         if echelonize and not already_echelonized:\n-> 3747             basis = self._echelonized_basis(ambient, basis)\n   3748\n   3749         FreeModule_generic.__init__(self, R, rank=len(basis), degree=ambient.degree(), sparse=ambient.is_sparse())\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/modules/free_module.py in _echelonized_basis(self, ambient, basis)\n   4794         E = A.echelon_form()\n   4795         # Return the first rank rows (i.e., the nonzero rows).\n-> 4796         return E.rows()[:E.rank()]\n   4797\n   4798     def is_ambient(self):\n\nTypeError: slice indices must be integers or None or have an __index__ method\n```\n\n\nAttached patch fixes this problem\n\nIssue created by migration from https://trac.sagemath.org/ticket/3962\n\n",
    "created_at": "2008-08-26T21:08:18Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Error in converting vector to SR",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3962",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein


```
sage: a=(QQ^3).subspace([[1,0,1]])
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

Issue created by migration from https://trac.sagemath.org/ticket/3962





---

archive/issue_comments_028400.json:
```json
{
    "body": "I've attached a patch which replaces the first one and fixes the problem by adding an __index__ method for SymbolicConstants.",
    "created_at": "2008-08-29T01:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28400",
    "user": "https://github.com/mwhansen"
}
```

I've attached a patch which replaces the first one and fixes the problem by adding an __index__ method for SymbolicConstants.



---

archive/issue_comments_028401.json:
```json
{
    "body": "mhansen's patch does indeed correct the issue and is much more general, so positive review for his patch.  Doctests in the freemodule directory pass.",
    "created_at": "2008-08-29T04:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28401",
    "user": "https://github.com/jasongrout"
}
```

mhansen's patch does indeed correct the issue and is much more general, so positive review for his patch.  Doctests in the freemodule directory pass.



---

archive/issue_comments_028402.json:
```json
{
    "body": "This patch causes a doctest failure:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2$ ./sage -t -long devel/sage/sage/structure/element.pyx\nsage -t -long devel/sage/sage/structure/element.pyx         \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/tmp/element.py\", line 1458:\n    sage: 2r**(SR(2)-1-1r)\nExpected:\n    Traceback (most recent call last):\n    ...\n    NotImplementedError: non-integral exponents not supported\nGot:\n    1\n**********************************************************************\n1 items had failures:\n   1 of  15 in __main__.example_60\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/tmp/.doctest_element.py\n         [6.1 s]\nexit code: 1024\n```\n",
    "created_at": "2008-08-29T06:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28402",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch causes a doctest failure:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2$ ./sage -t -long devel/sage/sage/structure/element.pyx
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

archive/issue_comments_028403.json:
```json
{
    "body": "huh, this means that something that used to not work (but should have) now works, so a doctest passes where it used to give an error.\n\nI'd say this is a sign of the success of this patch.  Change the doctest so that the result is what it should be!",
    "created_at": "2008-10-02T02:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28403",
    "user": "https://github.com/jasongrout"
}
```

huh, this means that something that used to not work (but should have) now works, so a doctest passes where it used to give an error.

I'd say this is a sign of the success of this patch.  Change the doctest so that the result is what it should be!



---

archive/issue_comments_028404.json:
```json
{
    "body": "With the doctest fixed, giving this a positive review.",
    "created_at": "2008-10-02T02:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28404",
    "user": "https://github.com/jasongrout"
}
```

With the doctest fixed, giving this a positive review.



---

archive/issue_comments_028405.json:
```json
{
    "body": "So the last two patches should be applied.  I haven't tested the last patch, but it's a simple doctest fix, so what could go wrong? :)",
    "created_at": "2008-10-02T02:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28405",
    "user": "https://github.com/jasongrout"
}
```

So the last two patches should be applied.  I haven't tested the last patch, but it's a simple doctest fix, so what could go wrong? :)



---

archive/issue_comments_028406.json:
```json
{
    "body": "Replying to [comment:7 jason]:\n> So the last two patches should be applied.  I haven't tested the last patch, but it's a simple doctest fix, so what could go wrong? :)\n\nMike Hansen had some reservations, so let's wait until he signs off on it.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-02T02:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28406",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:7 jason]:
> So the last two patches should be applied.  I haven't tested the last patch, but it's a simple doctest fix, so what could go wrong? :)

Mike Hansen had some reservations, so let's wait until he signs off on it.

Cheers,

Michael



---

archive/issue_comments_028407.json:
```json
{
    "body": "Okay, there is a problem.  Since __index__ just converts self to an int, it rounds 1/2 to zero, etc.  So we get 2^(SR(1/2)) = 1.\n\nChanging the __index__ method to return int(Integer(self)) fixes the problem.",
    "created_at": "2008-10-02T03:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28407",
    "user": "https://github.com/jasongrout"
}
```

Okay, there is a problem.  Since __index__ just converts self to an int, it rounds 1/2 to zero, etc.  So we get 2^(SR(1/2)) = 1.

Changing the __index__ method to return int(Integer(self)) fixes the problem.



---

archive/issue_comments_028408.json:
```json
{
    "body": "Attachment [trac_3962-3.patch](tarball://root/attachments/some-uuid/ticket3962/trac_3962-3.patch) by @jasongrout created at 2008-10-02 03:45:46\n\nApply trac_3962-3.patch only.  It incorporates both an updated __index__ method and the necessary doctest fixes and additions.",
    "created_at": "2008-10-02T03:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28408",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_3962-3.patch](tarball://root/attachments/some-uuid/ticket3962/trac_3962-3.patch) by @jasongrout created at 2008-10-02 03:45:46

Apply trac_3962-3.patch only.  It incorporates both an updated __index__ method and the necessary doctest fixes and additions.



---

archive/issue_comments_028409.json:
```json
{
    "body": "Adding the `__index__` method is the right thing to do. Works well and applies cleanly to 3.1.3.",
    "created_at": "2008-10-14T17:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28409",
    "user": "https://github.com/robertwb"
}
```

Adding the `__index__` method is the right thing to do. Works well and applies cleanly to 3.1.3.



---

archive/issue_comments_028410.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T15:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28410",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004190.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-10-18T15:11:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3962#event-4190"
}
```



---

archive/issue_comments_028411.json:
```json
{
    "body": "Merged trac_3962-3.patch in Sage 3.2.alpha0",
    "created_at": "2008-10-18T15:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3962#issuecomment-28411",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_3962-3.patch in Sage 3.2.alpha0
