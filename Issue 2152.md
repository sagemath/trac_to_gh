# Issue 2152: ticket: multivariate polynomial factorization over GF(p) in "three free world" is a total frickin' *EMBARRASSMENT*

archive/issues_002152.json:
```json
{
    "body": "Assignee: malb\n\n\n```\n\nteragon:~ was$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: abelian_rewrite\nsage: R.<x,y,z> = GF(5)[]\nsage: f = 2*y^9*z + 2*x^2*y^5*z^3 - y^9 - 2*x^4*z^2\nsage: g = -2*x^2*y^9*z^4 - 2*x*y^3*z^11 - x^3*y^8*z - 2*x*z^8\nsage: h = f*g\nsage: time h.factor()\n[hit control C after a few minutes!!]\n| SAGE Version 2.10.1, Release Date: 2008-02-02                      |\n| Type notebook() for the GUI, and license() for information.        |\nWTF?!  Give me a break!\nI mean this is pitiful, since in contrast, Magma takes 0.01 seconds.\n\nsage: t = magma.cputime(); k.Factorization(); magma.cputime(t)\n[\n<z, 1>,\n<x, 1>,\n<y^9*z + x^2*y^5*z^3 + 2*y^9 + 4*x^4*z^2, 1>,\n<x*y^9*z^3 + y^3*z^10 + 3*x^2*y^8 + z^7, 1>\n]\n0.01\n\n\nSame behavior on any random reducible input!\n\n------\n\nHere's an old email Allan Steel sent me nearly 8 years ago about\nexactly this sort of thing, where he calls Axioms performance on such\nproblems \"some kind of a record!  (For absurdity?)\".  He could\nhonestly say the same thing about Sage today (!) -- of course I really\nmean Singular since that is what is doing the real work. \n\n-------------------------------------\n\n \nI found this so funny that I had to pass it on to everyone.\n \nPaul Zimmermann keeps a web page with polynomial factorization challenges\nand records at:\n \n    http://www.loria.fr/~zimmerma/mupad/\n \nHere's the latest addition to it, which Paul Zimmermann inserted only\nyesterday (near the end of the screen):\n \n    _Here_ is a degree 35 polynomial with 172 terms over F_5[x,y,z] to factor\n    (from MUG, Nivaldo Nunes de Medeiros Junior , January 1996). John\n    Abbott managed to factor it using Axiom in July 2000 on a 200MHz\n    Pentium in about 145000 seconds. Magma V2.6-2 factors it in 0.3 second\n    on a PII-400 under Linux.\n \nI like the word \"managed\" -- sounds like a lot of effort!  In a mail\nfrom John Abbot passed on to us, he actually says that the Axiom\nmachine was 150MHz, so I think that the 200MHz above is wrong.  But\nallowing for Magma on a 400MHz machine versus Axiom on a 150MHz\nmachine, this gives a factor of:\n \n        145000 / 0.3 / (400/150) = 181250\n \nThis is somewhat ridiculous!   The Magma algorithm here is not an\nextremely smart algorithm, and I'm surprised to see how amazingly slow\nAxiom is for this!\n \nThe web page has the original poly and the Magma code too.  In the mail\npassed on to us, Paul Zimmermann said that he only discovered yesterday\nthat Magma takes less than a second when he tried it!\n \nI think this one must be some kind of a record!  (For absurdity?)\n \nAllan\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2152\n\n",
    "created_at": "2008-02-13T21:15:36Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "title": "ticket: multivariate polynomial factorization over GF(p) in \"three free world\" is a total frickin' *EMBARRASSMENT*",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2152",
    "user": "was"
}
```
Assignee: malb


```

teragon:~ was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: abelian_rewrite
sage: R.<x,y,z> = GF(5)[]
sage: f = 2*y^9*z + 2*x^2*y^5*z^3 - y^9 - 2*x^4*z^2
sage: g = -2*x^2*y^9*z^4 - 2*x*y^3*z^11 - x^3*y^8*z - 2*x*z^8
sage: h = f*g
sage: time h.factor()
[hit control C after a few minutes!!]
| SAGE Version 2.10.1, Release Date: 2008-02-02                      |
| Type notebook() for the GUI, and license() for information.        |
WTF?!  Give me a break!
I mean this is pitiful, since in contrast, Magma takes 0.01 seconds.

sage: t = magma.cputime(); k.Factorization(); magma.cputime(t)
[
<z, 1>,
<x, 1>,
<y^9*z + x^2*y^5*z^3 + 2*y^9 + 4*x^4*z^2, 1>,
<x*y^9*z^3 + y^3*z^10 + 3*x^2*y^8 + z^7, 1>
]
0.01


