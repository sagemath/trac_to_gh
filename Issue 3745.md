# Issue 3745: calculus -- bug in solve

archive/issues_003745.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n```\nOn Tue, Jul 29, 2008 at 6:05 PM, jamlatino <medrano.antonio@gmail.com> wrote:\n>\n> While working on the video tutorial for Sage I tried the following\n> equation:\n>\n> (sin(x) - 8*cos(x)*sin(x))*(sin(x)^2 + cos(x)) - (2*cos(x)*sin(x) -\n> sin(x))*(-2*sin(x)^2 + 2*cos(x)^2 - cos(x))\n>\n> if I use find_root in the interval 1,2 I get the following answer:\n> 1.9106332362490561\n>\n> but when I use solve to find the solution I get\n> [x == pi, x == pi/2, x == 0]\n>\n> pi/2 is 1.57, but when I try find_root in the interval 1.5,1.6 it\n> tells me that the equation has no zero in that interval, can someone\n> explain??\n\nThis appears to me to be a bug as pi/2 is not a solution.\nIf you do the following it is pretty clear that the 0's are\nat 0, 1.9..., etc. and not at pi/2:\n\nsage: f = (sin(x) - 8*cos(x)*sin(x))*(sin(x)^2 + cos(x)) -\n(2*cos(x)*sin(x) - sin(x))*(-2*sin(x)^2 + 2*cos(x)^2 - cos(x))\nsage: f(pi/2)\n-1\nsage: f.plot(-1,4)\n\nSage finds the numerical 0's using a numerical root\nfinder (from scipy).\n\nSage finds the exact solutions by calling the computer\nalgebra system Maxima, which indeed strangely claims that pi/2 is a solution:\n\n(%i1) solve((sin(x)-8*cos(x)*sin(x))*(sin(x)^2+cos(x))-(2*cos(x)*sin(x)-sin(x))*(-2*sin(x)^2+2*cos(x)^2-cos(x))=0,\nx);\n\n`solve' is using arc-trig functions to get a solution.\nSome solutions will be lost.\n                                        %pi\n(%o1)                      [x = %pi, x = ---, x = 0]\n                                         2\n\nIt looks like this might be a bug in Maxima's solve function.\n\nThere's not much for me to do besides:\n  * report this to the maxima folks (I've cc'd Robert Dodier\nin this email),\n  * completely rewrite Sage's solve to not use Maxima.\n\nFrom Robert Dodier:\n\n\nYup, that's a bug, all right ... I'll make a bug report.\n\n>    * completely rewrite Sage's solve to not use Maxima.\n\nWell, if you do that, please write it in pure Python so it is easier\nto translate to Lisp.\n\nMaxima's code for solving equations has more than a few bugs,\nand it's not clear what classes of problems it can handle, nor is\nit clear what method is used for each class, and there certainly\nare interesting and useful equations which it just can't handle.\nAll of this motivates a complete rewrite. Not that I'm volunteering;\nnot yet, anyway.\n\nFWIW\n\nRobert Dodier\n```\n\nI think we need to rewrite solve for Sage.  Any volunteers?  It will have to wait until we change to use either \"Gary's symbolics\" or \"Sympy\" for Sage's symbolics, since the current symbolics likely don't support enough to make implementing solve practical.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3745\n\n",
    "created_at": "2008-07-30T12:45:59Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "calculus -- bug in solve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3745",
    "user": "https://github.com/williamstein"
}
```
Assignee: @garyfurnish

```
On Tue, Jul 29, 2008 at 6:05 PM, jamlatino <medrano.antonio@gmail.com> wrote:
>
> While working on the video tutorial for Sage I tried the following
> equation:
>
> (sin(x) - 8*cos(x)*sin(x))*(sin(x)^2 + cos(x)) - (2*cos(x)*sin(x) -
> sin(x))*(-2*sin(x)^2 + 2*cos(x)^2 - cos(x))
>
> if I use find_root in the interval 1,2 I get the following answer:
> 1.9106332362490561
>
> but when I use solve to find the solution I get
> [x == pi, x == pi/2, x == 0]
>
> pi/2 is 1.57, but when I try find_root in the interval 1.5,1.6 it
> tells me that the equation has no zero in that interval, can someone
> explain??

