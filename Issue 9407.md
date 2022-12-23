# Issue 9407: fixed fields for dirichlet characters and conductors and dirichlet characters for abelian fields

Issue created by migration from https://trac.sagemath.org/ticket/9407

Original creator: wuthrich

Original creation time: 2010-07-02 05:16:55

Assignee: davidloeffler

Keywords: Dirichlet characters, abelian fields, class field theory

There is a correspondance between groups of Dirichlet characters and Galois groups of abelian fields (over Q). We implement here three functions

 * the conductor of an abelian field

 * the set of Dirichlet characters of an abelian field

 * the fixed field of a Dirichlet character


---

Attachment

exported against 4.4.4.alpha0


---

Comment by wuthrich created at 2010-07-30 16:59:39

exported against 4.5.2.alpha1


---

Attachment

Apart from the above the patch here also introduces the function `is_abelian` and improves `is_galois` for number fields. Subfields of abelian fields inherit both.

There are a few minor things that could be improved at a later state (which I write down here so that I won't forget) :

 * The 2-part of the conductor needs adjustment

 * We can prove that a field is NOT abelian even if we can not decide that it is Galois, by finding that a prime congruent to 1 modulo the hypothetical conductor that does not completely split.

 * Is there some effective Chebotarev that can be used to prove that a field is Galois ?


---

Comment by wuthrich created at 2010-07-30 17:19:58

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-07-30 17:19:58

This is ready for review, now. Only the second patch must be applied.


---

Comment by cremona created at 2010-10-31 21:21:47

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-10-31 21:21:47

This would all be a very useful enhancement.  I have a few comments, mostly minor.

The patch applies ok to 4.6.rc0 (with a little fuzz) and all doctests in rings/number_fields pass.

There are some spelling mistakes in the docstrings...

#9400 is now merged: does that help?

How hard is it to get the 2-part of the conductor?  If it is really hard, why not just honestly return the odd part (and change the name, or something)?

I am a bit worried about the 53-bit precision used to compute the polynomials.  Do you now that it always enough (surely not!), or is that wishful thinking?  Is it much too slow to use the appropriate cyclotomic field?


---

Comment by wuthrich created at 2010-11-11 22:11:34

> #9400 is now merged: does that help?

Maybe, I did not think about it.

> How hard is it to get the 2-part of the conductor?  If it is really hard, why not just honestly return the odd part (and change the name, or something)?

I don't know. Right now it give the right thing quite frequently, but not always. I would have to think harder to see if one can put the 2-part in as well. I won't do that, I fear.

> I am a bit worried about the 53-bit precision used to compute the polynomials.  Do you now that it always enough (surely not!), or is that wishful thinking?  Is it much too slow to use the appropriate cyclotomic field?

It is really very very slow with cyclotomic fields. To be honest, I do not think anyone wants to construct a field of the size that would require higher precision in this computation. But that is not an argument to improve this.


---

Comment by fwclarke created at 2010-12-19 10:07:09

I think the computation of fixed field polynomials can be made fasterusing Gauss's formula for the products of periods; see Disquisitiones §343 and/or van der Waerden §54. The formula involves only the exponents of $\zeta$ in the cyclotomic field $\QQ(\zeta)$, so the computation can be carried out computing only with integers (so any concerns about precision are avoided). 

The code with which I've been testing this follows. I've removed the requirement that the order d is prime, which is unnecessary, and dealt separately with the easy cases d = 2 and f = 1.


```
def fixed_field_polynomial_new(self):
    ZZ = IntegerRing()

    n = ZZ(self.conductor())
    if not n.is_prime():
        raise NotImplementedError, 'the conductor %s is supposed to be prime' % n
    
    d = self.order()
        
    # check that there will be such a field of degree d inside QQ(zeta_n)
    if euler_phi(n) % d != 0:
        raise ValueError, 'No field exists because %s does not divide %s=phi(%s)' % (d,euler_phi(n),n)
    f = euler_phi(n)/d

    S = PolynomialRing(ZZ, 'x')

    if f == 1:
        return cyclotomic_polynomial(n, S.gen())
    
    if d == 2:
        if n.mod(4) == 1:
            s = -1
        else:
            s = 1
        return S([s*(n + s)/4, 1, 1])

# Using the notation of van der Waerden, where $\zeta$ is a primitive 
# $n$-root of unity,
# $$
# \eta_i = \sum_{j=0}^{f-1}\zeta^{g^{i+dj}},
# $$
# is represented by eta[i] as the list of exponents.  
# 
# gen_index is a dictionary such that gen_index[r] = i if the exponent r 
# occurs in eta[i].  Thus $\eta^{(r)} = \eta_i$ in van der Waerden's 
# notation.

    R = IntegerModRing(n)
    g = R.unit_gens()[0]
    gen_index = {}
    eta = []
    for i in range(d):
        eta.append([])
        for j in range(f):
            r = g**(i + d*j)
            eta[i].append(r)
            gen_index[r] = i

# Using Gauss's formula
# $$
# \eta^{(r)}\eta^{(s)} = \sum_{j=0}^{f-1}\eta^{(r+sg^{dj})}
# $$
# (with $r=1$), we construct the matrix representing multiplication by
# $\eta_0=\eta^{(1)}$ with respect to the basis consisting of the $\eta_i$.
# Its characteristic polynomial generates the field.  The element
# $\eta^(0)$=f=-f\sum_{i=0}^{d-1}\eta_i$ is represented by eta_zero.

    V = FreeModule(ZZ, d)
    eta_zero = V([-f]*d)
    m = []
    for j in range(d):
       v = 0
       for e in eta[j]:
            try:
                s = V.gen(gen_index[1 + e])              
            except KeyError:
                s = eta_zero
            v += s
       m.append(v)
    m = matrix(m)
    return m.charpoly(S.0)
```



---

Comment by wuthrich created at 2011-02-07 14:44:06

Thanks to the suggestion of Francis Clarke above, I could improve this patch now. I substituted his suggested algorithm, which is indeed better.

As for the clumsy implementation of the conductor. I rewrote it a little bit. I did not look into the issue how to get the right power of 2; nor if there is a better algorithm (as this is all I will need for my work).

I believe #9400 does not help to make it better.


---

Comment by wuthrich created at 2011-02-07 14:45:01

replaces the previsou patches. exported against 4.6.1


---

Attachment


---

Comment by wuthrich created at 2011-02-07 17:29:14

Changing status from needs_work to needs_review.


---

Comment by mstreng created at 2011-02-16 12:18:00

Changing priority from minor to major.


---

Comment by mstreng created at 2011-02-16 12:18:00

Apply trac_9407_new.patch

What is that symbol meant to be on line 688 of sage/modular/dirichlet.py? Disquisitiones Â§343. It looks like A-hat for me.


---

Comment by mstreng created at 2011-02-16 13:58:02

All tests pass (including long). I did not take the time to check the algorithms. Documentation and code (aside from the actual algorithms) looks good. Here are some comments:

  * "`'the conductor %s is supposed to be prime' % n `", what do you mean by
  "supposed to be"? Do you mean the following?
  `"fixed_field_polynomial is only implemented if the conductor is prime, and %s is not" % n`

  * an example
  {{{
  sage: G = DirichletGroup(37)
  sage: psi = G.0^36; psi
  Dirichlet character modulo 37 of conductor 1 mapping 2 |--> 1
  sage: psi.fixed_field_polynomial()
  NotImplementedError: the conductor 1 is supposed to be prime
  }}}
  Why not add a simple check for this case to get the following?
  {{{
  sage: psi.fixed_field_polynomial()
  x
  sage: psi.fixed_field()
  Rational Field
  }}}

  * "`if euler_phi(n) % d != 0: `"
  This never happens: d is in a group of order `euler_phi(n)`, hence has order dividing that number

  {{{
  if f == 1: 
      from sage.misc.functional import cyclotomic_polynomial 
      return cyclotomic_polynomial(n, S.gen()) 
  }}}
  It would be good if this check is also added to `fixed_field()`, so that the output could be a `NumberField_cyclotomic`

  * when constructing a field from a character, you write
  {{{
  K.is_abelian.set_cache(True) 
  K.is_galois.set_cache(True) 
  }}}
  Why not add K.conductor.set_cache(self.conductor())
 
  * "`This assumes that `K/\mathbb{Q}` is an abelian extension;`" add "`even with check_abelian=True`"? Also, I think the developer's guide says something about how to typeset QQ, RR, ZZ etc. in the documentation, I think it is `QQ`.

  * "`.. warning: The 2-part of the conductor might be too big.`". Too big for what? Or do you mean that it is incorrect? Add an example and change the first line to "`Computes the conductor of the abelian field `K` up to a power of 2.`"

  * In the documentation of `dirichlet group`, "`a abelian`" should be "`an abelian`",
  and can you find a better word for "corresponding"? 

  * `# d could be improve to be the exponenent of the Galois group rather than the degree, but I do not see how to how about it already. ` I can't read this: not grammatical

  * "`Tough`" should be "`Though`"

  * "`Given a number field `K` of conductor `m` and degree `d`,`" add the word "abelian"

And then only the algorithms need to be checked.


---

Comment by wuthrich created at 2011-02-16 14:49:52

Thanks for all the comments. I will change these things (but not immediately, unfortunately) . Maybe I could even turn it into ablian groups rather than lists. ... When I have time.


---

Comment by wuthrich created at 2011-02-16 14:49:52

Changing status from needs_review to needs_work.


---

Comment by jwj created at 2017-07-18 19:30:44

If someone can bring this up to date, I can add the code to compute the 2-part of the conductor.


---

Comment by wuthrich created at 2017-07-18 19:48:39

This is very old code and I nor anyone else has looked at it for 6 years. I am still interested that these functionality gets added to sage at some point. I doubt that I will have much time at hand to do anything about it I am afraid.


---

Comment by alexjbest created at 2020-09-01 22:06:26

I converted this into a git branch and changed the fixed_field_polynomial functionality to use pari instead as discussed on https://github.com/LMFDB/lmfdb/issues/3994 , thanks to Aurel Page for the Pari code.

I have left the old code for fixed_field_polynomial intact, although it only works for prime conductor and order characters I like the idea of having a second easily viewable implementation in the source, to verify against if necessary.
----
New commits:


---

Comment by alexjbest created at 2020-09-01 22:06:53

Changing status from needs_work to needs_review.


---

Comment by edgarcosta created at 2020-09-01 22:27:21

What about

```
    def fixed_field_polynomial(self, algorithm = "pari"):
        ...
        if algorithm == "sage":
            ...
            return m.charpoly(xx)

        elif algorithm == "pari":
             ...
             return H.sage({"x":x})
        else:
             raise NotImplentedError("...")
```

instead of

```
    def fixed_field_polynomial(self, algorithm = "pari"):
        ...
        if algorithm == "sage":
            ...
            return m.charpoly(xx)

        # Use pari
        ...
        return H.sage({"x":x})
```

?


---

Comment by git created at 2020-09-01 22:31:11

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2020-09-11 17:54:04

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2020-10-18 08:57:55

typos:

"poynomial"

"Give a Dirichlet"

some dirichlet missing their D capital in the documentation

`f = euler_phi(n)/d` could use exact division `//`

`fixed_field_polynomial` should have doctests for all three algorithms: sage, pari and banana


---

Comment by chapoton created at 2020-10-18 09:01:23

This

```diff
+        K = NumberField(poly, 'a')
+        return K
```

could be just one line. Same for

```diff
+    A = [map_Zmstar_to_Zm(h) for h in Hgens]
+    return A
```



---

Comment by git created at 2020-10-21 17:40:29

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by alexjbest created at 2020-10-21 17:41:40

Thanks Frédéric! Should be all fixed but I didn't run tests locally.


---

Comment by git created at 2020-10-22 19:52:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2020-11-27 17:38:12

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-11-27 17:38:12

ok, let it be


---

Comment by vbraun created at 2020-12-05 22:13:24

Resolution: fixed
