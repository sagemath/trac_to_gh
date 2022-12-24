# Issue 9689: Numerical noise on devel/sage-main/sage/symbolic/expression.pyx

archive/issues_009689.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  jhpalmieri\n\nWhilst there is no complete 64-bit build of Sage on Solaris x86, a sufficiently large part of Sage does build (with a few changes) on Solaris 10 x86. When built on 'fulvia', a Dell Optiplex with Xeon processors, there was a numerical noise issue - see #9099\n\n\n```\nsage -t  -long devel/sage/sage/symbolic/expression.pyx\n**********************************************************************\nFile \"/home/palmieri/fulvia/sage-4.5.2.rc0/devel/sage-main/sage/symbolic/expression.pyx\", line 498\\\n3:\n    sage: maxima('sinh(1.0)')\nExpected:\n    1.175201193643801\nGot:\n    1.175201193643802\n```\n\n\nA computation with Mathematica, using 60 digits of precision gives \n\n\n```\nIn[2]:= N[Sinh[1],60]\n\nOut[2]= 1.17520119364380145688238185059560081515571798133409587022957\n```\n\n\nThe absolute error on Solaris x86 is slighly higher than seen on some other systems, but this is still a perfectly acceptable result.\n\nThis should be fairly easy to fix. I'll make a patch later today\n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9689\n\n",
    "created_at": "2010-08-05T08:27:45Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Numerical noise on devel/sage-main/sage/symbolic/expression.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9689",
    "user": "drkirkby"
}
```
Assignee: mvngu

CC:  jhpalmieri

Whilst there is no complete 64-bit build of Sage on Solaris x86, a sufficiently large part of Sage does build (with a few changes) on Solaris 10 x86. When built on 'fulvia', a Dell Optiplex with Xeon processors, there was a numerical noise issue - see #9099


```
sage -t  -long devel/sage/sage/symbolic/expression.pyx
**********************************************************************
File "/home/palmieri/fulvia/sage-4.5.2.rc0/devel/sage-main/sage/symbolic/expression.pyx", line 498\
3:
    sage: maxima('sinh(1.0)')
Expected:
    1.175201193643801
Got:
    1.175201193643802
```


A computation with Mathematica, using 60 digits of precision gives 


```
In[2]:= N[Sinh[1],60]

Out[2]= 1.17520119364380145688238185059560081515571798133409587022957
```


The absolute error on Solaris x86 is slighly higher than seen on some other systems, but this is still a perfectly acceptable result.

This should be fairly easy to fix. I'll make a patch later today

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9689





---

archive/issue_comments_094176.json:
```json
{
    "body": "I just realise the second failure shown on #9099\n\n\n```\nExpected:\n    0.881373587019543\nGot:\n    .8813735870195429\n```\n\n\nis the same file (devel/sage-main/sage/symbolic/expression.pyx) as this simple numerical noise issue. Hopefully be solved too. That's a less obvious problem to solve though. \n\nAny ideas anyone?",
    "created_at": "2010-08-05T17:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94176",
    "user": "drkirkby"
}
```

I just realise the second failure shown on #9099


```
Expected:
    0.881373587019543
Got:
    .8813735870195429