This appears to me to be a bug as pi/2 is not a solution.
If you do the following it is pretty clear that the 0's are
at 0, 1.9..., etc. and not at pi/2:

sage: f = (sin(x) - 8*cos(x)*sin(x))*(sin(x)^2 + cos(x)) -
(2*cos(x)*sin(x) - sin(x))*(-2*sin(x)^2 + 2*cos(x)^2 - cos(x))
sage: f(pi/2)
-1
sage: f.plot(-1,4)

Sage finds the numerical 0's using a numerical root
finder (from scipy).

Sage finds the exact solutions by calling the computer
algebra system Maxima, which indeed strangely claims that pi/2 is a solution:

(%i1) solve((sin(x)-8*cos(x)*sin(x))*(sin(x)^2+cos(x))-(2*cos(x)*sin(x)-sin(x))*(-2*sin(x)^2+2*cos(x)^2-cos(x))=0,
x);

`solve' is using arc-trig functions to get a solution.
Some solutions will be lost.
                                        %pi
(%o1)                      [x = %pi, x = ---, x = 0]
                                         2

It looks like this might be a bug in Maxima's solve function.

There's not much for me to do besides:
  * report this to the maxima folks (I've cc'd Robert Dodier
in this email),
  * completely rewrite Sage's solve to not use Maxima.

From Robert Dodier:


Yup, that's a bug, all right ... I'll make a bug report.

>    * completely rewrite Sage's solve to not use Maxima.

Well, if you do that, please write it in pure Python so it is easier
to translate to Lisp.

Maxima's code for solving equations has more than a few bugs,
and it's not clear what classes of problems it can handle, nor is
it clear what method is used for each class, and there certainly
are interesting and useful equations which it just can't handle.
All of this motivates a complete rewrite. Not that I'm volunteering;
not yet, anyway.

FWIW

Robert Dodier
```

I think we need to rewrite solve for Sage.  Any volunteers?  It will have to wait until we change to use either "Gary's symbolics" or "Sympy" for Sage's symbolics, since the current symbolics likely don't support enough to make implementing solve practical.

Issue created by migration from https://trac.sagemath.org/ticket/3745





---

archive/issue_comments_026538.json:
```json
{
    "body": "Also:\n\n```\nsage: var('a b c')\nsage: eqn1 = a - exp((-pi*b)/sqrt(1-b)) == 0\nsage: eqn2 = c - atan(2*b*sqrt(1/(sqrt(4*b^4+1) - 2*b^2)))==0\nsage: solve([eqn1,eqn2,a==0.1975],b,c,a) \n[]\n```",
    "created_at": "2008-08-13T00:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3745#issuecomment-26538",
    "user": "https://github.com/rlmill"
}
```

Also:

```
sage: var('a b c')
sage: eqn1 = a - exp((-pi*b)/sqrt(1-b)) == 0
sage: eqn2 = c - atan(2*b*sqrt(1/(sqrt(4*b^4+1) - 2*b^2)))==0
sage: solve([eqn1,eqn2,a==0.1975],b,c,a) 
[]
```



---

archive/issue_comments_026539.json:
```json
{
    "body": "And even:\n\n```\nsage: var('a,b,c,d')\nsage: m = matrix(2,[a,b,c,d])\nsage: i2=identity_matrix(SR,2)\nsage: eqlist=[(m*m).list()[i] - i2.list()[i] for i in range(4)]\nsage: solve(eqlist,a,b,c,d) \nTraceback (most recent call last):\n...\nValueError: Unable to solve [b*c + a^2 - 1, b*d + a*b, c*d + a*c, d^2 + b*c - 1] for (a, b, c, d)\n```",
    "created_at": "2008-08-13T04:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3745#issuecomment-26539",
    "user": "https://github.com/rlmill"
}
```

And even:

