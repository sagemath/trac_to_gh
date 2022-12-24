# Issue 6854: Something weird in the implementation of InfinitePolynomialRing

archive/issues_006854.json:
```json
{
    "body": "CC:  @mwhansen simonking\n\nHello !!\n\nI know nothing about Symbolics in Sage, but I will be using InfinitePolynomialRing and I think the following code can be considered a bug. I create an expression using an element from InfinitePolynomialRing, on which I use \"Tab\" to list its methods, some of them not being printed. Example :\n\n\n```\nsage: P.<x>=InfinitePolynomialRing(RR)\nsage: e=x[1]+x[3]\nsage: e.\ne.abs                           e.footprint                     e.multiplicative_order          e.save\ne.additive_order                e.is_nilpotent                  e.n                             e.squeezed\ne.base_extend                   e.is_one                        e.order                         e.stretch\ne.base_ring                     e.is_unit                       e.parent                        e.subs\ne.category                      e.is_zero                       e.polynomial                    e.substitute\ne.coefficient                   e.lc                            e.reduce                        e.symmetric_cancellation_order\ne.db                            e.lm                            e.rename                        e.tail\ne.dump                          e.lt                            e.reset_name                    e.variables\ne.dumps                         e.max_index                     e.ring                          e.version\nsage: e.constant_coefficient()\n0.000000000000000\n```\n\n\nBesides, I do not understand why ( and I would really need it the other way ) inequalities on such expression return binaries instead of being kept symbolic :\n\n\n```\nsage: e<3\nFalse\n```\n\n\nBut this may be intentional, even though I do not like it :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/6854\n\n",
    "created_at": "2009-09-01T08:17:04Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Something weird in the implementation of InfinitePolynomialRing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6854",
    "user": "@nathanncohen"
}
```
CC:  @mwhansen simonking

Hello !!

I know nothing about Symbolics in Sage, but I will be using InfinitePolynomialRing and I think the following code can be considered a bug. I create an expression using an element from InfinitePolynomialRing, on which I use "Tab" to list its methods, some of them not being printed. Example :


```
sage: P.<x>=InfinitePolynomialRing(RR)
sage: e=x[1]+x[3]
sage: e.
e.abs                           e.footprint                     e.multiplicative_order          e.save
e.additive_order                e.is_nilpotent                  e.n                             e.squeezed
e.base_extend                   e.is_one                        e.order                         e.stretch
e.base_ring                     e.is_unit                       e.parent                        e.subs
e.category                      e.is_zero                       e.polynomial                    e.substitute
e.coefficient                   e.lc                            e.reduce                        e.symmetric_cancellation_order
e.db                            e.lm                            e.rename                        e.tail
e.dump                          e.lt                            e.reset_name                    e.variables
e.dumps                         e.max_index                     e.ring                          e.version
sage: e.constant_coefficient()
0.000000000000000
```


Besides, I do not understand why ( and I would really need it the other way ) inequalities on such expression return binaries instead of being kept symbolic :


```
sage: e<3
False
```


But this may be intentional, even though I do not like it :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/6854





---

archive/issue_comments_056505.json:
```json
{
    "body": "I don't see what the reported bug is. Note that the `InfinitePolynomialRing` has nothing to do with symbolics.\n\nWhat is the problem in the first example?\n\nIf you want comparisons to remain symbolic, you should use symbolic variables that are declared with `var()`.\n\n\nFor reference, the relevant thread where this was discussed is here:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/8a129481e1a947ad/f36a68f20242b6d7",
    "created_at": "2009-11-30T14:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56505",
    "user": "@burcin"
}
```

I don't see what the reported bug is. Note that the `InfinitePolynomialRing` has nothing to do with symbolics.

What is the problem in the first example?

If you want comparisons to remain symbolic, you should use symbolic variables that are declared with `var()`.


For reference, the relevant thread where this was discussed is here:

http://groups.google.com/group/sage-devel/browse_thread/thread/8a129481e1a947ad/f36a68f20242b6d7



---

