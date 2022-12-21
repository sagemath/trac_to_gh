# Issue 3375: Fix building ntl on Solaris with make and ld [with patch needs review]

Issue created by migration from Trac.

Original creator: fbissey

Original creation time: 2008-06-06 01:22:51

Assignee: mabshoff

CC:  polybori-discuss@lists.sourceforge.net

OK so here is what got me through ntl on David's box.
The mfile patch is against the copy in the ntl patch folder 
not the source. It also patch ntl spkg-install to properly
setup and tune ntl as well as cleaning the installation bits
introduced to accommodate Tim & I.
I guess Tim and I will have to fend for ourselves separately.
Also we submitted a lot of patch in the ntl style. Since
I used some GNU-ism for building shared objects most of
them will have to be revised.

Francois



---

Comment by fbissey created at 2008-06-06 01:23:42

patch for ntl spkg-install and patch/mfile


---

Comment by craigcitro created at 2008-06-15 21:52:48

Changing keywords from "" to "editor_mabshoff".


---

Attachment


---

Comment by mabshoff created at 2008-06-20 04:10:31

Hi Francois, 

Unless I am overlooking something you are removing the "-fPIC" lines from the link phase. Are you sure that will work?

Cheers,

Michael


---

Comment by fbissey created at 2008-06-20 08:43:57

It works all right on linux (no text relocations) but I indeed 
cannot guaranty it on other platform. I just checked the gcc 
manual and they recommand passing the PIC flag used during 
compilation as well when using -shared so best to put it back:

`-shared'
     Produce a shared object which can then be linked with other
     objects to form an executable.  Not all systems support this
     option.  For predictable results, you must also specify the same
     set of options that were used to generate code (`-fpic', `-fPIC',
     or model suboptions) when you specify this option.(1)


---

Comment by fbissey created at 2015-02-22 23:05:40

Changing status from needs_work to needs_review.


---

Comment by fbissey created at 2015-02-22 23:07:01

Changing status from needs_review to positive_review.


---

Comment by fbissey created at 2015-02-22 23:07:01

Looking through old tickets this is sooo obsolete. Won't fix/invalid.


---

Comment by vbraun created at 2015-02-23 21:00:19

Resolution: invalid
