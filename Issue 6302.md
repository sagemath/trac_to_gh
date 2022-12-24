# Issue 6302: [with patch; needs review] make openopt an optional spkg

archive/issues_006302.json:
```json
{
    "body": "Assignee: tbd\n\nIt's here: \n\n  http://sage.math.washington.edu/home/wstein/patches/openopt-0.24.spkg\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6302\n\n",
    "created_at": "2009-06-15T16:27:20Z",
    "labels": [
        "packages: optional",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch; needs review] make openopt an optional spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6302",
    "user": "was"
}
```
Assignee: tbd

It's here: 

  http://sage.math.washington.edu/home/wstein/patches/openopt-0.24.spkg


Issue created by migration from https://trac.sagemath.org/ticket/6302





---

archive/issue_comments_050271.json:
```json
{
    "body": "This installs fine in 4.0.2.rc0 on ubuntu 9.04 amd64. Running tests now.",
    "created_at": "2009-06-15T17:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50271",
    "user": "wdj"
}
```

This installs fine in 4.0.2.rc0 on ubuntu 9.04 amd64. Running tests now.



---

archive/issue_comments_050272.json:
```json
{
    "body": "Passes sage -testall and also installs fine on a 10.4 macbook.",
    "created_at": "2009-06-15T22:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50272",
    "user": "wdj"
}
```

Passes sage -testall and also installs fine on a 10.4 macbook.



---

archive/issue_comments_050273.json:
```json
{
    "body": "The optional package `openopt-0.24.spkg` is now in the optional packages repository at\n\nhttp://www.sagemath.org/packages/optional/openopt-0.24.spkg",
    "created_at": "2009-07-19T18:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50273",
    "user": "mvngu"
}
```

The optional package `openopt-0.24.spkg` is now in the optional packages repository at

http://www.sagemath.org/packages/optional/openopt-0.24.spkg



---

archive/issue_comments_050274.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-19T18:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50274",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_050275.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-07-19T18:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50275",
    "user": "mvngu"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_050276.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-07-19T18:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50276",
    "user": "mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_050277.json:
```json
{
    "body": "After uncompressing \n\nhttp://sage.math.washington.edu/home/wstein/patches/openopt-0.24.spkg\n\nand doing `hg status`, I see lots of changes haven't been checked in. So I'm reopening this ticket. All changes need to be checked in via Mercurial. But note that the openopt project uses SVN for source code management.",
    "created_at": "2009-07-19T18:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50277",
    "user": "mvngu"
}
```

After uncompressing 

http://sage.math.washington.edu/home/wstein/patches/openopt-0.24.spkg

and doing `hg status`, I see lots of changes haven't been checked in. So I'm reopening this ticket. All changes need to be checked in via Mercurial. But note that the openopt project uses SVN for source code management.



---

archive/issue_comments_050278.json:
```json
{
    "body": "Replying to [comment:4 mvngu]:\n> After uncompressing \n> \n> http://sage.math.washington.edu/home/wstein/patches/openopt-0.24.spkg\n> \n> and doing `hg status`, I see lots of changes haven't been checked in.\n\nNo, that's wrong.  Everything was checked in.  The problem is that there was no hgignore, so all possible files that could get added to the repo (i.e. the stuff in src) got listed.  I've added an .hgignore and rebuilt the spkg then posted it again in the optional package repo.",
    "created_at": "2009-07-20T19:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50278",
    "user": "was"
}
```

Replying to [comment:4 mvngu]:
> After uncompressing 
> 
> http://sage.math.washington.edu/home/wstein/patches/openopt-0.24.spkg
> 
> and doing `hg status`, I see lots of changes haven't been checked in.

No, that's wrong.  Everything was checked in.  The problem is that there was no hgignore, so all possible files that could get added to the repo (i.e. the stuff in src) got listed.  I've added an .hgignore and rebuilt the spkg then posted it again in the optional package repo.



---

