# Issue 3276: [with patch] more generic assumptions in calculus

archive/issues_003276.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nFor example: \n\n\n```\nsage: var('n,m')\n(n, m)\nsage: assume(n, m, 'integer')\nsage: sin(n*m*pi)\n0\nsage: forget()\nsage: sin(n*m*pi)\nsin(pi*m*n)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3276\n\n",
    "created_at": "2008-05-23T08:13:34Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch] more generic assumptions in calculus",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3276",
    "user": "https://github.com/robertwb"
}
```
Assignee: @garyfurnish

For example: 


```
sage: var('n,m')
(n, m)
sage: assume(n, m, 'integer')
sage: sin(n*m*pi)
0
sage: forget()
sage: sin(n*m*pi)
sin(pi*m*n)
```


Issue created by migration from https://trac.sagemath.org/ticket/3276





---

archive/issue_comments_022611.json:
```json
{
    "body": "Attachment [3276-assume.patch](tarball://root/attachments/some-uuid/ticket3276/3276-assume.patch) by @robertwb created at 2008-05-23 08:16:38",
    "created_at": "2008-05-23T08:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22611",
    "user": "https://github.com/robertwb"
}
```

Attachment [3276-assume.patch](tarball://root/attachments/some-uuid/ticket3276/3276-assume.patch) by @robertwb created at 2008-05-23 08:16:38



---

archive/issue_events_007366.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-05-23T08:22:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "milestone": "sage-3.0.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3276#event-7366"
}
```



---

archive/issue_comments_022612.json:
```json
{
    "body": "Excellent work Robert -- this is really nice.  The code applies, passes, tests, and is well documented.",
    "created_at": "2008-05-23T08:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22612",
    "user": "https://github.com/mwhansen"
}
```

Excellent work Robert -- this is really nice.  The code applies, passes, tests, and is well documented.



---

archive/issue_comments_022613.json:
```json
{
    "body": "I'm giving this a negative review - see the email I'm writing to sage-devel on how introducing more maxima-isms without serious consideration is bad. There is nothing wrong with the code (so it is probably safe to use as a patch if someone needs this feature now), but introducing code to deprecate it two weeks or three weeks later is not good practice in my opinion.",
    "created_at": "2008-05-23T17:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22613",
    "user": "https://github.com/garyfurnish"
}
```

I'm giving this a negative review - see the email I'm writing to sage-devel on how introducing more maxima-isms without serious consideration is bad. There is nothing wrong with the code (so it is probably safe to use as a patch if someone needs this feature now), but introducing code to deprecate it two weeks or three weeks later is not good practice in my opinion.



---

archive/issue_comments_022614.json:
```json
{
    "body": "This is a feature that people have requested from me personally many times, so I think it's worthy of inclusion. I am skeptical that the new symbolics can be a drop-in replacement for maxima in two or three weeks (would be happy to be proven wrong) so I think that it has value. Also, the exposed interface, though it passes strings to maxima, is not tied to the way maxima does things and could easily be used in the new symbolics (if not, they are not a drop-in replacement). \n\nWould it be better if there was a smaller, limited set of options (e.g. \"integer\", \"even\", \"odd\", \"rational\", ...) that we will be sure to want to support in the future.",
    "created_at": "2008-05-23T18:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22614",
    "user": "https://github.com/robertwb"
}
```

This is a feature that people have requested from me personally many times, so I think it's worthy of inclusion. I am skeptical that the new symbolics can be a drop-in replacement for maxima in two or three weeks (would be happy to be proven wrong) so I think that it has value. Also, the exposed interface, though it passes strings to maxima, is not tied to the way maxima does things and could easily be used in the new symbolics (if not, they are not a drop-in replacement). 

Would it be better if there was a smaller, limited set of options (e.g. "integer", "even", "odd", "rational", ...) that we will be sure to want to support in the future.



---

archive/issue_comments_022615.json:
```json
{
    "body": "Drop in replacement for Maxima? doubtful.  Drop in replacement for sage.calculus? almost certainly.  Part of that is changing how assumptions work.  Like it or not assumptions are tied to the maxima way of doing things.  What makes you think I'm going to choose an assumption model that is 100% compatible with the Maxima way?  You can declare variables to be in ZZ instead of having to assume it, so immediately your method becomes very inefficient.  Also your patch has horrible error checking.  It allows for declaring a variable to be analytic or increasing.  This should almost certainly be handled better, even if your making an argument that this should go in now.  I am not going to waste time implementing complicated features in symbolics because people wern't willing to design them properly.",
    "created_at": "2008-05-23T19:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22615",
    "user": "https://github.com/garyfurnish"
}
```

Drop in replacement for Maxima? doubtful.  Drop in replacement for sage.calculus? almost certainly.  Part of that is changing how assumptions work.  Like it or not assumptions are tied to the maxima way of doing things.  What makes you think I'm going to choose an assumption model that is 100% compatible with the Maxima way?  You can declare variables to be in ZZ instead of having to assume it, so immediately your method becomes very inefficient.  Also your patch has horrible error checking.  It allows for declaring a variable to be analytic or increasing.  This should almost certainly be handled better, even if your making an argument that this should go in now.  I am not going to waste time implementing complicated features in symbolics because people wern't willing to design them properly.



---

archive/issue_comments_022616.json:
```json
{
    "body": "To summarize, you don't want this feature because it is at odds with the way you are handling it in your symbolics package (which is a perfectly valid argument).",
    "created_at": "2008-05-23T19:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22616",
    "user": "https://github.com/robertwb"
}
```

To summarize, you don't want this feature because it is at odds with the way you are handling it in your symbolics package (which is a perfectly valid argument).



---

archive/issue_comments_022617.json:
```json
{
    "body": "Basically yes.",
    "created_at": "2008-05-23T20:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22617",
    "user": "https://github.com/garyfurnish"
}
```

Basically yes.



---

archive/issue_comments_022618.json:
```json
{
    "body": "After discussion at dev1 we have decided that we should merge this but only the assume function should be considered \"public\" in that it will be supported after the symbolics rewrite.  The other support classes/methods will probably go away.",
    "created_at": "2008-06-18T21:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22618",
    "user": "https://github.com/garyfurnish"
}
```

After discussion at dev1 we have decided that we should merge this but only the assume function should be considered "public" in that it will be supported after the symbolics rewrite.  The other support classes/methods will probably go away.



---

archive/issue_comments_022619.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T09:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22619",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007367.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-25T09:15:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3276#event-7367"
}
```



---

archive/issue_events_007368.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-25T09:15:16Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "milestone": "sage-3.0.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3276#event-7368"
}
```



---

archive/issue_events_007369.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-25T09:15:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3276#event-7369"
}
```



---

archive/issue_comments_022620.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T09:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22620",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1
