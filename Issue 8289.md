# Issue 8289: Clean up WordMorphism.__call__

archive/issues_008289.json:
```json
{
    "body": "Assignee: slabbe\n\nCC:  abmasse\n\n`WordMorphism.__call__` is doing a conversion of the input into the domain which is not necessary. Basicly, all what is needed is that the input be iterable. Here are some timing improvements :\n\nBEFORE:\n\n\n```\nsage: m = WordMorphism('a->aab,b->ba')\nsage: %timeit w = m('a'*100)\n1000 loops, best of 3: 343 \u00b5s per loop\n```\n\n\nAFTER:\n\n\n```\nsage: m = WordMorphism('a->aab,b->ba')\nsage: %timeit w = m('a'*100)\n1000 loops, best of 3: 242 \u00b5s per loop\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8289\n\n",
    "created_at": "2010-02-16T22:17:45Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Clean up WordMorphism.__call__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8289",
    "user": "slabbe"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/8289





---

archive/issue_comments_073417.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-17T00:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73417",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073418.json:
```json
{
    "body": "Hello S\u00e9bastien !\n\nI started reviewing your patch with the sage-combinat mercurial queue and I noticed that some tests didn't pass. This is probably due to the patch where you remove the `check` function that verifies the 40 first letters, but for sake of sureness, could you move your patch up in the series file ?\n\nShort of that, I don't think it will be too hard to review.",
    "created_at": "2010-02-26T10:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73418",
    "user": "abmasse"
}
```

Hello Sébastien !

I started reviewing your patch with the sage-combinat mercurial queue and I noticed that some tests didn't pass. This is probably due to the patch where you remove the `check` function that verifies the 40 first letters, but for sake of sureness, could you move your patch up in the series file ?

Short of that, I don't think it will be too hard to review.



---

