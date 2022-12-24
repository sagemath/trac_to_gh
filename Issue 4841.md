# Issue 4841: Update Maxima to 5.17.x (new upstream)

archive/issues_004841.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @mwhansen @certik\n\nThere is a new Maxima spgk at\n\nhttp://sage.math.washington.edu/home/mabshoff/maxima-5.17.1.spkg\n\nbut there are issues. It will probably (hopefully?) not be the final stable release of 5.17.x.\n\nIssues coming up in the comment section next.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4841\n\n",
    "created_at": "2008-12-20T22:24:20Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Update Maxima to 5.17.x (new upstream)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4841",
    "user": "mabshoff"
}
```
Assignee: @burcin

CC:  @mwhansen @certik

There is a new Maxima spgk at

http://sage.math.washington.edu/home/mabshoff/maxima-5.17.1.spkg

but there are issues. It will probably (hopefully?) not be the final stable release of 5.17.x.

Issues coming up in the comment section next.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4841





---

archive/issue_comments_036715.json:
```json
{
    "body": "Limits and assumption problems in functional.py:\n\n```\nFile \"/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/functional.py\", line 19:\n    sage: limit(a*sin(x)/x, x=0)\n    <SNIP>\n    Is  a  positive, negative, or zero?\n```\n\nLimit regression, reported to maxima-dev already:\n\n```\nFile \"/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/functional.py\", line 301:\n    sage: lim(1/x, x=0)\nExpected:\n    und\nGot:\n    +Infinity\n```\n\nThis is also a limits+assumption issue, but WTF would that fail in sympy_test:\n\n```\nsage -t -long devel//sage/sage/calculus/test_sympy.py\nFile \"/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/test_sympy.py\", line 60:\n    : limit((tan(x+y) - tan(x))/y, y=0)\n    TypeError: Computation failed since Maxima requested additional constraints (use assume):\n    Is  tan(x)  positive, negative, or zero?\n```\n\nNot sure what happens here, i.e whether this is Maxima's or Sage's fault:\n\n```\nsage -t -long devel//sage/sage/functions/special.py\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/functions/special.py\", line 847:\n    sage: spherical_harmonic(3,2,x,y)\n    TypeError: Error executing code in Maxima\n    CODE:\n    \tsage5 : spherical_harmonic(3,2,x,y)$\n    Maxima ERROR:\n    \t\n    Bad argument to `genfact'\n```\n\nVersion failures, trivial to fix, but also erf seems to have improved:\n\n```\nsage -t -long devel//sage/sage/interfaces/maxima.py\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/interfaces/maxima.py\", line 999:\n    sage: maxima.version()\nExpected:\n    '5.16.3'\nGot:\n    '5.17.1'\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/interfaces/maxima.py\", line 1689:\n    sage: f.numer()         # I wonder how to get a real number (~1.463)??\nExpected:\n    -.8862269254527579*%i*erf(%i)\nGot:\n    -.8862269254527579*%i*(1.650425758797543*%i+1.110223024625156E-16)\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/interfaces/maxima.py\", line 2300:\n    sage: maxima_version()\nExpected:\n    '5.16.3'\nGot:\n    '5.17.1'\n**********************************************************************\n```\n\n\nIssue in calculus.py:\n\n```\nFile \"/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/calculus.py\", line 6618:\n    sage: complex(erf(3*I))\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: unable to simplify to complex approximation\nGot:\n    (1.110223024625156e-16+1629.9946226005709j)\n\n\nTrying:\n    p1 = plot(xt,Integer(0),Integer(1)/Integer(2),rgbcolor=(Integer(1),Integer(0),Integer(0)))###line 2452:_sage_    >>> p1 = plot(xt,0,1/2,rgbcolor=(1,0,0))\nExpecting nothing\nException exceptions.RuntimeError: RuntimeError('maximum recursion depth exceeded',) in  ignored\n<Repeated indefinitely>\n\nThe following doctest causes this:\n\n        Next we form the augmented matrix of the above system:\n            sage: A = matrix([[s, 16, 270],[1, s, 90+1/s]])\n            sage: E = A.echelon_form()\n            sage: xt = E[0,2].inverse_laplace(s,t)\n            sage: yt = E[1,2].inverse_laplace(s,t)\n            sage: print xt\n                                4 t         - 4 t\n                           91  e      629  e\n                         - -------- + ----------- + 1\n                              2            2\n            sage: print yt\n                                 4 t         - 4 t\n                            91  e      629  e\n                            -------- + -----------\n                               8            8\n            sage: p1 = plot(xt,0,1/2,rgbcolor=(1,0,0))\n            sage: p2 = plot(yt,0,1/2,rgbcolor=(0,1,0))\n            sage: (p1+p2).save()\n```\n\n\nThere are likely more issues in calculus.py\n\nCheers,\n\nMichael",
    "created_at": "2008-12-20T22:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4841#issuecomment-36715",
    "user": "mabshoff"
}
```

Limits and assumption problems in functional.py:

```
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/functional.py", line 19:
    sage: limit(a*sin(x)/x, x=0)
    <SNIP>
    Is  a  positive, negative, or zero?
```

Limit regression, reported to maxima-dev already:

```
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/functional.py", line 301:
    sage: lim(1/x, x=0)
Expected:
    und
Got:
    +Infinity
```

This is also a limits+assumption issue, but WTF would that fail in sympy_test:

```
sage -t -long devel//sage/sage/calculus/test_sympy.py
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/test_sympy.py", line 60:
    : limit((tan(x+y) - tan(x))/y, y=0)
    TypeError: Computation failed since Maxima requested additional constraints (use assume):
    Is  tan(x)  positive, negative, or zero?
```

Not sure what happens here, i.e whether this is Maxima's or Sage's fault:

```
sage -t -long devel//sage/sage/functions/special.py
**********************************************************************
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/functions/special.py", line 847:
    sage: spherical_harmonic(3,2,x,y)
    TypeError: Error executing code in Maxima
    CODE:
    	sage5 : spherical_harmonic(3,2,x,y)$
    Maxima ERROR:
    	
    Bad argument to `genfact'
```

Version failures, trivial to fix, but also erf seems to have improved:

```
sage -t -long devel//sage/sage/interfaces/maxima.py
**********************************************************************
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/interfaces/maxima.py", line 999:
    sage: maxima.version()
Expected:
    '5.16.3'
Got:
    '5.17.1'
**********************************************************************
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/interfaces/maxima.py", line 1689:
    sage: f.numer()         # I wonder how to get a real number (~1.463)??
Expected:
    -.8862269254527579*%i*erf(%i)
Got:
    -.8862269254527579*%i*(1.650425758797543*%i+1.110223024625156E-16)
**********************************************************************
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/interfaces/maxima.py", line 2300:
    sage: maxima_version()
Expected:
    '5.16.3'
Got:
    '5.17.1'
**********************************************************************
```


Issue in calculus.py:

```
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/calculus.py", line 6618:
    sage: complex(erf(3*I))
Expected:
    Traceback (most recent call last):
    ...
    TypeError: unable to simplify to complex approximation
Got:
    (1.110223024625156e-16+1629.9946226005709j)


Trying:
    p1 = plot(xt,Integer(0),Integer(1)/Integer(2),rgbcolor=(Integer(1),Integer(0),Integer(0)))###line 2452:_sage_    >>> p1 = plot(xt,0,1/2,rgbcolor=(1,0,0))
Expecting nothing
Exception exceptions.RuntimeError: RuntimeError('maximum recursion depth exceeded',) in  ignored
<Repeated indefinitely>

The following doctest causes this:

        Next we form the augmented matrix of the above system:
            sage: A = matrix([[s, 16, 270],[1, s, 90+1/s]])
            sage: E = A.echelon_form()
            sage: xt = E[0,2].inverse_laplace(s,t)
            sage: yt = E[1,2].inverse_laplace(s,t)
            sage: print xt
                                4 t         - 4 t
                           91  e      629  e
                         - -------- + ----------- + 1
                              2            2
            sage: print yt
                                 4 t         - 4 t
                            91  e      629  e
                            -------- + -----------
                               8            8
            sage: p1 = plot(xt,0,1/2,rgbcolor=(1,0,0))
            sage: p2 = plot(yt,0,1/2,rgbcolor=(0,1,0))
            sage: (p1+p2).save()
```


There are likely more issues in calculus.py

Cheers,

Michael



---

archive/issue_comments_036716.json:
```json
{
    "body": "Changing assignee from @burcin to mabshoff.",
    "created_at": "2008-12-20T22:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4841#issuecomment-36716",
    "user": "mabshoff"
}
```

Changing assignee from @burcin to mabshoff.



---

archive/issue_comments_036717.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-20T22:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4841#issuecomment-36717",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036718.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-12-26T18:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4841#issuecomment-36718",
    "user": "mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_036719.json:
```json
{
    "body": "Wontfix since there are regressions with assumptions that are too much of a problem compared with the benefit of upgrading. If someone disagrees feel free to reopen the ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-26T18:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4841#issuecomment-36719",
    "user": "mabshoff"
}
```

Wontfix since there are regressions with assumptions that are too much of a problem compared with the benefit of upgrading. If someone disagrees feel free to reopen the ticket.

Cheers,

Michael
