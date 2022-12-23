# Issue 5038: Add word path support

Issue created by migration from https://trac.sagemath.org/ticket/5038

Original creator: slabbe

Original creation time: 2009-01-20 19:56:41

Assignee: slabbe

CC:  sage-combinat saliola abmasse

This module implements word paths which belongs to Discrete Geometry seen from Combinatorics on Words point of view. A word path is the representation of a word
as a discrete path in a two (or more) dimensions space using a one-to-one
correspondence between the alphabet and a set of vectors called steps. Using combinatorics on words, many problems on discrete polygons on 2d lattice grid may be solved in linear time in length of the perimeter (self-intersecting, area, inertia moment, etc.). For now, the goal is to create all the classes hierarchy. Cool algorithms will come into an other ticket.

Here are some examples taken from the documentation of the current state of paths.py available in the sage-combinat tree.

The combinatorial class of all paths defined over three given steps:

```
sage: P = WordPaths('abc', steps=[(1,2), (-3,4), (0,-3)]); P
Finite Word Paths over 3 steps
```


Creation of a path from the combinatorial class P:

```
sage: p = P('abaccba'); p
Path: abaccba
sage: list(p.points())
[(0, 0), (1, 2), (-2, 6), (-1, 8), (-1, 5), (-1, 2), (-4, 6), (-3, 8)]
sage: p.is_closed()
False
sage: p.plot() 
```


Since p is a finite word, many functions from the word library are available:

```
sage: p.crochemore_factorization()
(a.b.a.c.c.ba)
sage: p.is_palindrome()
False
sage: p[:3]
Path: aba
sage: len(p)
7 
```


Some built-in combinatorial classes of paths:

```
sage: P = WordPaths('abAB', steps='square_grid'); P
Finite Word Paths on the square grid
```


```
sage: D = WordPaths('()', steps='dyck'); D
Finite Dyck paths
sage: d = D('()()()(())'); d
Path: ()()()(())
sage: d.plot()
```


```
sage: P = WordPaths('abcdef', steps='triangle_grid')
sage: p = P('babaddefadabcadefaadfafabacdefa')
sage: p.plot() 
```



---

Comment by slabbe created at 2009-01-20 19:58:48

Changing type from defect to enhancement.


---

Comment by slabbe created at 2009-09-07 23:02:01

I just uploaded a patch, but I forgot to do some stuff. Will upload another patch soon.


---

Comment by slabbe created at 2009-09-13 14:43:57

Changing status from new to assigned.


---

Comment by slabbe created at 2009-09-13 14:43:57

I refreshed the patch. Needs review !!

...Should I do something somewhere so that `sage/combinat/words/paths.py` get added to the documentation?


---

Comment by slabbe created at 2009-09-17 18:09:46

I updated the patch after #6903 reviews.


---

Comment by slabbe created at 2009-09-18 14:33:27

I just realized that the doctest coverage is not perfect right now. Will post a new patch soon.


---

Comment by slabbe created at 2009-09-18 21:29:33

Depends on #6903.


---

Attachment

New patch uploaded. Doctest coverage of paths.py : 100%. Added paths.py to the documentation.


---

Comment by slabbe created at 2009-09-18 21:38:51

Needs review!


---

Comment by mhansen created at 2009-09-26 03:33:14

Looks good to me.  I attached a patch to remove the import of GridLines since it isn't used.


---

Attachment


---

Comment by mvngu created at 2009-09-26 06:19:46

I got the following doctest failure:

```
sage -t -long devel/sage/sage/structure/sage_object.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/structure/sage_object.pyx", line 931:
    sage: sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Successfully unpickled 572 objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    ** failed:  _class__sage_combinat_words_utils_Factorization__.sobj
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Failed:
    _class__sage_combinat_words_utils_Factorization__.sobj
    Successfully unpickled 571 objects.
    Failed to unpickle 1 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_21
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_sage_object.py
	 [6.3 s]
```



