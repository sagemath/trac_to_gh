# Issue 7543: Add S-adiques to the word generator

archive/issues_007543.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @videlec @saliola\n\nThe definition of S-adiques words is found here :\n\n[Pytheas S-adiques](https://www.lirmm.fr/arith/wiki/PytheasFogg/S-adiques)\n\nThis patch adds S-adiques to the word generator :\n\n\n```\n    sage: tm = WordMorphism('a->ab,b->ba')\n    sage: fib = WordMorphism('a->ab,b->a')\n    sage: from itertools import repeat\n\nOne trivial example of infinite s-adique word::\n\n    sage: words.s_adique(repeat(tm),repeat('a'))\n    word: abbabaabbaababbabaababbaabbabaabbaababba...\n\nA less trivial infinite s-adique word::\n\n    sage: m = WordMorphism({0:tm,1:fib})\n    sage: tmword = words.ThueMorseWord()\n    sage: w = m(tmword)\n    sage: words.s_adique(w, repeat('a'))\n    word: abbaababbaabbaabbaababbaababbaabbaababba...\n\nRandom infinite s-adique words::\n\n    sage: from sage.misc.prandom import randint\n    sage: def it():\n    ...     while True: yield randint(0,1)\n    sage: words.s_adique(it(), repeat('a'), [tm,fib])\n    word: abbaabababbaababbaabbaababbaabababbaabba...\n    sage: words.s_adique(it(), repeat('a'), [tm,fib])\n```\n\n\nSee the patch for more examples.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7543\n\n",
    "created_at": "2009-11-27T15:27:44Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Add S-adiques to the word generator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7543",
    "user": "https://github.com/seblabbe"
}
```
Assignee: @mwhansen

CC:  @videlec @saliola

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

Issue created by migration from https://trac.sagemath.org/ticket/7543





---

archive/issue_comments_063883.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-27T15:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63883",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063884.json:
```json
{
    "body": "Changing assignee from @mwhansen to @seblabbe.",
    "created_at": "2009-12-08T12:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63884",
    "user": "https://github.com/seblabbe"
}
```

Changing assignee from @mwhansen to @seblabbe.



---

archive/issue_comments_063885.json:
```json
{
    "body": "I just updated the patch (doctest improvements) :\n\n\n```\n    sage: t = words.ThueMorseWord([tm,fib])\n    sage: words.s_adique(t, repeat('a'))\n    word: abbaababbaabbaabbaababbaababbaabbaababba...\n```\n\n\nI am wondering if I should add a `#random` where I use random examples. Sometimes, other computers gets different random sequence of numbers in the doctest routine...",
    "created_at": "2009-12-08T12:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63885",
    "user": "https://github.com/seblabbe"
}
```

I just updated the patch (doctest improvements) :


```
    sage: t = words.ThueMorseWord([tm,fib])
    sage: words.s_adique(t, repeat('a'))
    word: abbaababbaabbaabbaababbaababbaabbaababba...
```


I am wondering if I should add a `#random` where I use random examples. Sometimes, other computers gets different random sequence of numbers in the doctest routine...



---

archive/issue_comments_063886.json:
```json
{
    "body": "I just uploaded the patch. Some more examples. Better doc. The morphisms arguments can now be a callable so that the following works:\n\n\n```\n    sage: x = lambda h:WordMorphism({1:[2],2:[3]+[1]*(h+1),3:[3]+[1]*h})\n    sage: for h in [0,1,2,3]: print h, x(h)\n    0 WordMorphism: 1->2, 2->31, 3->3\n    1 WordMorphism: 1->2, 2->311, 3->31\n    2 WordMorphism: 1->2, 2->3111, 3->311\n    3 WordMorphism: 1->2, 2->31111, 3->3111\n    sage: w = Word(lambda n : valuation(n+1, 2) ); w\n    word: 0102010301020104010201030102010501020103...\n    sage: s = words.s_adique(w, repeat(3), x); s\n    word: 3232232232322322322323223223232232232232...\n    sage: prefixe = s[:10000]\n    sage: map(prefixe.number_of_factors, range(15))\n    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]\n    sage: [_[i+1] - _[i] for i in range(len(_)-1)]\n    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]\n```\n",
    "created_at": "2009-12-18T21:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63886",
    "user": "https://github.com/seblabbe"
}
```

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

archive/issue_comments_063887.json:
```json
{
    "body": "Attachment [trac_7543_word_s_adiques-sl.patch](tarball://root/attachments/some-uuid/ticket7543/trac_7543_word_s_adiques-sl.patch) by @videlec created at 2009-12-29 11:25:49\n\nHi Sebastien,\n\nI made the following changes in the documentation and the code seems to be OK.\n\n* In english the term is adic (like p-adic numbers)\n* I added lines between the item of the INPUT (http://www.sagemath.org/doc/developer/conventions.html#documentation-strings)\n\nTake care,\nVincent",
    "created_at": "2009-12-29T11:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63887",
    "user": "https://github.com/videlec"
}
```

