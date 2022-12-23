# Issue 9835: Linear Programming Thematic Tutorial

Issue created by migration from https://trac.sagemath.org/ticket/9836

Original creator: ncohen

Original creation time: 2010-08-29 03:56:30

Assignee: mvngu

CC:  minh rhinton

Here it is ! The long-promised tutorial for LP. It is a translation of the french sagebook, and I hope I will be able to keep the two coordinated `:-)`

This patchremoved the old tutorial from the "constructions" document where it shouldn't have been put in the first place, and creates a new file in thematic_tutorials. It is up-to-date for the moment, though I hope to be able to work on some improvements with the CPLEX interface soon. It may only change te way CPLEX has to be installed, which would only require a minor edit later.


---

Attachment


---

Attachment


---

Comment by ncohen created at 2010-08-29 04:06:40

The two pictures should be added to the `thematic_tutotials/` folder. This patch does not pass doctests for two reasons :

    * Sage forgets the definition of the variables between different code sections (if you have any idea about how to fix this `^^;`)

    * There is a random doctest which should fail every second run, but it is a bit hard to fix with all the previous errors

Sorry to send this patch like that. This may be the last time I can access internet before next week (and I incidentally skipped my second meal today to finish it `:-D`), so if somebody knows how to fix these.. Otherwise, I'll take care of it when I'm back `:-)`

Nathann


---

Comment by ncohen created at 2010-08-29 04:06:40

Changing status from new to needs_work.


---

Comment by ncohen created at 2010-09-04 11:26:24

Updated thanks to wise advice `:-)`

http://groups.google.com/group/sage-devel/browse_thread/thread/415a5c9fb8939c41/3c6d911b4d2fd2b3?lnk=gst&q=sphinx+forgets#3c6d911b4d2fd2b3

It is now ready for review !

Nathann


---

Comment by ncohen created at 2010-09-04 11:26:24

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-09-11 08:23:56

I'm happy with ncohen's tutorial. I have attached a reviewer patch to make it slightly better. Changes include:

 * Directly add the two images with `hg add`. This makes sure that the images are under revision control.
 * Where possible, cut off lines at about 75 characters.
 * Some consistency in how you space headings.
 * Some consistency in how you present Sage code.
 * Use 4 space indentation.
 * Numerous typo fixes.
 * Simplify some of the prose to suit a tutorial format.

I need another pair of eyes to check my patch.


---

Comment by ncohen created at 2010-09-11 10:48:43

Thank you for your patch Minh ! I noticed reviewing it that I had forgotten to rename a variable, ``"poids"``, which means "weight" in french `:-D`

Could you check this small patch before changing this ticket's status ?

Thanks !

Nathann


---

Attachment


---

Comment by mvngu created at 2010-09-11 11:07:13

Good! Let's get it into the standard documentation.


---

Comment by mvngu created at 2010-09-11 11:07:13

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 11:38:19

Resolution: fixed


---

Attachment

Add new .png files to `MANIFEST.in`


---

Comment by mpatel created at 2010-09-16 02:10:42

I've attached a patch that fixes two Sphinx warnings:

```
/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage/doc/en/thematic_tutorials/linear_programming.rst:: WARNING: image file not readable: static/lp_flot1.png
/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage/doc/en/thematic_tutorials/linear_programming.rst:: WARNING: image file not readable: static/lp_flot2.png
```

