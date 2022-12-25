# Issue 9407: fixed fields for dirichlet characters and conductors and dirichlet characters for abelian fields

archive/issues_009407.json:
```json
{
    "body": "Assignee: @loefflerd\n\nKeywords: Dirichlet characters, abelian fields, class field theory\n\nThere is a correspondance between groups of Dirichlet characters and Galois groups of abelian fields (over Q). We implement here three functions\n\n* the conductor of an abelian field\n\n* the set of Dirichlet characters of an abelian field\n\n* the fixed field of a Dirichlet character\n\nIssue created by migration from https://trac.sagemath.org/ticket/9407\n\n",
    "created_at": "2010-07-02T05:16:55Z",
    "labels": [
        "component: number fields",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.3",
    "title": "fixed fields for dirichlet characters and conductors and dirichlet characters for abelian fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9407",
    "user": "https://github.com/categorie"
}
```
Assignee: @loefflerd

Keywords: Dirichlet characters, abelian fields, class field theory

There is a correspondance between groups of Dirichlet characters and Galois groups of abelian fields (over Q). We implement here three functions

* the conductor of an abelian field

* the set of Dirichlet characters of an abelian field

* the fixed field of a Dirichlet character

Issue created by migration from https://trac.sagemath.org/ticket/9407





---

archive/issue_comments_089489.json:
```json
{
    "body": "Attachment [trac_9407.patch](tarball://root/attachments/some-uuid/ticket9407/trac_9407.patch) by @categorie created at 2010-07-02 05:27:33\n\nexported against 4.4.4.alpha0",
    "created_at": "2010-07-02T05:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89489",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_9407.patch](tarball://root/attachments/some-uuid/ticket9407/trac_9407.patch) by @categorie created at 2010-07-02 05:27:33

exported against 4.4.4.alpha0



---

archive/issue_comments_089490.json:
```json
{
    "body": "exported against 4.5.2.alpha1",
    "created_at": "2010-07-30T16:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89490",
    "user": "https://github.com/categorie"
}
```

exported against 4.5.2.alpha1



---

archive/issue_comments_089491.json:
```json
{
    "body": "Attachment [trac_9407.2.patch](tarball://root/attachments/some-uuid/ticket9407/trac_9407.2.patch) by @categorie created at 2010-07-30 17:19:26\n\nApart from the above the patch here also introduces the function `is_abelian` and improves `is_galois` for number fields. Subfields of abelian fields inherit both.\n\nThere are a few minor things that could be improved at a later state (which I write down here so that I won't forget) :\n\n* The 2-part of the conductor needs adjustment\n\n* We can prove that a field is NOT abelian even if we can not decide that it is Galois, by finding that a prime congruent to 1 modulo the hypothetical conductor that does not completely split.\n\n* Is there some effective Chebotarev that can be used to prove that a field is Galois ?",
    "created_at": "2010-07-30T17:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89491",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_9407.2.patch](tarball://root/attachments/some-uuid/ticket9407/trac_9407.2.patch) by @categorie created at 2010-07-30 17:19:26

Apart from the above the patch here also introduces the function `is_abelian` and improves `is_galois` for number fields. Subfields of abelian fields inherit both.

There are a few minor things that could be improved at a later state (which I write down here so that I won't forget) :

* The 2-part of the conductor needs adjustment

* We can prove that a field is NOT abelian even if we can not decide that it is Galois, by finding that a prime congruent to 1 modulo the hypothetical conductor that does not completely split.

* Is there some effective Chebotarev that can be used to prove that a field is Galois ?



---

archive/issue_comments_089492.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-30T17:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89492",
    "user": "https://github.com/categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089493.json:
```json
{
    "body": "This is ready for review, now. Only the second patch must be applied.",
    "created_at": "2010-07-30T17:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89493",
    "user": "https://github.com/categorie"
}
```

This is ready for review, now. Only the second patch must be applied.



---

archive/issue_comments_089494.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-31T21:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89494",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089495.json:
```json
{
    "body": "This would all be a very useful enhancement.  I have a few comments, mostly minor.\n\nThe patch applies ok to 4.6.rc0 (with a little fuzz) and all doctests in rings/number_fields pass.\n\nThere are some spelling mistakes in the docstrings...\n\n#9400 is now merged: does that help?\n\nHow hard is it to get the 2-part of the conductor?  If it is really hard, why not just honestly return the odd part (and change the name, or something)?\n\nI am a bit worried about the 53-bit precision used to compute the polynomials.  Do you now that it always enough (surely not!), or is that wishful thinking?  Is it much too slow to use the appropriate cyclotomic field?",
    "created_at": "2010-10-31T21:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89495",
    "user": "https://github.com/JohnCremona"
}
```

This would all be a very useful enhancement.  I have a few comments, mostly minor.

The patch applies ok to 4.6.rc0 (with a little fuzz) and all doctests in rings/number_fields pass.

There are some spelling mistakes in the docstrings...

#9400 is now merged: does that help?

How hard is it to get the 2-part of the conductor?  If it is really hard, why not just honestly return the odd part (and change the name, or something)?

I am a bit worried about the 53-bit precision used to compute the polynomials.  Do you now that it always enough (surely not!), or is that wishful thinking?  Is it much too slow to use the appropriate cyclotomic field?



---

archive/issue_comments_089496.json:
```json
{
    "body": "> #9400 is now merged: does that help?\n\nMaybe, I did not think about it.\n\n> How hard is it to get the 2-part of the conductor?  If it is really hard, why not just honestly return the odd part (and change the name, or something)?\n\nI don't know. Right now it give the right thing quite frequently, but not always. I would have to think harder to see if one can put the 2-part in as well. I won't do that, I fear.\n\n> I am a bit worried about the 53-bit precision used to compute the polynomials.  Do you now that it always enough (surely not!), or is that wishful thinking?  Is it much too slow to use the appropriate cyclotomic field?\n\nIt is really very very slow with cyclotomic fields. To be honest, I do not think anyone wants to construct a field of the size that would require higher precision in this computation. But that is not an argument to improve this.",
    "created_at": "2010-11-11T22:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89496",
    "user": "https://github.com/categorie"
}
```

> #9400 is now merged: does that help?

Maybe, I did not think about it.

> How hard is it to get the 2-part of the conductor?  If it is really hard, why not just honestly return the odd part (and change the name, or something)?

I don't know. Right now it give the right thing quite frequently, but not always. I would have to think harder to see if one can put the 2-part in as well. I won't do that, I fear.

> I am a bit worried about the 53-bit precision used to compute the polynomials.  Do you now that it always enough (surely not!), or is that wishful thinking?  Is it much too slow to use the appropriate cyclotomic field?

It is really very very slow with cyclotomic fields. To be honest, I do not think anyone wants to construct a field of the size that would require higher precision in this computation. But that is not an argument to improve this.



---

archive/issue_comments_089497.json:
```json
{
    "body": "I think the computation of fixed field polynomials can be made fasterusing Gauss's formula for the products of periods; see Disquisitiones \u00a7343 and/or van der Waerden \u00a754. The formula involves only the exponents of $\\zeta$ in the cyclotomic field $\\QQ(\\zeta)$, so the computation can be carried out computing only with integers\u00a0(so any concerns about precision are avoided).\u00a0\n\nThe code with which I've been testing this follows. I've removed the requirement that the order d is prime, which is unnecessary, and dealt separately with the easy cases d = 2 and f = 1.\n\n\n```\ndef fixed_field_polynomial_new(self):\n    ZZ = IntegerRing()\n\n    n = ZZ(self.conductor())\n    if not n.is_prime():\n        raise NotImplementedError, 'the conductor %s is supposed to be prime' % n\n    \n    d = self.order()\n        \n    # check that there will be such a field of degree d inside QQ(zeta_n)\n    if euler_phi(n) % d != 0:\n        raise ValueError, 'No field exists because %s does not divide %s=phi(%s)' % (d,euler_phi(n),n)\n    f = euler_phi(n)/d\n\n    S = PolynomialRing(ZZ, 'x')\n\n    if f == 1:\n        return cyclotomic_polynomial(n, S.gen())\n    \n    if d == 2:\n        if n.mod(4) == 1:\n            s = -1\n        else:\n            s = 1\n        return S([s*(n + s)/4, 1, 1])\n\n# Using the notation of van der Waerden, where $\\zeta$ is a primitive \n# $n$-root of unity,\n# $$\n# \\eta_i = \\sum_{j=0}^{f-1}\\zeta^{g^{i+dj}},\n# $$\n# is represented by eta[i] as the list of exponents.  \n# \n# gen_index is a dictionary such that gen_index[r] = i if the exponent r \n# occurs in eta[i].  Thus $\\eta^{(r)} = \\eta_i$ in van der Waerden's \n# notation.\n\n    R = IntegerModRing(n)\n    g = R.unit_gens()[0]\n    gen_index = {}\n    eta = []\n    for i in range(d):\n        eta.append([])\n        for j in range(f):\n            r = g**(i + d*j)\n            eta[i].append(r)\n            gen_index[r] = i\n\n# Using Gauss's formula\n# $$\n# \\eta^{(r)}\\eta^{(s)} = \\sum_{j=0}^{f-1}\\eta^{(r+sg^{dj})}\n# $$\n# (with $r=1$), we construct the matrix representing multiplication by\n# $\\eta_0=\\eta^{(1)}$ with respect to the basis consisting of the $\\eta_i$.\n# Its characteristic polynomial generates the field.  The element\n# $\\eta^(0)$=f=-f\\sum_{i=0}^{d-1}\\eta_i$ is represented by eta_zero.\n\n    V = FreeModule(ZZ, d)\n    eta_zero = V([-f]*d)\n    m = []\n    for j in range(d):\n       v = 0\n       for e in eta[j]:\n            try:\n                s = V.gen(gen_index[1 + e])              \n            except KeyError:\n                s = eta_zero\n            v += s\n       m.append(v)\n    m = matrix(m)\n    return m.charpoly(S.0)\n```\n",
    "created_at": "2010-12-19T10:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89497",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

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

archive/issue_comments_089498.json:
```json
{
    "body": "Thanks to the suggestion of Francis Clarke above, I could improve this patch now. I substituted his suggested algorithm, which is indeed better.\n\nAs for the clumsy implementation of the conductor. I rewrote it a little bit. I did not look into the issue how to get the right power of 2; nor if there is a better algorithm (as this is all I will need for my work).\n\nI believe #9400 does not help to make it better.",
    "created_at": "2011-02-07T14:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89498",
    "user": "https://github.com/categorie"
}
```

Thanks to the suggestion of Francis Clarke above, I could improve this patch now. I substituted his suggested algorithm, which is indeed better.

As for the clumsy implementation of the conductor. I rewrote it a little bit. I did not look into the issue how to get the right power of 2; nor if there is a better algorithm (as this is all I will need for my work).

I believe #9400 does not help to make it better.



---

archive/issue_comments_089499.json:
```json
{
    "body": "replaces the previsou patches. exported against 4.6.1",
    "created_at": "2011-02-07T14:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89499",
    "user": "https://github.com/categorie"
}
```

replaces the previsou patches. exported against 4.6.1



---

archive/issue_comments_089500.json:
```json
{
    "body": "Attachment [trac_9407_new.patch](tarball://root/attachments/some-uuid/ticket9407/trac_9407_new.patch) by @categorie created at 2011-02-07 17:29:14",
    "created_at": "2011-02-07T17:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89500",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_9407_new.patch](tarball://root/attachments/some-uuid/ticket9407/trac_9407_new.patch) by @categorie created at 2011-02-07 17:29:14



---

archive/issue_comments_089501.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-07T17:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89501",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089502.json:
```json
{
    "body": "Apply trac_9407_new.patch\n\nWhat is that symbol meant to be on line 688 of sage/modular/dirichlet.py? Disquisitiones \u00c2\u00a7343. It looks like A-hat for me.",
    "created_at": "2011-02-16T12:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89502",
    "user": "https://github.com/mstreng"
}
```

Apply trac_9407_new.patch

What is that symbol meant to be on line 688 of sage/modular/dirichlet.py? Disquisitiones Â§343. It looks like A-hat for me.



---

archive/issue_comments_089503.json:
```json
{
    "body": "All tests pass (including long). I did not take the time to check the algorithms. Documentation and code (aside from the actual algorithms) looks good. Here are some comments:\n\n* \"`'the conductor %s is supposed to be prime' % n `\", what do you mean by\n  \"supposed to be\"? Do you mean the following?\n  `\"fixed_field_polynomial is only implemented if the conductor is prime, and %s is not\" % n`\n\n* an example\n  {{{\n  sage: G = DirichletGroup(37)\n  sage: psi = G.0^36; psi\n  Dirichlet character modulo 37 of conductor 1 mapping 2 |--> 1\n  sage: psi.fixed_field_polynomial()\n  NotImplementedError: the conductor 1 is supposed to be prime\n  }}}\n  Why not add a simple check for this case to get the following?\n  {{{\n  sage: psi.fixed_field_polynomial()\n  x\n  sage: psi.fixed_field()\n  Rational Field\n  }}}\n\n* \"`if euler_phi(n) % d != 0: `\"\n  This never happens: d is in a group of order `euler_phi(n)`, hence has order dividing that number\n\n  {{{\n  if f == 1: \n      from sage.misc.functional import cyclotomic_polynomial \n      return cyclotomic_polynomial(n, S.gen()) \n  }}}\n  It would be good if this check is also added to `fixed_field()`, so that the output could be a `NumberField_cyclotomic`\n\n* when constructing a field from a character, you write\n  {{{\n  K.is_abelian.set_cache(True) \n  K.is_galois.set_cache(True) \n  }}}\n  Why not add K.conductor.set_cache(self.conductor())\n \n* \"`This assumes that `K/\\mathbb{Q}` is an abelian extension;`\" add \"`even with check_abelian=True`\"? Also, I think the developer's guide says something about how to typeset QQ, RR, ZZ etc. in the documentation, I think it is `QQ`.\n\n* \"`.. warning: The 2-part of the conductor might be too big.`\". Too big for what? Or do you mean that it is incorrect? Add an example and change the first line to \"`Computes the conductor of the abelian field `K` up to a power of 2.`\"\n\n* In the documentation of `dirichlet group`, \"`a abelian`\" should be \"`an abelian`\",\n  and can you find a better word for \"corresponding\"? \n\n* `# d could be improve to be the exponenent of the Galois group rather than the degree, but I do not see how to how about it already. ` I can't read this: not grammatical\n\n* \"`Tough`\" should be \"`Though`\"\n\n* \"`Given a number field `K` of conductor `m` and degree `d`,`\" add the word \"abelian\"\n\nAnd then only the algorithms need to be checked.",
    "created_at": "2011-02-16T13:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89503",
    "user": "https://github.com/mstreng"
}
```

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

archive/issue_comments_089504.json:
```json
{
    "body": "Thanks for all the comments. I will change these things (but not immediately, unfortunately) . Maybe I could even turn it into ablian groups rather than lists. ... When I have time.",
    "created_at": "2011-02-16T14:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89504",
    "user": "https://github.com/categorie"
}
```

Thanks for all the comments. I will change these things (but not immediately, unfortunately) . Maybe I could even turn it into ablian groups rather than lists. ... When I have time.



---

archive/issue_comments_089505.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-02-16T14:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89505",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_events_023226.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9407#event-23226"
}
```



---

archive/issue_events_023227.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9407#event-23227"
}
```



---

archive/issue_events_023228.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9407#event-23228"
}
```



---

archive/issue_events_023229.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9407#event-23229"
}
```



---

archive/issue_events_023230.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9407#event-23230"
}
```



