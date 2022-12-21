# Issue 8227: Improving iterated palindromic closure computation

Issue created by migration from Trac.

Original creator: abmasse

Original creation time: 2010-02-10 11:20:10

Assignee: AlexGhitza

CC:  slabbe

Keywords: iterated palindromic closure

There is a faster way to compute the iterated paindromic closure of a word than using the definition. The problem with the latter is that it needs to compute the longest f-palindromic suffix of the current word at each step, while it is possible to easily deduce this length only by looking at the directive word.


---

Comment by abmasse created at 2010-02-10 12:03:42

I had to implement two other functions: find() and rfind() that were only available for Word_str words. It is not the more efficient implementation yet, but that was not the goal of this ticket...


---

Comment by abmasse created at 2010-02-10 12:03:42

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-02-10 13:14:34

Changing assignee from AlexGhitza to abmasse.


---

Comment by abmasse created at 2010-02-10 13:16:50

Changing component from algebra to combinatorics.


---

Comment by slabbe created at 2010-02-11 00:13:59

1. I think the patch should follow the python behavior (i.e. return -1)


```
sage: '0123456789'.find('4566')
-1
sage: '0123456789'.rfind('4566')
-1
```


for those functions :


```
sage: Word(range(10)).rfind(Word([4,5,6,6]))
sage: Word(range(10)).find(Word([4,5,6,6]))
```


2. The following comment found in the doc of `find` and `rfind` 


```
This function is different for Word_str objects:
```


illustrates a problem : the behavior for `Word_str` should be the same (`Word_str` is wrong). Can you fix it? You may consult #8127 for an idea of how to handle it. Make sure to ask the parent using super if type of other is not an str or a `Word_str`.


3. An enumeration in the doc of the iterator function is broken as seen in the result of :


```
sage: w = Word(range(10))
sage: browse_sage_doc(w._iterated_right_palindromic_closure_recursive_iterator)
```


Adding a blank line before the itemize should repair the problem. I also suggest to put `WordMorphism`,  `'recursive'` and `_iterative_righ...iterator()` inside double backquotes (like input arguments).

4. Looking the function below but also how naive is the code of `find`, maybe the function `find` could use the function `first_pos_in` instead? This makes me realize that the function `first_pos_in` was probably a bad choice of name.... Using the new deprecation warning introduced recently by Florent Hivert this (name modif) can be done more easily now (but not in this ticket).


```
sage: %timeit Word([990,991,992,993]).first_pos_in(Word(range(1000)))
125 loops, best of 3: 1.65 ms per loop
sage: %timeit Word(range(1000)).find(Word([990,991,992,993]))
5 loops, best of 3: 48 ms per loop
```


5. Could `rfind` could be improved easily using `_pos_in` and other good suffix table already implemented? If so, it can be good to do it now. But if you don't care now, it is fine. The function could be improved later if it is valuable. Anyway, the next step for all those search stuff is to be cythoned...

That's all for my comments.


---

Comment by slabbe created at 2010-02-11 00:13:59

Changing status from needs_review to needs_work.


---

Comment by abmasse created at 2010-02-11 17:18:27

Thank you Sébastien for all those comments ! I agree with you on items 4 and 5, but I think these issues should be addressed in another ticket. I intend to do it in a close future, but this is in some way independent of the iterated palindromic closures functions. As for item 1, I agree with you as well, but I think it would be better if ``find()`` and ``rfind()`` functions could allow the user to choose between different string search algorithms (Boyer-Moore, KMP, etc.), so that it is maybe not necessary to make them look like the Python functions (what do you think?). If I understand you well in item 2, you would like me to change the ``find()`` and ``rfind()`` functions for Word_str objects or only to detect it in the algorithm computing the iterated palindromic closure? Finally, I will correct item 3 and the other problems as soon as you answer me.


---

Comment by slabbe created at 2010-02-14 18:35:34

Replying to [comment:5 abmasse]:
> Thank you Sébastien for all those comments ! I agree with you on items 4 and 5, but I think these issues should be addressed in another ticket. 

Well, ok for 5 : `rfind` could be improved later. But for 4, I would like your new find function to make use of `first_pos_in` since it is already there and is faster. If you want to keep your implementation there, I suggest you use a parameter `algorithm` that defaults to `suffix_table` or a similar word and that make use of `first_pos_in`.

> As for item 1, I agree with you as well, but I think it would be better if ``find()`` and ``rfind()`` functions could allow the user to choose between different string search algorithms (Boyer-Moore, KMP, etc.), so that it is maybe not necessary to make them look like the Python functions (what do you think?). 

I think both are possible (Je ne crois pas que l'un empêche l'autre) : one may selec the algorithm and the function can still behave like python. For example, 


```
sage: w = Word(range(10))
sage: u = Word(range(5, 8))
sage: w.find(u)
5
sage: w.find(u, algorithm='KMP')
5
sage: w.find(u*u)
-1
```


> If I understand you well in item 2, you would like me to change the ``find()`` and ``rfind()`` functions for Word_str objects or only to detect it in the algorithm computing the iterated palindromic closure? Finally, I will correct item 3 and the other problems as soon as you answer me.

Ok, so let's open a new ticket to clean up find and rfind.


---

Comment by abmasse created at 2010-02-21 01:53:30

I have corrected items 1 to 4.

As discussed, item 5 will be done in another ticket or directly in Cython.

I'll upload the new patch in a few minutes.


---

Attachment

Updated patch with corrections


---

Comment by abmasse created at 2010-02-21 01:57:32

Changing status from needs_work to needs_review.


---

Attachment

Applies over the precedent patch


---

Comment by slabbe created at 2010-02-23 02:47:27

I just tested the patch. All test passed in sage/combinat/words. The speed of the function is greatly improved. Doc builds fine. I am giving a positive review to this ticket.

Althought, I added a patch fixing some small sphinx editing and replace `l` for `L` because I was reading `1` at first glance. Alexandre, if you agree with my patch, I allow you to change the status of this ticket to positive review.


---

Comment by abmasse created at 2010-02-23 08:45:59

Changing status from needs_review to positive_review.


---

Comment by abmasse created at 2010-02-23 08:45:59

I agree with the changes. I tested the two patches and everything seems alright. All tests passed, no problem in the documentation. Positive review to Sébastien's changes.


---

Comment by mvngu created at 2010-03-02 21:22:52

Merged in this order:

 1. [trac_8227_iterated_palindromic_closure_improvement-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8227/trac_8227_iterated_palindromic_closure_improvement-abm.patch)
 1. [trac_8227_review-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8227/trac_8227_review-sl.patch)


---

Comment by mvngu created at 2010-03-02 21:22:52

Resolution: fixed
