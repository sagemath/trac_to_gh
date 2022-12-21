# Issue 6965: preventing repository corruption with MANIFEST.in

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-20 02:56:51

Assignee: tba

CC:  jason

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/61612a7bcca169e7/17f2ab8eb4f63b7f):

```
I should have posted this question here instead of at #6865, as the
answer is probably interesting to many people here.  I'd heard things
about MANIFEST.in, but for some reason didn't have a clear idea of what
it was or what I should do about it.  It would be nice if something was
added to the developer's guide... 
```



---

Comment by jhpalmieri created at 2009-09-21 23:19:13

For future reference: see [http://www.python.org/doc/2.6.2/distutils/sourcedist.html#specifying-the-files-to-distribute](http://www.python.org/doc/2.6.2/distutils/sourcedist.html#specifying-the-files-to-distribute) for the relevant part of the Python distribution.


---

Comment by jhpalmieri created at 2009-09-21 23:20:24

> For future reference: see http://www.python.org/doc/2.6.2/distutils/sourcedist.html#specifying-the-files-to-distribute for the relevant part of the Python distribution.

(change "distribution" to "documentation")


---

Comment by jhpalmieri created at 2009-12-22 00:43:45

Here's a patch.


---

Comment by jhpalmieri created at 2009-12-22 00:43:45

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-12-22 00:43:45

Changing priority from major to minor.


---

Comment by mvngu created at 2009-12-22 08:33:13

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2009-12-22 08:33:13

Looks good. Applied OK against Sage 4.3.rc0. As a side note, the URL for "Specifying the files to distribute" could also be 

http://docs.python.org/distutils/sourcedist.html#specifying-the-files-to-distribute

which is usually more up-to-date than the given URL. The given URL is more specific to Python 2.6.2.


---

Attachment

Good point about the URL.  I've replaced the patch with a new one, changing just the URL to the more permanent one.


---

Comment by mhansen created at 2010-01-03 22:04:51

Resolution: fixed
