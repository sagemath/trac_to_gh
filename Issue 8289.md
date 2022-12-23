# Issue 8289: Clean up WordMorphism.__call__

Issue created by migration from https://trac.sagemath.org/ticket/8289

Original creator: slabbe

Original creation time: 2010-02-16 22:17:45

Assignee: slabbe

CC:  abmasse

`WordMorphism.__call__` is doing a conversion of the input into the domain which is not necessary. Basicly, all what is needed is that the input be iterable. Here are some timing improvements :

BEFORE:


```
sage: m = WordMorphism('a->aab,b->ba')
sage: %timeit w = m('a'*100)
1000 loops, best of 3: 343 µs per loop
```


AFTER:


```
sage: m = WordMorphism('a->aab,b->ba')
sage: %timeit w = m('a'*100)
1000 loops, best of 3: 242 µs per loop
```



---

Comment by slabbe created at 2010-02-17 00:08:00

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-02-26 10:43:46

Hello Sébastien !

I started reviewing your patch with the sage-combinat mercurial queue and I noticed that some tests didn't pass. This is probably due to the patch where you remove the `check` function that verifies the 40 first letters, but for sake of sureness, could you move your patch up in the series file ?

Short of that, I don't think it will be too hard to review.


---

Comment by abmasse created at 2010-02-26 13:38:48

Here are more details.


```
[~/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words]$ sage -t *
sage -t  "devel/sage-combinat/sage/combinat/words/__init__.py"
	 [0.1 s]
sage -t  "devel/sage-combinat/sage/combinat/words/all.py"   
	 [0.1 s]
sage -t  "devel/sage-combinat/sage/combinat/words/alphabet.py"
	 [2.4 s]
sage -t  "devel/sage-combinat/sage/combinat/words/morphism.py"
	 [2.5 s]
sage -t  "devel/sage-combinat/sage/combinat/words/paths.py" 
	 [8.0 s]
sage -t  "devel/sage-combinat/sage/combinat/words/shuffle_product.py"
	 [2.1 s]
sage -t  "devel/sage-combinat/sage/combinat/words/suffix_trees.py"
	 [4.9 s]
sage -t  "devel/sage-combinat/sage/combinat/words/utils.py" 
	 [2.1 s]
sage -t  "devel/sage-combinat/sage/combinat/words/word.py"  
**********************************************************************
File "/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word.py", line 1894:
    sage: z + y
Expected:
    Traceback (most recent call last):
    ...
    ValueError: 5 not in alphabet!
Got:
    word: 1222353587
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_38
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_word.py
	 [11.6 s]
sage -t  "devel/sage-combinat/sage/combinat/words/word_content.py"
	 [2.2 s]
sage -t  "devel/sage-combinat/sage/combinat/words/word_datatypes.pyx"
	 [2.1 s]
sage -t  "devel/sage-combinat/sage/combinat/words/word_generators.py"
**********************************************************************
File "/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_generators.py", line 354:
    sage: words.ThueMorseWord(alphabet='ab', base=1)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: base (=1) and len(alphabet) (=2) must be at least 2
Got:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[9]>", line 1, in <module>
        words.ThueMorseWord(alphabet='ab', base=Integer(1))###line 354:
    sage: words.ThueMorseWord(alphabet='ab', base=1)
      File "/Users/alexandre/Applications/sage-4.3.3/local/lib/python/site-packages/sage/combinat/words/word_generators.py", line 376, in ThueMorseWord
        raise ValueError, "base (=%s) and size of alphabet (=%s) must be at least 2"%(base, m)
    ValueError: base (=1) and size of alphabet (=2) must be at least 2
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_9
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_word_generators.py
	 [8.4 s]
sage -t  "devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py"
**********************************************************************
File "/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py", line 499:
    sage: w._letter_cache
Expected:
    {0: 0, 1: 1, 2: 1, 3: 0, 4: 1, 5: 0, 6: 0, 7: 1, 8: 1, 9: 0, 10: 0, 11: 1, 12: 0, 13: 1, 14: 1, 15: 0, 16: 1, 17: 0, 18: 0, 19: 1, 20: 0, 21: 1, 22: 1, 23: 0, 24: 0, 25: 1, 26: 1, 27: 0, 28: 1, 29: 0, 30: 0, 31: 1, 32: 1, 33: 0, 34: 0, 35: 1, 36: 0, 37: 1, 38: 1, 39: 0}
Got:
    {}
**********************************************************************
File "/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py", line 503:
    sage: w._letter_cache
Expected:
    {0: 0, 1: 1, 2: 1, 3: 0, 4: 1, 5: 0, 6: 0, 7: 1, 8: 1, 9: 0, 10: 0, 11: 1, 12: 0, 13: 1, 14: 1, 15: 0, 16: 1, 17: 0, 18: 0, 19: 1, 20: 0, 21: 1, 22: 1, 23: 0, 24: 0, 25: 1, 26: 1, 27: 0, 28: 1, 29: 0, 30: 0, 31: 1, 32: 1, 33: 0, 34: 0, 35: 1, 36: 0, 37: 1, 38: 1, 39: 0, 100: 1}
Got:
    {100: 1}
**********************************************************************
File "/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py", line 820:
    sage: w.__reduce__()
Expected:
    (<function Word at ...>, (<generator object __iter__ at ...>, Words, 2, 'iter', False))
Got:
    (<function Word at 0x10b933b18>, (<generator object __iter__ at 0x10c4a00a0>, Words, None, 'iter', False))
**********************************************************************
File "/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py", line 1087:
    sage: w.__reduce__()
Expected:
    (<function Word at ...>, (<generator object __iter__ at ...>, Words, 2, 'iter', True))
Got:
    (<function Word at 0x10b933b18>, (<generator object __iter__ at 0x100468190>, Words, None, 'iter', True))
**********************************************************************
File "/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py", line 1104:
    sage: w._last_index, len(w._list)
Expected:
    (39, 40)
Got:
    (-1, 0)
**********************************************************************
4 items had failures:
   2 of   8 in __main__.example_11
   1 of   6 in __main__.example_15
   1 of   6 in __main__.example_19
   1 of   9 in __main__.example_20
***Test Failed*** 5 failures.
For whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_word_infinite_datatypes.py
	 [2.2 s]
sage -t  "devel/sage-combinat/sage/combinat/words/word_options.py"
	 [2.1 s]
sage -t  "devel/sage-combinat/sage/combinat/words/words.py" 
**********************************************************************
File "/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/words.py", line 207:
    sage: Words(range(10))(count())
Expected:
    Traceback (most recent call last):
    ...
    ValueError: 10 not in alphabet!
Got:
    word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...
**********************************************************************
File "/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/words.py", line 215:
    sage: Words("ab")("abca")
Expected:
    Traceback (most recent call last):
    ...
    ValueError: c not in alphabet!
Got:
    word: abca
**********************************************************************
1 items had failures:
   2 of   8 in __main__.example_4
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_words.py
	 [2.2 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-combinat/sage/combinat/words/word.py"
	sage -t  "devel/sage-combinat/sage/combinat/words/word_generators.py"
	sage -t  "devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py"
	sage -t  "devel/sage-combinat/sage/combinat/words/words.py"
Total time for all tests: 53.1 seconds
```



