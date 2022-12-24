# Issue 6925: Fast way of calculating cuspidal subgroup of J0(N)

archive/issues_006925.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  pbruin\n\nKeywords: cuspidal subgroup, modular abelian variety\n\nThis is the first implementation of Ligozat's method of calculating the rational cuspidal subgroup of J_0(N). This is done by doing linear algebra in d(N)*d(N) matrices, which seems considerably faster than the modular symbol methods.\n\nThis code is functional at this point. The problems with it are\na) __cmp__ is not called.\nb) Hecke operators aren't defined yet.\nc) can't coerce specific degree zero cuspidal divisors in our group.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6925\n\n",
    "created_at": "2009-09-11T23:49:01Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.0",
    "title": "Fast way of calculating cuspidal subgroup of J0(N)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6925",
    "user": "syazdani"
}
```
Assignee: tbd

CC:  pbruin

Keywords: cuspidal subgroup, modular abelian variety

This is the first implementation of Ligozat's method of calculating the rational cuspidal subgroup of J_0(N). This is done by doing linear algebra in d(N)*d(N) matrices, which seems considerably faster than the modular symbol methods.

This code is functional at this point. The problems with it are
a) __cmp__ is not called.
b) Hecke operators aren't defined yet.
c) can't coerce specific degree zero cuspidal divisors in our group.

Issue created by migration from https://trac.sagemath.org/ticket/6925





---

archive/issue_comments_057181.json:
```json
{
    "body": "Attachment [12846.patch](tarball://root/attachments/some-uuid/ticket6925/12846.patch) by syazdani created at 2009-09-11 23:50:12\n\nThis patch touches abvar.py and cuspidal_subgroup.py",
    "created_at": "2009-09-11T23:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57181",
    "user": "syazdani"
}
```

Attachment [12846.patch](tarball://root/attachments/some-uuid/ticket6925/12846.patch) by syazdani created at 2009-09-11 23:50:12

This patch touches abvar.py and cuspidal_subgroup.py



---

archive/issue_comments_057182.json:
```json
{
    "body": "Attachment [6925-rationalcuspidal.patch](tarball://root/attachments/some-uuid/ticket6925/6925-rationalcuspidal.patch) by syazdani created at 2009-09-17 20:14:09\n\nrebased against 5969",
    "created_at": "2009-09-17T20:14:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57182",
    "user": "syazdani"
}
```

Attachment [6925-rationalcuspidal.patch](tarball://root/attachments/some-uuid/ticket6925/6925-rationalcuspidal.patch) by syazdani created at 2009-09-17 20:14:09

rebased against 5969



---

archive/issue_comments_057183.json:
```json
{
    "body": "Changing component from algebra to modular forms.",
    "created_at": "2009-11-15T13:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57183",
    "user": "AlexGhitza"
}
```

Changing component from algebra to modular forms.



---

archive/issue_comments_057184.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-15T13:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57184",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057185.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-22T00:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57185",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_057186.json:
```json
{
    "body": "Has this been checked on Solaris? Or OS X? It's not clear what it has been tested on. \n\nThere's general information about building on Solaris at\n\n http://wiki.sagemath.org/solaris\n\nInformation specifically for 't2' at\n\n http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2\n\nBoth the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html\n\nDave",
    "created_at": "2010-02-22T00:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57186",
    "user": "drkirkby"
}
```

Has this been checked on Solaris? Or OS X? It's not clear what it has been tested on. 

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave



---

archive/issue_comments_057187.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-03-29T04:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57187",
    "user": "was"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_057188.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-06T01:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57188",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057189.json:
```json
{
    "body": "Hi Soroosh,\n\n1. Can you look into the following doctest failures (against sage-4.4.1, say, where your code applies fine)?\n\n```\n\nsage -t  devel/sage/sage/modular/abvar/cuspidal_subgroup.py\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py\", line 432:\n    sage: C._compute_lambda()\nExpected nothing\nGot:\n    [15/8 -3/8|-5/8  1/8]\n    [-3/8 15/8| 1/8 -5/8]\n    [---------+---------]\n    [-5/8  1/8|15/8 -3/8]\n    [ 1/8 -5/8|-3/8 15/8]\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py\", line 442:\n    sage: C._compute_lambda()\nExpected nothing\nGot:\n    [    1  -1/5     0]\n    [ -1/4 13/10  -1/4]\n    [    0  -1/5     1]\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py\", line 475:\n    sage: C._compute_P_d_integral()\nExpected nothing\nGot:\n    Free module of degree 3 and rank 3 over Integer Ring\n    Echelon basis matrix:\n    [1 0 0]\n    [0 4 0]\n    [0 0 1]\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py\", line 498:\n    sage: C._compute_parity_module()\nExpected nothing\nGot:\n    Free module of degree 3 and rank 3 over Integer Ring\n    Echelon basis matrix:\n    [1 0 0]\n    [0 2 0]\n    [0 0 1]\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py\", line 508:\n    sage: C._compute_parity_module()\nExpected nothing\nGot:\n    Free module of degree 4 and rank 4 over Integer Ring\n    Echelon basis matrix:\n    [1 0 0 0]\n    [0 1 1 1]\n    [0 0 2 0]\n    [0 0 0 2]\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py\", line 547:\n    sage: C.V0()\nExpected nothing\nGot:\n    Free module of degree 4 and rank 3 over Integer Ring\n    Echelon basis matrix:\n    [ 1  0  0 -1]\n    [ 0  1  0 -1]\n    [ 0  0  1 -1]\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py\", line 557:\n    sage: C.V0()\nExpected nothing\nGot:\n    Free module of degree 3 and rank 2 over Integer Ring\n    Echelon basis matrix:\n    [ 1  0 -1]\n    [ 0  4 -4]\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py\", line 590:\n    sage: C.Vprincipal()\nExpected nothing\nGot:\n    Free module of degree 3 and rank 2 over Integer Ring\n    Echelon basis matrix:\n    [ 1  0 -1]\n    [ 0  4 -4]\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py\", line 599:\n    sage: C.Vprincipal()\nExpected nothing\nGot:\n    Free module of degree 4 and rank 3 over Integer Ring\n    Echelon basis matrix:\n    [ 1  1  3 -5]\n    [ 0  2  0 -2]\n    [ 0  0  4 -4]\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py\", line 654:\n    sage: C.gens()\nExpected:\n    [-P15+P5, -P15+P3]\nGot:\n    [-P15 + P5, -P15 + P3]\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py\", line 703:\n    sage: C.0\nExpected:\n    [-P15 + P5, -P15 + P3]\n    sgae: (C.0).additive_order()\n    2\nGot:\n    -P15 + P5\n**********************************************************************\n7 items had failures:\n   2 of   8 in __main__.example_13\n   1 of   5 in __main__.example_14\n   2 of   8 in __main__.example_15\n   2 of   8 in __main__.example_16\n   2 of   8 in __main__.example_17\n   1 of   5 in __main__.example_19\n   1 of   5 in __main__.example_22\n***Test Failed*** 11 failures.\nFor whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_cuspidal_subgroup.py\n         [6.4 s]\n\n```\n\n\n2. Everwhere that you have\n\n```\nExamples::  \n    sage:\n```\n\nchange it to\n\n\n```\nEXAMPLES::  \n\n    sage:\n```\n\n(note the newline)\n\n3. Everywhere you have -'d lists, e.g.,\n\n```\n        691\t        - `` parent`` - a subgroup of the cuspidal subgroup of  \n \t692\t        J0(N) \n \t693\t \n \t694\t        - ``element`` - an element in the quotient module of degree zero divisors of cusps \n \t695\t        modulo principal divisors. \n \t696\t \n \t697\t        - ``check`` - bool (default: False) whether to check \n \t698\t        that element is in the appropriate module \n```\n\nchange them so the second line (etc.) starts exactly two spaces in from the dash so it lines up with the previous line's text, e.g., \n\n```\n        691\t        - `` parent`` - a subgroup of the cuspidal subgroup of  \n \t692\t          J0(N) \n \t693\t \n \t694\t        - ``element`` - an element in the quotient module of degree zero divisors of cusps \n \t695\t          modulo principal divisors. \n }}}\n\n4. Can you be more careful that the docstrings match what they are documenting, e.g., \n{{{\n764\t    def _sub_(self, other): \n \t765\t        r\"\"\" \n \t766\t        Adds two elements in the cuspidal subgroup. \n}}}\nIt should be \"Subtract\" not add. \n\n5. \n{{{\n        827\t    def __cmp__(self, other): \n \t828\t        r\"\"\" \n \t829\t        Checks if two elements are the same. Right now this is not called, and I'm not sure why. \n}}}\n\nYou probably need to use/call __richmp__ instead...  there is some funny rule that if you define __cmp__ you have to also define __hash__ or something. Search sage-devel about this. \n\n7. Change this\n{{{\n        495\t        TESTS: \n \t496\t            sage: J=J0(25) \n}}}\nto\n{{{\n        495\t        TESTS::\n        496\n \t497\t            sage: J=J0(25) \n}}}\n\n8. I'm not sure about the name \"RationalDirectCuspidalSubgroup\".  Maybe \"RationalCuspidalSubgroupLigozat\" or something, i.e., use \"Ligozat\" instead of direct?",
    "created_at": "2010-05-06T01:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57189",
    "user": "was"
}
```

Hi Soroosh,

1. Can you look into the following doctest failures (against sage-4.4.1, say, where your code applies fine)?

```

