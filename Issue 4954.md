# Issue 4954: Words_over_Alphabet should check the type of input alphabet

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2009-01-07 21:07:20

Assignee: mhansen

CC:  sage-combinat

Keywords: words alphabet

Do


```
sage: W=Words('ab')
sage: W.alphabet?
```


and you get the following help example :


```
sage: from sage.combinat.words.words import Words_over_Alphabet
sage: W = Words_over_Alphabet([1,2,3])
sage: W.alphabet()
[1, 2, 3]
sage: from sage.combinat.words.words import OrderedAlphabet
sage: W = Words_over_Alphabet(OrderedAlphabet('ab'))
sage: W.alphabet()
Ordered Alphabet ['a', 'b']
```


The first of the above example is misleading. In fact, it is not usable :


```
sage: from sage.combinat.words.words import Words_over_Alphabet
sage: W = Words_over_Alphabet([1,2,3])
sage: W.alphabet()
[1, 2, 3]
sage: W([1,1,1,2,1,3])
Traceback (most recent call last):
...
AttributeError: 'list' object has no attribute 'rank'
```


The problem comes from the fact that Words_over_Alphabet doesn't check the input alphabet before asigning it to self._alphabet(). It should either do `alphabet=OrderedAlphabet(alphabet)` before or check the type of the input alphabet with a isinstance.


---

Comment by slabbe created at 2009-01-07 21:08:01

Changing assignee from mhansen to slabbe.


---

Comment by slabbe created at 2009-07-22 20:39:25

This problem was solved by #6519 :


```
sage: from sage.combinat.words.words import Words_over_Alphabet
sage: W = Words_over_Alphabet([1,2,3])
sage: W.alphabet()
[1, 2, 3]
sage: W([1,1,1,2,1,3])
word: 111213
```



```
sage: Y = Words_over_Alphabet('abcde')
sage: Y.alphabet()
'abcde'
sage: Y('abababacde')
word: abababacde
```


So, I propose that this ticket be closed.


---

Comment by mvngu created at 2009-07-22 20:53:27

Closing this as a duplicate of #6519.


---

Comment by mvngu created at 2009-07-22 20:53:27

Resolution: duplicate
