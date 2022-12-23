# Issue 1235: bug solving equations using maxima

archive/issues_001235.json:
```json
{
    "body": "Assignee: was\n\n\n```\nOn Nov 20, 2007 12:28 PM, Ted Kosan <ted.kosan@gmail.com> wrote:\n> Does anyone have any thoughts on why the solve() function this program\n> returns an empty list?:\n> \n> sage: var('t')\n> sage: a = .004*(8*e^(-(300*t)) - 8*e^(-(1200*t)))*(720000*e^(-(300*t))\n> - 11520000*e^(-(1200*t))) +.004*(9600*e^(-(1200*t)) -\n> 2400*e^(-(300*t)))^2\n> sage: print a(t=.000411)\n> sage: show(plot(a,0,.002),xmin=0, xmax=.002)\n> sage: solve(a==0,t)\n\nMaxima stupidly decides there is no solution.  This is clearly a bug.  This\nis the sort of bug in Sage that is very difficult for us to fix since it's really\na bug in Maxima, and it's entirely possible that maxima developers would\nnot even call it a bug.  But clearly it is, since it's a mathematically incorrect result. \n\nHere's what happens when you try this in Maxima directly:\n\nsage: !maxima\nMaxima 5.13.0 http://maxima.sourceforge.net\nUsing Lisp CLISP 2.41 (2006-10-13)\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThis is a development version of Maxima. The function bug_report()\nprovides bug reporting information.\n(%i1) solve(0.004*(8*%e^-(300*t)-8*%e^-(1200*t))*(720000*%e^-(300*t)-11520000*%e^-(1200*t))+0.004*(9600*%e^-(1200*t)-2400*%e^-(300*t))^2=0, t)\n;\n`rat' replaced 0.004 by 1/250 = 0.004\n`rat' replaced 0.004 by 1/250 = 0.004\n(%o1)                                 []\n\n\nI strongly encourage you to report this to the maxima list, if you agree that it is\na bug in Maxima. \n\nI think in the long-run Sage will have to completely implement its own solve\nfunction, which is better than Maxima's.  Thoughts from Ondrej-sympy would be\nappreciated here. \n\n> And why the solve() function in this program hangs?:\n> \n> sage: var('t')\n> sage: v = 0.004*(9600*e^(-(1200*t)) - 2400*e^(-(300*t)))\n> sage: show(plot(v,0,.002),xmin=0,xmax = .002)\n> sage: solve(v == 0,t)\n\nHere maxima also gives the wrong answer:\n\nsage: maxima(v == 0)\n0.004*(9600*%e^-(1200*t)-2400*%e^-(300*t))=0\nsage: maxima(v == 0).solve(t)\n[]\n\nJust to emphasize that in my opinion this is *definitely* a bug,\nI've entered this into the tracker:\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1235\n\n",
    "created_at": "2007-11-21T16:08:22Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "bug solving equations using maxima",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1235",
    "user": "was"
}
```
Assignee: was


```
On Nov 20, 2007 12:28 PM, Ted Kosan <ted.kosan@gmail.com> wrote:
> Does anyone have any thoughts on why the solve() function this program
> returns an empty list?:
> 
> sage: var('t')
> sage: a = .004*(8*e^(-(300*t)) - 8*e^(-(1200*t)))*(720000*e^(-(300*t))
> - 11520000*e^(-(1200*t))) +.004*(9600*e^(-(1200*t)) -
> 2400*e^(-(300*t)))^2
> sage: print a(t=.000411)
> sage: show(plot(a,0,.002),xmin=0, xmax=.002)
> sage: solve(a==0,t)

Maxima stupidly decides there is no solution.  This is clearly a bug.  This
is the sort of bug in Sage that is very difficult for us to fix since it's really
a bug in Maxima, and it's entirely possible that maxima developers would
not even call it a bug.  But clearly it is, since it's a mathematically incorrect result. 

Here's what happens when you try this in Maxima directly:

sage: !maxima
Maxima 5.13.0 http://maxima.sourceforge.net
Using Lisp CLISP 2.41 (2006-10-13)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) solve(0.004*(8*%e^-(300*t)-8*%e^-(1200*t))*(720000*%e^-(300*t)-11520000*%e^-(1200*t))+0.004*(9600*%e^-(1200*t)-2400*%e^-(300*t))^2=0, t)
;
`rat' replaced 0.004 by 1/250 = 0.004
`rat' replaced 0.004 by 1/250 = 0.004
(%o1)                                 []


I strongly encourage you to report this to the maxima list, if you agree that it is
a bug in Maxima. 

