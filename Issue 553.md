# Issue 553: calling of symbolic expressions is sometimes ridiculous

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-01 17:22:55

Assignee: was


```

The input should be

       f = x^(1/9) + (2^(8/9) - 2^(1/9))*(x - 1) - x^(8/9)

Note that * before (x-1).  That your input was accepted is an indication
that SAGE should be more restrictive with what it allows.  What's
happening is that (2^(8/9) - 2^(1/9)) is parsed as a symbolic expression (a
constant function), and then 2^(8/9) - 2^(1/9))(x - 1) is the value of that
constant function at x-1.  Yep, that this is allowed is ridiculous, and should
be changed (I've filed a bug report). 
```



---

Attachment

I attached a patch which throws an error when trying to substitute into a constant expression.
It can be overridden by passing a substitute=True parameter to __call__. 

All doc tests pass with it.


---

Comment by mhansen created at 2007-09-06 22:49:40

Changing assignee from was to mhansen.


---

Comment by was created at 2007-09-07 04:14:20

Resolution: fixed


---

Comment by was created at 2007-09-07 07:21:31

Resolution changed from fixed to 


---

Comment by was created at 2007-09-07 07:21:31

Changing status from closed to reopened.


---

Comment by was created at 2007-09-07 07:21:31

This patch doesn't fix the problem at all.   If you apply it the above example
doesn't raise an error.  In fact, it's a patch against named substitutions, which
should *always* be allowed.  So this was totally wrong.

I'm worried actually that the expense of determining whether or not an expression
is too costly.  The only reasonable fix is to completely ban calling "non-callable"
symbolic expressions without an explicit substitution.  doing this is a lot more
work though.


---

Comment by was created at 2007-09-07 07:21:47

Changing type from defect to enhancement.


---

Comment by mhansen created at 2007-12-05 21:22:56

I think the best way to go about doing this is to add a number_of_arguments() to SymbolicExpressions:


```
sage: sin.number_of_arguments()
1
sage: (sin+1).number_of_arguments()
1
sage: (sin+x).number_of_arguments()
1
sage: (sin+x+y).number_of_arguments()
2
sage: (2^(8/9)-2^(1/9)).number_of_arguments()
0
```



---

Attachment


---

Comment by mhansen created at 2007-12-06 10:55:39

I've put up a new patch.


---

Comment by was created at 2007-12-15 11:12:33

apply this patch and the one right above it.


---

Attachment


---

Comment by mabshoff created at 2007-12-15 11:26:45

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 11:26:45

Merged in 2.9.rc0.
