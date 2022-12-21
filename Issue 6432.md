# Issue 6432: plot and especially animate are very slow

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-27 16:52:23

Assignee: was

CC:  mhansen

Keywords: plot speed slow animate

For anything but the smallest animations, I'm getting very slow times for `animate()` (of course, most of the time is spent writing individual png files).  Is this just the price for python?  Can we improve this to be at least usable for the several hundred frame animations I would like to create?

For example:

```
sage: anim
Animation with 22 frames
sage: %time show(anim)
CPU times: user 6.01 s, sys: 0.14 s, total: 6.15 s
Wall time: 9.68 s
```


The frames of this animation are just a few lines and points representing paths in the complex plane.


---

Comment by ncalexan created at 2009-06-27 16:52:32

Changing type from defect to enhancement.


---

Comment by mhampton created at 2009-07-17 12:34:48

This seems to overlap a lot with #1483:

[http://trac.sagemath.org/sage_trac/ticket/1483](http://trac.sagemath.org/sage_trac/ticket/1483)

The gifs that convert produces just aren't a very good solution once things are scaled up beyond small simple animations.
Using javascript instead seems like the best solution, but for very high quality exportable movies I don't see an alternative to an optional ffmpeg package.
