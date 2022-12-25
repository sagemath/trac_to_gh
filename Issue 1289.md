# Issue 1289: serious problems with how ceil and floor are computed symbolically

archive/issues_001289.json:
```json
{
    "body": "Assignee: somebody\n\nThese are mostly the result of maxima getting used at some point to do the computation (except the one that leaves floor(a) symbolic?!)\n\n\n```\nsage: a = factorial(50) / e\nsage: ceil(a)\n11188719610782480421414879249141773426630319613740326700720324608\nsage: floor(a)\nfloor(30414093201713378043612608166064768844377641568960512000000000000*e^-1)\nsage: ceil(factorial(50) / n(e,20000))\n11188719610782480504630258070757734324011354208865721592720336801\nsage: floor(factorial(50) / n(e,20000))\n11188719610782480504630258070757734324011354208865721592720336800\nsage: int(floor(a))\n11188719610782479690664060583690314324787903255598816872754053120L\n```\n\n\nBasically the ceil and floor need to be improved to *not* fall back on Maxima,\nbut hopefully do something more sensible, especially when large numbers are\ninvolved.  \n\nI think this is an extremely important bug to fix, since it is something\nthat will come up in practice and produce wrong results, e.g., in a recent\npatch by Dan Drake posted on sage-devel it *did*.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1289\n\n",
    "created_at": "2007-11-27T14:34:11Z",
    "labels": [
        "component: basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "serious problems with how ceil and floor are computed symbolically",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1289",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

These are mostly the result of maxima getting used at some point to do the computation (except the one that leaves floor(a) symbolic?!)


```
sage: a = factorial(50) / e
sage: ceil(a)
11188719610782480421414879249141773426630319613740326700720324608
sage: floor(a)
floor(30414093201713378043612608166064768844377641568960512000000000000*e^-1)
sage: ceil(factorial(50) / n(e,20000))
11188719610782480504630258070757734324011354208865721592720336801
sage: floor(factorial(50) / n(e,20000))
11188719610782480504630258070757734324011354208865721592720336800
sage: int(floor(a))
11188719610782479690664060583690314324787903255598816872754053120L
```


Basically the ceil and floor need to be improved to *not* fall back on Maxima,
but hopefully do something more sensible, especially when large numbers are
involved.  

I think this is an extremely important bug to fix, since it is something
that will come up in practice and produce wrong results, e.g., in a recent
patch by Dan Drake posted on sage-devel it *did*.

Issue created by migration from https://trac.sagemath.org/ticket/1289





---

archive/issue_comments_008070.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T21:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1289#issuecomment-8070",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008071.json:
```json
{
    "body": "Changing assignee from somebody to @mwhansen.",
    "created_at": "2007-12-06T21:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1289#issuecomment-8071",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from somebody to @mwhansen.



---

archive/issue_comments_008072.json:
```json
{
    "body": "Since this is a maxima issue as well, I posted about it upstream:\nhttp://www.math.utexas.edu/pipermail/maxima/2007/009327.html",
    "created_at": "2007-12-07T22:03:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1289#issuecomment-8072",
    "user": "https://github.com/mwhansen"
}
```

Since this is a maxima issue as well, I posted about it upstream:
http://www.math.utexas.edu/pipermail/maxima/2007/009327.html



---

archive/issue_comments_008073.json:
```json
{
    "body": "Attachment [1289.patch](tarball://root/attachments/some-uuid/ticket1289/1289.patch) by @mwhansen created at 2008-01-17 01:20:56",
    "created_at": "2008-01-17T01:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1289#issuecomment-8073",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1289.patch](tarball://root/attachments/some-uuid/ticket1289/1289.patch) by @mwhansen created at 2008-01-17 01:20:56



---

archive/issue_comments_008074.json:
```json
{
    "body": "Some irc conversation about this with examples:\n\n```\n17:34 < was-1289> Does the algorithm you implemented actually provably work?\n17:35 < was-1289> I'm having a little trouble seeing why it should always work.\n17:36 < mhansen> No, I don't think that it will always work, but I haven't found a case where it hasn't \n                 yet.  According to Fateman's posts, you won't ever be able to get something that \n                 provably works in general.\n17:37 < was-1289> It should say that in the documentation!\n17:37 < was-1289> :-)\n17:37 < was-1289> I wonder if Fateman is right though.\n17:37 < was-1289> I haven't got that far.\n17:37 < mhansen> There is a result from the 60s on this sort of thing.\n17:38 < was-1289> Then he says \"For expression in some subclass of what is allowed in Maxima, there are\n17:38 < was-1289> possibilities.\"\n17:38 < was-1289> Certainly for an arbitrary number given by an algorithm, it is impossible to decide if \n                  a number is 0 or not.\n17:38 < was-1289> That's really easy to see, since it happens all the time that one can't\n17:38 < was-1289> easily decide.\n17:39 < was-1289> But if the number is of a fairly restricted form, I bet the situation is different.\n17:39 < was-1289> Hmm.\n17:40 < mhansen> I really don't know enough of the mathematics in this area.  But, what is up there \n                 certainly improves things from before.\n17:40 < was-1289> your code gets this wrong:\n17:40 < was-1289> sage: a = SR(10^50 + 10^(-50))\n17:40 < was-1289> sage: ceil(a)\n17:40 < was-1289> 100000000000000000000000000000000000000000000000000\n17:41 < was-1289> If you started with a larger number of bits at the beginning, you would get the right \n                  answer.\n17:41 < was-1289> sage: RealField(500)(a).ceil()\n17:41 < was-1289> 100000000000000000000000000000000000000000000000001\n17:42 < mhansen> Hmm....\n17:42 < was-1289> Both Maple and Matheamtica have no trouble at all getting this right.\n17:42 < was-1289> sage: maple(a).ceil()\n17:42 < was-1289> 100000000000000000000000000000000000000000000000001\n17:42 < was-1289> sage: mathematica(a).Ceiling()\n17:42 < was-1289> 100000000000000000000000000000000000000000000000001\n [17:42] [was-1289(+i)] [2:#sage-devel(+ns)] [Act: 1]                                                    \n[#sage-devel] \n```\n\n\nThen Carl Witty comes to the rescue:\n\n```\n17:43 -!- cwitty_ is now known as cwitty\n17:44 < mhansen> Yeah, I know that.\n17:44 < was-1289> In my example, we could defeat it by first trying to coerce to QQ.\n17:44 < was-1289> I.e., instead of trying RealField(n) first, try QQ first. If that works we're in great \n                  shap.\n17:44 < mhansen> That seems like a reasonable plan.\n17:45 < was-1289> I wonder what else we should do.\n17:45 < cwitty> Here's another idea:\n17:45 < cwitty> Coerce into increasingly precise intervals.\n17:45 < cwitty> If you find an interval such that the lower and upper bound have the same ceiling, then \n                that's the answer.\n17:46 < was-1289> How do we coerce into increasingly precise intervals?\n17:46 < was-1289> got it.\n17:46 < was-1289> That's a great idea!!!!\n17:46 < was-1289> sage: RealIntervalField(500)(a)\n17:46 < mhansen> Yeah, that's really nice.\n17:46 < cwitty> If you find an interval that contains only one integer, then compare the original \n                symbolic expression against that integer to see if you can prove that it is less than \n                that integer, or greater than that integer, or equal to that integer.\n17:47 < was-1289> mhansen -- can you implement it?\n17:47 < mhansen> Yes, but I have to go meet someone for dinner now.  I will do it afterwards though.\n17:47 < was-1289> ok\n17:47 -!- mhansen is now known as mhansen-dinner\n}}}}",
    "created_at": "2008-01-17T01:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1289#issuecomment-8074",
    "user": "https://github.com/williamstein"
}
```

Some irc conversation about this with examples:

```
17:34 < was-1289> Does the algorithm you implemented actually provably work?
17:35 < was-1289> I'm having a little trouble seeing why it should always work.
17:36 < mhansen> No, I don't think that it will always work, but I haven't found a case where it hasn't 
                 yet.  According to Fateman's posts, you won't ever be able to get something that 
                 provably works in general.
17:37 < was-1289> It should say that in the documentation!
17:37 < was-1289> :-)
17:37 < was-1289> I wonder if Fateman is right though.
17:37 < was-1289> I haven't got that far.
17:37 < mhansen> There is a result from the 60s on this sort of thing.
17:38 < was-1289> Then he says "For expression in some subclass of what is allowed in Maxima, there are
17:38 < was-1289> possibilities."
17:38 < was-1289> Certainly for an arbitrary number given by an algorithm, it is impossible to decide if 
                  a number is 0 or not.
