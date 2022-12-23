# Issue 7431: @interact and %hide don't play nice together

Issue created by migration from https://trac.sagemath.org/ticket/7431

Original creator: kcrisman

Original creation time: 2009-11-11 19:47:36

Assignee: itolkov

CC:  jason


```
%hide 
@interact 
def _(n=2): 
    f(x,y)=x^n 
    show(plot(f,(x,0,1))) 
```

doesn't work well, especially if you update the interact. 


---

Comment by kcrisman created at 2010-01-04 20:22:32

Update on this:  Interact does work with hide, but for some reason only after you save, quit, and restart.  Why???


---

Comment by kcrisman created at 2010-04-22 01:52:52

Another update:  Lately, it's been working, but only if I remove the focus from that cell, then use the interact.  Anyway, it's confusing.  Perhaps someone else will have input.  Changing priority since no one else has touched this, though.


---

Comment by kcrisman created at 2010-04-22 01:52:52

Changing priority from major to minor.
