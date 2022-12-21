# Issue 7979: pari-2.3.3 sometimes ignores --graphic=none build option

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2010-01-18 17:48:44

Assignee: GeorgSWeber

CC:  jsp

pdehaye reported a build error in pari on IRC.

We tracked this down to what seems to be a bug in pari's Configure script (or rather config/get_fltk): if X11 is not found, and fltk is found, it ignores the --graphic=none option. It then tries to build with fltk support, and fails spectacularly.

(Aside: pari-2.4.2.alpha still has the same logic in config/get_fltk.)


---

Attachment

I contacted Karim Belabas about this, suggesting the attached patch to pari's `config/get_fltk`.


---

Comment by mvngu created at 2010-02-02 17:58:41

Updated spkg is up at

http://boxen.math.washington.edu/home/mvngu/spkg/standard/pari/pari-2.3.3.p8.spkg

This has Willem's patch for `src/config/get_fltk`. This spkg might need to be based on that at #8099.


---

Comment by mvngu created at 2010-02-02 17:58:41

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-04-29 06:09:56

Ticket #8453 upgrades Pari to version 2.3.5, so this ticket is no longer relevant. So I'm closing this ticket as "wontfix". However, the file `config/get_fltk` in Pari 2.3.5 has the same logic as in Pari 2.3.3 so it's possible that Pari 2.3.5 also ignores the build option "--graphic=none". If that issue comes up, open another ticket to patch Pari 2.3.5 for Sage.


---

Comment by mvngu created at 2010-04-29 06:09:56

Resolution: wontfix