```
sage: var('a,b,c,d')
sage: m = matrix(2,[a,b,c,d])
sage: i2=identity_matrix(SR,2)
sage: eqlist=[(m*m).list()[i] - i2.list()[i] for i in range(4)]
sage: solve(eqlist,a,b,c,d) 
Traceback (most recent call last):
...
ValueError: Unable to solve [b*c + a^2 - 1, b*d + a*b, c*d + a*c, d^2 + b*c - 1] for (a, b, c, d)
```



---

archive/issue_comments_026540.json:
```json
{
    "body": "Note this particular bug is still in Maxima as of 5.19.1.  More bugs (but also lots more correct answers) have been introduced in the last year, and other bugs  have been fixed.  Writing a solve from scratch still looks very hard.",
    "created_at": "2009-09-15T18:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3745#issuecomment-26540",
    "user": "https://github.com/kcrisman"
}
```

Note this particular bug is still in Maxima as of 5.19.1.  More bugs (but also lots more correct answers) have been introduced in the last year, and other bugs  have been fixed.  Writing a solve from scratch still looks very hard.



---

archive/issue_comments_026541.json:
```json
{
    "body": "Update from Maxima 5.20.1 in Sage:\n\n```\nsage: sage: var('a,b,c,d')\n(a, b, c, d)\nsage: sage: m = matrix(2,[a,b,c,d])\nsage: sage: i2=identity_matrix(SR,2)\nsage: sage: eqlist=[(m*m).list()[i] - i2.list()[i] for i in range(4)]\nsage: sage: solve(eqlist,a,b,c,d) \n[a^2 + b*c - 1, a*b + b*d, a*c + c*d, b*c + d^2 - 1]\n```\nso this one seems to be working now, at least in the sense that it doesn't throw an error.  \n\nThe second one now causes a hang.\n\nAnd the first one is still there :(",
    "created_at": "2009-12-24T03:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3745#issuecomment-26541",
    "user": "https://github.com/kcrisman"
}
```

Update from Maxima 5.20.1 in Sage:

```
sage: sage: var('a,b,c,d')
(a, b, c, d)
sage: sage: m = matrix(2,[a,b,c,d])
sage: sage: i2=identity_matrix(SR,2)
sage: sage: eqlist=[(m*m).list()[i] - i2.list()[i] for i in range(4)]
sage: sage: solve(eqlist,a,b,c,d) 
[a^2 + b*c - 1, a*b + b*d, a*c + c*d, b*c + d^2 - 1]
```
so this one seems to be working now, at least in the sense that it doesn't throw an error.  

The second one now causes a hang.

And the first one is still there :(



---

archive/issue_comments_026542.json:
```json
{
    "body": "<irrelevant rant>\nWe should write our own native solve from scratch.  Depending on maxima for solve is silly, for several reasons:\n\n* For algebraic systems we could do much better using Groebner basis and singular. \n\n* Coefficients for symbolic expressions can be in many base rings that don't even make sense to Maxima.\n\n</irrelevant rant>",
    "created_at": "2009-12-24T20:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3745#issuecomment-26542",
    "user": "https://github.com/williamstein"
}
```

<irrelevant rant>
We should write our own native solve from scratch.  Depending on maxima for solve is silly, for several reasons:

* For algebraic systems we could do much better using Groebner basis and singular. 

* Coefficients for symbolic expressions can be in many base rings that don't even make sense to Maxima.

</irrelevant rant>



---

archive/issue_comments_026543.json:
```json
{
    "body": "It could be worth trying these with #13364.",
    "created_at": "2013-01-20T01:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3745#issuecomment-26543",
    "user": "https://github.com/kcrisman"
}
```

It could be worth trying these with #13364.



---

archive/issue_events_008578.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3745#event-8578"
}
```



---

archive/issue_events_008579.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3745#event-8579"
}
```



---

archive/issue_events_008580.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3745#event-8580"
}
```



---

archive/issue_events_008581.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3745#event-8581"
}
```



---

archive/issue_events_008582.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3745#event-8582"
}
```



---

archive/issue_events_008583.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3745#event-8583"
}
```



---

