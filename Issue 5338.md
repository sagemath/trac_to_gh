# Issue 5338: Sage 3.2.2: speed regression/infite loop for "K.<b> = QQ[a]"

archive/issues_005338.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @robertwb\n\nThe code below works instantly in Sage 3.2.1, but starting with Sage 3.2.2 it doesn't even finish the last command in 30 minutes CPU time:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage:     sage: x = var('x')\nsage:     sage: eqn =  x^3 + sqrt(2)*x + 5 == 0\nsage:     sage: a = solve(eqn, x)[0].rhs()\nsage:     sage: K.<b> = QQ[a]\n```\nCarl Witty suggests:\n| Sage Version 3.2.2, Release Date: 2008-12-18                       |\n| Type notebook() for the GUI, and license() for information.        |\n```\n[10:23am] mabs: So far it has eaten *4 minutes* of CPU time.\n[10:23am] cwitty: It looks like somebody changed the embedding \nsystem to use QQbar instead of wstein's algdep-of-numerical-value.\n```\nThis is likely related to the new embedding code in Sage 3.2.2, so I am CCing RobertWB.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5338\n\n",
    "created_at": "2009-02-22T18:50:31Z",
    "labels": [
        "component: algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Sage 3.2.2: speed regression/infite loop for \"K.<b> = QQ[a]\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5338",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: tbd

CC:  @robertwb

The code below works instantly in Sage 3.2.1, but starting with Sage 3.2.2 it doesn't even finish the last command in 30 minutes CPU time:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage:     sage: x = var('x')
sage:     sage: eqn =  x^3 + sqrt(2)*x + 5 == 0
sage:     sage: a = solve(eqn, x)[0].rhs()
sage:     sage: K.<b> = QQ[a]
```
Carl Witty suggests:
| Sage Version 3.2.2, Release Date: 2008-12-18                       |
| Type notebook() for the GUI, and license() for information.        |
```
[10:23am] mabs: So far it has eaten *4 minutes* of CPU time.
[10:23am] cwitty: It looks like somebody changed the embedding 
system to use QQbar instead of wstein's algdep-of-numerical-value.
```
This is likely related to the new embedding code in Sage 3.2.2, so I am CCing RobertWB.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5338





---

archive/issue_comments_041041.json:
```json
{
    "body": "You can still access my old (numeric) minpoly code via\n\n```\nsage: x = var('x')\nsage: eqn =  x^3 + sqrt(2)*x + 5 == 0\nsage: a = solve(eqn, x)[0].rhs()\nsage: a.minpoly(algorithm='numeric')\nx^6 + 10*x^3 - 2*x^2 + 25\n```\n\nHowever, for many cases this is much slower or fails completely.",
    "created_at": "2009-02-23T20:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41041",
    "user": "https://github.com/robertwb"
}
```

You can still access my old (numeric) minpoly code via

```
sage: x = var('x')
sage: eqn =  x^3 + sqrt(2)*x + 5 == 0
sage: a = solve(eqn, x)[0].rhs()
sage: a.minpoly(algorithm='numeric')
x^6 + 10*x^3 - 2*x^2 + 25
```

However, for many cases this is much slower or fails completely.



---

archive/issue_comments_041042.json:
```json
{
    "body": "Hmm, this is insanely slow (i.e. never finishes for me)\n\n```\nsage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)\nsage: time QQbar(b).minpoly()\n```",
    "created_at": "2009-02-23T21:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41042",
    "user": "https://github.com/robertwb"
}
```

Hmm, this is insanely slow (i.e. never finishes for me)

```
sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
sage: time QQbar(b).minpoly()
```



---

archive/issue_comments_041043.json:
```json
{
    "body": "Note that for now the doctest has been disabled to get the doctests to pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T19:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41043",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Note that for now the doctest has been disabled to get the doctests to pass.

Cheers,

Michael



---

archive/issue_comments_041044.json:
```json
{
    "body": "Replying to [comment:2 robertwb]:\n> Hmm, this is insanely slow (i.e. never finishes for me)\n> \n> \n> ```\n> sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)\n> sage: time QQbar(b).minpoly()\n> ```\n\n\nThe problem seems to be here:\n\n```\nsage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)\nsage: c = QQbar(b)\nsage: od = c._descr\nsage: od.exactify()    # doesn't seem to finish\n```",
    "created_at": "2009-06-02T08:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41044",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:2 robertwb]:
> Hmm, this is insanely slow (i.e. never finishes for me)
> 
> 
> ```
> sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
> sage: time QQbar(b).minpoly()
> ```


The problem seems to be here:

```
sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
sage: c = QQbar(b)
sage: od = c._descr
sage: od.exactify()    # doesn't seem to finish
```



---

archive/issue_comments_041045.json:
```json
{
    "body": "Replying to [comment:5 AlexGhitza]:\n> Replying to [comment:2 robertwb]:\n> > Hmm, this is insanely slow (i.e. never finishes for me)\n> > \n> > \n> > ```\n> > sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)\n> > sage: time QQbar(b).minpoly()\n> > ```\n\n> \n> The problem seems to be here:\n> \n> \n> ```\n> sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)\n> sage: c = QQbar(b)\n> sage: od = c._descr\n> sage: od.exactify()    # doesn't seem to finish\n> ```\n\n\nAs far as I can see, the latter is getting into an infinite loop.  If that is right, it's real bug and not just a new inefficiency.",
    "created_at": "2009-09-06T21:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41045",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:5 AlexGhitza]:
> Replying to [comment:2 robertwb]:
> > Hmm, this is insanely slow (i.e. never finishes for me)
> > 
> > 
> > ```
> > sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
> > sage: time QQbar(b).minpoly()
> > ```

