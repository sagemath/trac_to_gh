# Issue 7998: Add William's Riemann Prime Counting Function code to Sage (EASY)

archive/issues_007998.json:
```json
{
    "body": "Assignee: was\n\nCC:  was leif\n\nKeywords: Riemann prime counting function\n\nAdd William's Riemann Prime Counting Function code to Sage.\nThere is already source available at http://wstein.org/rh/rh/code/code.sage.\nI have found this very useful.  There has been talk of using Ri or an approximation in the prime_pi function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7998\n\n",
    "created_at": "2010-01-19T15:17:52Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Add William's Riemann Prime Counting Function code to Sage (EASY)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7998",
    "user": "kevin.stueve"
}
```
Assignee: was

CC:  was leif

Keywords: Riemann prime counting function

Add William's Riemann Prime Counting Function code to Sage.
There is already source available at http://wstein.org/rh/rh/code/code.sage.
I have found this very useful.  There has been talk of using Ri or an approximation in the prime_pi function.

Issue created by migration from https://trac.sagemath.org/ticket/7998





---

archive/issue_comments_069897.json:
```json
{
    "body": "I was not aware that Sage already had an implementation of the Riemann prime counting function in mpmath.\n\n```\nimport mpmath \nmpmath.functions.riemannr(100)\n```\n\n\nIt would be nice if there was a page that listed the functions in Sage related to prime number theory, listing those in pari, mpmath, various other files, etc.\n\nI am going to open a new ticket for getting approximations to the prime counting function that use the nontrivial zeros into Sage.\n\nI am going to keep this ticket open, changing the task from \"Get Riemann Prime counting function into Sage\", to \"Improve prime number theory function documentation\".\n\n1) The docstring for Li, the logarithmic integral, should refer to the existence of a Riemann prime counting function in Sage.  The documentation for prime_pi should refer to the existence of the Li and R approximations.  The documentation for Li should refer to the existence of the prime_pi function.  mpmath's riemannr function refers to mpmath's primepi function (which is good documentation style).  Sage's local copy of mpmath's riemannr documentation should refer to Sage's prime_pi function (which currently uses Legendre's method, which is much better than mpmath's primepi).  Li, R, and prime_pi's documentation strings should all refer to each other.\n\n2) When I search for Riemann prime counting function, or especially the exact name of the function, riemannr, at http://www.sagemath.org/doc/reference/search.html, I should be able to find something about the Riemann prime counting function in Sage.  There should be a simple way to search for any function in Sage.\n\n3) By default searches should include documentation for subcomponents of Sage, such as mpmath (http://mpmath.googlecode.com/svn/trunk/doc/build/index.html).  At a minimum, a list of other pages to search (such as the mpmath documentation and pages for other subcomponents of Sage) should be provided after a search.  \"Some other pages that might contain the information you seek:.....\"\n\nIt was not until I researched mpmath's logarithmic integral implementation that I stumbled upon documentation for mpmath's Riemann prime counting function at http://mpmath.googlecode.com/svn/trunk/doc/build/functions/numtheory.html#riemannr\n\nI would imagine that many Sage users would have the same trouble I did.\n\nI believe that the Riemann prime counting function plays such a critical role in prime number theory that it should be accessible in Sage without importing from mpmath.",
    "created_at": "2010-01-31T06:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7998#issuecomment-69897",
    "user": "kevin.stueve"
}
```

I was not aware that Sage already had an implementation of the Riemann prime counting function in mpmath.

```
import mpmath 
mpmath.functions.riemannr(100)
```


It would be nice if there was a page that listed the functions in Sage related to prime number theory, listing those in pari, mpmath, various other files, etc.

I am going to open a new ticket for getting approximations to the prime counting function that use the nontrivial zeros into Sage.

I am going to keep this ticket open, changing the task from "Get Riemann Prime counting function into Sage", to "Improve prime number theory function documentation".

1) The docstring for Li, the logarithmic integral, should refer to the existence of a Riemann prime counting function in Sage.  The documentation for prime_pi should refer to the existence of the Li and R approximations.  The documentation for Li should refer to the existence of the prime_pi function.  mpmath's riemannr function refers to mpmath's primepi function (which is good documentation style).  Sage's local copy of mpmath's riemannr documentation should refer to Sage's prime_pi function (which currently uses Legendre's method, which is much better than mpmath's primepi).  Li, R, and prime_pi's documentation strings should all refer to each other.

2) When I search for Riemann prime counting function, or especially the exact name of the function, riemannr, at http://www.sagemath.org/doc/reference/search.html, I should be able to find something about the Riemann prime counting function in Sage.  There should be a simple way to search for any function in Sage.

3) By default searches should include documentation for subcomponents of Sage, such as mpmath (http://mpmath.googlecode.com/svn/trunk/doc/build/index.html).  At a minimum, a list of other pages to search (such as the mpmath documentation and pages for other subcomponents of Sage) should be provided after a search.  "Some other pages that might contain the information you seek:....."

It was not until I researched mpmath's logarithmic integral implementation that I stumbled upon documentation for mpmath's Riemann prime counting function at http://mpmath.googlecode.com/svn/trunk/doc/build/functions/numtheory.html#riemannr

I would imagine that many Sage users would have the same trouble I did.

I believe that the Riemann prime counting function plays such a critical role in prime number theory that it should be accessible in Sage without importing from mpmath.
