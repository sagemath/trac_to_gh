# Issue 1819: move crypto.mq.MPolynomialSystem somewhere else

Issue created by migration from https://trac.sagemath.org/ticket/1819

Original creator: malb

Original creation time: 2008-01-18 00:29:31

Assignee: malb

CC:  sbulygin mhampton

Though it is motivated by cryptography it is not specific to it, maybe move it to `sage.rings.polynomial` after all ideals are there as well?


---

Comment by malb created at 2011-01-13 17:14:05

Changing status from new to needs_review.


---

Comment by malb created at 2011-01-13 21:10:57

There are a few minor doctest failures:


```
sage -t  -long -force_lib devel/sage/sage/rings/residue_field.pyx # 3 doctests failed
sage -t  -long -force_lib devel/sage/sage/rings/ideal.py # 1 doctests failed
sage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_sequence.py # 2 doctests failed
sage -t  -long -force_lib devel/sage/sage/tests/cmdline.py # 1 doctests failed
```



---

Comment by malb created at 2011-01-14 14:35:10

The attached patch takes care of those doctest failures (except for the cmdline one which is not due to this patch)


---

Comment by malb created at 2011-01-22 14:39:43

Hi, can one of you two take a look at this patch? Cheers.


---

Comment by malb created at 2011-02-18 14:00:08

Btw. patchbot reports "Apply failed" because the patch is for 4.6.2.alpha4 instead of 4.6.1.


---

Comment by vbraun created at 2011-02-26 17:14:56

The whole rename looks reasonable to me.

Having said that, I don't understand why we need both `MPolynomialIdeal` and `PolynomialSequence`. It seems to be that both are essentially containers for polynomials in a common ring. Maybe the methods of `PolynomialSequence` could just be merged with the ideal code? Do you have any thoughts about that?


---

Comment by malb created at 2011-02-26 17:26:33

Replying to [comment:10 vbraun]:
> Having said that, I don't understand why we need both `MPolynomialIdeal` and 
> `PolynomialSequence`. It seems to be that both are essentially containers for 
> polynomials in a common ring. Maybe the methods of `PolynomialSequence` could just
> be merged with the ideal code? Do you have any thoughts about that?

I disagree with merging the two. Ideal are not the same as sequences of polynomials: ideals may be infinite, but our polynomial sequences are always finite. Furthermore, some methods don't make sense on ideals but do make sense for sequences of polynomials such as interreduction and weil restriction. That we have those methods on ideals now is not proper, I'd say. Another example: set operations on ideals are different from set operations on polynomial sequences.


---

Comment by vbraun created at 2011-02-26 17:39:17

Mathematically, they are of course not the same. But as far as the implementation goes, both are lists of polynomials with some methods attached. I don't understand your comment about finiteness, you can't generate a non-finitely generated ideal in Sage, nor could you construct the requisite infinite polynomial ring to evade Hilberts basis theorem. Moreover, I don't understand your comment about the `interreduced_basis` method in the ideal class. Where else but as a method of the ideal class should we define this functionality in OOP?


---

Comment by malb created at 2011-02-26 18:36:50

Replying to [comment:12 vbraun]:
> Mathematically, they are of course not the same. But as far as the implementation goes, both are lists of polynomials with some methods attached. I don't understand your comment about finiteness, you can't generate a non-finitely generated ideal in Sage, nor could you construct the requisite infinite polynomial ring to evade Hilberts basis theorem. Moreover, I don't understand your comment about the `interreduced_basis` method in the ideal class. Where else but as a method of the ideal class should we define this functionality in OOP?

I meant infinite but finitely generated which is for example relevant for set operations on them. Another example is reduction: reduction modulo the ideal is different from reduction modulo a list of polynomials. The method `interreduced_basis` assumes a particular basis for the ideal, i.e. violates the distinction between ideal and a list of polynomials. I'd say we should aim to have methods on ideals deal with ideals instead of the particular basis the user chose when constructing it.


---

Comment by vbraun created at 2011-02-26 18:54:14

In principle, it would be nice if the ideal class could represent some basis-free abstract notion of ideal. In practice, this is not possible as all non-trivial computations are exponential complexity due to the need for Groebner bases. Even worse, the Groebner basis computation often depends on a judiciously chosen term ordering which cannot be automated. This is why all computer algebra programs that I am aware of treat ideals as sequences of polynomials, and not as ideals in the mathematical sense. Barring any breakthrough in algebra it is not feasible to do otherwise.


---

Comment by malb created at 2011-02-26 19:17:38

I should have mentioned that the decision to treat ideals as such abstract basis-free objects was made before I joined the project, probably inherited from Magma. For example, cf. the intro of http://sagemath.org/doc/reference/sage/crypto/mq/mpolynomialsystem.html (which I admit to have written, though). Thus, many methods of the multivariate polynomial ideal class do compute a Gröbner basis behind the scenes. Btw. since ideals know their ring and rings contain the term ordering in Sage, we can compute GBs without any additionally provided information.


---

Comment by vbraun created at 2011-02-26 19:50:33

I don't see that anywhere in the `MPolynomialIdeal` class. Correct me if I'm wrong, but the chosen generators and their order is immutable. Even when computing a Groebner basis, the generators are not replaced by this much more useful basis. On the other hand, there are methods like `basis_is_groebner()` which are obviously basis-dependent. It seems to me that Sage implements ideals very much as an immutable sequence of polynomials with some methods attached. The individual methods do, of course, need Groebner bases but they never change the underlying sequence of polynomials.

I am aware that the ideals implicitly contain the term order, though I found that a somewhat mixed blessing in #10708.


---

Comment by malb created at 2011-02-26 20:09:02

Replying to [comment:16 vbraun]:
> I don't see that anywhere in the `MPolynomialIdeal` class. Correct me if I'm wrong,
> but the chosen generators and their order is immutable. 

