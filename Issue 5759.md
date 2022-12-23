# Issue 5759: bug in divides

archive/issues_005759.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: Zmod(2)(0).divides(Zmod(2)(1))\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/teragon.local/50691/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.CommutativeRingElement.divides (sage/structure/element.c:12423)()\n\n/Users/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/rings/integer_mod.so in sage.rings.integer_mod.IntegerMod_int.__mod__ (sage/rings/integer_mod.c:17834)()\n   1867     def __mod__(IntegerMod_int self, right):\n   1868         right = int(right)\n-> 1869         if self.__modulus.int32 % right != 0:\n   1870             raise ZeroDivisionError, \"reduction modulo right not defined.\"\n   1871         return integer_mod_ring.IntegerModRing(right)(self)\n\nZeroDivisionError: integer division or modulo by zero\n\nFound by  kilian__ on irc.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5759\n\n",
    "created_at": "2009-04-11T18:37:49Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "bug in divides",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5759",
    "user": "was"
}
```
Assignee: somebody


```
sage: Zmod(2)(0).divides(Zmod(2)(1))
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon.local/50691/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.CommutativeRingElement.divides (sage/structure/element.c:12423)()

/Users/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/rings/integer_mod.so in sage.rings.integer_mod.IntegerMod_int.__mod__ (sage/rings/integer_mod.c:17834)()
   1867     def __mod__(IntegerMod_int self, right):
   1868         right = int(right)
-> 1869         if self.__modulus.int32 % right != 0:
   1870             raise ZeroDivisionError, "reduction modulo right not defined."
   1871         return integer_mod_ring.IntegerModRing(right)(self)

ZeroDivisionError: integer division or modulo by zero

Found by  kilian__ on irc.
```


Issue created by migration from https://trac.sagemath.org/ticket/5759





---

archive/issue_comments_045007.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2009-04-11T22:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45007",
    "user": "kkilger"
}
```

Changing priority from minor to major.



---

archive/issue_comments_045008.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-11T22:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45008",
    "user": "kkilger"
}
```

Attachment



---

archive/issue_comments_045009.json:
```json
{
    "body": "Changing assignee from somebody to was.",
    "created_at": "2009-04-11T22:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45009",
    "user": "kkilger"
}
```

Changing assignee from somebody to was.



---

archive/issue_comments_045010.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-11T22:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45010",
    "user": "kkilger"
}
```

Attachment



---

archive/issue_comments_045011.json:
```json
{
    "body": "This breaks a doctest somewhere else:\n\n\n```\nwstein@sage:~/build/sage-3.4.1.rc2$ ./sage -t  devel/sage/sage/coding/code_constructions.py\nsage -t  \"devel/sage/sage/coding/code_constructions.py\"\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2/devel/sage/sage/coding/code_constructions.py\", line 530:\n    sage: g.divides(f)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_7[6]>\", line 1, in <module>\n        g.divides(f)###line 530:\n    sage: g.divides(f)\n      File \"element.pyx\", line 1380, in sage.structure.element.CommutativeRingElement.divides (sage/structure/element.c:12436)\n      File \"parent_old.pyx\", line 334, in sage.structure.parent_old.Parent._coerce_c (sage/structure/parent_old.c:5417)\n      File \"parent_old.pyx\", line 336, in sage.structure.parent_old.Parent._coerce_c (sage/structure/parent_old.c:5186)\n      File \"parent.pyx\", line 374, in sage.structure.parent.Parent.coerce (sage/structure/parent.c:4994)\n    TypeError: no canonical coercion from Univariate Polynomial Ring in x over Finite Field in a of size 3^2 to Univariate Polynomial Ring in x over Finite Field of size 3\n**********************************************************************\n1 items had failures:\n   1 of  14 in __main__.example_7\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2/tmp/.doctest_code_constructions.py\n         [4.2 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/coding/code_constructions.py\"\nTotal time for all tests: 4.2 seconds\n```\n",
    "created_at": "2009-04-12T04:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45011",
    "user": "was"
}
```

This breaks a doctest somewhere else:


```
wstein@sage:~/build/sage-3.4.1.rc2$ ./sage -t  devel/sage/sage/coding/code_constructions.py
sage -t  "devel/sage/sage/coding/code_constructions.py"
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage/sage/coding/code_constructions.py", line 530:
    sage: g.divides(f)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[6]>", line 1, in <module>
        g.divides(f)###line 530:
    sage: g.divides(f)
      File "element.pyx", line 1380, in sage.structure.element.CommutativeRingElement.divides (sage/structure/element.c:12436)
      File "parent_old.pyx", line 334, in sage.structure.parent_old.Parent._coerce_c (sage/structure/parent_old.c:5417)
      File "parent_old.pyx", line 336, in sage.structure.parent_old.Parent._coerce_c (sage/structure/parent_old.c:5186)
      File "parent.pyx", line 374, in sage.structure.parent.Parent.coerce (sage/structure/parent.c:4994)
    TypeError: no canonical coercion from Univariate Polynomial Ring in x over Finite Field in a of size 3^2 to Univariate Polynomial Ring in x over Finite Field of size 3