sage -t  devel/sage/sage/modular/abvar/cuspidal_subgroup.py
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 432:
    sage: C._compute_lambda()
Expected nothing
Got:
    [15/8 -3/8|-5/8  1/8]
    [-3/8 15/8| 1/8 -5/8]
    [---------+---------]
    [-5/8  1/8|15/8 -3/8]
    [ 1/8 -5/8|-3/8 15/8]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 442:
    sage: C._compute_lambda()
Expected nothing
Got:
    [    1  -1/5     0]
    [ -1/4 13/10  -1/4]
    [    0  -1/5     1]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 475:
    sage: C._compute_P_d_integral()
Expected nothing
Got:
    Free module of degree 3 and rank 3 over Integer Ring
    Echelon basis matrix:
    [1 0 0]
    [0 4 0]
    [0 0 1]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 498:
    sage: C._compute_parity_module()
Expected nothing
Got:
    Free module of degree 3 and rank 3 over Integer Ring
    Echelon basis matrix:
    [1 0 0]
    [0 2 0]
    [0 0 1]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 508:
    sage: C._compute_parity_module()
Expected nothing
Got:
    Free module of degree 4 and rank 4 over Integer Ring
    Echelon basis matrix:
    [1 0 0 0]
    [0 1 1 1]
    [0 0 2 0]
    [0 0 0 2]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 547:
    sage: C.V0()