I think in the long-run Sage will have to completely implement its own solve
function, which is better than Maxima's.  Thoughts from Ondrej-sympy would be
appreciated here. 

> And why the solve() function in this program hangs?:
> 
> sage: var('t')
> sage: v = 0.004*(9600*e^(-(1200*t)) - 2400*e^(-(300*t)))
> sage: show(plot(v,0,.002),xmin=0,xmax = .002)
> sage: solve(v == 0,t)

Here maxima also gives the wrong answer:

sage: maxima(v == 0)
0.004*(9600*%e^-(1200*t)-2400*%e^-(300*t))=0
sage: maxima(v == 0).solve(t)
[]

Just to emphasize that in my opinion this is *definitely* a bug,
I've entered this into the tracker:

```


Issue created by migration from https://trac.sagemath.org/ticket/1235





---

archive/issue_comments_007705.json:
```json
{
    "body": "\n```\nWilliam Stein to sage-support\n\t\nshow details 8:35 AM (1 minute ago)\n\t\n\t\n\t\nReply\n\t\n\t\nOn Nov 21, 2007 8:24 AM, Ondrej Certik <ondrej@certik.cz> wrote:\n>\n> > I think in the long-run Sage will have to completely implement its own solve\n> > function, which is better than Maxima's.  Thoughts from Ondrej-sympy would be\n> > appreciated here.\n>\n>\n> Isn't solve supposed to return an analylic solution only? Is there an\n> analytic solution to this equation? It doesn't seem so to me.\n\nI don't like that meaning for solve, since it is misleading to me, and\nis inconsistent. e.g., what about:\n\nsage: solve(x^5 + x^3 + 1, x)\n[0 == x^5 + x^3 + 1]\n\nWhen there is no explicit solution, maxima usually returns something\nto explicitly indicate this.\n\nAlso, as a data point, Maple returns an approximate solution if\nit doesn't find an exact one:\n\nsage: maple.eval('solve(38.40000000*exp(1)^(-1200*t)-9.600000000*exp(1)^(-300*t),\nt)')\n'.1540327068e-2'\n\nLikewise with Mathematica:\n\nsage: mathematica.eval('Solve[0.004*(9600/E^(1200*t) - 2400/E^(300*t))\n## 0, t]')\n\nSolve::ifun: Inverse functions are being used by Solve, so some solutions may\n    not be found; use Reduce for complete solution information.\n\n        {{t -> 0.00154033}}\n\n\nsage: mathematica('x^5 + x^3 + 1 == 0').Solve(x)\n\n{{x -> Root[1 + #1^3 + #1^5 & , 1, 0]},\n {x -> Root[1 + #1^3 + #1^5 & , 2, 0]},\n {x -> Root[1 + #1^3 + #1^5 & , 3, 0]},\n {x -> Root[1 + #1^3 + #1^5 & , 4, 0]}, {x -> Root[1 + #1^3 + #1^5 & , 5, 0]}}\n\n\n\n> My thoughts on these issues are still the same - slowly replacing\n> Maxima with our own things in Python, that are easy to fix and easy to\n> extend. But they need to do the same things as Maxima first (and be as\n> fast as Maxima).\n\nShouldn't we be able to write something that is way faster than Maxima?\nWhat do people even benchmark in the context of calculus?\n\n\n```\n",
    "created_at": "2007-11-21T17:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7705",
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

archive/issue_comments_007706.json:
```json
{
    "body": "The following is relevant:\n\n\n```\nsage: var('t')\nsage: a = .004*(8*e^(-(300*t)) - 8*e^(-(1200*t)))*(720000*e^(-(300*t)) - 11520000*e^(-(1200*t))) +.004*(9600*e^(-(1200*t)) - 2400*e^(-(300*t)))^2\nsage: from scipy.optimize import brentq\nsage: # Given two points x, y such that a(x) and a(y) have different sign, this\nsage: # brentq uses \"inverse quadratic extrapolation\" to find a root of a in the\nsage: # interval [x,y].  It has lots of extra tolerance and other options.\nsage: brentq(a, 0, 0.002)\n0.00041105140493493411\nsage: show(plot(a,0,.002),xmin=0, xmax=.002)\n```\n",
    "created_at": "2007-11-27T15:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7706",
    "user": "was"
}
```

The following is relevant:


```
sage: var('t')
sage: a = .004*(8*e^(-(300*t)) - 8*e^(-(1200*t)))*(720000*e^(-(300*t)) - 11520000*e^(-(1200*t))) +.004*(9600*e^(-(1200*t)) - 2400*e^(-(300*t)))^2
sage: from scipy.optimize import brentq
sage: # Given two points x, y such that a(x) and a(y) have different sign, this
sage: # brentq uses "inverse quadratic extrapolation" to find a root of a in the
sage: # interval [x,y].  It has lots of extra tolerance and other options.
sage: brentq(a, 0, 0.002)
0.00041105140493493411
sage: show(plot(a,0,.002),xmin=0, xmax=.002)
```




---

archive/issue_comments_007707.json:
```json
{
    "body": "\n```\nI don't know.  However, Ted, what do you think of the following, i.e.,\nit is a way in Sage to solve your problem which is probably pretty\nclean and flexible, and could certainly made a little more student\nfriendly?\n\nsage: var('t')\nsage: a = .004*(8*e^(-(300*t)) - 8*e^(-(1200*t)))*(720000*e^(-(300*t))\n- 11520000*e^(-(1200*t))) +.004*(9600*e^(-(1200*t)) -\n2400*e^(-(300*t)))^2\nsage: from scipy.optimize import brentq\nsage: # Given two points x, y such that a(x) and a(y) have different sign, this\nsage: # brentq uses \"inverse quadratic extrapolation\" to find a root of a in the\nsage: # interval [x,y].  It has lots of extra tolerance and other options.\nsage: brentq(a, 0, 0.002)\n0.00041105140493493411\nsage: show(plot(a,0,.002),xmin=0, xmax=.002)\n\nI.e., what we provide an numerical_root method so that\n    a.numerical_root(x,y)\nwould fine a numerical root of a in the interval [x,y], if it exists?\nIt could be built on brentq.  The main thing we would have to add\nis some sort of analysis to find x', y' in the interval so that a(x')\nhas different sign from a(y'), i.e., decide if there is a sign switch,\nwhich could be doable for many analytically defined functions at least.\n```\n",
    "created_at": "2007-11-27T15:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7707",
    "user": "was"
}
```


```
I don't know.  However, Ted, what do you think of the following, i.e.,
it is a way in Sage to solve your problem which is probably pretty
clean and flexible, and could certainly made a little more student
friendly?

