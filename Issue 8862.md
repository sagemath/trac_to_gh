# Issue 8862: failing resolution of a nonlinear system by solve

archive/issues_008862.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  kcrisman robert.marik jason\n\nKeywords: solve\n\nWe search the critical points of the function x|-> (x**2 + y**2)^x\n\nThis function has four critical points : \u00b1(0,1) and \u00b1(1/e,0) \n\nHowever the function solve can not find any of this.\n\nMore, solve returns (0,0) which is not a critical point since f is not differentiable at (0,0) !\n\n\n```\n  sage: var('x y')\n  sage: f(x,y) = (x^2 + y^2)^x\n  sage: solve([diff(f(x,y), x), diff(f(x,y), y)], x, y)\n  [[x == 0, y == 0]] \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8862\n\n",
    "created_at": "2010-05-03T19:55:59Z",
    "labels": [
        "calculus",
        "minor",
        "enhancement"
    ],
    "title": "failing resolution of a nonlinear system by solve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8862",
    "user": "casamayou"
}
```
Assignee: burcin

CC:  kcrisman robert.marik jason

Keywords: solve

We search the critical points of the function x|-> (x**2 + y**2)^x

This function has four critical points : ±(0,1) and ±(1/e,0) 

However the function solve can not find any of this.

More, solve returns (0,0) which is not a critical point since f is not differentiable at (0,0) !


```
  sage: var('x y')
  sage: f(x,y) = (x^2 + y^2)^x
  sage: solve([diff(f(x,y), x), diff(f(x,y), y)], x, y)
  [[x == 0, y == 0]] 
```


Issue created by migration from https://trac.sagemath.org/ticket/8862





---

archive/issue_comments_081449.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2010-05-03T20:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8862#issuecomment-81449",
    "user": "zimmerma"
}
```

Changing priority from minor to major.



---

archive/issue_comments_081450.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-05-03T20:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8862#issuecomment-81450",
    "user": "zimmerma"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_081451.json:
```json
{
    "body": "What is the expected improvement in this ticket?\n\nThe `solve()` function in Sage is just a wrapper around maxima for now. In this case we just return the result from maxima.\n\nThere are two problems here:\n* maxima's solve() cannot handle the given input, probably symbolic exponents defeat it\n* maxima's solve() can return undefined points as output (#2617)\n\nIf this ticket is about improving the capabilities of solve to handle the given input properly, this is an enhancement request. Do we know of any algorithm that will help with this? \n\nOtherwise, this ticket is a duplicate of #2617.\n\nComments?",
    "created_at": "2010-05-04T23:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8862#issuecomment-81451",
    "user": "burcin"
}
```

What is the expected improvement in this ticket?

The `solve()` function in Sage is just a wrapper around maxima for now. In this case we just return the result from maxima.

There are two problems here:
* maxima's solve() cannot handle the given input, probably symbolic exponents defeat it
* maxima's solve() can return undefined points as output (#2617)

If this ticket is about improving the capabilities of solve to handle the given input properly, this is an enhancement request. Do we know of any algorithm that will help with this? 

Otherwise, this ticket is a duplicate of #2617.

Comments?



---

archive/issue_comments_081452.json:
```json
{
    "body": "the issue here is not only that Sage returns undefined points (which indeed duplicates #2617) but\nthat it fails to find the following (trivial) solutions, which is a defect:\n\n```\nsage: sys=[diff(f(x,y), x), diff(f(x,y), y)]\nsage: map(lambda s: s.subs(x=0,y=1),sys)\n[0, 0]\nsage: map(lambda s: s.subs(x=0,y=-1),sys)\n[0, 0]\nsage: map(lambda s: s.subs(x=1/e,y=0),sys)\n[0, 0]\nsage: map(lambda s: s.subs(x=-1/e,y=0),sys)\n[0, 0]\n```\n\nFor example Maple finds:\n\n```\n> f := (x,y) -> (x^2 + y^2)^x:                                         \n> solve({diff(f(x,y), x), diff(f(x,y), y)}, {x, y}, Explicit=true);\n                                          exp(1)               exp(1)\n  {x = 0, y = 1}, {x = 0, y = -1}, {x = - ------, y = 0}, {x = ------, y = 0}\n                                          exp(2)               exp(2)\n```\n\nWhen some solutions are lost, at least a warning should be issued.",
    "created_at": "2010-05-05T06:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8862#issuecomment-81452",
    "user": "zimmerma"
}
```

the issue here is not only that Sage returns undefined points (which indeed duplicates #2617) but
that it fails to find the following (trivial) solutions, which is a defect:

```
sage: sys=[diff(f(x,y), x), diff(f(x,y), y)]
sage: map(lambda s: s.subs(x=0,y=1),sys)
[0, 0]
sage: map(lambda s: s.subs(x=0,y=-1),sys)
[0, 0]
sage: map(lambda s: s.subs(x=1/e,y=0),sys)
[0, 0]
sage: map(lambda s: s.subs(x=-1/e,y=0),sys)
[0, 0]
```

For example Maple finds:

```
> f := (x,y) -> (x^2 + y^2)^x:                                         
> solve({diff(f(x,y), x), diff(f(x,y), y)}, {x, y}, Explicit=true);
                                          exp(1)               exp(1)
  {x = 0, y = 1}, {x = 0, y = -1}, {x = - ------, y = 0}, {x = ------, y = 0}
                                          exp(2)               exp(2)
