# Issue 571: weird simon_two_descent doctest failure

archive/issues_000571.json:
```json
{
    "body": "Assignee: was\n\nI removed the # long after this doctest:\n\n```\n             sage: E = EllipticCurve([0, 0, 1, -23737, 960366])    \n             sage: r, s, G = E.simon_two_descent(); r,s       # long\n             (8, 8)\n```\n\nthen ran the doctests and it fails.  This is strange because from the console it works fine.\nThe failure (see below) suggests too low of precision in bnfsunit/get_arch (in PARI).  Very weird. \nJohn Cremona is working on many improvements to this very code, so maybe it will all be fixed\nby that. \n\n\n```\nwas@ubuntu:~/d/sage/sage/schemes/elliptic_curves$ sage -t ell_rational_field.py\nsage -t  ell_rational_field.py                               **********************************************************************\nFile \"ell_rational_field.py\", line 905:\n    sage: r, s, G = E.simon_two_descent(); r,s\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s.dev/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_22[19]>\", line 1, in <module>\n        r, s, G = E.simon_two_descent(); r,s###line 905:\n    sage: r, s, G = E.simon_two_descent(); r,s\n      File \"/home/was/s.dev/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 913, in simon_two_descent\n        maxprob=maxprob, limbigprime=limbigprime)\n      File \"/home/was/s.dev/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py\", line 93, in simon_two_descent\n        raise RuntimeError, \"%s\\nAn error occured while running Simon's 2-descent program\"%s\n    RuntimeError:   *** bnfsunit: precision too low in get_arch.\n    An error occured while running Simon's 2-descent program\n**********************************************************************\n1 items had failures:\n   1 of  20 in __main__.example_22\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_ell_rational_field.py\n         [51.1 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/571\n\n",
    "created_at": "2007-09-02T18:16:12Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "bug"
    ],
    "title": "weird simon_two_descent doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/571",
    "user": "was"
}
```
Assignee: was

I removed the # long after this doctest:

```
             sage: E = EllipticCurve([0, 0, 1, -23737, 960366])    
             sage: r, s, G = E.simon_two_descent(); r,s       # long
             (8, 8)
```

then ran the doctests and it fails.  This is strange because from the console it works fine.
The failure (see below) suggests too low of precision in bnfsunit/get_arch (in PARI).  Very weird. 
John Cremona is working on many improvements to this very code, so maybe it will all be fixed
by that. 


```
was@ubuntu:~/d/sage/sage/schemes/elliptic_curves$ sage -t ell_rational_field.py
sage -t  ell_rational_field.py                               **********************************************************************
File "ell_rational_field.py", line 905:
    sage: r, s, G = E.simon_two_descent(); r,s
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s.dev/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[19]>", line 1, in <module>
        r, s, G = E.simon_two_descent(); r,s###line 905:
    sage: r, s, G = E.simon_two_descent(); r,s
      File "/home/was/s.dev/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 913, in simon_two_descent
        maxprob=maxprob, limbigprime=limbigprime)
      File "/home/was/s.dev/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py", line 93, in simon_two_descent
        raise RuntimeError, "%s\nAn error occured while running Simon's 2-descent program"%s
    RuntimeError:   *** bnfsunit: precision too low in get_arch.
    An error occured while running Simon's 2-descent program
**********************************************************************
1 items had failures:
   1 of  20 in __main__.example_22
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_ell_rational_field.py
         [51.1 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/571





---

archive/issue_comments_002962.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2008-01-27T04:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2962",
    "user": "AlexGhitza"
}
```

Resolution: worksforme



---

archive/issue_comments_002963.json:
```json
{
    "body": "Just tried this in 2.10 on Gentoo and the problem seems to have vanished:\n\n\n```\nsage -t  ell_rational_field.py                              \n         [40.6 s]\n```\n",
    "created_at": "2008-01-27T04:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2963",
    "user": "AlexGhitza"
}
```

Just tried this in 2.10 on Gentoo and the problem seems to have vanished:


```
sage -t  ell_rational_field.py                              
         [40.6 s]
```




---

archive/issue_comments_002964.json:
```json
{
    "body": "I can confirm that the doctest passes with `-t -long` on OSX 10.5.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-27T05:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2964",
    "user": "mabshoff"
}
```

I can confirm that the doctest passes with `-t -long` on OSX 10.5.

Cheers,

Michael



---

archive/issue_comments_002965.json:
```json
{
    "body": "Resolution changed from worksforme to ",
    "created_at": "2008-01-27T12:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2965",
    "user": "was"
}
```

Resolution changed from worksforme to 



---

archive/issue_comments_002966.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-01-27T12:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2966",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002967.json:
```json
{
    "body": "John and Denis Simone in fact did greatly update this code and it is now in Sage (for quote some time).  And this particularly doctest runs almost instantly now:\n\n\n```\nsage: E = EllipticCurve([0, 0, 1, -23737, 960366])    \nsage: time r, s, G = E.simon_two_descent(); r,s\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.02 s\nWall time: 0.56\n```\n\n\nThe attached patch removes the #long.",
    "created_at": "2008-01-27T12:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2967",
    "user": "was"
}
```

John and Denis Simone in fact did greatly update this code and it is now in Sage (for quote some time).  And this particularly doctest runs almost instantly now:


```
sage: E = EllipticCurve([0, 0, 1, -23737, 960366])    
sage: time r, s, G = E.simon_two_descent(); r,s
CPU times: user 0.01 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.56
```


The attached patch removes the #long.



---

archive/issue_comments_002968.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-27T12:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2968",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_002969.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T14:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2969",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002970.json:
```json
{
    "body": "Merged trac-571-simon-2-descent.patch in Sage 2.10.1.rc2",
    "created_at": "2008-01-27T14:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2970",
    "user": "mabshoff"
}
```

Merged trac-571-simon-2-descent.patch in Sage 2.10.1.rc2



---

archive/issue_comments_002971.json:
```json
{
    "body": "Obviously: Patch is trivial and looks good to me.",
    "created_at": "2008-01-27T14:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2971",
    "user": "mabshoff"
}
```

Obviously: Patch is trivial and looks good to me.



---

archive/issue_comments_002972.json:
```json
{
    "body": "Has the pari version changed since this was reported?  That might have fixed it since there was an underlying precision bug in the pari library in sage which was fix fixed in the current version of libpari.",
    "created_at": "2008-01-28T13:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2972",
    "user": "cremona"
}
```

Has the pari version changed since this was reported?  That might have fixed it since there was an underlying precision bug in the pari library in sage which was fix fixed in the current version of libpari.



---

archive/issue_comments_002973.json:
```json
{
    "body": "> Has the pari version changed since this was reported?\n\nYes it has.  But more importantly Simone's 2-descent library was *totally* rewritten by Simone since this was reported, so that also may have resolved this issue.",
    "created_at": "2008-01-28T13:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/571#issuecomment-2973",
    "user": "was"
}
```

> Has the pari version changed since this was reported?

Yes it has.  But more importantly Simone's 2-descent library was *totally* rewritten by Simone since this was reported, so that also may have resolved this issue.
