# Issue 5055: Trivial but fatal typo in interact documentation

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-01-22 15:58:43

Assignee: itolkov

About halfway through the documentation of interact, there is this example:

```
sage: `@`interact
... def _(title=["A Plot Demo", "Something silly", "something tricky" , a=input_box(sin(x*sin(x*sin(x))), 'function'),
...     clr = Color('red'), thickness=[1..30], zoom=(1,0.95,..,0.1), plot_points=(200..2000)):
...     html('<h1 align=center>%s</h1>'%title)
...     print plot_points
...     show(plot(a, -zoom*pi,zoom*pi, color=clr, thickness=thickness, plot_points=plot_points))
<html>...
```

There should be a ] after the " after the word tricky.


---

Comment by mhansen created at 2009-01-23 09:05:42

Changing assignee from itolkov to mhansen.


---

Comment by mhansen created at 2009-01-23 09:05:42

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-23 09:05:42

Where are you seeing this error?  I can't find it in any of the official Sage files.  I'd vote for marking this as invalid.


---

Comment by kcrisman created at 2009-01-23 18:30:52

Replying to [comment:1 mhansen]:
> Where are you seeing this error?  I can't find it in any of the official Sage files.  I'd vote for marking this as invalid.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: interact?
```

| Sage Version 3.3.alpha0, Release Date: 2009-01-19                  |
| Type notebook() for the GUI, and license() for information.        |
And then it comes.  Also, just above that, there is something about an interact "campus", which sounds odd to me... Anyway, this is pretty valid.  Though trivial.  

According to search_src('tricky'), it is in server/notebook/interact.py


---

Comment by kcrisman created at 2009-01-23 20:01:57

Or, rather, it seems to be valid in a disturbing way...

> According to search_src('tricky'), it is in server/notebook/interact.py

Weirdly, when I actually look at that file, I see both [].  So now the question is why doesn't this appear when I type

```
interact?
```

Instead, there is a space showing where the ] is in the actual file.  But that is probably not for a typo ticket, so if it's reproducible it should be a separate ticket.

Attached is a patch fixing the word "campus" to "canvas", though, which *is* a trivial typo in the interact documentation.


---

Comment by kcrisman created at 2009-01-23 20:02:22

Based on 3.3.alpha0


---

Attachment


---

Comment by mabshoff created at 2009-01-28 14:12:58

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 14:12:58

Resolution: fixed
