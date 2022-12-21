# Issue 9161: update nzmath optional package to 1.0 and post about this to NMBRTHY

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-07 01:46:27

Assignee: tbd




---

Comment by was created at 2010-06-07 01:51:04

Changing status from new to needs_review.


---

Comment by was created at 2010-06-07 01:51:04

Spkg here:

 http://sage.math.washington.edu/home/wstein/patches/nzmath-1.0.0.spkg

The SPKG.txt should probably be formated more.  However, note that the nzmath0.6.0 spkg in our current repo doesn't even have an SPKG.txt!

I would like to make this available soon, so I can post a response on the number theory list.


---

Comment by AlexGhitza created at 2010-06-07 02:37:01

I added some info to SPKG.txt, and I created `.hgignore` to make Mercurial ignore the files in src/ .  The modified spkg is at

http://sage.math.washington.edu/home/ghitza/nzmath-1.0.0.spkg


---

Comment by AlexGhitza created at 2010-06-07 02:42:27

Forgot to say this, but I think only my changes need review at this point, I'm happy with the spkg otherwise.


---

Comment by mhansen created at 2010-06-07 05:06:11

Resolution: fixed


---

Comment by mhansen created at 2010-06-07 05:06:11

Alex's changes look good to me.
