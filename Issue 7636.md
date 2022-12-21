# Issue 7636: add decorator to make functions symbolic

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-12-09 10:19:40

Assignee: burcin

CC:  kcrisman

We should make a decorator that converts a Python function to a symbolic function, similar to those created by `sage.symbolic.function_factory.function`.

Example:


```
`@`sage.symbolic.function.symbolic
def my_func(x, n):
     if x < 0: return 0
     else: return exp(-1/x^n)
```


sage-devel thread:

http://groups.google.com/group/sage-devel/browse_thread/thread/902cf2ae1a06cf6e

