# Issue 7606: images not picked up when making source releases of Sage 4.3.alpha0 and 4.3.alpha1

Issue created by migration from https://trac.sagemath.org/ticket/7606

Original creator: mvngu

Original creation time: 2009-12-05 11:41:53

Assignee: mvngu

CC:  ncohen

From this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/11f432ca0302189e) thread (see also [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/af1fa373245166a7)):

```
> 10. sage: hg_sage.status()
>     Getting status of modified or unknown files:
>     cd "/home/SimonKing/sandbox/sage-4.3.alpha0/devel/sage" && hg
> status
>     ! doc/fr/a_tour_of_sage/eigen_plot.png
>     ! doc/fr/a_tour_of_sage/sin_plot.png

> Aha! There is a problem with the docs, right? Are these files missing?

You get those two lines with the exclamation marks because the file
MANIFEST.in in Sage 4.3.alpha0 isn't configured to pick up those two
image files. When ticket #7190 (French translation: A Tour of Sage)
[1] was merged in Sage 4.3.alpha0, the file
devel/sage-main/MANIFEST.in wasn't also changed to take into account
the new image files, so these are not picked up when releasing the
alpha0 tarball. A result is that one would not see the image files in
devel/sage-main/doc/fr/a_tour_of_sage. You can fix the missing files
problem as follows:

[mvngu@sage sage-4.3.alpha0-7473-sphinx]$ cd devel/sage-main/
[mvngu@sage sage-main]$ hg st
! doc/fr/a_tour_of_sage/eigen_plot.png
! doc/fr/a_tour_of_sage/sin_plot.png
[mvngu@sage sage-main]$ hg revert -a
reverting doc/fr/a_tour_of_sage/eigen_plot.png
reverting doc/fr/a_tour_of_sage/sin_plot.png
[mvngu@sage sage-main]$ hg st
<no output>
```

This missing files problem is due to #7190.


---

Attachment

based on Sage 4.3.alpha1


---

Comment by mvngu created at 2009-12-05 12:42:33

Here are some steps to fix the problem with missing image files. On a freshly compiled Sage 4.3.alpha1 or a newly unpacked binary of that version, do a Mercurial revert to recover the deleted images:

```
[mvngu@sage sage-4.3.alpha1-7606-images]$ cd devel/sage-main/
[mvngu@sage sage-main]$ hg st
! doc/fr/a_tour_of_sage/eigen_plot.png
! doc/fr/a_tour_of_sage/sin_plot.png
[mvngu@sage sage-main]$ hg revert -a
reverting doc/fr/a_tour_of_sage/eigen_plot.png
reverting doc/fr/a_tour_of_sage/sin_plot.png
[mvngu@sage sage-main]$ hg st
<no output>
```

Next, apply the patch `trac_7606-manifest.patch`, which configures MANIFEST.in to pick up those two image files when making a source release. Afterwards, making a source tarball with "./sage -sdist <version-number>" should also pick up the two image files.


---

Comment by mvngu created at 2009-12-05 12:42:33

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-12-06 06:52:20

Looks good to me.


---

Comment by mhansen created at 2009-12-06 06:52:20

Resolution: fixed
