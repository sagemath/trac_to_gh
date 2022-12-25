# Issue 8173: segfault in singular resultant

archive/issues_008173.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  polybori\n\nKeywords: singular\n\nOn 4.3.2.alpha2:\n\n\n```\nsage: R.<x,y,a,b,u>=PolynomialRing(ZZ, 5)\nsage: r = (x^4*y^2+x^2*y-y).resultant(x*y-y*a-x*b+a*b+u,x)\n\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread 0xb7d8b8c0 (LWP 28007)]\n0xb72844c5 in __gmpn_copyi ()\n   from /scratch/berocal/sage/i686/sage-4.3.rc0/local/lib/libgmp.so.3\nCurrent language:  auto; currently asm\n(gdb) bt\n#0  0xb72844c5 in __gmpn_copyi ()\n   from /scratch/berocal/sage/i686/sage-4.3.rc0/local/lib/libgmp.so.3\n#1  0xb72647f2 in __gmpz_init_set ()\n   from /scratch/berocal/sage/i686/sage-4.3.rc0/local/lib/libgmp.so.3\n#2  0x00000005 in ?? ()\n#3  0xbfe225b8 in ?? ()\n#4  0xbfe225f8 in ?? ()\n#5  0xb3d7fcb5 in conv_SingPFactoryP (p=0xb3efa4a0, r=0xb3db7980)\n    at clapconv.cc:143\nBacktrace stopped: previous frame inner to this frame (corrupt stack?)\n```\n\n\nSage calls `singclap_resultant()`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8173\n\n",
    "created_at": "2010-02-03T13:40:53Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "segfault in singular resultant",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8173",
    "user": "https://github.com/burcin"
}
```
Assignee: @malb

CC:  polybori

Keywords: singular

On 4.3.2.alpha2:


```
sage: R.<x,y,a,b,u>=PolynomialRing(ZZ, 5)
sage: r = (x^4*y^2+x^2*y-y).resultant(x*y-y*a-x*b+a*b+u,x)

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0xb7d8b8c0 (LWP 28007)]
0xb72844c5 in __gmpn_copyi ()
   from /scratch/berocal/sage/i686/sage-4.3.rc0/local/lib/libgmp.so.3
Current language:  auto; currently asm
(gdb) bt
#0  0xb72844c5 in __gmpn_copyi ()
   from /scratch/berocal/sage/i686/sage-4.3.rc0/local/lib/libgmp.so.3
#1  0xb72647f2 in __gmpz_init_set ()
   from /scratch/berocal/sage/i686/sage-4.3.rc0/local/lib/libgmp.so.3
#2  0x00000005 in ?? ()
#3  0xbfe225b8 in ?? ()
#4  0xbfe225f8 in ?? ()
#5  0xb3d7fcb5 in conv_SingPFactoryP (p=0xb3efa4a0, r=0xb3db7980)
    at clapconv.cc:143