**********************************************************************
1 items had failures:
   1 of  14 in __main__.example_7
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2/tmp/.doctest_code_constructions.py
         [4.2 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/coding/code_constructions.py"
Total time for all tests: 4.2 seconds
```




---

archive/issue_comments_045012.json:
```json
{
    "body": "The whole divides function is broken (nearly irreparable) with the effect that \"divides\" failes or gives *wrong* answers if and only if the ring is no polynomial ring or ZZ (which have their own (buggy) implementation). \n\nThe reason is that not all commutative rings are euclidean domains and \"modulo\" operation does not do what it is supposed to do in general commutative rings, for example in finite integer rings: Zmod(12)(3) % Zmod(12)(4) gives Zmod(3)(0) (which is also broken, by the way). \n\nThe only correct behaviour would be:\n\n1. to raise a NotImplementedError in element.py and let all subclasses implemenent their own divides. \n     or:\n2. define divides as \"inclusion of ideals\" and give errors if the subclasses can't check the inclusion of ideals. \n\nAlso: all doctests in element.py and other files are for polynomial rings only, with the effect that many functions in SAGE fail or give *wrong* answers if the ring is no polynomial ring.  \n\nGreetings,\nKilian.",
    "created_at": "2009-04-12T14:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45012",
    "user": "kkilger"
}
```

The whole divides function is broken (nearly irreparable) with the effect that "divides" failes or gives *wrong* answers if and only if the ring is no polynomial ring or ZZ (which have their own (buggy) implementation). 

The reason is that not all commutative rings are euclidean domains and "modulo" operation does not do what it is supposed to do in general commutative rings, for example in finite integer rings: Zmod(12)(3) % Zmod(12)(4) gives Zmod(3)(0) (which is also broken, by the way). 

The only correct behaviour would be:

1. to raise a NotImplementedError in element.py and let all subclasses implemenent their own divides. 
     or:
2. define divides as "inclusion of ideals" and give errors if the subclasses can't check the inclusion of ideals. 

Also: all doctests in element.py and other files are for polynomial rings only, with the effect that many functions in SAGE fail or give *wrong* answers if the ring is no polynomial ring.  

Greetings,
Kilian.



---

archive/issue_comments_045013.json:
```json
{
    "body": "I would have thought that even in this generality (element of a commutative ring) it would be worth adding the following special cases:\n\n1. if self=1 return True\n2. if x =0 return True; else if self =0 return False\n3. if self.is_unit() return True\n\nwhere in each case the test is wrapped in a try/except block so that if (for example) self.is_unit() is not implemented then it just passes.  Finally, if none of the above works then default to code as it is now.\n\nAny individual ring where the x%self computation will not work but where there is an easy alternative direct test (such as in Integers(n)) can have their own specific implementations.\n   \nIf there is any support for this I'm willing to try to do it.",
    "created_at": "2009-08-18T20:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45013",
    "user": "cremona"
}
```

I would have thought that even in this generality (element of a commutative ring) it would be worth adding the following special cases:

1. if self=1 return True
2. if x =0 return True; else if self =0 return False
3. if self.is_unit() return True

where in each case the test is wrapped in a try/except block so that if (for example) self.is_unit() is not implemented then it just passes.  Finally, if none of the above works then default to code as it is now.

Any individual ring where the x%self computation will not work but where there is an easy alternative direct test (such as in Integers(n)) can have their own specific implementations.
   
If there is any support for this I'm willing to try to do it.



---

archive/issue_comments_045014.json:
```json
{
    "body": "Note that #5347 (merged in 4.1.2.alpha2) fixes the easy cases I listed above.  We still have\n\n```\nsage: Zmod(5)(1).divides(Zmod(2)(1))\nTrue\n```\n\nbut this looks fine to me:\n\n```\n\nsage: Zmod(2).zero_ideal() == Zmod(2).zero_ideal()\nTrue\nsage: Zmod(2).zero_ideal() == Zmod(2).unit_ideal()\nFalse\n```\n\n\nHence the patches here need to be rebased and simplified to cater for the first one.",
    "created_at": "2009-10-05T13:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45014",
    "user": "cremona"
}
```

Note that #5347 (merged in 4.1.2.alpha2) fixes the easy cases I listed above.  We still have

```
sage: Zmod(5)(1).divides(Zmod(2)(1))
True
```

but this looks fine to me:

```

sage: Zmod(2).zero_ideal() == Zmod(2).zero_ideal()
True
sage: Zmod(2).zero_ideal() == Zmod(2).unit_ideal()
False
```


Hence the patches here need to be rebased and simplified to cater for the first one.



---

archive/issue_comments_045015.json:
```json
{
    "body": "In fact the original patches can be discarded since they only fixed things that have been fixed anyway in #5347.  What we do not have is a check the self and other are in \"the same ring\", which is not so obvious -- the simplest would be to throw an error if the parents were not identical, but that seems to harsh (it would cause 1.divides(1/2) to fail).  Better would be to coerce into a common parent first -- the sort of thing which is done for `__add___()`.",
    "created_at": "2009-10-05T13:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45015",
    "user": "cremona"
}
```

In fact the original patches can be discarded since they only fixed things that have been fixed anyway in #5347.  What we do not have is a check the self and other are in "the same ring", which is not so obvious -- the simplest would be to throw an error if the parents were not identical, but that seems to harsh (it would cause 1.divides(1/2) to fail).  Better would be to coerce into a common parent first -- the sort of thing which is done for `__add___()`.



---

archive/issue_comments_045016.json:
```json
{
    "body": "I add a patch to solve this problem. This patch is applied alone. Previous patches are discarded due to changes in the function during these months. See #5347\n\nThe algorithm first checks if parents coincide. If so, it runs the existing code. In other case, coerces both element to a common parent using the coercion model an runs the existing code on the coerced elements.\n\nThe patch works on 4.5.3",
    "created_at": "2010-09-14T09:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45016",
    "user": "lftabera"
}
```

I add a patch to solve this problem. This patch is applied alone. Previous patches are discarded due to changes in the function during these months. See #5347

The algorithm first checks if parents coincide. If so, it runs the existing code. In other case, coerces both element to a common parent using the coercion model an runs the existing code on the coerced elements.

The patch works on 4.5.3



---

archive/issue_comments_045017.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-14T09:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45017",
    "user": "lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_045018.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-14T09:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45018",
    "user": "lftabera"
}
```

Attachment



---

archive/issue_comments_045019.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-03T15:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45019",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_045020.json:
```json
{
    "body": "The patch applies fine to 4.6.alpha1, and all test pass (I tested the whole sage library on account of earlier difficulties).  No generic function can deliver everything, but this deals with simple generic cases, as the new doctests show.",
    "created_at": "2010-10-03T15:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45020",
    "user": "cremona"
}
```

The patch applies fine to 4.6.alpha1, and all test pass (I tested the whole sage library on account of earlier difficulties).  No generic function can deliver everything, but this deals with simple generic cases, as the new doctests show.



---

archive/issue_comments_045021.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-04T02:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5759#issuecomment-45021",
    "user": "mpatel"
}
```

Resolution: fixed