---

archive/issue_events_023231.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9407#event-23231"
}
```



---

archive/issue_events_023232.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9407#event-23232"
}
```



---

archive/issue_comments_089506.json:
```json
{
    "body": "If someone can bring this up to date, I can add the code to compute the 2-part of the conductor.",
    "created_at": "2017-07-18T19:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89506",
    "user": "https://trac.sagemath.org/admin/accounts/users/jwj"
}
```

If someone can bring this up to date, I can add the code to compute the 2-part of the conductor.



---

archive/issue_comments_089507.json:
```json
{
    "body": "This is very old code and I nor anyone else has looked at it for 6 years. I am still interested that these functionality gets added to sage at some point. I doubt that I will have much time at hand to do anything about it I am afraid.",
    "created_at": "2017-07-18T19:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89507",
    "user": "https://github.com/categorie"
}
```

This is very old code and I nor anyone else has looked at it for 6 years. I am still interested that these functionality gets added to sage at some point. I doubt that I will have much time at hand to do anything about it I am afraid.



---

archive/issue_comments_089508.json:
```json
{
    "body": "I converted this into a git branch and changed the fixed_field_polynomial functionality to use pari instead as discussed on https://github.com/LMFDB/lmfdb/issues/3994 , thanks to Aurel Page for the Pari code.\n\nI have left the old code for fixed_field_polynomial intact, although it only works for prime conductor and order characters I like the idea of having a second easily viewable implementation in the source, to verify against if necessary.\n----\nNew commits:",
    "created_at": "2020-09-01T22:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89508",
    "user": "https://github.com/alexjbest"
}
```

