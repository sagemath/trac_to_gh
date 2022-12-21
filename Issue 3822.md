# Issue 3822: Interact - slider breaks defaulting on too many values

Issue created by migration from Trac.

Original creator: itolkov

Original creation time: 2008-08-12 20:20:22

Assignee: itolkov

> Unfortunately, as soon as the range of values gets at all large --
> e.g., a few thousand, -- this causes *major* problems,
> which lead to the browser spitting out errors, etc.  Basically you
> exceed hard limits.

The problem is that something like

```
slider(1, 10^6)
```

generates 10<sup>6</sup> values, which get sent back to the user. Now, there is no reason to use 10<sup>6</sup> values when the maximum number of accessible values (via manipulating the slider) is 500.



---

Attachment

1. Changed default step size from 1 to such that there are 500 steps
 2. `(a, b)` is now equivalent to `slider(a, b)`


---

Comment by was created at 2008-08-12 21:52:53

It is still broken since you didn't deal with the case when the input is a list of values.  

E.g.,

```
`@`interact
def _(n=range_slider([1..10000])):
    print n
```


breaks it.


---

Comment by mabshoff created at 2008-08-13 06:46:09

Changing component from notebook to interact.


---

Attachment

Apply after sage.patch


---

Comment by itolkov created at 2008-08-14 19:14:05

3. `slider(a, b, c)` is equivalent to `slider([a,a+c..b])`
 4. Improved performance for input like `slider(a, b, c)`


---

Comment by was created at 2008-08-15 10:01:01

Good job.  Note that this still breaks things.  But still this patch needs to go in.


```
`@`interact
def _(n=[1..10^5]):
    print n
```



---

Attachment


---

Comment by was created at 2008-08-15 10:02:49

I fixed some failed doctests.


---

Comment by mabshoff created at 2008-08-15 10:32:50

Merged all three patches in Sage 3.1.rc0. William's patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-15 10:32:50

Resolution: fixed
