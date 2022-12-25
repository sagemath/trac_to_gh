# Issue 211: speed up polynomial root finding

archive/issues_000211.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nOn Tue, 23 Jan 2007 14:09:56 -0800, Kiran S. Kedlaya <kedlaya@mit.edu> wrote:\n \n> Here's a benchmark I just tried, which annoys me.\n>  \n> sage: def test1():\n> ....:     P.<x> = PolynomialRing(RationalField())\n> ....:     t = x^8 - 11*x^7 + x^5 - 1\n> ....:     for _ in xrange(1000):\n> ....:         t.complex_roots()\n> ....:\n> sage: time test1()\n> CPU times: user 6.78 s, sys: 0.02 s, total: 6.80 s\n> Wall time: 6.80\n> sage: def test2():\n> ....:     t = pari(\"x^8 - 11*x^7 + x^5 - 1\")\n> ....:     for _ in xrange(1000):\n> ....:          t.polroots()\n> ....:\n> sage: time test2()\n> CPU times: user 6.15 s, sys: 0.00 s, total: 6.15 s\n> Wall time: 6.15\n> sage: %magma\n> magma: procedure test3()\n> magma:     P<x> := PolynomialRing(RealField(53));\n> magma:     u := x^8 - 11*x^7 + x^5 - 1;\n> magma:     for i := 1 to 1000 do\n> magma:         t := Roots(u);\n> magma:     end for;\n> magma: end procedure;\n> magma: time test3();\n>  Time: 1.200\n>  \n> The thing that bugs me is that Magma does not have some fancy\n> proprietary algorithm for finding roots of a univariate polynomial; it\n> uses PARI! So why are we so much slower?\n \nWhy do you think MAGMA uses PARI for this?  (And this isn't so much\na problem with SAGE but with PARI....  Try the same computation\ndirectly in PARI and it is just as slow.)\n \nIf you really want the answer to only 53-bits precision, by the way,\nnumpy can do it much much faster than MAGMA. For example,\n \nsage: import numpy\nsage: f = numpy.array([1,-11,0,1,0,0,0,0,-1]))\nsage: numpy.roots(f)\nsage: array([ 10.99172314+0.j        ,  -0.72174425+0.j        ,\n         -0.45332013+0.53432014j,  -0.45332013-0.53432014j,\n          0.66182264+0.30451078j,   0.66182264-0.30451078j,\n          0.15650805+0.67766101j,   0.15650805-0.67766101j])\nsage: time v=[numpy.roots(f) for _ in range(1000)]\nCPU times: user 0.28 s, sys: 0.00 s, total: 0.28 s\nWall time: 0.28\n \nThat's already about 5 times faster than MAGMA.  And I bet\nthat on larger degree numpy beats MAGMA by a lot more...\n \nSAGE doesn't use numpy for root finding yet, partly because\nnumpy was added to SAGE only very recently, and I haven't\ntouched the root finding code in a while.\n \nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/211\n\n",
    "created_at": "2007-01-23T23:15:09Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "speed up polynomial root finding",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/211",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
On Tue, 23 Jan 2007 14:09:56 -0800, Kiran S. Kedlaya <kedlaya@mit.edu> wrote:
 
> Here's a benchmark I just tried, which annoys me.
>  
> sage: def test1():
> ....:     P.<x> = PolynomialRing(RationalField())
> ....:     t = x^8 - 11*x^7 + x^5 - 1
> ....:     for _ in xrange(1000):
> ....:         t.complex_roots()
> ....:
> sage: time test1()
> CPU times: user 6.78 s, sys: 0.02 s, total: 6.80 s
> Wall time: 6.80
> sage: def test2():
> ....:     t = pari("x^8 - 11*x^7 + x^5 - 1")
> ....:     for _ in xrange(1000):
> ....:          t.polroots()
> ....:
> sage: time test2()
> CPU times: user 6.15 s, sys: 0.00 s, total: 6.15 s
> Wall time: 6.15
> sage: %magma
> magma: procedure test3()
> magma:     P<x> := PolynomialRing(RealField(53));
> magma:     u := x^8 - 11*x^7 + x^5 - 1;
> magma:     for i := 1 to 1000 do
> magma:         t := Roots(u);
> magma:     end for;
> magma: end procedure;
> magma: time test3();
>  Time: 1.200
>  
> The thing that bugs me is that Magma does not have some fancy
> proprietary algorithm for finding roots of a univariate polynomial; it
> uses PARI! So why are we so much slower?
 
Why do you think MAGMA uses PARI for this?  (And this isn't so much
a problem with SAGE but with PARI....  Try the same computation
directly in PARI and it is just as slow.)
 
If you really want the answer to only 53-bits precision, by the way,
numpy can do it much much faster than MAGMA. For example,
 
sage: import numpy
sage: f = numpy.array([1,-11,0,1,0,0,0,0,-1]))
sage: numpy.roots(f)
sage: array([ 10.99172314+0.j        ,  -0.72174425+0.j        ,
         -0.45332013+0.53432014j,  -0.45332013-0.53432014j,
          0.66182264+0.30451078j,   0.66182264-0.30451078j,
          0.15650805+0.67766101j,   0.15650805-0.67766101j])
sage: time v=[numpy.roots(f) for _ in range(1000)]
CPU times: user 0.28 s, sys: 0.00 s, total: 0.28 s
Wall time: 0.28
 
That's already about 5 times faster than MAGMA.  And I bet
that on larger degree numpy beats MAGMA by a lot more...
 
SAGE doesn't use numpy for root finding yet, partly because
numpy was added to SAGE only very recently, and I haven't
touched the root finding code in a while.
 
William
```


Issue created by migration from https://trac.sagemath.org/ticket/211





---

archive/issue_comments_000942.json:
```json
{
    "body": "In light of bug #442, this might be bad -- factoring input precise to 53 bits gives output precise to about 5 bits.",
    "created_at": "2007-08-18T19:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/211#issuecomment-942",
    "user": "https://github.com/rlmill"
}
```

In light of bug #442, this might be bad -- factoring input precise to 53 bits gives output precise to about 5 bits.



---

archive/issue_comments_000943.json:
```json
{
    "body": "In other words, numpy's speed is probably coming from its lack of accuracy. GSL gives highly accurate results, at least in the example given here:\n\nhttp://www.gnu.org/software/gsl/manual/html_node/Roots-of-Polynomials-Examples.html",
    "created_at": "2007-08-18T20:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/211#issuecomment-943",
    "user": "https://github.com/rlmill"
}
```

In other words, numpy's speed is probably coming from its lack of accuracy. GSL gives highly accurate results, at least in the example given here:

http://www.gnu.org/software/gsl/manual/html_node/Roots-of-Polynomials-Examples.html



---

archive/issue_comments_000944.json:
```json
{
    "body": "in sage-2.8.1/local/lib/python2.5/site-packages/numpy/lib/polynomial.py, line 116 appears to be casting whatever float type is given to just float. This might be why numpy is giving inaccurate output.",
    "created_at": "2007-08-18T20:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/211#issuecomment-944",
    "user": "https://github.com/rlmill"
}
```

in sage-2.8.1/local/lib/python2.5/site-packages/numpy/lib/polynomial.py, line 116 appears to be casting whatever float type is given to just float. This might be why numpy is giving inaccurate output.



---

archive/issue_comments_000945.json:
```json
{
    "body": "Carl Witty and John Voight have done some work in this area, so we should discuss what has been done and needs to be done (if any)\n\nCheers,\n\nMichael",
    "created_at": "2007-10-21T12:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/211#issuecomment-945",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Carl Witty and John Voight have done some work in this area, so we should discuss what has been done and needs to be done (if any)

Cheers,

Michael



---

archive/issue_comments_000946.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2007-11-03T17:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/211#issuecomment-946",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_000947.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-03T17:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/211#issuecomment-947",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_000948.json:
```json
{
    "body": "Fixed by cwitty's code that went into 2.8.12.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-25T18:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/211#issuecomment-948",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by cwitty's code that went into 2.8.12.

Cheers,

Michael



---

archive/issue_comments_000949.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-25T18:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/211#issuecomment-949",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