sage: var('t')
sage: a = .004*(8*e^(-(300*t)) - 8*e^(-(1200*t)))*(720000*e^(-(300*t))
- 11520000*e^(-(1200*t))) +.004*(9600*e^(-(1200*t)) -
2400*e^(-(300*t)))^2
sage: from scipy.optimize import brentq
sage: # Given two points x, y such that a(x) and a(y) have different sign, this
sage: # brentq uses "inverse quadratic extrapolation" to find a root of a in the
sage: # interval [x,y].  It has lots of extra tolerance and other options.
sage: brentq(a, 0, 0.002)
0.00041105140493493411
sage: show(plot(a,0,.002),xmin=0, xmax=.002)

I.e., what we provide an numerical_root method so that
    a.numerical_root(x,y)
would fine a numerical root of a in the interval [x,y], if it exists?
It could be built on brentq.  The main thing we would have to add
is some sort of analysis to find x', y' in the interval so that a(x')
has different sign from a(y'), i.e., decide if there is a sign switch,
which could be doable for many analytically defined functions at least.
```




---

archive/issue_comments_007708.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-08T08:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7708",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_007709.json:
```json
{
    "body": "Attachment\n\nSeems good to me. Tested the patch (both parts).\nIt appears to work robustly in the cases I tried.",
    "created_at": "2007-12-08T09:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7709",
    "user": "jkantor"
}
```

Attachment

Seems good to me. Tested the patch (both parts).
It appears to work robustly in the cases I tried.



---

archive/issue_comments_007710.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-09T13:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7710",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007711.json:
```json
{
    "body": "Merged in 2.9.alpha2.",
    "created_at": "2007-12-09T13:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7711",
    "user": "mabshoff"
}
```

Merged in 2.9.alpha2.



---

archive/issue_comments_007712.json:
```json
{
    "body": "Attachment\n\nThis fixes a doctest failure on Redhat Linux 32-bit.",
    "created_at": "2007-12-10T15:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7712",
    "user": "was"
}
```

Attachment

This fixes a doctest failure on Redhat Linux 32-bit.



---

archive/issue_comments_007713.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-10T15:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7713",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_007714.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-10T15:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7714",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_007715.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-12-10T15:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7715",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_007716.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-10T21:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7716",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007717.json:
```json
{
    "body": "Merged trac-1235-doctest_fix.patch   in 2.9.alpha5.",
    "created_at": "2007-12-10T21:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1235#issuecomment-7717",
    "user": "mabshoff"
}
```

Merged trac-1235-doctest_fix.patch   in 2.9.alpha5.