Backtrace stopped: previous frame inner to this frame (corrupt stack?)
```


Sage calls `singclap_resultant()`.

Issue created by migration from https://trac.sagemath.org/ticket/8173





---

archive/issue_comments_071872.json:
```json
{
    "body": "This works:\n\n\n```\nsage: R.<x,y,a,b,u>=PolynomialRing(QQ, 5)  \nsage: (x^4*y^2+x^2*y-y).resultant(x*y-y*a-x*b+a*b+u,x)\ny^6*a^4 - 4*y^5*a^4*b + 6*y^4*a^4*b^2 - 4*y^3*a^4*b^3 + y^2*a^4*b^4 - 4*y^5*a^3*u + 12*y^4*a^3*b*u - 12*y^3*a^3*b^2*u + 4*y^2*a^3*b^3*u + 6*y^4*a^2*u^2 - 12*y^3*a^2*b*u^2 + 6*y^2*a^2*b^2*u^2 + y^5*a^2 - 4*y^4*a^2*b + 6*y^3*a^2*b^2 - 4*y^2*a^2*b^3 + y*a^2*b^4 - 4*y^3*a*u^3 + 4*y^2*a*b*u^3 - 2*y^4*a*u + 6*y^3*a*b*u - 6*y^2*a*b^2*u + 2*y*a*b^3*u + y^2*u^4 - y^5 + 4*y^4*b - 6*y^3*b^2 + 4*y^2*b^3 - y*b^4 + y^3*u^2 - 2*y^2*b*u^2 + y*b^2*u^2\n```\n",
    "created_at": "2010-02-03T14:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71872",
    "user": "https://github.com/burcin"
}
```

This works:


```
sage: R.<x,y,a,b,u>=PolynomialRing(QQ, 5)  
sage: (x^4*y^2+x^2*y-y).resultant(x*y-y*a-x*b+a*b+u,x)
y^6*a^4 - 4*y^5*a^4*b + 6*y^4*a^4*b^2 - 4*y^3*a^4*b^3 + y^2*a^4*b^4 - 4*y^5*a^3*u + 12*y^4*a^3*b*u - 12*y^3*a^3*b^2*u + 4*y^2*a^3*b^3*u + 6*y^4*a^2*u^2 - 12*y^3*a^2*b*u^2 + 6*y^2*a^2*b^2*u^2 + y^5*a^2 - 4*y^4*a^2*b + 6*y^3*a^2*b^2 - 4*y^2*a^2*b^3 + y*a^2*b^4 - 4*y^3*a*u^3 + 4*y^2*a*b*u^3 - 2*y^4*a*u + 6*y^3*a*b*u - 6*y^2*a*b^2*u + 2*y*a*b^3*u + y^2*u^4 - y^5 + 4*y^4*b - 6*y^3*b^2 + 4*y^2*b^3 - y*b^4 + y^3*u^2 - 2*y^2*b*u^2 + y*b^2*u^2
```




---

archive/issue_comments_071873.json:
```json
{
    "body": "In Singular:\n\n\n```\n> ring r = integer,(x,y,a,b,u),dp;\n> poly f = x^4*y^2+x^2*y-y;\n> resultant(f,x*y-y*a-x*b+a*b+u,x);\n   ? not implemented\n```\n\n\nvs.\n\n\n```\n> ring r = 0,(x,y,a,b,u),dp;\n> poly f = x^4*y^2+x^2*y-y;\n> resultant(f,x*y-y*a-x*b+a*b+u,x);\ny6a4-4y5a4b+6y4a4b2-4y3a4b3+y2a4b4-4y5a3u+12y4a3bu-12y3a3b2u+4y2a3b3u+6y4a2u2-12y3a2bu2+6y2a2b2u2+y5a2-4y4a2b+6y3a2b2-4y2a2b3+ya2b4-4y3au3+4y2abu3-2y4au+6y3abu-6y2ab2u+2yab3u+y2u4-y5+4y4b-6y3b2+4y2b3-yb4+y3u2-2y2bu2+yb2u2\n```\n\n\nSo shall we lift to QQ, compute the resultant and then convert back?",
    "created_at": "2010-02-03T14:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71873",
    "user": "https://github.com/malb"
}
```

In Singular:


```
> ring r = integer,(x,y,a,b,u),dp;
> poly f = x^4*y^2+x^2*y-y;
> resultant(f,x*y-y*a-x*b+a*b+u,x);
   ? not implemented