archive/issue_comments_050279.json:
```json
{
    "body": "installs fine on kbuntu 9.04/32bit /w sage 4.1. I'm able to run an arbitrary example from the openopt website as a test problem. It uses the \"ralg\" solver provided by openopt.\n\n\n```\npreparser(False)\nfrom numpy import *\nfrom openopt import NLP\nn = 10\nan = arange(n) # array [0, 1, 2, ..., n-1]\nx0 = n+15*(1+cos(an))\nf = lambda x: (x**2).sum() + sqrt(x**3-arange(n)**3).sum()\ndf = lambda x: 2*x + 0.5*3*x**2/sqrt(x**3-arange(n)**3)\nc = lambda x: an**3 - x**3\ndc = lambda x: diag(-3 * x**2)\nlb = arange(n)\np = NLP(f, x0, df=df, lb=lb, c=c, dc=dc, iprint = 100, maxIter = 10000, maxFunEvals = 1e8)\nr = p.solve('ralg')\n# expected r.xf = [0, 1, 2, ..., n-1]\n```\n\n\n\n```\nsage: r = p.solve('ralg')\n-----------------------------------------------------\nsolver: ralg   problem: unnamed   goal: minimum\n iter    objFunVal    log10(maxResidual)\n    0  9.129e+03            -100.00\n  100  4.104e+03            -100.00\n  169  2.878e+02            -100.00\nistop:  3 (|| X[k] - X[k-1] || < xtol)\nSolver:   Time Elapsed = 2.41   CPU Time Elapsed = 1.88\nobjFunValue: 287.75368 (feasible, max constraint =  0)\n\nsage: # expected r.xf = [0, 1, 2, ..., n-1]\nsage: r.xf\n\narray([ 0.5964556 ,  1.00355187,  2.00415294,  3.00156818,  4.0012493 ,\n        5.00080644,  6.00036981,  7.00052146,  8.00016061,  9.00015341])\n\n```\n",
    "created_at": "2009-07-27T13:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50279",
    "user": "schilly"
}
```

installs fine on kbuntu 9.04/32bit /w sage 4.1. I'm able to run an arbitrary example from the openopt website as a test problem. It uses the "ralg" solver provided by openopt.


```
preparser(False)
from numpy import *
from openopt import NLP
n = 10
an = arange(n) # array [0, 1, 2, ..., n-1]
x0 = n+15*(1+cos(an))
f = lambda x: (x**2).sum() + sqrt(x**3-arange(n)**3).sum()
df = lambda x: 2*x + 0.5*3*x**2/sqrt(x**3-arange(n)**3)
c = lambda x: an**3 - x**3
dc = lambda x: diag(-3 * x**2)
lb = arange(n)
p = NLP(f, x0, df=df, lb=lb, c=c, dc=dc, iprint = 100, maxIter = 10000, maxFunEvals = 1e8)
r = p.solve('ralg')
# expected r.xf = [0, 1, 2, ..., n-1]
```



```
sage: r = p.solve('ralg')
-----------------------------------------------------
solver: ralg   problem: unnamed   goal: minimum
 iter    objFunVal    log10(maxResidual)
    0  9.129e+03            -100.00
  100  4.104e+03            -100.00
  169  2.878e+02            -100.00
istop:  3 (|| X[k] - X[k-1] || < xtol)
Solver:   Time Elapsed = 2.41   CPU Time Elapsed = 1.88
objFunValue: 287.75368 (feasible, max constraint =  0)

sage: # expected r.xf = [0, 1, 2, ..., n-1]
sage: r.xf

array([ 0.5964556 ,  1.00355187,  2.00415294,  3.00156818,  4.0012493 ,
        5.00080644,  6.00036981,  7.00052146,  8.00016061,  9.00015341])

```




---

archive/issue_comments_050280.json:
```json
{
    "body": "What other tests need to be run before this can be given a positive review?",
    "created_at": "2009-07-27T13:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50280",
    "user": "wdj"
}
```

What other tests need to be run before this can be given a positive review?



---

archive/issue_comments_050281.json:
```json
{
    "body": "Well, I've never reviewd a spkg before. So far as I can tell everything works as expected and therefore green light from me. Everything is only Python, and I think we can assume that it works on all platforms and there are no interferences with other parts of Sage, too.",
    "created_at": "2009-07-27T13:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50281",
    "user": "schilly"
}
```

Well, I've never reviewd a spkg before. So far as I can tell everything works as expected and therefore green light from me. Everything is only Python, and I think we can assume that it works on all platforms and there are no interferences with other parts of Sage, too.



---

archive/issue_comments_050282.json:
```json
{
    "body": "Okay, me too. I'll change it to positive review then.",
    "created_at": "2009-07-27T14:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50282",
    "user": "wdj"
}
```

Okay, me too. I'll change it to positive review then.



---

archive/issue_comments_050283.json:
```json
{
    "body": "Merged in the optional spkg repository on the Sage website.",
    "created_at": "2009-07-29T12:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50283",
    "user": "mvngu"
}
```

Merged in the optional spkg repository on the Sage website.



---

archive/issue_comments_050284.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-29T12:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6302#issuecomment-50284",
    "user": "mvngu"
}
```

Resolution: fixed
