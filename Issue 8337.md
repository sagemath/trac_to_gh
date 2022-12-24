# Issue 8337: factorization of multivariate polynomials is terribly slow

archive/issues_008337.json:
```json
{
    "body": "Assignee: malb\n\nFrom http://groups.google.com/group/sage-support/browse_thread/thread/72fbc6d6f5a7d746#, with sage 4.3.3:\n\n```\nsage: var('E1, E2, E4, E5, E10, E20'); \nsage: var( 'q' ); \nsage: t=(E20^16*E5^8*q^4*E2^24 + (-E20^16*E5^8*q^4*E4^8*E1^16 + (-E10^24 + E20^8*E5^16)*E4^16*E1^8)) \nsage: factor(t)\n```\n\ndoes not answer in reasonable time (a few seconds).\n\nMaple 13 answers in less than a second (and says the polynomial\nis irreducible).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8337\n\n",
    "created_at": "2010-02-23T18:18:55Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "factorization of multivariate polynomials is terribly slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8337",
    "user": "zimmerma"
}
```
Assignee: malb

From http://groups.google.com/group/sage-support/browse_thread/thread/72fbc6d6f5a7d746#, with sage 4.3.3:

```
sage: var('E1, E2, E4, E5, E10, E20'); 
sage: var( 'q' ); 
sage: t=(E20^16*E5^8*q^4*E2^24 + (-E20^16*E5^8*q^4*E4^8*E1^16 + (-E10^24 + E20^8*E5^16)*E4^16*E1^8)) 
sage: factor(t)
```

does not answer in reasonable time (a few seconds).

Maple 13 answers in less than a second (and says the polynomial
is irreducible).

Issue created by migration from https://trac.sagemath.org/ticket/8337





---

archive/issue_comments_074436.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2013-08-23T15:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8337#issuecomment-74436",
    "user": "zimmerma"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_074437.json:
```json
{
    "body": "seems to be fixed in Sage 5.11:\n\n```\nsage: %time factor(t)\nCPU times: user 0.05 s, sys: 0.00 s, total: 0.05 s\nWall time: 0.09 s\nE2^24*E20^16*E5^8*q^4 - E1^16*E20^16*E4^8*E5^8*q^4 - E1^8*E10^24*E4^16 + E1^8*E20^8*E4^16*E5^16\n```\n\nShould I add a doctest for that? If yes, how to check the computation is fast enough?\n\nPaul",
    "created_at": "2013-08-23T15:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8337#issuecomment-74437",
    "user": "zimmerma"
}
```

seems to be fixed in Sage 5.11:

```
sage: %time factor(t)
CPU times: user 0.05 s, sys: 0.00 s, total: 0.05 s
Wall time: 0.09 s
E2^24*E20^16*E5^8*q^4 - E1^16*E20^16*E4^8*E5^8*q^4 - E1^8*E10^24*E4^16 + E1^8*E20^8*E4^16*E5^16
```

Should I add a doctest for that? If yes, how to check the computation is fast enough?

Paul



---

archive/issue_comments_074438.json:
```json
{
    "body": "Changing component from commutative algebra to performance.",
    "created_at": "2013-08-24T08:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8337#issuecomment-74438",
    "user": "jdemeyer"
}
```

Changing component from commutative algebra to performance.



---

archive/issue_comments_074439.json:
```json
{
    "body": "There currently isn't really a way in Sage to test timings. There has been a lot of thought about this, but it's hard to do right.\n\nSo the most reasonable thing to do is to close this ticket.",
    "created_at": "2013-08-24T08:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8337#issuecomment-74439",
    "user": "jdemeyer"
}
```

There currently isn't really a way in Sage to test timings. There has been a lot of thought about this, but it's hard to do right.

So the most reasonable thing to do is to close this ticket.



---

archive/issue_comments_074440.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2013-08-24T08:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8337#issuecomment-74440",
    "user": "jdemeyer"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_074441.json:
```json
{
    "body": "> So the most reasonable thing to do is to close this ticket. \n\nok, fine to me.\n\nPaul",
    "created_at": "2013-08-24T08:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8337#issuecomment-74441",
    "user": "zimmerma"
}
```

> So the most reasonable thing to do is to close this ticket. 

ok, fine to me.

Paul



---

archive/issue_comments_074442.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-08-30T08:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8337#issuecomment-74442",
    "user": "jdemeyer"
}
```

Resolution: worksforme
