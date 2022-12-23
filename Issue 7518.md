# Issue 7518: flint -- hangs computing certain degenerate case xgcd's

archive/issues_007518.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  david.kirkby@onetel.net\n\nObserve:\n\n\n```\nsage: Q.<x> = ZZ[]\nsage: gcd(Q(2),x^2)\n1\nsage: xgcd(Q(2),x^2)\n<hang forever!>\n```\n\n\nwhereas\n\n\n```\nsage: Q.<x> = PolynomialRing(ZZ,implementation=\"NTL\")\nsage: type(x)\n<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>\nsage: gcd(Q(2),x^2)\n1\nsage: xgcd(Q(2),x^2)\n(4, 2, 0)\n```\n\n\nworks fine.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7518\n\n",
    "created_at": "2009-11-23T07:00:21Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "flint -- hangs computing certain degenerate case xgcd's",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7518",
    "user": "was"
}
```
Assignee: AlexGhitza

CC:  david.kirkby@onetel.net

Observe:


```
sage: Q.<x> = ZZ[]
sage: gcd(Q(2),x^2)
1
sage: xgcd(Q(2),x^2)
<hang forever!>
```


whereas


```
sage: Q.<x> = PolynomialRing(ZZ,implementation="NTL")
sage: type(x)
<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>
sage: gcd(Q(2),x^2)
1
sage: xgcd(Q(2),x^2)
(4, 2, 0)
```


works fine.


Issue created by migration from https://trac.sagemath.org/ticket/7518





---

archive/issue_comments_063683.json:
```json
{
    "body": "The 'Report Upstream:' field is set to N/A. Is that appropiate, or should it be reported to the flint developers?",
    "created_at": "2009-12-24T03:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63683",
    "user": "drkirkby"
}
```

The 'Report Upstream:' field is set to N/A. Is that appropiate, or should it be reported to the flint developers?



---

archive/issue_comments_063684.json:
```json
{
    "body": "That Report Upstream button is *annoying*.  I just reported it upstream, and the only option I can select to change from \"Not yet reported\" is \"Reported; little feedback\".  Huh?   I want to change it \"Reported upstream\".  Of course there is no feedback, since I reported it seconds ago.",
    "created_at": "2009-12-24T20:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63684",
    "user": "was"
}
```

That Report Upstream button is *annoying*.  I just reported it upstream, and the only option I can select to change from "Not yet reported" is "Reported; little feedback".  Huh?   I want to change it "Reported upstream".  Of course there is no feedback, since I reported it seconds ago.



---

archive/issue_comments_063685.json:
```json
{
    "body": "\n```\nfrom\tBill Hart <goodwillhart@googlemail.com>\nto\tWilliam Stein <wstein@gmail.com>\ndate\tThu, Dec 24, 2009 at 5:23 PM\nsubject\tRe: flint bug maybe\n\t\nhide details 5:23 PM (7 hours ago)\n\t\nYes, it is a (fairly trivial) flint bug. I'll try and issue a fix later today.\n\nThanks.\n\nBill.\n```\n",
    "created_at": "2009-12-25T08:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63685",
    "user": "was"
}
```


```
from	Bill Hart <goodwillhart@googlemail.com>
to	William Stein <wstein@gmail.com>
date	Thu, Dec 24, 2009 at 5:23 PM
subject	Re: flint bug maybe
	
hide details 5:23 PM (7 hours ago)
	
Yes, it is a (fairly trivial) flint bug. I'll try and issue a fix later today.

Thanks.

