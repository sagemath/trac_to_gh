# Issue 7368: Further work on isogenies and endomorphisms of elliptic curves

archive/issues_007368.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  weigandt pbruin sbesnier lorenz\n\nKeywords: elliptic curves, isogeny, isogenies, endomorphism ring\n\nWorking on ticket #7096, I realised that there are many functionalities concerning morphisms of elliptic curves that are not implemented or implemented badly.\n\nSee also #6887, and #7262.\n\nHere is a wish-list\n\n* General isogenies, not only cyclic ones should be implemented.\n  Possibly this could be done in a clever way, by having it \n  internally factored into cyclic isogenies.\n* Non seperable isogenies, i.e. Frobenii should be there too. See \n  also #6413.\n* One should be able to compose them\n* Is there a way of constructing a (not necessarily normalized)\n  isogeny knowing the degree and the domain and codomain ?\n* There should be an addition for isogenies with the same domain \n  and codomain.\n* There should be an endomorphism_ring for ellliptic curves whose\n  elements are isogenies.\n* Similar automorphisms should give a group of isogenies.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7368\n\n",
    "created_at": "2009-11-01T14:26:11Z",
    "labels": [
        "elliptic curves",
        "major",
        "enhancement"
    ],
    "title": "Further work on isogenies and endomorphisms of elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7368",
    "user": "wuthrich"
}
```
Assignee: cremona

CC:  weigandt pbruin sbesnier lorenz

Keywords: elliptic curves, isogeny, isogenies, endomorphism ring

Working on ticket #7096, I realised that there are many functionalities concerning morphisms of elliptic curves that are not implemented or implemented badly.

See also #6887, and #7262.

Here is a wish-list

* General isogenies, not only cyclic ones should be implemented.
  Possibly this could be done in a clever way, by having it 
  internally factored into cyclic isogenies.
* Non seperable isogenies, i.e. Frobenii should be there too. See 
  also #6413.
* One should be able to compose them
* Is there a way of constructing a (not necessarily normalized)
  isogeny knowing the degree and the domain and codomain ?
* There should be an addition for isogenies with the same domain 
  and codomain.
* There should be an endomorphism_ring for ellliptic curves whose
  elements are isogenies.
* Similar automorphisms should give a group of isogenies.

Issue created by migration from https://trac.sagemath.org/ticket/7368





---

archive/issue_comments_061749.json:
```json
{
    "body": "added",
    "created_at": "2015-10-20T18:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7368#issuecomment-61749",
    "user": "adhalanay"
}
```

added
