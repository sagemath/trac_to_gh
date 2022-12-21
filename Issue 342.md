# Issue 342: ComplexNumber constructor seg faults

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-04-01 14:47:38

Assignee: somebody


```
Found by: Pablo De Napoli
> Another problem that i've found is that calling ComplexNumber (for example
> by)
> 
> ComplexNumber(2,3)
> 
> causes a segmentation fault.
> (using sage-2.4.1.2)
 
That's definitely a bug.   It's now trac #342.
```



---

Comment by mhansen created at 2007-08-18 19:58:34

Resolution: fixed