```


vs.


```
> ring r = 0,(x,y,a,b,u),dp;
> poly f = x^4*y^2+x^2*y-y;
> resultant(f,x*y-y*a-x*b+a*b+u,x);
y6a4-4y5a4b+6y4a4b2-4y3a4b3+y2a4b4-4y5a3u+12y4a3bu-12y3a3b2u+4y2a3b3u+6y4a2u2-12y3a2bu2+6y2a2b2u2+y5a2-4y4a2b+6y3a2b2-4y2a2b3+ya2b4-4y3au3+4y2abu3-2y4au+6y3abu-6y2ab2u+2yab3u+y2u4-y5+4y4b-6y3b2+4y2b3-yb4+y3u2-2y2bu2+yb2u2
```


So shall we lift to QQ, compute the resultant and then convert back?



---

archive/issue_comments_071874.json:
```json
{
    "body": "> So shall we lift to QQ, compute the resultant and then convert back?\nsounds reasonable.",
    "created_at": "2010-02-03T14:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71874",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

> So shall we lift to QQ, compute the resultant and then convert back?
sounds reasonable.



---

archive/issue_comments_071875.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-09T20:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71875",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071876.json:
```json
{
    "body": "Burcin, can you review this ticket?",
    "created_at": "2010-03-03T12:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71876",
    "user": "https://github.com/malb"
}
```

Burcin, can you review this ticket?



---

archive/issue_comments_071877.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-15T06:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71877",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071878.json:
```json
{
    "body": "Wow, I just ran into exactly this same segfault \"in the wild\" while doing some math.  \n\nI'm glad you fixed this.",
    "created_at": "2010-03-15T06:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71878",
    "user": "https://github.com/williamstein"
}
```

Wow, I just ran into exactly this same segfault "in the wild" while doing some math.  

I'm glad you fixed this.



---

archive/issue_comments_071879.json:
```json
{
    "body": "One doctest fails on sage.math after applying the patch:\n\n```\nsage -t  devel/sage/sage/rings/polynomial/term_order.py                                \n         [3.0 s]                                                                       \nsage -t  devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx             \n**********************************************************************                 \nFile \"/virtual/scratch/wstein/build/sage-4.3.4.alpha1/devel/sage-main/sage/rings/polynomial/multi_polynomial_libsingular.pyx\", line 4293:                                             \n    sage: r                                                                                \nExpected:                                                                                  \n    y^6*a^4 - 4*y^5*a^4*b - 4*y^5*a^3*u + y^5*a^2 - y^5 + 6*y^4*a^4*b^2 + 12*y^4*a^3*b*u - 4*y^4*a^2*b + 6*y^4*a^2*u^2 - 2*y^4*a*u + 4*y^4*b \\                                        \n    - 4*y^3*a^4*b^3 - 12*y^3*a^3*b^2*u + 6*y^3*a^2*b^2 - 12*y^3*a^2*b*u^2 + 6*y^3*a*b*u - 4*y^3*a*u^3 - 6*y^3*b^2 + y^3*u^2 + y^2*a^4*b^4 \\                                           \n    + 4*y^2*a^3*b^3*u - 4*y^2*a^2*b^3 + 6*y^2*a^2*b^2*u^2 - 6*y^2*a*b^2*u + 4*y^2*a*b*u^3 + 4*y^2*b^3 - 2*y^2*b*u^2 + y^2*u^4 + y*a^2*b^4 \\                                           \n    + 2*y*a*b^3*u - y*b^4 + y*b^2*u^2                                                      \nGot:                                                                                       \n    y^6*a^4 - 4*y^5*a^4*b - 4*y^5*a^3*u + y^5*a^2 - y^5 + 6*y^4*a^4*b^2 + 12*y^4*a^3*b*u - 4*y^4*a^2*b + 6*y^4*a^2*u^2 - 2*y^4*a*u + 4*y^4*b - 4*y^3*a^4*b^3 - 12*y^3*a^3*b^2*u + 6*y^3*a^2*b^2 - 12*y^3*a^2*b*u^2 + 6*y^3*a*b*u - 4*y^3*a*u^3 - 6*y^3*b^2 + y^3*u^2 + y^2*a^4*b^4 + 4*y^2*a^3*b^3*u - 4*y^2*a^2*b^3 + 6*y^2*a^2*b^2*u^2 - 6*y^2*a*b^2*u + 4*y^2*a*b*u^3 + 4*y^2*b^3 - 2*y^2*b*u^2 + y^2*u^4 + y*a^2*b^4 + 2*y*a*b^3*u - y*b^4 + y*b^2*u^2             \n**********************************************************************                     \n1 items had failures:                                                                      \n   1 of  19 in __main__.example_84                                                         \n***Test Failed*** 1 failures.                                                              \nFor whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_multi_polynomial_libsingular.py                                                                                \n         [9.5 s]            \n```\n",
    "created_at": "2010-03-15T06:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71879",
    "user": "https://github.com/williamstein"
}
```

One doctest fails on sage.math after applying the patch:

```
sage -t  devel/sage/sage/rings/polynomial/term_order.py                                
         [3.0 s]                                                                       
sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx             
**********************************************************************                 
File "/virtual/scratch/wstein/build/sage-4.3.4.alpha1/devel/sage-main/sage/rings/polynomial/multi_polynomial_libsingular.pyx", line 4293:                                             
    sage: r                                                                                