archive/issue_comments_056506.json:
```json
{
    "body": "Hello !!!\n\nAmong the two remarks, the most important was the fact that the introspection in class InfinitePolynomialRing seems to be flawed as some functions ( for example constant_coefficient() ) does not appear.. :-)\n\n( I learnt some terminology since )\n\nNathann",
    "created_at": "2009-11-30T15:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56506",
    "user": "@nathanncohen"
}
```

Hello !!!

Among the two remarks, the most important was the fact that the introspection in class InfinitePolynomialRing seems to be flawed as some functions ( for example constant_coefficient() ) does not appear.. :-)

( I learnt some terminology since )

Nathann



---

archive/issue_comments_056507.json:
```json
{
    "body": "AFAICT, introspection doesn't work simply because the given class doesn't have such a method. If you look at the file `sage/rings/polynomial/infinite_polynomial_element.py`, you'll see that a custom `__getattr__` method is used to pass the call on to the *real element* `self._p`.\n\nMaybe Mike knows a trick to make introspection work as well.",
    "created_at": "2009-11-30T16:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56507",
    "user": "@burcin"
}
```

AFAICT, introspection doesn't work simply because the given class doesn't have such a method. If you look at the file `sage/rings/polynomial/infinite_polynomial_element.py`, you'll see that a custom `__getattr__` method is used to pass the call on to the *real element* `self._p`.

Maybe Mike knows a trick to make introspection work as well.



---

archive/issue_comments_056508.json:
```json
{
    "body": "Changing component from symbolics to misc.",
    "created_at": "2009-11-30T16:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56508",
    "user": "@burcin"
}
```

Changing component from symbolics to misc.



---

archive/issue_comments_056509.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-11-30T18:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56509",
    "user": "@simon-king-jena"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_056510.json:
```json
{
    "body": "Hi Nathann!\n\nFirstly, as was mentioned by Burcin, you mixed two completely different things, namely symbolics and commutative algebra. InfinitePolynomialRing is about the latter. It isn't \"misc\" either, so, I am changing the component again.\n\nConcerning `e<3` returning `True`: This is clearly intentional and most certainly not a bug. It is essential to have polynomial rings ordered, if one wants to compute Gr\u00f6bner bases -- and this is what InfinitePolynomialRing is about.\n\nTherefore I changed the Summary of the ticket (which was too unspecific anyway).\n\nConcerning TAB completion: It is correct that the custom `__getattr__` is to blame.\n\nBut I just learned something. Namely, if a class has a method `_getAttributeNames` that returns a list of strings, then these are used to do auto completion. Apparently methods `__members__`, `__methods__` and `trait_names` also play a role, but I don't know which. \n\nA possible solution is to implement `_getAttributeNames` so that it returns `dir(underlying polynomial)`. I just tested: TAB-completion will then show *both* the genuine attributes of InfinitePolynomials *and* the attributes inherited from usual polynomials.\n\nBut I don't think that this is a bug. So, I change the ticket type into \"enhancement\", and also added key words.\n\nI will implement it (after dinner...) and post a patch.\n\nCheers,\nSimon",
    "created_at": "2009-11-30T18:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56510",
    "user": "@simon-king-jena"
}
```

Hi Nathann!

Firstly, as was mentioned by Burcin, you mixed two completely different things, namely symbolics and commutative algebra. InfinitePolynomialRing is about the latter. It isn't "misc" either, so, I am changing the component again.

Concerning `e<3` returning `True`: This is clearly intentional and most certainly not a bug. It is essential to have polynomial rings ordered, if one wants to compute Gröbner bases -- and this is what InfinitePolynomialRing is about.

Therefore I changed the Summary of the ticket (which was too unspecific anyway).

Concerning TAB completion: It is correct that the custom `__getattr__` is to blame.

But I just learned something. Namely, if a class has a method `_getAttributeNames` that returns a list of strings, then these are used to do auto completion. Apparently methods `__members__`, `__methods__` and `trait_names` also play a role, but I don't know which. 

A possible solution is to implement `_getAttributeNames` so that it returns `dir(underlying polynomial)`. I just tested: TAB-completion will then show *both* the genuine attributes of InfinitePolynomials *and* the attributes inherited from usual polynomials.

