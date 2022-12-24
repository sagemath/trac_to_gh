# Issue 2021: SR eigenvalues and eigenvectors returns nonsense in both cases in the simplest example

archive/issues_002021.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: a = matrix(SR, 2, [1,2,3,4])\nsage: a.eigenspaces()\nTraceback (most recent call last):\n...\nTypeError: 'SymbolicArithmetic' object is not iterable\nsage: a.eigenvalues()\n[]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2021\n\n",
    "created_at": "2008-02-01T03:29:51Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "SR eigenvalues and eigenvectors returns nonsense in both cases in the simplest example",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2021",
    "user": "was"
}
```
Assignee: was


```
sage: a = matrix(SR, 2, [1,2,3,4])
sage: a.eigenspaces()
Traceback (most recent call last):
...
TypeError: 'SymbolicArithmetic' object is not iterable
sage: a.eigenvalues()
[]
```


Issue created by migration from https://trac.sagemath.org/ticket/2021





---

archive/issue_comments_013041.json:
```json
{
    "body": "The problems go on:\n\n\n```\nsage: a.eigenvalues(SR)\nTraceback (most recent call last):\n...\nNotImplementedError\nsage: a.eigenvalues(CC)\nTraceback (most recent call last):\n...\nTypeError: len() of unsized object\nsage: a.eigenvalues?\nDocstring: [nothing]\n```\n",
    "created_at": "2008-02-01T03:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13041",
    "user": "was"
}
```

The problems go on:


```
sage: a.eigenvalues(SR)
Traceback (most recent call last):
...
NotImplementedError
sage: a.eigenvalues(CC)
Traceback (most recent call last):
...
TypeError: len() of unsized object
sage: a.eigenvalues?
Docstring: [nothing]
```




---

archive/issue_comments_013042.json:
```json
{
    "body": "Something *very* weird is going on here.  Here is something that I think is causing the problem with a.eigenvalues above:\n\n\n```\nsage: from sage.calculus.calculus import SymbolicVariable\nsage: tmp=SymbolicVariable('tmp_var')\nsage: a=matrix(SR,[[1,2],[3,4]])\nsage: a.charpoly(tmp).expand().solve(tmp)\n[]\nsage: (tmp^2+2*tmp).solve(tmp)\n[]\nsage: tmp=SymbolicVariable('tmp_var')\nsage: (tmp^2+2*tmp).solve(tmp)\n[tmp_var == -2, tmp_var == 0]\nsage:\nExiting SAGE (CPU time 0m0.13s, Wall time 0m46.43s).\nExiting spawned Maxima process.\nExiting spawned Maxima process.\n```\n\n\nThe suspicious thing is the *two* maxima processes that are exiting when I exit sage.",
    "created_at": "2008-02-01T15:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13042",
    "user": "jason"
}
```

Something *very* weird is going on here.  Here is something that I think is causing the problem with a.eigenvalues above:


```
sage: from sage.calculus.calculus import SymbolicVariable
sage: tmp=SymbolicVariable('tmp_var')
sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(tmp).expand().solve(tmp)
[]
sage: (tmp^2+2*tmp).solve(tmp)
[]
sage: tmp=SymbolicVariable('tmp_var')
sage: (tmp^2+2*tmp).solve(tmp)
[tmp_var == -2, tmp_var == 0]
sage:
Exiting SAGE (CPU time 0m0.13s, Wall time 0m46.43s).
Exiting spawned Maxima process.
Exiting spawned Maxima process.
```


The suspicious thing is the *two* maxima processes that are exiting when I exit sage.



---

archive/issue_comments_013043.json:
```json
{
    "body": "More data below.  When calling a.charpoly(y).expand().solve(y) first, things are messed up.  When calling it after solving an equation with y, things work fine\n\n\n```\nsage: from sage.calculus.calculus import SymbolicVariable\nsage: y=SymbolicVariable('y')\nsage: a=matrix(SR,[[1,2],[3,4]])\nsage: # First solve an equation, then solve a.charpoly\nsage: (y+1).solve(y)\n[y == -1]\nsage: a.charpoly(y).expand().solve(y)\n[y == (5 - sqrt(33))/2, y == (sqrt(33) + 5)/2]\nsage: y=SymbolicVariable('y')\nsage: # Now solve a.charpoly, then solve an equation\nsage: a.charpoly(y).expand().solve(y)\n[]\nsage: (y+1).solve(y)\n[]\n```\n",
    "created_at": "2008-02-01T15:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13043",
    "user": "jason"
}
```

More data below.  When calling a.charpoly(y).expand().solve(y) first, things are messed up.  When calling it after solving an equation with y, things work fine


```
sage: from sage.calculus.calculus import SymbolicVariable
sage: y=SymbolicVariable('y')
sage: a=matrix(SR,[[1,2],[3,4]])
sage: # First solve an equation, then solve a.charpoly
sage: (y+1).solve(y)
[y == -1]
sage: a.charpoly(y).expand().solve(y)
[y == (5 - sqrt(33))/2, y == (sqrt(33) + 5)/2]
sage: y=SymbolicVariable('y')
sage: # Now solve a.charpoly, then solve an equation
sage: a.charpoly(y).expand().solve(y)
[]
sage: (y+1).solve(y)
[]
```




---

archive/issue_comments_013044.json:
```json
{
    "body": "This is a complete shot in the dark, but does the problem have to do with asking one maxima instance a question that only makes sense to the other maxima instance?  In which instance is the symbolic variable kept and in which instance is the matrix kept?",
    "created_at": "2008-02-01T15:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13044",
    "user": "jason"
}
```

This is a complete shot in the dark, but does the problem have to do with asking one maxima instance a question that only makes sense to the other maxima instance?  In which instance is the symbolic variable kept and in which instance is the matrix kept?



---

archive/issue_comments_013045.json:
```json
{
    "body": "The key part here seems to be that \nsage: a=matrix(SR,[[1,2],[3,4]])\nsage: a.charpoly(x).solve(x)\n[]\nwhile\nsage: x._maxima_()\nx\nsage: a=matrix(SR,[[1,2],[3,4]])\nsage: a.charpoly(x).solve(x)\n[x == (5 - sqrt(33))/2, x == (sqrt(33) + 5)/2]\n\nIn fact, we may manually reproduce this behavior by \nsage: x._maxima_(maxima)sage: a=matrix(SR,[[1,2],[3,4]])\nsage: a.charpoly(x).solve(x)\n[]\n\nIt follows the likely cause is then not importing maxima from calculus somewhere and using instead the global maxima for a calculation involving charpoly.",
    "created_at": "2008-02-01T18:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13045",
    "user": "gfurnish"
}
```

The key part here seems to be that 
sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(x).solve(x)
[]
while
sage: x._maxima_()
x
sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(x).solve(x)
[x == (5 - sqrt(33))/2, x == (sqrt(33) + 5)/2]

In fact, we may manually reproduce this behavior by 
sage: x._maxima_(maxima)sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(x).solve(x)
[]

It follows the likely cause is then not importing maxima from calculus somewhere and using instead the global maxima for a calculation involving charpoly.



---

archive/issue_comments_013046.json:
```json
{
    "body": "The key part here seems to be that \n\n\n```\nsage: a=matrix(SR,[[1,2],[3,4]])\nsage: a.charpoly(x).solve(x) []\n```\n\nwhile \n\n\n```\nsage: x._maxima_() \nx \nsage: a=matrix(SR,[[1,2],[3,4]])\nsage: a.charpoly(x).solve(x) \n[x == (5 - sqrt(33))/2, x == (sqrt(33) + 5)/2]\n```\n\n\nIn fact, we may manually reproduce this behavior by\n\n\n```\nsage: x._maxima_(maxima)\nx\nsage: a=matrix(SR,[[1,2],[3,4]]) \nsage: a.charpoly(x).solve(x) []\n```\n\n\nIt follows the likely cause is then not importing maxima from calculus somewhere and using instead the global maxima for a calculation involving charpoly.  Sorry about the double post but this at least is readable.",
    "created_at": "2008-02-01T18:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13046",
    "user": "gfurnish"
}
```

The key part here seems to be that 


```
sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(x).solve(x) []
```

while 


```
sage: x._maxima_() 
x 
sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(x).solve(x) 
[x == (5 - sqrt(33))/2, x == (sqrt(33) + 5)/2]
```


In fact, we may manually reproduce this behavior by


```
sage: x._maxima_(maxima)
x
sage: a=matrix(SR,[[1,2],[3,4]]) 
sage: a.charpoly(x).solve(x) []
```


It follows the likely cause is then not importing maxima from calculus somewhere and using instead the global maxima for a calculation involving charpoly.  Sorry about the double post but this at least is readable.



---

archive/issue_comments_013047.json:
```json
{
    "body": "changing the import in matrix_symbolic_dense from from\n\n\n```\nfrom sage.interfaces.maxima import maxima\n```\n\nto \n\n```\nfrom sage.calculus.calculus import maxima\n```\n\nappears to fix the problem.  However, it appears that this issue is unrelated to the original eigenspaces issue.",
    "created_at": "2008-02-01T18:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13047",
    "user": "gfurnish"
}
```

changing the import in matrix_symbolic_dense from from


```
from sage.interfaces.maxima import maxima
```

to 

```
from sage.calculus.calculus import maxima
```

appears to fix the problem.  However, it appears that this issue is unrelated to the original eigenspaces issue.



---

archive/issue_comments_013048.json:
```json
{
    "body": "Attachment [symbolic-matrix-maxima.patch](tarball://root/attachments/some-uuid/ticket2021/symbolic-matrix-maxima.patch) by jason created at 2008-02-01 19:09:46\n\nThanks to gfurnish's brilliance, we found a sticky maxima issue corrected in the first patch (with an added doctest to make sure something like that doesn't happen again!)",
    "created_at": "2008-02-01T19:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13048",
    "user": "jason"
}
```

Attachment [symbolic-matrix-maxima.patch](tarball://root/attachments/some-uuid/ticket2021/symbolic-matrix-maxima.patch) by jason created at 2008-02-01 19:09:46

Thanks to gfurnish's brilliance, we found a sticky maxima issue corrected in the first patch (with an added doctest to make sure something like that doesn't happen again!)



---

archive/issue_comments_013049.json:
```json
{
    "body": "Illustrating the eigenspaces issue:\n\n\n```\nsage: a=matrix(SR,[[1,2],[3,4]])\nsage: b=matrix(QQ,[[1,2],[3,4]])\nsage: [i for i in a.fcp()]\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/grout/sage/devel/sage-main/sage/matrix/<ipython console> in <module>()\n\n<type 'exceptions.TypeError'>: 'SymbolicArithmetic' object is not iterable\nsage: [i for i in b.fcp()]\n[(x^2 - 5*x - 2, 1)]\n```\n",
    "created_at": "2008-02-01T19:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13049",
    "user": "jason"
}
```

Illustrating the eigenspaces issue:


```
sage: a=matrix(SR,[[1,2],[3,4]])
sage: b=matrix(QQ,[[1,2],[3,4]])
sage: [i for i in a.fcp()]
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/matrix/<ipython console> in <module>()

