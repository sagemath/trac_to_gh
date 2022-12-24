# Issue 1236: tate pairings on elliptic curves -- add to sage

archive/issues_001236.json:
```json
{
    "body": "Assignee: was\n\nCC:  cremona mariah aly.deines jdemeyer\n\n\n```\n\nHi, I needed some calculation period benchmark for pairings. I could\nnot find anything build in, but the following implementation solved my\nproblem:\n\nhttp://maths.straylight.co.uk/archives/104\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1236\n\n",
    "created_at": "2007-11-21T16:22:42Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "tate pairings on elliptic curves -- add to sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1236",
    "user": "was"
}
```
Assignee: was

CC:  cremona mariah aly.deines jdemeyer


```

Hi, I needed some calculation period benchmark for pairings. I could
not find anything build in, but the following implementation solved my
problem:

http://maths.straylight.co.uk/archives/104
```


Issue created by migration from https://trac.sagemath.org/ticket/1236





---

archive/issue_comments_007718.json:
```json
{
    "body": "\n```\n\nThanks!  I've made adding this to Sage proper ticket\n\n   http://trac.sagemath.org/sage_trac/ticket/1236\n\nCan you make some sort of GPL-compatible license statement about your code,\nif you haven't already?\n\nWilliam\n```\n",
    "created_at": "2007-11-21T16:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7718",
    "user": "was"
}
```


```

Thanks!  I've made adding this to Sage proper ticket

   http://trac.sagemath.org/sage_trac/ticket/1236

Can you make some sort of GPL-compatible license statement about your code,
if you haven't already?

William
```




---

archive/issue_comments_007719.json:
```json
{
    "body": "\n```\nWilliam Stein to sage-support\n\t\nshow details 8:35 AM (1 minute ago)\n\t\n\t\n\t\nReply\n\t\n\t\nOn Nov 21, 2007 8:24 AM, Ondrej Certik <ondrej@certik.cz> wrote:\n>\n> > I think in the long-run Sage will have to completely implement its own solve\n> > function, which is better than Maxima's.  Thoughts from Ondrej-sympy would be\n> > appreciated here.\n>\n>\n> Isn't solve supposed to return an analylic solution only? Is there an\n> analytic solution to this equation? It doesn't seem so to me.\n\nI don't like that meaning for solve, since it is misleading to me, and\nis inconsistent. e.g., what about:\n\nsage: solve(x^5 + x^3 + 1, x)\n[0 == x^5 + x^3 + 1]\n\nWhen there is no explicit solution, maxima usually returns something\nto explicitly indicate this.\n\nAlso, as a data point, Maple returns an approximate solution if\nit doesn't find an exact one:\n\nsage: maple.eval('solve(38.40000000*exp(1)^(-1200*t)-9.600000000*exp(1)^(-300*t),\nt)')\n'.1540327068e-2'\n\nLikewise with Mathematica:\n\nsage: mathematica.eval('Solve[0.004*(9600/E^(1200*t) - 2400/E^(300*t))\n## 0, t]')\n\nSolve::ifun: Inverse functions are being used by Solve, so some solutions may\n    not be found; use Reduce for complete solution information.\n\n        {{t -> 0.00154033}}\n\n\nsage: mathematica('x^5 + x^3 + 1 == 0').Solve(x)\n\n{{x -> Root[1 + #1^3 + #1^5 & , 1, 0]},\n {x -> Root[1 + #1^3 + #1^5 & , 2, 0]},\n {x -> Root[1 + #1^3 + #1^5 & , 3, 0]},\n {x -> Root[1 + #1^3 + #1^5 & , 4, 0]}, {x -> Root[1 + #1^3 + #1^5 & , 5, 0]}}\n\n\n\n> My thoughts on these issues are still the same - slowly replacing\n> Maxima with our own things in Python, that are easy to fix and easy to\n> extend. But they need to do the same things as Maxima first (and be as\n> fast as Maxima).\n\nShouldn't we be able to write something that is way faster than Maxima?\nWhat do people even benchmark in the context of calculus?\n\n\n```\n",
    "created_at": "2007-11-21T16:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7719",
    "user": "was"
}
```


```
William Stein to sage-support
	
show details 8:35 AM (1 minute ago)
	
	
	
