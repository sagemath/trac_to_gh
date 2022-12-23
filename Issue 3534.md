# Issue 3534: plot -- fix circle example in the documentation

Issue created by migration from https://trac.sagemath.org/ticket/3534

Original creator: was

Original creation time: 2008-06-30 00:37:59

Assignee: tba


```

> The first example here:
> http://www.sagemath.org/doc/html/tut/node21.html
> .. shows creating a circle plot via:
> L = [[cos(pi*i/100),sin(pi*i/100)] for i in range(200)]
> p = polygon(L, rgbcolor=(1,1,0))
> p.save()          ## or   p.show()
>
> When I try this, I get an ellipse!  Or more precisely, the plot has
> unequal axis scaling.
>
> Here's a picture:
> http://backspaces.net/temp/Safari116.png

Use this instead:

L = [[cos(pi*i/100),sin(pi*i/100)] for i in range(200)]
p = polygon(L, rgbcolor=(1,1,0))
p.save(aspect_ratio=1)          ## or   p.show()

```



---

Comment by was created at 2008-06-30 00:43:26

The attached patch fixes the above issue.  It also greatly improves all the examples to simply
show the plots instead of having hacking notes outside the examples to show the plots, which was
done before when the doctesting framework couldn't handle plotting.


---

Attachment

It would be better to patch against the new version of the tutorial (the one in 3.0.4.alpha1): see
[http://trac.sagemath.org/sage_trac/ticket/3347](http://trac.sagemath.org/sage_trac/ticket/3347).


---

Comment by mhansen created at 2008-07-02 21:04:29

Changing keywords from "" to "editor_mhansen".


---

Comment by mhansen created at 2008-07-02 21:04:29

I'll be an editor for this since I did #3347.


---

Attachment

Here's a new patch, based on William's but done against the new version of the tutorial.  (This means that the details are different, but I've tried to preserve the ideas behind his changes.)


---

Comment by mhansen created at 2008-09-16 02:17:27

Looks good to me.  I'll make these changes in the ReST version too.


---

Comment by mabshoff created at 2008-09-16 03:53:17

Resolution: fixed


---

Comment by mabshoff created at 2008-09-16 03:53:17

Merged in Sage 3.1.2.rc5
