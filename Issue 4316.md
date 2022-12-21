# Issue 4316: notebook: '%html $x<y$' doesn't work right

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-10-17 23:20:57

Assignee: boothby

Keywords: notebook, %html

If I type

```
%html some math: $x<y$.
```

in the notebook, then the "<y" gets swallowed. (If I "Edit" the worksheet, I see

```
<html><font color='black'>some math: <span class="math">x<y</span>.</font></html>
```

but in the worksheet view I see "some math: x.")

Putting a space between "<" and "y" fixes the problem. Also,

```
%html some math: $x<6y$.
}}} 
works just fine, and the same with $x<-y$ and similar things; the problem seems to just be with "<" followed by a letter.  The greater than sign seems to present no problems.

Is this related to (or the same problem as) #4245?


---

Comment by mhansen created at 2009-01-24 07:35:32

Resolution: duplicate


---

Comment by mhansen created at 2009-01-24 07:35:32

This is a duplicate of #4245.