17:38 < was-1289> That's really easy to see, since it happens all the time that one can't
17:38 < was-1289> easily decide.
17:39 < was-1289> But if the number is of a fairly restricted form, I bet the situation is different.
17:39 < was-1289> Hmm.
17:40 < mhansen> I really don't know enough of the mathematics in this area.  But, what is up there 
                 certainly improves things from before.
17:40 < was-1289> your code gets this wrong:
17:40 < was-1289> sage: a = SR(10^50 + 10^(-50))
17:40 < was-1289> sage: ceil(a)
17:40 < was-1289> 100000000000000000000000000000000000000000000000000
17:41 < was-1289> If you started with a larger number of bits at the beginning, you would get the right 
                  answer.
17:41 < was-1289> sage: RealField(500)(a).ceil()
17:41 < was-1289> 100000000000000000000000000000000000000000000000001
17:42 < mhansen> Hmm....
17:42 < was-1289> Both Maple and Matheamtica have no trouble at all getting this right.
17:42 < was-1289> sage: maple(a).ceil()
17:42 < was-1289> 100000000000000000000000000000000000000000000000001
17:42 < was-1289> sage: mathematica(a).Ceiling()
17:42 < was-1289> 100000000000000000000000000000000000000000000000001
 [17:42] [was-1289(+i)] [2:#sage-devel(+ns)] [Act: 1]                                                    
[#sage-devel] 
```


Then Carl Witty comes to the rescue:

```
17:43 -!- cwitty_ is now known as cwitty
17:44 < mhansen> Yeah, I know that.
17:44 < was-1289> In my example, we could defeat it by first trying to coerce to QQ.
17:44 < was-1289> I.e., instead of trying RealField(n) first, try QQ first. If that works we're in great 
                  shap.
17:44 < mhansen> That seems like a reasonable plan.
17:45 < was-1289> I wonder what else we should do.
17:45 < cwitty> Here's another idea:
17:45 < cwitty> Coerce into increasingly precise intervals.
17:45 < cwitty> If you find an interval such that the lower and upper bound have the same ceiling, then 
                that's the answer.
17:46 < was-1289> How do we coerce into increasingly precise intervals?
17:46 < was-1289> got it.
17:46 < was-1289> That's a great idea!!!!
17:46 < was-1289> sage: RealIntervalField(500)(a)
17:46 < mhansen> Yeah, that's really nice.
17:46 < cwitty> If you find an interval that contains only one integer, then compare the original 
                symbolic expression against that integer to see if you can prove that it is less than 
                that integer, or greater than that integer, or equal to that integer.
17:47 < was-1289> mhansen -- can you implement it?
17:47 < mhansen> Yes, but I have to go meet someone for dinner now.  I will do it afterwards though.
17:47 < was-1289> ok
17:47 -!- mhansen is now known as mhansen-dinner
}}}}



