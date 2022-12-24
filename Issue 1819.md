# Issue 1819: move crypto.mq.MPolynomialSystem somewhere else

archive/issues_001819.json:
```json
{
    "body": "Assignee: malb\n\nCC:  sbulygin mhampton\n\nThough it is motivated by cryptography it is not specific to it, maybe move it to `sage.rings.polynomial` after all ideals are there as well?\n\nIssue created by migration from https://trac.sagemath.org/ticket/1819\n\n",
    "created_at": "2008-01-18T00:29:31Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "title": "move crypto.mq.MPolynomialSystem somewhere else",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1819",
    "user": "malb"
}
```
Assignee: malb

CC:  sbulygin mhampton

Though it is motivated by cryptography it is not specific to it, maybe move it to `sage.rings.polynomial` after all ideals are there as well?

Issue created by migration from https://trac.sagemath.org/ticket/1819





---

archive/issue_comments_011488.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-13T17:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11488",
    "user": "malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_011489.json:
```json
{
    "body": "There are a few minor doctest failures:\n\n\n```\nsage -t  -long -force_lib devel/sage/sage/rings/residue_field.pyx # 3 doctests failed\nsage -t  -long -force_lib devel/sage/sage/rings/ideal.py # 1 doctests failed\nsage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_sequence.py # 2 doctests failed\nsage -t  -long -force_lib devel/sage/sage/tests/cmdline.py # 1 doctests failed\n```\n",
    "created_at": "2011-01-13T21:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11489",
    "user": "malb"
}
```

There are a few minor doctest failures:


```
sage -t  -long -force_lib devel/sage/sage/rings/residue_field.pyx # 3 doctests failed
sage -t  -long -force_lib devel/sage/sage/rings/ideal.py # 1 doctests failed
sage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_sequence.py # 2 doctests failed
sage -t  -long -force_lib devel/sage/sage/tests/cmdline.py # 1 doctests failed
```




---

archive/issue_comments_011490.json:
```json
{
    "body": "The attached patch takes care of those doctest failures (except for the cmdline one which is not due to this patch)",
    "created_at": "2011-01-14T14:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11490",
    "user": "malb"
}
```

The attached patch takes care of those doctest failures (except for the cmdline one which is not due to this patch)



---

archive/issue_comments_011491.json:
```json
{
    "body": "Hi, can one of you two take a look at this patch? Cheers.",
    "created_at": "2011-01-22T14:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11491",
    "user": "malb"
}
```

Hi, can one of you two take a look at this patch? Cheers.



---

archive/issue_comments_011492.json:
```json
{
    "body": "Btw. patchbot reports \"Apply failed\" because the patch is for 4.6.2.alpha4 instead of 4.6.1.",
    "created_at": "2011-02-18T14:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11492",
    "user": "malb"
}
```

Btw. patchbot reports "Apply failed" because the patch is for 4.6.2.alpha4 instead of 4.6.1.



---

archive/issue_comments_011493.json:
```json
{
    "body": "The whole rename looks reasonable to me.\n\nHaving said that, I don't understand why we need both `MPolynomialIdeal` and `PolynomialSequence`. It seems to be that both are essentially containers for polynomials in a common ring. Maybe the methods of `PolynomialSequence` could just be merged with the ideal code? Do you have any thoughts about that?",
    "created_at": "2011-02-26T17:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11493",
    "user": "vbraun"
}
```

The whole rename looks reasonable to me.

Having said that, I don't understand why we need both `MPolynomialIdeal` and `PolynomialSequence`. It seems to be that both are essentially containers for polynomials in a common ring. Maybe the methods of `PolynomialSequence` could just be merged with the ideal code? Do you have any thoughts about that?



---

archive/issue_comments_011494.json:
```json
{
    "body": "Replying to [comment:10 vbraun]:\n> Having said that, I don't understand why we need both `MPolynomialIdeal` and \n> `PolynomialSequence`. It seems to be that both are essentially containers for \n> polynomials in a common ring. Maybe the methods of `PolynomialSequence` could just\n> be merged with the ideal code? Do you have any thoughts about that?\n\nI disagree with merging the two. Ideal are not the same as sequences of polynomials: ideals may be infinite, but our polynomial sequences are always finite. Furthermore, some methods don't make sense on ideals but do make sense for sequences of polynomials such as interreduction and weil restriction. That we have those methods on ideals now is not proper, I'd say. Another example: set operations on ideals are different from set operations on polynomial sequences.",
    "created_at": "2011-02-26T17:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11494",
    "user": "malb"
}
```

Replying to [comment:10 vbraun]:
> Having said that, I don't understand why we need both `MPolynomialIdeal` and 
> `PolynomialSequence`. It seems to be that both are essentially containers for 
> polynomials in a common ring. Maybe the methods of `PolynomialSequence` could just
> be merged with the ideal code? Do you have any thoughts about that?

I disagree with merging the two. Ideal are not the same as sequences of polynomials: ideals may be infinite, but our polynomial sequences are always finite. Furthermore, some methods don't make sense on ideals but do make sense for sequences of polynomials such as interreduction and weil restriction. That we have those methods on ideals now is not proper, I'd say. Another example: set operations on ideals are different from set operations on polynomial sequences.



---

archive/issue_comments_011495.json:
```json
{
    "body": "Mathematically, they are of course not the same. But as far as the implementation goes, both are lists of polynomials with some methods attached. I don't understand your comment about finiteness, you can't generate a non-finitely generated ideal in Sage, nor could you construct the requisite infinite polynomial ring to evade Hilberts basis theorem. Moreover, I don't understand your comment about the `interreduced_basis` method in the ideal class. Where else but as a method of the ideal class should we define this functionality in OOP?",
    "created_at": "2011-02-26T17:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11495",
    "user": "vbraun"
}
```

Mathematically, they are of course not the same. But as far as the implementation goes, both are lists of polynomials with some methods attached. I don't understand your comment about finiteness, you can't generate a non-finitely generated ideal in Sage, nor could you construct the requisite infinite polynomial ring to evade Hilberts basis theorem. Moreover, I don't understand your comment about the `interreduced_basis` method in the ideal class. Where else but as a method of the ideal class should we define this functionality in OOP?



---

archive/issue_comments_011496.json:
```json
{
    "body": "Replying to [comment:12 vbraun]:\n> Mathematically, they are of course not the same. But as far as the implementation goes, both are lists of polynomials with some methods attached. I don't understand your comment about finiteness, you can't generate a non-finitely generated ideal in Sage, nor could you construct the requisite infinite polynomial ring to evade Hilberts basis theorem. Moreover, I don't understand your comment about the `interreduced_basis` method in the ideal class. Where else but as a method of the ideal class should we define this functionality in OOP?\n\nI meant infinite but finitely generated which is for example relevant for set operations on them. Another example is reduction: reduction modulo the ideal is different from reduction modulo a list of polynomials. The method `interreduced_basis` assumes a particular basis for the ideal, i.e. violates the distinction between ideal and a list of polynomials. I'd say we should aim to have methods on ideals deal with ideals instead of the particular basis the user chose when constructing it.",
    "created_at": "2011-02-26T18:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11496",
    "user": "malb"
}
```

Replying to [comment:12 vbraun]:
> Mathematically, they are of course not the same. But as far as the implementation goes, both are lists of polynomials with some methods attached. I don't understand your comment about finiteness, you can't generate a non-finitely generated ideal in Sage, nor could you construct the requisite infinite polynomial ring to evade Hilberts basis theorem. Moreover, I don't understand your comment about the `interreduced_basis` method in the ideal class. Where else but as a method of the ideal class should we define this functionality in OOP?

I meant infinite but finitely generated which is for example relevant for set operations on them. Another example is reduction: reduction modulo the ideal is different from reduction modulo a list of polynomials. The method `interreduced_basis` assumes a particular basis for the ideal, i.e. violates the distinction between ideal and a list of polynomials. I'd say we should aim to have methods on ideals deal with ideals instead of the particular basis the user chose when constructing it.



---

archive/issue_comments_011497.json:
```json
{
    "body": "In principle, it would be nice if the ideal class could represent some basis-free abstract notion of ideal. In practice, this is not possible as all non-trivial computations are exponential complexity due to the need for Groebner bases. Even worse, the Groebner basis computation often depends on a judiciously chosen term ordering which cannot be automated. This is why all computer algebra programs that I am aware of treat ideals as sequences of polynomials, and not as ideals in the mathematical sense. Barring any breakthrough in algebra it is not feasible to do otherwise.",
    "created_at": "2011-02-26T18:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11497",
    "user": "vbraun"
}
```

In principle, it would be nice if the ideal class could represent some basis-free abstract notion of ideal. In practice, this is not possible as all non-trivial computations are exponential complexity due to the need for Groebner bases. Even worse, the Groebner basis computation often depends on a judiciously chosen term ordering which cannot be automated. This is why all computer algebra programs that I am aware of treat ideals as sequences of polynomials, and not as ideals in the mathematical sense. Barring any breakthrough in algebra it is not feasible to do otherwise.



---

archive/issue_comments_011498.json:
```json
{
    "body": "I should have mentioned that the decision to treat ideals as such abstract basis-free objects was made before I joined the project, probably inherited from Magma. For example, cf. the intro of http://sagemath.org/doc/reference/sage/crypto/mq/mpolynomialsystem.html (which I admit to have written, though). Thus, many methods of the multivariate polynomial ideal class do compute a Gr\u00f6bner basis behind the scenes. Btw. since ideals know their ring and rings contain the term ordering in Sage, we can compute GBs without any additionally provided information.",
    "created_at": "2011-02-26T19:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11498",
    "user": "malb"
}
```

I should have mentioned that the decision to treat ideals as such abstract basis-free objects was made before I joined the project, probably inherited from Magma. For example, cf. the intro of http://sagemath.org/doc/reference/sage/crypto/mq/mpolynomialsystem.html (which I admit to have written, though). Thus, many methods of the multivariate polynomial ideal class do compute a Gröbner basis behind the scenes. Btw. since ideals know their ring and rings contain the term ordering in Sage, we can compute GBs without any additionally provided information.



---

archive/issue_comments_011499.json:
```json
{
    "body": "I don't see that anywhere in the `MPolynomialIdeal` class. Correct me if I'm wrong, but the chosen generators and their order is immutable. Even when computing a Groebner basis, the generators are not replaced by this much more useful basis. On the other hand, there are methods like `basis_is_groebner()` which are obviously basis-dependent. It seems to me that Sage implements ideals very much as an immutable sequence of polynomials with some methods attached. The individual methods do, of course, need Groebner bases but they never change the underlying sequence of polynomials.\n\nI am aware that the ideals implicitly contain the term order, though I found that a somewhat mixed blessing in #10708.",
    "created_at": "2011-02-26T19:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11499",
    "user": "vbraun"
}
```

I don't see that anywhere in the `MPolynomialIdeal` class. Correct me if I'm wrong, but the chosen generators and their order is immutable. Even when computing a Groebner basis, the generators are not replaced by this much more useful basis. On the other hand, there are methods like `basis_is_groebner()` which are obviously basis-dependent. It seems to me that Sage implements ideals very much as an immutable sequence of polynomials with some methods attached. The individual methods do, of course, need Groebner bases but they never change the underlying sequence of polynomials.

I am aware that the ideals implicitly contain the term order, though I found that a somewhat mixed blessing in #10708.



---

archive/issue_comments_011500.json:
```json
{
    "body": "Replying to [comment:16 vbraun]:\n> I don't see that anywhere in the `MPolynomialIdeal` class. Correct me if I'm wrong,\n> but the chosen generators and their order is immutable. \n\nYep.\n\n> Even when computing a Groebner basis, the generators are not replaced by this much \n> more useful basis. \n\nBut the GB is cached and used for \"interesting\" operations.\n\n> On the other hand, there are methods like `basis_is_groebner()` which are obviously\n> basis-dependent. \n\nThis was the compromise reached to (a) keep the notion that ideals are different objects than their generators and to (b) still allow to query some information about the basis. We should have separated stuff back then perhaps. In any case, it was this method's name which sparked the debate we're having between William and myself. \n\n> It seems to me that Sage implements ideals very much as an immutable sequence of \n> polynomials with some methods attached. \n\nI'd say: it attempts to present a view on ideals which abstracts away chosen bases but with varying success.\n\n> The individual methods do, of course, need Groebner bases but they never change the > underlying sequence of polynomials.\n\nBut e.g. `intersection()` and `reduce()` actually use the GB and not the provided basis, they are methods on the ideal and not on the generating set. Some other methods are less clear such as `basis_is_groebner()` and `interreduced_basis()`. These could perhaps be moved to `PolynomialSequence`.\n\n> I am aware that the ideals implicitly contain the term order, though I found that a somewhat mixed blessing in #10708.\n\nI wouldn't say this is because of the containment of term orderings but because of lack of care dealing with them?",
    "created_at": "2011-02-26T20:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11500",
    "user": "malb"
}
```

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

archive/issue_comments_011501.json:
```json
{
    "body": "Replying to [comment:17 malb]:\nit was this method's name which sparked the debate we're having between William and myself. \n\nWe are having? Where? Or you were having at one point (and if yes, did you decide anything)?",
    "created_at": "2011-02-26T20:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11501",
    "user": "vbraun"
}
```

Replying to [comment:17 malb]:
it was this method's name which sparked the debate we're having between William and myself. 

We are having? Where? Or you were having at one point (and if yes, did you decide anything)?



---

archive/issue_comments_011502.json:
```json
{
    "body": "Replying to [comment:18 vbraun]:\n> Replying to [comment:17 malb]:\n> it was this method's name which sparked the debate we're having between William and myself. \n> \n> We are having? Where? Or you were having at one point (and if yes, did you decide anything)?\n\nSorry, my English failed me: William and I had a debate about whether ideal class == list of polynomials a few years back (October 2006). It was essentially about the same issue which we are discussion here now (I realised while double checking that it wasn't about `basis_is_groebner()` but about the return type of `groebner_basis()`) The decision was: ideals are objects in their own right in Sage and not lists of polynomials.\n\nShould we move this discussion to [sage-devel]?",
    "created_at": "2011-02-26T21:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11502",
    "user": "malb"
}
```

Replying to [comment:18 vbraun]:
> Replying to [comment:17 malb]:
> it was this method's name which sparked the debate we're having between William and myself. 
> 
> We are having? Where? Or you were having at one point (and if yes, did you decide anything)?

Sorry, my English failed me: William and I had a debate about whether ideal class == list of polynomials a few years back (October 2006). It was essentially about the same issue which we are discussion here now (I realised while double checking that it wasn't about `basis_is_groebner()` but about the return type of `groebner_basis()`) The decision was: ideals are objects in their own right in Sage and not lists of polynomials.

Should we move this discussion to [sage-devel]?



---

archive/issue_comments_011503.json:
```json
{
    "body": "Now that I see some of the bigger picture I'm happy with distinguishing ideals and polynomial sequences in the way you are implementing. I don't quite get how the multiple parts of the polynomial sequence are supposed to fit into this. The documentation should either stress that this is optional (and that, by default, there is only a unique part) or separate this functionality into a derived class. \n\nSome other suggestions, though that could easily be postponed to followup tickets:\n* Document the relationship between ideals and polynomial sequences in the ideals module.\n* An alias `MPolynomialIdeal.basis` = `MPolynomialIdeal.gens`\n* Move `MPolynomialIdeal.basis_is_groebner` to `PolynomialSequence.is_groebner`\n* Move `MPolynomialIdeal.interreduced_basis` to `PolynomialSequence.interreduce` and make it return a `PolynomialSequence` instead of a list.\n* there shouldn't be a `PolynomialSequence.groebner_basis`\n* Perhaps move `MPolynomialIdeal.weil_restriction` since you say that it depends on the presentation.",
    "created_at": "2011-02-26T21:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11503",
    "user": "vbraun"
}
```

Now that I see some of the bigger picture I'm happy with distinguishing ideals and polynomial sequences in the way you are implementing. I don't quite get how the multiple parts of the polynomial sequence are supposed to fit into this. The documentation should either stress that this is optional (and that, by default, there is only a unique part) or separate this functionality into a derived class. 

Some other suggestions, though that could easily be postponed to followup tickets:
* Document the relationship between ideals and polynomial sequences in the ideals module.
* An alias `MPolynomialIdeal.basis` = `MPolynomialIdeal.gens`
* Move `MPolynomialIdeal.basis_is_groebner` to `PolynomialSequence.is_groebner`
* Move `MPolynomialIdeal.interreduced_basis` to `PolynomialSequence.interreduce` and make it return a `PolynomialSequence` instead of a list.
* there shouldn't be a `PolynomialSequence.groebner_basis`
* Perhaps move `MPolynomialIdeal.weil_restriction` since you say that it depends on the presentation.



---

archive/issue_comments_011504.json:
```json
{
    "body": "Replying to [comment:20 vbraun]:\n> Now that I see some of the bigger picture I'm happy with distinguishing ideals and polynomial sequences in the way you are implementing. I don't quite get how the multiple parts of the polynomial sequence are supposed to fit into this. The documentation should either stress that this is optional (and that, by default, there is only a unique part)\n\nGood idea.\n\n> Some other suggestions, though that could easily be postponed to followup tickets:\n>   * Document the relationship between ideals and polynomial sequences in the ideals module.\n\nDone.\n\n>   * An alias `MPolynomialIdeal.basis` = `MPolynomialIdeal.gens`\n>   * Move `MPolynomialIdeal.basis_is_groebner` to `PolynomialSequence.is_groebner`\n>   * Move `MPolynomialIdeal.interreduced_basis` to `PolynomialSequence.interreduce` and make it return a `PolynomialSequence` instead of a list.\n>   * there shouldn't be a `PolynomialSequence.groebner_basis`\n\nThis is now #10856.\n\n>   * Perhaps move `MPolynomialIdeal.weil_restriction` since you say that it depends on the presentation.\n\nThinking about it: it's about the variety and thus can stay with the ideals.",
    "created_at": "2011-02-26T22:16:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11504",
    "user": "malb"
}
```

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

archive/issue_comments_011505.json:
```json
{
    "body": "The attached updated patch clarifies \"parts\" and the relation between ideals and polynomial sequences.",
    "created_at": "2011-02-26T22:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11505",
    "user": "malb"
}
```

The attached updated patch clarifies "parts" and the relation between ideals and polynomial sequences.



---

archive/issue_comments_011506.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-26T22:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11506",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_011507.json:
```json
{
    "body": "Ok looks good to me. Applies to Sage-4.6.2.rc1, too.",
    "created_at": "2011-02-26T22:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11507",
    "user": "vbraun"
}
```

Ok looks good to me. Applies to Sage-4.6.2.rc1, too.



---

archive/issue_comments_011508.json:
```json
{
    "body": "There is a Sphinx warning:\n\n```\nmnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py:docstring of sage.rings.polynomial.multi_polynomial_ideal:206: (ERROR/3) Unknown interpreted text role \"cls\".\n```\n",
    "created_at": "2011-02-28T19:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11508",
    "user": "jdemeyer"
}
```

There is a Sphinx warning:

```
mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py:docstring of sage.rings.polynomial.multi_polynomial_ideal:206: (ERROR/3) Unknown interpreted text role "cls".
```




---

archive/issue_comments_011509.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-02-28T19:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11509",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_011510.json:
```json
{
    "body": "rebased to 4.6.2.alpha4",
    "created_at": "2011-02-28T20:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11510",
    "user": "malb"
}
```

rebased to 4.6.2.alpha4



---

archive/issue_comments_011511.json:
```json
{
    "body": "Attachment [trac_1819.patch.diff](tarball://root/attachments/some-uuid/ticket1819/trac_1819.patch.diff) by malb created at 2011-02-28 20:06:23\n\ndiff of this version of the patch and the last version",
    "created_at": "2011-02-28T20:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11511",
    "user": "malb"
}
```

Attachment [trac_1819.patch.diff](tarball://root/attachments/some-uuid/ticket1819/trac_1819.patch.diff) by malb created at 2011-02-28 20:06:23

diff of this version of the patch and the last version



---

archive/issue_comments_011512.json:
```json
{
    "body": "The updated attached patch fixes the reported issue. However, I'm not setting this to **positive review** myself since I fixed a few more formating issues wrt to the reference manual. I also a diff between the current and the previous version of the patch for easy reviewing of those changes.",
    "created_at": "2011-02-28T20:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11512",
    "user": "malb"
}
```

The updated attached patch fixes the reported issue. However, I'm not setting this to **positive review** myself since I fixed a few more formating issues wrt to the reference manual. I also a diff between the current and the previous version of the patch for easy reviewing of those changes.



---

archive/issue_comments_011513.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-28T20:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11513",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_011514.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-28T20:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11514",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_011515.json:
```json
{
    "body": "Looks good. Fixes the documentation warning.",
    "created_at": "2011-02-28T20:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11515",
    "user": "vbraun"
}
```

Looks good. Fixes the documentation warning.



---

archive/issue_comments_011516.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-08T21:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1819#issuecomment-11516",
    "user": "jdemeyer"
}
```

Resolution: fixed