<type 'exceptions.TypeError'>: 'SymbolicArithmetic' object is not iterable
sage: [i for i in b.fcp()]
[(x^2 - 5*x - 2, 1)]
```




---

archive/issue_comments_013050.json:
```json
{
    "body": "And another note:\n\n\n```\nsage: a=matrix(SR,[[1,2],[3,4]])\nsage: [i for i in a.fcp().factor_list()]\n[(x^2 - 5*x - 2, 1)]\n```\n\n\nSo apparently we need to somehow call factor_list() when we have a symbolic matrix or we need to change SymbolicArithmetic to iterate through factor_list() when we ask for an iterator.",
    "created_at": "2008-02-01T19:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13050",
    "user": "jason"
}
```

And another note:


```
sage: a=matrix(SR,[[1,2],[3,4]])
sage: [i for i in a.fcp().factor_list()]
[(x^2 - 5*x - 2, 1)]
```


So apparently we need to somehow call factor_list() when we have a symbolic matrix or we need to change SymbolicArithmetic to iterate through factor_list() when we ask for an iterator.



---

archive/issue_comments_013051.json:
```json
{
    "body": "[positive review] for symbolic-matrix-maxima.patch.  This is a serious bug fix that should be included ASAP.",
    "created_at": "2008-02-01T22:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13051",
    "user": "was"
}
```

[positive review] for symbolic-matrix-maxima.patch.  This is a serious bug fix that should be included ASAP.



---

archive/issue_comments_013052.json:
```json
{
    "body": "don't close this issue yet, though.  A second patch should be coming along to fix the eigenspaces issue.",
    "created_at": "2008-02-01T22:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13052",
    "user": "jason"
}
```

don't close this issue yet, though.  A second patch should be coming along to fix the eigenspaces issue.



---

archive/issue_comments_013053.json:
```json
{
    "body": "Replying to [comment:12 jason]:\n> don't close this issue yet, though.  A second patch should be coming along to fix the eigenspaces issue.\n\nJason, please open another ticket for that issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-02T03:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13053",
    "user": "mabshoff"
}
```

Replying to [comment:12 jason]:
> don't close this issue yet, though.  A second patch should be coming along to fix the eigenspaces issue.

Jason, please open another ticket for that issue.

Cheers,

Michael



---

archive/issue_comments_013054.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-02T03:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13054",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013055.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc5",
    "created_at": "2008-02-02T03:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2021#issuecomment-13055",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc5
