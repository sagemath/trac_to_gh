# Issue 8127: Wraps string features into WordDatatypes

Issue created by migration from https://trac.sagemath.org/ticket/8127

Original creator: vdelecroix

Original creation time: 2010-01-29 23:05:14

Assignee: vdelecroix

CC:  slabbe sage-combinat

Keywords: string, word

Python has low-level operations for strings and we should allow them for words. For example

```
sage: sage: s = "ma maman est magique"
sage: s.split(' ')
['ma', 'maman', 'est', 'magique']
sage: s.split('ma')
['', ' ', '', 'n est ', 'gique']
```


The patch implements split and partition for words

```
sage: w = Word("ma maman est magique")
sage: w.split(' ')
[word: ma, word: maman, word: est, word: magique]
sage: w.split('ma')
[word: , word:  , word: , word: n est , word: gique]
```




---

Comment by slabbe created at 2010-01-31 22:38:46

With the patch applied, I obtain some doctest failures :



```
sage -t  "devel/sage-combinat/sage/combinat/words/morphism.py"
**********************************************************************
File "/Users/slabbe/Applications/sage-4.3.1/devel/sage-combinat/sage/combinat/words/morphism.py", line 485:
    sage: w = m('aaab',datatype='str')
Exception raised:
    Traceback (most recent call last):
      File "/Users/slabbe/Applications/sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/slabbe/Applications/sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/slabbe/Applications/sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[28]>", line 1, in <module>
        w = m('aaab',datatype='str')###line 485:
    sage: w = m('aaab',datatype='str')
      File "/Users/slabbe/Applications/sage-4.3.1/local/lib/python/site-packages/sage/combinat/words/morphism.py", line 582, in __call__
        return self.codomain()((x for y in w for x in self._morph[y]), length=length, datatype=datatype)
      File "/Users/slabbe/Applications/sage-4.3.1/local/lib/python/site-packages/sage/combinat/words/words.py", line 272, in __call__
        self._check(w)
      File "/Users/slabbe/Applications/sage-4.3.1/local/lib/python/site-packages/sage/combinat/words/words.py", line 501, in _check
        for a in itertools.islice(w, length):
      File "word_datatypes.pyx", line 244, in sage.combinat.words.word_datatypes.WordDatatype_str.__iter__ (sage/combinat/words/word_datatypes.cpp:1480)
        return iter(self._data)
    TypeError: 'NoneType' object is not iterable
**********************************************************************
File "/Users/slabbe/Applications/sage-4.3.1/devel/sage-combinat/sage/combinat/words/morphism.py", line 486:
    sage: type(w)
Expected:
    <class 'sage.combinat.words.word.FiniteWord_str'>
Got:
    <class 'sage.combinat.words.word.FiniteWord_list'>
**********************************************************************
File "/Users/slabbe/Applications/sage-4.3.1/devel/sage-combinat/sage/combinat/words/morphism.py", line 507:
    sage: w = m([0],4,datatype='str')
Expected:
    Traceback (most recent call last):
    ...
    ValueError: 0 not in alphabet!
Got:
    Traceback (most recent call last):
      File "/Users/slabbe/Applications/sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/slabbe/Applications/sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/slabbe/Applications/sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[37]>", line 1, in <module>
        w = m([Integer(0)],Integer(4),datatype='str')###line 507:
    sage: w = m([0],4,datatype='str')
      File "/Users/slabbe/Applications/sage-4.3.1/local/lib/python/site-packages/sage/combinat/words/morphism.py", line 586, in __call__
        return self(self(w, order-1),datatype=datatype)
      File "/Users/slabbe/Applications/sage-4.3.1/local/lib/python/site-packages/sage/combinat/words/morphism.py", line 582, in __call__
        return self.codomain()((x for y in w for x in self._morph[y]), length=length, datatype=datatype)
      File "/Users/slabbe/Applications/sage-4.3.1/local/lib/python/site-packages/sage/combinat/words/words.py", line 272, in __call__
        self._check(w)
      File "/Users/slabbe/Applications/sage-4.3.1/local/lib/python/site-packages/sage/combinat/words/words.py", line 501, in _check
        for a in itertools.islice(w, length):
      File "word_datatypes.pyx", line 244, in sage.combinat.words.word_datatypes.WordDatatype_str.__iter__ (sage/combinat/words/word_datatypes.cpp:1480)
        return iter(self._data)
    TypeError: 'NoneType' object is not iterable
**********************************************************************
1 items had failures:
   3 of  48 in __main__.example_8
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/slabbe/.sage//tmp/.doctest_morphism.py
	 [3.6 s]
exit code: 1024

```



