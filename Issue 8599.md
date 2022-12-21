# Issue 8599: Allow size as an argument for point2d

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-03-24 15:30:11

Assignee: slabbe

For 3d points, one must use the argument `size`  :


```
sage: point((2,3,4), size=100)
```


But for 2d points, one must use the argument `pointsize`  :


```
sage: point((2,3), size=100)
verbose 0 (136: primitive.py, options) WARNING: Ignoring option 'size'=100
verbose 0 (136: primitive.py, options) 
The allowed options for Point set defined by 1 point(s) are:
    alpha          How transparent the line is.                                
    faceted        If True color the edge of the point.                        
    hue            The color given as a hue.                                   
    pointsize      How big the point is.                                       
    rgbcolor       The color as an RGB tuple.                                  
    zorder         The layer level in which to draw                            


sage: point((2,3), pointsize=100)
```


I think `pointsize` is kind of redundant and `size` would not be ambiguous. At least, if we keep `pointsize` for backward compatibility reasons, I would like


```
sage: point((2,3), size=100)
```


to work.



---

Comment by slabbe created at 2010-03-24 17:46:40

Changing status from new to needs_review.


---

Attachment


---

Comment by slabbe created at 2010-03-25 13:40:24

I improved a comment about pointsize vs size and just uploaded the patch.


---

Comment by jason created at 2010-03-25 16:51:11

Positive review on slabbe's patch.

I enhanced the documentation for pointsize, added a deprecation functionality for the rename decorator, and then deprecated the pointsize keyword in my patch.  My patch needs to be reviewed now.


---

Comment by jason created at 2010-03-25 19:08:49

apply on top of previous patch


---

Attachment

Okay, I moved the deprecation code over to #8607, since William requested that we don't deprecate the pointsize option (for mma compatibility).  I've instead posted a new patch which just contains a few documentation enhancements and fixes.  Sebastien, can you review my patch?  If it's a positive review, then set this to positive review.


---

Comment by slabbe created at 2010-03-26 13:46:23

Positive review for Jason's doc fixes.

#8607 = great!


---

Comment by slabbe created at 2010-03-26 13:46:23

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:51:09

Merged in 4.4.alpha0:
 - trac_8599_pointsize-sl.patch
 - trac-8599-fix-docs.patch


---

Comment by jhpalmieri created at 2010-04-16 18:51:09

Resolution: fixed
