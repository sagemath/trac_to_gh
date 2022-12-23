# Issue 3097: pbuild: make sure the files from setup.py's scripts section are copied

Issue created by migration from https://trac.sagemath.org/ticket/3097

Original creator: mabshoff

Original creation time: 2008-05-03 15:18:09

Assignee: mabshoff

If one uses pbuild to build the Sage library the files from the scripts section are not copied into $SAGE_ROOT/local/bin:

```
      scripts = ['sage/dsage/scripts/dsage_worker.py',
                 'sage/dsage/scripts/dsage_setup.py',
                 'spkg-debian-maybe',
                ],
```

Ergo DSage's doctest just hang at 0% CPU use.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-03 15:18:37

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-05-04 04:09:19

Changing assignee from mabshoff to gfurnish.


---

Comment by mabshoff created at 2008-05-04 04:09:19

Changing component from build to pbuild.


---

Attachment


---

Attachment


---

Comment by gfurnish created at 2008-05-04 11:55:40

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-04 13:22:19

The patches will not work as is:

 * this patchset, especially the bit to setup.py will break slowbuild
 * the scripts repo will be broken once you -sdist
 * what happens on clone

This is as-is not going into 3.0.1 :(.

Cheers,

Michael


---

Comment by gfurnish created at 2008-05-04 14:50:22

1) The patchset should not break slowbuild (infact the change to slowbuild should fix it for the scripts repo).
2) I don't understand why -sdist is going to break the scripts repo.  I added the files to the hg scripts repo, why will sdist break this?
3) the dsage/web directory is a link to devel/sage/...... so it will keep pointing at the right target on clone.


---

Comment by yi created at 2008-05-07 00:22:15

I haven't been able to test this set of patches yet but from speaking with gfurnish on IRC it seems to be the right way to go to resolve the pbuild issue. I'll try these patches out and provide feedback then.


---

Attachment


---

Attachment

this  is a slightly updated version of the original patch by Gary


---

Attachment

oops - this ought to fix the issue


---

Comment by mabshoff created at 2008-05-23 06:23:15

Ok, now the `-sdist` issue is resolved. I did an sdist followed by a full rebuild and a testall. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-23 06:23:30

Merged all six patches in Sage 3.0.2.rc0


---

Comment by mabshoff created at 2008-05-23 06:23:30

Resolution: fixed