```


is the same file (devel/sage-main/sage/symbolic/expression.pyx) as this simple numerical noise issue. Hopefully be solved too. That's a less obvious problem to solve though. 

Any ideas anyone?



---

archive/issue_comments_094177.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-05T22:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94177",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094178.json:
```json
{
    "body": "Attachment [9689-sinh-noise-fix.patch](tarball://root/attachments/some-uuid/ticket9689/9689-sinh-noise-fix.patch) by drkirkby created at 2010-08-05 22:39:19\n\nSolves the numerical noise issue computing sinh(1.0). The archsinh case is more complex, and will be on another ticket.",
    "created_at": "2010-08-05T22:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94178",
    "user": "drkirkby"
}
```

Attachment [9689-sinh-noise-fix.patch](tarball://root/attachments/some-uuid/ticket9689/9689-sinh-noise-fix.patch) by drkirkby created at 2010-08-05 22:39:19

Solves the numerical noise issue computing sinh(1.0). The archsinh case is more complex, and will be on another ticket.



---

archive/issue_comments_094179.json:
```json
{
    "body": "It's not very pretty, but \n\n```\nabs(float(maxima('asinh(1.0)')) - 0.881373587019543) < 1e-15\n```\n\nor\n\n```\nmaxima('abs(asinh(1.0) - 0.881373587019543)') < 1e-15\n```\n\nwork for the other test.  Or:\n\n```\nsage: float(maxima('asinh(1.0)'))\n0.8813735870195429...\n```\n",
    "created_at": "2010-08-05T23:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94179",
    "user": "jhpalmieri"
}
```

It's not very pretty, but 

```
abs(float(maxima('asinh(1.0)')) - 0.881373587019543) < 1e-15
```

or

```
maxima('abs(asinh(1.0) - 0.881373587019543)') < 1e-15
```

work for the other test.  Or:

```
sage: float(maxima('asinh(1.0)'))
0.8813735870195429...
```




---

archive/issue_comments_094180.json:
```json
{
    "body": "Or replace \"float\" with \"RR\", etc.",
    "created_at": "2010-08-05T23:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94180",
    "user": "jhpalmieri"
}
```

Or replace "float" with "RR", etc.



---

archive/issue_comments_094181.json:
```json
{
    "body": "Yes, we can get this to pass, but that is just covering up a bug, as the number should never be printed as `.8813735870195429` It is a numerically correct result, but it is not printed the way one would expect a piece of software to print the number. \n \t \t\nCarl Witty is of the opinion this is either a Maxima or ECL bug\n\nhttp://groups.google.com/group/sage-devel/msg/aa318e11e84afe8d?hl=en\n\nI think its better to leave the `asinh(1.0)` case failing. It will be a constant reminder we need to get a real solution, not hack the doctest to get it to pass. \n\nUltimately, I feel the doctest has discovered a bug, which is what a good test should do. \n\nDave",
    "created_at": "2010-08-05T23:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94181",
    "user": "drkirkby"
}
```

Yes, we can get this to pass, but that is just covering up a bug, as the number should never be printed as `.8813735870195429` It is a numerically correct result, but it is not printed the way one would expect a piece of software to print the number. 
 	 	
Carl Witty is of the opinion this is either a Maxima or ECL bug

http://groups.google.com/group/sage-devel/msg/aa318e11e84afe8d?hl=en

I think its better to leave the `asinh(1.0)` case failing. It will be a constant reminder we need to get a real solution, not hack the doctest to get it to pass. 

Ultimately, I feel the doctest has discovered a bug, which is what a good test should do. 

Dave



---

archive/issue_comments_094182.json:
```json
{
    "body": "I created #9693 to resolve the leading zero problem and are going to copy the problem to the ECL and Maxima mailing lists, to see if we get any response. \n\nDave",
    "created_at": "2010-08-05T23:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94182",
    "user": "drkirkby"
}
```

I created #9693 to resolve the leading zero problem and are going to copy the problem to the ECL and Maxima mailing lists, to see if we get any response. 

Dave



---

archive/issue_comments_094183.json:
```json
{
    "body": "This looks fine to me and passed tests (in that file) on both 32-bit and 64-bit ubuntu.",
    "created_at": "2010-08-12T17:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94183",
    "user": "cremona"
}
```

This looks fine to me and passed tests (in that file) on both 32-bit and 64-bit ubuntu.



---

archive/issue_comments_094184.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-12T17:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94184",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094185.json:
```json
{
    "body": "Replying to [comment:8 cremona]:\n> This looks fine to me and passed tests (in that file) on both 32-bit and 64-bit ubuntu.\n\nThank you for the review John. \n\nDave",
    "created_at": "2010-08-12T18:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94185",
    "user": "drkirkby"
}
```

Replying to [comment:8 cremona]:
> This looks fine to me and passed tests (in that file) on both 32-bit and 64-bit ubuntu.

Thank you for the review John. 

Dave



---

archive/issue_comments_094186.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-08-16T21:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94186",
    "user": "mpatel"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_094187.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-24T02:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9689#issuecomment-94187",
    "user": "mpatel"
}
```

Resolution: fixed