> 
> The problem seems to be here:
> 
> 
> ```
> sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
> sage: c = QQbar(b)
> sage: od = c._descr
> sage: od.exactify()    # doesn't seem to finish
> ```


As far as I can see, the latter is getting into an infinite loop.  If that is right, it's real bug and not just a new inefficiency.



---

archive/issue_comments_041046.json:
```json
{
    "body": "It seems that `exactify` is not the culprit, it's just a bit slow:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)\nsage: c = QQbar(b)\nsage: od = c._descr\nsage: time od.exactify()\nCPU times: user 102.89 s, sys: 0.17 s, total: 103.06 s\nWall time: 117.04 s\n-13576/8180757*a^23 + 833411/13634595*a^20 - 6092092/13634595*a^17 + 2402147/4544865*a^14 + 16778234/4544865*a^11 - 5085581/504985*a^8 + 2414627/302991*a^5 - 1318781/504985*a^2 where a^24 - 36*a^21 + 240*a^18 - 144*a^15 - 2214*a^12 + 4320*a^9 - 2484*a^6 + 648*a^3 - 162 = 0 and a in -0.4328720060607604? + 0.7497563076715000?*I\n```",
    "created_at": "2009-11-10T20:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41046",
    "user": "https://github.com/aghitza"
}
```

It seems that `exactify` is not the culprit, it's just a bit slow:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
sage: c = QQbar(b)
sage: od = c._descr
sage: time od.exactify()
CPU times: user 102.89 s, sys: 0.17 s, total: 103.06 s
Wall time: 117.04 s
-13576/8180757*a^23 + 833411/13634595*a^20 - 6092092/13634595*a^17 + 2402147/4544865*a^14 + 16778234/4544865*a^11 - 5085581/504985*a^8 + 2414627/302991*a^5 - 1318781/504985*a^2 where a^24 - 36*a^21 + 240*a^18 - 144*a^15 - 2214*a^12 + 4320*a^9 - 2484*a^6 + 648*a^3 - 162 = 0 and a in -0.4328720060607604? + 0.7497563076715000?*I
```



---

archive/issue_comments_041047.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-19T21:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41047",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_041048.json:
```json
{
    "body": "I've attached a patch that reverses the order: it first tries the numerical algorithm, and if that fails, it then tries the algebraic algorithm.  This makes vastly more sense to me, since the numerical algorithm -- if it will fail -- is likely to fail in a reasonable amount of time, but the algebraic algorithm can succeed and take a huge amount of time.",
    "created_at": "2009-11-19T21:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41048",
    "user": "https://github.com/williamstein"
}
```

I've attached a patch that reverses the order: it first tries the numerical algorithm, and if that fails, it then tries the algebraic algorithm.  This makes vastly more sense to me, since the numerical algorithm -- if it will fail -- is likely to fail in a reasonable amount of time, but the algebraic algorithm can succeed and take a huge amount of time.



---

archive/issue_comments_041049.json:
```json
{
    "body": "```\nsage: b = sin(pi/5)\nsage: time sage.calculus.calculus.minpoly(b, algorithm='algebraic')\nCPU times: user 0.05 s, sys: 0.00 s, total: 0.05 s\nWall time: 0.05 s\nx^4 - 5/4*x^2 + 5/16\nsage: time sage.calculus.calculus.minpoly(b)\nTraceback (most recent call last):\n...\nNotImplementedError: Could not prove minimal polynomial x^4 - 5/4*x^2 + 5/16 (epsilon 0.00000000000000e-1)\n```\n\nWe need to wrap raising this error to not be raised if the algorithm is numeric... \n\nI remember doing it in this order because there were cases where the numeric algorithm was way slower, but at least the numeric one finishes in constant bounded time. \n\nI really feel there should be a quicker way of computing compositums than using QQbar.",
    "created_at": "2009-11-20T02:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41049",
    "user": "https://github.com/robertwb"
}
```

```
sage: b = sin(pi/5)
sage: time sage.calculus.calculus.minpoly(b, algorithm='algebraic')
CPU times: user 0.05 s, sys: 0.00 s, total: 0.05 s
Wall time: 0.05 s
x^4 - 5/4*x^2 + 5/16
sage: time sage.calculus.calculus.minpoly(b)
Traceback (most recent call last):
...
NotImplementedError: Could not prove minimal polynomial x^4 - 5/4*x^2 + 5/16 (epsilon 0.00000000000000e-1)
```

We need to wrap raising this error to not be raised if the algorithm is numeric... 

I remember doing it in this order because there were cases where the numeric algorithm was way slower, but at least the numeric one finishes in constant bounded time. 

I really feel there should be a quicker way of computing compositums than using QQbar.



---

archive/issue_comments_041050.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-20T02:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41050",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_041051.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-02T04:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41051",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041052.json:
```json
{
    "body": "Attachment [trac_5338.2.patch](tarball://root/attachments/some-uuid/ticket5338/trac_5338.2.patch) by @robertwb created at 2009-12-02 04:02:32",
    "created_at": "2009-12-02T04:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41052",
    "user": "https://github.com/robertwb"
}
```

Attachment [trac_5338.2.patch](tarball://root/attachments/some-uuid/ticket5338/trac_5338.2.patch) by @robertwb created at 2009-12-02 04:02:32



---

archive/issue_comments_041053.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-02T04:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41053",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_012447.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-02T08:44:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5338#event-12447"
}
```



---

archive/issue_comments_041054.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-02T08:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5338#issuecomment-41054",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