Expected nothing
Got:
    Free module of degree 4 and rank 3 over Integer Ring
    Echelon basis matrix:
    [ 1  0  0 -1]
    [ 0  1  0 -1]
    [ 0  0  1 -1]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 557:
    sage: C.V0()
Expected nothing
Got:
    Free module of degree 3 and rank 2 over Integer Ring
    Echelon basis matrix:
    [ 1  0 -1]
    [ 0  4 -4]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 590:
    sage: C.Vprincipal()
Expected nothing
Got:
    Free module of degree 3 and rank 2 over Integer Ring
    Echelon basis matrix:
    [ 1  0 -1]
    [ 0  4 -4]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 599:
    sage: C.Vprincipal()
Expected nothing
Got:
    Free module of degree 4 and rank 3 over Integer Ring
    Echelon basis matrix:
    [ 1  1  3 -5]
    [ 0  2  0 -2]
    [ 0  0  4 -4]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 654:
    sage: C.gens()
Expected:
    [-P15+P5, -P15+P3]
Got:
    [-P15 + P5, -P15 + P3]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 703:
    sage: C.0
Expected:
    [-P15 + P5, -P15 + P3]
    sgae: (C.0).additive_order()
    2
Got:
    -P15 + P5
**********************************************************************
7 items had failures:
   2 of   8 in __main__.example_13
   1 of   5 in __main__.example_14
   2 of   8 in __main__.example_15
   2 of   8 in __main__.example_16
   2 of   8 in __main__.example_17
   1 of   5 in __main__.example_19
   1 of   5 in __main__.example_22
***Test Failed*** 11 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_cuspidal_subgroup.py
         [6.4 s]

```


2. Everwhere that you have

```
Examples::  
    sage:
