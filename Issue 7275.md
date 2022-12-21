# Issue 7275: [with patch, needs review] numerical noise in tutorial/tour_algebra.rst

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-10-23 21:43:58

Assignee: jhpalmieri

From [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/d2b922ad4ffba33c):

```
sage -t  "devel/sage/doc/en/tutorial/tour_algebra.rst" 
********************************************************************** 
File "/home/jaap/downloads/sage-4.2.alpha0/devel/sage/doc/en/tutorial/tour_algeb ra.rst", line 87: 
     sage: find_root(cos(phi)==sin(phi),0,pi/2) 
Expected: 
     0.78539816339744839 
Got: 
     0.78539816339744828 
********************************************************************** 
1 items had failures: 
Same as in alpha0! No ticket yet? 
```



---

Attachment


---

Comment by jhpalmieri created at 2009-10-23 21:44:54

Changing status from new to needs_review.


---

Comment by jsp created at 2009-10-23 21:59:43

I could not have done this better!



```
sage -t  "devel/sage/doc/en/tutorial/tour_algebra.rst"      
	 [81.2 s]
 
----------------------------------------------------------------------
All tests passed!

```


So positive review.

Jaap


---

Comment by mhansen created at 2009-10-24 03:45:26

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-24 03:46:38

Resolution: fixed


---

Comment by chapoton created at 2017-07-19 08:53:09

unique name please
