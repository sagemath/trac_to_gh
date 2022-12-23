# Issue 9472: Remove (duplicate) BOOST and M4RI source trees from PolyBoRi spkg, some clean-up

Issue created by migration from https://trac.sagemath.org/ticket/9472

Original creator: leif

Original creation time: 2010-07-11 00:05:23

Assignee: tbd

CC:  kcrisman

`SPKG.txt` excerpt from the _modified_ spkg:

```
### polybori-0.6.4.p2 (Leif Leonhardy, July 10th, 2010)
 * Removed Michael Abshoff from maintainer list (see #7738)
 * Deleted Boost source tree again since it was split off into a separate
   spkg (see below, 0.5.rc.p7), modified spkg-install accordingly
 * Deleted M4RI source tree, because it is a standard Sage package
 * Little clean-up and minor fixes in patches/custom.py
   - Note that CFLAGS etc. are still *overwritten* rather than modified!
 * Updated "Dependencies" section above
```


Slightly more readable:
 * Removed _Michael Abshoff_ from maintainer list (see #7738)
 * Deleted Boost source tree again since it was split off into a separate
   spkg (see below, 0.5.rc.p7), modified `spkg-install` accordingly
 * Deleted M4RI source tree, because it is a standard Sage package
 * Little clean-up and minor fixes in `patches/custom.py`
   - Note that `CFLAGS` etc. are still *overwritten* rather than modified!
 * Updated _"Dependencies"_ section above


During upgrade to 0.6.x, the Boost source unintentionally got in again. The new spkg is about 1.7MB, i.e. 300KB smaller.

To test _the patch_, the directories have to be removed manually (the attached patch doesn't delete them from 0.6.4.p1), but *the new spkg will be uploaded to sage.math soon*.

Since PolyBoRi also uses GD, `$SAGE_ROOT/spkg/standard/deps` should be updated (but there seem to have been no issues with that in the past).


---

Attachment

Apply to polybori-0.6.4.p1. Source trees have to be removed manually.


---

Comment by leif created at 2010-07-11 01:00:27

Changing status from new to needs_review.


---

Comment by leif created at 2010-07-11 01:00:27


```
$ diff -qr polybori-0.6.4.p1/ polybori-0.6.4.p2/
...
Files polybori-0.6.4.p1/SPKG.txt and polybori-0.6.4.p2/SPKG.txt differ
Files polybori-0.6.4.p1/patches/custom.py and polybori-0.6.4.p2/patches/custom.py differ
Files polybori-0.6.4.p1/spkg-install and polybori-0.6.4.p2/spkg-install differ
Only in polybori-0.6.4.p1/src: boost_1_34_1.cropped
Only in polybori-0.6.4.p1/src/polybori-0.6.4: M4RI
```

I.e., to remove the Boost and M4RI source trees, do:

```sh
rm -rv polybori-0.6.4.p1/src/boost_1_34_1.cropped
rm -rv polybori-0.6.4.p1/src/polybori-0.6.4/M4RI
```


I've tested the spkg with Sage 4.5.alpha4 (with SageNB 0.8.1 and zodb3 3.7.0.p4) on Ubuntu 9.04 x86_64; all tests, including long ones, passed.


---

Comment by schilly created at 2010-07-11 10:04:50

leif's updated spkg: [polybori-0.6.4.p2.spkg](http://sage.math.washington.edu/home/schilly/sage/spkg/polybori-0.6.4.p2.spkg)


---

Comment by malb created at 2010-07-11 18:58:12

I replaced thePolyBoRi SPKG in Sage 4.5.alpha4 with the one linked above and built Sage from scratch without problems. All doctests also pass on sage.math. I checked the install log andPolyBoRi reports M4RI found (and wouldn't build without Boost anyway).


---

Comment by malb created at 2010-07-11 18:58:12

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-07 11:04:13

It seems that we can install PolyBoRi in parallel with, e.g.,

```sh
$ env MAKEOPTS="-j20" ./sage -f http://sage.math.washington.edu/home/schilly/sage/spkg/polybori-0.6.4.p2.spkg
```

But I haven't tested this extensively.


---

Comment by mpatel created at 2010-08-09 09:39:13

Resolution: fixed


---

Comment by leif created at 2010-08-09 17:09:12

Replying to [comment:6 mpatel]:

Did you also update/correct `standard/deps` to reflect the GD dependency (cf. bottom note in the ticket's description)?


---

Comment by mpatel created at 2010-08-09 22:45:16

Replying to [comment:7 leif]:
> Replying to [comment:6 mpatel]:
> 
> Did you also update/correct `standard/deps` to reflect the GD dependency (cf. bottom note in the ticket's description)?

No, I didn't.  I apologize for that.  (We should have, for the record, an updated `deps` file, or a `deps.diff` _at minimum_, attached to trac.)

Since "there seem to have been no issues with that [the missing GD dependency] in the past" and I'm nearly ready to release the current trial 4.5.3.alpha0, I've opened #9712 and suggest that we merge it in 4.5.3.alpha1.

I assume the GD change itself is already reviewed, so I can review #9712 fairly quickly.  Or, if I have a spare moment, I'll post a new `deps` and `deps.diff`.

(Ticket #9433 should help with these types of changes.)


---

Comment by leif created at 2010-08-10 22:01:07

Karl-Dieter (kcrisman) has just reported on sage-release updating from 4.5.2 to 4.5.3.alpha0 failed on MacOS X 10.6 because this new PolyBoRi package failed to build:

```
...
Checking for C library m4ri... no
Checking for C header file gd.h... yes
Checking for C library gd... no
Symlinking to M4RI/m4ri ...
OSError: [Errno 2] No such file or directory:
  File "/Users/.../sage-4.5.2/spkg/build/polybori-0.6.4.p2/src/
polybori-0.6.4/SConstruct", line 421:
    os.symlink('.', m4ri_inc)
Error building PolyBoRi.
 
real	0m1.425s
user	0m0.860s
sys	0m0.473s
sage: An error occurred while installing polybori-0.6.4.p2
...
```


I'll open a new ticket for that shortly (unless someone else is faster).


---

Comment by mpatel created at 2010-08-11 01:18:35

Replying to [comment:9 leif]:
> I'll open a new ticket for that shortly (unless someone else is faster).

I've opened #9721 for this.
