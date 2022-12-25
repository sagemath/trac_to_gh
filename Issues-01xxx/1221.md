# Issue 1221: Consider using Mathematica syntax for integration

archive/issues_001221.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @jasongrout\n\nI think we should use this syntax for integration:\n\n```\n>>> integrate(x**3, (x, -1, 1))\n0\n>>> integrate(sin(x), (x, 0, pi/2))\n1\n>>> integrate(cos(x), (x, -pi/2, pi/2))\n2\n```\n\ninstead of\n\n```\nsage: integral(x/(x^2+1), x, 0, 1)\n     log(2)/2\n```\n\nas in SAGE currently, to be close to Mathematica. Because then you can\nuse the syntax:\n\nintegrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))\n\nfor multiple integrals.\n\nSee also [1], how we discussed this in SymPy.\n\n[1] http://code.google.com/p/sympy/issues/detail?id=25\n\nIssue created by migration from https://trac.sagemath.org/ticket/1221\n\n",
    "closed_at": "2010-09-08T12:29:13Z",
    "created_at": "2007-11-20T22:22:35Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Consider using Mathematica syntax for integration",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1221",
    "user": "https://github.com/certik"
}
```
Assignee: @mwhansen

CC:  @jasongrout

I think we should use this syntax for integration:

```
>>> integrate(x**3, (x, -1, 1))
0
>>> integrate(sin(x), (x, 0, pi/2))
1
>>> integrate(cos(x), (x, -pi/2, pi/2))
2
```

instead of

```
sage: integral(x/(x^2+1), x, 0, 1)
     log(2)/2
```

as in SAGE currently, to be close to Mathematica. Because then you can
use the syntax:

integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))

for multiple integrals.

See also [1], how we discussed this in SymPy.

[1] http://code.google.com/p/sympy/issues/detail?id=25

Issue created by migration from https://trac.sagemath.org/ticket/1221





---

archive/issue_events_003237.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-21T16:11:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1221#event-3237"
}
```



---

archive/issue_comments_007570.json:
```json
{
    "body": "I changed this to sage-2.9, since it will be very easy to implement.",
    "created_at": "2007-11-21T16:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7570",
    "user": "https://github.com/williamstein"
}
```

I changed this to sage-2.9, since it will be very easy to implement.



---

