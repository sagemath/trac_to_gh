# Issue 7520: Improving word construction and datatype handling

Issue created by migration from https://trac.sagemath.org/ticket/7520

Original creator: slabbe

Original creation time: 2009-11-23 15:54:48

Assignee: mhansen

CC:  saliola

The `_check` function of the Combinatorial class of all words (checking that the 40 first letters of the word are in the parent) is called for each word created by the user ....and by any other function. It would be good to add a check parameter (True or False) whether to do the checking. For example, for internal function, it could be turned off. Here is a example of what can be gained from this modification when generating all words of a given length :

BEFORE:

```
sage: W = Words([0,1])
sage: time l = list(W.iterate_by_length(15))
CPU times: user 2.60 s, sys: 0.09 s, total: 2.69 s
Wall time: 2.71 s
```


AFTER:


```
sage: W = Words([0,1])
sage: time l = list(W.iterate_by_length(15))
CPU times: user 1.99 s, sys: 0.06 s, total: 2.05 s
Wall time: 2.08 s
```



Creation of a word from a word when the parent changes doesn't work well :


```
sage: w = Word('abab')
sage: P = WordPaths('abcd')
sage: P(w)
word: abab
sage: type(w)
<class 'sage.combinat.words.word.FiniteWord_str'>
sage: type(P(w))
<class 'sage.combinat.words.word.FiniteWord_str'>
```


Creation of a word represented by list from a word represented as str doesn't work well and could work easily:


```
sage: w = Word('aababababab')
sage: Word(w, datatype='list')
word: aababababab
sage: type(_)
<class 'sage.combinat.words.word.FiniteWord_str'>
```



---

Comment by slabbe created at 2009-11-23 15:55:22

Will post a patch soon...


---

Comment by slabbe created at 2009-11-23 15:55:22

Changing type from defect to enhancement.


---

Comment by slabbe created at 2009-11-30 15:20:55

My patch needs work:


```
sage: P = WordPaths([0,1,2,3])
sage: P
Word Paths on the square grid
sage: w = words.ChristoffelWord(5,8)
sage: P(w)
Traceback (most recent call last):
...
AttributeError: 'LowerChristoffelWord' object has no attribute '_class_str'
```


I must admit my patch was not that clean and it now shows its limits. The problem concerns the creation of a word from a word especially when the parent changes. Should we try to use some sort of shorcut (like simply change some important attributes like `__class__`) or not? I have an idea of something better which doesn't use any shortcut. For example, if the input word is a `FiniteWord_list`, we could simply restore the list and pass through the usual steps for when the input is a list. I think this should be more safe. I just have to think for a solution what we do when the word is defined as an iterator. A new patch (with cleaner code) to be posted soon.

Ideas are welcome.


---

Comment by slabbe created at 2009-11-30 15:20:55

Changing status from new to needs_work.


---

Comment by slabbe created at 2009-12-08 12:23:32

In the new patch, I made the corrections to `words.py` which handles in a some better way construction of words from words. There was one single strange doctest failing in `word.py` involving word morphisms. So, I improved again the `__call__` method of `WordMorphism` which was doing to much useless stuff.


---

Comment by slabbe created at 2009-12-08 12:23:32

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2009-12-08 12:23:47

Changing assignee from mhansen to slabbe.


---

Comment by slabbe created at 2010-01-06 18:57:47

I am changing the status to "needs work" because I thought of a cleaner way of solving this.

I will fold the two actual patches, improve them and post a new patch soon...


---

Comment by slabbe created at 2010-01-06 18:57:47

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2010-01-08 17:54:22

Forget about this patch.


---

Attachment


---

Comment by slabbe created at 2010-01-14 15:52:04

> I am changing the status to "needs work" because I thought of a cleaner way of solving this.

I still think that the construction of words is not clean, but I will not clean it in this ticket. This ticket solves some problems and I believe it can now get a review and an eventual merge into sage. 

Here are some key points I am actually thinking (I am writing them as a reference for future improvements):

 - The first version of sage-words got merged into sage in the end of December 2008. In January 2009, we quickly realized that many improvements should be done to the library (involving word construction, reorganisation of the classes and of course, many pickle problem...). In July 2009, the big reorganisation was merged into sage without breaking any pickle (Thanks to Franco for the quirk).
 - The code now looks really ugly for supporting the old pickled objects and I don't like ugly code. 
 - I am looking forward to get rid of word_content, utils and friends. 
 - I don't hide that I would be happy to have the right to break the pickle of the old word objects and replace the ugly code by clean and simple code.
 - Looking afterward, I think we should not have supported any pickling of word objects for the first year (by suggesting the users to save their word objects as lists). Doing so, it would have allow some time for us to find really what we think is the good solution for classes and word constructors.
 - `CallableFromListOfWords` inherits from tuple which I think is bad because (1) it doesn't have to and (2) it is the only last reason why one must use the datatype='callable' for word creation.
 - Then, get rid of the datatype argument.
 - I think that creating classes inline from bases classes (`MathObject` + `DataObject`) would work. And, in this case, `__reduce__` should not return a class as first argument but the usual Word function. Did Nicolas Thiéry convinced anyone about creating inline classes? Was it used in the lastly merged category code?
 - `WordDatatype_callable` is storing its data into the attributes `self._func` while I think all those `WordDatatype` should save their data into the same `self._data`.
 - When writing a `__reduce__` function, always make sure to put only essential things because this might become a problematic argument to be supported by creation function in the future. Moreover, the first argument of the tuple returned should be think as a function (or a class) that will always exist.
 - Right now only `WordDatatype` provide `__reduce__` function. Now, what if the `FiniteWord_class` now wants to store some attributes. How to set them again after loading a pickle word? It might work by defining `__setstate__` and `__getstate__` for `FiniteWord_class`... To be checked! I would be great if we could do it without defining any function in the (inline) classes like `FiniteWord_list`.

> I will fold the two actual patches, improve them and post a new patch soon...

So I did folded the two actual patches. I also updated the description of the patch to help the review. The patch now needs review!


---

Comment by slabbe created at 2010-01-14 15:52:04

Changing status from needs_work to needs_review.


---

Attachment

Apply only this one.


---

Comment by slabbe created at 2010-02-16 22:23:43

I just separated this ticket into three parts. It will make things easier for the reviewer like that since the three parts were really independant. See #8287 and #8289 for the issues that used to be discussed here.


---

Comment by saliola created at 2010-03-02 02:14:08

Sebastien, great job with the patch. I'm really glad the efficiency of the code is improving!

The patch applies cleanly to sage-4.3.3 and all doctests pass. Positive review.


---

Comment by saliola created at 2010-03-02 02:14:08

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-03 13:58:55

Resolution: fixed


---

Comment by mvngu created at 2010-03-03 13:58:55

Merged [trac_7520_words_construction_improvements-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7520/trac_7520_words_construction_improvements-sl.patch).
