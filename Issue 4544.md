# Issue 4544: comparison of CDF (or any inexact) elements needs work

archive/issues_004544.json:
```json
{
    "body": "Assignee: jkantor\n\nSo currently, we compare elements of inexact rings like `CDF` by just comparing their components as `double`s. We use this for sorting, and expect the results to be consistent between runs, architectures, etc. However, this is wildly untrue. Here's a good example:\n\n\n```\nsage: z1, z2 = [ x[0] for x in f.roots()[-2:] ]\nsage: R = CDF['x']\nsage: f = R([17,1,0,0,0,1]) ; f\n1.0*x^5 + 1.0*x + 17.0\nsage: f.roots()\n[(-1.72502775061, 1),\n (1.4372759883 + 1.06991737978*I, 1),\n (1.4372759883 - 1.06991737978*I, 1),\n (-0.574762112991 + 1.65506825348*I, 1),\n (-0.574762112991 - 1.65506825348*I, 1)]\nsage: z1, z2 = [ x[0] for x in f.roots()[-2:] ]\nsage: z1\n-0.574762112991 + 1.65506825348*I\nsage: z2\n-0.574762112991 - 1.65506825348*I\nsage: z1.real() == z2.real()\nFalse\n```\n\n\nNotice that the `+`/`-` ordering is different for the two pairs of complex conjugate roots. What we **should** do is pass a parameter to `__cmp__` that describes a threshold such that if the difference is smaller than this threshold in absolute value, things compare equal. This could even be a parameter to the ring.\n\nThere are a ton of questions this brings up, such as, \"how is this done in other systems?\" Notice this also underlies the following confusing result:\n\n\n```\nsage: [ f(x[0]).is_zero() for x in f.roots() ]\n[False, False, False, False, False]\n```\n\n\nSomeone should do some research and start a sage-devel conversation, probably. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4544\n\n",
    "created_at": "2008-11-18T09:28:24Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "comparison of CDF (or any inexact) elements needs work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4544",
    "user": "https://github.com/craigcitro"
}
```
Assignee: jkantor

So currently, we compare elements of inexact rings like `CDF` by just comparing their components as `double`s. We use this for sorting, and expect the results to be consistent between runs, architectures, etc. However, this is wildly untrue. Here's a good example:


```
sage: z1, z2 = [ x[0] for x in f.roots()[-2:] ]
sage: R = CDF['x']
sage: f = R([17,1,0,0,0,1]) ; f
1.0*x^5 + 1.0*x + 17.0
sage: f.roots()
[(-1.72502775061, 1),
 (1.4372759883 + 1.06991737978*I, 1),
 (1.4372759883 - 1.06991737978*I, 1),
 (-0.574762112991 + 1.65506825348*I, 1),
 (-0.574762112991 - 1.65506825348*I, 1)]
sage: z1, z2 = [ x[0] for x in f.roots()[-2:] ]
sage: z1
-0.574762112991 + 1.65506825348*I
sage: z2
-0.574762112991 - 1.65506825348*I
sage: z1.real() == z2.real()
False
```


Notice that the `+`/`-` ordering is different for the two pairs of complex conjugate roots. What we **should** do is pass a parameter to `__cmp__` that describes a threshold such that if the difference is smaller than this threshold in absolute value, things compare equal. This could even be a parameter to the ring.

There are a ton of questions this brings up, such as, "how is this done in other systems?" Notice this also underlies the following confusing result:


```
sage: [ f(x[0]).is_zero() for x in f.roots() ]
[False, False, False, False, False]
```


Someone should do some research and start a sage-devel conversation, probably. 

Issue created by migration from https://trac.sagemath.org/ticket/4544





---

archive/issue_comments_033970.json:
```json
{
    "body": "Note: this was also part of the problem underlying #4469. In particular, two things need to happen to fix #4469 properly:\n\n* in `sage/rings/polynomial/polynomial_element.pyx`, the `roots` function should also call `crts.sort()`.\n\n* someone should fix this bug, so that we **actually** have something resembling dictionary order on `CDF`, as claimed in the `_cmp_` method for `CDF` elements.",
    "created_at": "2008-11-18T09:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4544#issuecomment-33970",
    "user": "https://github.com/craigcitro"
}
```

Note: this was also part of the problem underlying #4469. In particular, two things need to happen to fix #4469 properly:

* in `sage/rings/polynomial/polynomial_element.pyx`, the `roots` function should also call `crts.sort()`.

* someone should fix this bug, so that we **actually** have something resembling dictionary order on `CDF`, as claimed in the `_cmp_` method for `CDF` elements.



