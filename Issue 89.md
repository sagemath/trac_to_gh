# Issue 89: another p-adic division bug

Issue created by migration from https://trac.sagemath.org/ticket/89

Original creator: dmharvey

Original creation time: 2006-09-27 13:34:52

Assignee: dmharvey


```
sage: (1 + O(5^2)) / (1 + O(5))
 1 + O(5^2)
```


Clearly the answer should be instead

```
 1 + O(5)
```




---

Comment by dmharvey created at 2006-09-27 13:37:52

Actually the problem is apparently with `__invert__`:

```
sage: (1 + O(5)).__invert__()
 1 + O(5^20)
```



---

Comment by dmharvey created at 2006-10-10 23:58:17

fixed in sage 1.4


---

Comment by dmharvey created at 2006-10-10 23:58:17

Resolution: fixed
