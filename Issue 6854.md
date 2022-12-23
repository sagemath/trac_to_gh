# Issue 6854: Something weird in the implementation of InfinitePolynomialRing

Issue created by migration from https://trac.sagemath.org/ticket/6854

Original creator: ncohen

Original creation time: 2009-09-01 08:17:04

CC:  mhansen simonking

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


---

Comment by burcin created at 2009-11-30 14:40:14

I don't see what the reported bug is. Note that the `InfinitePolynomialRing` has nothing to do with symbolics.

What is the problem in the first example?

If you want comparisons to remain symbolic, you should use symbolic variables that are declared with `var()`.


For reference, the relevant thread where this was discussed is here:

http://groups.google.com/group/sage-devel/browse_thread/thread/8a129481e1a947ad/f36a68f20242b6d7


---

Comment by ncohen created at 2009-11-30 15:47:23

Hello !!!

Among the two remarks, the most important was the fact that the introspection in class InfinitePolynomialRing seems to be flawed as some functions ( for example constant_coefficient() ) does not appear.. :-)

( I learnt some terminology since )

Nathann


---

Comment by burcin created at 2009-11-30 16:18:01

AFAICT, introspection doesn't work simply because the given class doesn't have such a method. If you look at the file `sage/rings/polynomial/infinite_polynomial_element.py`, you'll see that a custom `__getattr__` method is used to pass the call on to the _real element_ `self._p`.

Maybe Mike knows a trick to make introspection work as well.


---

Comment by burcin created at 2009-11-30 16:18:01

Changing component from symbolics to misc.


---

Comment by SimonKing created at 2009-11-30 18:25:21

Changing type from defect to enhancement.


---

Comment by SimonKing created at 2009-11-30 18:25:21

Hi Nathann!

Firstly, as was mentioned by Burcin, you mixed two completely different things, namely symbolics and commutative algebra. InfinitePolynomialRing is about the latter. It isn't "misc" either, so, I am changing the component again.

Concerning `e<3` returning `True`: This is clearly intentional and most certainly not a bug. It is essential to have polynomial rings ordered, if one wants to compute Gröbner bases -- and this is what InfinitePolynomialRing is about.

Therefore I changed the Summary of the ticket (which was too unspecific anyway).

Concerning TAB completion: It is correct that the custom `__getattr__` is to blame.

But I just learned something. Namely, if a class has a method `_getAttributeNames` that returns a list of strings, then these are used to do auto completion. Apparently methods `__members__`, `__methods__` and `trait_names` also play a role, but I don't know which. 

A possible solution is to implement `_getAttributeNames` so that it returns `dir(underlying polynomial)`. I just tested: TAB-completion will then show _both_ the genuine attributes of InfinitePolynomials _and_ the attributes inherited from usual polynomials.

But I don't think that this is a bug. So, I change the ticket type into "enhancement", and also added key words.

I will implement it (after dinner...) and post a patch.

Cheers,
Simon


---

Comment by SimonKing created at 2009-11-30 18:25:21

Changing keywords from "" to "tab completion, InfinitePolynomialRing".


---

Comment by SimonKing created at 2009-11-30 18:25:21

Changing component from misc to commutative algebra.


---

Comment by SimonKing created at 2009-11-30 20:28:56

Changing status from new to needs_review.


---

Comment by SimonKing created at 2009-11-30 20:28:56

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

Comment by SimonKing created at 2009-11-30 20:29:15

Set assignee to SimonKing.


---

Comment by SimonKing created at 2009-11-30 21:28:34

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

Comment by SimonKing created at 2009-11-30 22:06:07

Introspection and tab completion(plus doc tests) for elements of InfinitePolynomialRing


---

Attachment

Hi!

Yet another patch (still under the same name). This time, I added some doc tests. 

`dir()` provides a nice indirect doc test for `__getattr__` (after all, this is where the introspection eventually got implemented). But I still don't know how to properly test tab completion. Hence, I call the relevant method directly, although it is underscore. 

Cheers,
Simon


---

Comment by SimonKing created at 2009-12-01 13:54:29

Adding a better doc test for tab completion


---

Attachment

The second patch (to be applied after the first) provides a nice indirect doc test for tab completion, according to William's advice at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/1bf6652891c4e45).


---

Comment by SimonKing created at 2009-12-02 21:54:41

I am currently overhauling the InfinitePolynomialRing code, and I do so at ticket #7580. 

My impression is that it would simplify the work flow if this ticket would be closed as unresolved, and that the implementation of tab completion should be part of #7580.

Also, I found that the method `_getAttributeNames` is not needed. It suffices for both tab completion and introspection if the `__getattr__` method returns `dir(underlying polynomial` if the attribute `__methods__` is requested.

I only wonder if it is dangerous to make `p.__methods__` return things that aren't methods. However, when I googled for it, my impression was that the use of `__methods__` in Python is not consistent. What is the Sage policy?

And do you agree that the work should be moved to #7580 ?


---

Comment by malb created at 2009-12-08 14:00:32

Patch looks good, applies fine against alpha1, I have two doctest failures:


```
sage -t  devel/sage/sage/graphs/graph_generators.py # 2 doctests failed
sage -t  devel/sage/sage/server/misc.py # Segfault
```


The first one is a known alpha1 problem and the second one I cannot reproduce (it would also be rather unrelated).


---

Comment by malb created at 2009-12-08 14:00:32

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-09 02:57:28

Resolution: fixed


---

Comment by nthiery created at 2010-01-14 10:00:32

Replying to [comment:7 SimonKing]:
> Hi!
> 
> Now I learned that the method `__members__` is used by `dir()`
> 
> It is a bit strange, since `dir?` explains that it would use a method `__dir__` if it exists; but in fact it doesn't.

?

It actually works for me. In #7921, I added a dir to Element, which broke the current doctests in infinite polynomials. I just removed the __members__ logic, and renamed _getAttributeNames into __dir__, and the doctests pass again (see patch on #7921). Could you have a look, and provide me with other tests if you think it could break something else in infinite polynomials?
