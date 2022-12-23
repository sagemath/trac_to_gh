# Issue 4653: Merge sage-words code into Sage

Issue created by migration from https://trac.sagemath.org/ticket/4653

Original creator: saliola

Original creation time: 2008-11-29 12:45:28

Assignee: saliola

CC:  saliola anakha slabbe mhansen sage-combinat

Keywords: sage-combinat

The sage-word project wants to implement a complete package for word manipulation and combinatorics under Sage. The project maintains a [Google code page](http://code.google.com/p/sage-words).

The code has already been merged into sage-combinat, and although it needs a bit of work, it is ready to be merged into Sage. (By "needs a bit of work", I mean that there are some algorithms that need to be improved, but the code greatly improves the rudimentary functionality that exists in Sage.) The code is well documented, and a worksheet highlighting the features of the code can be found here:

 * [Sage worksheet](http://www-igm.univ-mlv.fr/~saliola/maths/talks/slides/SageTalk2/06_Words.sws)
 * [PDF file of worksheet](http://www-igm.univ-mlv.fr/~saliola/maths/talks/slides/SageTalk2/06_Words.pdf)

Arnaud Bergeron, Amy Glen, Sébastien Labbé, and Franco Saliola all contributed to the project, so they all deserve credit for this patch.


---

Comment by saliola created at 2008-11-29 12:46:23

Changing status from new to assigned.


---

Comment by saliola created at 2008-11-29 12:46:23

Changing type from defect to enhancement.


---

Comment by slabbe created at 2008-11-29 15:53:03

Good move saliola! I was going to ask what were the objectives before getting the code into sage. I had one :
 - Get back to the 100% documentation and coverage we had in sage-word google code. In fact, some functions had been added without doc and/or tests while merging the code in sage-combinat.
 - Any other?


---

Attachment

patch against 3.2


---

Comment by saliola created at 2008-11-30 00:05:27

> Good move saliola! I was going to ask what were the objectives before getting the code into sage. I had one :
>  - Get back to the 100% documentation and coverage we had in sage-word google code. In fact, some functions had been added without doc and/or tests while merging the code in sage-combinat.

Done. I added the missing doctests this evening. It is now at 100% again.

>  - Any other?

I think there are a few things that should be done at some point, but they are not "blockers". They are mostly issues to polish some of the rough edges.


---

Comment by mabshoff created at 2008-11-30 05:52:14

Hi guys,

one issue that might be worth considering now before merging is "name space pollution", i.e. there was some discussion at SD 11 that it would be better to have most of the functionality of certain packages like quadratic forms not in the global namespace. I am not sure what the situation with words is (sorry, no time to apply the patch and play :)), but it would be nice if most of the functionality would be in

```
words.$FOO
```

Sooner or later things will start colliding in the global namespace, so the time to fix this would be pre-merge :)

Cheers,

Michael


---

Comment by saliola created at 2008-11-30 11:42:21

Hello Michael,

Replying to [comment:4 mabshoff]:
> one issue that might be worth considering now before merging is "name space pollution", i.e. there was some discussion at SD 11 that it would be better to have most of the functionality of certain packages like quadratic forms not in the global namespace. I am not sure what the situation with words is (sorry, no time to apply the patch and play :)), but it would be nice if most of the functionality would be in
> {{{
> words.$FOO
> }}}
The all.py file imports only a few things into the global namespace:

```
Alphabet
Word
WordMorphism
WordOptions
Words
words
```

Should we merge them all into the new "words" class? I assume then that a user should be able to do something like the following to load all the commands into the global namespace easily:

```
from words import *
```

or 

```
LoadPackage(words)
```

Is there a standard way of doing this? I.e. a standard way of naming the class that gets imported as words, a standard way of naming the file that contains this class, etc. I think it would be nice if these are decided upon soon because it would make finding them in the source code easy.

Franco


---

Comment by mabshoff created at 2008-11-30 11:47:53

Replying to [comment:5 saliola]:
> Hello Michael,

Hi Franco,

> The all.py file imports only a few things into the global namespace:
> Alphabet
> Word
> WordMorphism
> WordOptions
> Words
> words

Ok, that seems acceptable. But what is the difference between words and Words? I can tell you that there are many people (including William) around in Sage that absolutely dislike case sensitivity behavior changes, i.e. think LinAlg in Maple 10 or so. 