Bill.
```




---

archive/issue_comments_063686.json:
```json
{
    "body": "I don't see why the 'Reported; little feedback' should be annoying. The fact you have reported it is acknowldeged, the fact you have got no feedback is true. \n\nOnce you get some feedback, then update it. It this case, I would have updated it to 'Preported Upstream. Developers acknowldge it's a bug', since at this point in time, there is no fix. \n\nWhat I think would be usefully added is 'Reported upstream. Useful feedback'. Sometimes it takes quite a bit of discussion to decide whether its a Sage bug or a bug in the upstream code.",
    "created_at": "2009-12-25T15:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63686",
    "user": "drkirkby"
}
```

I don't see why the 'Reported; little feedback' should be annoying. The fact you have reported it is acknowldeged, the fact you have got no feedback is true. 

Once you get some feedback, then update it. It this case, I would have updated it to 'Preported Upstream. Developers acknowldge it's a bug', since at this point in time, there is no fix. 

What I think would be usefully added is 'Reported upstream. Useful feedback'. Sometimes it takes quite a bit of discussion to decide whether its a Sage bug or a bug in the upstream code.



---

archive/issue_comments_063687.json:
```json
{
    "body": "\n```\nOK, I persisted with the very slow machine and got flint-1.5.1\nreleased, which fixes this bug. All the test code passes, including\nthe test function I wrote for the case reported.\n-- Bill Hart\n```\n",
    "created_at": "2009-12-25T18:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63687",
    "user": "was"
}
```


```
OK, I persisted with the very slow machine and got flint-1.5.1
released, which fixes this bug. All the test code passes, including
the test function I wrote for the case reported.
-- Bill Hart
```




---

archive/issue_comments_063688.json:
```json
{
    "body": "Is anyone looking up updating the flint package in Sage to cure this bug? According to this ticket, flint 1.5.1 was released 8 months ago. \n\nDave",
    "created_at": "2010-08-23T20:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63688",
    "user": "drkirkby"
}
```

Is anyone looking up updating the flint package in Sage to cure this bug? According to this ticket, flint 1.5.1 was released 8 months ago. 

Dave



---

archive/issue_comments_063689.json:
```json
{
    "body": "Changing component from basic arithmetic to packages.",
    "created_at": "2011-09-01T22:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63689",
    "user": "leif"
}
```

Changing component from basic arithmetic to packages.



---

archive/issue_comments_063690.json:
```json
{
    "body": "Changing assignee from AlexGhitza to tbd.",
    "created_at": "2011-09-01T22:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63690",
    "user": "leif"
}
```

Changing assignee from AlexGhitza to tbd.



---

archive/issue_comments_063691.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> Is anyone looking up updating the flint package in Sage to cure this bug? According to this ticket, flint 1.5.1 was released 8 months ago. \n> \n> Dave \n\nI'm upgrading FLINT to 1.5.2 (not 1.6, at least for the moment, nor 2.x) for a couple of reasons (e.g. failing to build the test suite with MPIR 2.x, cf. #9858, #8664; ARM support, cf. #10328). I had an almost ready spkg last year, but now have to rebase my changes since the p5 has meanwhile become a p9. (There's a lot wrong with this spkg, especially the `makefile`, but also `spkg-install` and even `SPKG.txt`.)\n\nI so far can confirm that the failing example given above works with FLINT 1.5.2, so this ticket can most probably be closed when a new FLINT spkg has been merged.\n\nStay tuned on #9858.",
    "created_at": "2011-09-01T22:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63691",
    "user": "leif"
}
```

Replying to [comment:7 drkirkby]:
> Is anyone looking up updating the flint package in Sage to cure this bug? According to this ticket, flint 1.5.1 was released 8 months ago. 
> 
> Dave 

I'm upgrading FLINT to 1.5.2 (not 1.6, at least for the moment, nor 2.x) for a couple of reasons (e.g. failing to build the test suite with MPIR 2.x, cf. #9858, #8664; ARM support, cf. #10328). I had an almost ready spkg last year, but now have to rebase my changes since the p5 has meanwhile become a p9. (There's a lot wrong with this spkg, especially the `makefile`, but also `spkg-install` and even `SPKG.txt`.)

I so far can confirm that the failing example given above works with FLINT 1.5.2, so this ticket can most probably be closed when a new FLINT spkg has been merged.

Stay tuned on #9858.



---

archive/issue_comments_063692.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2011-09-01T22:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63692",
    "user": "leif"
}
```

Changing priority from major to critical.



---

archive/issue_comments_063693.json:
```json
{
    "body": "Works now.",
    "created_at": "2013-05-16T08:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63693",
    "user": "jdemeyer"
}
```

Works now.



---

archive/issue_comments_063694.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-05-16T08:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7518#issuecomment-63694",
    "user": "jdemeyer"
}
```

Resolution: worksforme
