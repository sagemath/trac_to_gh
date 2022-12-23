# Issue 6302: [with patch; needs review] make openopt an optional spkg

Issue created by migration from https://trac.sagemath.org/ticket/6302

Original creator: was

Original creation time: 2009-06-15 16:27:20

Assignee: tbd

It's here: 

  http://sage.math.washington.edu/home/wstein/patches/openopt-0.24.spkg



---

Comment by wdj created at 2009-06-15 17:29:53

This installs fine in 4.0.2.rc0 on ubuntu 9.04 amd64. Running tests now.


---

Comment by wdj created at 2009-06-15 22:17:38

Passes sage -testall and also installs fine on a 10.4 macbook.


---

Comment by mvngu created at 2009-07-19 18:16:02

The optional package `openopt-0.24.spkg` is now in the optional packages repository at

http://www.sagemath.org/packages/optional/openopt-0.24.spkg


---

Comment by mvngu created at 2009-07-19 18:16:02

Resolution: fixed


---

Comment by mvngu created at 2009-07-19 18:31:36

Changing status from closed to reopened.


---

Comment by mvngu created at 2009-07-19 18:31:36

Resolution changed from fixed to 


---

Comment by mvngu created at 2009-07-19 18:31:36

After uncompressing 

http://sage.math.washington.edu/home/wstein/patches/openopt-0.24.spkg

and doing `hg status`, I see lots of changes haven't been checked in. So I'm reopening this ticket. All changes need to be checked in via Mercurial. But note that the openopt project uses SVN for source code management.


---

Comment by was created at 2009-07-20 19:04:19

Replying to [comment:4 mvngu]:
> After uncompressing 
> 
> http://sage.math.washington.edu/home/wstein/patches/openopt-0.24.spkg
> 
> and doing `hg status`, I see lots of changes haven't been checked in.

No, that's wrong.  Everything was checked in.  The problem is that there was no hgignore, so all possible files that could get added to the repo (i.e. the stuff in src) got listed.  I've added an .hgignore and rebuilt the spkg then posted it again in the optional package repo.


---

Comment by schilly created at 2009-07-27 13:22:59

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

Comment by wdj created at 2009-07-27 13:30:44

What other tests need to be run before this can be given a positive review?


---

Comment by schilly created at 2009-07-27 13:44:14

Well, I've never reviewd a spkg before. So far as I can tell everything works as expected and therefore green light from me. Everything is only Python, and I think we can assume that it works on all platforms and there are no interferences with other parts of Sage, too.


---

Comment by wdj created at 2009-07-27 14:08:25

Okay, me too. I'll change it to positive review then.


---

Comment by mvngu created at 2009-07-29 12:20:29

Merged in the optional spkg repository on the Sage website.


---

Comment by mvngu created at 2009-07-29 12:20:29

Resolution: fixed