---

archive/issue_comments_033971.json:
```json
{
    "body": "changed the title so it doesn't get picked up by the wrong trac report",
    "created_at": "2008-11-29T07:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4544#issuecomment-33971",
    "user": "https://github.com/aghitza"
}
```

changed the title so it doesn't get picked up by the wrong trac report



---

archive/issue_comments_033972.json:
```json
{
    "body": "Attachment [trac4544.patch](tarball://root/attachments/some-uuid/ticket4544/trac4544.patch) by cwitty created at 2009-01-24 06:26:40\n\nI'm totally unwilling to add some sort of epsilon for complex comparison in general; it's just a bad idea.\n\nHowever, the goal of sorting the output of .roots() is not so bad, and I'm willing to put an epsilon comparison in that sorting routine (since it's basically only for display, and especially since it helps doctest consistency); so that's what I've done in the attached patch.",
    "created_at": "2009-01-24T06:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4544#issuecomment-33972",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac4544.patch](tarball://root/attachments/some-uuid/ticket4544/trac4544.patch) by cwitty created at 2009-01-24 06:26:40

I'm totally unwilling to add some sort of epsilon for complex comparison in general; it's just a bad idea.

However, the goal of sorting the output of .roots() is not so bad, and I'm willing to put an epsilon comparison in that sorting routine (since it's basically only for display, and especially since it helps doctest consistency); so that's what I've done in the attached patch.



---

archive/issue_comments_033973.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-02-03T18:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4544#issuecomment-33973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_033974.json:
```json
{
    "body": "Carl Witty claims that this ticket will fix #5167, so let's make this a blocker for 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T18:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4544#issuecomment-33974",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Carl Witty claims that this ticket will fix #5167, so let's make this a blocker for 3.3.

Cheers,

Michael



---

archive/issue_comments_033975.json:
```json
{
    "body": "Patch looks good to me. It applies to my 3.3.alpha5 merge tree, but there is one doctest failure due to recently merged code:\n\n```\nsage -t -long \"devel/sage/sage/calculus/calculus.py\"        \n**********************************************************************\nFile \"/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py\", line 3206:\n    sage: f.roots(ring=CC)\nExpected:\n    [(-0.0588115223184495, 1), (1.36050567903502 + 1.51880872209965*I, 1), (-1.331099917875... + 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1), (-1.33109991787580 - 1.52241655183732*I, 1)]\nGot:\n    [(-0.0588115223184495, 1), (-1.33109991787579 - 1.52241655183732*I, 1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1), (1.36050567903502 + 1.51880872209965*I, 1)]\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py\", line 3210:\n    sage: f.roots(ring=CC, multiplicities=False)\nExpected:\n    [-0.0588115223184495, 1.36050567903502 + 1.51880872209965*I, -1.331099917875... + 1.52241655183732*I, 1.36050567903502 - 1.51880872209965*I, -1.33109991787580 - 1.52241655183732*I]\nGot:\n    [-0.0588115223184495, -1.33109991787579 - 1.52241655183732*I, -1.33109991787579 + 1.52241655183732*I, 1.36050567903502 - 1.51880872209965*I, 1.36050567903502 + 1.51880872209965*I]\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py\", line 3214:\n    sage: f.roots(ring=QQbar, multiplicities=False)\nExpected:\n    [-0.05881152231844944?, 1.360505679035020? + 1.518808722099650?*I, -1.331099917875796? + 1.522416551837318?*I, 1.360505679035020? - 1.518808722099650?*I, -1.331099917875796? - 1.522416551837318?*I]\nGot:\n    [-0.05881152231844944?, -1.331099917875796? - 1.522416551837318?*I, -1.331099917875796? + 1.522416551837318?*I, 1.360505679035020? - 1.518808722099650?*I, 1.360505679035020? + 1.518808722099650?*I]\n**********************************************************************\n```\n\nI will post a reviewers patch to fix that issue shortly.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T19:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4544#issuecomment-33975",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. It applies to my 3.3.alpha5 merge tree, but there is one doctest failure due to recently merged code:

```
sage -t -long "devel/sage/sage/calculus/calculus.py"        
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py", line 3206:
    sage: f.roots(ring=CC)
Expected:
    [(-0.0588115223184495, 1), (1.36050567903502 + 1.51880872209965*I, 1), (-1.331099917875... + 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1), (-1.33109991787580 - 1.52241655183732*I, 1)]
Got:
    [(-0.0588115223184495, 1), (-1.33109991787579 - 1.52241655183732*I, 1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1), (1.36050567903502 + 1.51880872209965*I, 1)]
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py", line 3210:
    sage: f.roots(ring=CC, multiplicities=False)
Expected:
    [-0.0588115223184495, 1.36050567903502 + 1.51880872209965*I, -1.331099917875... + 1.52241655183732*I, 1.36050567903502 - 1.51880872209965*I, -1.33109991787580 - 1.52241655183732*I]
Got:
    [-0.0588115223184495, -1.33109991787579 - 1.52241655183732*I, -1.33109991787579 + 1.52241655183732*I, 1.36050567903502 - 1.51880872209965*I, 1.36050567903502 + 1.51880872209965*I]
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py", line 3214:
    sage: f.roots(ring=QQbar, multiplicities=False)
Expected:
    [-0.05881152231844944?, 1.360505679035020? + 1.518808722099650?*I, -1.331099917875796? + 1.522416551837318?*I, 1.360505679035020? - 1.518808722099650?*I, -1.331099917875796? - 1.522416551837318?*I]
Got:
    [-0.05881152231844944?, -1.331099917875796? - 1.522416551837318?*I, -1.331099917875796? + 1.522416551837318?*I, 1.360505679035020? - 1.518808722099650?*I, 1.360505679035020? + 1.518808722099650?*I]
**********************************************************************
```

I will post a reviewers patch to fix that issue shortly.

Cheers,

Michael



---

archive/issue_comments_033976.json:
```json
{
    "body": "Attachment [trac_4544_reviewer.patch](tarball://root/attachments/some-uuid/ticket4544/trac_4544_reviewer.patch) by mabshoff created at 2009-02-03 19:51:11\n\nNote that the reviewer patch depends on #5129 being applied.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T19:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4544#issuecomment-33976",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4544_reviewer.patch](tarball://root/attachments/some-uuid/ticket4544/trac_4544_reviewer.patch) by mabshoff created at 2009-02-03 19:51:11

Note that the reviewer patch depends on #5129 being applied.

Cheers,

Michael



---

archive/issue_comments_033977.json:
```json
{
    "body": "I read the reviewer patch, and it looks good.  (But I haven't tried to actually apply it, or to run doctests.)",
    "created_at": "2009-02-03T20:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4544#issuecomment-33977",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I read the reviewer patch, and it looks good.  (But I haven't tried to actually apply it, or to run doctests.)



---

archive/issue_comments_033978.json:
```json
{
    "body": "Carl says:\n\n```\n[11:50am] cwitty: I won't have time to actually apply the patch and run doctests until this evening.\n[11:50am] cwitty: Reading the patch, it looks entirely reasonable.\n[11:51am] cwitty: As release manager, will you accept that sort of review?\n[12:01pm] mabs: cwitty: yes\n[12:02pm] mabs: I am just crossing ts and dotting is here \n[12:02pm] mabs: I posted another patch which partially reverted #5129, so it blew up on geom.\n[12:02pm] mabs: Good that I tested \n[12:04pm] cwitty: OK, positive review.\n```\n\nSo we are good to go. Note that one of the issues Craig raises is\n\n```\nsage: [ f(x[0]).is_zero() for x in f.roots() ]\n[False, False, False, False, False]\n```\n\nwhich is not resolved by this ticket.\n\nCraig: If you think this is worth a follow up ticket please open such a ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T20:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4544#issuecomment-33978",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Carl says:

```
[11:50am] cwitty: I won't have time to actually apply the patch and run doctests until this evening.
[11:50am] cwitty: Reading the patch, it looks entirely reasonable.
[11:51am] cwitty: As release manager, will you accept that sort of review?
[12:01pm] mabs: cwitty: yes
[12:02pm] mabs: I am just crossing ts and dotting is here 
[12:02pm] mabs: I posted another patch which partially reverted #5129, so it blew up on geom.
[12:02pm] mabs: Good that I tested 
[12:04pm] cwitty: OK, positive review.
```

So we are good to go. Note that one of the issues Craig raises is

```
sage: [ f(x[0]).is_zero() for x in f.roots() ]
[False, False, False, False, False]
```

which is not resolved by this ticket.

Craig: If you think this is worth a follow up ticket please open such a ticket.

Cheers,

Michael



---

archive/issue_comments_033979.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha5.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T20:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4544#issuecomment-33979",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.alpha5.

Cheers,

Michael



---

archive/issue_events_004789.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-03T20:09:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4544#event-4789"
}
```



---

archive/issue_comments_033980.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-03T20:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4544#issuecomment-33980",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
