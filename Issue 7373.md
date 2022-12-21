# Issue 7373: [with spkg; needs review] Disable assembly code in libgcrypt on Solaris x86 & rare platforms.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-11-02 01:05:58

Assignee: drkirkby

On my Sun Ultra 27, which has a quad core Xeon, running OpenSolaris 06/2009, libgrcypt would not build. The error message indicated it was related to the use of assembly code. 

However, I believe libgcrypt did not cause an issue on 'disk.math', so I'm somewhat surprised it did on my Ultra 27. But I think it is safer to disable assembly language on all Solaris x86 systems. (It is *not* necessary to do so on Solaris on SPARC)

I also added some tests for other platforms (AIX, HP-UX, Tru64 and IRIX) and disabled assembly language on them too. It is most unlikely assembly code for them will work, and I hope to try at least some of these platforms in the near future. 

The only updates are to spkg-install and SPKG.txt. The revised files will be put into 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/libgcrypt-1.4.4.p1 

within 30 minutes of this post. (I thought I'd get the trac ticket in first, so the trac number can go into the SPKG.txt)



Dave


---

Comment by drkirkby created at 2009-11-02 04:25:32

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-02 04:58:22

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-02 04:58:22

Looks good to me.


---

Comment by mhansen created at 2009-11-02 05:48:52

Resolution: fixed
