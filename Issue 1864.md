# Issue 1864: simple notebook bug -- typing ? in a comment yields introspection but shouldn't (easy to fix in worksheet.py, probably)

Issue created by migration from https://trac.sagemath.org/ticket/1864

Original creator: was

Original creation time: 2008-01-20 16:40:44

Assignee: boothby

Try this in the notebook

```
# This is a question?
```

and hit shift enter.  You get introspection on the word "question".  



---

Comment by boothby created at 2008-03-16 19:13:58

I can't reproduce this in Firefox or Opera -- has it been fixed?


---

Comment by was created at 2008-03-16 20:39:03

This is easy to reproduce in firefox and has not been fixed.
See this screenshot:

http://sage.math.washington.edu/home/was/tmp/screenshot-comment.png


---

Attachment


---

Comment by boothby created at 2008-05-12 05:31:34

This breaks previously supported functionality (that I won't miss).  It used to be, one could type


```
foo?
```


and press shift-enter to introspect.  I give this a positive review *if* that was an intended change.


---

Comment by was created at 2008-05-15 02:08:15

The referee claims that say

```
log?[shift-enter]
```

doesn't work.  

However it *does* work fine with this patch.  The referee needs to try again.


---

Comment by boothby created at 2008-05-17 19:46:09

Weird. Works now.


---

Comment by mabshoff created at 2008-05-17 19:54:56

Resolution: fixed


---

Comment by mabshoff created at 2008-05-17 19:54:56

Merged in Sage 3.0.2.alpha1
