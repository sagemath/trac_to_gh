# Issue 4839: update desolve_laplace like #4285 did for desolve

archive/issues_004839.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @mwhansen @jdemeyer\n\nMake it so that the following works:\n\n```\nsage: var('t')\nt\nsage: x=function('x', t)\nsage: soln=desolve_laplace(diff(x,t)+x==1, x, ics=[0,2]) \nsage: soln(3) \ne^-3 + 1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4839\n\n",
    "closed_at": "2010-11-04T19:30:45Z",
    "created_at": "2008-12-20T20:12:20Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "update desolve_laplace like #4285 did for desolve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4839",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @burcin

CC:  @mwhansen @jdemeyer

Make it so that the following works:

```
sage: var('t')
t
sage: x=function('x', t)
sage: soln=desolve_laplace(diff(x,t)+x==1, x, ics=[0,2]) 
sage: soln(3) 
e^-3 + 1
```


Issue created by migration from https://trac.sagemath.org/ticket/4839





---

archive/issue_comments_036618.json:
```json
{
    "body": "This would be awesome! \n\nBTW, ICs used with desolve really does not work: from the docstring, you see\n\n```\n           sage: x = var('x')\n            sage: y = function('y', x)\n            sage: de = diff(y,x,2) - y == x\n            sage: desolve(de, y)\n            k1*e^x + k2*e^(-x) - x\n            sage: f = desolve(de, y, [10,2,1]); f\n            (e^10*y(10) + 8*e^10)*e^(-x)/2 + (y(10) +12)*e^(x - 10)/2 - x\n```\nso for some reason 2 is not plugged in for y(10).",
    "created_at": "2008-12-20T20:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36618",
    "user": "https://github.com/wdjoyner"
}
```

This would be awesome! 

BTW, ICs used with desolve really does not work: from the docstring, you see

```
           sage: x = var('x')
            sage: y = function('y', x)
            sage: de = diff(y,x,2) - y == x
            sage: desolve(de, y)
            k1*e^x + k2*e^(-x) - x
            sage: f = desolve(de, y, [10,2,1]); f
            (e^10*y(10) + 8*e^10)*e^(-x)/2 + (y(10) +12)*e^(x - 10)/2 - x
```
so for some reason 2 is not plugged in for y(10).



---

archive/issue_comments_036619.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36619",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_036620.json:
```json
{
    "body": "Replying to [comment:1 wdj]:\n> BTW, ICs used with desolve really does not work: from the docstring, \n\n\nhas been fixed in http://trac.sagemath.org/sage_trac/ticket/6479",
    "created_at": "2009-10-06T20:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36620",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:1 wdj]:
> BTW, ICs used with desolve really does not work: from the docstring, 


has been fixed in http://trac.sagemath.org/sage_trac/ticket/6479



---

archive/issue_comments_036621.json:
```json
{
    "body": "The desolve_laplace has been fixed together with other things in http://trac.sagemath.org/sage_trac/ticket/6479 and got positive review. Can be closed now as a duplicate.",
    "created_at": "2009-11-08T00:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36621",
    "user": "https://github.com/robert-marik"
}
```

The desolve_laplace has been fixed together with other things in http://trac.sagemath.org/sage_trac/ticket/6479 and got positive review. Can be closed now as a duplicate.



---

archive/issue_comments_036622.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2009-11-08T00:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36622",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_036623.json:
```json
{
    "body": "To release manager: please see previous comment.",
    "created_at": "2009-11-18T18:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36623",
    "user": "https://github.com/kcrisman"
}
```

To release manager: please see previous comment.



---

archive/issue_comments_036624.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> To release manager: please see previous comment.\n\n\nBump; please close.",
    "created_at": "2009-12-24T03:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36624",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:5 kcrisman]:
> To release manager: please see previous comment.


Bump; please close.



---

archive/issue_comments_036625.json:
```json
{
    "body": "Bump again - release manager, please close :)",
    "created_at": "2010-11-04T18:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36625",
    "user": "https://github.com/kcrisman"
}
```

Bump again - release manager, please close :)



---

archive/issue_comments_036626.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-11-04T19:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36626",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate



---

archive/issue_events_011114.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-11-04T19:30:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4839#event-11114"
}
```



---

archive/issue_comments_036627.json:
```json
{
    "body": "Fixed by #6479.",
    "created_at": "2010-11-04T19:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36627",
    "user": "https://github.com/mwhansen"
}
```

Fixed by #6479.



---

archive/issue_events_011115.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-11-04T19:30:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4839#event-11115"
}
```



---

archive/issue_comments_036628.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> Bump again - release manager, please close :)\n\nNext time, just make the ticket reviewed (put it to needs_review asking somebody to confirm to close the ticket).\n\nThis way we have a peer-reviewed proposal to close and the release manager will see that the ticket has positive_review.",
    "created_at": "2010-11-04T19:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36628",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:7 kcrisman]:
> Bump again - release manager, please close :)

Next time, just make the ticket reviewed (put it to needs_review asking somebody to confirm to close the ticket).

This way we have a peer-reviewed proposal to close and the release manager will see that the ticket has positive_review.



---

archive/issue_comments_036629.json:
```json
{
    "body": "Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.\n\nAnyway, no problem - but in that case let me change the reviewer!  (I can't do the diacritical mark in Robert's name, though.)",
    "created_at": "2010-11-04T20:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36629",
    "user": "https://github.com/kcrisman"
}
```

Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.

Anyway, no problem - but in that case let me change the reviewer!  (I can't do the diacritical mark in Robert's name, though.)



---

archive/issue_comments_036630.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.\n\nWell, I myself have gotten complaints about closing tickets (for whatever reason) when not being a release manager.  I also think it is good to review the fact that the bug is indeed invalid.\n\n> I can't do the diacritical mark in Robert's name, though.\n\nCopy and paste from [http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames) :-)",
    "created_at": "2010-11-04T20:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36630",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:10 kcrisman]:
> Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.

Well, I myself have gotten complaints about closing tickets (for whatever reason) when not being a release manager.  I also think it is good to review the fact that the bug is indeed invalid.

> I can't do the diacritical mark in Robert's name, though.

Copy and paste from [http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames) :-)



---

archive/issue_comments_036631.json:
```json
{
    "body": "> > Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.\n\n> Well, I myself have gotten complaints about closing tickets (for whatever reason) when not being a release manager. \nYes, as have I; I think that only having release managers (or possibly experienced non-current release managers like Mike and Minh) actually close the tickets is wise.  \n\nBut in this case, you *are* the release manager!   As Robin Williams says in 'Aladdin', \"Phenomenal cosmic powers! Itty bitty living space.\"\n\n> I also think it is good to review the fact that the bug is indeed invalid.\n\n\nOf course, one should review that a bug is invalid, but in this case it is the duplicate status that is at issue, which is more of a release issue.  Anyway, I don't mind Robert getting more props!",
    "created_at": "2010-11-04T20:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36631",
    "user": "https://github.com/kcrisman"
}
```

> > Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.

> Well, I myself have gotten complaints about closing tickets (for whatever reason) when not being a release manager. 
Yes, as have I; I think that only having release managers (or possibly experienced non-current release managers like Mike and Minh) actually close the tickets is wise.  

But in this case, you *are* the release manager!   As Robin Williams says in 'Aladdin', "Phenomenal cosmic powers! Itty bitty living space."

> I also think it is good to review the fact that the bug is indeed invalid.


Of course, one should review that a bug is invalid, but in this case it is the duplicate status that is at issue, which is more of a release issue.  Anyway, I don't mind Robert getting more props!
