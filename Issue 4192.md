# Issue 4192: is_Blah functions: deprecate and then remove them from top level imports

archive/issues_004192.json:
```json
{
    "body": "Assignee: mhansen\n\nKeywords: imports\n\nFunctions like `is_FractionField` should not be imported at the top level, since they don't necessarily make sense mathematically, only programmatically. Thus, situations like\n\n```\nsage: is_FractionField(FractionField(ZZ))\nFalse\n```\n\nmight confuse people.  \n\nSee the discussion in #4149. I think the best solution, as propounded there by cremona and robertwb, is to have `is_Blah` *methods* which are, as much as possible, mathematically correct.  In contrast, `is_Blah` *functions* should be data-checks, existing primarily for use in the code.\n\nmhansen has volunteered to do at least some of this work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4192\n\n",
    "created_at": "2008-09-24T17:04:34Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "is_Blah functions: deprecate and then remove them from top level imports",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4192",
    "user": "jhpalmieri"
}
```
Assignee: mhansen

Keywords: imports

Functions like `is_FractionField` should not be imported at the top level, since they don't necessarily make sense mathematically, only programmatically. Thus, situations like

```
sage: is_FractionField(FractionField(ZZ))
False
```

might confuse people.  

See the discussion in #4149. I think the best solution, as propounded there by cremona and robertwb, is to have `is_Blah` *methods* which are, as much as possible, mathematically correct.  In contrast, `is_Blah` *functions* should be data-checks, existing primarily for use in the code.

mhansen has volunteered to do at least some of this work.

Issue created by migration from https://trac.sagemath.org/ticket/4192





---

archive/issue_comments_030422.json:
```json
{
    "body": "There still might be some failures due to ones that I missed, but I think I got most of them.",
    "created_at": "2008-09-26T04:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4192#issuecomment-30422",
    "user": "mhansen"
}
```

There still might be some failures due to ones that I missed, but I think I got most of them.



---

