# Issue 9659: EK.regulator_of_points() doctest error in ell_number_field.py

archive/issues_009659.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  cremona ddrake leif\n\nReported by Leif Leonhardy on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/a932af7b005283b4#a932af7b005283b4):\n\n```\nOn 32-bit Ubuntu 9.04 (P4 Prescott 3.2GHz, gcc 4.3.3, native code) \n[...]\n   sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\"\n   ***************************************************************\n   File \"/home/leif/sage-4.5.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\", line 444:\n       sage: EK.regulator_of_points([P,T])\n   Expected:\n       -1.23259516440783e-32\n   Got:\n       -4.93038065763132e-32\n   ***************************************************************\n   1 items had failures:\n      1 of  42 in __main__.example_5\n   ***Test Failed*** 1 failures.\n   For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_ell_number_field.py\n            [171.9 s] \n```\n\n\nSee [this thread](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8315/trac_8315-doc_sidebar.patch) for a discussion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9659\n\n",
    "created_at": "2010-08-01T10:17:05Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "EK.regulator_of_points() doctest error in ell_number_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9659",
    "user": "mpatel"
}
```
Assignee: mvngu

CC:  cremona ddrake leif

Reported by Leif Leonhardy on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/a932af7b005283b4#a932af7b005283b4):

```
On 32-bit Ubuntu 9.04 (P4 Prescott 3.2GHz, gcc 4.3.3, native code) 
[...]
   sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py"
   ***************************************************************
   File "/home/leif/sage-4.5.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_number_field.py", line 444:
       sage: EK.regulator_of_points([P,T])
   Expected:
       -1.23259516440783e-32
   Got:
       -4.93038065763132e-32
   ***************************************************************
   1 items had failures:
      1 of  42 in __main__.example_5
   ***Test Failed*** 1 failures.
   For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_ell_number_field.py
            [171.9 s] 