archive/issue_events_008584.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3745#event-8584"
}
```



---

archive/issue_comments_026544.json:
```json
{
    "body": "https://sourceforge.net/p/maxima/bugs/2846/",
    "created_at": "2014-11-21T13:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3745#issuecomment-26544",
    "user": "https://github.com/kcrisman"
}
```

https://sourceforge.net/p/maxima/bugs/2846/



---

archive/issue_comments_026545.json:
```json
{
    "body": "The one in comment:1 hangs for me as before, but upon Ctrl-C it does give `[]`.  For what it's worth.  Though in Maxima I got \n\n```\n(%i1) solve([a - exp((-pi*b)/sqrt(1-b)) = 0, c - atan(2*b*sqrt(1/(sqrt(4*b^4+1) - 2*b^2)))=0,a=0.1975],[b,c,a]);\n\nrat: replaced -0.1975 by -79/400 = -0.1975\n(%o1)                                 []\n```\nalmost immediately.  So I'm not sure why it hangs.  Is there even a solution to that?  It seems quite arbitrary.",
    "created_at": "2014-11-21T13:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3745#issuecomment-26545",
    "user": "https://github.com/kcrisman"
}
```

The one in comment:1 hangs for me as before, but upon Ctrl-C it does give `[]`.  For what it's worth.  Though in Maxima I got 

```
(%i1) solve([a - exp((-pi*b)/sqrt(1-b)) = 0, c - atan(2*b*sqrt(1/(sqrt(4*b^4+1) - 2*b^2)))=0,a=0.1975],[b,c,a]);

rat: replaced -0.1975 by -79/400 = -0.1975
(%o1)                                 []
```
almost immediately.  So I'm not sure why it hangs.  Is there even a solution to that?  It seems quite arbitrary.



---

archive/issue_comments_026546.json:
```json
{
    "body": "> https://sourceforge.net/p/maxima/bugs/2846/\n\nBy the way, in the original report which has been erased, a Maxima dev suggested he'd reported this, so perhaps this is redundant, but I don't know where it would be.",
    "created_at": "2014-11-21T13:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3745#issuecomment-26546",
    "user": "https://github.com/kcrisman"
}
```

> https://sourceforge.net/p/maxima/bugs/2846/

By the way, in the original report which has been erased, a Maxima dev suggested he'd reported this, so perhaps this is redundant, but I don't know where it would be.



---

archive/issue_comments_026547.json:
```json
{
    "body": "I would like to point out that this bug still exists, 7 years later. There were a couple other cases of maxima's solve giving an incorrect answer (for eg, giving 0 when the function is undefined at 0). I am interested in studying this problem, does anyone have any recommendations on what would make for a better equation solver? And, if possible, some information on why Maxima's isn't great?",
    "created_at": "2016-11-27T01:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3745#issuecomment-26547",
    "user": "https://trac.sagemath.org/admin/accounts/users/zonova"
}
```

I would like to point out that this bug still exists, 7 years later. There were a couple other cases of maxima's solve giving an incorrect answer (for eg, giving 0 when the function is undefined at 0). I am interested in studying this problem, does anyone have any recommendations on what would make for a better equation solver? And, if possible, some information on why Maxima's isn't great?



---

archive/issue_comments_026548.json:
```json
{
    "body": "Basically, the short answer is that solving in general cases isn't easy.  The long answer is that Maxima's is reasonable but often has small changes that impact other things.  You are likely to get some response on the Maxima email list if you mention this bug.  But writing a new one from scratch isn't a good idea; on the other hand, perhaps [sympy](http://www.sympy.org/en/index.html)'s solver is now ready to swap in for Maxima's in Sage, I don't know.  We do have both available.",
    "created_at": "2016-11-28T15:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3745#issuecomment-26548",
    "user": "https://github.com/kcrisman"
}
```

Basically, the short answer is that solving in general cases isn't easy.  The long answer is that Maxima's is reasonable but often has small changes that impact other things.  You are likely to get some response on the Maxima email list if you mention this bug.  But writing a new one from scratch isn't a good idea; on the other hand, perhaps [sympy](http://www.sympy.org/en/index.html)'s solver is now ready to swap in for Maxima's in Sage, I don't know.  We do have both available.
