# Issue 8441: Coleman-Gross local height pairing on hyperelliptic curves

archive/issues_008441.json:
```json
{
    "body": "Assignee: was\n\nCC:  kedlaya\n\nKeywords: heights, Coleman integration, hyperelliptic curves\n\nCurrently, a work in progress (lots of doctests need to be written and internal print statements removed; the code itself will be cleaned up over the next few weeks), but the main function, which computes the Coleman-Gross local height pairing at p for hyperelliptic curves, does the following:\n\n(This example is computing h_7(D_1, D_2) and h_7(D_2, D_1), for D_1 = (P) - (Q) and D_2 = (Pprime)-(Qprime), in the notation of R. Coleman and B. Gross, p-adic heights on curves, Algebraic Number Theory, 1989, pp-73-81.)\n\n\n```\n        sage: R.<x> = QQ[]                                                                                \n        sage: H = HyperellipticCurve(x*(x-1)*(x+9))                                                       \n        sage: K = Qp(7,10)                                                                                \n        sage: HK = H.change_ring(K)                                                                       \n        sage: P = HK(9,36)                                                                                \n        sage: Q = HK.teichmuller(P)                                                                       \n        sage: Pprime = HK(-4,10)                                                                          \n        sage: Qprime = HK.teichmuller(Pprime)                                                             \n        sage: HK.height([(1,P),(-1,Q)],[(1,Pprime),(-1,Qprime)],10)                                       \n        2*7^2 + 5*7^3 + 7^4 + 7^5 + 2*7^6 + 3*7^7 + 7^8 + 3*7^9 + O(7^10)                                 \n        sage: HK.height([(1,Pprime),(-1,Qprime)],[(1,P),(-1,Q)],10)                                       \n        2*7^2 + 5*7^3 + 7^4 + 7^5 + 2*7^6 + 3*7^7 + 7^8 + 3*7^9 + O(7^10)      \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8441\n\n",
    "created_at": "2010-03-05T01:26:33Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "Coleman-Gross local height pairing on hyperelliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8441",
    "user": "jen"
}
```
Assignee: was

CC:  kedlaya

Keywords: heights, Coleman integration, hyperelliptic curves

Currently, a work in progress (lots of doctests need to be written and internal print statements removed; the code itself will be cleaned up over the next few weeks), but the main function, which computes the Coleman-Gross local height pairing at p for hyperelliptic curves, does the following:

(This example is computing h_7(D_1, D_2) and h_7(D_2, D_1), for D_1 = (P) - (Q) and D_2 = (Pprime)-(Qprime), in the notation of R. Coleman and B. Gross, p-adic heights on curves, Algebraic Number Theory, 1989, pp-73-81.)


```
        sage: R.<x> = QQ[]                                                                                
        sage: H = HyperellipticCurve(x*(x-1)*(x+9))                                                       
        sage: K = Qp(7,10)                                                                                
        sage: HK = H.change_ring(K)                                                                       
        sage: P = HK(9,36)                                                                                
        sage: Q = HK.teichmuller(P)                                                                       
        sage: Pprime = HK(-4,10)                                                                          
        sage: Qprime = HK.teichmuller(Pprime)                                                             
        sage: HK.height([(1,P),(-1,Q)],[(1,Pprime),(-1,Qprime)],10)                                       
        2*7^2 + 5*7^3 + 7^4 + 7^5 + 2*7^6 + 3*7^7 + 7^8 + 3*7^9 + O(7^10)                                 
        sage: HK.height([(1,Pprime),(-1,Qprime)],[(1,P),(-1,Q)],10)                                       
        2*7^2 + 5*7^3 + 7^4 + 7^5 + 2*7^6 + 3*7^7 + 7^8 + 3*7^9 + O(7^10)      