archive/issue_comments_030423.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-26T04:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4192#issuecomment-30423",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030424.json:
```json
{
    "body": "Mike,\n\nyou missed a couple (this is with -long):\n\n```\nsage -t -long devel/sage/sage/calculus/calculus.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/calculus.py\", line 5587:\n    sage: is_CallableSymbolicExpression(f)\nExpected:\n    True\nGot:\n    doctest:1: DeprecationWarning: \n    Using is_CallableSymbolicExpression from the top level is deprecated since it was designed to be used by developers rather than end users.\n    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.\n    True\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/calculus.py\", line 431:\n    sage: is_SymbolicExpression(SR(I))\nExpected:\n    True\nGot:\n    doctest:1: DeprecationWarning: \n    Using is_SymbolicExpression from the top level is deprecated since it was designed to be used by developers rather than end users.\n    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.\n    True\n**********************************************************************\n2 items had failures:\n   1 of   8 in __main__.example_159\n   1 of   9 in __main__.example_7\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_calculus.py\n```\n\nparent_old.pyx:\n\n```\nsage -t -long devel/sage/sage/structure/parent_old.pyx      \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/parent_old.py\", line 45:\n    sage: is_Parent(Primes())\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_1\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_parent_old.py\n         [3.1 s]\nexit code: 1024\n```\n\nschemes.py:\n\n```\nsage -t -long devel/sage/sage/schemes/generic/scheme.py     \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/scheme.py\", line 41:\n    sage: from sage.scheme.generic.scheme import is_Scheme\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[2]>\", line 1, in <module>\n        from sage.scheme.generic.scheme import is_Scheme###line 41:\n    sage: from sage.scheme.generic.scheme import is_Scheme\n    ImportError: No module named scheme.generic.scheme\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/scheme.py\", line 42:\n    sage: is_Scheme(5)\nExpected:\n    False\nGot:\n    doctest:1: DeprecationWarning: \n    Using is_Scheme from the top level is deprecated since it was designed to be used by developers rather than end users.\n    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.\n    False\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/scheme.py\", line 505:\n    sage: from sage.schemes.generic.schemes import is_AffineScheme\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_23[2]>\", line 1, in <module>\n        from sage.schemes.generic.schemes import is_AffineScheme###line 505:\n    sage: from sage.schemes.generic.schemes import is_AffineScheme\n    ImportError: No module named schemes\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/scheme.py\", line 506:\n    sage: is_AffineScheme(5)\nExpected:\n    False\nGot:\n    doctest:1: DeprecationWarning: \n    Using is_AffineScheme from the top level is deprecated since it was designed to be used by developers rather than end users.\n    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.\n    False\n**********************************************************************\n2 items had failures:\n   2 of   6 in __main__.example_1\n   2 of   6 in __main__.example_23\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_scheme.py\n         [11.2 s]\nexit code: 1024\n```\n\nfree_monoid.py:\n\n```\nsage -t -long devel/sage/sage/monoids/free_monoid.py        \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/free_monoid.py\", line 75:\n    sage: is_FreeMonoid(5)\nExpected:\n    False\nGot:\n    doctest:1: DeprecationWarning: \n    Using is_FreeMonoid from the top level is deprecated since it was designed to be used by developers rather than end users.\n    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.\n    False\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_free_monoid.py\n         [2.3 s]\nexit code: 1024\n```\n\nfree_ablian_monoid.py:\n\n```\nsage -t -long devel/sage/sage/monoids/free_abelian_monoid.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/free_abelian_monoid.py\", line 98:\n    sage: is_FreeAbelianMonoid(5)\nExpected:\n    False\nGot:\n    doctest:1: DeprecationWarning: \n    Using is_FreeAbelianMonoid from the top level is deprecated since it was designed to be used by developers rather than end users.\n    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.\n    False\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_free_abelian_monoid.py\n         [2.5 s]\nexit code: 1024\n```\n\nA strange on in magma.py:\n\n```\nsage -t -long devel/sage/sage/interfaces/magma.py           \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/magma.py\", line 1096:\n    sage: R.assign_names(['x'])\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_28[2]>\", line 1, in <module>\n        R.assign_names(['x'])###line 1096:\n    sage: R.assign_names(['x'])\n    AttributeError: type object 'R' has no attribute 'assign_names'\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_28\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_magma.py\n         [3.3 s]\n```\n\nhomset.py:\n\n```\nsage -t -long devel/sage/sage/categories/homset.py          \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/homset.py\", line 190:\n    sage: is_Endset(S)\nExpected:\n    True\nGot:\n    doctest:1: DeprecationWarning: \n    Using is_Endset from the top level is deprecated since it was designed to be used by developers rather than end users.\n    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.\n    True\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_3\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_homset.py\n         [2.3 s]\nexit code: 1024\n```\n\nand finally functor.pyx:\n\n```\nsage -t -long devel/sage/sage/categories/functor.pyx        \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/functor.py\", line 38:\n    sage: is_Functor(F)\nExpected:\n    True\nGot:\n    doctest:1: DeprecationWarning: \n    Using is_Functor from the top level is deprecated since it was designed to be used by developers rather than end users.\n    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.\n    True\n**********************************************************************\n1 items had failures:\n   1 of  12 in __main__.example_1\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_functor.py\n         [2.3 s]\nexit code: 1024\n```\n\nOther than that the patch looks good.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T05:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4192#issuecomment-30424",
    "user": "mabshoff"
}
```

Mike,

you missed a couple (this is with -long):

```
sage -t -long devel/sage/sage/calculus/calculus.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/calculus.py", line 5587:
    sage: is_CallableSymbolicExpression(f)
Expected:
    True
Got:
    doctest:1: DeprecationWarning: 
    Using is_CallableSymbolicExpression from the top level is deprecated since it was designed to be used by developers rather than end users.
    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.
    True
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/calculus.py", line 431:
    sage: is_SymbolicExpression(SR(I))
Expected:
    True
Got:
    doctest:1: DeprecationWarning: 
    Using is_SymbolicExpression from the top level is deprecated since it was designed to be used by developers rather than end users.
    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.
    True
**********************************************************************
2 items had failures:
   1 of   8 in __main__.example_159
   1 of   9 in __main__.example_7
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_calculus.py
```

parent_old.pyx:

```
sage -t -long devel/sage/sage/structure/parent_old.pyx      
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/parent_old.py", line 45:
    sage: is_Parent(Primes())
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_parent_old.py
         [3.1 s]
exit code: 1024
```

schemes.py:

```
sage -t -long devel/sage/sage/schemes/generic/scheme.py     
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/scheme.py", line 41:
    sage: from sage.scheme.generic.scheme import is_Scheme
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1, in <module>
        from sage.scheme.generic.scheme import is_Scheme###line 41:
    sage: from sage.scheme.generic.scheme import is_Scheme
    ImportError: No module named scheme.generic.scheme
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/scheme.py", line 42:
    sage: is_Scheme(5)
Expected:
    False
