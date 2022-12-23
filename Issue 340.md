# Issue 340: error in sageinspect: ode_solver?

Issue created by migration from https://trac.sagemath.org/ticket/340

Original creator: was

Original creation time: 2007-04-01 14:43:12

Assignee: was


```


On 4/1/07, Joshua Kantor <kantor.jm@gmail.com> wrote:
> I just installed a new version of sage and 
> ode_solver?  fails with the same errors as in his message. Did something
> change 
> which would obviously cause this.

This is probably bug in the misc/sageinspect.py, which Nick Alexander recently rewrote
(so the bug is either mine or his).  In any case, a temporary work around is to type
ode_solver?? which will show the documentation (and source code). 
```



---

Comment by ncalexan created at 2007-06-27 06:01:54

In my sage, version 2.6, and in the new public notebook, this works as expected.  Please reopen and contact me (ncalexan) if this breaks in the future.


---

Comment by ncalexan created at 2007-06-27 06:01:54

Changing assignee from was to ncalexan.


---

Comment by ncalexan created at 2007-08-19 01:20:44

Resolution: worksforme
