# Issue 5642: Overconvergent modular forms for genus 0 primes

archive/issues_005642.json:
```json
{
    "body": "Assignee: davidloeffler\n\nI have written some code that computes approximations to the q-expansions of overconvergent p-adic modular forms of tame level 1, when p is one of the primes {2, 3, 5, 7, 13} (so X_0(p) has genus 0). See the notes of my talk at the Heilbronn Institute for background: \n\nhttp://www.dpmms.cam.ac.uk/~dl267/maths/lecturenotes/overconvergent_lecture.pdf.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5642\n\n",
    "created_at": "2009-03-30T09:50:20Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "title": "Overconvergent modular forms for genus 0 primes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5642",
    "user": "davidloeffler"
}
```
Assignee: davidloeffler

I have written some code that computes approximations to the q-expansions of overconvergent p-adic modular forms of tame level 1, when p is one of the primes {2, 3, 5, 7, 13} (so X_0(p) has genus 0). See the notes of my talk at the Heilbronn Institute for background: 

http://www.dpmms.cam.ac.uk/~dl267/maths/lecturenotes/overconvergent_lecture.pdf.

Issue created by migration from https://trac.sagemath.org/ticket/5642





---

archive/issue_comments_044065.json:
```json
{
    "body": "Attachment\n\npatch against 3.4.1.alpha0",
    "created_at": "2009-03-30T09:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5642#issuecomment-44065",
    "user": "davidloeffler"
}
```

Attachment

patch against 3.4.1.alpha0



---

archive/issue_comments_044066.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-30T09:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5642#issuecomment-44066",
    "user": "davidloeffler"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044067.json:
```json
{
    "body": "REFEREE REPORT:\n\n1. Could we rename `WeightSpace` to `pAdicWeightSpace`?  I say that only because Sage is so broad and in combinatorics/representation theory `WeightSpace` could have some completely different meaning.\n2. Could `WeightSpace?` give more useful documentation?   \n3. I'm very happy with how good `OverconvergentModularForms` docstring is, but there should be doctests that illustrate all of the options to the `OverconvergentModularForms` function. Right now the doctests don't at all test/illustrate `base_ring` or `prec`. \n4. Here's a bug. This was *literally* the first random thing I tried:\n\n```\nsage: M = OverconvergentModularForms(3, 0, 1/2)\nsage: w = M.weight()\nsage: w.Lvalue()\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/scratch/wstein/sage/temp/sage.math.washington.edu/30657/_scratch_wstein_sage_init_sage_0.py in <module>()\n\n/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/modular/overconvergent/weightspace.pyc in Lvalue(self)\n    457             return -self.chi.bernoulli(self.k)/self.k\n    458         if self.is_trivial():\n--> 459             return Infinity\n    460         else:\n    461             raise NotImplementedError, \"Don't know how to compute value of this L-function\"\n\nNameError: global name 'Infinity' is not defined\n```\n\n1. Continuing the above example, the second thing I tried also fails:\n\n```\nsage: w.base_extend(QQ)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n...\nAttributeError: 'WeightSpace_class' object has no attribute 'base_extend'\n```\n\n1. The third thing I tried gives nonsense.  Shouldn't w.base_ring() either raise an error, or return a ring?\n\n```\nsage: w.base_ring()\nsage: w.base_ring() is None\nTrue\n```\n\n1. Do you really want that I can just change the attribute k (the weight) of the p-adic Weight space like this?\n\n```\nsage: w.k = 10\nsage: w\n10\nsage: M.weight()   # that can't be good\n10\n```\n\n1. This is pretty weird:\n\n```\nsage: w.n()\ninit_coerce() for  <class 'sage.modular.overconvergent.weightspace.WeightSpace_class'>\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\nZeroDivisionError: hello\n```\n\n1. I'm unhappy that one_over_Lvalue() outputs a Python int.  I would rather get a Sage Integer or a Rational or p-adic or something.  \n\n```\nsage: w.one_over_Lvalue()\n0\nsage: type(w.one_over_Lvalue())\n<type 'int'>\n```\n\n\n1. This isn't good, and is why I would never ever expose attributes like this.  It's best to use self.__prime and make a method or use the Python \"properties\" protocol. \n\n```\nsage: w.prime = 6\nsage: w.prime\n6\nsage: w.parent()\nSpace of 3-adic weight-characters\n```\n\n\n1. Moving back to `M=OverconvergentModularForms(3, 0, 1/2)`, and going through some of the methods, the first one I try is broken.  I realize this is broken because a function in the abstract base class for Hecke modules assumes certain things and you wrote code that doesn't satisfy those assumption.  But we have to find a way to make this all work.   Half the functions in the abstract base class assume there is a function `M.hecke_matrix(n)` that works, so if you do `M.<tab>` and try things, you'll find a whole bunch of functions that don't work. \n\n```\nsage: M.hecke_polynomial(2)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n   1028         OUTPUT: a polynomial\n   1029         \"\"\"\n-> 1030         return self.hecke_operator(n).charpoly(var)\n   1031 \n   1032     def is_simple(self):\n\nTypeError: hecke_operator() takes exactly 3 arguments (2 given)\n```\n\n\n1. Here's another bug, which I realize is probably actually a bug in code I wrote long ago but it would be cool if you fixed it :-)\n\n```\nsage: M.zero_submodule()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/scratch/wstein/sage/temp/sage.math.washington.edu/30657/_scratch_wstein_sage_init_sage_0.py in <module>()\n\n/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/module.pyc in zero_submodule(self)\n   1248             Modular Forms subspace of dimension 0 of Modular Forms space of dimension 4 for Congruence Subgroup Gamma0(11) of weight 4 over Rational Field\n   1249         \"\"\"\n-> 1250         return self.submodule(self.free_module().zero_submodule(), check=False)\n   1251     \n   1252         \n\nAttributeError: 'PowerSeriesRing_over_field' object has no attribute 'zero_submodule'\n```\n\n1. That one can do this is *not* good, IMHO:\n\n```\nsage: M.q\nq\nsage: M.q = 10\nsage: M.q\n10\nsage: M=OverconvergentModularForms(3, 0, 1/2)\nsage: M.q\n10\n(so I restart -- there should be maybe a use_cache=False option to the constructor...)\n```\n\n1. This could be more graceful:\n\n```\nsage: M.list()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/scratch/wstein/sage/temp/sage.math.washington.edu/31166/_scratch_wstein_sage_init_sage_0.py in <module>()\n\n/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.list (sage/structure/parent.c:5211)()\n\n/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/structure/gens_py.pyc in abelian_iterator(M)\n     48 def abelian_iterator(M):\n     49     from sage.rings.all import infinity    \n---> 50     G = M.gens()\n     51     if len(G) == 0:\n     52         yield M(0)\n\n/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.gens (sage/structure/parent_gens.c:2749)()\n\nTypeError: an integer is required\n```\n\n1. This \"M.gsr\" thing is 100% totally cryptic and confusing, and again can easily lead to brokeness (same with M.qsr):\n\n```\nsage: M.gsr\nPower Series Ring in g over Rational Field\nsage: M.gsr = 10\n# badness\n```\n\n1. Here's another problem\n\n```\nsage: M.new_submodule()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/scratch/wstein/sage/temp/sage.math.washington.edu/31246/_scratch_wstein_sage_init_sage_0.py in <module>()\n\n/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/ambient_module.pyc in new_submodule(self, p)\n    538             f = 1\n    539         else:\n--> 540             f = eps.conductor()\n    541         if p == None:\n    542             D = arith.prime_divisors(N)\n\nAttributeError: 'AlgebraicWeight' object has no attribute 'conductor'\n```\n\n\n\nAnyway, as you can see, I hope you could take each of the main new objects that this code introduces, try each method, and fix the issues.   You can probably clean this all up pretty quickly.\n\nPlease don't take the above in too negative away.  This is frickin' *awesome* code, and I'm very very happy and excited to finally see a real implementation of overconvergent p-adic modular forms in Sage.  This is wonderful!",
    "created_at": "2009-03-31T05:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5642#issuecomment-44067",
    "user": "was"
}
```

REFEREE REPORT:

1. Could we rename `WeightSpace` to `pAdicWeightSpace`?  I say that only because Sage is so broad and in combinatorics/representation theory `WeightSpace` could have some completely different meaning.
2. Could `WeightSpace?` give more useful documentation?   
3. I'm very happy with how good `OverconvergentModularForms` docstring is, but there should be doctests that illustrate all of the options to the `OverconvergentModularForms` function. Right now the doctests don't at all test/illustrate `base_ring` or `prec`. 
4. Here's a bug. This was *literally* the first random thing I tried:

```
sage: M = OverconvergentModularForms(3, 0, 1/2)
sage: w = M.weight()
sage: w.Lvalue()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/scratch/wstein/sage/temp/sage.math.washington.edu/30657/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/modular/overconvergent/weightspace.pyc in Lvalue(self)
    457             return -self.chi.bernoulli(self.k)/self.k
    458         if self.is_trivial():