But I don't think that this is a bug. So, I change the ticket type into "enhancement", and also added key words.

I will implement it (after dinner...) and post a patch.

Cheers,
Simon



---

archive/issue_comments_056511.json:
```json
{
    "body": "Changing keywords from \"\" to \"tab completion, InfinitePolynomialRing\".",
    "created_at": "2009-11-30T18:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56511",
    "user": "@simon-king-jena"
}
```

Changing keywords from "" to "tab completion, InfinitePolynomialRing".



---

archive/issue_comments_056512.json:
```json
{
    "body": "Changing component from misc to commutative algebra.",
    "created_at": "2009-11-30T18:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56512",
    "user": "@simon-king-jena"
}
```

Changing component from misc to commutative algebra.



---

archive/issue_comments_056513.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-30T20:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56513",
    "user": "@simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056514.json:
```json
{
    "body": "The dinner was good, and I hope the 3-line patch is as well. \n\nI hope there is no need to rebase it, since I made it with sage-4.2.1. \n\nWith the patch, I get (on the command line):\n\n```\nsage: R.<t>=InfinitePolynomialRing(QQ)\nsage: p=t[1]+3*t[4]\nsage: p.<TAB>\np.abs                           p.jacobian_ideal\np.add_m_mul_q                   p.lc\np.additive_order                p.lcm\np.args                          p.lift\np.base_extend                   p.lm\np.base_ring                     p.lt\np.category                      p.map_coefficients\np.change_ring                   p.max_index\np.coefficient                   p.mod\np.coefficients                  p.monomial_coefficient\np.constant_coefficient          p.monomials\np.content                       p.multiplicative_order\np.db                            p.n\np.degree                        p.newton_polytope\np.degrees                       p.nvariables\np.derivative                    p.order\np.dict                          p.parent\np.divides                       p.polynomial\np.dump                          p.quo_rem\np.dumps                         p.reduce\np.exponents                     p.rename\np.factor                        p.reset_name\np.footprint                     p.resultant\n--More--\n```\n\n\nIt seems to me that this is what tab completion should do.\n\nI understood that the new trac system is that I don't need to add [with patch, needs review] to the summary, but to tick \"needs review\"; correct me if I'm wrong.",
    "created_at": "2009-11-30T20:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56514",
    "user": "@simon-king-jena"
}
```

The dinner was good, and I hope the 3-line patch is as well. 

I hope there is no need to rebase it, since I made it with sage-4.2.1. 

With the patch, I get (on the command line):

```
sage: R.<t>=InfinitePolynomialRing(QQ)
sage: p=t[1]+3*t[4]
sage: p.<TAB>
p.abs                           p.jacobian_ideal
p.add_m_mul_q                   p.lc
p.additive_order                p.lcm
p.args                          p.lift
p.base_extend                   p.lm
p.base_ring                     p.lt
p.category                      p.map_coefficients
p.change_ring                   p.max_index
p.coefficient                   p.mod
p.coefficients                  p.monomial_coefficient
p.constant_coefficient          p.monomials
p.content                       p.multiplicative_order
p.db                            p.n
p.degree                        p.newton_polytope
p.degrees                       p.nvariables
p.derivative                    p.order
p.dict                          p.parent
p.divides                       p.polynomial
p.dump                          p.quo_rem
p.dumps                         p.reduce
p.exponents                     p.rename
p.factor                        p.reset_name
p.footprint                     p.resultant
--More--
```


It seems to me that this is what tab completion should do.

I understood that the new trac system is that I don't need to add [with patch, needs review] to the summary, but to tick "needs review"; correct me if I'm wrong.



---

archive/issue_comments_056515.json:
```json
{
    "body": "Set assignee to @simon-king-jena.",
    "created_at": "2009-11-30T20:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56515",
    "user": "@simon-king-jena"
}
```

Set assignee to @simon-king-jena.



---

