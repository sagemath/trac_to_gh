# Issue 3637: [with patch, needs review] jacobi sums implementation

archive/issues_003637.json:
```json
{
    "body": "Assignee: was\n\nImplement Jacobi sums of Dirichlet characters.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3637\n\n",
    "created_at": "2008-07-10T21:55:11Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] jacobi sums implementation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3637",
    "user": "ekirkman"
}
```
Assignee: was

Implement Jacobi sums of Dirichlet characters.

Issue created by migration from https://trac.sagemath.org/ticket/3637





---

archive/issue_comments_025724.json:
```json
{
    "body": "Attachment\n\nApplies to 3.0.4 and passes sage -testall.\n\nLet e, f be elements of D = DirichletGroup(N), for some N, and define the Jacobi sum by \nJ(e,f) = sum([e(x)*f(1-x) for x in IntegerModRing(N)]).\nExcept in \"corner cases\", this patch defines J(e,f) by G(e)*G(f)/G(e*f). \nThis is okay in most cases. (I'm having to rely on \nwww.math.mcgill.ca/goren/SeminarOnCohomology/mycohomologytalk.pdf since my books are disorganized due to some renovation at my house, but I'm going to assume Proposition 3.3 in that paper is correct.) However, the case of J(trivial, trivial) does not always seem to return the correct answer in general:\n\nsage: N = 9\nsage: D = DirichletGroup(N)\nsage: g = D(1)\nsage: g.jacobi_sum(g)\n7\nsage: sum([g(x)*g(1-x) for x in IntegerModRing(N)])\n3\n\nI could be wrong but possibly this needs to be looked at.\n\nIn any case, here are some amusing examples which could be mixed into the \ndocstring if desired:\n\nsage: N = 9\nsage: D = DirichletGroup(N)\nsage: e = D.0\nsage: e(-1)\n-1\nsage: f = D[-1]\nsage: e*f\n[1]\nsage: j1 = e.jacobi_sum(e)\nsage: j2 = f.jacobi_sum(f)\nsage: j3 = e.jacobi_sum(f)\nsage: j1*j1.conjugate(); j2*j2.conjugate(); j3*j3.conjugate()\n9\n9\n1\nsage: j1; (j1/3)^3\n-3*zeta18^3\n1\nsage: j2; (j2/3)^3\n3*zeta18^3 - 3\n1",
    "created_at": "2008-07-12T09:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3637#issuecomment-25724",
    "user": "wdj"
}
```

Attachment

Applies to 3.0.4 and passes sage -testall.

