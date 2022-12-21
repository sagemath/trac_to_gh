# Issue 3877: fix arrow so that they scale properly

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-08-15 21:35:54

Assignee: was

Look at the differences between


```
sage: arrow((0,0), (100, 100))
```


and


```
sage: arrow((0,0), (1/1000, 1/1000))
```


This depends on #3806.


---

Attachment


---

Comment by itolkov created at 2008-08-16 19:12:00

Scaling seems to be working. There is still a problem with arrows, but it is outside this defect.


---

Comment by itolkov created at 2008-08-16 19:16:12

Replying to [comment:2 itolkov]:
> Scaling seems to be working. There is still a problem with arrows, but it is outside this defect.

You are overriding passed width and other parameters. According to the docs,

```
sage: arrow((1, 1), (3, 3), width=0.05)
```


I didn't notice this before.


---

Comment by mabshoff created at 2008-08-16 19:17:38

We are in freeze, so only critical bugs will get fixed.

Cheers,

Michael


---

Comment by jason created at 2008-08-18 20:52:30

It looks like `width` is actually the only parameter being overridden, so doing something like checking to see if width was passed, and if it wasn't making the default the scalar*length should do it.


---

Comment by jason created at 2008-08-18 20:56:19

Actually, this patch makes it so that all arrows have different sized lines and arrow heads.  That sounds bad, especially if you are combining arrows of different lengths in the same graphic.  Or if you are putting a really small arrow in a really large graphic; it sounds like it would get lost.

I guess the real way to do things would be to have the arrow/head width a constant in screen coordinates rather than in plot coordinates.


---

Comment by jason created at 2008-08-18 22:18:30

Reading the matplotlib-0.98.3 source, there are two arrows in patches.py:

1. FancyArrow, which is drawn in plot coordinates

2. YAArrow (Yet Another Arrow), which is drawn in display coordinates.

It sounds like we want the YAArrow class, which would provide the same "look", no matter the zoom level.


---

Comment by mhansen created at 2008-08-18 22:19:10

We need to upgrade to that version of matplotlib first.


---

Comment by jason created at 2008-08-18 23:26:04

YAArrow exists in the current matplotlib that Sage uses, but has a bug that has been fixed since then in the getpoints() function.  Also, I didn't get YAArrow to look nice, no matter the scale, and have run out of time for now.


---

Comment by rlm created at 2008-08-18 23:47:27

This should be taken care of at the same time as #3880


---

Comment by rlm created at 2008-08-19 01:32:20

Take it back, this is different from #3880. I also wonder why arrows are skewed so badly: after #3880, take a look at

```
sage: arrow((-.1,-.1), (0,0))
```

The skewing isn't as bad here as I've seen it elsewhere, but I wonder why it is doing this...


---

Comment by mabshoff created at 2008-08-19 01:48:18

Fixed by #3880.

Cheers,

Mcihael


---

Comment by mabshoff created at 2008-08-19 01:49:14

Resolution: fixed


---

Comment by mabshoff created at 2008-08-19 01:49:14

Fixed by #3880. Hence: closed.

Cheers, 

Michael


---

Comment by mabshoff created at 2008-08-19 01:49:56

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-08-19 01:49:56

Oops, rlm says this is a different issue. Sorry Mike.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-19 01:49:56

Resolution changed from fixed to 


---

Comment by jason created at 2008-08-27 09:46:19

I'm working on a patch for #3922 which will make this issue obsolete.


---

Comment by mabshoff created at 2008-09-04 02:04:43

Resolution: fixed


---

Comment by mabshoff created at 2008-09-04 02:04:43

Fixed since #3922 has been merged.

Cheers,

Michael
