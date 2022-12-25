# Issue 9793: Make easy wrapper for symbolic lagrange interpolation

archive/issues_009793.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @jasongrout\n\nCurrently, one has to do something like one of these.\n\n```\n > 1. There is no way to get a symbolic interpolated polynomial de novo \n > without going through polynomial rings, e.g. all these steps: \n > \n > pts = [(1,2),(2,3),(3,2),(4,3),(5,2),(6,3)] \n > R.<x>=QQ[] \n > f = R.lagrange_polynomial(pts) \n > SR(f) \n > \nYes.  You could define your own function :) (see \nhttp://sage.cs.drake.edu/home/pub/2/, for example).  Also, mpmath and \nnumpy/scipy can get numerical values for the coefficients, I believe. \nMaxima also can construct a lagrange polynomial (load the 'interpol' \npackage) \nsage: maxima.load('interpol') \n\"/home/jason/sage-4.4.2/local/share/maxima/5.20.1/share/numeric/interpol.ma c\" \nsage: maxima.lagrange([[1,2],[3,4]]) \n-x+2*(x-1)+3 \n```\n\nThat's too bad; we need to wrap this to make it very easy to get the interpolation from a list of points with one command from SR.\n\nOne thing to discuss would be whether one would want an approximate one if the coefficients were floats/RR, or always to try for an exact one.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9794\n\n",
    "created_at": "2010-08-24T15:18:15Z",
    "labels": [
        "component: symbolics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Make easy wrapper for symbolic lagrange interpolation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9793",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @burcin

CC:  @jasongrout

Currently, one has to do something like one of these.

```
 > 1. There is no way to get a symbolic interpolated polynomial de novo 
 > without going through polynomial rings, e.g. all these steps: 
 > 
 > pts = [(1,2),(2,3),(3,2),(4,3),(5,2),(6,3)] 
 > R.<x>=QQ[] 
 > f = R.lagrange_polynomial(pts) 
 > SR(f) 
 > 
Yes.  You could define your own function :) (see 
http://sage.cs.drake.edu/home/pub/2/, for example).  Also, mpmath and 
numpy/scipy can get numerical values for the coefficients, I believe. 
Maxima also can construct a lagrange polynomial (load the 'interpol' 
package) 
sage: maxima.load('interpol') 
"/home/jason/sage-4.4.2/local/share/maxima/5.20.1/share/numeric/interpol.ma c" 
sage: maxima.lagrange([[1,2],[3,4]]) 
-x+2*(x-1)+3 
```

That's too bad; we need to wrap this to make it very easy to get the interpolation from a list of points with one command from SR.

One thing to discuss would be whether one would want an approximate one if the coefficients were floats/RR, or always to try for an exact one.

Issue created by migration from https://trac.sagemath.org/ticket/9794


