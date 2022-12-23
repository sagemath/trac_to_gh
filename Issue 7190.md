# Issue 7190: French translation: A Tour of Sage

Issue created by migration from https://trac.sagemath.org/ticket/7190

Original creator: mvngu

Original creation time: 2009-10-12 02:06:53

Assignee: tba

CC:  loufer

French translation of the document: "A Tour of Sage".


---

Comment by ncohen created at 2009-10-12 06:33:52

Changing status from new to needs_review.


---

Attachment

Here it is !!!

Some remarks, though :

    * I copied the file conf.py, without being sure of why...
    * I did not touch it either, but it may be necessary
    * The two .png files, which are copied from the original directory, do not seem to be included in the patch I exported.
    * As you can see, it is very quick to write translations.. I did not forget what I said about translating Sage in French. Actually, I began to look for things that needed translations and intended to write a list of it, but ended up doing other things instead... Though when I know what is to be translated, once more, it is very quick :-)

I'm sending an email to Philippe Saade, as I do not know his username to add him in Cc.

Nathann


---

Comment by mvngu created at 2009-10-12 06:57:58

Luis F. Villegas has also made a French translation of this document.


---

Attachment

add png images into fr/a_tour_of_sage


---

Attachment

attachment:trac_7190_add_images.patch adds in the images. I'd prefer that we have only one copy of the images, but I don't know how to convince Sphinx to load the images from the en/a_tour_of_sage directory.

Nathann's patch looks good, although I can't comment on his writing.


---

Comment by ddrake created at 2009-10-30 01:53:42

#7353 depends on this ticket -- it switches Sphinx's language to French.

Also, should the document title (the "project" line in conf.py) be "Une tournée de Sage"?


---

Attachment

Looks good to me.


---

Comment by mhansen created at 2009-11-17 07:55:35

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-17 07:55:45

Resolution: fixed


---

Comment by mvngu created at 2009-12-05 11:43:02

See #7606 for a follow up to this ticket.