Got:
    doctest:1: DeprecationWarning: 
    Using is_Scheme from the top level is deprecated since it was designed to be used by developers rather than end users.
    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.
    False
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/scheme.py", line 505:
    sage: from sage.schemes.generic.schemes import is_AffineScheme
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_23[2]>", line 1, in <module>
        from sage.schemes.generic.schemes import is_AffineScheme###line 505:
    sage: from sage.schemes.generic.schemes import is_AffineScheme
    ImportError: No module named schemes
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/scheme.py", line 506:
    sage: is_AffineScheme(5)
Expected:
    False
Got:
    doctest:1: DeprecationWarning: 
    Using is_AffineScheme from the top level is deprecated since it was designed to be used by developers rather than end users.
    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.
    False
**********************************************************************
2 items had failures:
   2 of   6 in __main__.example_1
   2 of   6 in __main__.example_23
***Test Failed*** 4 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_scheme.py
         [11.2 s]
exit code: 1024
```

free_monoid.py:

```
sage -t -long devel/sage/sage/monoids/free_monoid.py        
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/free_monoid.py", line 75:
    sage: is_FreeMonoid(5)
Expected:
    False
Got:
    doctest:1: DeprecationWarning: 
    Using is_FreeMonoid from the top level is deprecated since it was designed to be used by developers rather than end users.
    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.
    False
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_free_monoid.py
         [2.3 s]
exit code: 1024
```

free_ablian_monoid.py:

```
sage -t -long devel/sage/sage/monoids/free_abelian_monoid.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/free_abelian_monoid.py", line 98:
    sage: is_FreeAbelianMonoid(5)
Expected:
    False
Got:
    doctest:1: DeprecationWarning: 
    Using is_FreeAbelianMonoid from the top level is deprecated since it was designed to be used by developers rather than end users.
    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.
    False
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_free_abelian_monoid.py
         [2.5 s]
exit code: 1024
```

A strange on in magma.py:

```
sage -t -long devel/sage/sage/interfaces/magma.py           
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/magma.py", line 1096:
    sage: R.assign_names(['x'])
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[2]>", line 1, in <module>
        R.assign_names(['x'])###line 1096:
    sage: R.assign_names(['x'])
    AttributeError: type object 'R' has no attribute 'assign_names'
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_28
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_magma.py
         [3.3 s]
```

homset.py:

```
sage -t -long devel/sage/sage/categories/homset.py          
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/homset.py", line 190:
    sage: is_Endset(S)
Expected:
    True
Got:
    doctest:1: DeprecationWarning: 
    Using is_Endset from the top level is deprecated since it was designed to be used by developers rather than end users.
    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.
    True
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_homset.py
         [2.3 s]
exit code: 1024
```

and finally functor.pyx:

```
sage -t -long devel/sage/sage/categories/functor.pyx        
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/functor.py", line 38:
    sage: is_Functor(F)
Expected:
    True
Got:
    doctest:1: DeprecationWarning: 
    Using is_Functor from the top level is deprecated since it was designed to be used by developers rather than end users.
    It most likely does not do what you would expect it to do.  If you really need to use it, import it from the module that it is defined in.
    True
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_functor.py
         [2.3 s]
exit code: 1024
```

Other than that the patch looks good.

Cheers,

Michael



---

archive/issue_comments_030425.json:
```json
{
    "body": "Attachment [trac_4192.patch](tarball://root/attachments/some-uuid/ticket4192/trac_4192.patch) by mhansen created at 2008-09-26 07:02:57",
    "created_at": "2008-09-26T07:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4192#issuecomment-30425",
    "user": "mhansen"
}
```

Attachment [trac_4192.patch](tarball://root/attachments/some-uuid/ticket4192/trac_4192.patch) by mhansen created at 2008-09-26 07:02:57



---

archive/issue_comments_030426.json:
```json
{
    "body": "I've updated the patch to fix those issues.",
    "created_at": "2008-09-26T07:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4192#issuecomment-30426",
    "user": "mhansen"
}
```

I've updated the patch to fix those issues.



---

archive/issue_comments_030427.json:
```json
{
    "body": "Ok, things work now. Positive review. Followup work should be directed to new tickets.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T07:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4192#issuecomment-30427",
    "user": "mabshoff"
}
```

Ok, things work now. Positive review. Followup work should be directed to new tickets.

Cheers,

Michael



---

archive/issue_comments_030428.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-26T07:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4192#issuecomment-30428",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030429.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-26T07:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4192#issuecomment-30429",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2
