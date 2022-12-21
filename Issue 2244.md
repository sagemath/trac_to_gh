# Issue 2244: [with patch; needs review] add a randomize=False option to the plot command, to avoid "wiggle" in animations

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-21 06:41:53

Assignee: was




---

Comment by was created at 2008-02-21 06:46:52

The attached patch *also* fixes a bug where the right hand endpoint in the plot
range wasn't included.  This is very clear when doing plots with very few points.


---

Comment by was created at 2008-02-21 06:54:24

Apply this after #2236.

Ignore the comment above about also fixing endpoints -- #2236 also did so.


---

Attachment

apply after William's patch


---

Comment by jason created at 2008-02-21 21:22:51

Williams patch looks good to me, but I slightly changed the wording of his examples to specify that the *initial* sample points were the things guaranteed to be consistent.

I also added a small type-cast to the adaptive code to be consistent with the code above for regular sample points.


---

Comment by mabshoff created at 2008-02-24 03:00:27

Both patches fail to apply cleanly against 2.10.2. Please rebase.

Cheers,

Michael


---

Comment by was created at 2008-02-24 04:57:04

this should apply cleanly (it replaces the patch that was here before)


---

Attachment

Apply sage-2244-nowiggle.patch (which has now been rebased) followed by wiggle-interior.patch which will apply correctly with some "fuzz". 

 -- William


---

Comment by mabshoff created at 2008-02-25 02:11:23

Replying to [comment:6 was]:
> Apply sage-2244-nowiggle.patch (which has now been rebased) followed by wiggle-interior.patch which will apply correctly with some "fuzz". 
> 
>  -- William

No, it doesn't, at least for me:

```
sage$ patch -p1 --dry-run < trac_2244-nowiggle.patch 
patching file sage/plot/plot.py
Hunk #1 FAILED at 3284.
Hunk #2 succeeded at 3421 with fuzz 2 (offset -11 lines).
Hunk #3 succeeded at 3445 (offset -12 lines).
1 out of 3 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
```

I checked for hunk one in plot.py and it just isn't there. Maybe this patch depends on another patch to be applied first? 

Cheers,

Michael


---

Comment by mhansen created at 2008-03-05 00:37:43

This gives the following reject:


```

--- plot.py
+++ plot.py
`@``@` -3284,8 +3284,9 `@``@` class PlotFactory(GraphicPrimitiveFactor
         200
         sage: P          # render
 
-    We plot with randomize=False, so that the same points are
-    evenly spaced (and always the same):
+    We plot with randomize=False, which makes the initial sample
+    points evenly spaced (hence always the same).  Adaptive plotting
+    might insert other points, however.
         sage: p = plot(sin,-1,1,plot_points=3,plot_division=0,randomize=False)
         sage: p[0][1][0]
         -0.66666666666666...

```


and the corresponding bit in plot.py in 2.10.3.rc1 is


```

        sage: len(P[0])  # random output
        80
        sage: P          # render

    Some colored functions:

        sage: plot(sin, 0, 10, rgbcolor='#ff00ff')
        sage: plot(sin, 0, 10, rgbcolor='purple')
    
    We plot several functions together by passing a list
    of functions as input:
        sage: plot([sin(n*x) for n in [1..4]], (0, pi))

```



---

Attachment

apply instead of the two above


---

Comment by AlexGhitza created at 2008-03-15 18:11:35

I'm attaching a new patch replacing the other two, made against sage-2.10.3.  doctests in sage/plot/ work fine on it.


---

Comment by mabshoff created at 2008-03-15 23:40:02

Merged 2244_nowiggle_new.patch in Sage 2.10.4.rc0


---

Comment by mabshoff created at 2008-03-15 23:40:02

Resolution: fixed