Let e, f be elements of D = DirichletGroup(N), for some N, and define the Jacobi sum by 
J(e,f) = sum([e(x)*f(1-x) for x in IntegerModRing(N)]).
Except in "corner cases", this patch defines J(e,f) by G(e)*G(f)/G(e*f). 
This is okay in most cases. (I'm having to rely on 
www.math.mcgill.ca/goren/SeminarOnCohomology/mycohomologytalk.pdf since my books are disorganized due to some renovation at my house, but I'm going to assume Proposition 3.3 in that paper is correct.) However, the case of J(trivial, trivial) does not always seem to return the correct answer in general:

sage: N = 9
sage: D = DirichletGroup(N)
sage: g = D(1)
sage: g.jacobi_sum(g)
7
sage: sum([g(x)*g(1-x) for x in IntegerModRing(N)])
3

I could be wrong but possibly this needs to be looked at.

In any case, here are some amusing examples which could be mixed into the 
docstring if desired:

sage: N = 9
sage: D = DirichletGroup(N)
sage: e = D.0
sage: e(-1)
-1
sage: f = D[-1]
sage: e*f
[1]
sage: j1 = e.jacobi_sum(e)
sage: j2 = f.jacobi_sum(f)
sage: j3 = e.jacobi_sum(f)
sage: j1*j1.conjugate(); j2*j2.conjugate(); j3*j3.conjugate()
9
9
1
sage: j1; (j1/3)^3
-3*zeta18^3
1
sage: j2; (j2/3)^3
3*zeta18^3 - 3
1



---

archive/issue_comments_025725.json:
```json
{
    "body": "I am not convinced that Sage should compute Gauss sums and Jacobi sums for Dirichlet characters of non-prime conductor.  By definition (see for instance the book by Berndt-Evans-Williams), these are sums over elements of a finite field GF(q), of values of character(s) of GF(q).  If q=p happens to be prime, we get the same result by working with a Dirichlet character on Z/pZ.  But in general Z/qZ and GF(q) have nothing to do with each other, and it's not clear to me what exactly we're computing if we're working with Z/qZ.\n\nSo I guess what I'm proposing is that we raise an exception if a Gauss or Jacobi sum is requested for a Dirichlet character of non-prime conductor.  And we should eventually implement these things over GF(q) for q non-prime.",
    "created_at": "2008-07-16T19:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3637#issuecomment-25725",
    "user": "AlexGhitza"
}
```

I am not convinced that Sage should compute Gauss sums and Jacobi sums for Dirichlet characters of non-prime conductor.  By definition (see for instance the book by Berndt-Evans-Williams), these are sums over elements of a finite field GF(q), of values of character(s) of GF(q).  If q=p happens to be prime, we get the same result by working with a Dirichlet character on Z/pZ.  But in general Z/qZ and GF(q) have nothing to do with each other, and it's not clear to me what exactly we're computing if we're working with Z/qZ.

So I guess what I'm proposing is that we raise an exception if a Gauss or Jacobi sum is requested for a Dirichlet character of non-prime conductor.  And we should eventually implement these things over GF(q) for q non-prime.



---

archive/issue_comments_025726.json:
```json
{
    "body": "Even in the prime case, I think the last two outputs below should agree:\n\n```\nsage: N = 13\nsage: D = DirichletGroup(N)\nsage: g = D(1)\nsage: g.jacobi_sum(g)\n13\nsage: sum([g(x)*g(1-x) for x in IntegerModRing(N)])\n11\n```\n\n(My previous comment was with N=9, which is not prime.) If your proposal is accepted and an exception is raised, I'd prefer to have an option where the exception is over-written and the result computed anyway. (Some people do research on finite ring computations and might find the ring-theoretic Jacobi+Gauss sum functions interesting.)",
    "created_at": "2008-07-16T20:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3637#issuecomment-25726",
    "user": "wdj"
}
```

Even in the prime case, I think the last two outputs below should agree:

```
sage: N = 13
sage: D = DirichletGroup(N)
sage: g = D(1)
sage: g.jacobi_sum(g)
13
sage: sum([g(x)*g(1-x) for x in IntegerModRing(N)])
11
```

(My previous comment was with N=9, which is not prime.) If your proposal is accepted and an exception is raised, I'd prefer to have an option where the exception is over-written and the result computed anyway. (Some people do research on finite ring computations and might find the ring-theoretic Jacobi+Gauss sum functions interesting.)



---

archive/issue_comments_025727.json:
```json
{
    "body": "Attachment\n\n`3637-ekirkman-jacobi-sums.patch` adds an error (and a check=False) option preventing Jacobi sums with non-prime moduli.  It also sets J(1, 1) = p-1, rather than the previous J(1, 1) = p+1 (which was the cause of wdj's error).\n\nNeeds review.",
    "created_at": "2008-08-11T03:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3637#issuecomment-25727",
    "user": "ncalexan"
}
```

Attachment

`3637-ekirkman-jacobi-sums.patch` adds an error (and a check=False) option preventing Jacobi sums with non-prime moduli.  It also sets J(1, 1) = p-1, rather than the previous J(1, 1) = p+1 (which was the cause of wdj's error).

Needs review.



---

archive/issue_comments_025728.json:
```json
{
    "body": "The patch 3637-ekirkman-jacobi-sums.patch replaces the older patch. It applies cleanly to sage-3.1.alpha0 and pases sage -testall. \n\nI give this a positive review. It neatly handles all the comments made by Alex and I. I also like the way the error message is worded for non-prime arguments.",
    "created_at": "2008-08-11T14:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3637#issuecomment-25728",
    "user": "wdj"
}
```

The patch 3637-ekirkman-jacobi-sums.patch replaces the older patch. It applies cleanly to sage-3.1.alpha0 and pases sage -testall. 

I give this a positive review. It neatly handles all the comments made by Alex and I. I also like the way the error message is worded for non-prime arguments.



---

archive/issue_comments_025729.json:
```json
{
    "body": "Merged in Sage 3.1.alpha2",
    "created_at": "2008-08-12T00:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3637#issuecomment-25729",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha2



---

archive/issue_comments_025730.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-12T00:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3637#issuecomment-25730",
    "user": "mabshoff"
}
```

Resolution: fixed