```

change it to


```
EXAMPLES::  

    sage:
```

(note the newline)

3. Everywhere you have -'d lists, e.g.,

```
        691	        - `` parent`` - a subgroup of the cuspidal subgroup of  
 	692	        J0(N) 
 	693	 
 	694	        - ``element`` - an element in the quotient module of degree zero divisors of cusps 
 	695	        modulo principal divisors. 
 	696	 
 	697	        - ``check`` - bool (default: False) whether to check 
 	698	        that element is in the appropriate module 
```

change them so the second line (etc.) starts exactly two spaces in from the dash so it lines up with the previous line's text, e.g., 

```
        691	        - `` parent`` - a subgroup of the cuspidal subgroup of  
 	692	          J0(N) 
 	693	 
 	694	        - ``element`` - an element in the quotient module of degree zero divisors of cusps 
 	695	          modulo principal divisors. 
 }}}

4. Can you be more careful that the docstrings match what they are documenting, e.g., 
{{{
764	    def _sub_(self, other): 
 	765	        r""" 
 	766	        Adds two elements in the cuspidal subgroup. 
}}}
It should be "Subtract" not add. 

5. 
{{{
        827	    def __cmp__(self, other): 
 	828	        r""" 
 	829	        Checks if two elements are the same. Right now this is not called, and I'm not sure why. 
}}}

You probably need to use/call __richmp__ instead...  there is some funny rule that if you define __cmp__ you have to also define __hash__ or something. Search sage-devel about this. 

7. Change this
{{{
        495	        TESTS: 
 	496	            sage: J=J0(25) 
}}}
to
{{{
        495	        TESTS::
        496
 	497	            sage: J=J0(25) 
}}}

8. I'm not sure about the name "RationalDirectCuspidalSubgroup".  Maybe "RationalCuspidalSubgroupLigozat" or something, i.e., use "Ligozat" instead of direct?



---

archive/issue_comments_057190.json:
```json
{
    "body": "for the bot:\n\napply 6925-rationalcuspidal.patch\u200b",
    "created_at": "2013-08-02T07:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57190",
    "user": "chapoton"
}
```

for the bot:

apply 6925-rationalcuspidal.patch​



---

archive/issue_comments_057191.json:
```json
{
    "body": "apply only 6925-rationalcuspidal.patch",
    "created_at": "2013-08-02T07:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57191",
    "user": "chapoton"
}
```

apply only 6925-rationalcuspidal.patch



---

archive/issue_comments_057192.json:
```json
{
    "body": "here is a first cleanup patch.\n\nThere is one failing doctest that needs a mathematical check.",
    "created_at": "2013-08-02T08:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57192",
    "user": "chapoton"
}
```

here is a first cleanup patch.

There is one failing doctest that needs a mathematical check.



---

archive/issue_comments_057193.json:
```json
{
    "body": "Could please someone with the required math knowledge check the unique failing doctest (see patchbot report by clicking on the round icon at the top of the page) ?",
    "created_at": "2013-10-04T08:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57193",
    "user": "chapoton"
}
```

Could please someone with the required math knowledge check the unique failing doctest (see patchbot report by clicking on the round icon at the top of the page) ?



---

archive/issue_comments_057194.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-10-04T19:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57194",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057195.json:
```json
{
    "body": "I have replaced the failing test, without checking the mathematical side..\n\nI have also added a reference to Ligozat, hopefully the correct one ?\n\nThis should now pass all tests.",
    "created_at": "2013-10-04T19:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57195",
    "user": "chapoton"
}
```

I have replaced the failing test, without checking the mathematical side..

I have also added a reference to Ligozat, hopefully the correct one ?

This should now pass all tests.



---

archive/issue_comments_057196.json:
```json
{
    "body": "updated patch, to ensure 100% doctest coverage",
    "created_at": "2013-10-05T09:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57196",
    "user": "chapoton"
}
```

updated patch, to ensure 100% doctest coverage



---

archive/issue_comments_057197.json:
```json
{
    "body": "changed the name to rational_cuspidal_subgroup_ligozat, and few other changes.",
    "created_at": "2013-10-07T05:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57197",
    "user": "syazdani"
}
```

changed the name to rational_cuspidal_subgroup_ligozat, and few other changes.



---