---

Comment by vdelecroix created at 2010-02-01 00:17:06

Changing status from new to needs_review.


---

Comment by slabbe created at 2010-02-01 22:22:11

I just tested the patch. All test passed. Not tested the sphinx docbuild because the affected file is not part of the doc (maybe it should?). But I wonder if no blank line before the INPUT: line could raise a error in the docbuild process. I think the patch needs work for the reasons explained below.


The `string_rep()` output depends on the current state of the truncate length :


```
sage: u = Word('abcdbruitbruit01234...ababbruitbruit01234...abababab')
sage: u.string_rep()
'abcdbruitbruit01234...ababbruitbruit0123...'
```


which leads to the following bug :


```
sage: w = Word(range(20))
sage: u.split(w)
[word: abcdbruitbruit01234...ababbruitbruit0123...]
sage: WordOptions(truncate_length=5)
sage: u.split(w)
[word: abcdb..., word: ababb..., word: ababa...]
```


To correct this, I suggest that the function `split` be supported only for str and `WordDatatype_str` object.

Same suggestion for partition function:


```
sage: u = Word('abcdbruitbruit01234...ababbruitbruit01234...abababab')
sage: w = Word(range(20))
sage: u.partition(w)
[word: abcdbruitbruit01234...ababbruitbruit0123..., word: , word: ]
sage: WordOptions(truncate_length=5)
sage: u.partition(w)
[word: abcdb..., word: 01234..., word: ababb...]
```



I think split should follow the behavior of the python split for str, i.e works for no input given :


```
sage: s = 'absdg asdfas asdfa'
sage: s.split()
['absdg', 'asdfas', 'asdfa']
sage: s.split(' ')
['absdg', 'asdfas', 'asdfa']
sage: s.split(None)
['absdg', 'asdfas', 'asdfa']
sage: w = Word(s)
sage: w.split()
Traceback (most recent call last):
...
AttributeError: 'NoneType' object has no attribute 'string_rep'
sage: w.split(' ')
[word: absdg, word: asdfas, word: asdfa]
sage: w.split(None)
Traceback (most recent call last):
...
AttributeError: 'NoneType' object has no attribute 'string_rep'
```


The INPUT block of `split` should mention the part `(optional, default: None)` for both arguments.

For both functions, I suggest to move the `..notes` block after the OUTPUT block.


---

Comment by slabbe created at 2010-02-01 22:22:11

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2010-02-05 03:56:31

Changing component from algebra to combinatorics.


---

Comment by vdelecroix created at 2010-02-08 21:03:56

the broken thing is resolved (lines removed)


---

Comment by vdelecroix created at 2010-02-08 21:07:42

Changing status from needs_work to needs_review.


---

Attachment

This now needed to have a string (or a WordDatatype_str) as separator. A ValueError is raised when it's not the case.


---

Comment by slabbe created at 2010-02-10 00:21:59

Applies over the precedent patch


---

Attachment

I just added a patch which changes split function to follow python behavior for when no arguments are given and changed some doc mise en forme.

All tests passed. The above problem is solve. Sphinx builds fine on both functions. I am giving a positive review to Vincent's patch.

Vincent, if you agree with my patch, you can change the status of this ticket for positive review.


---

Comment by vdelecroix created at 2010-02-10 14:05:03

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2010-02-10 14:05:03

It's all right ;-)


---

Comment by mpatel created at 2010-02-11 14:49:25

Resolution: fixed