---

Comment by slabbe created at 2009-09-29 12:21:00

Applies over the precedent 2 patches.


---

Attachment

The above failure is now fixed by the patch I just uploaded. Needs review.


---

Comment by slabbe created at 2009-10-13 10:06:41

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2009-10-13 10:06:41

I am reviewing my own patch... There is something I dislike in the patch that I would like to discuss before including it into Sage. There are pros and cons for having a word path being a word. One thing I dislike right now is the pollution on the tab completion :


```
sage: P = WordPaths('abcd')
sage: p = P('aaaaa')
sage: p.
Display all 146 possibilities? (y or n)
```


whereas it could be something like below if a word path wouldn't inherit from `FiniteWord` (but still from `WordDatatype` :


```
sage: P = WordPaths('abcd')
sage: p = P('abbbbccd')
sage: p.
p.animate           p.find              p.points
p.area              p.has_prefix        p.rename
p.category          p.has_suffix        p.reset_name
p.count             p.is_closed         p.rfind
p.db                p.is_prefix         p.save
p.directive_vector  p.is_simple         p.start_point
p.dump              p.is_suffix         p.tikz_trajectory
p.dumps             p.length            p.version
p.end_point         p.plot          
```


But since I still want to know if a wordpath is a palindrome and other questions already implemented for words, something like below could exist :


```
sage: P = WordPaths('abcd')
sage: p = P('abbbbccd')
sage: p.to_word()
sage: p.
Display all 146 possibilities? (y or n)
sage: p.is_palindrome()
False
```


Of course I would want the `to_word` to be constant time (no copy) : I am thinking of simply adding the `FiniteWord` class to the base classes of `p`.


Franco, Mike Hansen : Do you have any comments ? I am sure you have useful ideas I could use!

Thank you,

Sébastien


---

Comment by saliola created at 2009-10-15 15:21:10

Replying to [comment:12 slabbe]:

> But since I still want to know if a wordpath is a palindrome and other questions already implemented for words, something like below could exist :

You need to decide whether or not a "wordpath" is a word. If it is, then it
should inherit all the methods. A user will be totally confused if it is
supposed to be a word but doesn't behave like one.

If it is not a word, then having a `to_word` method is fine, but it
needs to return a word. In your suggestion, it returns `None` but this
is unusual since most `to_*` methods in Sage (at least in combinatorics
code) do not modify the original object but return a new object. 

Perhaps you want to work with paths instead of word paths?


> Of course I would want the `to_word` to be constant time (no copy) : I am thinking of simply adding the `FiniteWord` class to the base classes of `p`.

The creation of u in the following is constant time:

```
sage: w = Word([0,1,1,0,1,0,0,1])
sage: u = Word(w._data)
```


Hope this helps.


---

Attachment


---

Comment by slabbe created at 2009-10-20 11:28:33

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2009-10-20 11:28:33

> You need to decide whether or not a "wordpath" is a word. If it is, then it
> should inherit all the methods. A user will be totally confused if it is
> supposed to be a word but doesn't behave like one.

I want a word path to be a word. So, I will keep it as it is.

> Hope this helps.

Yes, thank you!

I added a patch that improves the documentation and that suggests to use `help(p)` to get the specific word paths functions.

Needs review!


---

Attachment

apply on top of the others


---

Comment by saliola created at 2009-10-20 16:55:24

I posted a small patch to address some errors in the documentation introduced in the last patch. Otherwise, positive review. Sébastien, take a look at my patch, and if it is okay, then change the summary to positive review.


---

Comment by slabbe created at 2009-10-21 08:53:00

Great. Thanks for the grammatical corrections and for the '-' as well. I am giving positive review to your changes, so that I change the status of the ticket for positive review.


---

Comment by slabbe created at 2009-10-21 08:53:00

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-21 11:39:23

Resolution: fixed
