# Issue 8137: Thomas R. Nicely's Hardy-Littlewood logarithmic integral approximations to counts of prime constellations

archive/issues_008137.json:
```json
{
    "body": "Assignee: Kevin Stueve\n\nCC:  @nexttime\n\nGet Thomas R. Nicely's code for approximating the counts of twin primes and other primes into Sage.\n\nThe code can be found at http://www.trnicely.net/.\n\nSage already has a Li implementation, so all that needs to be added to Sage is code for the twin primes, prime triplets, and prime quadruplets.  However, Sage's default Li implementation uses direct numerical integration.  Maybe this should be switched out for an equivalent (and faster) series implementation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8137\n\n",
    "created_at": "2010-01-31T07:42:26Z",
    "labels": [
        "component: number theory"
    ],
    "title": "Thomas R. Nicely's Hardy-Littlewood logarithmic integral approximations to counts of prime constellations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8137",
    "user": "https://trac.sagemath.org/admin/accounts/users/kevin.stueve"
}
```
Assignee: Kevin Stueve

CC:  @nexttime

Get Thomas R. Nicely's code for approximating the counts of twin primes and other primes into Sage.

The code can be found at http://www.trnicely.net/.

Sage already has a Li implementation, so all that needs to be added to Sage is code for the twin primes, prime triplets, and prime quadruplets.  However, Sage's default Li implementation uses direct numerical integration.  Maybe this should be switched out for an equivalent (and faster) series implementation.

Issue created by migration from https://trac.sagemath.org/ticket/8137





---

archive/issue_comments_071435.json:
```json
{
    "body": "Take note of Remark 4 in Introduction to twin primes and Brun\u2019s constant computation, by Pascal Sebah and Xavier Gourdon at numbers.computation.free.fr/Constants/constants.html (July 30, 2002)\n\n\"Remark 4 The function Li2 (n) occuring in (1) may be related to the logarithmic integral Li(n) by the trivial relation\n\n                      Li2(n) = Li(n) +   2 / log(2) - n / log(n).\"\n\nKevin Stueve",
    "created_at": "2010-01-31T18:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8137#issuecomment-71435",
    "user": "https://trac.sagemath.org/admin/accounts/users/kevin.stueve"
}
```

Take note of Remark 4 in Introduction to twin primes and Brun’s constant computation, by Pascal Sebah and Xavier Gourdon at numbers.computation.free.fr/Constants/constants.html (July 30, 2002)

"Remark 4 The function Li2 (n) occuring in (1) may be related to the logarithmic integral Li(n) by the trivial relation

                      Li2(n) = Li(n) +   2 / log(2) - n / log(n)."

Kevin Stueve



---

archive/issue_comments_071436.json:
```json
{
    "body": "Replying to [comment:1 kevin.stueve]:\n> Take note of Remark 4 in Introduction to twin primes and Brun\u2019s constant computation, by Pascal Sebah and Xavier Gourdon at http://numbers.computation.free.fr/Constants/constants.html (July 30, 2002)\n\n\nThe specific web page http://numbers.computation.free.fr/Constants/Primes/twin.html is also available in PDF: http://numbers.computation.free.fr/Constants/Primes/twin.pdf, the mentioned remark is on page 5.",
    "created_at": "2010-02-01T21:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8137#issuecomment-71436",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:1 kevin.stueve]:
> Take note of Remark 4 in Introduction to twin primes and Brun’s constant computation, by Pascal Sebah and Xavier Gourdon at http://numbers.computation.free.fr/Constants/constants.html (July 30, 2002)


The specific web page http://numbers.computation.free.fr/Constants/Primes/twin.html is also available in PDF: http://numbers.computation.free.fr/Constants/Primes/twin.pdf, the mentioned remark is on page 5.
