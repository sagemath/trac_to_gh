# Issue 2992: notebook -- help(foo) in the notebook should not word wrap

Issue created by migration from https://trac.sagemath.org/ticket/2992

Original creator: was

Original creation time: 2008-04-21 17:50:20

Assignee: boothby

This is *very* easy to implement:

  1. Make it so help is a wrapper around internal help.  (Already true?)

  1. If in notebook then display the result using html and pre.  Done.




---

Attachment


---

Comment by was created at 2008-05-11 05:44:42

The attached patch does this:

```

  1. Wrote new version of help command for the notebook.
  2. Slightly modified how truncation is done to account for 1.	 While I was at	it, I fixed another
     but where reloading a page would put multiple "output truncated" messages at the top of the page.

```



---

Comment by boothby created at 2008-05-12 05:54:16

This is ugly -- scroll down:

```
help(interact)
```


I don't know if this is worth a fully negative review, but I think this looks like crap.  Perhaps a pre tag would make it all better?


---

Attachment

I completely rewrote help(...) to address the referee remark and to make help(...) vastly more robust when the output is MASSIVE (which it often is).  Try, e.g., 


```
import numpy
help(numpy)
```


with the new version, and your browser will *not* get killed.  I had my browser
crash in class when teaching with the old version.

Of course the issues with help(interact) are also fixed. 

Apply both patches, in order.


---

Comment by boothby created at 2008-05-15 04:34:54

Failed to apply :(


---

Comment by boothby created at 2008-05-17 19:33:36

Works for me.


---

Comment by mabshoff created at 2008-05-17 19:55:41

Merged both patches in in Sage 3.0.2.alpha1. The dependecy tree is borked since part 2 depends on #3024 being merged. D'oh


---

Comment by mabshoff created at 2008-05-17 19:55:41

Resolution: fixed