Same behavior on any random reducible input!

------

Here's an old email Allan Steel sent me nearly 8 years ago about
exactly this sort of thing, where he calls Axioms performance on such
problems "some kind of a record!  (For absurdity?)".  He could
honestly say the same thing about Sage today (!) -- of course I really
mean Singular since that is what is doing the real work. 

-------------------------------------

 
I found this so funny that I had to pass it on to everyone.
 
Paul Zimmermann keeps a web page with polynomial factorization challenges
and records at:
 
    http://www.loria.fr/~zimmerma/mupad/
 
Here's the latest addition to it, which Paul Zimmermann inserted only
yesterday (near the end of the screen):
 
    _Here_ is a degree 35 polynomial with 172 terms over F_5[x,y,z] to factor
    (from MUG, Nivaldo Nunes de Medeiros Junior , January 1996). John
    Abbott managed to factor it using Axiom in July 2000 on a 200MHz
    Pentium in about 145000 seconds. Magma V2.6-2 factors it in 0.3 second
    on a PII-400 under Linux.
 
I like the word "managed" -- sounds like a lot of effort!  In a mail
from John Abbot passed on to us, he actually says that the Axiom
machine was 150MHz, so I think that the 200MHz above is wrong.  But
allowing for Magma on a 400MHz machine versus Axiom on a 150MHz
machine, this gives a factor of:
 
        145000 / 0.3 / (400/150) = 181250
 
This is somewhat ridiculous!   The Magma algorithm here is not an
extremely smart algorithm, and I'm surprised to see how amazingly slow
Axiom is for this!
 
The web page has the original poly and the Magma code too.  In the mail
passed on to us, Paul Zimmermann said that he only discovered yesterday
that Magma takes less than a second when he tried it!
 
I think this one must be some kind of a record!  (For absurdity?)
 
Allan
```



Issue created by migration from https://trac.sagemath.org/ticket/2152





---

archive/issue_comments_014125.json:
```json
{
    "body": "This looks very relevant:\n   http://portal.acm.org/citation.cfm?id=780506.780532",
    "created_at": "2008-02-13T21:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2152#issuecomment-14125",
    "user": "was"
}
```

This looks very relevant:
   http://portal.acm.org/citation.cfm?id=780506.780532



---

archive/issue_comments_014126.json:
```json
{
    "body": "I tried this again today and:\n\n\n```\nbsd:sage-3.2.alpha0 was$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.2.alpha0, Release Date: 2008-10-20                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: R.<x,y,z> = GF(5)[]\nsage: sage: f = 2*y^9*z + 2*x^2*y^5*z^3 - y^9 - 2*x^4*z^2\nsage: sage: g = -2*x^2*y^9*z^4 - 2*x*y^3*z^11 - x^3*y^8*z - 2*x*z^8\nsage: sage: h = f*g\nsage: sage: time h.factor()\nCPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s\nWall time: 0.08 s\nz * x * (y^9*z + x^2*y^5*z^3 + 2*y^9 - x^4*z^2) * (x*y^9*z^3 + y^3*z^10 - 2*x^2*y^8 + z^7)\nsage: sage: time h.factor()\n[... wait for minutes!!!!...]\n```\n\n\nSo, again I say - WTF?  \n\nWilliam",
    "created_at": "2008-10-30T17:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2152#issuecomment-14126",
    "user": "was"
}
```

I tried this again today and:


```
bsd:sage-3.2.alpha0 was$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.2.alpha0, Release Date: 2008-10-20                  |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: R.<x,y,z> = GF(5)[]
sage: sage: f = 2*y^9*z + 2*x^2*y^5*z^3 - y^9 - 2*x^4*z^2
sage: sage: g = -2*x^2*y^9*z^4 - 2*x*y^3*z^11 - x^3*y^8*z - 2*x*z^8
sage: sage: h = f*g
sage: sage: time h.factor()
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.08 s
z * x * (y^9*z + x^2*y^5*z^3 + 2*y^9 - x^4*z^2) * (x*y^9*z^3 + y^3*z^10 - 2*x^2*y^8 + z^7)
sage: sage: time h.factor()
[... wait for minutes!!!!...]
```


So, again I say - WTF?  

William



---

archive/issue_comments_014127.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-10-30T17:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2152#issuecomment-14127",
    "user": "was"
}
```

Resolution: duplicate



---

archive/issue_comments_014128.json:
```json
{
    "body": "This is a dup of #1343",
    "created_at": "2008-10-30T17:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2152#issuecomment-14128",
    "user": "was"
}
```

This is a dup of #1343