archive/issue_comments_007571.json:
```json
{
    "body": "```\nSage math appInbox\nReply to all\nForward\nReply by chat\nFilter messages like this\nPrint\nAdd to Contacts list\nDelete this message\nReport phishing\nReport not phishing\nShow original\nMessage text garbled?\nWhy is this spam/nonspam?\nchris@seberino.org\t\nW. Stein I wanted to commend you for leading Sage. I think it is a great idea...\n\t\nNov 19 (2 days ago)\nWilliam Stein\t\nOn Nov 20, 2007 11:10 AM, seberino@spawar.navy.mil So do I. I think we should...\n\t\n11:17 AM (20 hours ago)\nOndrej Certik to sage-devel\n\t\nshow details 2:22 PM (17 hours ago)\n\t\n\t\n\t\nReply\n\t\n\t\n\nOn Nov 20, 2007 8:17 PM, William Stein <wstein@gmail.com> wrote:\n>\n> On Nov 20, 2007 11:10 AM, seberino@spawar.navy.mil\n> <seberino@spawar.navy.mil> wrote:\n> > > As to syntax, I think in Python we could use:\n> > > >>> integrate(cos(x), (x, -pi/2, pi/2))\n> > >  Because then you can\n> > > use the syntax:\n> > >\n> > > integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))\n> > >\n> > > for multiple integrals. But anyway, it's just a cosmetic issue.\n> >\n> > When I commended Sage's syntax I was assuming you were using this\n> > Mathematica like syntax already.  I agree with Ondrej and think his\n> > suggestion above is the way to go.\n>\n> So do I.  I think we should change that functions as suggested.  Anybody\n> want to submit a patch?  Ondrej, could you create a trac ticket making precise\n> what you want, etc.?\n\nhttp://sagetrac.org/sage_trac/ticket/1221\n\nOndrej\n- Show quoted text -\n\n--~--~---------~--~----~------------~-------~--~----~\nTo post to this group, send email to sage-devel@googlegroups.com\nTo unsubscribe from this group, send email to sage-devel-unsubscribe@googlegroups.com\nFor more options, visit this group at http://groups.google.com/group/sage-devel\nURLs: http://sage.scipy.org/sage/ and http://modular.math.washington.edu/sage/\n-~----------~----~----~----~------~----~------~--~---\n\nReply\n\t\t\nForward\n\t\t\n\t\nStephen Forrest to sage-devel\n\t\nshow details 2:44 PM (17 hours ago)\n\t\n\t\n\t\nReply\n\t\n\t\n\nOn Nov 20, 2007 2:10 PM, seberino@spawar.navy.mil\n<seberino@spawar.navy.mil> wrote:\n\n[snip]\n> >  Because then you can\n> > use the syntax:\n> >\n> > integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))\n> >\n> > for multiple integrals. But anyway, it's just a cosmetic issue.\n>\n> When I commended Sage's syntax I was assuming you were using this\n> Mathematica like syntax already.  I agree with Ondrej and think his\n> suggestion above is the way to go.\n\nThis probably goes without saying, but presumably after the change one\nwill still be able to use the syntax 'integrate(sin(x),x) ' for\nindefinite integration?  That is, the second argument may be a triple\nor a symbol?\n\nSteve\n- Show quoted text -\n\n--~--~---------~--~----~------------~-------~--~----~\nTo post to this group, send email to sage-devel@googlegroups.com\nTo unsubscribe from this group, send email to sage-devel-unsubscribe@googlegroups.com\nFor more options, visit this group at http://groups.google.com/group/sage-devel\nURLs: http://sage.scipy.org/sage/ and http://modular.math.washington.edu/sage/\n-~----------~----~----~----~------~----~------~--~---\n\nReply\n\t\t\nForward\n\t\t\nInvite Stephen Forrest to chat\n\t\nOndrej Certik to sage-devel\n\t\nshow details 5:11 PM (14 hours ago)\n\t\n\t\n\t\nReply\n\t\n\t\n\nOn Nov 20, 2007 11:44 PM, Stephen Forrest <stephen.forrest@gmail.com> wrote:\n>\n> On Nov 20, 2007 2:10 PM, seberino@spawar.navy.mil\n> <seberino@spawar.navy.mil> wrote:\n>\n> [snip]\n> > >  Because then you can\n> > > use the syntax:\n> > >\n> > > integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))\n> > >\n> > > for multiple integrals. But anyway, it's just a cosmetic issue.\n> >\n> > When I commended Sage's syntax I was assuming you were using this\n> > Mathematica like syntax already.  I agree with Ondrej and think his\n> > suggestion above is the way to go.\n>\n> This probably goes without saying, but presumably after the change one\n> will still be able to use the syntax 'integrate(sin(x),x) ' for\n> indefinite integration?  That is, the second argument may be a triple\n> or a symbol?\n\nExactly as you say.\n\nOndrej\n- Show quoted text -\n```",
    "created_at": "2007-11-21T16:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7571",
    "user": "https://github.com/williamstein"
}
```

```
Sage math appInbox
Reply to all
Forward
Reply by chat
Filter messages like this
Print
Add to Contacts list
Delete this message
Report phishing
Report not phishing
Show original
Message text garbled?
Why is this spam/nonspam?
chris@seberino.org	
W. Stein I wanted to commend you for leading Sage. I think it is a great idea...
	
Nov 19 (2 days ago)
William Stein	
On Nov 20, 2007 11:10 AM, seberino@spawar.navy.mil So do I. I think we should...
	
11:17 AM (20 hours ago)
Ondrej Certik to sage-devel
	
show details 2:22 PM (17 hours ago)
	
	
	
Reply
	
	

