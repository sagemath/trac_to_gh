# Issue 933: Permanents of (0,1)-matrices

Issue created by migration from https://trac.sagemath.org/ticket/933

Original creator: jsp

Original creation time: 2007-10-19 19:00:37

Assignee: was

Let A = (a_{ij}) be an m x n (m <= n) (0,1)-matrix. We define a
matrix X = (x_{ij}) with independent indeterminates x_{ij}:
x_{ij} = 0 iff a_{ij} = 0.

So x_{ij} only exists iff a_{ij} = 1.


Now define a list of equations: (how do I format them properly here?)

\sum_{i=1}^{i=m} x_{ij} = 1 for j = 1, ..., n

\sum_{j=1}^{j=n} x_{ij} = 1 for i = 1, ..., m

x_{ij}^2 = x_{ij} for i = 1, ..., m and j = 1, ..., n


It is easy to prove that the number of solutions to this equations is
equal to the permanent of A.

Based on a paper from Bernasconi, et al.: Computing Groebner Bases
in the Boolean Setting with Applications to Counting (1997) (which
restricts itself to square matrices and a number of polynomials less than 255),
we can do the following:

1) calculate a Groebner basis

2) compute the number of solutions (the permanent)

If this could be done fast, it beats Ryser's algorithm (See the
article above).

Jaap


---

Comment by malb created at 2008-09-17 14:06:02

> calculate a Groebner basis 

over which field?


---

Comment by vdelecroix created at 2015-08-17 12:19:11

Replying to [comment:3 malb]:
> > calculate a Groebner basis 
> 
> over which field?

`ZZ`. You want the `0-1` solutions and the `x = x^2` guarantees exactly that.
