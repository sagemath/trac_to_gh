# Issue 7368: Meta-ticket: Further work on isogenies and endomorphisms of elliptic curves

archive/issues_007368.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  weigandt @pjbruin sbesnier @yyyyx4\n\nKeywords: elliptic curves, isogeny, isogenies, endomorphism ring\n\nWorking on ticket #7096, I realised that there are many functionalities concerning morphisms of elliptic curves that are not implemented or implemented badly.\n\nSee also #6887, and #7262.\n\nHere is a wish-list:\n\n* General isogenies, not only cyclic ones should be implemented.\n  Possibly this could be done in a clever way, by having it \n  internally factored into cyclic isogenies. \u2192 #32744\n* Inseparable isogenies (e.g. Frobenii) should be possible too. \u2192 #33915 (See also #6413.)\n* One should be able to compose isogenies. \u2192 #16245, #32744\n* There should be an addition for isogenies with the same domain \n  and codomain.\n* There should be an endomorphism_ring for elliptic curves whose\n  elements are isogenies.\n* Similarly, automorphisms should give a group of isogenies.\n* Isogenies of large prime degree \u2113 can be computed in time O\u0303(\u221a\u2113) using https://velusqrt.isogeny.org/ \u2192 #34303\n* Is there a way of constructing a (not necessarily normalized)\n  isogeny knowing the degree and the domain and codomain?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7368\n\n",
    "created_at": "2009-11-01T14:26:11Z",
    "labels": [
        "component: elliptic curves"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "Meta-ticket: Further work on isogenies and endomorphisms of elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7368",
    "user": "https://github.com/categorie"
}
```
Assignee: @JohnCremona

CC:  weigandt @pjbruin sbesnier @yyyyx4

Keywords: elliptic curves, isogeny, isogenies, endomorphism ring

Working on ticket #7096, I realised that there are many functionalities concerning morphisms of elliptic curves that are not implemented or implemented badly.

See also #6887, and #7262.

Here is a wish-list:

* General isogenies, not only cyclic ones should be implemented.
  Possibly this could be done in a clever way, by having it 
  internally factored into cyclic isogenies. → #32744
* Inseparable isogenies (e.g. Frobenii) should be possible too. → #33915 (See also #6413.)
* One should be able to compose isogenies. → #16245, #32744
* There should be an addition for isogenies with the same domain 
  and codomain.
* There should be an endomorphism_ring for elliptic curves whose
  elements are isogenies.
* Similarly, automorphisms should give a group of isogenies.
* Isogenies of large prime degree ℓ can be computed in time Õ(√ℓ) using https://velusqrt.isogeny.org/ → #34303
* Is there a way of constructing a (not necessarily normalized)
  isogeny knowing the degree and the domain and codomain?


Issue created by migration from https://trac.sagemath.org/ticket/7368





---

archive/issue_comments_061635.json:
```json
{
    "body": "added",
    "created_at": "2015-10-20T18:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7368#issuecomment-61635",
    "user": "https://trac.sagemath.org/admin/accounts/users/adhalanay"
}
```

added
