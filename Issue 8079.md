# Issue 8079: Better documentation for patching spgk's

Issue created by migration from Trac.

Original creator: vbraun

Original creation time: 2010-01-26 14:41:10

Assignee: mvngu

CC:  mvngu

It would be great if the best-practices for patching sage packages were better (at all) documented. The following blog post should be definitely included into the developer manual:

http://mvngu.wordpress.com/2010/01/20/how-to-patch-a-sage-package/

In addition, I'd like to know how to deal with updated configure scripts. Some issues are:
  * The automake sources (configure.ac, Makefile.am, more?) are small and their changes need to be recorded in case upstream makes a new release.
  * The automake sources might be automake-version dependent.
  * Not everyone has all versions of automake installed, so spkg-install can't call automake.
  * Running autoconf/automake generates big shell scripts (configure, makefile). Differences in these need not be recorded.   
  * But different versions of automake will produce different scripts, which would clutter up naive patches.


---

Comment by mvngu created at 2010-02-09 12:10:28

The attachment [trac_8079-patching-spkgs.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8079/trac_8079-patching-spkgs.patch) adds a chapter to the Developer's Guide, explaining how to patch an existing spkg. This attachment also solves the issues reported at #8104 and #3882. Once this ticket is closed, tickets #8104 and #3882 can also be closed as fixed.


---

Comment by mvngu created at 2010-02-09 12:10:28

Changing status from new to needs_review.


---

Attachment

based on Sage 4.3.2; depends on #8199


---

Comment by rossk created at 2010-02-11 06:00:36

Applied patches from tickets #8079, #8199, #7944. Both html and pdf developer manuals built without error. Have little experience with the material but FWIW, it reads very clearly and will be valued by new developers (+1 for positive review)


---

Comment by kcrisman created at 2010-02-12 02:09:45

Overall this looks nice and would have been very helpful to me when first trying spkgs (and still is helpful!).  I don't on a first reading see an explicit reference to the first patched version being .p0 (computer science/Python/Sage numbering) as opposed to .p1 (math numbering), though there is one implicit reference to this.


---

Comment by rossk created at 2010-02-12 09:49:28

Changing status from needs_review to positive_review.


---

Comment by rossk created at 2010-02-12 09:49:28

Changing keywords from "" to "Developer's Guide patching spkg".


---

Comment by mvngu created at 2010-02-14 14:36:51

Feel free to open another ticket for the remaining issues in the ticket description.


---

Comment by mvngu created at 2010-02-14 14:36:51

Resolution: fixed
