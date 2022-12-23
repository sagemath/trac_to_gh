# Issue 512: update gap package

Issue created by migration from https://trac.sagemath.org/ticket/512

Original creator: wdj

Original creation time: 2007-08-29 14:43:30

Assignee: wdj

The package 
http://sage.math.washington.edu/home/wdj/patches/gap-4.4.9.p1.spkg
has the latest version of guava (guava 3.0, incorporating work
of Robert Miller and Tom Boothby). 


---

Comment by was created at 2007-08-29 22:40:31

Resolution: fixed


---

Comment by was created at 2007-08-29 22:40:31

done for sage-2.8.3.


---

Comment by was created at 2007-08-30 06:48:27

Changing status from closed to reopened.


---

Comment by was created at 2007-08-30 06:48:27

Resolution changed from fixed to 


---

Comment by was created at 2007-08-30 06:53:19


```

David,

I made some fixes to gap-4.4.9.p1.spkg  to make it suitable for inclusion in SAGE.
Unfortunately when I did a clean build of SAGE with this gap package there were
numerous doctest failures in all the following packages;

        sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py
        sage -t  devel/sage-main/sage/coding/guava.py
        sage -t  devel/sage-main/sage/coding/linear_code.py
        sage -t  devel/sage-main/sage/coding/code_constructions.py
        sage -t  devel/sage-main/sage/coding/code_bounds.py

I'm reverting to the previous gap package until I figure how to get these resolved.

I've put my version of gap-4.4.9.p1.spkg here:
   http://sage.math.washington.edu/tmp

 -- William
```



---

Comment by was created at 2007-10-05 03:29:19

Changing component from coding theory to packages.


---

Comment by was created at 2007-10-05 03:29:19

Changing priority from minor to major.


---

Comment by was created at 2007-10-05 03:29:55

From David Joyner

```
(1) The package

http://sage.math.washington.edu/home/wdj/patches/gap-4.4.10.spkg

installs okay passes these tests. However, I added a build for Leon's code,
which
(a) was only tested on one machine,
(b) is based on my negligable knowledge of how Makefiles/spkg install
files work (so I got lucky that it seemss to have worked even on one
machine!).

I think GAP version 4.4.10 will be officially released tomorrow.

(2) This might be way too old, but I wonder if you could at least try
to apply the patch

http://sage.math.washington.edu/home/wdj/patches/maxima-patch-latest-really.hg

which I think fixes some old minor bugs in the interface to special
functions. (The file dates from November of last year!) I created a
clone, viewed it using hg_sage.inspect and noticed it
seems to only affect special functions. Then I applied the patch and ran

./sage -t "/home/wdj/sagefiles/sage-2.8.3.rc3/devel/sage-maxima/sage/functions/special.py"

(All tests passed.) I tried to view it again (to see what else it
might change, in case I misssed something) but couldn't.


+++++++++++++++++++++++++++++++++++++++++++++++++++

```



---

Comment by was created at 2007-10-20 20:51:28

Resolution: fixed


---

Comment by was created at 2007-10-20 20:51:28

I've upgraded everything to gap-4.4.10, and fixed the insanely bloated 4.4.10 spkg that was on David's web page.
