# Issue 9194: Expose and extend the thematic tutorial on symmetric functions

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-06-09 07:52:41

Assignee: sage-combinat

CC:  sage-combinat

Keywords: symmetric functions

Sage needs a good thematic tutorial on symmetric functions. An embryo is in sage.combinat.sf.symmetric_functions, but it's quite indigent (I wrote it, and take the blame):

 - Reference it from doc/en/reference/combinat/symmetric_functions.rst and highlight it as the *main* entry point for symmetric functions
 - Make sure `sage.combinat.sf?` points to this tutorial
 - Extend it! (for general use, but also for kschur and the like)

References:

 - [MuPAD-Combinat's tutorial on Symmetric functions](http://mupad-combinat.sourceforge.net/doc/en/index/guidedTour-predefinedCombinatorialAlgebras.html#index-guidedTour-symmetricFunctions) ([Sources](http://mupad-combinat.svn.sourceforge.net/viewvc/mupad-combinat/trunk/MuPAD-Combinat/lib/DOC/guidedTour-predefinedCombinatorialAlgebras.mupdoc))

 - [Francois's advanced tutorial for MuPAD-Combinat](http://mupad-combinat.sourceforge.net/Papers/TutorialSymFcts.pdf)



---

Comment by jbandlow created at 2010-06-28 15:15:01

I've put a first version on the sage-combinat queue.  It can be built with `sage -docbuild thematic_tutorials html`.  Currently no effort has been made to coordinate with #8533, which will have to be done eventually.  I will continue to work on this, but suggestions and advice are welcome here.


---

Comment by nthiery created at 2013-02-09 23:36:45

This ticket can be closed as soon as #14900 is merged. #5457 took care of providing a nice tutorial, and #14090 exposes it nicely in the thematic tutorials.


---

Comment by nthiery created at 2013-02-09 23:36:45

Changing status from new to needs_review.


---

Comment by nthiery created at 2013-02-09 23:37:09

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-06 13:55:49

Resolution: duplicate
