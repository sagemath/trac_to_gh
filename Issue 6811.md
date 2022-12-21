# Issue 6811: prime_pi.plot is wrong (!)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-08-23 04:11:08

Assignee: was

I was computed Riemann's analytic formula for pi(X), and was disturbed it wasn't converging to pi(X).  It turned out that the function in Sage for a while for plotting prime_pi is buggy! For example, try this:

```
sage: prime_pi.plot(5,10).show(gridlines='minor',frame=True)
sage: prime_pi(8)
4
```

You'll see a plot that has a horizontal line at height 5 on it.  

This is very bad and embarrassing!



---

Comment by was created at 2009-08-23 05:13:43

I've attached code to fix this bug.  It does things right.  

  (1) I created a plot_step_function command that can be used to plot general step functions, and added it to the reference manual. 

  (2) I changed the current broken prime_pi.plot to use that and use a much easier to understand (hence right) algorithm to generate the plot.

  (3) I fixed a bunch of ReST mistakes in prime_pi.pyx while I was at it.  

  (4) I added prime_pi to the reference manual.


---

Attachment


---

Comment by ohanar created at 2009-08-23 09:45:12

Looks fine:
 1. Importing sage.plot.all is no longer necessary in prime_pi.pyx
 1. May want to change

```
for i in range(len(v)):
    w.append(v[i])
    if i+1 < len(v):
        w.append((v[i+1][0],v[i][1]))
```

to

```
for i in range(len(v)-1):
    w.append(v[i])
    w.append((v[i+1][0],v[i][1]))
w.append(v[len(v)-1])
```

for readability.
 1. The plot_step_function always starts horizontal and ends vertically, this can sometimes lead to rather odd looking results in my opinion. For example, compare

```
sage: plot_step_function([(i,i^3) for i in range(6)])
sage: plot_step_function([(i,i^3) for i in range(6)]) + line([(5,125),(6,125)])
```

    a. If we are to make any changes to this, we would need to consider uneven intervals of definition (say the function `[(i<sup>2,i</sup>3) for i in range(6)]`).
 1. Might be useful to use the plot_step_function elsewhere. For example, with Riemann sums it is either difficult or impossible to enable vertical lines, and the floor function is in the opposite situation.


---

Comment by ohanar created at 2009-08-23 09:57:23

Also, we need to fix the credit situation in prime_pi.pyx


---

Comment by mvngu created at 2009-08-24 06:03:47

reviewer patch; fixes typos


---

Attachment

The reviewer patch `trac_6811-reviewer.patch` fixes some typos in `trac_6811.patch`. One of these typos results in a warning when building the reference manual.


---

Comment by mvngu created at 2009-08-24 06:43:15

Merged both patches.


---

Comment by mvngu created at 2009-08-24 06:43:15

Resolution: fixed