archive/issue_comments_073419.json:
```json
{
    "body": "Here are more details.\n\n\n```\n[~/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words]$ sage -t *\nsage -t  \"devel/sage-combinat/sage/combinat/words/__init__.py\"\n\t [0.1 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/all.py\"   \n\t [0.1 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/alphabet.py\"\n\t [2.4 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/morphism.py\"\n\t [2.5 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/paths.py\" \n\t [8.0 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/shuffle_product.py\"\n\t [2.1 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/suffix_trees.py\"\n\t [4.9 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/utils.py\" \n\t [2.1 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/word.py\"  \n**********************************************************************\nFile \"/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word.py\", line 1894:\n    sage: z + y\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: 5 not in alphabet!\nGot:\n    word: 1222353587\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_38\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_word.py\n\t [11.6 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/word_content.py\"\n\t [2.2 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/word_datatypes.pyx\"\n\t [2.1 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/word_generators.py\"\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_generators.py\", line 354:\n    sage: words.ThueMorseWord(alphabet='ab', base=1)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: base (=1) and len(alphabet) (=2) must be at least 2\nGot:\n    Traceback (most recent call last):\n      File \"/Users/alexandre/Applications/sage-4.3.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage-4.3.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage-4.3.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_9[9]>\", line 1, in <module>\n        words.ThueMorseWord(alphabet='ab', base=Integer(1))###line 354:\n    sage: words.ThueMorseWord(alphabet='ab', base=1)\n      File \"/Users/alexandre/Applications/sage-4.3.3/local/lib/python/site-packages/sage/combinat/words/word_generators.py\", line 376, in ThueMorseWord\n        raise ValueError, \"base (=%s) and size of alphabet (=%s) must be at least 2\"%(base, m)\n    ValueError: base (=1) and size of alphabet (=2) must be at least 2\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_9\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_word_generators.py\n\t [8.4 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py\"\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py\", line 499:\n    sage: w._letter_cache\nExpected:\n    {0: 0, 1: 1, 2: 1, 3: 0, 4: 1, 5: 0, 6: 0, 7: 1, 8: 1, 9: 0, 10: 0, 11: 1, 12: 0, 13: 1, 14: 1, 15: 0, 16: 1, 17: 0, 18: 0, 19: 1, 20: 0, 21: 1, 22: 1, 23: 0, 24: 0, 25: 1, 26: 1, 27: 0, 28: 1, 29: 0, 30: 0, 31: 1, 32: 1, 33: 0, 34: 0, 35: 1, 36: 0, 37: 1, 38: 1, 39: 0}\nGot:\n    {}\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py\", line 503:\n    sage: w._letter_cache\nExpected:\n    {0: 0, 1: 1, 2: 1, 3: 0, 4: 1, 5: 0, 6: 0, 7: 1, 8: 1, 9: 0, 10: 0, 11: 1, 12: 0, 13: 1, 14: 1, 15: 0, 16: 1, 17: 0, 18: 0, 19: 1, 20: 0, 21: 1, 22: 1, 23: 0, 24: 0, 25: 1, 26: 1, 27: 0, 28: 1, 29: 0, 30: 0, 31: 1, 32: 1, 33: 0, 34: 0, 35: 1, 36: 0, 37: 1, 38: 1, 39: 0, 100: 1}\nGot:\n    {100: 1}\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py\", line 820:\n    sage: w.__reduce__()\nExpected:\n    (<function Word at ...>, (<generator object __iter__ at ...>, Words, 2, 'iter', False))\nGot:\n    (<function Word at 0x10b933b18>, (<generator object __iter__ at 0x10c4a00a0>, Words, None, 'iter', False))\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py\", line 1087:\n    sage: w.__reduce__()\nExpected:\n    (<function Word at ...>, (<generator object __iter__ at ...>, Words, 2, 'iter', True))\nGot:\n    (<function Word at 0x10b933b18>, (<generator object __iter__ at 0x100468190>, Words, None, 'iter', True))\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py\", line 1104:\n    sage: w._last_index, len(w._list)\nExpected:\n    (39, 40)\nGot:\n    (-1, 0)\n**********************************************************************\n4 items had failures:\n   2 of   8 in __main__.example_11\n   1 of   6 in __main__.example_15\n   1 of   6 in __main__.example_19\n   1 of   9 in __main__.example_20\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_word_infinite_datatypes.py\n\t [2.2 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/word_options.py\"\n\t [2.1 s]\nsage -t  \"devel/sage-combinat/sage/combinat/words/words.py\" \n**********************************************************************\nFile \"/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/words.py\", line 207:\n    sage: Words(range(10))(count())\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: 10 not in alphabet!\nGot:\n    word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage-4.3.3/devel/sage-combinat/sage/combinat/words/words.py\", line 215:\n    sage: Words(\"ab\")(\"abca\")\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: c not in alphabet!\nGot:\n    word: abca\n**********************************************************************\n1 items had failures:\n   2 of   8 in __main__.example_4\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_words.py\n\t [2.2 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"devel/sage-combinat/sage/combinat/words/word.py\"\n\tsage -t  \"devel/sage-combinat/sage/combinat/words/word_generators.py\"\n\tsage -t  \"devel/sage-combinat/sage/combinat/words/word_infinite_datatypes.py\"\n\tsage -t  \"devel/sage-combinat/sage/combinat/words/words.py\"\nTotal time for all tests: 53.1 seconds\n```\n",
    "created_at": "2010-02-26T13:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73419",
    "user": "abmasse"
}
```

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

archive/issue_comments_073420.json:
```json
{
    "body": "Attachment [trac_8289_wordmorphism_call-sl.patch](tarball://root/attachments/some-uuid/ticket8289/trac_8289_wordmorphism_call-sl.patch) by slabbe created at 2010-02-26 23:57:38",
    "created_at": "2010-02-26T23:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73420",
    "user": "slabbe"
}
```

Attachment [trac_8289_wordmorphism_call-sl.patch](tarball://root/attachments/some-uuid/ticket8289/trac_8289_wordmorphism_call-sl.patch) by slabbe created at 2010-02-26 23:57:38



---

archive/issue_comments_073421.json:
```json
{
    "body": "> I started reviewing your patch with the sage-combinat mercurial queue and I noticed that some tests didn't pass. This is probably due to the patch where you remove the `check` function that verifies the 40 first letters, but for sake of sureness, could you move your patch up in the series file ?\n\nDone. I removed the check patch since I found a better solution for it. The patch 8289 should now be fine in the sage-combinat tree.",
    "created_at": "2010-02-27T01:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73421",
    "user": "slabbe"
}
```

> I started reviewing your patch with the sage-combinat mercurial queue and I noticed that some tests didn't pass. This is probably due to the patch where you remove the `check` function that verifies the 40 first letters, but for sake of sureness, could you move your patch up in the series file ?

Done. I removed the check patch since I found a better solution for it. The patch 8289 should now be fine in the sage-combinat tree.



---

archive/issue_comments_073422.json:
```json
{
    "body": "Hello, S\u00e9bastien !\n\nJust one question. I get the following:\n\n\n```\nsage: m = WordMorphism('a->b,b->a')\nsage: m(Word())\nword: \nsage: m(Word(), oo)\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/Users/alexandre/<ipython console> in <module>()\n\n/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/words/morphism.pyc in __call__(self, w, order, datatype)\n    561         if order is Infinity:\n    562             if isinstance(w, (tuple,str,list,FiniteWord_class)):\n--> 563                 letter = w[0]\n    564             elif hasattr(w, '__iter__'):\n    565                 letter = w.next()\n\n/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/words/word_datatypes.so in sage.combinat.words.word_datatypes.WordDatatype_list.__getitem__ (sage/combinat/words/word_datatypes.cpp:1407)()\n\nIndexError: list index out of range\n```\n\n\nDon't you think we should get the empty word in that case ? This seems to be well-defined.",
    "created_at": "2010-02-28T11:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73422",
    "user": "abmasse"
}
```

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

archive/issue_comments_073423.json:
```json
{
    "body": "By the way, you don't need to modify your patch accordingly if you agree, I've already started one for the review, so I can add it easily.",
    "created_at": "2010-02-28T11:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73423",
    "user": "abmasse"
}
```

By the way, you don't need to modify your patch accordingly if you agree, I've already started one for the review, so I can add it easily.



---

archive/issue_comments_073424.json:
```json
{
    "body": "Replying to [comment:6 abmasse]:\n> By the way, you don't need to modify your patch accordingly if you agree, I've already started one for the review, so I can add it easily.\n\nOf course I agree. We should return the empty word in this case...",
    "created_at": "2010-02-28T14:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73424",
    "user": "slabbe"
}
```

Replying to [comment:6 abmasse]:
> By the way, you don't need to modify your patch accordingly if you agree, I've already started one for the review, so I can add it easily.

Of course I agree. We should return the empty word in this case...



---

archive/issue_comments_073425.json:
```json
{
    "body": "I'm finished with the review! The changes brought by this patch appears reasonable and do indeed speed up some treatments without slowing down other ones.\n\nI modified some formatting in the documentation, and I treated the case where the morphism is applied on the empty word with infinite order.  Everything seems fine to me. I wait until you check my change to set this patch to positive review.\n\nUploading the review patch in a few seconds.",
    "created_at": "2010-02-28T23:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73425",
    "user": "abmasse"
}
```

I'm finished with the review! The changes brought by this patch appears reasonable and do indeed speed up some treatments without slowing down other ones.

I modified some formatting in the documentation, and I treated the case where the morphism is applied on the empty word with infinite order.  Everything seems fine to me. I wait until you check my change to set this patch to positive review.

Uploading the review patch in a few seconds.



---

archive/issue_comments_073426.json:
```json
{
    "body": "Attachment [trac_8289_review-abm.patch](tarball://root/attachments/some-uuid/ticket8289/trac_8289_review-abm.patch) by abmasse created at 2010-02-28 23:40:47\n\nReview - doc changes and empty word case -- apply on top of the first patch",
    "created_at": "2010-02-28T23:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73426",
    "user": "abmasse"
}
```

Attachment [trac_8289_review-abm.patch](tarball://root/attachments/some-uuid/ticket8289/trac_8289_review-abm.patch) by abmasse created at 2010-02-28 23:40:47

Review - doc changes and empty word case -- apply on top of the first patch



---

archive/issue_comments_073427.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-01T00:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73427",
    "user": "slabbe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073428.json:
```json
{
    "body": "Thanks for your review. I like your changes. I tested them: all tests passed. Doc builds fine. Empty word problem fixed.\n\nPositive review.",
    "created_at": "2010-03-01T00:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73428",
    "user": "slabbe"
}
```

Thanks for your review. I like your changes. I tested them: all tests passed. Doc builds fine. Empty word problem fixed.

Positive review.



---

archive/issue_comments_073429.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8289_wordmorphism_call-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8289/trac_8289_wordmorphism_call-sl.patch)\n2. [trac_8289_review-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8289/trac_8289_review-abm.patch)",
    "created_at": "2010-03-02T21:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73429",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_8289_wordmorphism_call-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8289/trac_8289_wordmorphism_call-sl.patch)
2. [trac_8289_review-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8289/trac_8289_review-abm.patch)



---

archive/issue_comments_073430.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8289#issuecomment-73430",
    "user": "mvngu"
}
```

Resolution: fixed