--> 459             return Infinity
    460         else:
    461             raise NotImplementedError, "Don't know how to compute value of this L-function"

NameError: global name 'Infinity' is not defined
```

1. Continuing the above example, the second thing I tried also fails:

```
sage: w.base_extend(QQ)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
AttributeError: 'WeightSpace_class' object has no attribute 'base_extend'
```

1. The third thing I tried gives nonsense.  Shouldn't w.base_ring() either raise an error, or return a ring?

```
sage: w.base_ring()
sage: w.base_ring() is None
True
```

1. Do you really want that I can just change the attribute k (the weight) of the p-adic Weight space like this?

```
sage: w.k = 10
sage: w
10
sage: M.weight()   # that can't be good
10
```

1. This is pretty weird:

```
sage: w.n()
init_coerce() for  <class 'sage.modular.overconvergent.weightspace.WeightSpace_class'>
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
ZeroDivisionError: hello
```

1. I'm unhappy that one_over_Lvalue() outputs a Python int.  I would rather get a Sage Integer or a Rational or p-adic or something.  

```
sage: w.one_over_Lvalue()
0
sage: type(w.one_over_Lvalue())
<type 'int'>
```


1. This isn't good, and is why I would never ever expose attributes like this.  It's best to use self.__prime and make a method or use the Python "properties" protocol. 

```
sage: w.prime = 6
sage: w.prime
6
sage: w.parent()
Space of 3-adic weight-characters
```


1. Moving back to `M=OverconvergentModularForms(3, 0, 1/2)`, and going through some of the methods, the first one I try is broken.  I realize this is broken because a function in the abstract base class for Hecke modules assumes certain things and you wrote code that doesn't satisfy those assumption.  But we have to find a way to make this all work.   Half the functions in the abstract base class assume there is a function `M.hecke_matrix(n)` that works, so if you do `M.<tab>` and try things, you'll find a whole bunch of functions that don't work. 

```
sage: M.hecke_polynomial(2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
   1028         OUTPUT: a polynomial
   1029         """
-> 1030         return self.hecke_operator(n).charpoly(var)
   1031 
   1032     def is_simple(self):

TypeError: hecke_operator() takes exactly 3 arguments (2 given)
```


1. Here's another bug, which I realize is probably actually a bug in code I wrote long ago but it would be cool if you fixed it :-)

```
sage: M.zero_submodule()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/scratch/wstein/sage/temp/sage.math.washington.edu/30657/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/module.pyc in zero_submodule(self)
   1248             Modular Forms subspace of dimension 0 of Modular Forms space of dimension 4 for Congruence Subgroup Gamma0(11) of weight 4 over Rational Field
   1249         """
-> 1250         return self.submodule(self.free_module().zero_submodule(), check=False)
   1251     
   1252         

AttributeError: 'PowerSeriesRing_over_field' object has no attribute 'zero_submodule'
```

1. That one can do this is *not* good, IMHO:

```
sage: M.q
q
sage: M.q = 10
sage: M.q
10
sage: M=OverconvergentModularForms(3, 0, 1/2)
sage: M.q
10
(so I restart -- there should be maybe a use_cache=False option to the constructor...)
```

1. This could be more graceful:

```
sage: M.list()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/scratch/wstein/sage/temp/sage.math.washington.edu/31166/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.list (sage/structure/parent.c:5211)()

/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/structure/gens_py.pyc in abelian_iterator(M)
     48 def abelian_iterator(M):
     49     from sage.rings.all import infinity    
---> 50     G = M.gens()
     51     if len(G) == 0:
     52         yield M(0)

/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.gens (sage/structure/parent_gens.c:2749)()

TypeError: an integer is required
```

1. This "M.gsr" thing is 100% totally cryptic and confusing, and again can easily lead to brokeness (same with M.qsr):

```
sage: M.gsr
Power Series Ring in g over Rational Field
sage: M.gsr = 10
# badness
```

1. Here's another problem

```
sage: M.new_submodule()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/scratch/wstein/sage/temp/sage.math.washington.edu/31246/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/ambient_module.pyc in new_submodule(self, p)
    538             f = 1
    539         else:
--> 540             f = eps.conductor()
    541         if p == None:
    542             D = arith.prime_divisors(N)

AttributeError: 'AlgebraicWeight' object has no attribute 'conductor'
```



Anyway, as you can see, I hope you could take each of the main new objects that this code introduces, try each method, and fix the issues.   You can probably clean this all up pretty quickly.

Please don't take the above in too negative away.  This is frickin' *awesome* code, and I'm very very happy and excited to finally see a real implementation of overconvergent p-adic modular forms in Sage.  This is wonderful!



---

archive/issue_comments_044068.json:
```json
{
    "body": "Most of these are plain stupidity on my part and I will fix them, and add doctests to prove that they are fixed. I will also hide some more attributes.",
    "created_at": "2009-03-31T07:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5642#issuecomment-44068",
    "user": "davidloeffler"
}
```

Most of these are plain stupidity on my part and I will fix them, and add doctests to prove that they are fixed. I will also hide some more attributes.



---

archive/issue_comments_044069.json:
```json
{
    "body": "Attachment\n\napply over previous patch",
    "created_at": "2009-04-01T14:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5642#issuecomment-44069",
    "user": "davidloeffler"
}
```

Attachment

apply over previous patch



---

archive/issue_comments_044070.json:
```json
{
    "body": "Here's a new version. Overconvergent spaces + elements now inherit from Module and ModuleElement, not HeckeModule and HeckeModuleElement, which is a pity, but leads to fewer meaningless inherited methods. I've also hidden lots of things away out of sight of the user, and improved the documentation somewhat.",
    "created_at": "2009-04-01T14:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5642#issuecomment-44070",
    "user": "davidloeffler"
}
```

Here's a new version. Overconvergent spaces + elements now inherit from Module and ModuleElement, not HeckeModule and HeckeModuleElement, which is a pity, but leads to fewer meaningless inherited methods. I've also hidden lots of things away out of sight of the user, and improved the documentation somewhat.



---

archive/issue_comments_044071.json:
```json
{
    "body": "OK, this is now very good.  Excellent! Thanks!!",
    "created_at": "2009-04-02T16:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5642#issuecomment-44071",
    "user": "was"
}
```

OK, this is now very good.  Excellent! Thanks!!



---

archive/issue_comments_044072.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-02T18:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5642#issuecomment-44072",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_comments_044073.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-02T18:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5642#issuecomment-44073",
    "user": "mabshoff"
}
```

Resolution: fixed
