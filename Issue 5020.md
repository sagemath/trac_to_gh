# Issue 5020: auto-cells do not automaticall evaluate (or at least update)

Issue created by migration from https://trac.sagemath.org/ticket/5020

Original creator: mhansen

Original creation time: 2009-01-19 04:17:47

Assignee: boothby

Notebook cells that start with "#auto" do not automatically evaluate on the when a worksheet is opened.


---

Comment by mhampton created at 2009-01-19 04:38:39

They do on sagenb, which is running sage-3.2.3, but do not seem to on my laptop (also running sage-3.2.3)...?


---

Comment by mhampton created at 2009-01-19 04:53:59

As a clarification, #auto seems totally broken for me on an unpatched sage-3.2.3 (on intel OS X 10.5).  That install does have a lot of optional spkgs and the tinymce spkgs, but Dan Drake reports it working with the tinymce patches+spkgs, so I don't know what's going on.


---

Attachment

I've add a test to the notebook selenium test suite which tests this.


---

Comment by mhansen created at 2009-01-19 05:35:00

I should mention why this fixes things :-)

The cells are evaluated when .sage() is called, but the HTML send to the web browser was generated before that.


---

Comment by ddrake created at 2009-01-19 05:48:20

Looks good. Positive review.


---

Comment by mabshoff created at 2009-01-19 06:09:54

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-19 06:09:54

Resolution: fixed
