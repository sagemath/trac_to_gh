# Issue 4653: Merge sage-words code into Sage

archive/issues_004653.json:
```json
{
    "body": "Assignee: saliola\n\nCC:  saliola anakha slabbe mhansen sage-combinat\n\nKeywords: sage-combinat\n\nThe sage-word project wants to implement a complete package for word manipulation and combinatorics under Sage. The project maintains a [Google code page](http://code.google.com/p/sage-words).\n\nThe code has already been merged into sage-combinat, and although it needs a bit of work, it is ready to be merged into Sage. (By \"needs a bit of work\", I mean that there are some algorithms that need to be improved, but the code greatly improves the rudimentary functionality that exists in Sage.) The code is well documented, and a worksheet highlighting the features of the code can be found here:\n\n* [Sage worksheet](http://www-igm.univ-mlv.fr/~saliola/maths/talks/slides/SageTalk2/06_Words.sws)\n* [PDF file of worksheet](http://www-igm.univ-mlv.fr/~saliola/maths/talks/slides/SageTalk2/06_Words.pdf)\n\nArnaud Bergeron, Amy Glen, S\u00e9bastien Labb\u00e9, and Franco Saliola all contributed to the project, so they all deserve credit for this patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4653\n\n",
    "created_at": "2008-11-29T12:45:28Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Merge sage-words code into Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4653",
    "user": "saliola"
}
```
Assignee: saliola

CC:  saliola anakha slabbe mhansen sage-combinat

Keywords: sage-combinat

