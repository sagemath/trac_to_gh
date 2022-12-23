# Issue 4167: wrong colors cornercase in list_plot

Issue created by migration from https://trac.sagemath.org/ticket/4167

Original creator: schilly

Original creation time: 2008-09-22 12:05:05

Assignee: was

CC:  wavetable@gmx.at

[published example of this bug](https://sage.math.washington.edu:8101/home/pub/27/)

Plotting 


```
x=srange(0, 1.1, 0.5)
w=srange(0, 1.1, 0.5)
xw = zip(x,w)
list_plot(xw, rgbcolor=(0.8, 0.8, 0), pointsize=40)
```

produces blue and brown dots.

Plotting

```
x=srange(0, 2.1, 0.5)
w=srange(0, 2.1, 0.5)
xw = zip(x,w)
list_plot(xw, rgbcolor=(0.8, 0.8, 0), pointsize=40)
```


4 yellow ones.

original report:

```
list_plot with a list of len == 3 produces 'random' point colors.
it works with len != 3.

i've created a worksheet on the milnix server, that shows the problem.
http://75.75.6.176/home/pub/17
```



---

Comment by mabshoff created at 2008-09-22 22:56:30

Resolution: duplicate


---

Comment by mabshoff created at 2008-09-22 22:56:30

This is a dupe of #2076 which has a patch and will likely be in 3.1.3.

Cheers,

Michael


---

Comment by jason created at 2008-09-23 00:48:23

FYI, with the patch at #2076, both of the above examples correctly produce yellow dots.