---

Attachment


---

Comment by slabbe created at 2010-02-27 01:27:08

> I started reviewing your patch with the sage-combinat mercurial queue and I noticed that some tests didn't pass. This is probably due to the patch where you remove the `check` function that verifies the 40 first letters, but for sake of sureness, could you move your patch up in the series file ?

Done. I removed the check patch since I found a better solution for it. The patch 8289 should now be fine in the sage-combinat tree.


---

Comment by abmasse created at 2010-02-28 11:42:59

Hello, Sébastien !

Just one question. I get the following:


```
sage: m = WordMorphism('a->b,b->a')
sage: m(Word())
word: 
sage: m(Word(), oo)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/Users/alexandre/<ipython console> in <module>()

/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/words/morphism.pyc in __call__(self, w, order, datatype)
    561         if order is Infinity:
    562             if isinstance(w, (tuple,str,list,FiniteWord_class)):
--> 563                 letter = w[0]
    564             elif hasattr(w, '__iter__'):
    565                 letter = w.next()

/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/words/word_datatypes.so in sage.combinat.words.word_datatypes.WordDatatype_list.__getitem__ (sage/combinat/words/word_datatypes.cpp:1407)()

IndexError: list index out of range
```


Don't you think we should get the empty word in that case ? This seems to be well-defined.


---

Comment by abmasse created at 2010-02-28 11:43:57

By the way, you don't need to modify your patch accordingly if you agree, I've already started one for the review, so I can add it easily.


---

Comment by slabbe created at 2010-02-28 14:13:03

Replying to [comment:6 abmasse]:
> By the way, you don't need to modify your patch accordingly if you agree, I've already started one for the review, so I can add it easily.

Of course I agree. We should return the empty word in this case...


---

Comment by abmasse created at 2010-02-28 23:39:40

I'm finished with the review! The changes brought by this patch appears reasonable and do indeed speed up some treatments without slowing down other ones.

I modified some formatting in the documentation, and I treated the case where the morphism is applied on the empty word with infinite order.  Everything seems fine to me. I wait until you check my change to set this patch to positive review.

Uploading the review patch in a few seconds.


---

Attachment

Review - doc changes and empty word case -- apply on top of the first patch


---

Comment by slabbe created at 2010-03-01 00:37:04

Changing status from needs_review to positive_review.


---

Comment by slabbe created at 2010-03-01 00:37:04

Thanks for your review. I like your changes. I tested them: all tests passed. Doc builds fine. Empty word problem fixed.

Positive review.


---

Comment by mvngu created at 2010-03-02 21:32:23

Merged in this order:

 1. [trac_8289_wordmorphism_call-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8289/trac_8289_wordmorphism_call-sl.patch)
 1. [trac_8289_review-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8289/trac_8289_review-abm.patch)


---

Comment by mvngu created at 2010-03-02 21:32:23

Resolution: fixed
