# Issue 8862: failing resolution of a nonlinear system by solve

Issue created by migration from Trac.

Original creator: casamayou

Original creation time: 2010-05-03 19:55:59

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
  [This is the Trac macro *x == 0, y == 0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x == 0, y == 0-macro) 
```



---

Comment by zimmerma created at 2010-05-03 20:44:26

Changing priority from minor to major.


---

Comment by zimmerma created at 2010-05-03 20:44:26

Changing type from enhancement to defect.


---

Comment by burcin created at 2010-05-04 23:39:39

What is the expected improvement in this ticket?

The `solve()` function in Sage is just a wrapper around maxima for now. In this case we just return the result from maxima.

There are two problems here:
 * maxima's solve() cannot handle the given input, probably symbolic exponents defeat it
 * maxima's solve() can return undefined points as output (#2617)

If this ticket is about improving the capabilities of solve to handle the given input properly, this is an enhancement request. Do we know of any algorithm that will help with this? 

Otherwise, this ticket is a duplicate of #2617.

Comments?


---

Comment by zimmerma created at 2010-05-05 06:47:36

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

Comment by burcin created at 2010-05-06 17:07:43

Replying to [comment:3 zimmerma]:
> the issue here is not only that Sage returns undefined points (which indeed duplicates #2617) but
> that it fails to find the following (trivial) solutions, which is a defect:
<snip>
> When some solutions are lost, at least a warning should be issued.

I don't think we can get that information out of maxima. Can someone more experienced in maxima comment on this? Or ask the maxima developers what they think about this problem?

Another option is to take this as an opportunity to start implementing some native `solve()` functionality in Sage. I have no idea how to (more or less algorithmically) find a solution to this system though. I'd appreciate any pointers.


---

Comment by kcrisman created at 2011-03-16 16:10:22


```
Maxima 5.23.2 http://maxima.sourceforge.net
using Lisp ECL 11.1.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) solve([(2*x^2/(x^2 + y^2) + log(x^2 + y^2))*(x^2 + y^2)^x,2*x*y*(x^2 + y^2)^(x - 1)],[x,y]);
(%o1)                          [This is the Trac macro *x = 0, y = 0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x = 0, y = 0-macro)
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

Comment by mafra created at 2016-10-07 23:04:10

Just a random comment: sympy can solve this. I tested it in the 'live shell' in their webpage:



```
solve([(x**2 + y**2)**x*(2*x**2/(x**2 + y**2) + log(x**2 + y**2)),2*(x**2 + y**2)**(x - 1)*x*y],x,y)
[(0,−1),(0,1),(−1/e,0),(1/e,0)]
```


(I edited the output because copy&paste mangled it).

It would be nice to have an 'algorithm=sympy' option to solve(). It seems that nobody is working in the Maxima bug.
