# Issue 4544: comparison of CDF (or any inexact) elements needs work

Issue created by migration from https://trac.sagemath.org/ticket/4544

Original creator: craigcitro

Original creation time: 2008-11-18 09:28:24

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


Notice that the `+`/`-` ordering is different for the two pairs of complex conjugate roots. What we *should* do is pass a parameter to `__cmp__` that describes a threshold such that if the difference is smaller than this threshold in absolute value, things compare equal. This could even be a parameter to the ring.

There are a ton of questions this brings up, such as, "how is this done in other systems?" Notice this also underlies the following confusing result:


```
sage: [ f(x[0]).is_zero() for x in f.roots() ]
[False, False, False, False, False]
```


Someone should do some research and start a sage-devel conversation, probably. 


---

Comment by craigcitro created at 2008-11-18 09:30:35

Note: this was also part of the problem underlying #4469. In particular, two things need to happen to fix #4469 properly:

 * in `sage/rings/polynomial/polynomial_element.pyx`, the `roots` function should also call `crts.sort()`.

 * someone should fix this bug, so that we *actually* have something resembling dictionary order on `CDF`, as claimed in the `_cmp_` method for `CDF` elements.


---

Comment by AlexGhitza created at 2008-11-29 07:09:04

changed the title so it doesn't get picked up by the wrong trac report


---

Attachment

I'm totally unwilling to add some sort of epsilon for complex comparison in general; it's just a bad idea.

However, the goal of sorting the output of .roots() is not so bad, and I'm willing to put an epsilon comparison in that sorting routine (since it's basically only for display, and especially since it helps doctest consistency); so that's what I've done in the attached patch.


---

Comment by mabshoff created at 2009-02-03 18:33:04

Changing priority from major to blocker.


---

Comment by mabshoff created at 2009-02-03 18:33:04

Carl Witty claims that this ticket will fix #5167, so let's make this a blocker for 3.3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 19:36:41

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

Attachment

Note that the reviewer patch depends on #5129 being applied.

Cheers,

Michael


---

Comment by cwitty created at 2009-02-03 20:07:22

I read the reviewer patch, and it looks good.  (But I haven't tried to actually apply it, or to run doctests.)


---

Comment by mabshoff created at 2009-02-03 20:09:12

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

Comment by mabshoff created at 2009-02-03 20:09:59

Merged both patches in Sage 3.3.alpha5.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 20:09:59

Resolution: fixed
