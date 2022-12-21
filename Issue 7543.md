# Issue 7543: Add S-adiques to the word generator

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2009-11-27 15:27:44

Assignee: mhansen

CC:  vdelecroix saliola

The definition of S-adiques words is found here :

[Pytheas S-adiques](https://www.lirmm.fr/arith/wiki/PytheasFogg/S-adiques)

This patch adds S-adiques to the word generator :


```
    sage: tm = WordMorphism('a->ab,b->ba')
    sage: fib = WordMorphism('a->ab,b->a')
    sage: from itertools import repeat

One trivial example of infinite s-adique word::

    sage: words.s_adique(repeat(tm),repeat('a'))
    word: abbabaabbaababbabaababbaabbabaabbaababba...

A less trivial infinite s-adique word::

    sage: m = WordMorphism({0:tm,1:fib})
    sage: tmword = words.ThueMorseWord()
    sage: w = m(tmword)
    sage: words.s_adique(w, repeat('a'))
    word: abbaababbaabbaabbaababbaababbaabbaababba...

Random infinite s-adique words::

    sage: from sage.misc.prandom import randint
    sage: def it():
    ...     while True: yield randint(0,1)
    sage: words.s_adique(it(), repeat('a'), [tm,fib])
    word: abbaabababbaababbaabbaababbaabababbaabba...
    sage: words.s_adique(it(), repeat('a'), [tm,fib])
```


See the patch for more examples.


---

Comment by slabbe created at 2009-11-27 15:46:06

Changing status from new to needs_review.


---

Comment by slabbe created at 2009-12-08 12:10:45

Changing assignee from mhansen to slabbe.


---

Comment by slabbe created at 2009-12-08 12:10:45

I just updated the patch (doctest improvements) :


```
    sage: t = words.ThueMorseWord([tm,fib])
    sage: words.s_adique(t, repeat('a'))
    word: abbaababbaabbaabbaababbaababbaabbaababba...
```


I am wondering if I should add a `#random` where I use random examples. Sometimes, other computers gets different random sequence of numbers in the doctest routine...


---

Comment by slabbe created at 2009-12-18 21:58:44

I just uploaded the patch. Some more examples. Better doc. The morphisms arguments can now be a callable so that the following works:


```
    sage: x = lambda h:WordMorphism({1:[2],2:[3]+[1]*(h+1),3:[3]+[1]*h})
    sage: for h in [0,1,2,3]: print h, x(h)
    0 WordMorphism: 1->2, 2->31, 3->3
    1 WordMorphism: 1->2, 2->311, 3->31
    2 WordMorphism: 1->2, 2->3111, 3->311
    3 WordMorphism: 1->2, 2->31111, 3->3111
    sage: w = Word(lambda n : valuation(n+1, 2) ); w
    word: 0102010301020104010201030102010501020103...
    sage: s = words.s_adique(w, repeat(3), x); s
    word: 3232232232322322322323223223232232232232...
    sage: prefixe = s[:10000]
    sage: map(prefixe.number_of_factors, range(15))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    sage: [_[i+1] - _[i] for i in range(len(_)-1)]
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```



---

Attachment

Hi Sebastien,

I made the following changes in the documentation and the code seems to be OK.

   * In english the term is adic (like p-adic numbers)
   * I added lines between the item of the INPUT (http://www.sagemath.org/doc/developer/conventions.html#documentation-strings)

Take care,
Vincent


---

Comment by vdelecroix created at 2009-12-29 11:25:49

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2009-12-29 11:40:46

corrections in documentation string


---

Attachment


---

Comment by slabbe created at 2009-12-30 10:21:53

Thanks for the review Vincent. I agree with your changes.

There are two lines that should be keep "s-adiques" : the reference html to pytheas. Will post a patch soon.


---

Comment by slabbe created at 2009-12-30 10:21:53

Changing status from positive_review to needs_work.


---

Comment by slabbe created at 2009-12-30 10:41:49

Vincent, I let you change the status to positive review.


---

Comment by slabbe created at 2009-12-30 10:41:49

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2010-01-06 16:38:43

I just uploaded the corrections patch because I did some doc and sphinx improvements.

Vincent, can you review those small changes I did?


---

Comment by slabbe created at 2010-01-06 16:44:12

Applies over the precedent 2 patches.


---

Comment by vdelecroix created at 2010-01-07 23:38:59

Changing status from needs_review to positive_review.


---

Attachment

Replying to [comment:8 slabbe]:
> I just uploaded the corrections patch because I did some doc and sphinx improvements.
> 
> Vincent, can you review those small changes I did?

The doc is OK. positive review.


---

Comment by rlm created at 2010-01-13 09:21:08

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-01-13 09:21:08


```
The following tests failed:

        sage -t -long devel/sage-main/sage/combinat/words/word_generators.py # 23 doctests failed
        sage -t -long devel/sage-main/sage/categories/hopf_algebras_with_basis.py # Segfault
```



---

Comment by slabbe created at 2010-01-13 11:33:37

Apply only this one.


---

Attachment

Sorry for that. There was something depending on patches at #7520. I commented out the offending line and now it should be fine.

Beware, I folded all patches in the same "final" one.

Needs review again!


---

Comment by slabbe created at 2010-01-13 11:38:27

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2010-01-15 11:37:02

> I commented out the offending line and now it should be fine.

Vincent, to help you make the final review, here is what I changed in the patch to correct the failed doctests (the parameter check doesn't exist yet):

```
- kwds['check'] = False  
+ #kwds['check'] = False 
```

> Beware, I folded all patches in the same "final" one.
> 
> Needs review again!


---

Comment by vdelecroix created at 2010-01-15 14:07:45

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2010-01-15 14:07:45

In the .identity_morphism() there a big problem with infinite alphabet ! The following will never finish


```
sage: W = Words(alphabet=Alphabet(name="NN"))
sage: W.identity_morphism()
```


Anyway, it seems that WordMorphism is not implemented for infinite alphabet. Could you just raise an Error saying "Not implemented for infinite alphabet" or something like this ?

The rest is OK (I've got no doctesting error with the patch applied on a native 4.3 release)


---

Attachment

This patch applies over the above 'final' patch.


---

Comment by slabbe created at 2010-01-15 17:40:03

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2010-01-15 17:40:03

> Anyway, it seems that WordMorphism is not implemented for infinite alphabet. Could you just raise an Error saying "Not implemented for infinite alphabet" or something like this ?

Done. Thanks for finding this problem. Needs review again!


---

Comment by vdelecroix created at 2010-01-15 20:10:29

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2010-01-15 20:10:29

Knowing that

```
sage: timeit('W.size_of_alphabet() not in ZZ')
625 loops, best of 3: 24 µs per loop
sage: timeit('W.size_of_alphabet() is Infinity')
625 loops, best of 3: 3.43 µs per loop
```


We can win 21 micro seconds (at least on my computer) ! As it not important I switch to postive review... 

Nice patch this sadic one !


---

Comment by rlm created at 2010-01-18 23:45:53

Resolution: fixed