On Nov 20, 2007 8:17 PM, William Stein <wstein@gmail.com> wrote:
>
> On Nov 20, 2007 11:10 AM, seberino@spawar.navy.mil
> <seberino@spawar.navy.mil> wrote:
> > > As to syntax, I think in Python we could use:
> > > >>> integrate(cos(x), (x, -pi/2, pi/2))
> > >  Because then you can
> > > use the syntax:
> > >
> > > integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))
> > >
> > > for multiple integrals. But anyway, it's just a cosmetic issue.
> >
> > When I commended Sage's syntax I was assuming you were using this
> > Mathematica like syntax already.  I agree with Ondrej and think his
> > suggestion above is the way to go.
>
> So do I.  I think we should change that functions as suggested.  Anybody
> want to submit a patch?  Ondrej, could you create a trac ticket making precise
> what you want, etc.?

http://sagetrac.org/sage_trac/ticket/1221

Ondrej
- Show quoted text -

--~--~---------~--~----~------------~-------~--~----~
To post to this group, send email to sage-devel@googlegroups.com
To unsubscribe from this group, send email to sage-devel-unsubscribe@googlegroups.com
For more options, visit this group at http://groups.google.com/group/sage-devel
URLs: http://sage.scipy.org/sage/ and http://modular.math.washington.edu/sage/
-~----------~----~----~----~------~----~------~--~---

Reply
		
Forward
		
	
Stephen Forrest to sage-devel
	
show details 2:44 PM (17 hours ago)
	
	
	
Reply
	
	

On Nov 20, 2007 2:10 PM, seberino@spawar.navy.mil
<seberino@spawar.navy.mil> wrote:

[snip]
> >  Because then you can
> > use the syntax:
> >
> > integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))
> >
> > for multiple integrals. But anyway, it's just a cosmetic issue.
>
> When I commended Sage's syntax I was assuming you were using this
> Mathematica like syntax already.  I agree with Ondrej and think his
> suggestion above is the way to go.

This probably goes without saying, but presumably after the change one
will still be able to use the syntax 'integrate(sin(x),x) ' for
indefinite integration?  That is, the second argument may be a triple
or a symbol?

Steve
- Show quoted text -

--~--~---------~--~----~------------~-------~--~----~
To post to this group, send email to sage-devel@googlegroups.com
To unsubscribe from this group, send email to sage-devel-unsubscribe@googlegroups.com
For more options, visit this group at http://groups.google.com/group/sage-devel
URLs: http://sage.scipy.org/sage/ and http://modular.math.washington.edu/sage/
-~----------~----~----~----~------~----~------~--~---

Reply
		
Forward
		
Invite Stephen Forrest to chat
	
Ondrej Certik to sage-devel
	
show details 5:11 PM (14 hours ago)
	
	
	
Reply
	
	

On Nov 20, 2007 11:44 PM, Stephen Forrest <stephen.forrest@gmail.com> wrote:
>
> On Nov 20, 2007 2:10 PM, seberino@spawar.navy.mil
> <seberino@spawar.navy.mil> wrote:
>
> [snip]
> > >  Because then you can
> > > use the syntax:
> > >
> > > integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))
> > >
> > > for multiple integrals. But anyway, it's just a cosmetic issue.
> >
> > When I commended Sage's syntax I was assuming you were using this
> > Mathematica like syntax already.  I agree with Ondrej and think his
> > suggestion above is the way to go.
>
> This probably goes without saying, but presumably after the change one
> will still be able to use the syntax 'integrate(sin(x),x) ' for
> indefinite integration?  That is, the second argument may be a triple
> or a symbol?

Exactly as you say.