```

When some solutions are lost, at least a warning should be issued.



---

archive/issue_comments_081453.json:
```json
{
    "body": "Replying to [comment:3 zimmerma]:\n> the issue here is not only that Sage returns undefined points (which indeed duplicates #2617) but\n> that it fails to find the following (trivial) solutions, which is a defect:\n<snip>\n> When some solutions are lost, at least a warning should be issued.\n\nI don't think we can get that information out of maxima. Can someone more experienced in maxima comment on this? Or ask the maxima developers what they think about this problem?\n\nAnother option is to take this as an opportunity to start implementing some native `solve()` functionality in Sage. I have no idea how to (more or less algorithmically) find a solution to this system though. I'd appreciate any pointers.",
    "created_at": "2010-05-06T17:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8862#issuecomment-81453",
    "user": "burcin"
}
```

Replying to [comment:3 zimmerma]:
> the issue here is not only that Sage returns undefined points (which indeed duplicates #2617) but
> that it fails to find the following (trivial) solutions, which is a defect:
<snip>
> When some solutions are lost, at least a warning should be issued.

I don't think we can get that information out of maxima. Can someone more experienced in maxima comment on this? Or ask the maxima developers what they think about this problem?

Another option is to take this as an opportunity to start implementing some native `solve()` functionality in Sage. I have no idea how to (more or less algorithmically) find a solution to this system though. I'd appreciate any pointers.



---

archive/issue_comments_081454.json:
```json
{
    "body": "\n```\nMaxima 5.23.2 http://maxima.sourceforge.net\nusing Lisp ECL 11.1.1\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) solve([(2*x^2/(x^2 + y^2) + log(x^2 + y^2))*(x^2 + y^2)^x,2*x*y*(x^2 + y^2)^(x - 1)],[x,y]);\n(%o1)                          [[x = 0, y = 0]]\n```\n\nSo still present in 4.7.alpha1.\n\nThis is a pretty straightforward Maxima bug/enhancement need.   \n\nThe issue about it not being a critical point is irrelevant, since this is exactly equivalent to the uninterpreted\n\n```\nsolve([(2*x^2/(x^2 + y^2) + log(x^2 + y^2))*(x^2 + y^2)^x,2*x*y*(x^2 + y^2)^(x - 1)],[x,y])\n```\n\nSo the relevant problem is that it's returning something not in the domain of the functions in question, which is indeed a problem.  In addition to not finding other solutions.\n\nThis is now Maxima bug [3216684](https://sourceforge.net/tracker/?func=detail&aid=3216684&group_id=4933&atid=104933).",
    "created_at": "2011-03-16T16:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8862#issuecomment-81454",
    "user": "kcrisman"
}
```


```
Maxima 5.23.2 http://maxima.sourceforge.net
using Lisp ECL 11.1.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) solve([(2*x^2/(x^2 + y^2) + log(x^2 + y^2))*(x^2 + y^2)^x,2*x*y*(x^2 + y^2)^(x - 1)],[x,y]);
(%o1)                          [[x = 0, y = 0]]
```

So still present in 4.7.alpha1.

This is a pretty straightforward Maxima bug/enhancement need.   

The issue about it not being a critical point is irrelevant, since this is exactly equivalent to the uninterpreted

```
solve([(2*x^2/(x^2 + y^2) + log(x^2 + y^2))*(x^2 + y^2)^x,2*x*y*(x^2 + y^2)^(x - 1)],[x,y])
```

So the relevant problem is that it's returning something not in the domain of the functions in question, which is indeed a problem.  In addition to not finding other solutions.

This is now Maxima bug [3216684](https://sourceforge.net/tracker/?func=detail&aid=3216684&group_id=4933&atid=104933).



---

archive/issue_comments_081455.json:
```json
{
    "body": "Just a random comment: sympy can solve this. I tested it in the 'live shell' in their webpage:\n\n\n\n```\nsolve([(x**2 + y**2)**x*(2*x**2/(x**2 + y**2) + log(x**2 + y**2)),2*(x**2 + y**2)**(x - 1)*x*y],x,y)\n[(0,\u22121),(0,1),(\u22121/e,0),(1/e,0)]\n```\n\n\n(I edited the output because copy&paste mangled it).\n\nIt would be nice to have an 'algorithm=sympy' option to solve(). It seems that nobody is working in the Maxima bug.",
    "created_at": "2016-10-07T23:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8862#issuecomment-81455",
    "user": "mafra"
}
```

Just a random comment: sympy can solve this. I tested it in the 'live shell' in their webpage:



```
solve([(x**2 + y**2)**x*(2*x**2/(x**2 + y**2) + log(x**2 + y**2)),2*(x**2 + y**2)**(x - 1)*x*y],x,y)
[(0,−1),(0,1),(−1/e,0),(1/e,0)]
```


(I edited the output because copy&paste mangled it).

It would be nice to have an 'algorithm=sympy' option to solve(). It seems that nobody is working in the Maxima bug.
