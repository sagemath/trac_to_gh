# Issue 1456: gaussian_binomial bug

Issue created by migration from https://trac.sagemath.org/ticket/1456

Original creator: wdj

Original creation time: 2007-12-11 01:07:28

Assignee: mhansen

CC:  sage-combinat

There are some problems with the function gaussian_binomial
in sage 2.8.14. The help string contains a typo:

 binom{n}{k}_q = frac{(1-q<sup>m)(1-q</sup>{m-1})... (1-q^{m-r+1})}
                    {(1-q)(1-q^2)... (1-q^r)}.

The typo is that m and r on the RHS should match n and k on the LHS.

I feel that to be useful gaussian_binomial(n,k,q) should work if n
and k are integers and 0<=k<=n, no matter what q is. At the moment,
the function requires q to be an integer but there will be
applications if q is an indeterminate.  Moreover if q = 1 this
should give the ordinary binomial coefficient but the current
implementation fails due to division by zero.

Perhaps the following is one way to improve the
function would be as follows. Then it gives the
correct behavior when q is an indeterminate or q=1.

Why does the original function use misc.prod instead
of prod?

Daniel Bump


```
def gaussian_binomial(n,k,q):
   r"""
   Return the gaussian binomial
   $$
      \binom{n}{k}_q = \frac{(1-q^n)(1-q^{n-1})\cdots (1-q^{n-k+1})}
                            {(1-q)(1-q^2)\cdots (1-q^k)}.
   $$

   EXAMPLES:
       sage: gaussian_binomial(5,1,2)
       31

   AUTHOR: David Joyner and William Stein
   """

   R.<x>=QQ[]

   n = prod([1 - x**i for i in range((n-k+1),n+1)])
   d = prod([1 - x**i for i in range(1,k+1)])

   return (n / d).subs(x = q)
```




---

Comment by mhansen created at 2008-01-23 21:28:00

Changing status from new to assigned.


---

Attachment


---

Comment by cwitty created at 2008-01-27 01:41:02

Looks good; doctests pass.


---

Comment by mabshoff created at 2008-01-27 01:55:33

Merged in Sage 2.10.1.rc1


---

Comment by mabshoff created at 2008-01-27 01:55:33

Resolution: fixed
