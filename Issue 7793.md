# Issue 7793: zorder not implemented in disk

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-12-30 03:40:26

Assignee: was

CC:  jason

From the report a bug link:

It seems that the zorder does not work with disk(). I found a report saying that this was resolved for point() and polygon(), (and I know it works) but nothing about disk(). I found this using the following test:

```
d1 = disk((0,0), 1, (0, 2*pi), color = 'red', zorder=0) 
d2 = disk((0,0), 0.75, (0, 2*pi), color = 'brown', zorder=1)
d3 = disk((0,0), 0.5, (0, 2*pi), color = 'green', zorder= 2)
d4 = disk((0,0), 0.25, (0, 2*pi), color = 'yellow', zorder=3)
final = d4 + d3 + d2 + d1
final.show(aspect_ratio = 1)
```


Incidentally (not in the report), this shows that axes apparently have default zorder of 2.  So do arrows, but polygons have a default of 1.  This is confusing.


---

Comment by kcrisman created at 2009-12-30 03:40:59

Based on 4.3


---

Comment by kcrisman created at 2009-12-30 03:44:03

Changing status from new to needs_review.


---

Attachment

Would be open to suggestions as to how to handle the issues raised in [this](http://groups.google.com/group/sage-devel/browse_thread/thread/ec30de67075e116f) thread, but for now this is up for review.


---

Comment by rossk created at 2010-01-31 11:34:26

Changing status from needs_review to positive_review.


---

Comment by rossk created at 2010-01-31 11:34:26

The patch fixes the zorder problem (the code below produces 3 colorful bullseyes).

```
sage: d1 = disk((0,0), 1, (0, 2*pi), color = 'red', zorder=0) 
sage: d2 = disk((0,0), 0.75, (0, 2*pi), color = 'brown', zorder=1)
sage: d3 = disk((0,0), 0.5, (0, 2*pi), color = 'green', zorder= 2)
sage: d4 = disk((0,0), 0.25, (0, 2*pi), color = 'yellow', zorder=3)
sage: final = d4 + d3 + d2 + d1
sage: final.show(aspect_ratio = 1) 
sage: final2 = d1 + d2 + d3 + d4                                   
sage: final2.show(aspect_ratio = 1)                                
sage: final3 = d3 + d2 + d4 + d1   
sage: final3.show(aspect_ratio = 1)
```

(Note: Intuitively, final, final2 and final3 should all produce the same image and they do)


---

Comment by mpatel created at 2010-02-11 14:56:07

Please remember to update the relevant ticket fields --- the release
managers use an automated script to generate lists of merged tickets.


---

Comment by mpatel created at 2010-02-11 14:56:07

Resolution: fixed