archive/issue_comments_057198.json:
```json
{
    "body": "Attachment [trac_6925_addon2.patch](tarball://root/attachments/some-uuid/ticket6925/trac_6925_addon2.patch) by syazdani created at 2013-10-07 05:55:00\n\nChapoton's fix was correct. The initial doctest was incorrect.\n\nAlso, that is the correct Ligozat reference. I added the reference to my paper as well, which is what the algorithm is based upon.\n\nI changed the name of rational_direct_cuspidal_subgroup to rational_cuspidal_subgroup_ligozat, as it was suggested, and replaced cmp function with eq and ne functions instead.\n\nFinally, sorry for being MIA on this ticket for so long. I think I had an incorrect filter archiving these emails automatically.",
    "created_at": "2013-10-07T05:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57198",
    "user": "syazdani"
}
```

Attachment [trac_6925_addon2.patch](tarball://root/attachments/some-uuid/ticket6925/trac_6925_addon2.patch) by syazdani created at 2013-10-07 05:55:00

Chapoton's fix was correct. The initial doctest was incorrect.

Also, that is the correct Ligozat reference. I added the reference to my paper as well, which is what the algorithm is based upon.

I changed the name of rational_direct_cuspidal_subgroup to rational_cuspidal_subgroup_ligozat, as it was suggested, and replaced cmp function with eq and ne functions instead.

Finally, sorry for being MIA on this ticket for so long. I think I had an incorrect filter archiving these emails automatically.



---

archive/issue_comments_057199.json:
```json
{
    "body": "the addon2 patch does not apply",
    "created_at": "2013-10-13T11:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57199",
    "user": "chapoton"
}
```

the addon2 patch does not apply



---

archive/issue_comments_057200.json:
```json
{
    "body": "hmm... are the patches supposed to be made from a clean build, or from the previous build? I applied your patches, and then used hg_sage.export. So, three patches need to be applied in order. That might not be the correct approach though.",
    "created_at": "2013-10-13T15:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57200",
    "user": "syazdani"
}
```

hmm... are the patches supposed to be made from a clean build, or from the previous build? I applied your patches, and then used hg_sage.export. So, three patches need to be applied in order. That might not be the correct approach though.



---

archive/issue_comments_057201.json:
```json
{
    "body": "Hello,\n\nit seems that your patch was twice the same thing. Anyway, I have folded it into a new version of trac_6925_addon1.patch\n\napply 6925-rationalcuspidal.patch trac_6925_addon1.patch",
    "created_at": "2013-10-17T19:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57201",
    "user": "chapoton"
}
```

Hello,

it seems that your patch was twice the same thing. Anyway, I have folded it into a new version of trac_6925_addon1.patch

apply 6925-rationalcuspidal.patch trac_6925_addon1.patch



---

archive/issue_comments_057202.json:
```json
{
    "body": "Attachment [trac_6925_addon1.patch](tarball://root/attachments/some-uuid/ticket6925/trac_6925_addon1.patch) by chapoton created at 2013-10-23 19:13:31\n\nnew patch, minor details changed, should now pass the tests",
    "created_at": "2013-10-23T19:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57202",
    "user": "chapoton"
}
```

Attachment [trac_6925_addon1.patch](tarball://root/attachments/some-uuid/ticket6925/trac_6925_addon1.patch) by chapoton created at 2013-10-23 19:13:31

new patch, minor details changed, should now pass the tests



---

archive/issue_comments_057203.json:
```json
{
    "body": "Attachment [trac-6925-rationalcuspidal-rebased-v1.patch](tarball://root/attachments/some-uuid/ticket6925/trac-6925-rationalcuspidal-rebased-v1.patch) by chapoton created at 2013-10-25 18:00:00",
    "created_at": "2013-10-25T18:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57203",
    "user": "chapoton"
}
```

Attachment [trac-6925-rationalcuspidal-rebased-v1.patch](tarball://root/attachments/some-uuid/ticket6925/trac-6925-rationalcuspidal-rebased-v1.patch) by chapoton created at 2013-10-25 18:00:00



---

archive/issue_comments_057204.json:
```json
{
    "body": "new patch, folded and rebased on 5.13.beta1\n\nfor the **patchbots**\n\napply trac-6925-rationalcuspidal-rebased-v1.patch",
    "created_at": "2013-10-25T18:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57204",
    "user": "chapoton"
}
```

new patch, folded and rebased on 5.13.beta1

for the **patchbots**

apply trac-6925-rationalcuspidal-rebased-v1.patch



---

archive/issue_comments_057205.json:
```json
{
    "body": "New commits:",
    "created_at": "2013-12-02T21:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57205",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_057206.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-01-03T21:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57206",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_057207.json:
```json
{
    "body": "resolved merge conflicts",
    "created_at": "2014-04-26T14:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57207",
    "user": "pbruin"
}
```

resolved merge conflicts



---

archive/issue_comments_057208.json:
```json
{
    "body": "All tests pass, but I can't look at this in detail now.",
    "created_at": "2014-04-26T14:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57208",
    "user": "pbruin"
}
```

All tests pass, but I can't look at this in detail now.



---

archive/issue_comments_057209.json:
```json
{
    "body": "patchbot failed with coverage:\n\n```\ntests/cmdline.py: 100.0% (1 of 1)\ntests/\nTraceback (most recent call last):\n  File \"/home/ralf/sage/local/bin/patchbot/patchbot.py\", line 468, in test_a_ti\ncket\n    res = plugin(ticket, is_git=True, baseline=baseline, **kwds)\n  File \"/home/ralf/git/sage-patchbot/src/plugins.py\", line 152, in doctest_cont\ninuation\n    exclude_new(ticket, regex=r'^\\s*\\.\\.\\.\\s', msg=\"Old-style doctest continuat\nion\", **kwds)\n  File \"/home/ralf/git/sage-patchbot/src/plugins.py\", line 143, in exclude_new\n    raise ValueError(full_msg)\nValueError: Old-style doctest continuation inserted on 2 non-empty lines\n```\n\nbut this may be spurious because nothing in `tests/` is changed...",
    "created_at": "2014-05-07T09:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57209",
    "user": "rws"
}
```

patchbot failed with coverage:

```
tests/cmdline.py: 100.0% (1 of 1)
tests/
Traceback (most recent call last):
  File "/home/ralf/sage/local/bin/patchbot/patchbot.py", line 468, in test_a_ti
cket
    res = plugin(ticket, is_git=True, baseline=baseline, **kwds)
  File "/home/ralf/git/sage-patchbot/src/plugins.py", line 152, in doctest_cont
inuation
    exclude_new(ticket, regex=r'^\s*\.\.\.\s', msg="Old-style doctest continuat
ion", **kwds)
  File "/home/ralf/git/sage-patchbot/src/plugins.py", line 143, in exclude_new
    raise ValueError(full_msg)
ValueError: Old-style doctest continuation inserted on 2 non-empty lines
```

but this may be spurious because nothing in `tests/` is changed...



---

archive/issue_comments_057210.json:
```json
{
    "body": "Replying to [comment:29 rws]:\n> patchbot failed\nThe failed plugin is `non_ascii`, because of the French accents in the author and journal of Ligozat's article.  We can ignore this, since the file has a `coding: utf-8` declaration in its first line.",
    "created_at": "2014-05-07T16:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57210",
    "user": "pbruin"
}
```

Replying to [comment:29 rws]:
> patchbot failed
The failed plugin is `non_ascii`, because of the French accents in the author and journal of Ligozat's article.  We can ignore this, since the file has a `coding: utf-8` declaration in its first line.



---

archive/issue_comments_057211.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-27T06:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57211",
    "user": "rws"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057212.json:
```json
{
    "body": "\n```\n+++ b/src/sage/modular/abvar/cuspidal_subgroup.py\n\n@@ -371,6 +378,538 @@ def is_rational_cusp_gamma0(c, N, data):\n\n+    .. [Ligo] G\u00c3\u00a9rard Ligozat, Courbes modulaires de genre 1.\n+       M\u00c3\u00a9moires de la Soci\u00c3\u00a9t\u00c3\u00a9 Math\u00c3\u00a9matique de France, 43 (1975), p. 5-80,\n\nNon-ascii characters inserted on 2 non-empty linesmultiple lines, ''no wiki''\n      white space respected\n```\n",
    "created_at": "2014-05-27T06:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57212",
    "user": "rws"
}
```


```
+++ b/src/sage/modular/abvar/cuspidal_subgroup.py

@@ -371,6 +378,538 @@ def is_rational_cusp_gamma0(c, N, data):

+    .. [Ligo] GÃ©rard Ligozat, Courbes modulaires de genre 1.
+       MÃ©moires de la SociÃ©tÃ© MathÃ©matique de France, 43 (1975), p. 5-80,

Non-ascii characters inserted on 2 non-empty linesmultiple lines, ''no wiki''
      white space respected
```




---

archive/issue_comments_057213.json:
```json
{
    "body": "What do you mean by `needs work` ? Unicode characters are ok as soon as the utf8 encoding is specified at top of the file, which is the case here. Is there anything that really needs to be corrected ???",
    "created_at": "2014-05-27T07:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57213",
    "user": "chapoton"
}
```

What do you mean by `needs work` ? Unicode characters are ok as soon as the utf8 encoding is specified at top of the file, which is the case here. Is there anything that really needs to be corrected ???



---

archive/issue_comments_057214.json:
```json
{
    "body": "I usually trust what patchbot is outputting but, as this and the other patchbot bugs show, I should be more careful. Thanks.",
    "created_at": "2014-05-27T08:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57214",
    "user": "rws"
}
```

I usually trust what patchbot is outputting but, as this and the other patchbot bugs show, I should be more careful. Thanks.



---

archive/issue_comments_057215.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-05-27T08:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57215",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057216.json:
```json
{
    "body": "I have correct the failing repr. Now there are failing doctests.\n----\nNew commits:",
    "created_at": "2015-02-16T10:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57216",
    "user": "chapoton"
}
```

I have correct the failing repr. Now there are failing doctests.
----
New commits:



---

archive/issue_comments_057217.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-02-16T10:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57217",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057218.json:
```json
{
    "body": "could someone knowledgeable about the subject have a look at the failing doctests ?",
    "created_at": "2015-04-17T18:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57218",
    "user": "chapoton"
}
```

could someone knowledgeable about the subject have a look at the failing doctests ?



---

archive/issue_comments_057219.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-14T09:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57219",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_057220.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2015-07-17T11:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57220",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_057221.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-21T20:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57221",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_057222.json:
```json
{
    "body": "***ping*** ?",
    "created_at": "2016-01-21T20:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57222",
    "user": "chapoton"
}
```

***ping*** ?



---

archive/issue_comments_057223.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-29T18:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57223",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_057224.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-04-17T08:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57224",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_057225.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2017-04-17T08:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57225",
    "user": "chapoton"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_057226.json:
```json
{
    "body": "Do `RationalCuspidalSubgroupLigozat` and `RationalCuspSubgroup` provide the same features? Apparently it does\n\n```\nsage: X.rational_cuspidal_subgroup_ligozat()\nFinite subgroup with invariants (2, 4) over QQ of Abelian variety J0(15) of dimension 1\nsage: X.rational_cuspidal_subgroup()\nFinite subgroup with invariants [2, 4] over QQ of Abelian variety J0(15) of dimension 1\n```\n\nIt would be much better to provide an optional argument to `rational_cuspidal_subgroup` rather than having a distinct method. This branch provides (important) implementation details but nothing mathematically relevant. Moreover, inheritance choices should be more clearly explained.\n\nThe function names `_compute_XXX` make no sense. Should just be `_XXX`.",
    "created_at": "2017-07-13T18:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57226",
    "user": "vdelecroix"
}
```

Do `RationalCuspidalSubgroupLigozat` and `RationalCuspSubgroup` provide the same features? Apparently it does

```
sage: X.rational_cuspidal_subgroup_ligozat()
Finite subgroup with invariants (2, 4) over QQ of Abelian variety J0(15) of dimension 1
sage: X.rational_cuspidal_subgroup()
Finite subgroup with invariants [2, 4] over QQ of Abelian variety J0(15) of dimension 1
```

It would be much better to provide an optional argument to `rational_cuspidal_subgroup` rather than having a distinct method. This branch provides (important) implementation details but nothing mathematically relevant. Moreover, inheritance choices should be more clearly explained.

The function names `_compute_XXX` make no sense. Should just be `_XXX`.



---

archive/issue_comments_057227.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-07-13T18:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57227",
    "user": "vdelecroix"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057228.json:
```json
{
    "body": "They don't provide the same features so I think they should stay separate. For instance,\n\n```\nsage: J = J0(15)\nsage: G = J.rational_cuspidal_subgroup()\nsage: H = J.rational_cuspidal_subgroup_ligozat()\nsage: G.intersection(J)\nFinite subgroup with invariants [2, 4] over QQ of Abelian variety J0(15) of dimension 1\nsage: H.intersection(J)\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n<ipython-input-16-7e6428c7da6a> in <module>()\n----> 1 H.intersection(J)\n \n/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in intersection(self, other)\n    399             K = coercion_model.common_parent(self.field_of_definition(), other.field_of_definition())\n    400\n--> 401         L = self.lattice()\n    402         if A != B:\n    403             # TODO: This might be way slower than what we could do if\n \n/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in lattice(self)\n    182             [   0    3   -2   -1    2    0]\n    183         \"\"\"\n--> 184         raise NotImplementedError\n    185\n    186     def _relative_basis_matrix(self):\n \nNotImplementedError:\n```\n\n\n```\nsage: G == G\nTrue\nsage: H == H\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n<ipython-input-18-bc37629c2b89> in <module>()\n----> 1 H == H\n \n/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in __cmp__(self, other)\n    253         L = A.lattice() + B.lattice()\n    254         # Minus sign because order gets reversed in passing to lattices.\n--> 255         return -cmp(self.lattice() + L, other.lattice() + L)\n    256\n    257     def is_subgroup(self, other):\n \n/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in lattice(self)\n    182             [   0    3   -2   -1    2    0]\n    183         \"\"\"\n--> 184         raise NotImplementedError\n    185\n    186     def _relative_basis_matrix(self):\n \nNotImplementedError:\n```\n",
    "created_at": "2017-07-20T00:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57228",
    "user": "klui"
}
```

They don't provide the same features so I think they should stay separate. For instance,

```
sage: J = J0(15)
sage: G = J.rational_cuspidal_subgroup()
sage: H = J.rational_cuspidal_subgroup_ligozat()
sage: G.intersection(J)
Finite subgroup with invariants [2, 4] over QQ of Abelian variety J0(15) of dimension 1
sage: H.intersection(J)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-16-7e6428c7da6a> in <module>()
----> 1 H.intersection(J)
 
/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in intersection(self, other)
    399             K = coercion_model.common_parent(self.field_of_definition(), other.field_of_definition())
    400
--> 401         L = self.lattice()
    402         if A != B:
    403             # TODO: This might be way slower than what we could do if
 
/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in lattice(self)
    182             [   0    3   -2   -1    2    0]
    183         """
--> 184         raise NotImplementedError
    185
    186     def _relative_basis_matrix(self):
 
NotImplementedError:
```


```
sage: G == G
True
sage: H == H
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-18-bc37629c2b89> in <module>()
----> 1 H == H
 
/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in __cmp__(self, other)
    253         L = A.lattice() + B.lattice()
    254         # Minus sign because order gets reversed in passing to lattices.
--> 255         return -cmp(self.lattice() + L, other.lattice() + L)
    256
    257     def is_subgroup(self, other):
 
/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in lattice(self)
    182             [   0    3   -2   -1    2    0]
    183         """
--> 184         raise NotImplementedError
    185
    186     def _relative_basis_matrix(self):
 
NotImplementedError:
```




---

archive/issue_comments_057229.json:
```json
{
    "body": "Replying to [comment:49 klui]:\n> They don't provide the same features so I think they should stay separate. For instance,\n\nThat was not my question. Do they represent the same mathematical object? The fact that some methods are not implemented is a minor difference.",
    "created_at": "2017-07-20T08:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57229",
    "user": "vdelecroix"
}
```

Replying to [comment:49 klui]:
> They don't provide the same features so I think they should stay separate. For instance,

That was not my question. Do they represent the same mathematical object? The fact that some methods are not implemented is a minor difference.



---

archive/issue_comments_057230.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-07-20T16:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57230",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_057231.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-07-20T16:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57231",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_057232.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-05-01T14:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57232",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_057233.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-06-27T06:10:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6925#issuecomment-57233",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:
