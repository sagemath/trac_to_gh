# Issue 163: plot hypergeometric_U fails

archive/issues_000163.json:
```json
{
    "body": "Assignee: was\n\nKeywords: pari, hyperu\n\nThis is funny:\n\n\n```\nP = plot(hypergeometric_U(1.0,1.0,x),0.1,0.9)\n```\n\nfails (hangs, actually) but \n\n```\nsage: f = lambda x: gp.eval(\"hyperu(1,1,%s)\"%x)\nsage: P = plot(f,0,1)\nsage: show(P)\n```\n\n\nhypergeometric_U is in functions/special.py. The error\nmay have something to do with the pari class.\n\nworks fine.\n\nIssue created by migration from https://trac.sagemath.org/ticket/163\n\n",
    "created_at": "2006-10-29T22:51:31Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "plot hypergeometric_U fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/163",
    "user": "wdj"
}
```
Assignee: was

Keywords: pari, hyperu

This is funny:


```
P = plot(hypergeometric_U(1.0,1.0,x),0.1,0.9)
```

fails (hangs, actually) but 

```
sage: f = lambda x: gp.eval("hyperu(1,1,%s)"%x)
sage: P = plot(f,0,1)
sage: show(P)
```


hypergeometric_U is in functions/special.py. The error
may have something to do with the pari class.

works fine.

Issue created by migration from https://trac.sagemath.org/ticket/163





---

archive/issue_comments_000726.json:
```json
{
    "body": "With Sage 2.8.2 I get:\n\n```\n[mabshoff@m940 sage-2.8.2]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.2, Release Date: 2007-08-22                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: P = plot(hypergeometric_U(1.0,1.0,x),0.1,0.9)\n---------------------------------------------------------------------------\n<class 'gen.PariError'>                   Traceback (most recent call last)\n\n/tmp/Work2/sage-2.8.2/<ipython console> in <module>()\n\n/tmp/Work2/sage-2.8.2/local/lib/python2.5/site-packages/sage/functions/special.py in hypergeometric_U(alpha, beta, x, prec)\n    570     from sage.libs.pari.all import pari\n    571     R,a = _setup(prec)\n--> 572     b = R(pari(x).hyperu(alpha,beta))\n    573     pari.set_real_precision(a)\n    574     return b\n\n/tmp/Work2/sage-2.8.2/gen.pyx in gen._pari_trap()\n\n<class 'gen.PariError'>: incorrect type (20)\n```\n\nMaybe this is something for Sage Bug Day 2.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-28T18:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/163#issuecomment-726",
    "user": "mabshoff"
}
```

With Sage 2.8.2 I get:

```
[mabshoff@m940 sage-2.8.2]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.2, Release Date: 2007-08-22                       |
| Type notebook() for the GUI, and license() for information.        |
sage: P = plot(hypergeometric_U(1.0,1.0,x),0.1,0.9)
---------------------------------------------------------------------------
<class 'gen.PariError'>                   Traceback (most recent call last)

/tmp/Work2/sage-2.8.2/<ipython console> in <module>()

/tmp/Work2/sage-2.8.2/local/lib/python2.5/site-packages/sage/functions/special.py in hypergeometric_U(alpha, beta, x, prec)
    570     from sage.libs.pari.all import pari
    571     R,a = _setup(prec)
--> 572     b = R(pari(x).hyperu(alpha,beta))
    573     pari.set_real_precision(a)
    574     return b

/tmp/Work2/sage-2.8.2/gen.pyx in gen._pari_trap()

<class 'gen.PariError'>: incorrect type (20)
```

Maybe this is something for Sage Bug Day 2.

Cheers,

Michael



---

archive/issue_comments_000727.json:
```json
{
    "body": "Changing component from interfaces to number theory.",
    "created_at": "2007-08-28T18:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/163#issuecomment-727",
    "user": "mabshoff"
}
```

Changing component from interfaces to number theory.



---

archive/issue_comments_000728.json:
```json
{
    "body": "Changing type from task to defect.",
    "created_at": "2007-09-23T14:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/163#issuecomment-728",
    "user": "mabshoff"
}
```

Changing type from task to defect.



---

archive/issue_comments_000729.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T01:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/163#issuecomment-729",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000730.json:
```json
{
    "body": "This now gives a type error, as it should.  The right thing to do is:\n\n```\nsage: P = plot(lambda x: hypergeometric_U(1.0,1.0,x),0.1,0.9)\nsage: show(P)\n```\n",
    "created_at": "2007-10-21T01:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/163#issuecomment-730",
    "user": "was"
}
```

This now gives a type error, as it should.  The right thing to do is:

```
sage: P = plot(lambda x: hypergeometric_U(1.0,1.0,x),0.1,0.9)
sage: show(P)
```

