# Issue 7705: graphs: replace the worldmap sobj by some code (or something else that is transparent)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-16 08:45:55

Assignee: rlm

CC:  ncohen

This command in sage-4.3 returns a loaded sobj:

```
sage: graphs.WorldMap()
Graph on 251 vertices
```



---

Comment by was created at 2009-12-16 08:53:39

See also #7706.


---

Comment by ncohen created at 2009-12-16 18:22:08

Changing status from new to needs_review.


---

Comment by ncohen created at 2009-12-16 18:23:27

With this patch applied, the file SAGE_DATA+"graphs/graph_world.sobj" could be removed !

Nathann


---

Comment by rlm created at 2009-12-16 18:49:37

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-17 01:08:54

Thanks.  However, you forgot to include the gps_coordinates attribute that was in graph_world.sobj.


---

Comment by was created at 2009-12-17 01:08:54

Changing status from positive_review to needs_work.


---

Comment by ncohen created at 2009-12-17 09:48:18

You're absolutely right !! With some luck, someone will take the time to translate these GPS coordinates using the Mercator projection to obtain good plottings of the world :-)

Nathann


---

Comment by ncohen created at 2009-12-17 09:48:18

Changing status from needs_work to needs_review.


---

Attachment


---

Attachment


---

Comment by rlm created at 2009-12-17 21:40:03

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 20:21:24

Resolution: fixed
