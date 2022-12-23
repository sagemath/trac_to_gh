# Issue 4248: aspect_ratio is buggy in plot3d

Issue created by migration from https://trac.sagemath.org/ticket/4248

Original creator: jhpalmieri

Original creation time: 2008-10-06 23:01:06

Assignee: somebody

Keywords: aspect_ratio, plot3d

`aspect_ratio` doesn't obey its documentation.  If I type

```
sage: var('x y')
sage: Q = plot3d(sin(x+y), (-3,3), (-2,2))
sage: Q.show(aspect_ratio=[1,1,1])
```

then I get what I expect: the x-, y-, and z-axes are given the same scale, so ratio of the length of the x-axis to the length of the y-axis is 3:2.  But if I do

```
sage: Q.show(aspect_ratio=[1,1,2])
```

then suddenly the y-axis goes from -4 to 4, and the ratio of the lengths of the x- and y-axes is 3:4 (so the aspect_ratio in the two dimensions x and y is [2,1] instead of [1,1]).

Here is a web page with pictures showing the problem:
[http://www.math.washington.edu/~palmieri/Sage/ar.html](http://www.math.washington.edu/~palmieri/Sage/ar.html)



---

Attachment


---

Comment by jhpalmieri created at 2008-10-20 20:49:46

I'm attaching a patch.  Some comments:

1. the only significant change is the removal of the line

```
if i != longest_side: 
```

and the ensuing change in indentation.

2. the variable `new_box`, defined at the beginning of the old code, wasn't used anywhere, so I deleted it.

3. my other changes are basically cosmetic.


---

Comment by mhampton created at 2008-10-22 19:58:55

Positive review.  I was surprised by the bad coverage in plot/plot3d/base.pyx, its only 5%, but fixing that is way beyond the scope of this patch.  This seems to fix the noted problem and passes what few tests there are in base.pyx.


---

Comment by mabshoff created at 2008-10-25 21:22:30

Resolution: fixed


---

Comment by mabshoff created at 2008-10-25 21:22:30

Merged in Sage 3.2.alpha1
