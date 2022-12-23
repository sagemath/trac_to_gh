# Issue 1778: plot() does not follow the same interval range conventions as plot3d()

Issue created by migration from https://trac.sagemath.org/ticket/1778

Original creator: moretti

Original creation time: 2008-01-14 22:58:12

Assignee: moretti

Keywords: plotting, plot3d, plot

sage: plot3d(x^2 + y^2, (x,-2,2), (y,-2,2))

is valid, however, to do a 2d plot, you use the syntax

sage: plot(x^2, x, -2, 2).

I spoke with William about this, he wants to deprecate the plot(x^2, -2, 2) syntax for 2d plotting and introduce a new preferred syntax:

sage: plot(x^2, (x, -2, 2))


---

Attachment

Ignore the previous patch, it does not have all the required changes.


---

Attachment


---

Comment by moretti created at 2008-01-15 00:34:49

I implemented this in the attached. It makes both the old and new style of plot() syntax valid. However the documentation mentions that plot(x^2, (x, a, b)) is the preferred syntax. Please test it out.


---

Comment by was created at 2008-01-15 05:52:20

That this doesn't work anymore is definitely a bug:

```
sage: plot(sin(2), (x,0,10*pi))
BOOM!
```


Likewise for 

```
sage: plot(sin(2), 0,10*pi)
BOOM
```


I'll try to fix this....


---

Comment by was created at 2008-01-15 05:52:20

Changing priority from minor to major.


---

Comment by was created at 2008-01-15 05:55:38

It turns out the `plot(sin(2), (x,0,10*pi))` problem above was a really genuine bug coming from an indentation mistake on line 624 (I will attach a patch fixing this and other issues).


---

Attachment

apply the hg bundle that bobby posted, then apply this plain text patch which fixes one serious bug.


---

Comment by was created at 2008-01-15 06:21:14

Apply the plot.hg followed by trac-1778-referee.patch


---

Comment by mabshoff created at 2008-01-15 07:12:27

I had to resolve some slight merge conflict with #1779 in `setup.py`.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-15 07:12:50

Resolution: fixed


---

Comment by mabshoff created at 2008-01-15 07:12:50

Merged in Sage 2.10.alpha3
