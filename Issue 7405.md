# Issue 7405: Change the print of predefined words to the default behavior.

Issue created by migration from https://trac.sagemath.org/ticket/7405

Original creator: slabbe

Original creation time: 2009-11-06 17:24:26

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


---

Attachment


---

Comment by slabbe created at 2009-11-06 17:55:10

Changing status from new to needs_review.


---

Comment by hivert created at 2009-11-22 19:00:16

The patch looks good and all tests pass. I'm ready to give a positive review.

However I'm not a word expert so that I'd like someone who is to confirm that the change of printing is really the wanted behavior. Franco: once you agree with that please put a positive review on that patch. I will shorten a bit more the combinat queue... 

Cheers,

Florent


---

Comment by slabbe created at 2009-11-23 13:05:34

Thanks Florent for the review.

I also would like Franco to agree with the print changes before any inclusion in sage since he wrote some of those rename of objects.

Sébastien


---

Comment by saliola created at 2009-11-23 14:46:01

I strongly agree with the changes. I think this way is much better.


---

Comment by saliola created at 2009-11-23 14:46:01

Changing status from needs_review to positive_review.


---

Comment by saliola created at 2009-11-23 14:47:02

Opps, I forgot to change the summary.


---

Comment by mhansen created at 2009-11-29 05:29:35

Resolution: fixed
