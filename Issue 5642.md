# Issue 5642: Overconvergent modular forms for genus 0 primes

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-03-30 09:50:20

Assignee: davidloeffler

I have written some code that computes approximations to the q-expansions of overconvergent p-adic modular forms of tame level 1, when p is one of the primes {2, 3, 5, 7, 13} (so X_0(p) has genus 0). See the notes of my talk at the Heilbronn Institute for background: 

http://www.dpmms.cam.ac.uk/~dl267/maths/lecturenotes/overconvergent_lecture.pdf.


---

Attachment

patch against 3.4.1.alpha0


---

Comment by davidloeffler created at 2009-03-30 09:52:22

Changing status from new to assigned.


---

Comment by was created at 2009-03-31 05:03:11

REFEREE REPORT:

 1. Could we rename `WeightSpace` to `pAdicWeightSpace`?  I say that only because Sage is so broad and in combinatorics/representation theory `WeightSpace` could have some completely different meaning.
 1. Could `WeightSpace?` give more useful documentation?   
 1. I'm very happy with how good `OverconvergentModularForms` docstring is, but there should be doctests that illustrate all of the options to the `OverconvergentModularForms` function. Right now the doctests don't at all test/illustrate `base_ring` or `prec`. 
 1. Here's a bug. This was *literally* the first random thing I tried:

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

Comment by davidloeffler created at 2009-03-31 07:36:15

Most of these are plain stupidity on my part and I will fix them, and add doctests to prove that they are fixed. I will also hide some more attributes.


---

Attachment

apply over previous patch


---

Comment by davidloeffler created at 2009-04-01 14:21:59

Here's a new version. Overconvergent spaces + elements now inherit from Module and ModuleElement, not HeckeModule and HeckeModuleElement, which is a pity, but leads to fewer meaningless inherited methods. I've also hidden lots of things away out of sight of the user, and improved the documentation somewhat.


---

Comment by was created at 2009-04-02 16:52:54

OK, this is now very good.  Excellent! Thanks!!


---

Comment by mabshoff created at 2009-04-02 18:45:44

Merged both patches in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-02 18:45:44

Resolution: fixed