Reply
	
	
On Nov 21, 2007 8:24 AM, Ondrej Certik <ondrej@certik.cz> wrote:
>
> > I think in the long-run Sage will have to completely implement its own solve
> > function, which is better than Maxima's.  Thoughts from Ondrej-sympy would be
> > appreciated here.
>
>
> Isn't solve supposed to return an analylic solution only? Is there an
> analytic solution to this equation? It doesn't seem so to me.

I don't like that meaning for solve, since it is misleading to me, and
is inconsistent. e.g., what about:

sage: solve(x^5 + x^3 + 1, x)
[0 == x^5 + x^3 + 1]

When there is no explicit solution, maxima usually returns something
to explicitly indicate this.

Also, as a data point, Maple returns an approximate solution if
it doesn't find an exact one:

sage: maple.eval('solve(38.40000000*exp(1)^(-1200*t)-9.600000000*exp(1)^(-300*t),
t)')
'.1540327068e-2'

Likewise with Mathematica:

sage: mathematica.eval('Solve[0.004*(9600/E^(1200*t) - 2400/E^(300*t))
## 0, t]')

Solve::ifun: Inverse functions are being used by Solve, so some solutions may
    not be found; use Reduce for complete solution information.

        {{t -> 0.00154033}}


sage: mathematica('x^5 + x^3 + 1 == 0').Solve(x)

{{x -> Root[1 + #1^3 + #1^5 & , 1, 0]},
 {x -> Root[1 + #1^3 + #1^5 & , 2, 0]},
 {x -> Root[1 + #1^3 + #1^5 & , 3, 0]},
 {x -> Root[1 + #1^3 + #1^5 & , 4, 0]}, {x -> Root[1 + #1^3 + #1^5 & , 5, 0]}}



> My thoughts on these issues are still the same - slowly replacing
> Maxima with our own things in Python, that are easy to fix and easy to
> extend. But they need to do the same things as Maxima first (and be as
> fast as Maxima).

Shouldn't we be able to write something that is way faster than Maxima?
What do people even benchmark in the context of calculus?


```




---

archive/issue_comments_007720.json:
```json
{
    "body": "disregard above comment",
    "created_at": "2007-11-21T17:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7720",
    "user": "was"
}
```

disregard above comment



---

archive/issue_comments_007721.json:
```json
{
    "body": "Assigned to new \"elliptic curves\" component.",
    "created_at": "2009-07-20T19:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7721",
    "user": "davidloeffler"
}
```

Assigned to new "elliptic curves" component.



---

archive/issue_comments_007722.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-20T19:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7722",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_007723.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7723",
    "user": "davidloeffler"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_007724.json:
```json
{
    "body": "Remove assignee davidloeffler.",
    "created_at": "2009-10-09T09:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7724",
    "user": "davidloeffler"
}
```

Remove assignee davidloeffler.



---

archive/issue_comments_007725.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-08-31T12:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7725",
    "user": "zimmerma"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_007726.json:
```json
{
    "body": "should this ticket be closed now that #10912 is fixed?\n\nPaul",
    "created_at": "2011-08-31T12:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7726",
    "user": "zimmerma"
}
```

should this ticket be closed now that #10912 is fixed?

Paul



---

archive/issue_comments_007727.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-09-16T09:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7727",
    "user": "nestibal"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_007728.json:
```json
{
    "body": "Weil, Tate and ate pairings are know implemented in sage. I think this ticket may be closed.\n\nThe reference\n  [http://maths.straylight.co.uk/archives/104](http://maths.straylight.co.uk/archives/104)\nshows implementation using elliptic net. This is not in sage now but this is not needed for the Tate pairing.",
    "created_at": "2011-09-16T09:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7728",
    "user": "nestibal"
}
```

Weil, Tate and ate pairings are know implemented in sage. I think this ticket may be closed.

The reference
  [http://maths.straylight.co.uk/archives/104](http://maths.straylight.co.uk/archives/104)
shows implementation using elliptic net. This is not in sage now but this is not needed for the Tate pairing.



---

archive/issue_comments_007729.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-11-19T04:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7729",
    "user": "roed"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_007730.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-11-26T13:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1236#issuecomment-7730",
    "user": "jdemeyer"
}
```

Resolution: duplicate
