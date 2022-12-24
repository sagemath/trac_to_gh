# Issue 2498: PARI's is_irreducible being used inappropriately

archive/issues_002498.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  malb@informatik.uni-bremen.de\n\nPARI's polynomial irreducibility and factoring routines are being used incorrectly for certain base rings. Here is an example:\n\n\n```\nsage: R.<x> = PolynomialRing(Integers(35))\nsage: f = (x^2+2*x+2)*(x^2+3*x+9)\nsage: f\nx^4 + 5*x^3 + 17*x^2 + 24*x + 18\nsage: factor(f)\nx^4 + 5*x^3 + 17*x^2 + 24*x + 18\nsage: f.is_irreducible()\nTrue\n```\n\n\nThe PARI documentation for `polisirreducible` says: \"Irreducibility is checked over the smallest base field over which pol seems to be defined\", whatever that means.\n\nWe should put in some checking to make sure this crazy behaviour doesn't happen, or at the very least put in big fat warnings in the documentation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2498\n\n",
    "created_at": "2008-03-12T16:24:48Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "PARI's is_irreducible being used inappropriately",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2498",
    "user": "dmharvey"
}
```
Assignee: somebody

CC:  malb@informatik.uni-bremen.de

PARI's polynomial irreducibility and factoring routines are being used incorrectly for certain base rings. Here is an example:


```
sage: R.<x> = PolynomialRing(Integers(35))
sage: f = (x^2+2*x+2)*(x^2+3*x+9)
sage: f
x^4 + 5*x^3 + 17*x^2 + 24*x + 18
sage: factor(f)
x^4 + 5*x^3 + 17*x^2 + 24*x + 18
sage: f.is_irreducible()
True
```


The PARI documentation for `polisirreducible` says: "Irreducibility is checked over the smallest base field over which pol seems to be defined", whatever that means.

We should put in some checking to make sure this crazy behaviour doesn't happen, or at the very least put in big fat warnings in the documentation.


Issue created by migration from https://trac.sagemath.org/ticket/2498





---

archive/issue_comments_016931.json:
```json
{
    "body": "> We should put in some checking to make sure this crazy behaviour \n> doesn't happen, \n\n+1 -- definitely. \n\n> or at the very least put in big fat warnings \n> in the documentation.\n\n-1 -- let's just not allow this crap.\n\n> \"Irreducibility is checked over the smallest base field over which pol seems to be defined\"\n\nThat's the sort of ick that I don't like about PARI.",
    "created_at": "2008-03-12T16:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2498#issuecomment-16931",
    "user": "was"
}
```

> We should put in some checking to make sure this crazy behaviour 
> doesn't happen, 

+1 -- definitely. 

> or at the very least put in big fat warnings 
> in the documentation.

-1 -- let's just not allow this crap.

> "Irreducibility is checked over the smallest base field over which pol seems to be defined"

That's the sort of ick that I don't like about PARI.



---

archive/issue_comments_016932.json:
```json
{
    "body": "Just checking that I understand what we want to see here: suppose we are dealing with a polynomial over Z/nZ with composite n.  Then we want that both factor() and is_irreducible() throw a NotImplementedError instead of calling pari and getting an incorrect answer.\n\nI wanted to make sure before I went and changed this.",
    "created_at": "2008-03-21T23:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2498#issuecomment-16932",
    "user": "AlexGhitza"
}
```

Just checking that I understand what we want to see here: suppose we are dealing with a polynomial over Z/nZ with composite n.  Then we want that both factor() and is_irreducible() throw a NotImplementedError instead of calling pari and getting an incorrect answer.

I wanted to make sure before I went and changed this.



---

archive/issue_comments_016933.json:
```json
{
    "body": "When n is composite in the sense that it has more than one prime factor, I agree with throwing NotImplementedErrror.  When n is a prime power we could try to be more clever (if f mod p has a factorization into coprime factors then this would lift uniquely to a factorization over Z/nZ, for example) but for now I suggest again making this NotImplemented.",
    "created_at": "2008-03-22T18:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2498#issuecomment-16933",
    "user": "cremona"
}
```

When n is composite in the sense that it has more than one prime factor, I agree with throwing NotImplementedErrror.  When n is a prime power we could try to be more clever (if f mod p has a factorization into coprime factors then this would lift uniquely to a factorization over Z/nZ, for example) but for now I suggest again making this NotImplemented.



---

archive/issue_comments_016934.json:
```json
{
    "body": "Attachment [2498_factor_pari.patch](tarball://root/attachments/some-uuid/ticket2498/2498_factor_pari.patch) by AlexGhitza created at 2008-03-22 19:54:47\n\nYes, it should be possible to do something smart here.  For now, I'm just making factor() and is_irreducible() throw NotImplementedError so we don't get wrong answers.\n\nSee the attached patch.",
    "created_at": "2008-03-22T19:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2498#issuecomment-16934",
    "user": "AlexGhitza"
}
```

Attachment [2498_factor_pari.patch](tarball://root/attachments/some-uuid/ticket2498/2498_factor_pari.patch) by AlexGhitza created at 2008-03-22 19:54:47

Yes, it should be possible to do something smart here.  For now, I'm just making factor() and is_irreducible() throw NotImplementedError so we don't get wrong answers.

See the attached patch.



---

archive/issue_comments_016935.json:
```json
{
    "body": "Instead of explicitly mentioning Z/nZ (for composite n) as not implemented, would it not be more useful to list which rings this _is_ implemented for?  (Fields, Z, anything else?)",
    "created_at": "2008-03-22T20:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2498#issuecomment-16935",
    "user": "cremona"
}
```

Instead of explicitly mentioning Z/nZ (for composite n) as not implemented, would it not be more useful to list which rings this _is_ implemented for?  (Fields, Z, anything else?)



---

archive/issue_comments_016936.json:
```json
{
    "body": "> Instead of explicitly mentioning Z/nZ (for composite n) as \n> not implemented, would it not be more useful to list which \n> rings this _is_ implemented for? (Fields, Z, anything else?)\n\nIt might be more useful now, but it's bound to become out of\ndate, in which case such a list would be wrong, and could turn\nout to be way *less* useful than nothing.\n\nWilliam",
    "created_at": "2008-03-22T20:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2498#issuecomment-16936",
    "user": "was"
}
```

> Instead of explicitly mentioning Z/nZ (for composite n) as 
> not implemented, would it not be more useful to list which 
> rings this _is_ implemented for? (Fields, Z, anything else?)

It might be more useful now, but it's bound to become out of
date, in which case such a list would be wrong, and could turn
out to be way *less* useful than nothing.

William



---

archive/issue_comments_016937.json:
```json
{
    "body": "Replying to [comment:8 was]:\n> > Instead of explicitly mentioning Z/nZ (for composite n) as \n> > not implemented, would it not be more useful to list which \n> > rings this _is_ implemented for? (Fields, Z, anything else?)\n> \n> It might be more useful now, but it's bound to become out of\n> date, in which case such a list would be wrong, and could turn\n> out to be way *less* useful than nothing.\n> \n> William\n\nOK then -- the patch gets a thumbs up from me!",
    "created_at": "2008-03-22T22:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2498#issuecomment-16937",
    "user": "cremona"
}
```

Replying to [comment:8 was]:
> > Instead of explicitly mentioning Z/nZ (for composite n) as 
> > not implemented, would it not be more useful to list which 
> > rings this _is_ implemented for? (Fields, Z, anything else?)
> 
> It might be more useful now, but it's bound to become out of
> date, in which case such a list would be wrong, and could turn
> out to be way *less* useful than nothing.
> 
> William

OK then -- the patch gets a thumbs up from me!



---

archive/issue_comments_016938.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-23T20:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2498#issuecomment-16938",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_016939.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-23T20:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2498#issuecomment-16939",
    "user": "mabshoff"
}
```

Resolution: fixed