```


Issue created by migration from https://trac.sagemath.org/ticket/8441





---

archive/issue_comments_075791.json:
```json
{
    "body": "a first attempt at collecting all of the local heights code",
    "created_at": "2010-03-05T01:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75791",
    "user": "jen"
}
```

a first attempt at collecting all of the local heights code



---

archive/issue_comments_075792.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-03-05T01:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75792",
    "user": "jen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_075793.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-05T01:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75793",
    "user": "jen"
}
```

Attachment



---

archive/issue_comments_075794.json:
```json
{
    "body": "here is a tentative of rebasing on 5.12.beta3\n\n* the part in ``hyperelliptic_generic`` is rather clean and could even go in a separate ticket\n\n* the part in ``hyperelliptic_padic_field`` needs a lot of work and care",
    "created_at": "2013-08-29T09:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75794",
    "user": "chapoton"
}
```

here is a tentative of rebasing on 5.12.beta3

* the part in ``hyperelliptic_generic`` is rather clean and could even go in a separate ticket

* the part in ``hyperelliptic_padic_field`` needs a lot of work and care



---

archive/issue_comments_075795.json:
```json
{
    "body": "apply only trac_8441_rebased.patch\u200b",
    "created_at": "2013-08-29T10:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75795",
    "user": "chapoton"
}
```

apply only trac_8441_rebased.patch​



---

archive/issue_comments_075796.json:
```json
{
    "body": "apply only trac_8441_rebased.patch",
    "created_at": "2013-08-29T16:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75796",
    "user": "chapoton"
}
```

apply only trac_8441_rebased.patch



---

archive/issue_comments_075797.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-10-04T21:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75797",
    "user": "chapoton"
}
```

Attachment



---

archive/issue_comments_075798.json:
```json
{
    "body": "apply only trac_8441_rebased.patch",
    "created_at": "2013-10-15T18:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75798",
    "user": "chapoton"
}
```

apply only trac_8441_rebased.patch



---

archive/issue_comments_075799.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-09T19:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75799",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_075800.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-06-23T19:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75800",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075801.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-24T20:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75801",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075802.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-07-27T11:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75802",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075803.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-06T20:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75803",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075804.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-02-26T10:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75804",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075805.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-27T17:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75805",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075806.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-29T11:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75806",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075807.json:
```json
{
    "body": "So is there any mathematical obstruction to giving this a positive review? (I haven't checked all the doctest formatting, so maybe that is still an issue.)",
    "created_at": "2016-08-11T15:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75807",
    "user": "kedlaya"
}
```

So is there any mathematical obstruction to giving this a positive review? (I haven't checked all the doctest formatting, so maybe that is still an issue.)



---

archive/issue_comments_075808.json:
```json
{
    "body": "To answer my own question: it looks like there are still some missing doctests on intermediate functions, and some comments in the code that suggest points that still need to be addressed (but I didn't look more closely at the code to evaluate the suggestions).\n\nWould it make to separate out the part of this code which is actually done into a ticket that can be reviewed and merged right away (and make that a dependency for this ticket)?",
    "created_at": "2016-08-17T15:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75808",
    "user": "kedlaya"
}
```

To answer my own question: it looks like there are still some missing doctests on intermediate functions, and some comments in the code that suggest points that still need to be addressed (but I didn't look more closely at the code to evaluate the suggestions).

Would it make to separate out the part of this code which is actually done into a ticket that can be reviewed and merged right away (and make that a dependency for this ticket)?



---

archive/issue_comments_075809.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-08-17T18:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75809",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075810.json:
```json
{
    "body": "One could easily split to another ticket the simple (but not so interesting) changes in the file `hyperelliptic_generic`.",
    "created_at": "2016-08-17T19:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75810",
    "user": "chapoton"
}
```

One could easily split to another ticket the simple (but not so interesting) changes in the file `hyperelliptic_generic`.



---

archive/issue_comments_075811.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. Last 10 new commits:",
    "created_at": "2016-08-19T00:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8441#issuecomment-75811",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:
