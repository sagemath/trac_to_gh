# Issue 2645: arrow3d is sometimes too long

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-22 15:41:23

Assignee: was

The patch below cuts off the shaft and part of the head if an arrow3d is too long for the given vector.


---

Attachment


---

Comment by mabshoff created at 2008-03-22 21:16:28

In https://groups.google.com/group/sage-devel/browse_thread/thread/d88bc7503638af0c Robert Bradshaw commented:

```
The line3d command will produce much faster arrows:

line3d([(0,0,0), (1,2,3)], thickness=2, arrow_head=True)

The ds parameter is supposed to relate the size of the overall scene  
to the number of pixels in the final render. I agree there needs to  
be a better way to set it. 
```


Cheers,

Michael


---

Comment by jason created at 2008-03-22 22:14:59

The comment about line3d does not change the bug and does not change the patch.  The comment about line3d was to address a problem with plot_vector_field3d (#2646)


---

Comment by robertwb created at 2008-03-27 06:29:32

Works great for me. A good example of this is


```
sage: sum([arrow3d((cos(t),sin(t),0),(cos(t),sin(t),t/10)) for t in [0,0.3,..,2*pi]])
```



---

Comment by mabshoff created at 2008-03-27 07:42:10

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-27 07:42:10

Resolution: fixed
