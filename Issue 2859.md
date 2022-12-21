# Issue 2859: plotting the vector (0,0,-1) really plots (0,0,1)

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-08 21:10:09

Assignee: was

Try the following:


```
plot(vector((0,0,-1)))
```


The resulting vector points up, but should point down.


---

Comment by jason created at 2008-04-08 21:38:09

The problem is in arrow3d:


```
sage: arrow3d((0,0,0), (0,0,-1))
*points up*
```



---

Comment by jason created at 2008-04-08 22:16:54

All right, this was because we were taking the cross product with (0,0,1) and using that to decide whether or not to rotate the vector, ignoring the case that we point in the opposite direction (but still have a cross product of zero).

Patch will be attached.  I'm marking this a blocker since it gives a *wrong* result and William said that wrong results should be marked as blockers.


---

Comment by jason created at 2008-04-08 22:17:01

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-04-09 01:22:37

Jason,

how does this ticket related to #1777? [also opened by you]

Cheers,

Michael


---

Comment by jason created at 2008-04-09 01:33:33

It doesn't relate.  

In this ticket, the arrow is actually wrong (the assumption in the code is that "parallel to (0,0,1)" == "pointing in the same direction as (0,0,1)", which is just wrong.

The issue in #1777 is a cosmetic issue related to the menus in JMOL.


---

Comment by ddrake created at 2008-04-09 07:19:48

The patch works as advertised and the code looks good to me. Positive review for the code, and I'll give it full positive review once you sort out this minor complaint about the doctest: instead of "A downward pointing arrow should have a transformation scaling the points to their negatives" do you mean to say something like "a downward-pointing arrow _corresponds_ to a transformation _which reverses the z-coordinates_ of points"?

Mostly I'm confused because when you give me a vector in R<sup>3</sup> and ask me what linear transformation of R<sup>3</sup> to itself that it's describing, I naturally think of reflection across the perpendicular plane. The vector (0,0,-1) doesn't say "take (x,y,z) to (-x,-y,-z)" to me...but maybe this is just me, and perhaps it's more an issue with `get_transformation` than with `arrow3d`.

At any rate, if you're a bit more clear in that description, you'll be good to go.


---

Comment by jason created at 2008-04-09 08:00:06

Arrows are always constructed pointing up in the z direction from the origin, and then rotated/translated into place.  This works for every arrow direction except the -z direction.  I take care of the issue by testing to see if the arrow should point in the -z direction, and if it should, just scaling the constructed arrow by -1 (i.e., every point is sent to its negative).  The scaled arrow then points downwards.  The doctest just tests that the scale of -1 is applied to the arrow.  I'm not sure how to make it clearer.


---

Attachment

I put up a new patch with the above explanation above the doctest.


---

Comment by mabshoff created at 2008-04-09 09:05:27

Looks good to me. I like the added explanation. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-09 10:01:04

Resolution: fixed


---

Comment by mabshoff created at 2008-04-09 10:01:04

Merged in Sage 3.0.alpha3
