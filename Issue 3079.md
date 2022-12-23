# Issue 3079: quaddouble configuration and spkg-install cleaning

Issue created by migration from https://trac.sagemath.org/ticket/3079

Original creator: fbissey

Original creation time: 2008-05-02 11:34:25

Assignee: mabshoff

The current spkg-install keep the strange default of the qd 
package. The proposed patch enable ieee error compliant addition
and disable sloppy division and multiplication.
Further spkg-install currently comes with the following strange
settings:
 CXXFLAGS='-fPIC -O3 -Dx86'
-fpic, beside being platform specific, is useless in this case
as no shared object is produced. Flags like -Dx86 are best left
to the configure script, fortunately this should be without effect,
the correct parameter being "X86". Both flags should be removed as well. 


---

Attachment


---

Comment by craigcitro created at 2008-06-15 21:58:01

Changing keywords from "" to "editor_mabshoff".


---

Comment by mabshoff created at 2008-08-11 05:25:57

Since we are dumping quaddouble this ticket is wontfix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-11 05:25:57

Resolution: wontfix