Attachment [trac_7543_word_s_adiques-sl.patch](tarball://root/attachments/some-uuid/ticket7543/trac_7543_word_s_adiques-sl.patch) by @videlec created at 2009-12-29 11:25:49

Hi Sebastien,

I made the following changes in the documentation and the code seems to be OK.

* In english the term is adic (like p-adic numbers)
* I added lines between the item of the INPUT (http://www.sagemath.org/doc/developer/conventions.html#documentation-strings)

Take care,
Vincent



---

archive/issue_comments_063888.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-29T11:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63888",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063889.json:
```json
{
    "body": "corrections in documentation string",
    "created_at": "2009-12-29T11:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63889",
    "user": "https://github.com/videlec"
}
```

corrections in documentation string



---

archive/issue_comments_063890.json:
```json
{
    "body": "Attachment [trac_7543-review-vd.patch](tarball://root/attachments/some-uuid/ticket7543/trac_7543-review-vd.patch) by @videlec created at 2009-12-29 11:42:23",
    "created_at": "2009-12-29T11:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63890",
    "user": "https://github.com/videlec"
}
```

Attachment [trac_7543-review-vd.patch](tarball://root/attachments/some-uuid/ticket7543/trac_7543-review-vd.patch) by @videlec created at 2009-12-29 11:42:23



---

archive/issue_comments_063891.json:
```json
{
    "body": "Thanks for the review Vincent. I agree with your changes.\n\nThere are two lines that should be keep \"s-adiques\" : the reference html to pytheas. Will post a patch soon.",
    "created_at": "2009-12-30T10:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63891",
    "user": "https://github.com/seblabbe"
}
```

Thanks for the review Vincent. I agree with your changes.

There are two lines that should be keep "s-adiques" : the reference html to pytheas. Will post a patch soon.



---

archive/issue_comments_063892.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-30T10:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63892",
    "user": "https://github.com/seblabbe"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063893.json:
```json
{
    "body": "Vincent, I let you change the status to positive review.",
    "created_at": "2009-12-30T10:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63893",
    "user": "https://github.com/seblabbe"
}
```

Vincent, I let you change the status to positive review.



---

archive/issue_comments_063894.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-30T10:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63894",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063895.json:
```json
{
    "body": "I just uploaded the corrections patch because I did some doc and sphinx improvements.\n\nVincent, can you review those small changes I did?",
    "created_at": "2010-01-06T16:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63895",
    "user": "https://github.com/seblabbe"
}
```

I just uploaded the corrections patch because I did some doc and sphinx improvements.

Vincent, can you review those small changes I did?



---

archive/issue_comments_063896.json:
```json
{
    "body": "Applies over the precedent 2 patches.",
    "created_at": "2010-01-06T16:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63896",
    "user": "https://github.com/seblabbe"
}
```

Applies over the precedent 2 patches.



---

archive/issue_comments_063897.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-07T23:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63897",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063898.json:
```json
{
    "body": "Attachment [trac_7543_correction-sl.patch](tarball://root/attachments/some-uuid/ticket7543/trac_7543_correction-sl.patch) by @videlec created at 2010-01-07 23:38:59\n\nReplying to [comment:8 slabbe]:\n> I just uploaded the corrections patch because I did some doc and sphinx improvements.\n> \n> Vincent, can you review those small changes I did?\n\nThe doc is OK. positive review.",
    "created_at": "2010-01-07T23:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63898",
    "user": "https://github.com/videlec"
}
```

Attachment [trac_7543_correction-sl.patch](tarball://root/attachments/some-uuid/ticket7543/trac_7543_correction-sl.patch) by @videlec created at 2010-01-07 23:38:59

Replying to [comment:8 slabbe]:
> I just uploaded the corrections patch because I did some doc and sphinx improvements.
> 
> Vincent, can you review those small changes I did?

The doc is OK. positive review.



---

archive/issue_comments_063899.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-13T09:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63899",
    "user": "https://github.com/rlmill"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063900.json:
```json
{
    "body": "\n```\nThe following tests failed:\n\n        sage -t -long devel/sage-main/sage/combinat/words/word_generators.py # 23 doctests failed\n        sage -t -long devel/sage-main/sage/categories/hopf_algebras_with_basis.py # Segfault\n```\n",
    "created_at": "2010-01-13T09:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63900",
    "user": "https://github.com/rlmill"
}
```


```
The following tests failed:

        sage -t -long devel/sage-main/sage/combinat/words/word_generators.py # 23 doctests failed
        sage -t -long devel/sage-main/sage/categories/hopf_algebras_with_basis.py # Segfault
```




---

archive/issue_comments_063901.json:
```json
{
    "body": "Apply only this one.",
    "created_at": "2010-01-13T11:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63901",
    "user": "https://github.com/seblabbe"
}
```

Apply only this one.



---

archive/issue_comments_063902.json:
```json
{
    "body": "Attachment [trac_7543_s_adic_final.patch](tarball://root/attachments/some-uuid/ticket7543/trac_7543_s_adic_final.patch) by @seblabbe created at 2010-01-13 11:38:27\n\nSorry for that. There was something depending on patches at #7520. I commented out the offending line and now it should be fine.\n\nBeware, I folded all patches in the same \"final\" one.\n\nNeeds review again!",
    "created_at": "2010-01-13T11:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63902",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_7543_s_adic_final.patch](tarball://root/attachments/some-uuid/ticket7543/trac_7543_s_adic_final.patch) by @seblabbe created at 2010-01-13 11:38:27

Sorry for that. There was something depending on patches at #7520. I commented out the offending line and now it should be fine.

Beware, I folded all patches in the same "final" one.

Needs review again!



---

archive/issue_comments_063903.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-13T11:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63903",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063904.json:
```json
{
    "body": "> I commented out the offending line and now it should be fine.\n\nVincent, to help you make the final review, here is what I changed in the patch to correct the failed doctests (the parameter check doesn't exist yet):\n\n```\n- kwds['check'] = False  \n+ #kwds['check'] = False \n```\n\n> Beware, I folded all patches in the same \"final\" one.\n> \n> Needs review again!",
    "created_at": "2010-01-15T11:37:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63904",
    "user": "https://github.com/seblabbe"
}
```

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

archive/issue_comments_063905.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-15T14:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63905",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063906.json:
```json
{
    "body": "In the .identity_morphism() there a big problem with infinite alphabet ! The following will never finish\n\n\n```\nsage: W = Words(alphabet=Alphabet(name=\"NN\"))\nsage: W.identity_morphism()\n```\n\n\nAnyway, it seems that WordMorphism is not implemented for infinite alphabet. Could you just raise an Error saying \"Not implemented for infinite alphabet\" or something like this ?\n\nThe rest is OK (I've got no doctesting error with the patch applied on a native 4.3 release)",
    "created_at": "2010-01-15T14:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63906",
    "user": "https://github.com/videlec"
}
```

In the .identity_morphism() there a big problem with infinite alphabet ! The following will never finish


```
sage: W = Words(alphabet=Alphabet(name="NN"))
sage: W.identity_morphism()
```


Anyway, it seems that WordMorphism is not implemented for infinite alphabet. Could you just raise an Error saying "Not implemented for infinite alphabet" or something like this ?

The rest is OK (I've got no doctesting error with the patch applied on a native 4.3 release)



---

archive/issue_comments_063907.json:
```json
{
    "body": "Attachment [trac_7543_infinite_alphabet-sl.patch](tarball://root/attachments/some-uuid/ticket7543/trac_7543_infinite_alphabet-sl.patch) by @seblabbe created at 2010-01-15 17:37:52\n\nThis patch applies over the above 'final' patch.",
    "created_at": "2010-01-15T17:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63907",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_7543_infinite_alphabet-sl.patch](tarball://root/attachments/some-uuid/ticket7543/trac_7543_infinite_alphabet-sl.patch) by @seblabbe created at 2010-01-15 17:37:52

This patch applies over the above 'final' patch.



---

archive/issue_comments_063908.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-15T17:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63908",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063909.json:
```json
{
    "body": "> Anyway, it seems that WordMorphism is not implemented for infinite alphabet. Could you just raise an Error saying \"Not implemented for infinite alphabet\" or something like this ?\n\nDone. Thanks for finding this problem. Needs review again!",
    "created_at": "2010-01-15T17:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63909",
    "user": "https://github.com/seblabbe"
}
```

> Anyway, it seems that WordMorphism is not implemented for infinite alphabet. Could you just raise an Error saying "Not implemented for infinite alphabet" or something like this ?

Done. Thanks for finding this problem. Needs review again!



---

archive/issue_comments_063910.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-15T20:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63910",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063911.json:
```json
{
    "body": "Knowing that\n\n```\nsage: timeit('W.size_of_alphabet() not in ZZ')\n625 loops, best of 3: 24 \u00b5s per loop\nsage: timeit('W.size_of_alphabet() is Infinity')\n625 loops, best of 3: 3.43 \u00b5s per loop\n```\n\n\nWe can win 21 micro seconds (at least on my computer) ! As it not important I switch to postive review... \n\nNice patch this sadic one !",
    "created_at": "2010-01-15T20:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63911",
    "user": "https://github.com/videlec"
}
```

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

archive/issue_events_007773.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-18T23:45:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7543#event-7773"
}
```



---

archive/issue_comments_063912.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T23:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7543#issuecomment-63912",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