The sage-word project wants to implement a complete package for word manipulation and combinatorics under Sage. The project maintains a [Google code page](http://code.google.com/p/sage-words).

The code has already been merged into sage-combinat, and although it needs a bit of work, it is ready to be merged into Sage. (By "needs a bit of work", I mean that there are some algorithms that need to be improved, but the code greatly improves the rudimentary functionality that exists in Sage.) The code is well documented, and a worksheet highlighting the features of the code can be found here:

* [Sage worksheet](http://www-igm.univ-mlv.fr/~saliola/maths/talks/slides/SageTalk2/06_Words.sws)
* [PDF file of worksheet](http://www-igm.univ-mlv.fr/~saliola/maths/talks/slides/SageTalk2/06_Words.pdf)

Arnaud Bergeron, Amy Glen, Sébastien Labbé, and Franco Saliola all contributed to the project, so they all deserve credit for this patch.

Issue created by migration from https://trac.sagemath.org/ticket/4653





---

archive/issue_comments_035025.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-29T12:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35025",
    "user": "saliola"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035026.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-11-29T12:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35026",
    "user": "saliola"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_035027.json:
```json
{
    "body": "Good move saliola! I was going to ask what were the objectives before getting the code into sage. I had one :\n- Get back to the 100% documentation and coverage we had in sage-word google code. In fact, some functions had been added without doc and/or tests while merging the code in sage-combinat.\n- Any other?",
    "created_at": "2008-11-29T15:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35027",
    "user": "slabbe"
}
```

Good move saliola! I was going to ask what were the objectives before getting the code into sage. I had one :
- Get back to the 100% documentation and coverage we had in sage-word google code. In fact, some functions had been added without doc and/or tests while merging the code in sage-combinat.
- Any other?



---

archive/issue_comments_035028.json:
```json
{
    "body": "Attachment\n\npatch against 3.2",
    "created_at": "2008-11-29T23:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35028",
    "user": "saliola"
}
```

Attachment

patch against 3.2



---

archive/issue_comments_035029.json:
```json
{
    "body": "> Good move saliola! I was going to ask what were the objectives before getting the code into sage. I had one :\n>  - Get back to the 100% documentation and coverage we had in sage-word google code. In fact, some functions had been added without doc and/or tests while merging the code in sage-combinat.\n\nDone. I added the missing doctests this evening. It is now at 100% again.\n\n>  - Any other?\n\nI think there are a few things that should be done at some point, but they are not \"blockers\". They are mostly issues to polish some of the rough edges.",
    "created_at": "2008-11-30T00:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35029",
    "user": "saliola"
}
```

> Good move saliola! I was going to ask what were the objectives before getting the code into sage. I had one :
>  - Get back to the 100% documentation and coverage we had in sage-word google code. In fact, some functions had been added without doc and/or tests while merging the code in sage-combinat.

Done. I added the missing doctests this evening. It is now at 100% again.

>  - Any other?

I think there are a few things that should be done at some point, but they are not "blockers". They are mostly issues to polish some of the rough edges.



---

archive/issue_comments_035030.json:
```json
{
    "body": "Hi guys,\n\none issue that might be worth considering now before merging is \"name space pollution\", i.e. there was some discussion at SD 11 that it would be better to have most of the functionality of certain packages like quadratic forms not in the global namespace. I am not sure what the situation with words is (sorry, no time to apply the patch and play :)), but it would be nice if most of the functionality would be in\n\n```\nwords.$FOO\n```\n\nSooner or later things will start colliding in the global namespace, so the time to fix this would be pre-merge :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T05:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35030",
    "user": "mabshoff"
}
```

Hi guys,

one issue that might be worth considering now before merging is "name space pollution", i.e. there was some discussion at SD 11 that it would be better to have most of the functionality of certain packages like quadratic forms not in the global namespace. I am not sure what the situation with words is (sorry, no time to apply the patch and play :)), but it would be nice if most of the functionality would be in

```
words.$FOO
```

Sooner or later things will start colliding in the global namespace, so the time to fix this would be pre-merge :)

Cheers,

Michael



---

archive/issue_comments_035031.json:
```json
{
    "body": "Hello Michael,\n\nReplying to [comment:4 mabshoff]:\n> one issue that might be worth considering now before merging is \"name space pollution\", i.e. there was some discussion at SD 11 that it would be better to have most of the functionality of certain packages like quadratic forms not in the global namespace. I am not sure what the situation with words is (sorry, no time to apply the patch and play :)), but it would be nice if most of the functionality would be in\n> {{{\n> words.$FOO\n> }}}\nThe all.py file imports only a few things into the global namespace:\n\n```\nAlphabet\nWord\nWordMorphism\nWordOptions\nWords\nwords\n```\n\nShould we merge them all into the new \"words\" class? I assume then that a user should be able to do something like the following to load all the commands into the global namespace easily:\n\n```\nfrom words import *\n```\n\nor \n\n```\nLoadPackage(words)\n```\n\nIs there a standard way of doing this? I.e. a standard way of naming the class that gets imported as words, a standard way of naming the file that contains this class, etc. I think it would be nice if these are decided upon soon because it would make finding them in the source code easy.\n\nFranco",
    "created_at": "2008-11-30T11:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35031",
    "user": "saliola"
}
```

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

archive/issue_comments_035032.json:
```json
{
    "body": "Replying to [comment:5 saliola]:\n> Hello Michael,\n\nHi Franco,\n\n> The all.py file imports only a few things into the global namespace:\n> Alphabet\n> Word\n> WordMorphism\n> WordOptions\n> Words\n> words\n\nOk, that seems acceptable. But what is the difference between words and Words? I can tell you that there are many people (including William) around in Sage that absolutely dislike case sensitivity behavior changes, i.e. think LinAlg in Maple 10 or so. \n\n> Should we merge them all into the new \"words\" class? I assume then that a user should be able to do something like the following to load all the commands into the global namespace easily\n\nAs mentioned above five symbols in global namespace is fine. There are other subsystems that are much, much worst in this regard and it will take a while to fix those.\n\n> Is there a standard way of doing this? I.e. a standard way of naming the class that gets imported as words, a standard way of naming the file that contains this class, etc. I think it would be nice if these are decided upon soon because it would make finding them in the source code easy.\n\nThere is no standard way AFAIK, but we might want to come up with one as more and more \"libraries\" are becoming part of standard Sage.\n \n> Franco\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T11:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35032",
    "user": "mabshoff"
}
```

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

archive/issue_comments_035033.json:
```json
{
    "body": "Replying to [comment:6 mabshoff]:\n> Replying to [comment:5 saliola]:\n> > Hello Michael,\n> \n> Hi Franco,\n> \n> > The all.py file imports only a few things into the global namespace:\n> > Alphabet\n> > Word\n> > WordMorphism\n> > WordOptions\n> > Words\n> > words\n> \n> Ok, that seems acceptable. But what is the difference between words and Words? I can tell you that there are many people (including William) around in Sage that absolutely dislike case sensitivity behavior changes, i.e. think LinAlg in Maple 10 or so. \n\nWe got the idea from graphs to put all examples/pre-defined words into a class. So one could do something like words.FibonacciWord(), for example. But there is no Graphs class, so this is not a problem with graphs (although I suspect that if Nicolas reads this, then he'll want to create a combinatorial class of all graphs). I will change it, but I need a better name. Perhaps WordExamples or WordConstructor? That has the benefit of showing up in tab-completion. Is something similar done anywhere besides in graphs? It would be good to be consistent. \n\nFranco",
    "created_at": "2008-11-30T12:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35033",
    "user": "saliola"
}
```

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

archive/issue_comments_035034.json:
```json
{
    "body": "This discussion should probably be moved over to sage-devel and sage-combinat-devel.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T12:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35034",
    "user": "mabshoff"
}
```

This discussion should probably be moved over to sage-devel and sage-combinat-devel.

Cheers,

Michael



---

archive/issue_comments_035035.json:
```json
{
    "body": ">  I will change it, but I need a better name. Perhaps WordExamples or WordConstructor? That has the benefit of showing up in tab-completion.\n\nInstead of the actual 'words', a suggestion could be 'lexicon' or 'wordbook' (I prefer the latter but I'm still not convinced).\n\nslabbe",
    "created_at": "2008-12-09T22:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35035",
    "user": "slabbe"
}
```

>  I will change it, but I need a better name. Perhaps WordExamples or WordConstructor? That has the benefit of showing up in tab-completion.

Instead of the actual 'words', a suggestion could be 'lexicon' or 'wordbook' (I prefer the latter but I'm still not convinced).

slabbe



---

archive/issue_comments_035036.json:
```json
{
    "body": "Replying to [comment:9 slabbe]:\n> \n> >  I will change it, but I need a better name. Perhaps WordExamples or WordConstructor? That has the benefit of showing up in tab-completion.\n> \n> Instead of the actual 'words', a suggestion could be 'lexicon' or 'wordbook' (I prefer the latter but I'm still not convinced).\n\nI really like the idea of putting everything under \"words\", so that all the functionality is available using tab completion:\n\n```\nsage: words.[tab]\nwords.Alphabet\nwords.Examples\nwords.Morphism\nwords.Word\nwords.Words\n```\n\nThen one can do:\n\n```\nsage: words.examples.ThueMorseWord()\n```\n \nSee finance.[tab] for a working example.\n\nI also propose loading Words and Word into the global name space, in which case Words would be an alias for words (so words(\"ab\") is the combinatorial class of all words over \"ab\").\n\nSince we will want to add a bunch of other objects and not necessarily load them into the global name space (for example: Paths), this might be the best way to proceed.\n \nWhat do you think? Other suggestions? We can also wait to see what the reviewer suggests.\n\nFranco",
    "created_at": "2008-12-11T20:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35036",
    "user": "saliola"
}
```

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
```
 
See finance.[tab] for a working example.

I also propose loading Words and Word into the global name space, in which case Words would be an alias for words (so words("ab") is the combinatorial class of all words over "ab").

Since we will want to add a bunch of other objects and not necessarily load them into the global name space (for example: Paths), this might be the best way to proceed.
 
What do you think? Other suggestions? We can also wait to see what the reviewer suggests.

Franco



---

archive/issue_comments_035037.json:
```json
{
    "body": "Another blocker :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-15T18:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35037",
    "user": "mabshoff"
}
```

Another blocker :)

Cheers,

Michael



---

archive/issue_comments_035038.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-12-15T18:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35038",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_035039.json:
```json
{
    "body": "Franco,\n\nall that needs rebasing is the first hunk from permutation.py. This is my attempt:\n\n```\n--- a/sage/combinat/permutation.py\tSun Dec 14 22:48:15 2008 -0800\n+++ b/sage/combinat/permutation.py\tMon Dec 15 10:58:10 2008 -0800\n@@ -213,7 +213,8 @@\n             raise ValueError, \"cannot convert l (= %s) to a Permutation\"%l\n \n     # otherwise, it gets processed by CombinatorialObject's __init__.\n-    return Permutation_class(l)\n+    # Unfortunately, it requires objects to be lists.\n+    return Permutation_class(list(l))\n \n class Permutation_class(CombinatorialObject):\n     def __hash__(self):\n```\n\nAfter some discussion with Mike in IRC we decided to postpone the words vs. Words issue to later.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-15T19:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35039",
    "user": "mabshoff"
}
```

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

archive/issue_comments_035040.json:
```json
{
    "body": "I am seeing two doctest failures, one which could have been caused by my dumb rebase attempt:\n\n```\nsage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests \nsage -t -long devel/sage/sage/combinat/words/word_generators.py # 1 doctests failed\n```\n\nIn detail: This might be caused by missing pickles in the pickle jar:\n\n```\nsage -t -long \"devel/sage/sage/structure/sage_object.pyx\"   \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/structure/sage_object.pyx\", line 371, in __main__.example_16\nFailed example:\n    sage.structure.sage_object.unpickle_all(std)###line 682:_sage_    >>> sage.structure.sage_object.unpickle_all(std)\nExpected:\n    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n    Successfully unpickled ... objects.\n    Failed to unpickle 0 objects.\nGot:\n    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n    ** failed:  _class__sage_combinat_word_Words_alphabet__.sobj\n    ** failed:  _class__sage_combinat_word_Words_n__.sobj\n    ** failed:  _class__sage_combinat_word_ShuffleProduct_overlapping__.sobj\n    ** failed:  _class__sage_combinat_word_ShuffleProduct_shifted__.sobj\n    ** failed:  _class__sage_combinat_word_ShuffleProduct_overlapping_r__.sobj\n    ** failed:  _class__sage_combinat_word_ShuffleProduct_w1w2__.sobj\n    Failed:\n    _class__sage_combinat_word_Words_alphabet__.sobj\n    _class__sage_combinat_word_Words_n__.sobj\n    _class__sage_combinat_word_ShuffleProduct_overlapping__.sobj\n    _class__sage_combinat_word_ShuffleProduct_shifted__.sobj\n    _class__sage_combinat_word_ShuffleProduct_overlapping_r__.sobj\n    _class__sage_combinat_word_ShuffleProduct_w1w2__.sobj\n    Successfully unpickled 448 objects.\n    Failed to unpickle 6 objects.\n**********************************************************************\n```\n\nand\n\n```\nsage -t -long \"devel/sage/sage/combinat/words/word_generators.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/combinat/words/word_generators.py\", line 282, in __main__.example_6\nFailed example:\n    f[:Integer(10000)] == u[:Integer(10000)] #long time###line 286:_sage_    >>> f[:10000] == u[:10000] #long time\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-15T19:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35040",
    "user": "mabshoff"
}
```

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

archive/issue_comments_035041.json:
```json
{
    "body": "I am taking care of the second one (related to word_generators.py) right now!\n\nIt will be in the sage-combinat tree in the next minutes...\n\nslabbe",
    "created_at": "2008-12-15T20:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35041",
    "user": "slabbe"
}
```

I am taking care of the second one (related to word_generators.py) right now!

It will be in the sage-combinat tree in the next minutes...

slabbe



---

archive/issue_comments_035042.json:
```json
{
    "body": "I put my changes into sage_words-4653-final.patch . Should I have done a new patch for the modification I did?\n\nslabbe",
    "created_at": "2008-12-15T21:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35042",
    "user": "slabbe"
}
```

I put my changes into sage_words-4653-final.patch . Should I have done a new patch for the modification I did?

slabbe



---

archive/issue_comments_035043.json:
```json
{
    "body": "Attachment\n\nrebased version of the previous patch (so apply only this patch)",
    "created_at": "2008-12-15T22:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35043",
    "user": "saliola"
}
```

Attachment

rebased version of the previous patch (so apply only this patch)



---

archive/issue_comments_035044.json:
```json
{
    "body": "I didn't see you message slabbe. I've already fixed the issue in the above patch.\n\nI haven't done anything to address the words vs Words issue yet. But this is something that needs to be addressed soon. I like the idea of putting everything into words.[tab] and using 'from words.all import *' to pollute the global name space. I can do this fairly quickly (the hard part would be correcting the doctests).\n\nMichael: just apply trac_4653.patch; and make sure that sage/combinat/word.py got deleted. Thanks.",
    "created_at": "2008-12-15T23:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35044",
    "user": "saliola"
}
```

I didn't see you message slabbe. I've already fixed the issue in the above patch.

I haven't done anything to address the words vs Words issue yet. But this is something that needs to be addressed soon. I like the idea of putting everything into words.[tab] and using 'from words.all import *' to pollute the global name space. I can do this fairly quickly (the hard part would be correcting the doctests).

Michael: just apply trac_4653.patch; and make sure that sage/combinat/word.py got deleted. Thanks.



---

archive/issue_comments_035045.json:
```json
{
    "body": "Replying to [comment:16 saliola]:\n> I didn't see you message slabbe. I've already fixed the issue in the above patch.\n\nOk, the patch will go into rc1.\n\n> I haven't done anything to address the words vs Words issue yet. But this is something that needs to be addressed soon. I like the idea of putting everything into words.[tab] and using 'from words.all import *' to pollute the global name space. I can do this fairly quickly (the hard part would be correcting the doctests).\n\nI am not sure this is a good idea. For now I would suggest to keep everything as is.\n\n> Michael: just apply trac_4653.patch; and make sure that sage/combinat/word.py got deleted. Thanks.\n\nok.\n\nMike: Can you give this an official review?\n\nCheers,\n\nMicheal",
    "created_at": "2008-12-16T03:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35045",
    "user": "mabshoff"
}
```

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

archive/issue_comments_035046.json:
```json
{
    "body": "I've looked over almost all of the code and am happy with it.  I think it should go in.  If any issues come up, we can take care of them later.\n\nAssuming that this applies and passes tests, I give it a positive review.",
    "created_at": "2008-12-17T11:03:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35046",
    "user": "mhansen"
}
```

I've looked over almost all of the code and am happy with it.  I think it should go in.  If any issues come up, we can take care of them later.

Assuming that this applies and passes tests, I give it a positive review.



---

archive/issue_comments_035047.json:
```json
{
    "body": "With Franco's latest patch there is at least one import issue:\n\n```\n  File \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/combinat/sf/ns_macdonald.py\", line 2, in <module>\n    import sage.combinat.word as word\nImportError: No module named word\n```\n\nTo reproduce nuke the old words py and pyc files from the build directory. I am poking around.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-17T16:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35047",
    "user": "mabshoff"
}
```

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

archive/issue_comments_035048.json:
```json
{
    "body": "Attachment\n\nPositive review on words-import-fix.patch",
    "created_at": "2008-12-17T16:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35048",
    "user": "mabshoff"
}
```

Attachment

Positive review on words-import-fix.patch



---

archive/issue_comments_035049.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-17T16:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35049",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035050.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc1 - the pickling issue will be dealt with at #4640",
    "created_at": "2008-12-17T16:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4653#issuecomment-35050",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.rc1 - the pickling issue will be dealt with at #4640
