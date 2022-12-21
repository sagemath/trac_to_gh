# Issue 7459: sage virtualbox -- install imagemagick

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-14 17:56:37

Assignee: tbd

CC:  kcrisman

When we make the virtualbox sage image for sage-4.2.1, do the following:


```
The easiest way is :

1) Within VirtualBox, use the integrated web navigator SeaMonkey to go
at :

http://www.murga-linux.com/puppy/viewtopic.php?t=45981

2) download the two packages :
ImageMagick-6.5.6-10.pet
ImageMagick_DEV-6.5.6-10.pet

and in dialog, choose : open with petget

3) installation is automatic.
```



---

Comment by vbraun created at 2012-06-02 12:48:08

Changing status from new to needs_review.


---

Comment by vbraun created at 2012-06-02 12:48:08

The current virtual machine contains ImageMagick and I just tested that creating of an animated gif works as expected. Also, for future reference note that you don't need ImageMagick-dev since we just call the executable.

Ticket can be closed.


---

Comment by vbraun created at 2012-06-02 12:48:14

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-06-02 13:31:10

Resolution: worksforme