> Should we merge them all into the new "words" class? I assume then that a user should be able to do something like the following to load all the commands into the global namespace easily

As mentioned above five symbols in global namespace is fine. There are other subsystems that are much, much worst in this regard and it will take a while to fix those.

> Is there a standard way of doing this? I.e. a standard way of naming the class that gets imported as words, a standard way of naming the file that contains this class, etc. I think it would be nice if these are decided upon soon because it would make finding them in the source code easy.

There is no standard way AFAIK, but we might want to come up with one as more and more "libraries" are becoming part of standard Sage.
 
> Franco

Cheers,

Michael


---

Comment by saliola created at 2008-11-30 12:08:48

Replying to [comment:6 mabshoff]:
> Replying to [comment:5 saliola]:
> > Hello Michael,
> 
> Hi Franco,
> 
> > The all.py file imports only a few things into the global namespace:
> > Alphabet
> > Word
> > WordMorphism
> > WordOptions
> > Words
> > words
> 
> Ok, that seems acceptable. But what is the difference between words and Words? I can tell you that there are many people (including William) around in Sage that absolutely dislike case sensitivity behavior changes, i.e. think LinAlg in Maple 10 or so. 

We got the idea from graphs to put all examples/pre-defined words into a class. So one could do something like words.FibonacciWord(), for example. But there is no Graphs class, so this is not a problem with graphs (although I suspect that if Nicolas reads this, then he'll want to create a combinatorial class of all graphs). I will change it, but I need a better name. Perhaps WordExamples or WordConstructor? That has the benefit of showing up in tab-completion. Is something similar done anywhere besides in graphs? It would be good to be consistent. 

Franco


---

Comment by mabshoff created at 2008-11-30 12:12:30

This discussion should probably be moved over to sage-devel and sage-combinat-devel.

Cheers,

Michael


---

Comment by slabbe created at 2008-12-09 22:34:36

>  I will change it, but I need a better name. Perhaps WordExamples or WordConstructor? That has the benefit of showing up in tab-completion.

Instead of the actual 'words', a suggestion could be 'lexicon' or 'wordbook' (I prefer the latter but I'm still not convinced).

slabbe


---

Comment by saliola created at 2008-12-11 20:13:58

Replying to [comment:9 slabbe]:
> 
> >  I will change it, but I need a better name. Perhaps WordExamples or WordConstructor? That has the benefit of showing up in tab-completion.
> 
> Instead of the actual 'words', a suggestion could be 'lexicon' or 'wordbook' (I prefer the latter but I'm still not convinced).

I really like the idea of putting everything under "words", so that all the functionality is available using tab completion:

```
sage: words.[tab]
words.Alphabet
words.Examples
words.Morphism
words.Word
words.Words
```

Then one can do:

```
sage: words.examples.ThueMorseWord()
}}} 
See finance.[tab] for a working example.

I also propose loading Words and Word into the global name space, in which case Words would be an alias for words (so words("ab") is the combinatorial class of all words over "ab").

Since we will want to add a bunch of other objects and not necessarily load them into the global name space (for example: Paths), this might be the best way to proceed.
 
What do you think? Other suggestions? We can also wait to see what the reviewer suggests.

Franco


---

Comment by mabshoff created at 2008-12-15 18:53:40

Another blocker :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-15 18:53:40

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-12-15 19:10:09

Franco,

all that needs rebasing is the first hunk from permutation.py. This is my attempt:

```
--- a/sage/combinat/permutation.py	Sun Dec 14 22:48:15 2008 -0800
+++ b/sage/combinat/permutation.py	Mon Dec 15 10:58:10 2008 -0800
@@ -213,7 +213,8 @@
             raise ValueError, "cannot convert l (= %s) to a Permutation"%l
 
     # otherwise, it gets processed by CombinatorialObject's __init__.
-    return Permutation_class(l)
+    # Unfortunately, it requires objects to be lists.
+    return Permutation_class(list(l))
 
 class Permutation_class(CombinatorialObject):
     def __hash__(self):
```

After some discussion with Mike in IRC we decided to postpone the words vs. Words issue to later.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-15 19:20:27

I am seeing two doctest failures, one which could have been caused by my dumb rebase attempt:

```
sage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests 
sage -t -long devel/sage/sage/combinat/words/word_generators.py # 1 doctests failed
```

In detail: This might be caused by missing pickles in the pickle jar:

```
sage -t -long "devel/sage/sage/structure/sage_object.pyx"   
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/structure/sage_object.pyx", line 371, in __main__.example_16
Failed example:
    sage.structure.sage_object.unpickle_all(std)###line 682:_sage_    >>> sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    ** failed:  _class__sage_combinat_word_Words_alphabet__.sobj
    ** failed:  _class__sage_combinat_word_Words_n__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_overlapping__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_shifted__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_overlapping_r__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_w1w2__.sobj
    Failed:
    _class__sage_combinat_word_Words_alphabet__.sobj
    _class__sage_combinat_word_Words_n__.sobj
    _class__sage_combinat_word_ShuffleProduct_overlapping__.sobj
    _class__sage_combinat_word_ShuffleProduct_shifted__.sobj
    _class__sage_combinat_word_ShuffleProduct_overlapping_r__.sobj
    _class__sage_combinat_word_ShuffleProduct_w1w2__.sobj
    Successfully unpickled 448 objects.
    Failed to unpickle 6 objects.
**********************************************************************
```

and

```
sage -t -long "devel/sage/sage/combinat/words/word_generators.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/combinat/words/word_generators.py", line 282, in __main__.example_6
Failed example:
    f[:Integer(10000)] == u[:Integer(10000)] #long time###line 286:_sage_    >>> f[:10000] == u[:10000] #long time
Expected:
    True
Got:
    False
**********************************************************************
```


Cheers,

Michael


---

Comment by slabbe created at 2008-12-15 20:37:59

I am taking care of the second one (related to word_generators.py) right now!

It will be in the sage-combinat tree in the next minutes...

slabbe


---

Comment by slabbe created at 2008-12-15 21:05:31

I put my changes into sage_words-4653-final.patch . Should I have done a new patch for the modification I did?

slabbe


---

Attachment

rebased version of the previous patch (so apply only this patch)


---

Comment by saliola created at 2008-12-15 23:06:09

I didn't see you message slabbe. I've already fixed the issue in the above patch.

I haven't done anything to address the words vs Words issue yet. But this is something that needs to be addressed soon. I like the idea of putting everything into words.[tab] and using 'from words.all import *' to pollute the global name space. I can do this fairly quickly (the hard part would be correcting the doctests).

Michael: just apply trac_4653.patch; and make sure that sage/combinat/word.py got deleted. Thanks.


---

Comment by mabshoff created at 2008-12-16 03:54:51

Replying to [comment:16 saliola]:
> I didn't see you message slabbe. I've already fixed the issue in the above patch.

Ok, the patch will go into rc1.

> I haven't done anything to address the words vs Words issue yet. But this is something that needs to be addressed soon. I like the idea of putting everything into words.[tab] and using 'from words.all import *' to pollute the global name space. I can do this fairly quickly (the hard part would be correcting the doctests).

I am not sure this is a good idea. For now I would suggest to keep everything as is.

> Michael: just apply trac_4653.patch; and make sure that sage/combinat/word.py got deleted. Thanks.

ok.

Mike: Can you give this an official review?

Cheers,

Micheal


---

Comment by mhansen created at 2008-12-17 11:03:35

I've looked over almost all of the code and am happy with it.  I think it should go in.  If any issues come up, we can take care of them later.

Assuming that this applies and passes tests, I give it a positive review.


---

Comment by mabshoff created at 2008-12-17 16:31:52

With Franco's latest patch there is at least one import issue:

```
  File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/combinat/sf/ns_macdonald.py", line 2, in <module>
    import sage.combinat.word as word
ImportError: No module named word
```

To reproduce nuke the old words py and pyc files from the build directory. I am poking around.

Cheers,

Michael


---

Attachment

Positive review on words-import-fix.patch


---

Comment by mabshoff created at 2008-12-17 16:58:05

Resolution: fixed


---

Comment by mabshoff created at 2008-12-17 16:58:05

Merged in Sage 3.2.2.rc1 - the pickling issue will be dealt with at #4640
