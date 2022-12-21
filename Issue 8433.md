# Issue 8433: plot3d for tachyon hangs

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2010-03-04 08:08:52

Assignee: AlexGhitza

CC:  jason robertwb drkirkby mhampton jdemeyer mvngu

The following plot command fails (tachyon gets all CPU usage and no picture is shown)

```
y=var('y')
B=plot3d(sqrt(sin(x)*sin(y)),(x,-2*pi,2*pi),(y,-2*pi,2*pi),viewer='tachyon')
B.show()
```

This works fine

```
y=var('y')
B=plot3d(sqrt(sin(x)*sin(y)),(x,0,2),(y,0,2), viewer='tachyon')
B.show()
```

and this does not work

```
y=var('y')
B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')
B.show()
```

Related trac is #8424, but the problem seems to be independent.


---

Comment by robert.marik created at 2010-03-04 08:09:22

Changing assignee from AlexGhitza to was.


---

Comment by robert.marik created at 2010-03-04 08:09:22

Changing component from algebra to graphics.


---

Comment by jason created at 2010-03-04 10:52:38

This sounds like the NaNs are giving tachyon (or the triangle constructing routine) problems.  That's where I would look first for the problem, anyway.


---

Comment by ryan created at 2010-11-03 00:41:59

All three commands produce output on my sage-4.5.3 installation.


---

Comment by ryan created at 2010-11-03 00:41:59

Changing status from new to needs_info.


---

Comment by jason created at 2010-11-03 00:46:24

Yep, seems to work for me too (sage 4.6).  I think this has been fixed.

Ccing the release manager.  I don't know if he wants to close it as invalid or fixed.  Also CCing Minh, who knows the policy for closing these sorts of things.


---

Comment by mvngu created at 2010-11-03 07:01:39

Changing status from needs_info to needs_review.


---

Comment by mvngu created at 2010-11-03 07:01:39

Replying to [comment:5 jason]:
> Also CCing Minh, who knows the policy for closing these sorts of things.

It's better to add the above doctests to the documentation for `plot3d.py` just to be safe. See the attachment.


---

Comment by mvngu created at 2010-11-03 07:06:36

Changing priority from major to trivial.


---

Comment by jdemeyer created at 2010-11-03 09:31:46

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-11-03 09:31:46

I agree that these doctests pass, but the actual problem is not solved.  When doing

```
y=var('y')
B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')
B.show()
```

in the notebook, Tachyon runs forever.

Minor comment: the tests should be marked "long time".  On my Linux x86_64 machine, testing `plot3d.py` goes from 18s to 30s.


---

Comment by ryan created at 2010-11-03 12:16:24

Replying to [comment:10 jdemeyer]:
> I agree that these doctests pass, but the actual problem is not solved.  When doing
> {{{
> y=var('y')
> B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')
> B.show()
> }}}
> in the notebook, Tachyon runs forever.


I didn't run doctests.  I ran the three commands in notebook().  All three produced output (attached is the output I receive for the command above).  What version of sage are you using?


---

Attachment

notebook output to second commmand in bug report


---

Comment by ryan created at 2010-11-03 12:18:54

sorry, make the the third command

y=var('y')
B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')
B.show()


---

Attachment


---

Comment by mvngu created at 2010-11-04 04:54:25

Replying to [comment:10 jdemeyer]:
> Minor comment: the tests should be marked "long time".

Done. See the updated patch.


---

Comment by mvngu created at 2010-11-04 04:54:25

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-11-04 08:32:55

Changing priority from trivial to major.


---

Comment by jdemeyer created at 2010-11-04 08:32:55

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-11-04 08:32:55

Replying to [comment:11 ryan]:
> I didn't run doctests.  I ran the three commands in notebook().  All three produced output (attached is the output I receive for the command above).  What version of sage are you using?

This is with sage-4.6.1.alpha0 on a Gentoo Linux x86_64 system.

For me, only the second plot in the bug report works.


---

Comment by jdemeyer created at 2010-11-04 08:33:45

Everything does work on alpha.sagenb.org (sage-4.6.rc0, Ubuntu Linux x86_64).


---

Comment by cremona created at 2010-11-04 09:11:15

All three work for me (4.6 on ubuntu 64-bit + firefox)


---

Comment by jason created at 2010-11-04 12:59:44

Possibly for another ticket, but notice this:


```
sage: var('y')
sage: B=plot3d(sqrt(sin(x)*sin(y)),(x,-2*pi,2*pi),(y,-2*pi,2*pi),viewer='tachyon',adaptive=True)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/grout/<ipython console> in <module>()

/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in plot3d(f, urange, vrange, adaptive, transformation, **kwds)
    684             raise ValueError, 'unknown transformation type'
    685     elif adaptive:
--> 686         P = plot3d_adaptive(f, urange, vrange, **kwds)
    687     else:
    688         u=fast_float_arg(0)

/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in plot3d_adaptive(f, x_range, y_range, color, grad_f, max_bend, max_depth, initial_depth, num_colors, **kwds)
    775             else:
    776                 span = (len(texture)-1) / (max_z - min_z)    # max to avoid dividing by 0
--> 777             parts = P.partition(lambda x,y,z: int((z-min_z)*span))
    778         all = []
    779         for k, G in parts.iteritems():

/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/index_face_set.so in sage.plot.plot3d.index_face_set.IndexFaceSet.partition (sage/plot/plot3d/index_face_set.c:6081)()

/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in <lambda>(x, y, z)
    775             else:
    776                 span = (len(texture)-1) / (max_z - min_z)    # max to avoid dividing by 0
--> 777             parts = P.partition(lambda x,y,z: int((z-min_z)*span))
    778         all = []
    779         for k, G in parts.iteritems():

ValueError: cannot convert float NaN to integer
```



---

Comment by kcrisman created at 2010-11-04 14:08:58

#7423 would be at least related to the NaN issue.


---

Comment by jason created at 2010-11-04 14:23:09

Replying to [comment:18 kcrisman]:
> #7423 would be at least related to the NaN issue.

That ticket now works for me, so maybe people should test it to see if it should be closed too?


---

Comment by drkirkby created at 2010-11-06 00:00:35

Why are the tests marked "long time"? They take about 1.5 seconds on my machine. 

Dave


---

Comment by jdemeyer created at 2010-11-06 00:15:58

Replying to [comment:20 drkirkby]:
> Why are the tests marked "long time"? They take about 1.5 seconds on my machine. 

I seem to remember a policy that 1 second is the bound for "long time".


---

Comment by chapoton created at 2014-07-25 14:29:11

Changing keywords from "" to "tachyon".


---

Comment by mkoeppe created at 2021-07-22 01:07:59

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2021-07-22 01:07:59

outdated, works for me


---

Comment by kcrisman created at 2021-07-22 01:57:34

> outdated, works for me

Already outdated years ago.  Should we still add a doctest?

By the way, Jason's comment in comment:17 is still true, so it is now #32261.


---

Comment by mkoeppe created at 2021-07-22 05:48:12

Replying to [comment:28 kcrisman]:
> Should we still add a doctest?
I don't think this would be useful

> By the way, Jason's comment in comment:17 is still true, so it is now #32261.
Thanks! This bug appears to be unrelated to the `fast_float` cleanup that we are doing, but someone who knows about the plotting code may want to take a look


---

Comment by kcrisman created at 2021-07-22 12:21:13

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-08-26 02:08:43

Resolution: invalid
