# Issue 7964: axis labels in weird scientific notation

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-01-17 10:31:15

Assignee: was

The vertical axis labels look weird here.  What is "1e"?


```
sage: plot(abs(exp(i*x)), (x,1,2))
```




---

Comment by mmezzarobba created at 2014-03-04 15:49:15

Confirmed with sage-6.2.beta3.


---

Comment by kcrisman created at 2022-07-27 13:29:48

[Sage 9.6](https://sagecell.sagemath.org/?z=eJwryMkv0UhMKtZIrSjQyNSq0NTUUdCo0DHUMdLUBACHAwgR&lang=sage&interacts=eJyLjgUAARUAuQ==) does not seem to have this problem, but still has a different related error with

```
plot(x^2,(x,0,5000))
```

See [this sage-devel discussion](https://groups.google.com/g/sage-devel/c/s39WysaG0fI).
