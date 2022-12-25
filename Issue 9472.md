# Issue 9472: Remove (duplicate) BOOST and M4RI source trees from PolyBoRi spkg, some clean-up

archive/issues_009472.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @kcrisman\n\n`SPKG.txt` excerpt from the *modified* spkg:\n\n```\n### polybori-0.6.4.p2 (Leif Leonhardy, July 10th, 2010)\n * Removed Michael Abshoff from maintainer list (see #7738)\n * Deleted Boost source tree again since it was split off into a separate\n   spkg (see below, 0.5.rc.p7), modified spkg-install accordingly\n * Deleted M4RI source tree, because it is a standard Sage package\n * Little clean-up and minor fixes in patches/custom.py\n   - Note that CFLAGS etc. are still *overwritten* rather than modified!\n * Updated \"Dependencies\" section above\n```\n\n\nSlightly more readable:\n* Removed *Michael Abshoff* from maintainer list (see #7738)\n* Deleted Boost source tree again since it was split off into a separate\n  spkg (see below, 0.5.rc.p7), modified `spkg-install` accordingly\n* Deleted M4RI source tree, because it is a standard Sage package\n* Little clean-up and minor fixes in `patches/custom.py`\n  - Note that `CFLAGS` etc. are still **overwritten** rather than modified!\n* Updated *\"Dependencies\"* section above\n\n\nDuring upgrade to 0.6.x, the Boost source unintentionally got in again. The new spkg is about 1.7MB, i.e. 300KB smaller.\n\nTo test *the patch*, the directories have to be removed manually (the attached patch doesn't delete them from 0.6.4.p1), but **the new spkg will be uploaded to sage.math soon**.\n\nSince PolyBoRi also uses GD, `$SAGE_ROOT/spkg/standard/deps` should be updated (but there seem to have been no issues with that in the past).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9472\n\n",
    "created_at": "2010-07-11T00:05:23Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Remove (duplicate) BOOST and M4RI source trees from PolyBoRi spkg, some clean-up",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9472",
    "user": "https://github.com/nexttime"
}
```
Assignee: tbd

CC:  @kcrisman

`SPKG.txt` excerpt from the *modified* spkg:

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
* Removed *Michael Abshoff* from maintainer list (see #7738)
* Deleted Boost source tree again since it was split off into a separate
  spkg (see below, 0.5.rc.p7), modified `spkg-install` accordingly
* Deleted M4RI source tree, because it is a standard Sage package
* Little clean-up and minor fixes in `patches/custom.py`
  - Note that `CFLAGS` etc. are still **overwritten** rather than modified!
* Updated *"Dependencies"* section above


During upgrade to 0.6.x, the Boost source unintentionally got in again. The new spkg is about 1.7MB, i.e. 300KB smaller.

To test *the patch*, the directories have to be removed manually (the attached patch doesn't delete them from 0.6.4.p1), but **the new spkg will be uploaded to sage.math soon**.

Since PolyBoRi also uses GD, `$SAGE_ROOT/spkg/standard/deps` should be updated (but there seem to have been no issues with that in the past).

Issue created by migration from https://trac.sagemath.org/ticket/9472





---

archive/issue_comments_090701.json:
```json
{
    "body": "Attachment [polybori-0.6.4.p1-p2.patch](tarball://root/attachments/some-uuid/ticket9472/polybori-0.6.4.p1-p2.patch) by @nexttime created at 2010-07-11 00:12:21\n\nApply to polybori-0.6.4.p1. Source trees have to be removed manually.",
    "created_at": "2010-07-11T00:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90701",
    "user": "https://github.com/nexttime"
}
```

Attachment [polybori-0.6.4.p1-p2.patch](tarball://root/attachments/some-uuid/ticket9472/polybori-0.6.4.p1-p2.patch) by @nexttime created at 2010-07-11 00:12:21

Apply to polybori-0.6.4.p1. Source trees have to be removed manually.



---

archive/issue_comments_090702.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-11T01:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90702",
    "user": "https://github.com/nexttime"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090703.json:
```json
{
    "body": "\n```\n$ diff -qr polybori-0.6.4.p1/ polybori-0.6.4.p2/\n...\nFiles polybori-0.6.4.p1/SPKG.txt and polybori-0.6.4.p2/SPKG.txt differ\nFiles polybori-0.6.4.p1/patches/custom.py and polybori-0.6.4.p2/patches/custom.py differ\nFiles polybori-0.6.4.p1/spkg-install and polybori-0.6.4.p2/spkg-install differ\nOnly in polybori-0.6.4.p1/src: boost_1_34_1.cropped\nOnly in polybori-0.6.4.p1/src/polybori-0.6.4: M4RI\n```\n\nI.e., to remove the Boost and M4RI source trees, do:\n\n```sh\nrm -rv polybori-0.6.4.p1/src/boost_1_34_1.cropped\nrm -rv polybori-0.6.4.p1/src/polybori-0.6.4/M4RI\n```\n\n\nI've tested the spkg with Sage 4.5.alpha4 (with SageNB 0.8.1 and zodb3 3.7.0.p4) on Ubuntu 9.04 x86_64; all tests, including long ones, passed.",
    "created_at": "2010-07-11T01:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90703",
    "user": "https://github.com/nexttime"
}
```


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

archive/issue_comments_090704.json:
```json
{
    "body": "leif's updated spkg: [polybori-0.6.4.p2.spkg](http://sage.math.washington.edu/home/schilly/sage/spkg/polybori-0.6.4.p2.spkg)",
    "created_at": "2010-07-11T10:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90704",
    "user": "https://github.com/haraldschilly"
}
```

leif's updated spkg: [polybori-0.6.4.p2.spkg](http://sage.math.washington.edu/home/schilly/sage/spkg/polybori-0.6.4.p2.spkg)



---

archive/issue_comments_090705.json:
```json
{
    "body": "I replaced thePolyBoRi SPKG in Sage 4.5.alpha4 with the one linked above and built Sage from scratch without problems. All doctests also pass on sage.math. I checked the install log andPolyBoRi reports M4RI found (and wouldn't build without Boost anyway).",
    "created_at": "2010-07-11T18:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90705",
    "user": "https://github.com/malb"
}
```

I replaced thePolyBoRi SPKG in Sage 4.5.alpha4 with the one linked above and built Sage from scratch without problems. All doctests also pass on sage.math. I checked the install log andPolyBoRi reports M4RI found (and wouldn't build without Boost anyway).



---

archive/issue_comments_090706.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-11T18:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90706",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090707.json:
```json
{
    "body": "It seems that we can install PolyBoRi in parallel with, e.g.,\n\n```sh\n$ env MAKEOPTS=\"-j20\" ./sage -f http://sage.math.washington.edu/home/schilly/sage/spkg/polybori-0.6.4.p2.spkg\n```\n\nBut I haven't tested this extensively.",
    "created_at": "2010-08-07T11:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90707",
    "user": "https://github.com/qed777"
}
```

It seems that we can install PolyBoRi in parallel with, e.g.,

```sh
$ env MAKEOPTS="-j20" ./sage -f http://sage.math.washington.edu/home/schilly/sage/spkg/polybori-0.6.4.p2.spkg
```

But I haven't tested this extensively.



---

archive/issue_comments_090708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90708",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_090709.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n\nDid you also update/correct `standard/deps` to reflect the GD dependency (cf. bottom note in the ticket's description)?",
    "created_at": "2010-08-09T17:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90709",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:6 mpatel]:

Did you also update/correct `standard/deps` to reflect the GD dependency (cf. bottom note in the ticket's description)?



---

archive/issue_comments_090710.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> Replying to [comment:6 mpatel]:\n> \n> Did you also update/correct `standard/deps` to reflect the GD dependency (cf. bottom note in the ticket's description)?\n\nNo, I didn't.  I apologize for that.  (We should have, for the record, an updated `deps` file, or a `deps.diff` *at minimum*, attached to trac.)\n\nSince \"there seem to have been no issues with that [the missing GD dependency] in the past\" and I'm nearly ready to release the current trial 4.5.3.alpha0, I've opened #9712 and suggest that we merge it in 4.5.3.alpha1.\n\nI assume the GD change itself is already reviewed, so I can review #9712 fairly quickly.  Or, if I have a spare moment, I'll post a new `deps` and `deps.diff`.\n\n(Ticket #9433 should help with these types of changes.)",
    "created_at": "2010-08-09T22:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90710",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:7 leif]:
> Replying to [comment:6 mpatel]:
> 
> Did you also update/correct `standard/deps` to reflect the GD dependency (cf. bottom note in the ticket's description)?

No, I didn't.  I apologize for that.  (We should have, for the record, an updated `deps` file, or a `deps.diff` *at minimum*, attached to trac.)

Since "there seem to have been no issues with that [the missing GD dependency] in the past" and I'm nearly ready to release the current trial 4.5.3.alpha0, I've opened #9712 and suggest that we merge it in 4.5.3.alpha1.

I assume the GD change itself is already reviewed, so I can review #9712 fairly quickly.  Or, if I have a spare moment, I'll post a new `deps` and `deps.diff`.

(Ticket #9433 should help with these types of changes.)



---

archive/issue_comments_090711.json:
```json
{
    "body": "Karl-Dieter (kcrisman) has just reported on sage-release updating from 4.5.2 to 4.5.3.alpha0 failed on MacOS X 10.6 because this new PolyBoRi package failed to build:\n\n```\n...\nChecking for C library m4ri... no\nChecking for C header file gd.h... yes\nChecking for C library gd... no\nSymlinking to M4RI/m4ri ...\nOSError: [Errno 2] No such file or directory:\n  File \"/Users/.../sage-4.5.2/spkg/build/polybori-0.6.4.p2/src/\npolybori-0.6.4/SConstruct\", line 421:\n    os.symlink('.', m4ri_inc)\nError building PolyBoRi.\n \nreal\t0m1.425s\nuser\t0m0.860s\nsys\t0m0.473s\nsage: An error occurred while installing polybori-0.6.4.p2\n...\n```\n\n\nI'll open a new ticket for that shortly (unless someone else is faster).",
    "created_at": "2010-08-10T22:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90711",
    "user": "https://github.com/nexttime"
}
```

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

archive/issue_comments_090712.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n> I'll open a new ticket for that shortly (unless someone else is faster).\n\nI've opened #9721 for this.",
    "created_at": "2010-08-11T01:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9472#issuecomment-90712",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:9 leif]:
> I'll open a new ticket for that shortly (unless someone else is faster).

I've opened #9721 for this.
