# Issue 6951: Singular fails to build on t2.math with GCC

Issue created by migration from https://trac.sagemath.org/ticket/6951

Original creator: mvngu

Original creation time: 2009-09-17 21:39:42

Assignee: mabshoff

CC:  malb drkirkby

As the subject says. I have attached an install log of Sage 4.1.2.alpha1, building on t2.math with GCC 4.4.1.


---

Attachment

install log for Sage 4.1.2.alpha1 on t2.math with GCC 4.4.1


---

Comment by malb created at 2009-09-17 21:53:45

Here is the relevant portion:


```
for file in *.h; do \
../.././install-sh -c $file /scratch/mvngu/sage-4.1.2.alpha1-6945-readline-cliquer-ecl/local/include/singular; \
done
/bin/sh: ../.././install-sh: not found
```


IIRC Dave fixed this before but I must have missed to include his fix (the update was a bit chaotic because quite a few fixed from different people went in). David, would you mind reminding me how to fix this?


---

Comment by GeorgSWeber created at 2009-09-22 20:49:28

Briefly, we're missing a file "install-sh" for Sun, and possibly a switch change from -O2 to -O0 on Itanium; copied from my post at the sage-devel thread:
Hi Minh,

obviously (look at your own trace output), you are talking about
"singular-3-1-0-4-20090818.spkg", not
"singular-3-1-0-4-20090723.spkg".

Just looking at the top entries of the "SPKG.txt" file of the old
(Sage-4.1.1) "singular-3-1-0-2-20090620.p0.spkg", and of the current
Sage-4.1.2-alpha "singular-3-1-0-4-20090818.spkg", shows what the
problem is, that the latter spkg might be broken also on Itanium
(ia64, see trac #6360 and #6240) i.e. not only on Sun, and what to do
about it.
I can look into building a new spkg with the necessary fixes tomorrow,
or the day after, if nobody beats me to it.

Cheers,
Georg


---

Comment by GeorgSWeber created at 2009-09-24 22:15:18

New ".p0" spkg is up at:

http://sage.math.washington.edu/home/weberg/spkg/singular-3-1-0-4-20090818.p0.spkg


---

Comment by mvngu created at 2009-09-27 04:02:05

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 04:02:05

See my report at #6849. Also builds on t2.math. Now the compilation on t2.math fails when building the package sage-4.1.2.alpha2.spkg. Positive review.


---

Comment by mvngu created at 2009-09-27 11:04:23

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
