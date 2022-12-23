# Issue 8196: bad documentation output in tty mode

Issue created by migration from https://trac.sagemath.org/ticket/8196

Original creator: zimmerma

Original creation time: 2010-02-05 20:14:00

Assignee: mvngu


```
sage: a=mod(3,15)
sage: a.is_square?
...
            ALGORITHM: Calculate the Jacobi symbol
            `(mathtt{self}/p)` at each prime `p`
            dividing `n`. It must be 1 or 0 for each prime, and if it
            is 0 mod `p`, where `p^k || n`, then
            `ord_p(mathtt{self})` must be even or greater than
```

Clearly the math formulae are not displayed correctly in tty mode.


---

Comment by jhpalmieri created at 2010-02-05 20:47:10

> Clearly the math formulae are not displayed correctly in tty mode.

How would you expect them to be displayed, given that it's tty mode?


---

Comment by zimmerma created at 2010-02-07 21:16:47

> How would you expect them to be displayed, given that it's tty mode? 

the "mathtt{...}" should not appear, thus we should get something like:

```
            ALGORITHM: Calculate the Jacobi symbol
            `(self/p)` at each prime `p`
            dividing `n`. It must be 1 or 0 for each prime, and if it
            is 0 mod `p`, where `p^k || n`, then
            `ord_p(self)` must be even or greater than
```



---

Comment by jhpalmieri created at 2010-02-07 21:23:59

Replying to [comment:2 zimmerma]:
> the "mathtt{...}" should not appear

The patch at #8209 does this, but really only because mathtt is broken everywhere: broken in notebook documentation and in the reference manual, so might as well fix it from the command line, too.  I really don't think we want to write what would essentially be a LaTeX --> text converter, so there are limits to how good the help strings will look from the command line.

I suggest we close this, since #8209 takes care of the specific issue here.


---

Comment by zimmerma created at 2010-02-07 21:36:44

I confirm #8209 fixes that issue, thus ok to close #8196.


---

Comment by mvngu created at 2010-02-07 22:43:44

Resolution: wontfix
