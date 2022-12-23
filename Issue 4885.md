# Issue 4885: fix fallout from sloppy review of 4535

Issue created by migration from https://trac.sagemath.org/ticket/4885

Original creator: was

Original creation time: 2008-12-28 23:25:41

Assignee: was

I refereed trac #4535 and I made some serious mistakes in accepting that patch.  This ticket will be about fixing all of those mistakes.

 * the function xmin/xmax/ymin/ymax were all removed.  They *must* be all added back exactly as before.  There is a lot of code out there that depends on it.  Also, we do not just delete functions in sage without deprecating them for at least 6 months first.

 * some of the new functions get_* have no documentation or docstrings.  Fix this. 

 * Do "sage -t" on the *old* plot.py using the newest version of sage, and make sure nothing breaks (e.g., examples that use .xmin, etc.)  Fix anything that does, or at least *discuss* it.


Unless somebody beats me to it, I'll do this, since it is my fault #4535 got a positive review.  I'll post to this ticket, as soon as I work on this, so if I haven't posted a message below that I'm working on it, I haven't started. 

  -- William 



---

Comment by jason created at 2008-12-29 11:15:07

Is that an official deprecation policy now?  (I think it's a great idea.)  Is that deprecation policy documented somewhere?  If not, it should be.


---

Comment by was created at 2008-12-30 01:21:33

> Is that an official deprecation policy now? (I think it's a great idea.)

Yes. 

> Is that deprecation policy documented somewhere? If not, it should be. 

I think it was only documented in sage-devel.  It would be good add more documentation if I'm wrong.


---

Comment by mabshoff created at 2008-12-30 01:24:21

The deprecation policy isn't documented and we could definitely need a good example and something official in the development manual.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-30 11:23:55

I thought this was high priority to get in? I have been waiting to see something happening here, otherwise this will get bumped.

Cheers,

Michael


---

Comment by was created at 2008-12-30 23:27:25

> I thought this was high priority to get in? I have been waiting to see something 
> happening here, otherwise this will get bumped. 

Thanks for the reminder.  This is high priority.


---

Comment by was created at 2008-12-31 00:13:49

I'm doctesting the old plot.py and finding what was broke by the refactoring. 

1. Lots of xmin/xmax, etc.  That's known.

2. The API of text changed:

```
    sage: text("Sage is really neat!!",(2,12,1))
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/build/sage-3.2.3.alpha0/local/lib/python2.5/site-packages/sage/plot/text.py", line 79, in text
        def text(string, (x,y), **options):
    ValueError: too many values to unpack
```


Instead of ValueError, it might be better to be

```
ValueError: too many values to unpack (try using text3d)
```

at least when 3 coordinates are given.  This will help with people transition code that uses the old text command. 

This example used to work fine before the refactoring, but #4535 broke it:

```
E = EllipticCurve('37a')
P = E(0,0)
def get_points(n): return sum([point(i*P, pointsize=3) for i in range(-n,n) if i != 0 and (i*P)[0] < 3])
sum([get_points(15*n).plot3d(z=n) for n in range(1,10)])
```


it fails with this error:


```
        self.loc = (float(center[0]), float(center[1]), float(center[2]))
      File "rational.pyx", line 1112, in sage.rings.rational.Rational.__getitem__ (sage/rings/rational.c:8532)
    IndexError: index n (=1) out of range; it must be 0
```


Everything else is harmless as far as I can tell.


---

Attachment

this patch fixes all the problems reported in the tickets and commentary up to this point.


---

Comment by mhansen created at 2009-01-02 05:31:48

I posted a new patch which makes it so that get_minmax_data is *not* cached.  Having it cached will break things if new primitives are added to the graphics object.  The idea is that get_minmax_data comes directly from the primitives, and any custom stuff the user wants is stored in axes_range.


---

Comment by was created at 2009-01-02 07:15:03

The idea is good.  I don't like that you replaced:

```
>  WARNING: The returned dictionary is mutable, but changing it does 
>  not change the xmin/xmax/ymin/ymax data.  To change that, call 
>   the methods xmin, xmax, ymin, and ymax.  
```

by 

```
> Note that this is recomputed every time the function is called. 
```


The first is very clear and explicit, but of course not right anymore.  The second implicitly suggests what the first said.  The WARNING would be a good place to make it clear that it doesn't make sense to change the minmax data, since it's a function of the actual points in the objects.  And there one could point to the other relevant functions for setting the axes ranges.


---

Attachment

Assuming mhansen gave my patch a positive review modulo me giving his a positive review, this gets a positive review. I nitpick about the docs, but that's not enough to stop this going in.


---

Comment by mabshoff created at 2009-01-02 22:15:09

Merged both patches in Sage 3.2.3.final


---

Comment by mabshoff created at 2009-01-02 22:15:09

Resolution: fixed