archive/issue_comments_056516.json:
```json
{
    "body": "Hi!\n\nNow I learned that the method `__members__` is used by `dir()`\n\nIt is a bit strange, since `dir?` explains that it would use a method `__dir__` if it exists; but in fact it doesn't.\n\nAnyway. With the new patch, one has both tab completion and introspection.\nNote that according to the original post, `constant_coefficient`, which is inherited from the underlying polynomial, did not appear.\n\n```\nsage: R.<t>=InfinitePolynomialRing(QQ)\nsage: p=t[1]+3*t[4]\nsage: L=dir(p)\nsage: [X for X in L if X.startswith('c')]\n\n['category',\n 'change_ring',\n 'coefficient',\n 'coefficients',\n 'constant_coefficient',\n 'content']\n```\n\n\nAnd tab completion works as with the previous patch.\n\nOne concern though: How can one test tab completion? Note that the `_getAttributeNames` and `__members__` methods have no doc test yet. How should it best look?",
    "created_at": "2009-11-30T21:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56516",
    "user": "@simon-king-jena"
}
```

Hi!

Now I learned that the method `__members__` is used by `dir()`

It is a bit strange, since `dir?` explains that it would use a method `__dir__` if it exists; but in fact it doesn't.

Anyway. With the new patch, one has both tab completion and introspection.
Note that according to the original post, `constant_coefficient`, which is inherited from the underlying polynomial, did not appear.

```
sage: R.<t>=InfinitePolynomialRing(QQ)
sage: p=t[1]+3*t[4]
sage: L=dir(p)
sage: [X for X in L if X.startswith('c')]

['category',
 'change_ring',
 'coefficient',
 'coefficients',
 'constant_coefficient',
 'content']
```


And tab completion works as with the previous patch.

One concern though: How can one test tab completion? Note that the `_getAttributeNames` and `__members__` methods have no doc test yet. How should it best look?



---

archive/issue_comments_056517.json:
```json
{
    "body": "Introspection and tab completion(plus doc tests) for elements of InfinitePolynomialRing",
    "created_at": "2009-11-30T22:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56517",
    "user": "@simon-king-jena"
}
```

Introspection and tab completion(plus doc tests) for elements of InfinitePolynomialRing



---

archive/issue_comments_056518.json:
```json
{
    "body": "Attachment [6854_tab_completion.patch](tarball://root/attachments/some-uuid/ticket6854/6854_tab_completion.patch) by @simon-king-jena created at 2009-11-30 22:10:52\n\nHi!\n\nYet another patch (still under the same name). This time, I added some doc tests. \n\n`dir()` provides a nice indirect doc test for `__getattr__` (after all, this is where the introspection eventually got implemented). But I still don't know how to properly test tab completion. Hence, I call the relevant method directly, although it is underscore. \n\nCheers,\nSimon",
    "created_at": "2009-11-30T22:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56518",
    "user": "@simon-king-jena"
}
```