Expected:                                                                                  
    y^6*a^4 - 4*y^5*a^4*b - 4*y^5*a^3*u + y^5*a^2 - y^5 + 6*y^4*a^4*b^2 + 12*y^4*a^3*b*u - 4*y^4*a^2*b + 6*y^4*a^2*u^2 - 2*y^4*a*u + 4*y^4*b \                                        
    - 4*y^3*a^4*b^3 - 12*y^3*a^3*b^2*u + 6*y^3*a^2*b^2 - 12*y^3*a^2*b*u^2 + 6*y^3*a*b*u - 4*y^3*a*u^3 - 6*y^3*b^2 + y^3*u^2 + y^2*a^4*b^4 \                                           
    + 4*y^2*a^3*b^3*u - 4*y^2*a^2*b^3 + 6*y^2*a^2*b^2*u^2 - 6*y^2*a*b^2*u + 4*y^2*a*b*u^3 + 4*y^2*b^3 - 2*y^2*b*u^2 + y^2*u^4 + y*a^2*b^4 \                                           
    + 2*y*a*b^3*u - y*b^4 + y*b^2*u^2                                                      
Got:                                                                                       
    y^6*a^4 - 4*y^5*a^4*b - 4*y^5*a^3*u + y^5*a^2 - y^5 + 6*y^4*a^4*b^2 + 12*y^4*a^3*b*u - 4*y^4*a^2*b + 6*y^4*a^2*u^2 - 2*y^4*a*u + 4*y^4*b - 4*y^3*a^4*b^3 - 12*y^3*a^3*b^2*u + 6*y^3*a^2*b^2 - 12*y^3*a^2*b*u^2 + 6*y^3*a*b*u - 4*y^3*a*u^3 - 6*y^3*b^2 + y^3*u^2 + y^2*a^4*b^4 + 4*y^2*a^3*b^3*u - 4*y^2*a^2*b^3 + 6*y^2*a^2*b^2*u^2 - 6*y^2*a*b^2*u + 4*y^2*a*b*u^3 + 4*y^2*b^3 - 2*y^2*b*u^2 + y^2*u^4 + y*a^2*b^4 + 2*y*a*b^3*u - y*b^4 + y*b^2*u^2             
**********************************************************************                     
1 items had failures:                                                                      
   1 of  19 in __main__.example_84                                                         
***Test Failed*** 1 failures.                                                              
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_multi_polynomial_libsingular.py                                                                                
         [9.5 s]            
```




---

archive/issue_comments_071880.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-15T06:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71880",
    "user": "https://github.com/williamstein"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071881.json:
```json
{
    "body": "Replying to [comment:7 was]:\n> One doctest fails on sage.math after applying the patch: [...]\n\nit seems just a formatting issue, both outputs are equal (and I don't understand why the 'expected'\none was split among several lines).\n\nNote that I also had this problem with:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: P.<x,y> = PolynomialRing(ZZ,2)\nsage: f = x+y\nsage: g=y^2+x \nsage: f.resultant(g,y)\n------------------------------------------------------------\nUnhandled SIGFPE: An unhandled floating point exception occured in Sage.\nThis probably occured because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n```\n\n| Sage Version 4.4.2, Release Date: 2010-05-19                       |\n| Type notebook() for the GUI, and license() for information.        |\nMaybe we can just fix the doctest?",
    "created_at": "2010-06-05T11:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71881",
    "user": "https://github.com/zimmermann6"
}
```

Replying to [comment:7 was]:
> One doctest fails on sage.math after applying the patch: [...]

it seems just a formatting issue, both outputs are equal (and I don't understand why the 'expected'
one was split among several lines).

Note that I also had this problem with:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: P.<x,y> = PolynomialRing(ZZ,2)
sage: f = x+y
sage: g=y^2+x 
sage: f.resultant(g,y)
------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```

| Sage Version 4.4.2, Release Date: 2010-05-19                       |
| Type notebook() for the GUI, and license() for information.        |
Maybe we can just fix the doctest?



---

archive/issue_comments_071882.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-06-05T11:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71882",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_071883.json:
```json
{
    "body": "I just tried the example above in my private Singular 3-1-1-3 + Sage 4.4 copy.\u00a0\n\n\n```\nsage: P.<x,y> = PolynomialRing(ZZ,2)\nsage: f = x+y\nsage: g=y^2+x \nsage: f.resultant(g,y)\ny^2 - y\n```\n\nThus, once#8059 is in, we can recheck and merge this patch?",
    "created_at": "2010-07-14T13:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71883",
    "user": "https://github.com/malb"
}
```

