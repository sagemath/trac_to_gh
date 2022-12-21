# Issue 9261: RealIntervalField: enable option style='bracket'

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-06-18 10:01:29

Assignee: AlexGhitza

CC:  was cwitty mhansen

Currently, the option style='bracket' (to display intervals as
[1.1 ... 1.2]) is only available in the `str` method, so that
one has to provide it each time one calls str.

It would be nice to have an option style=... in the *creation* of the
field, to override the default style. For example one would have:

```
sage: R = RealIntervalField(42, style='brackets')
sage: R(pi)
[3.1415926535892 .. 3.1415926535902]
```



---

Comment by jason created at 2010-06-18 16:23:29

This is almost implemented in #7682.  The patch there is probably ready for review, but it's been a while since I looked at the patch, so it should probably have doctests run and possibly have a bit more documentation written.  And it would be nice to implement this ticket either on top of #7682, or just by adding a few lines to #7682.


---

Comment by cwitty created at 2010-07-20 21:16:49

I don't like the idea of putting the print style in the parent.  (I think the current sci_not is a design error that shouldn't be perpetuated.)

One problem is that if you have objects like `RealIntervalField(42, style='brackets')(pi)` and `RealIntervalField(42)(pi)`, then arithmetic between them is slower than between objects with the same parent.  Also, there are several parts of Sage that create their own `RealIntervalField` parents and return elements to the user, so the option you suggest would not suffice to hide question-mark printing from the user.

IMHO a global setting is a more sensible option; would that be all right, or do you really want the setting to be per-parent?

If a global setting is acceptable, then we're in luck, because it already exists: :)

```
sage: a = RIF(pi)
sage: a
3.141592653589794?
sage: sage.rings.real_mpfi.printing_style = 'brackets'
sage: a
[3.1415926535897931 .. 3.1415926535897936]
```


We could certainly document this global setting (I think it's entirely undocumented now), if that would help.


---

Comment by zimmerma created at 2010-07-21 07:43:53

> We could certainly document this global setting (I think it's entirely undocumented now), if that would help. 

I strongly support this. This global setting was something I was missing since a long time, it is
now in my init.sage file.


---

Comment by jason created at 2010-07-21 08:14:32

Replying to [comment:2 cwitty]:

> IMHO a global setting is a more sensible option; would that be all right, or do you really want the setting to be per-parent?

+1 to making such things (and keeping such things) global settings.


---

Comment by was created at 2010-07-21 10:17:16

I'm OK with this, because it only impacts the *appearance* (not the mathematics) of the elements.
