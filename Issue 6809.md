# Issue 6809: abstract_methods_of_class

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-08-22 22:57:13

Assignee: nthiery

CC:  sage-combinat

Keywords: abstract methods

Implement a utility abstract_methods_of_class which lists all the optional and mandatory abstract methods of the class.




---

Attachment


---

Comment by hivert created at 2009-10-16 11:33:58

New version with is_optional method


---

Comment by hivert created at 2009-10-16 11:41:13

Changing status from new to needs_review.


---

Attachment

I'm done reviewing this patch. It is good upto a small detail: the code access to a private attribute. I've added an accessor method. 

I just uploaded a new version of the patch after review which add a is_optional method for better encapsulation (as suggested by former comment in the code).

Nicolas: please add a positive review when you finished reviewing my changes.

Cheers,

Florent


---

Comment by hivert created at 2009-10-16 11:47:56

During his review of my change Nicolas spotted a missing blank line after 'EXAMPLE::'... I'm re-uploading the patch...

Cheers,

Florent


---

Comment by hivert created at 2009-10-16 11:54:53

Added missing blank line


---

Attachment

After Blank line added, Nicolas allows me to put the positive review. 

Only apply the last trac_6809_abstract_methods_of_class.3.patch

Florent


---

Comment by hivert created at 2009-10-16 11:58:03

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-19 13:26:02

Resolution: fixed
