# Issue 7942: latex(I) should be the string "i" not "I"

Issue created by migration from https://trac.sagemath.org/ticket/7942

Original creator: was

Original creation time: 2010-01-16 03:27:15

Assignee: burcin


```

That is dumb and should be fixed!

sage: latex(I)
I
sage: latex(i)
I

It should output "i" not "I".
```



---

Comment by burcin created at 2010-01-16 09:12:10

This is a duplicate of #6405. Number field elements don't support a separate latex name option, so we have 3 options:
 * Use `i` for both modes
 * Use `I` for both modes
 * implement a latex_name option for number field elements.


---

Comment by burcin created at 2010-01-16 09:12:10

Resolution: duplicate
