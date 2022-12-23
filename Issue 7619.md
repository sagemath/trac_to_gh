# Issue 7619: Pickling support for finite word defined by callable and iterable

Issue created by migration from https://trac.sagemath.org/ticket/7619

Original creator: slabbe

Original creation time: 2009-12-08 12:45:18

Assignee: slabbe

CC:  saliola

Currently pickling doesn't work for finite word defined by iterator and callable :


```
sage: w = Word(iter('abcdefghijkl'))
sage: loads(dumps(w))
Traceback (most recent call last):
...
PicklingError: Can't pickle <type 'generator'>: attribute lookup __builtin__.generator failed
```


This is not too hard to support. One just have to expand the iterator to a list  (or a tuple?) and save the list instead:


```
sage: w = Word(iter('abcdefghijkl'))
sage: loads(dumps(w))
word: abcdefghijkl
sage: type(_)
<class 'sage.combinat.words.word.FiniteWord_list'>
```


This is more general solution to the problem solved in #7519.



---

Comment by slabbe created at 2009-12-08 12:52:09

Changing status from new to needs_review.


---

Comment by slabbe created at 2009-12-08 12:52:09

The patch save those finite words to list. I wonder if tuple is better or is the same?


---

Comment by slabbe created at 2010-01-14 18:14:28

I just uploaded the patch. Pickle is now supported for infinite word defined from a function :


```
sage: w = Word(lambda n:n)
sage: loads(dumps(w))
word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...
```


It uses the `pickle_function` and `unpickle_function` (which gives a new utility for `datatype` argument)


```
sage: lambda n:n
<function <lambda> at 0x887e764>
sage: pickle_function(_)
"csage.misc.fpickle\ncode_ctor\np1\n(I1\nI1\nI1\nI67\nS'|\\x00\\x00S'\np2\n(t(t(S'n'\ntp3\nS'<ipython console>'\np4\nS'<lambda>'\np5\nI1\nS''\ntRp6\n."
sage: Word(_, datatype='pickled_function')
word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...
```


Since `pickle_function` fails on `CallableFromListOfWords`, those finite words are expanded as a list in order to be saved:


```
sage: w = Word(range(5)) * Word('abcde')
sage: type(w)
<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>
sage: z = loads(dumps(w))
sage: z
word: 01234abcde
sage: type(z)
<class 'sage.combinat.words.word.FiniteWord_list'>
```


Needs review!!


---

Comment by slabbe created at 2010-02-16 22:33:24

Forget about this patch!


---

Attachment

Depends on #7520.


---

Comment by saliola created at 2010-03-02 02:20:23

Changing keywords from "" to "words".


---

Comment by saliola created at 2010-03-02 02:20:23

Hello Sebastien. I've taken a look at the patch. Great changes! We can now pickle objects that we could not have pickled before.

The patch applies cleanly to sage-4.3.3 and all tests passed for `make test`.


---

Comment by saliola created at 2010-03-02 02:20:23

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-03 14:01:40

Merged [trac_7619_pickle_for_FiniteWord_iter_callable-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7619/trac_7619_pickle_for_FiniteWord_iter_callable-sl.patch).


---

Comment by mvngu created at 2010-03-03 14:01:40

Resolution: fixed