Yep.

> Even when computing a Groebner basis, the generators are not replaced by this much 
> more useful basis. 

But the GB is cached and used for "interesting" operations.

> On the other hand, there are methods like `basis_is_groebner()` which are obviously
> basis-dependent. 

This was the compromise reached to (a) keep the notion that ideals are different objects than their generators and to (b) still allow to query some information about the basis. We should have separated stuff back then perhaps. In any case, it was this method's name which sparked the debate we're having between William and myself. 

> It seems to me that Sage implements ideals very much as an immutable sequence of 
> polynomials with some methods attached. 

I'd say: it attempts to present a view on ideals which abstracts away chosen bases but with varying success.

> The individual methods do, of course, need Groebner bases but they never change the > underlying sequence of polynomials.

But e.g. `intersection()` and `reduce()` actually use the GB and not the provided basis, they are methods on the ideal and not on the generating set. Some other methods are less clear such as `basis_is_groebner()` and `interreduced_basis()`. These could perhaps be moved to `PolynomialSequence`.

> I am aware that the ideals implicitly contain the term order, though I found that a somewhat mixed blessing in #10708.

I wouldn't say this is because of the containment of term orderings but because of lack of care dealing with them?


---

Comment by vbraun created at 2011-02-26 20:16:38

Replying to [comment:17 malb]:
it was this method's name which sparked the debate we're having between William and myself. 

We are having? Where? Or you were having at one point (and if yes, did you decide anything)?


---

Comment by malb created at 2011-02-26 21:06:13

Replying to [comment:18 vbraun]:
> Replying to [comment:17 malb]:
> it was this method's name which sparked the debate we're having between William and myself. 
> 
> We are having? Where? Or you were having at one point (and if yes, did you decide anything)?

Sorry, my English failed me: William and I had a debate about whether ideal class == list of polynomials a few years back (October 2006). It was essentially about the same issue which we are discussion here now (I realised while double checking that it wasn't about `basis_is_groebner()` but about the return type of `groebner_basis()`) The decision was: ideals are objects in their own right in Sage and not lists of polynomials.

Should we move this discussion to [sage-devel]?


---

Comment by vbraun created at 2011-02-26 21:22:54

Now that I see some of the bigger picture I'm happy with distinguishing ideals and polynomial sequences in the way you are implementing. I don't quite get how the multiple parts of the polynomial sequence are supposed to fit into this. The documentation should either stress that this is optional (and that, by default, there is only a unique part) or separate this functionality into a derived class. 

Some other suggestions, though that could easily be postponed to followup tickets:
  * Document the relationship between ideals and polynomial sequences in the ideals module.
  * An alias `MPolynomialIdeal.basis` = `MPolynomialIdeal.gens`
  * Move `MPolynomialIdeal.basis_is_groebner` to `PolynomialSequence.is_groebner`
  * Move `MPolynomialIdeal.interreduced_basis` to `PolynomialSequence.interreduce` and make it return a `PolynomialSequence` instead of a list.
  * there shouldn't be a `PolynomialSequence.groebner_basis`
  * Perhaps move `MPolynomialIdeal.weil_restriction` since you say that it depends on the presentation.


---

Comment by malb created at 2011-02-26 22:16:09

Replying to [comment:20 vbraun]:
> Now that I see some of the bigger picture I'm happy with distinguishing ideals and polynomial sequences in the way you are implementing. I don't quite get how the multiple parts of the polynomial sequence are supposed to fit into this. The documentation should either stress that this is optional (and that, by default, there is only a unique part)

Good idea.

> Some other suggestions, though that could easily be postponed to followup tickets:
>   * Document the relationship between ideals and polynomial sequences in the ideals module.

Done.

>   * An alias `MPolynomialIdeal.basis` = `MPolynomialIdeal.gens`
>   * Move `MPolynomialIdeal.basis_is_groebner` to `PolynomialSequence.is_groebner`
>   * Move `MPolynomialIdeal.interreduced_basis` to `PolynomialSequence.interreduce` and make it return a `PolynomialSequence` instead of a list.
>   * there shouldn't be a `PolynomialSequence.groebner_basis`

This is now #10856.

>   * Perhaps move `MPolynomialIdeal.weil_restriction` since you say that it depends on the presentation.

Thinking about it: it's about the variety and thus can stay with the ideals.


---

Comment by malb created at 2011-02-26 22:18:01

The attached updated patch clarifies "parts" and the relation between ideals and polynomial sequences.


---

Comment by vbraun created at 2011-02-26 22:38:19

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2011-02-26 22:38:19

Ok looks good to me. Applies to Sage-4.6.2.rc1, too.


---

Comment by jdemeyer created at 2011-02-28 19:36:39

There is a Sphinx warning:

```
mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py:docstring of sage.rings.polynomial.multi_polynomial_ideal:206: (ERROR/3) Unknown interpreted text role "cls".
```



---

Comment by jdemeyer created at 2011-02-28 19:36:39

Changing status from positive_review to needs_work.


---

Comment by malb created at 2011-02-28 20:05:56

rebased to 4.6.2.alpha4


---

Attachment

diff of this version of the patch and the last version


---

Comment by malb created at 2011-02-28 20:07:56

The updated attached patch fixes the reported issue. However, I'm not setting this to *positive review* myself since I fixed a few more formating issues wrt to the reference manual. I also a diff between the current and the previous version of the patch for easy reviewing of those changes.


---

Comment by malb created at 2011-02-28 20:07:56

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2011-02-28 20:15:32

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2011-02-28 20:15:32

Looks good. Fixes the documentation warning.


---

Comment by jdemeyer created at 2011-03-08 21:45:01

Resolution: fixed
