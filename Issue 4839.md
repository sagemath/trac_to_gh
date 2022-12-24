# Issue 4839: update desolve_laplace like #4285 did for desolve

archive/issues_004839.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  mhansen jdemeyer\n\nMake it so that the following works:\n\n\n```\nsage: var('t')\nt\nsage: x=function('x', t)\nsage: soln=desolve_laplace(diff(x,t)+x==1, x, ics=[0,2]) \nsage: soln(3) \ne^-3 + 1\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4839\n\n",
    "created_at": "2008-12-20T20:12:20Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "update desolve_laplace like #4285 did for desolve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4839",
    "user": "jason"
}
```
Assignee: burcin

CC:  mhansen jdemeyer

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

archive/issue_comments_036690.json:
```json
{
    "body": "This would be awesome! \n\nBTW, ICs used with desolve really does not work: from the docstring, you see\n\n\n```\n           sage: x = var('x')\n            sage: y = function('y', x)\n            sage: de = diff(y,x,2) - y == x\n            sage: desolve(de, y)\n            k1*e^x + k2*e^(-x) - x\n            sage: f = desolve(de, y, [10,2,1]); f\n            (e^10*y(10) + 8*e^10)*e^(-x)/2 + (y(10) +12)*e^(x - 10)/2 - x\n```\n\nso for some reason 2 is not plugged in for y(10).",
    "created_at": "2008-12-20T20:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36690",
    "user": "wdj"
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

archive/issue_comments_036691.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36691",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_036692.json:
```json
{
    "body": "Replying to [comment:1 wdj]:\n> BTW, ICs used with desolve really does not work: from the docstring, \n\nhas been fixed in http://trac.sagemath.org/sage_trac/ticket/6479",
    "created_at": "2009-10-06T20:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36692",
    "user": "robert.marik"
}
```

Replying to [comment:1 wdj]:
> BTW, ICs used with desolve really does not work: from the docstring, 

has been fixed in http://trac.sagemath.org/sage_trac/ticket/6479



---

archive/issue_comments_036693.json:
```json
{
    "body": "The desolve_laplace has been fixed together with other things in http://trac.sagemath.org/sage_trac/ticket/6479 and got positive review. Can be closed now as a duplicate.",
    "created_at": "2009-11-08T00:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36693",
    "user": "robert.marik"
}
```

The desolve_laplace has been fixed together with other things in http://trac.sagemath.org/sage_trac/ticket/6479 and got positive review. Can be closed now as a duplicate.



---

archive/issue_comments_036694.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2009-11-08T00:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36694",
    "user": "robert.marik"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_036695.json:
```json
{
    "body": "To release manager: please see previous comment.",
    "created_at": "2009-11-18T18:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36695",
    "user": "kcrisman"
}
```

To release manager: please see previous comment.



---

archive/issue_comments_036696.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> To release manager: please see previous comment.\n\nBump; please close.",
    "created_at": "2009-12-24T03:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36696",
    "user": "kcrisman"
}
```

Replying to [comment:5 kcrisman]:
> To release manager: please see previous comment.

Bump; please close.



---

archive/issue_comments_036697.json:
```json
{
    "body": "Bump again - release manager, please close :)",
    "created_at": "2010-11-04T18:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36697",
    "user": "kcrisman"
}
```

Bump again - release manager, please close :)



---

archive/issue_comments_036698.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-11-04T19:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36698",
    "user": "mhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_036699.json:
```json
{
    "body": "Fixed by #6479.",
    "created_at": "2010-11-04T19:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36699",
    "user": "mhansen"
}
```

Fixed by #6479.



---

archive/issue_comments_036700.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> Bump again - release manager, please close :)\nNext time, just make the ticket reviewed (put it to needs_review asking somebody to confirm to close the ticket).\n\nThis way we have a peer-reviewed proposal to close and the release manager will see that the ticket has positive_review.",
    "created_at": "2010-11-04T19:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36700",
    "user": "jdemeyer"
}
```

Replying to [comment:7 kcrisman]:
> Bump again - release manager, please close :)
Next time, just make the ticket reviewed (put it to needs_review asking somebody to confirm to close the ticket).

This way we have a peer-reviewed proposal to close and the release manager will see that the ticket has positive_review.



---

archive/issue_comments_036701.json:
```json
{
    "body": "Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.\n\nAnyway, no problem - but in that case let me change the reviewer!  (I can't do the diacritical mark in Robert's name, though.)",
    "created_at": "2010-11-04T20:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36701",
    "user": "kcrisman"
}
```

Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.

Anyway, no problem - but in that case let me change the reviewer!  (I can't do the diacritical mark in Robert's name, though.)



---

archive/issue_comments_036702.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.\nWell, I myself have gotten complaints about closing tickets (for whatever reason) when not being a release manager.  I also think it is good to review the fact that the bug is indeed invalid.\n\n> I can't do the diacritical mark in Robert's name, though.\nCopy and paste from [http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames) :-)",
    "created_at": "2010-11-04T20:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36702",
    "user": "jdemeyer"
}
```

Replying to [comment:10 kcrisman]:
> Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.
Well, I myself have gotten complaints about closing tickets (for whatever reason) when not being a release manager.  I also think it is good to review the fact that the bug is indeed invalid.

> I can't do the diacritical mark in Robert's name, though.
Copy and paste from [http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames) :-)



---

archive/issue_comments_036703.json:
```json
{
    "body": "> > Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.\n> Well, I myself have gotten complaints about closing tickets (for whatever reason) when not being a release manager. \nYes, as have I; I think that only having release managers (or possibly experienced non-current release managers like Mike and Minh) actually close the tickets is wise.  \n\nBut in this case, you *are* the release manager!   As Robin Williams says in 'Aladdin', \"Phenomenal cosmic powers! Itty bitty living space.\"\n\n> I also think it is good to review the fact that the bug is indeed invalid.\n\nOf course, one should review that a bug is invalid, but in this case it is the duplicate status that is at issue, which is more of a release issue.  Anyway, I don't mind Robert getting more props!",
    "created_at": "2010-11-04T20:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4839#issuecomment-36703",
    "user": "kcrisman"
}
```

> > Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.
> Well, I myself have gotten complaints about closing tickets (for whatever reason) when not being a release manager. 
Yes, as have I; I think that only having release managers (or possibly experienced non-current release managers like Mike and Minh) actually close the tickets is wise.  

But in this case, you *are* the release manager!   As Robin Williams says in 'Aladdin', "Phenomenal cosmic powers! Itty bitty living space."

> I also think it is good to review the fact that the bug is indeed invalid.

Of course, one should review that a bug is invalid, but in this case it is the duplicate status that is at issue, which is more of a release issue.  Anyway, I don't mind Robert getting more props!