I just tried the example above in my private Singular 3-1-1-3 + Sage 4.4 copy. 


```
sage: P.<x,y> = PolynomialRing(ZZ,2)
sage: f = x+y
sage: g=y^2+x 
sage: f.resultant(g,y)
y^2 - y
```

Thus, once#8059 is in, we can recheck and merge this patch?



---

archive/issue_comments_071884.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-07-14T13:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71884",
    "user": "https://github.com/malb"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_071885.json:
```json
{
    "body": "Replying to [comment:9 malb]:\n> Thus, once#8059 is in, we can recheck and merge this patch?\n\nyes this needs work, since the resultant in `y` should not contain `y`!!!",
    "created_at": "2010-07-14T14:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71885",
    "user": "https://github.com/zimmermann6"
}
```

Replying to [comment:9 malb]:
> Thus, once#8059 is in, we can recheck and merge this patch?

yes this needs work, since the resultant in `y` should not contain `y`!!!



---

archive/issue_comments_071886.json:
```json
{
    "body": "Argh, I didn't even check the output. Btw:\n\n\n```\nsage: P.<x,y> = PolynomialRing(QQ,2)\nsage: f = x+\nsage: g=y^2+\nsage: f.resultant(g,y\nx^2 + x\n```\n",
    "created_at": "2010-07-14T20:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71886",
    "user": "https://github.com/malb"
}
```

Argh, I didn't even check the output. Btw:


```
sage: P.<x,y> = PolynomialRing(QQ,2)
sage: f = x+
sage: g=y^2+
sage: f.resultant(g,y
x^2 + x
```




---

archive/issue_comments_071887.json:
```json
{
    "body": "Attachment [trac_8173.patch](tarball://root/attachments/some-uuid/ticket8173/trac_8173.patch) by @malb created at 2010-07-14 21:20:45\n\nfixed the issue reported bu Paul",
    "created_at": "2010-07-14T21:20:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71887",
    "user": "https://github.com/malb"
}
```

Attachment [trac_8173.patch](tarball://root/attachments/some-uuid/ticket8173/trac_8173.patch) by @malb created at 2010-07-14 21:20:45

fixed the issue reported bu Paul



---

archive/issue_comments_071888.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-14T21:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71888",
    "user": "https://github.com/malb"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_071889.json:
```json
{
    "body": "The updated patch should fix the issue.",
    "created_at": "2010-07-14T21:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71889",
    "user": "https://github.com/malb"
}
```

The updated patch should fix the issue.



---

archive/issue_comments_071890.json:
```json
{
    "body": "Martin,\n\n> status  changed from needs_work to positive_review\n\nI guess you meant \"needs review\" instead of \"positive review\", since you are the author of the\npatch? Otherwise you forgot to fill the author and reviewer fields :-)\n\nPaul",
    "created_at": "2010-07-15T08:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71890",
    "user": "https://github.com/zimmermann6"
}
```

Martin,

> status  changed from needs_work to positive_review

I guess you meant "needs review" instead of "positive review", since you are the author of the
patch? Otherwise you forgot to fill the author and reviewer fields :-)

Paul



---

archive/issue_comments_071891.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-15T08:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71891",
    "user": "https://github.com/malb"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071892.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-15T08:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71892",
    "user": "https://github.com/malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071893.json:
```json
{
    "body": "Paul, I don't know where my head was yesterday. Thanks a lot for spotting this!",
    "created_at": "2010-07-15T08:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71893",
    "user": "https://github.com/malb"
}
```

Paul, I don't know where my head was yesterday. Thanks a lot for spotting this!



---

archive/issue_comments_071894.json:
```json
{
    "body": "Positive review. All doctests pass. Good work!\n\nPaul",
    "created_at": "2010-07-15T09:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71894",
    "user": "https://github.com/zimmermann6"
}
```

Positive review. All doctests pass. Good work!

Paul



---

archive/issue_comments_071895.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-15T09:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71895",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008376.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-07-21T01:45:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8173#event-8376"
}
```



---

archive/issue_comments_071896.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8173#issuecomment-71896",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
