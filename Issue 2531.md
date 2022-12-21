# Issue 2531: pretty-print issue in fractions

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2008-03-15 12:42:31

Assignee: was

CC:  burcin

Some symbolic fractions are not printed correctly:

```
sage: print z

                                  arcsin(x)
                                    -------
                                       2
```

One would expect the '-' bar to start under 'a' on the left.

This was found from an example in calculus.py:

```
sage: x = var('x')
sage: y = x^2
sage: dy = derivative(y,x)
sage: z = integral(sqrt(1 + dy^2), x, 0, 2)
sage: print z
                     arcsinh(4) + 4 sqrt(17)
                     ---------------------
                               4
```

Note that the actual output I get with 2.10.3 slightly differs:

```
sage: print z

                           arcsinh(4) + 4 sqrt(17)
                             ---------------------
                                       4

```

I wonder why sage -t calculus.py does not point that output difference.


---

Comment by mhansen created at 2008-03-15 15:12:35

The issue comes from Maxima using asinh instead of arcsinh.  Thus,  we're simply doing a substitution in the string that Maxima returns.  The testing framework doesn't catch it because it is set to ignore certain whitespace issues.


I think a good, and probably not too difficult task would be to have our own native pretty printer.  I believe there is already one in Sympy that we could make use of.


---

Comment by zimmerma created at 2008-03-15 22:34:55

Would it be possible to do the substitution asinh -> arcsinh within Maxima, and then calling
Maxima's pretty printer?


---

Comment by mhansen created at 2008-03-15 22:36:33

I have no idea how that'd be done.


---

Comment by mhansen created at 2009-10-05 07:23:38

Since we don't use Maxima's pretty-printing anymore, I'm going to close this as invalid.


---

Comment by mhansen created at 2009-10-05 07:23:38

Resolution: invalid
