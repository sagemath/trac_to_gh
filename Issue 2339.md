# Issue 2339: xmin/xmax now broken in plot()

Issue created by migration from https://trac.sagemath.org/ticket/2339

Original creator: bober

Original creation time: 2008-02-28 02:36:46

Assignee: was

CC:  bober mhampton kcrisman


```
r(t) = 1000 * t * e^(-.5 * t)
plot(r, xmin=0, xmax=20).show()
```


doesn't work. But

```
plot(r, (0,20)).show()
```

does. The documentation still says

```
    PLOT OPTIONS:
    The plot options are
    [...]
        xmin -- starting x value
        xmax -- ending x value
    [...]
```



---

Comment by mabshoff created at 2008-04-05 00:17:19

This is still broken in Sage 3.0.alpha1.

Cheers,

Michael


---

Comment by mhampton created at 2008-05-17 18:49:06

Changing assignee from was to mhampton.


---

Comment by mhampton created at 2008-05-17 20:33:06

Changing keywords from "" to "plot, xmin, xmax".


---

Comment by mhampton created at 2008-05-17 20:33:06

Changing assignee from mhampton to somebody.


---

Comment by mhampton created at 2008-05-17 20:33:06

In addition to fixing this problem, I also enforced the xmin, xmax that are given if they are inside [-1,1].


---

Comment by mhampton created at 2008-05-17 20:33:36

should fix the problem


---

Attachment

Looks okay to me, although I don't understand the purpose of the change from


```
G = Graphics() 
for i in range(0, len(funcs)): 
```


to


```
G = plot(funcs[0], (xmin, xmax), polar=polar, **kwds) 
for i in range(1, len(funcs)): 
```



---

Comment by mhampton created at 2008-06-12 11:59:40

The purpose of that change was: I was trying to avoid the xmin of the output being set to -1 if the argument xmin was greater than that.  If you initialize something as Graphics(), xmin is set to -1. 

There is probably a better systematic way of solving that problem but I don't have it in hand.


---

Comment by jhpalmieri created at 2008-06-12 15:03:23

Hm. If I do:

```
sage: r(t) = 1000 * t * e^(-0.5*t)
sage: plot(r, xmin=10, xmax=20).show()
```

or (to make sure I didn't misunderstand "greater than" -1):

```
sage: r(t) = 1000 * t * e^(-0.5*t)
sage: plot(r, xmin=-2, xmax=20).show()
```

then I seem to get the same behavior with or without this particular change in the code.

I have two more questions: what should the following do?

```
plot (r, xmin=10, xmax=-2).show()
```

It should probably print an error (since xmin > xmax), but right now I get a graph which is a bad approximation to 

```
plot (r, xmin=-2, xmax=10).show()
```

It's actually pretty strange looking...

Also, do you have any idea why, if I do

```
plot (r, xmin=5, xmax=20).show()
```

then the vertical axis is the line x=5, not x=0?  When xmin is positive, I seem to get x=xmin as the vertical axis, which looks strange to me.  I guess the same happens if both xmin and xmax are negative: then x=xmax is drawn as the vertical axis.  (This is probably a completely separate issue, but I thought I'd ask.)


---

Comment by craigcitro created at 2008-06-20 04:43:35

Changing keywords from "plot, xmin, xmax" to "plot, xmin, xmax, editor_gfurnish".


---

Comment by gfurnish created at 2008-06-20 06:26:08

This seems correct except for an error check, can we get a patch?


---

Comment by jhpalmieri created at 2008-07-08 19:12:34

Here's a new version of the patch.  This (I hope) takes the arguments called xmin and xmax, and sets xmin to be the smaller of the two, xmax to be the larger.  This should fix the strange plots that commands like

```
plot (r, xmin=10, xmax=-2).show()
```

were giving, as I mentioned above.


---

Comment by jhpalmieri created at 2008-07-08 19:13:33

new version of 2399 patch, fixing problem when xmin > xmax


---

Attachment

By the way, my patch supersedes Marshall's, but he should get credit for most of the work.  (Is it better to have one patch, for easier installation, or two, to make sure the right people get credit for their work?)

One question: in my patch, as I described, if you call plot with arguments xmin=10 and xmax=0, then the plot gets drawn between x=0 and x=10, with no error message.  Is this the best behavior, or should an exception be raised instead?


---

Comment by mhampton created at 2008-07-08 23:07:42

I thought about that issue a bit (xmin > xmax), and I think the lack of an error message is OK. Thanks for working on this more, I am really swamped with other stuff at the moment.


---

Comment by jhpalmieri created at 2008-07-16 01:18:21

Can I give a positive review to mhampton's contribution, and vice versa?


---

Comment by mabshoff created at 2008-07-16 01:21:00

Replying to [comment:13 jhpalmieri]:
> Can I give a positive review to mhampton's contribution, and vice versa?
> 

Yes, that is perfectly fine.

Cheers,

Michael


---

Comment by mhampton created at 2008-08-24 15:53:49

My apologies, I should have positively reviewed this before.  Now I think the patch has to be rebased.  I will try to do that.


---

Comment by kcrisman created at 2008-10-21 18:19:35

File 2339-3.2.alpha0.patch is rebased patch against 3.2.alpha0.   As JHP says, please give credit to Marshall.

Interestingly, all the plot improvements as of late have already fixed both the Graphics initialization problem of [-1,1] and the problem if you get the range in backwards, i.e. all of the following work with this patch:

```
plot(r, xmin=10, xmax=-2).show()
plot(r, 10,-2).show()
plot(r, (10,-2)).show()
```



---

Comment by kcrisman created at 2008-10-21 18:20:17

Rebased to 3.2.alpha0


---

Attachment

This is a simple change that seems to solve the problem, positive review.


---

Comment by mhampton created at 2008-10-22 19:27:26

By the way, thanks Karl, this had fallen off my radar.


---

Comment by kcrisman created at 2008-10-23 00:10:37

No problem; during the school year I don't have much time for new stuff, but I figure I can help out in this way at least!


---

Comment by mabshoff created at 2008-10-26 03:18:18

Merged 2339-3.2.alpha0.patch only in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-26 03:18:18

Resolution: fixed