I converted this into a git branch and changed the fixed_field_polynomial functionality to use pari instead as discussed on https://github.com/LMFDB/lmfdb/issues/3994 , thanks to Aurel Page for the Pari code.

I have left the old code for fixed_field_polynomial intact, although it only works for prime conductor and order characters I like the idea of having a second easily viewable implementation in the source, to verify against if necessary.
----
New commits:



---

archive/issue_events_023233.json:
```json
{
    "actor": "https://github.com/alexjbest",
    "created_at": "2020-09-01T22:06:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9407#event-23233"
}
```



---

archive/issue_events_023234.json:
```json
{
    "actor": "https://github.com/alexjbest",
    "created_at": "2020-09-01T22:06:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "milestone": "sage-9.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9407#event-23234"
}
```



---

archive/issue_comments_089509.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-09-01T22:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89509",
    "user": "https://github.com/alexjbest"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089510.json:
```json
{
    "body": "What about\n\n```\n    def fixed_field_polynomial(self, algorithm = \"pari\"):\n        ...\n        if algorithm == \"sage\":\n            ...\n            return m.charpoly(xx)\n\n        elif algorithm == \"pari\":\n             ...\n             return H.sage({\"x\":x})\n        else:\n             raise NotImplentedError(\"...\")\n```\n\ninstead of\n\n```\n    def fixed_field_polynomial(self, algorithm = \"pari\"):\n        ...\n        if algorithm == \"sage\":\n            ...\n            return m.charpoly(xx)\n\n        # Use pari\n        ...\n        return H.sage({\"x\":x})\n```\n\n?",
    "created_at": "2020-09-01T22:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89510",
    "user": "https://github.com/edgarcosta"
}
```

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

archive/issue_comments_089511.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-09-01T22:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89511",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_089512.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-09-11T17:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89512",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_089513.json:
```json
{
    "body": "typos:\n\n\"poynomial\"\n\n\"Give a Dirichlet\"\n\nsome dirichlet missing their D capital in the documentation\n\n`f = euler_phi(n)/d` could use exact division `//`\n\n`fixed_field_polynomial` should have doctests for all three algorithms: sage, pari and banana",
    "created_at": "2020-10-18T08:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89513",
    "user": "https://github.com/fchapoton"
}
```

typos:

"poynomial"

"Give a Dirichlet"

some dirichlet missing their D capital in the documentation

`f = euler_phi(n)/d` could use exact division `//`

