# Issue 1232: bug in modular symbols over GF(2)

archive/issues_001232.json:
```json
{
    "body": "Assignee: @williamstein\n\nRunning\n\n```\nModularSymbols(1,6,0,GF(2)).simple_factors()\n```\n\nresults in\n\n```\n---------------------------------------------------------------------------\n<type 'exceptions.AssertionError'>        Traceback (most recent call last)\n\n/home/ghitza/sage/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/modular/modsym/space.py in simple_factors(self)\n    996         ASSUMPTION: self is a module over the anemic Hecke algebra.\n    997         \"\"\"\n--> 998         return [S for S,_ in self.factorization()]\n    999 \n   1000     def star_eigenvalues(self):\n\n/opt/sage/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py in factorization(self)\n   1064         D = sage.structure.all.Factorization(D, cr=True)\n   1065         assert r == s, \"bug in factorization --  self has dimension %s, but sum of dimensions of factors is %s\\n%s\"%(\n-> 1066             r, s, D)\n   1067         self._factorization = D\n   1068         return self._factorization\n\n<type 'exceptions.AssertionError'>: bug in factorization --  self has dimension 2, but sum of dimensions of factors is 3\n(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 6 with sign 0 over Finite Field of size 2) * \n(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 6 with sign 0 over Finite Field of size 2) * \n(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 6 with sign 0 over Finite Field of size 2)\n```\n\nOutcome is similar for higher weights, e.g. for weight 100 I get \"self has dimension 33, but sum of dimensions of factors is 65\".\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1232\n\n",
    "created_at": "2007-11-21T03:49:42Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "bug in modular symbols over GF(2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1232",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

Running

```
ModularSymbols(1,6,0,GF(2)).simple_factors()
```

results in

```
---------------------------------------------------------------------------
<type 'exceptions.AssertionError'>        Traceback (most recent call last)

/home/ghitza/sage/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/modular/modsym/space.py in simple_factors(self)
    996         ASSUMPTION: self is a module over the anemic Hecke algebra.
    997         """
--> 998         return [S for S,_ in self.factorization()]
    999 
   1000     def star_eigenvalues(self):

/opt/sage/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py in factorization(self)
   1064         D = sage.structure.all.Factorization(D, cr=True)
   1065         assert r == s, "bug in factorization --  self has dimension %s, but sum of dimensions of factors is %s\n%s"%(
-> 1066             r, s, D)
   1067         self._factorization = D
   1068         return self._factorization

<type 'exceptions.AssertionError'>: bug in factorization --  self has dimension 2, but sum of dimensions of factors is 3
(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 6 with sign 0 over Finite Field of size 2) * 
(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 6 with sign 0 over Finite Field of size 2) * 
(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 6 with sign 0 over Finite Field of size 2)
```

Outcome is similar for higher weights, e.g. for weight 100 I get "self has dimension 33, but sum of dimensions of factors is 65".


Issue created by migration from https://trac.sagemath.org/ticket/1232





---

archive/issue_events_003253.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-23T00:13:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1232",
    "milestone": "sage-2.8.14",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1232#event-3253"
}
```



---

archive/issue_comments_007650.json:
```json
{
    "body": "So the problem here is straightforward to find -- M.factorization() breaks up the cuspidal parts into +1 and -1 eigenspaces; since 1 == -1 mod 2, they all get counted twice (so that the dimension will always be 2*cuspidal part + eisenstein part). The fix is also easy -- if 2 == 0, don't add the minus part in. However, the question is whether the space is still simple in this case, because otherwise we're now producing wrong answers.",
    "created_at": "2007-12-02T11:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1232#issuecomment-7650",
    "user": "https://github.com/craigcitro"
}
```

So the problem here is straightforward to find -- M.factorization() breaks up the cuspidal parts into +1 and -1 eigenspaces; since 1 == -1 mod 2, they all get counted twice (so that the dimension will always be 2*cuspidal part + eisenstein part). The fix is also easy -- if 2 == 0, don't add the minus part in. However, the question is whether the space is still simple in this case, because otherwise we're now producing wrong answers.



---

archive/issue_comments_007651.json:
```json
{
    "body": "Attachment [trac_1232.patch](tarball://root/attachments/some-uuid/ticket1232/trac_1232.patch) by @craigcitro created at 2007-12-12 04:30:33",
    "created_at": "2007-12-12T04:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1232#issuecomment-7651",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_1232.patch](tarball://root/attachments/some-uuid/ticket1232/trac_1232.patch) by @craigcitro created at 2007-12-12 04:30:33



---

archive/issue_comments_007652.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2007-12-12T04:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1232#issuecomment-7652",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_007653.json:
```json
{
    "body": "Added a fix for this. The issue was what I mentioned above, namely the fact that +1 == -1 in characteristic 2. Alex Ghitza offered the following explanation of why this is a mathematically valid fix:\n\nHere's my line of thought:\n-- in Sage, \"simple\" means \"simple as a module over the anemic Hecke\nalgebra adjoined the star involution *\"\n-- in characteristic 2, the star involution is actually not an\ninvolution, but rather the identity map, and so \"simple\" should just\nmean \"simple as a module over the anemic Hecke algebra\", so synonymous\nto \"splittable_anemic\" in Sage terminology\n-- the factorization() aka simple_factors() function for modular\nsymbols uses the HeckeModule_free_module.decomposition() function,\nwhich implements an algorithm that breaks up the module as much as\npossible using the anemic Hecke algebra; therefore the resulting\nfactors are \"splittable_anemic\", and so \"simple\" (for char 2).\n\nThe attached patch fixes the problem, and adds a doctest or two.",
    "created_at": "2007-12-12T04:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1232#issuecomment-7653",
    "user": "https://github.com/craigcitro"
}
```

Added a fix for this. The issue was what I mentioned above, namely the fact that +1 == -1 in characteristic 2. Alex Ghitza offered the following explanation of why this is a mathematically valid fix:

Here's my line of thought:
-- in Sage, "simple" means "simple as a module over the anemic Hecke
algebra adjoined the star involution *"
-- in characteristic 2, the star involution is actually not an
involution, but rather the identity map, and so "simple" should just
mean "simple as a module over the anemic Hecke algebra", so synonymous
to "splittable_anemic" in Sage terminology
-- the factorization() aka simple_factors() function for modular
symbols uses the HeckeModule_free_module.decomposition() function,
which implements an algorithm that breaks up the module as much as
possible using the anemic Hecke algebra; therefore the resulting
factors are "splittable_anemic", and so "simple" (for char 2).

The attached patch fixes the problem, and adds a doctest or two.



---

archive/issue_comments_007654.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-12T04:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1232#issuecomment-7654",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007655.json:
```json
{
    "body": "This is good (ok and better than before).  Note however that in a lot of cases simple_factors still won't work (due to the algorithm not really being meant for GF(p) -- instead one should use decomposition):\n\n```\nsage: n = ModularSymbols(54,weight=2,base_ring=GF(2)); n\nModular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2\nsage: m =n.new_subspace()\nsage: n.simple_factors()\nTraceback (most recent call last):\n...\nAssertionError: bug in factorization --  self has dimension 19, but sum of dimensions of factors is 11\n(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 1 for Gamma_0(2) of weight 2 with sign 0 over Finite Field of size 2)^7 * \n(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 7 for Gamma_0(27) of weight 2 with sign 0 over Finite Field of size 2)^2 * \n(Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2)\nsage: m.simple_factors()\n[Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2, Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2]\nsage: f = n.decomposition(5)\nsage: f\n[\nModular Symbols subspace of dimension 4 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2,\nModular Symbols subspace of dimension 15 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2\n]\n```",
    "created_at": "2007-12-15T06:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1232#issuecomment-7655",
    "user": "https://github.com/williamstein"
}
```

This is good (ok and better than before).  Note however that in a lot of cases simple_factors still won't work (due to the algorithm not really being meant for GF(p) -- instead one should use decomposition):

```
sage: n = ModularSymbols(54,weight=2,base_ring=GF(2)); n
Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2
sage: m =n.new_subspace()
sage: n.simple_factors()
Traceback (most recent call last):
...
AssertionError: bug in factorization --  self has dimension 19, but sum of dimensions of factors is 11
(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 1 for Gamma_0(2) of weight 2 with sign 0 over Finite Field of size 2)^7 * 
(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 7 for Gamma_0(27) of weight 2 with sign 0 over Finite Field of size 2)^2 * 
(Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2)
sage: m.simple_factors()
[Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2, Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2]
sage: f = n.decomposition(5)
sage: f
[
Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2,
Modular Symbols subspace of dimension 15 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2
]
```



---

archive/issue_comments_007656.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T06:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1232#issuecomment-7656",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007657.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T06:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1232#issuecomment-7657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_events_003254.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T06:49:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1232",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1232#event-3254"
}
```