Attachment [6854_tab_completion.patch](tarball://root/attachments/some-uuid/ticket6854/6854_tab_completion.patch) by @simon-king-jena created at 2009-11-30 22:10:52

Hi!

Yet another patch (still under the same name). This time, I added some doc tests. 

`dir()` provides a nice indirect doc test for `__getattr__` (after all, this is where the introspection eventually got implemented). But I still don't know how to properly test tab completion. Hence, I call the relevant method directly, although it is underscore. 

Cheers,
Simon



---

archive/issue_comments_056519.json:
```json
{
    "body": "Adding a better doc test for tab completion",
    "created_at": "2009-12-01T13:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56519",
    "user": "@simon-king-jena"
}
```

Adding a better doc test for tab completion



---

archive/issue_comments_056520.json:
```json
{
    "body": "Attachment [6854_tab_completion_doctest.patch](tarball://root/attachments/some-uuid/ticket6854/6854_tab_completion_doctest.patch) by @simon-king-jena created at 2009-12-01 13:56:00\n\nThe second patch (to be applied after the first) provides a nice indirect doc test for tab completion, according to William's advice at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/1bf6652891c4e45).",
    "created_at": "2009-12-01T13:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56520",
    "user": "@simon-king-jena"
}
```

Attachment [6854_tab_completion_doctest.patch](tarball://root/attachments/some-uuid/ticket6854/6854_tab_completion_doctest.patch) by @simon-king-jena created at 2009-12-01 13:56:00

The second patch (to be applied after the first) provides a nice indirect doc test for tab completion, according to William's advice at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/1bf6652891c4e45).



---

archive/issue_comments_056521.json:
```json
{
    "body": "I am currently overhauling the InfinitePolynomialRing code, and I do so at ticket #7580. \n\nMy impression is that it would simplify the work flow if this ticket would be closed as unresolved, and that the implementation of tab completion should be part of #7580.\n\nAlso, I found that the method `_getAttributeNames` is not needed. It suffices for both tab completion and introspection if the `__getattr__` method returns `dir(underlying polynomial` if the attribute `__methods__` is requested.\n\nI only wonder if it is dangerous to make `p.__methods__` return things that aren't methods. However, when I googled for it, my impression was that the use of `__methods__` in Python is not consistent. What is the Sage policy?\n\nAnd do you agree that the work should be moved to #7580 ?",
    "created_at": "2009-12-02T21:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56521",
    "user": "@simon-king-jena"
}
```

I am currently overhauling the InfinitePolynomialRing code, and I do so at ticket #7580. 

My impression is that it would simplify the work flow if this ticket would be closed as unresolved, and that the implementation of tab completion should be part of #7580.

Also, I found that the method `_getAttributeNames` is not needed. It suffices for both tab completion and introspection if the `__getattr__` method returns `dir(underlying polynomial` if the attribute `__methods__` is requested.

I only wonder if it is dangerous to make `p.__methods__` return things that aren't methods. However, when I googled for it, my impression was that the use of `__methods__` in Python is not consistent. What is the Sage policy?

And do you agree that the work should be moved to #7580 ?



---

archive/issue_comments_056522.json:
```json
{
    "body": "Patch looks good, applies fine against alpha1, I have two doctest failures:\n\n\n```\nsage -t  devel/sage/sage/graphs/graph_generators.py # 2 doctests failed\nsage -t  devel/sage/sage/server/misc.py # Segfault\n```\n\n\nThe first one is a known alpha1 problem and the second one I cannot reproduce (it would also be rather unrelated).",
    "created_at": "2009-12-08T14:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56522",
    "user": "@malb"
}
```

Patch looks good, applies fine against alpha1, I have two doctest failures:


```
sage -t  devel/sage/sage/graphs/graph_generators.py # 2 doctests failed
sage -t  devel/sage/sage/server/misc.py # Segfault
```


The first one is a known alpha1 problem and the second one I cannot reproduce (it would also be rather unrelated).



---

archive/issue_comments_056523.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T14:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56523",
    "user": "@malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056524.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T02:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56524",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_056525.json:
```json
{
    "body": "Replying to [comment:7 SimonKing]:\n> Hi!\n> \n> Now I learned that the method `__members__` is used by `dir()`\n> \n> It is a bit strange, since `dir?` explains that it would use a method `__dir__` if it exists; but in fact it doesn't.\n\n?\n\nIt actually works for me. In #7921, I added a dir to Element, which broke the current doctests in infinite polynomials. I just removed the __members__ logic, and renamed _getAttributeNames into __dir__, and the doctests pass again (see patch on #7921). Could you have a look, and provide me with other tests if you think it could break something else in infinite polynomials?",
    "created_at": "2010-01-14T10:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6854#issuecomment-56525",
    "user": "@nthiery"
}
```

Replying to [comment:7 SimonKing]:
> Hi!
> 
> Now I learned that the method `__members__` is used by `dir()`
> 
> It is a bit strange, since `dir?` explains that it would use a method `__dir__` if it exists; but in fact it doesn't.

?

It actually works for me. In #7921, I added a dir to Element, which broke the current doctests in infinite polynomials. I just removed the __members__ logic, and renamed _getAttributeNames into __dir__, and the doctests pass again (see patch on #7921). Could you have a look, and provide me with other tests if you think it could break something else in infinite polynomials?
