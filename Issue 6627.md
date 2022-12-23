# Issue 6627: lyndon and standard factorization of words is broken

Issue created by migration from https://trac.sagemath.org/ticket/6627

Original creator: saliola

Original creation time: 2009-07-26 09:54:18

Assignee: saliola

CC:  slabbe

The last 1 in the word disappeared:

```
sage: Word([1,2,1,3,1,2,1]).lyndon_factorization()
(1213.12)
```


Lyndon factorization of the empty word should work.

```
sage: Words('01')('').lyndon_factorization()
Traceback (most recent call last):
...
StopIteration
```


The standard factorization of 321 is 32.1.

```
sage: sage: Word([3,2,1]).standard_factorization()
(321.)
}}} 

The standard factorization of the empty word should return the empty word, and not two copies of the empty word. 
{{{
sage: Words('123')('').standard_factorization()
(.)
}}}


---

Attachment

based on sage-4.1.1.alpha0


---

Comment by saliola created at 2009-07-26 12:11:33

This new implementation is correct and also faster.

```
sage: sage: Word([1,2,1,3,1,2,1]).lyndon_factorization()
(1213, 12, 1)
sage: sage: Words('01')('').lyndon_factorization()
()
sage: sage: sage: Word([3,2,1]).standard_factorization()
(32, 1)
sage: sage: Words('123')('').standard_factorization()
()
```


I also changed the repr of the (word) Factorization class to use ',' instead of '.' because otherwise the period is confusing if you factor a long word:

```
sage: WordOptions(truncate_length=10)
sage: tm = words.ThueMorseWord()
sage: tm[:100].lyndon_factorization()
(011, 01, 0011, 00101101, 0010110011..., 0010110011..., 0010110011..., 0010110011, 0)
```



---

Comment by mvngu created at 2009-08-24 23:54:20

Resolution: fixed