---

archive/issue_comments_008075.json:
```json
{
    "body": "Attachment [1289.2.patch](tarball://root/attachments/some-uuid/ticket1289/1289.2.patch) by @mwhansen created at 2008-01-17 05:44:08",
    "created_at": "2008-01-17T05:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1289#issuecomment-8075",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1289.2.patch](tarball://root/attachments/some-uuid/ticket1289/1289.2.patch) by @mwhansen created at 2008-01-17 05:44:08



---

archive/issue_comments_008076.json:
```json
{
    "body": "New patch up implementing the interval method.",
    "created_at": "2008-01-17T05:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1289#issuecomment-8076",
    "user": "https://github.com/mwhansen"
}
```

New patch up implementing the interval method.



---

archive/issue_events_003386.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-18T01:45:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1289",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1289#event-3386"
}
```



---

archive/issue_comments_008077.json:
```json
{
    "body": "Positive review by wstein. Merged in Sage 2.10.alpha4.",
    "created_at": "2008-01-18T01:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1289#issuecomment-8077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review by wstein. Merged in Sage 2.10.alpha4.



---

archive/issue_comments_008078.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-18T01:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1289#issuecomment-8078",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003387.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-18T01:48:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1289",
    "milestone": "sage-2.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1289#event-3387"
}
```
