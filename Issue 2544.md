# Issue 2544: modabvar -- rewrite of modular abelian varieties rewrite

Issue created by migration from https://trac.sagemath.org/ticket/2544

Original creator: was

Original creation time: 2008-03-16 08:51:56

Assignee: was

CC:  robertwb




---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by craigcitro created at 2008-03-18 07:47:37

(code depends on these patches)


---

Attachment

(code depends on these patches)


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment

The final patch is the attached file abvar.hg


---

Comment by was created at 2008-04-04 17:03:36

From CRAIG:

```
So I think I'm ready for this to get merged. I've played around with
just about all of the code, and I looked through the last 2-3 files
that I hadn't looked at much since Tucson. I can't say that I read
every line of everything, of course, but I feel pretty comfortable
with the code overall. There are lots of things I want to start
working on, of course, but none of them are defects -- they're all
enhancements.

I went ahead and reformatted one or two things, and added some long
doctests to the top of homspace.py. I feel like adding a 387th patch
to the ticket is silly, since you'll probably also have one or two
small touch-ups, so you'll probably just re-roll the bundle. I'm
attaching the patch to this email.

As long as you feel like the code you didn't write seems reasonable
enough, I feel like this is ready to get merged.
```



I've posted a new abvar.hg patch, which is the one that should be applied.


---

Comment by mabshoff created at 2008-04-04 17:12:24

Resolution: fixed


---

Attachment

Merged in Sage 3.0.alpha1 :)


---

Comment by mabshoff created at 2008-04-04 17:38:00

I am seeing one doctest failure:

```
sage -t -long devel/sage/sage/modular/abvar/abvar.py        
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/abvar.py", line 276:
    sage: cmp(J0(37), 5)
Expected:
    1
Got:
    -1
**********************************************************************
```


IIRC this compares just memory posititions, so it ought to be #random.

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-04 19:43:14

Fix doctest failure after William confirmed that this is the right fix


---

Attachment

rac_2544_doctest-failure__cmp__fix.patch fixes the issue.

Cheers,

Michael


---

Comment by mrennekamp created at 2017-03-22 01:01:52

Modular Abelian Varieties

Code at http://trac.sagemath.org/sage_trac/ticket/2544

Todo on Wednesday, March 19

9:00-12:00am

DONE (craig) 3: Hom(A,B) for A, B simple
DONE (robert) 3: Hom(A,B) in general
DONE (william) 2: cokernels of morphisms
DONE (william) 2: dual of A when A is maximal
DONE (william) images of abelian varieties and groups under morphisms. (2 hours)
DONE (william) intersections of finite groups
12:00am - 5am + airport:

plan for:
trim the paper
doctests
optimization
bug hunting

(craig) 2: norm equations (clean up patch) (1 hour)
5: minimal isogeny degree (3 hours)
intersection pairing.

(william) 3: dual isogeny when A,B both maximal
Todo on Tuesday, March 18

DONE (craig) 2: disc(End(A))
DONE (craig) 2: degeneracy maps
DONE (craig) 1: fix hecke operators
DONE (robert) 1: create newforms and abvars from label, where label is 389aG1, 389aGH[2,3], 389b, 389c, etc.
DONE (robert) 1: complementary isogeny (invert matrix and clear denom)
DONE (william) 2: quotient by abelian subvariety
DONE (william) 2: kernels of morphisms
DONE (william) 2: projection (only when 'maximal')
Todo on March 16

DONE (craig) Newforms issue:
   sage: f = CuspForms(37).newforms('a')[0]
   sage: f.coefficients(10)
   ------------------------------------
   <type 'exceptions.TypeError'>             Traceback (most recent call last)
   sage: f.coefficients([2..10])
   ------------------------------------
   <type 'exceptions.AttributeError'>        Traceback (most recent call last)
   ...
   <type 'exceptions.AttributeError'>: 'Newform' object has no attribute '_compute'
DONE (william) This is completely wrong (the modabvar function on modular symbols assumes it's ambient!):
   sage: m = ModularSymbols(37)[1]
   sage: m.modular_abelian_variety()
   Jacobian of the modular curve associated to the congruence subgroup Gamma0(37)
DONE (william) Move functions out of abvar_modsym_factor into abvar and delete that file.
DONE (william) Torsion subgroups:
(already done) Refactor base class
(done) Get implementation to work with defining data being (lattice, abvar); compute generators.
(done) Quotients by finite subgroup
DONE (craig) Implement f.number() for f a newform.
DONE-ish (craig) Compute the Hecke algebra image in End(A) and find a good clean way to represent for Hecke stable. New object that is a subring of End(A). Have methods like R.index_in(S).
DONE (craig) abelian varieties should cache their ambient modular abelian variety
Todo on Monday, March 17

(craig) Compute End(A):
for simple AfAf (DONE)
in general.
disc of it.
ideals and annihilators
order in a ring of integers (for A simple)
given a ring R in EndAlg(A) where every element has integral charpoly, find an isogenous abelian variety with End(A) = R.
explicit isomorphism between HeckeAlgebra sitting in End(A) and a commutative ring
base extension of End(A)
(craig) Degeneracy maps
(william) Decomposition:
three types:
ungrouped as simple abvars (default)
groups abvars
over End(A)
deprecate hecke_decomposition
(DONE) label function
create from label
(william/craig) Morphisms:
Kernels
Cokernels
(william/craig) Isogenies:
Complementary -- invert matrix, clear denom.
Dual
(william) Intersection pairing
(?) Poincare Reducibility:
projection
quotients by abelian subvariety
(craig/william) Minimal isogeny degree for A, B simple.
(craig/william) Create a small mock database
Todo on Wednesday, March 19

Write doctests, etc., for everything above.
Optimize everything
