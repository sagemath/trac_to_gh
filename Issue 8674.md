# Issue 8674: Comparison of combinatorial class of words with word paths is broken

Issue created by migration from https://trac.sagemath.org/ticket/8674

Original creator: slabbe

Original creation time: 2010-04-11 14:17:52

Assignee: slabbe

CC:  abmasse

This is fine :


```
sage: m = WordMorphism('a->adab,b->ab,c->cbcd,d->cd')
sage: m.is_endomorphism()
True
```


But we would like the following to be an endomorphism as well:


```
sage: P = WordPaths('abcd')
sage: m = WordMorphism('a->adab,b->ab,c->cbcd,d->cd', codomain=P)
sage: m.is_endomorphism()
False
```



---

Comment by slabbe created at 2010-04-11 14:41:09

Does not depend on any known patch. Applies on 4.3.4.


---

Comment by slabbe created at 2010-04-11 14:41:40

Changing status from new to needs_review.


---

Attachment


---

Comment by abmasse created at 2010-04-17 16:03:54

Changing status from needs_review to needs_info.


---

Comment by abmasse created at 2010-04-17 16:03:54

I understand that you want to correct the function `is_endormorphism`, but there is something strange about combinatorial class comparison.

For instance, I get the following:


```
sage: Words('ab') == WordPaths('ab')
False
sage: Words('ab') <= WordPaths('ab')
True
sage: Words('ab') >= WordPaths('ab')
False
```


Wouldn't we want


```
sage: Words('ab') == WordPaths('ab')
True
```


or is there something I miss ?

If it is a problem, maybe it's not necessary to fix the `__eq__` operator now but do it in another ticket, but since you're at it...


---

Attachment

Applies over the precedent patch


---

Comment by slabbe created at 2010-04-19 10:30:43

The second patch attached answers Alexandre's comments. The equality test is now 

* large for Words paths


* considers the ordering of the alphabet

which can be both discussed. But I think that what is proposed is an extension of what exist. If we want to change the behavior, it could be done in another ticket.

Needs review again.


---

Comment by slabbe created at 2010-04-19 10:30:43

Changing status from needs_info to needs_review.


---

Comment by abmasse created at 2010-11-14 01:35:31

Changing status from needs_review to needs_work.


---

Comment by abmasse created at 2010-11-14 01:35:31

Already 7 months !!!! Sorry again for the delay...

I retested on sage-4.6 the two patches but I get a bunch of doctest failures. Were they already there or do they come from the fact that the patches were submitted seven months ago?


```
labo [~/Applications/sage/devel/sage-t8674/sage/combinat/words]
 $ sage -t *
sage -t  "devel/sage-t8674/sage/combinat/words/__init__.py" 
	 [0.1 s]
sage -t  "devel/sage-t8674/sage/combinat/words/abstract_word.py"
	 [2.6 s]
sage -t  "devel/sage-t8674/sage/combinat/words/all.py"      
	 [0.1 s]
sage -t  "devel/sage-t8674/sage/combinat/words/alphabet.py" 
	 [2.4 s]
sage -t  "devel/sage-t8674/sage/combinat/words/finite_word.py"
	 [13.2 s]
sage -t  "devel/sage-t8674/sage/combinat/words/infinite_word.py"
	 [2.4 s]
sage -t  "devel/sage-t8674/sage/combinat/words/morphism.py" 
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t8674/sage/combinat/words/morphism.py", line 907:
    sage: m.is_endomorphism()
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_17
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_morphism.py
	 [2.9 s]
sage -t  "devel/sage-t8674/sage/combinat/words/nfactor_enumerable_word.py"
	 [5.5 s]
sage -t  "devel/sage-t8674/sage/combinat/words/paths.py"    
	 [7.5 s]
sage -t  "devel/sage-t8674/sage/combinat/words/shuffle_product.py"
	 [2.5 s]
sage -t  "devel/sage-t8674/sage/combinat/words/suffix_trees.py"
	 [5.2 s]
sage -t  "devel/sage-t8674/sage/combinat/words/utils.py"    
	 [2.4 s]
sage -t  "devel/sage-t8674/sage/combinat/words/word.py"     
	 [2.5 s]
sage -t  "devel/sage-t8674/sage/combinat/words/word_content.py"
	 [2.5 s]
sage -t  "devel/sage-t8674/sage/combinat/words/word_datatypes.pyx"
	 [2.5 s]
sage -t  "devel/sage-t8674/sage/combinat/words/word_generators.py"
	 [7.9 s]
sage -t  "devel/sage-t8674/sage/combinat/words/word_infinite_datatypes.py"
	 [2.5 s]
sage -t  "devel/sage-t8674/sage/combinat/words/word_options.py"
	 [2.6 s]
sage -t  "devel/sage-t8674/sage/combinat/words/words.py"    
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t8674/sage/combinat/words/words.py", line 690:
    sage: WordPaths('abcd') != Words('abcd')
Expected:
    False
Got:
    True
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t8674/sage/combinat/words/words.py", line 692:
    sage: Words('abcd') != WordPaths('abcd')
Expected:
    False
Got:
    True
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t8674/sage/combinat/words/words.py", line 925:
    sage: WordPaths('abcd') <= Words('abcd')
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t8674/sage/combinat/words/words.py", line 952:
    sage: Words('abcd') >= WordPaths('abcd')
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t8674/sage/combinat/words/words.py", line 437:
    sage: type(z)
Expected:
    <class 'sage.combinat.words.word.FiniteWord_list'>
Got:
    <class 'sage.combinat.words.word.FiniteWord_str'>
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t8674/sage/combinat/words/words.py", line 661:
    sage: WordPaths('abcd') == Words('abcd')
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t8674/sage/combinat/words/words.py", line 663:
    sage: Words('abcd') == WordPaths('abcd')
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t8674/sage/combinat/words/words.py", line 667:
    sage: WordPaths('bacd') == WordPaths('abcd')
Expected:
    False
Got:
    True
**********************************************************************
5 items had failures:
   2 of   7 in __main__.example_10
   1 of   7 in __main__.example_22
   1 of   7 in __main__.example_23
   1 of  63 in __main__.example_5
   3 of  12 in __main__.example_9
***Test Failed*** 8 failures.
For whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_words.py
	 [2.9 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-t8674/sage/combinat/words/morphism.py"
	sage -t  "devel/sage-t8674/sage/combinat/words/words.py"
Total time for all tests: 70.4 seconds
```



---

Comment by slabbe created at 2010-11-14 06:20:41

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2010-11-14 06:20:41

> I retested on sage-4.6 the two patches but I get a bunch of doctest failures.

On sage-4.6, I get All tests passed. Did you sage -b ?


---

Comment by abmasse created at 2010-11-14 16:51:52

Changing status from needs_review to positive_review.


---

Comment by abmasse created at 2010-11-14 16:51:52

Hi!

Sorry, I must have forgotten to do it... I'm a bit rusty with all the steps of reviewing a patch. Indeed all tests pass, and the modified functions appear well in the documentation generated by Sphinx. I verified by hand that it solves the defect raised in the subject of this ticket.

Positive review.


---

Comment by jdemeyer created at 2010-11-18 22:25:58

Resolution: fixed