```


See [this thread](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8315/trac_8315-doc_sidebar.patch) for a discussion.

Issue created by migration from https://trac.sagemath.org/ticket/9659





---

archive/issue_comments_093755.json:
```json
{
    "body": "If someone provides a patch, I can test it, but not much more at the moment.\n\nSo this might change to a 4.5.3 blocker. (I wouldn't mind, especially since I haven't yet done anything to track this issue down further.)",
    "created_at": "2010-08-01T17:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93755",
    "user": "leif"
}
```

If someone provides a patch, I can test it, but not much more at the moment.

So this might change to a 4.5.3 blocker. (I wouldn't mind, especially since I haven't yet done anything to track this issue down further.)



---

archive/issue_comments_093756.json:
```json
{
    "body": "I've inquired about this problem at [comment:ticket:9343:159 #9343].",
    "created_at": "2010-08-01T22:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93756",
    "user": "mpatel"
}
```

I've inquired about this problem at [comment:ticket:9343:159 #9343].



---

archive/issue_comments_093757.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-02T01:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93757",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093758.json:
```json
{
    "body": "The correct mathematical result is an exact 0,  obtained as a 2x2 determinant of the form [a,0; 0,0]:\n\n```\nsage: EK.height_pairing_matrix([P,T])\n[     1.41516132073186 -1.11022302462516e-16]\n[-1.11022302462516e-16     0.000000000000000]\n```\n\nI think the best way to get a machine-independent test here is to have\n\n```\nsage: EK.regulator_of_points([P,T]).abs() < 1e30\nTrue\n```\n\ninstead of putting the spurious small value into the doctest.\n\nThe patch does this (as well as leaving the original test with a #random tag).",
    "created_at": "2010-08-02T01:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93758",
    "user": "cremona"
}
```

The correct mathematical result is an exact 0,  obtained as a 2x2 determinant of the form [a,0; 0,0]:

```
sage: EK.height_pairing_matrix([P,T])
[     1.41516132073186 -1.11022302462516e-16]
[-1.11022302462516e-16     0.000000000000000]
```

I think the best way to get a machine-independent test here is to have

```
sage: EK.regulator_of_points([P,T]).abs() < 1e30
True
```

instead of putting the spurious small value into the doctest.

The patch does this (as well as leaving the original test with a #random tag).



---

archive/issue_comments_093759.json:
```json
{
    "body": "Just to be sure:  Should that be `1e30`, in order to be ultra-safe, or its reciprocal?",
    "created_at": "2010-08-02T01:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93759",
    "user": "mpatel"
}
```

Just to be sure:  Should that be `1e30`, in order to be ultra-safe, or its reciprocal?



---

archive/issue_comments_093760.json:
```json
{
    "body": "Hmmm, really `< 1e30`?\n\nAlso, I'd add a backref to this ticket.",
    "created_at": "2010-08-02T01:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93760",
    "user": "leif"
}
```

Hmmm, really `< 1e30`?

Also, I'd add a backref to this ticket.



---

archive/issue_comments_093761.json:
```json
{
    "body": "Replying to [comment:6 leif]:\n> Hmmm, really `< 1e30`?\n> \n> Also, I'd add a backref to this ticket.\n>\n \nIf you have a better suggestion, just do it.  Any specific numerical result will change with the new pari anyway.\n\nThe height of a torsion point is already exactly 0.  We could add more special cases for the regulator of two points P,Q that if either P or Q or P-Q were torsion then the regulator is 0, but as the necessary condition is that some linear combination n*P+m*Q=0 no such code would catch all these special cases.",
    "created_at": "2010-08-02T01:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93761",
    "user": "cremona"
}
```

Replying to [comment:6 leif]:
> Hmmm, really `< 1e30`?
> 
> Also, I'd add a backref to this ticket.
>
 
If you have a better suggestion, just do it.  Any specific numerical result will change with the new pari anyway.

The height of a torsion point is already exactly 0.  We could add more special cases for the regulator of two points P,Q that if either P or Q or P-Q were torsion then the regulator is 0, but as the necessary condition is that some linear combination n*P+m*Q=0 no such code would catch all these special cases.



---

archive/issue_comments_093762.json:
```json
{
    "body": "This is again a really weird one. The affected machine has just finished `ptestlong` on rc0: \"**All** tests passed!\" (This time the exclamation mark is appropriate, if it is intended to express surprise.)\n\nThe only thing I've changed w.r.t. the alpha0 and alpha1 builds is that I've added `-O2` to `CFLAGS` and `CXXFLAGS` (for the first time btw, not expecting this would make a difference regarding this doctest, since most parts are compiled with `-O2` or `-O3` by default).\n\nIn fact, `./sage -t -long` on `ell_number_field.py` now takes only about 159 seconds instead of the previous 172-173 seconds. (The whole `ptestlong` though took almost exactly four hours as usual.)\n\nI don't know what we should do with this ticket now. Merge anyway (with corrected upper bound)?\n\n\nP.S.: I just meant 1<sup>-30</sup> instead of 1<sup>30</sup> (as Mitesh noted, too).",
    "created_at": "2010-08-02T02:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93762",
    "user": "leif"
}
```

This is again a really weird one. The affected machine has just finished `ptestlong` on rc0: "**All** tests passed!" (This time the exclamation mark is appropriate, if it is intended to express surprise.)

The only thing I've changed w.r.t. the alpha0 and alpha1 builds is that I've added `-O2` to `CFLAGS` and `CXXFLAGS` (for the first time btw, not expecting this would make a difference regarding this doctest, since most parts are compiled with `-O2` or `-O3` by default).

In fact, `./sage -t -long` on `ell_number_field.py` now takes only about 159 seconds instead of the previous 172-173 seconds. (The whole `ptestlong` though took almost exactly four hours as usual.)

I don't know what we should do with this ticket now. Merge anyway (with corrected upper bound)?


P.S.: I just meant 1<sup>-30</sup> instead of 1<sup>30</sup> (as Mitesh noted, too).



---

archive/issue_comments_093763.json:
```json
{
    "body": "applies to 4.5.2.alpha0",
    "created_at": "2010-08-02T02:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93763",
    "user": "cremona"
}
```

applies to 4.5.2.alpha0



---

archive/issue_comments_093764.json:
```json
{
    "body": "Attachment\n\nOK, my mistake -- I have updated the patch so it now says 1e-30.\n\nThe optimization change will effect this a lot.   The optimization flag on a pari build was downgraded a while back for a silly reason; and upped again on the ticket upgrading pari.  This will effect all the number field code.",
    "created_at": "2010-08-02T02:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93764",
    "user": "cremona"
}
```

Attachment

OK, my mistake -- I have updated the patch so it now says 1e-30.

The optimization change will effect this a lot.   The optimization flag on a pari build was downgraded a while back for a silly reason; and upped again on the ticket upgrading pari.  This will effect all the number field code.



---

archive/issue_comments_093765.json:
```json
{
    "body": "Strange though this seems to only have a \"visible\" effect (i.e., numerical noise in a doctest) on that specific processor.",
    "created_at": "2010-08-02T02:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93765",
    "user": "leif"
}
```

Strange though this seems to only have a "visible" effect (i.e., numerical noise in a doctest) on that specific processor.



---

archive/issue_comments_093766.json:
```json
{
    "body": "(I actually touched that file on both Pentiums and compared the compile commands previously - there was no difference; of course not knowing this doctest uses external code.)",
    "created_at": "2010-08-02T02:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93766",
    "user": "leif"
}
```

(I actually touched that file on both Pentiums and compared the compile commands previously - there was no difference; of course not knowing this doctest uses external code.)



---

archive/issue_comments_093767.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-02T10:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93767",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093768.json:
```json
{
    "body": "Replying to [comment:9 cremona]:\n> OK, my mistake -- I have updated the patch so it now says 1e-30.\n\nThat looks reasonable to me. \n\n> The optimization change will effect this a lot.   The optimization flag on a pari build was downgraded a while back for a silly reason; and upped again on the ticket upgrading pari.  This will effect all the number field code.\n  \nAs a matter of interest, [I asked on gcc-help about the use of -O1 and -O3](http://gcc.gnu.org/ml/gcc-help/2010-07/msg00190.html). To quote from someone who I believe is a gcc developer\n\n''The -O3 optoin should be safe for correct code.  An important difference between -O2/-O3 and -O1 is that -O2 and -O3 enable strict aliasing and strict overflow.  Those options provide better optimization for correct code, but are far more likely to cause unexpected code generation for incorrect code.  See the -fstrict-aliasing and -fstrict-overflow\noptions.'' \n\n''The main difference between -O3 and -O2 is that -O3 enables more\nspeculative optimizations.  These should not miscompile your code, but\nthey may cause your program to run more slowly.''\n\nIt's not to me whether -O2 or -O3 is the better choice. You might find -O2 is actually faster than -O3!\n\nIMHO, we really do need set of benchmark results. \n\nBut the patch looks quite reasonable to me. The [IEEE 754 standard](http://en.wikipedia.org/wiki/IEEE_754-2008) does not guarantee that different systems implementing IEEE 754 maths will give the same result. Nor is there anything to say that any two different processors from Intel will give the same result. \n\nSince the correct result should be 0.0, a test that expected a number like -1.23259516440783e-32  was clearly flawed. \n\nPositive review. \n\nDave",
    "created_at": "2010-08-02T10:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93768",
    "user": "drkirkby"
}
```

Replying to [comment:9 cremona]:
> OK, my mistake -- I have updated the patch so it now says 1e-30.

That looks reasonable to me. 

> The optimization change will effect this a lot.   The optimization flag on a pari build was downgraded a while back for a silly reason; and upped again on the ticket upgrading pari.  This will effect all the number field code.
  
As a matter of interest, [I asked on gcc-help about the use of -O1 and -O3](http://gcc.gnu.org/ml/gcc-help/2010-07/msg00190.html). To quote from someone who I believe is a gcc developer

''The -O3 optoin should be safe for correct code.  An important difference between -O2/-O3 and -O1 is that -O2 and -O3 enable strict aliasing and strict overflow.  Those options provide better optimization for correct code, but are far more likely to cause unexpected code generation for incorrect code.  See the -fstrict-aliasing and -fstrict-overflow
options.'' 

''The main difference between -O3 and -O2 is that -O3 enables more
speculative optimizations.  These should not miscompile your code, but
they may cause your program to run more slowly.''

It's not to me whether -O2 or -O3 is the better choice. You might find -O2 is actually faster than -O3!

IMHO, we really do need set of benchmark results. 

But the patch looks quite reasonable to me. The [IEEE 754 standard](http://en.wikipedia.org/wiki/IEEE_754-2008) does not guarantee that different systems implementing IEEE 754 maths will give the same result. Nor is there anything to say that any two different processors from Intel will give the same result. 

Since the correct result should be 0.0, a test that expected a number like -1.23259516440783e-32  was clearly flawed. 

Positive review. 

Dave



---

archive/issue_comments_093769.json:
```json
{
    "body": "Just to check and for the record:  Leif, does Dr. Cremona's patch fix the failure with your alpha0 (or alpha1) build and, if you have one available, a similarly built rc0?",
    "created_at": "2010-08-02T21:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93769",
    "user": "mpatel"
}
```

Just to check and for the record:  Leif, does Dr. Cremona's patch fix the failure with your alpha0 (or alpha1) build and, if you have one available, a similarly built rc0?



---

archive/issue_comments_093770.json:
```json
{
    "body": "I'm merging the patch into my working copy of 4.5.2.rc1.",
    "created_at": "2010-08-04T02:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93770",
    "user": "mpatel"
}
```

I'm merging the patch into my working copy of 4.5.2.rc1.



---

archive/issue_comments_093771.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-04T02:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9659#issuecomment-93771",
    "user": "mpatel"
}
```

Resolution: fixed