`fixed_field_polynomial` should have doctests for all three algorithms: sage, pari and banana



---

archive/issue_comments_089514.json:
```json
{
    "body": "This\n\n```diff\n+        K = NumberField(poly, 'a')\n+        return K\n```\n\ncould be just one line. Same for\n\n```diff\n+    A = [map_Zmstar_to_Zm(h) for h in Hgens]\n+    return A\n```\n",
    "created_at": "2020-10-18T09:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89514",
    "user": "https://github.com/fchapoton"
}
```

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

archive/issue_comments_089515.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-10-21T17:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89515",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_089516.json:
```json
{
    "body": "Thanks Fr\u00e9d\u00e9ric! Should be all fixed but I didn't run tests locally.",
    "created_at": "2020-10-21T17:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89516",
    "user": "https://github.com/alexjbest"
}
```

Thanks Frédéric! Should be all fixed but I didn't run tests locally.



---

archive/issue_comments_089517.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-10-22T19:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89517",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_089518.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-11-27T17:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89518",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089519.json:
```json
{
    "body": "ok, let it be",
    "created_at": "2020-11-27T17:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89519",
    "user": "https://github.com/fchapoton"
}
```

ok, let it be



---

archive/issue_comments_089520.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-12-05T22:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9407#issuecomment-89520",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_023235.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2020-12-05T22:13:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9407",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9407#event-23235"
}
```
