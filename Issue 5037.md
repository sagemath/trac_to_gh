# Issue 5037: Bug fixes and new functionalities for Words library

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2009-01-20 19:27:34

Assignee: slabbe

CC:  sage-combinat

Add to Word Morphism the following functions :
 * `__add__()` that merges two Word Morphisms on disjoint domain.
 * `restriction(self, alphabet)` that returns a new Word Morphism constructed from self by restricting the domain to Words over the given alphabet.
 * `disjoint_alphabet(self)`, for involutions only, that returns a partition A,B,C of the alphabet s.t. self(A) = B, self(B)=A and self(C) = C.

*Note : I am still not convince of those three names.*

Fix in Word Morphism the following function :
 * `is_involution(self)` : should first check that self is an endomorphism

Fix in word.py the following functions :
 * `colored_vector` : Fails on empty word.

Add in word.py the following possibilities:
 * `colored_vector` : Put a label on the graphical word displayed.
 


---

Comment by slabbe created at 2009-07-22 21:33:12

This is the example of a bad ticket having many feature to fix/add. Fortunately, all of those were solved by #6519 merged in sage recently.

In fact, you can now glue word morphism together using the function `extend_by` :


```
sage: n = WordMorphism({0:1,1:0,'a':5})
sage: m = WordMorphism('a->ab,b->ba')
sage: print n.extend_by(m)
WordMorphism: 0->1, 1->0, a->5, b->ba
sage: 
sage: print m.extend_by(n)
WordMorphism: 0->1, 1->0, a->ab, b->ba
```


You can now restrict the domain of a morphism by using `restrict_domain` :

```
sage: print n.restrict_domain([0,'a'])
WordMorphism: 0->1, a->5
```


You can now get the partition of the domain alphabet defined (not uniquely) by a involution :


```
sage: inv = WordMorphism({0:1,1:0,2:2,3:3,4:5,5:4})
sage: inv.is_involution()
True
sage: inv.partition_of_domain_alphabet()
({0, 4}, {1, 5}, {2, 3})
```



The code of `is_involution` first check that self is an endomorphism before comptuting the square of self, which gives a better error message :


```
sage: print n
WordMorphism: 0->1, 1->0, a->5
sage: n.is_involution()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/slabbe/.sage/temp/slabbe_laptop/8706/_home_slabbe__sage_init_sage_0.py in <module>()

/home/slabbe/sage-4.1/local/lib/python2.6/site-packages/sage/combinat/words/morphism.pyc in is_involution(self)
    973         """
    974         if not self.is_endomorphism():
--> 975             raise TypeError, "self (=%s) is not a endomorphism"%self
    976 
    977         return (self*self).is_identity()

TypeError: self (=WordMorphism: 0->1, 1->0, a->5) is not a endomorphism
```


The colored vector is not broken anymore on the empty word :


```
sage: empty = Word(); empty
word: 
sage: empty.colored_vector()

```


A label can now be added to the colored vector of a word (a graphic object useful to study equations on words) :


```
sage: w = Word([0..10]+[10,9..0])
sage: w.colored_vector(label='a palindrome rainbow')

```


Hence, I recommand that this ticket be closed.


---

Comment by mvngu created at 2009-07-22 21:44:52

Closing this as a duplicate of #6519.


---

Comment by mvngu created at 2009-07-22 21:44:52

Resolution: duplicate
