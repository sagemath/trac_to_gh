# Issue 7405: Change the print of predefined words to the default behavior.

archive/issues_007405.json:
```json
{
    "body": "Assignee: slabbe\n\nCC:  saliola\n\nKeywords: words\n\nThis ticket concern 3 relatively small things.\n\n(1) Change the print of predefined words to the default behavior.\n\n(2) Correct a bug of `__mul__` of `WordMorphism.`\n\n(3) Adds the Fibonacci word defined from function.\n\n\nSee below for more explanations.\n\n(1) The `rename` function is used a lot for predefined words :\n\n\n```\nsage: words.FibonacciWord()\nFibonacci word over Ordered Alphabet [0, 1], defined recursively\nsage: words.FibonacciWord((0,1),'fixed point')\nFibonacci word over Ordered Alphabet [0, 1], defined as the fixed point of a morphism\nsage: words.ThueMorseWord(alphabet = (3,4))\nThue-Morse word over Ordered Alphabet [3, 4]\nsage: words.FixedPointOfMorphism('a->ab,b->ba','a')\nFixed point beginning with 'a' of the morphism WordMorphism: a->ab, b->ba\nsage: words.ChristoffelWord(4,7)\nLower Christoffel word of slope 4/7 over Ordered Alphabet [0, 1]\n```\n\n\nBut I more and more dislike this behavior made for the user since (1) it repeats the information already given by the user and (2) the first thing that the user do with the word is to look the prefix of the word (well, that's what I always do and that's what is done everywhere in the doctests).\n\nTo print a prefix, one needs to crete it (which is not always necessary for the user) :\n\n\n```\nsage: f = words.FibonacciWord()\nsage: f\nFibonacci word over Ordered Alphabet [0, 1], defined recursively\nsage: print f\nFibonacci word over Ordered Alphabet [0, 1], defined recursively\nsage: f[:100]\nword: 0100101001001010010100100101001001010010...\nsage: print f[:100]\nword: 0100101001001010010100100101001001010010100100101001010010010100100101001010010010100100101001010010\n```\n\n\nI would simply like the following to work :\n\n\n```\nsage:  words.FibonacciWord()\nword: 0100101001001010010100100101001001010010...\n```\n\n\nwhich is the default behavior anyway :\n\n```\nsage: Word(lambda n:n%10)\nword: 0123456789012345678901234567890123456789...\n```\n\n\n\n(2) The codomain of the product of `WordMorphism` is not correct :\n\n\n```\nsage: m = WordMorphism('0->a,1->b')\nsage: n = WordMorphism('a->c,b->e',codomain=Words('abcde'))\nsage: p = n * m\nsage: p.codomain()\nWords over Ordered Alphabet ['c', 'e']\n```\n\n\n(3) See the patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7405\n\n",
    "created_at": "2009-11-06T17:24:26Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Change the print of predefined words to the default behavior.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7405",
    "user": "slabbe"
}
```
Assignee: slabbe

CC:  saliola

Keywords: words

This ticket concern 3 relatively small things.

(1) Change the print of predefined words to the default behavior.

(2) Correct a bug of `__mul__` of `WordMorphism.`

(3) Adds the Fibonacci word defined from function.


See below for more explanations.

(1) The `rename` function is used a lot for predefined words :


```
sage: words.FibonacciWord()
Fibonacci word over Ordered Alphabet [0, 1], defined recursively
sage: words.FibonacciWord((0,1),'fixed point')
Fibonacci word over Ordered Alphabet [0, 1], defined as the fixed point of a morphism
sage: words.ThueMorseWord(alphabet = (3,4))
Thue-Morse word over Ordered Alphabet [3, 4]
sage: words.FixedPointOfMorphism('a->ab,b->ba','a')
Fixed point beginning with 'a' of the morphism WordMorphism: a->ab, b->ba
sage: words.ChristoffelWord(4,7)
Lower Christoffel word of slope 4/7 over Ordered Alphabet [0, 1]
```


But I more and more dislike this behavior made for the user since (1) it repeats the information already given by the user and (2) the first thing that the user do with the word is to look the prefix of the word (well, that's what I always do and that's what is done everywhere in the doctests).

To print a prefix, one needs to crete it (which is not always necessary for the user) :


```
sage: f = words.FibonacciWord()
sage: f
Fibonacci word over Ordered Alphabet [0, 1], defined recursively
sage: print f
Fibonacci word over Ordered Alphabet [0, 1], defined recursively
sage: f[:100]
word: 0100101001001010010100100101001001010010...
sage: print f[:100]
word: 0100101001001010010100100101001001010010100100101001010010010100100101001010010010100100101001010010
```


I would simply like the following to work :


```
sage:  words.FibonacciWord()
word: 0100101001001010010100100101001001010010...
```


which is the default behavior anyway :

```
sage: Word(lambda n:n%10)
word: 0123456789012345678901234567890123456789...
```



(2) The codomain of the product of `WordMorphism` is not correct :


```
sage: m = WordMorphism('0->a,1->b')
sage: n = WordMorphism('a->c,b->e',codomain=Words('abcde'))
sage: p = n * m
sage: p.codomain()
Words over Ordered Alphabet ['c', 'e']
```


(3) See the patch.

Issue created by migration from https://trac.sagemath.org/ticket/7405





---

archive/issue_comments_062311.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-06T17:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7405#issuecomment-62311",
    "user": "slabbe"
}
```

Attachment



---

archive/issue_comments_062312.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-06T17:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7405#issuecomment-62312",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062313.json:
```json
{
    "body": "The patch looks good and all tests pass. I'm ready to give a positive review.\n\nHowever I'm not a word expert so that I'd like someone who is to confirm that the change of printing is really the wanted behavior. Franco: once you agree with that please put a positive review on that patch. I will shorten a bit more the combinat queue... \n\nCheers,\n\nFlorent",
    "created_at": "2009-11-22T19:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7405#issuecomment-62313",
    "user": "hivert"
}
```

The patch looks good and all tests pass. I'm ready to give a positive review.

However I'm not a word expert so that I'd like someone who is to confirm that the change of printing is really the wanted behavior. Franco: once you agree with that please put a positive review on that patch. I will shorten a bit more the combinat queue... 

Cheers,

Florent



---

archive/issue_comments_062314.json:
```json
{
    "body": "Thanks Florent for the review.\n\nI also would like Franco to agree with the print changes before any inclusion in sage since he wrote some of those rename of objects.\n\nS\u00e9bastien",
    "created_at": "2009-11-23T13:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7405#issuecomment-62314",
    "user": "slabbe"
}
```

Thanks Florent for the review.

I also would like Franco to agree with the print changes before any inclusion in sage since he wrote some of those rename of objects.

Sébastien



---

archive/issue_comments_062315.json:
```json
{
    "body": "I strongly agree with the changes. I think this way is much better.",
    "created_at": "2009-11-23T14:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7405#issuecomment-62315",
    "user": "saliola"
}
```

I strongly agree with the changes. I think this way is much better.



---

archive/issue_comments_062316.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-23T14:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7405#issuecomment-62316",
    "user": "saliola"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062317.json:
```json
{
    "body": "Opps, I forgot to change the summary.",
    "created_at": "2009-11-23T14:47:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7405#issuecomment-62317",
    "user": "saliola"
}
```

Opps, I forgot to change the summary.



---

archive/issue_comments_062318.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7405#issuecomment-62318",
    "user": "mhansen"
}
```

Resolution: fixed