Ondrej
- Show quoted text -
```



---

archive/issue_comments_007572.json:
```json
{
    "body": "Changing component from algebraic geometry to calculus.",
    "created_at": "2007-12-06T21:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7572",
    "user": "https://github.com/mwhansen"
}
```

Changing component from algebraic geometry to calculus.



---

archive/issue_comments_007573.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-12-06T21:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7573",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_007574.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T21:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7574",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007575.json:
```json
{
    "body": "This will break backward compatibility in a massive way, so I would suggest setting it to \"won't fix\".\n\nCheers,\n\nMichael",
    "created_at": "2008-08-10T08:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7575",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This will break backward compatibility in a massive way, so I would suggest setting it to "won't fix".

Cheers,

Michael



---

archive/issue_comments_007576.json:
```json
{
    "body": "Well, I haven't replied here when you suggested won't fix, as I was thinking about this.\n\nI understand that breaking code is bad.\n\nBut still consistency is consistency. There are ways to improve the API in a non compatible way, e.g. introduce both versions and raise python warning for the old API. and after couple releases, remove it.\n\nAlso this was agreed on the sage-devel, so if you seek a different conclusion, you should (imho) advocate that on the list.",
    "created_at": "2008-08-31T00:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7576",
    "user": "https://github.com/certik"
}
```

Well, I haven't replied here when you suggested won't fix, as I was thinking about this.

I understand that breaking code is bad.

But still consistency is consistency. There are ways to improve the API in a non compatible way, e.g. introduce both versions and raise python warning for the old API. and after couple releases, remove it.

Also this was agreed on the sage-devel, so if you seek a different conclusion, you should (imho) advocate that on the list.



---

archive/issue_comments_007577.json:
```json
{
    "body": "See also #2787.",
    "created_at": "2008-08-31T14:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7577",
    "user": "https://github.com/jicama"
}
```

See also #2787.



---

archive/issue_comments_007578.json:
```json
{
    "body": "I suggest we close this ticket since we now support the suggested syntax:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: integrate(x**3, (x, -1, 1))\n0\nsage: integrate(sin(x), (x, 0, pi/2))\n1\nsage: integrate(cos(x), (x, -pi/2, pi/2))\n2\n```\n| Sage Version 4.4.1.alpha2-patched, Release Date: 2010-04-29        |\n| Type notebook() for the GUI, and license() for information.        |\nThe docstring for `sage.misc.functional.integrate()` and `sage.symbolic.integration.integral.integral()` contains plenty of doctests to test the tuple syntax.\n\nFurther discussion on\n* implementing multiple integrals with `integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))` and\n* replacing the examples in the docstrings with the tuple syntax and deprecating the old one\ncan be continued in #2787.\n\nComments?",
    "created_at": "2010-05-01T21:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7578",
    "user": "https://github.com/burcin"
}
```

I suggest we close this ticket since we now support the suggested syntax:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: integrate(x**3, (x, -1, 1))
0
sage: integrate(sin(x), (x, 0, pi/2))
1
sage: integrate(cos(x), (x, -pi/2, pi/2))
2
```
| Sage Version 4.4.1.alpha2-patched, Release Date: 2010-04-29        |
| Type notebook() for the GUI, and license() for information.        |
The docstring for `sage.misc.functional.integrate()` and `sage.symbolic.integration.integral.integral()` contains plenty of doctests to test the tuple syntax.

Further discussion on
* implementing multiple integrals with `integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))` and
* replacing the examples in the docstrings with the tuple syntax and deprecating the old one
can be continued in #2787.

Comments?



---

archive/issue_comments_007579.json:
```json
{
    "body": "I think so, the one-variable issue is resolved and the double integrals are covered in #2787",
    "created_at": "2010-08-24T20:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7579",
    "user": "https://github.com/robert-marik"
}
```

I think so, the one-variable issue is resolved and the double integrals are covered in #2787



---

archive/issue_comments_007580.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-08-24T20:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7580",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_007581.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-08T12:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7581",
    "user": "https://github.com/burcin"
}
```

Resolution: fixed



---

archive/issue_comments_007582.json:
```json
{
    "body": "I'm closing this as fixed. See comment:8 for more info.",
    "created_at": "2010-09-08T12:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1221#issuecomment-7582",
    "user": "https://github.com/burcin"
}
```

I'm closing this as fixed. See comment:8 for more info.



---

archive/issue_events_003238.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2010-09-08T12:29:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1221#event-3238"
}
```



---

archive/issue_events_003239.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2010-09-08T12:29:13Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1221#event-3239"
}
```



---

archive/issue_events_003240.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2010-09-08T12:29:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1221",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1221#event-3240"
}
```
