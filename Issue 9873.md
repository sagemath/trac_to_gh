# Issue 9873: add a function for the derivative of ceil and floor

Issue created by migration from https://trac.sagemath.org/ticket/9874

Original creator: burcin

Original creation time: 2010-09-08 11:41:23

Assignee: burcin

CC:  ktkohl rws kcrisman pelegm

We should define a new symbolic function for the derivative of `ceil` or `floor`. 

In Maple:


```
> diff(floor(x),x);
                                  floor(1, x)
> diff(floor(x),x,x);
                                  floor(1, x)
> diff(ceil(x),x,x); 
                                  floor(1, x)
> eval(diff(ceil(x),x,x),x=1.5);
                                       0
> eval(diff(ceil(x),x,x),x=0);  
Error, (in floor) floor is not differentiable at integers
```



---

Comment by ktkohl created at 2012-01-12 14:48:25

Changing keywords from "" to "sd35.5".


---

Comment by ktkohl created at 2015-05-25 18:44:27

These give the right answer but also a runtime error:

```
sage: floor(x).derivative().subs(x=1.5)
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in 'sage.structure.parent.good_as_coerce_domain' ignored
0
sage: ceil(x).derivative().subs(x=1.5)
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in 'sage.structure.parent.good_as_coerce_domain' ignored
0
```


----
New commits:


---

Comment by rws created at 2015-05-26 06:11:29

Just a quick note that there are empty examples and tests fields but you probably know that.
