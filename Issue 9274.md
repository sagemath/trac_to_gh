# Issue 9274: do some cleanup of the deps file, as suggested by Carl Hansen

archive/issues_009274.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  drkirkby @jhpalmieri\n\n\n```\n\nHere is an excerpt from \"deps\" , the makefile in spkg/standard\n\n$(INST)/$(FORTRAN):\n       $(SAGE_SPKG) $(FORTRAN) 2>&1\n\n$(INST)/$(F2C): $(INST)/$(FORTRAN)\n       $(SAGE_SPKG) $(INST)/$(F2C) 2>&1\n                    ^^^^^^^ --------------------Notice that this is\nwrong.\n                                              the INST is not needed\nand is wrong.\n$(INST)/$(PIL): $(INST)/$(PYTHON)\n       $(SAGE_SPKG) $(PIL) 2>&1\n\n\nThe only reason it works is that the script that reads it cleans it up\nwith\n\"basename\".\n\nBut that's imperfect.\n\n\nThere are 3 instances, shown in this diff:\n\n\n401c400\n<       $(SAGE_SPKG) $(F2C) 2>&1\n---\n>       $(SAGE_SPKG) $(INST)/$(F2C) 2>&1\n413c412\n<       $(SAGE_SPKG) $(LAPACK) 2>&1\n---\n>       $(SAGE_SPKG) $(INST)/$(LAPACK) 2>&1\n416c415\n<       $(SAGE_SPKG) $(BLAS) 2>&1\n---\n>       $(SAGE_SPKG) $(INST)/$(BLAS) 2>&1\n\n\n\n\nAlso in deps there are references to   TWISTEDWEB2  but that doesn't\nseem to exist anymore.\n\n\nI do not write access to the code. I hope someone who does will take\nthis\nand do right thing with it.\n\n************************************************\ncarlhansen1234\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9274\n\n",
    "created_at": "2010-06-19T17:01:07Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "do some cleanup of the deps file, as suggested by Carl Hansen",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9274",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber

CC:  drkirkby @jhpalmieri


```

Here is an excerpt from "deps" , the makefile in spkg/standard

$(INST)/$(FORTRAN):
       $(SAGE_SPKG) $(FORTRAN) 2>&1

$(INST)/$(F2C): $(INST)/$(FORTRAN)
       $(SAGE_SPKG) $(INST)/$(F2C) 2>&1
                    ^^^^^^^ --------------------Notice that this is
wrong.
                                              the INST is not needed
and is wrong.
$(INST)/$(PIL): $(INST)/$(PYTHON)
       $(SAGE_SPKG) $(PIL) 2>&1


The only reason it works is that the script that reads it cleans it up
with
"basename".

But that's imperfect.


There are 3 instances, shown in this diff:


401c400
<       $(SAGE_SPKG) $(F2C) 2>&1
---
>       $(SAGE_SPKG) $(INST)/$(F2C) 2>&1
413c412
<       $(SAGE_SPKG) $(LAPACK) 2>&1
---
>       $(SAGE_SPKG) $(INST)/$(LAPACK) 2>&1
416c415
<       $(SAGE_SPKG) $(BLAS) 2>&1
---
>       $(SAGE_SPKG) $(INST)/$(BLAS) 2>&1




Also in deps there are references to   TWISTEDWEB2  but that doesn't
seem to exist anymore.


I do not write access to the code. I hope someone who does will take
this
and do right thing with it.

************************************************
carlhansen1234
```


Issue created by migration from https://trac.sagemath.org/ticket/9274





---

archive/issue_comments_087206.json:
```json
{
    "body": "Please see [comment:ticket:8306:73 John Palmieri's comment] (or [attachment:ticket:8306:deps-deps-new.diff this diff]) at #8306 for some other suggestions.",
    "created_at": "2010-06-26T08:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87206",
    "user": "https://github.com/qed777"
}
```

Please see [comment:ticket:8306:73 John Palmieri's comment] (or [attachment:ticket:8306:deps-deps-new.diff this diff]) at #8306 for some other suggestions.



---

archive/issue_comments_087207.json:
```json
{
    "body": "Updated `spkg/install/deps` based on 4.5.alpha1.",
    "created_at": "2010-06-30T02:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87207",
    "user": "https://github.com/qed777"
}
```

Updated `spkg/install/deps` based on 4.5.alpha1.



---

archive/issue_comments_087208.json:
```json
{
    "body": "Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9274/deps.diff) by @qed777 created at 2010-06-30 02:43:53\n\nDiff of `spkg/install/deps` vs. 4.5.alpha1.",
    "created_at": "2010-06-30T02:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87208",
    "user": "https://github.com/qed777"
}
```

Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9274/deps.diff) by @qed777 created at 2010-06-30 02:43:53

Diff of `spkg/install/deps` vs. 4.5.alpha1.



---

archive/issue_comments_087209.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-06-30T03:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87209",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to minor.



---

archive/issue_comments_087210.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-30T03:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87210",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_087211.json:
```json
{
    "body": "The attached `deps` incorporates suggestions from [Carl Hansen](http://groups.google.com/group/sage-devel/browse_thread/thread/d15b668609983181/268094db15092f85?#268094db15092f85), [David Kirkby](http://groups.google.com/group/sage-devel/browse_thread/thread/7763c990fdc1d5ac#), and [comment:ticket:8306:73 John Palmieri].\n\nMain changes:\n\n* Remove unnecessary `$(INST)/`'s.\n* Make all non-`$(BASE)` packages depend explicitly on `$(BASE)`.\n* Make the target `all` depend explicitly on all standard packages.\n\nWith `SAGE_PARALLEL_SPKG_BUILD=\"yes\"`: The long tests pass on bsd.math.  They also pass on sage.math, if after building Sage, I reinstall Maxima via `sage -f`.  I don't know why, but I'll keep testing.",
    "created_at": "2010-06-30T03:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87211",
    "user": "https://github.com/qed777"
}
```

The attached `deps` incorporates suggestions from [Carl Hansen](http://groups.google.com/group/sage-devel/browse_thread/thread/d15b668609983181/268094db15092f85?#268094db15092f85), [David Kirkby](http://groups.google.com/group/sage-devel/browse_thread/thread/7763c990fdc1d5ac#), and [comment:ticket:8306:73 John Palmieri].

Main changes:

* Remove unnecessary `$(INST)/`'s.
* Make all non-`$(BASE)` packages depend explicitly on `$(BASE)`.
* Make the target `all` depend explicitly on all standard packages.

With `SAGE_PARALLEL_SPKG_BUILD="yes"`: The long tests pass on bsd.math.  They also pass on sage.math, if after building Sage, I reinstall Maxima via `sage -f`.  I don't know why, but I'll keep testing.



---

archive/issue_events_022846.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-06-30T03:14:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9274#event-22846"
}
```



---

archive/issue_comments_087212.json:
```json
{
    "body": "#9351, which has positive review, makes Sagetex dependant on both gap and Sage, since you need a working Sage in order that Sagetex can be tested with SAGE_CHECK=yes. So the 'deps' file attached to this ticket would need that dependency updating.\n\nI've printed this on paper and looked though it fairly carefully, and can't see anything wrong with it. Everything looks logical to me. On a few occasions where things only depended on 'BASE', but I was slightly suspicious they might have other dependencies, I checked the packages more carefully by inspection of their contents. I can't see anything wrong. \n\nI've used this 'deps' file to build Sage on my OpenSolaris machine, and found the 'deps' file appears OK, though since neither R or Maxima build on OpenSolaris, I'm unable to test this 'deps' file fully on OpenSolaris. Since you have a specific issue with Maxima, I can't provide convincing evidence this is OK. But it looks OK to me. \n\nI would never be totally surprised by any failures of builds on the *.math.washington.edu network if an NFS-shared directory is used for building Sage - which includes the home directories. Most of the hard disks are attached to a server called 'disk.math.washington.edu' which is running OpenSolaris. But the ZFS intent Log (ZIL) has been disabled to increase NFS speed. This means that if you write something to disk, then try to read it, there is no guarantee it can be read. Hence (on t2), the system log shows things like\n\n\n```\nJun 30 19:06:03 t2 nfs: [ID 236337 kern.info] NOTICE: [NFS4][Server: disk][Mntpt: /home]NFS op OP_SETATTR got error NFS4ERR_DELAY causing recovery action NR_DELAY.\nJun 30 19:06:03 t2 last message repeated 2 times\nJun 30 19:06:03 t2 nfs: [ID 236337 kern.info] NOTICE: [NFS4][Server: disk][Mntpt: /home]NFS op OP_CLOSE got error NFS4ERR_STALE causing recovery action NR_STALE.\nJun 30 19:06:03 t2 nfs: [ID 286389 kern.info] NOTICE: [NFS4][Server: disk][Mntpt: /home]File configure (rnode_pt: 3000cdca018) was closed due to NFS recovery error on server disk(failed to recover from NFS4ERR_STALE NFS4ERR_STALE)\nJun 30 19:06:03 t2 nfs: [ID 941083 kern.info] NOTICE: NFS4 FACT SHEET: \nJun 30 19:06:03 t2  Action: NR_STALE \nJun 30 19:06:03 t2  NFS4 error: NFS4ERR_STALE   \n```\n\n\nSo if you get strange behavior, I would try it on a scratch area, with local storage, since I would not 100% trust the way the ZFS pools are configured.",
    "created_at": "2010-07-03T19:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87212",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

#9351, which has positive review, makes Sagetex dependant on both gap and Sage, since you need a working Sage in order that Sagetex can be tested with SAGE_CHECK=yes. So the 'deps' file attached to this ticket would need that dependency updating.

I've printed this on paper and looked though it fairly carefully, and can't see anything wrong with it. Everything looks logical to me. On a few occasions where things only depended on 'BASE', but I was slightly suspicious they might have other dependencies, I checked the packages more carefully by inspection of their contents. I can't see anything wrong. 

I've used this 'deps' file to build Sage on my OpenSolaris machine, and found the 'deps' file appears OK, though since neither R or Maxima build on OpenSolaris, I'm unable to test this 'deps' file fully on OpenSolaris. Since you have a specific issue with Maxima, I can't provide convincing evidence this is OK. But it looks OK to me. 

I would never be totally surprised by any failures of builds on the *.math.washington.edu network if an NFS-shared directory is used for building Sage - which includes the home directories. Most of the hard disks are attached to a server called 'disk.math.washington.edu' which is running OpenSolaris. But the ZFS intent Log (ZIL) has been disabled to increase NFS speed. This means that if you write something to disk, then try to read it, there is no guarantee it can be read. Hence (on t2), the system log shows things like


```
Jun 30 19:06:03 t2 nfs: [ID 236337 kern.info] NOTICE: [NFS4][Server: disk][Mntpt: /home]NFS op OP_SETATTR got error NFS4ERR_DELAY causing recovery action NR_DELAY.
Jun 30 19:06:03 t2 last message repeated 2 times
Jun 30 19:06:03 t2 nfs: [ID 236337 kern.info] NOTICE: [NFS4][Server: disk][Mntpt: /home]NFS op OP_CLOSE got error NFS4ERR_STALE causing recovery action NR_STALE.
Jun 30 19:06:03 t2 nfs: [ID 286389 kern.info] NOTICE: [NFS4][Server: disk][Mntpt: /home]File configure (rnode_pt: 3000cdca018) was closed due to NFS recovery error on server disk(failed to recover from NFS4ERR_STALE NFS4ERR_STALE)
Jun 30 19:06:03 t2 nfs: [ID 941083 kern.info] NOTICE: NFS4 FACT SHEET: 
Jun 30 19:06:03 t2  Action: NR_STALE 
Jun 30 19:06:03 t2  NFS4 error: NFS4ERR_STALE   
```


So if you get strange behavior, I would try it on a scratch area, with local storage, since I would not 100% trust the way the ZFS pools are configured.



---

archive/issue_comments_087213.json:
```json
{
    "body": "I really want sage-4.5 to be a better release, so I'm adding this to the blockers. Just like the issue that #9431 is exposing, this is too egregous to delay.\n\nThe GLPK alpha release is nearly ready, and will include #9412 specifically so that this can be rebased on top and merged into the alpha release following that one.\n\nWhat work is left for this to be ready, other than waiting for #9412?",
    "created_at": "2010-07-05T21:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87213",
    "user": "https://github.com/rlmill"
}
```

I really want sage-4.5 to be a better release, so I'm adding this to the blockers. Just like the issue that #9431 is exposing, this is too egregous to delay.

The GLPK alpha release is nearly ready, and will include #9412 specifically so that this can be rebased on top and merged into the alpha release following that one.

What work is left for this to be ready, other than waiting for #9412?



---

archive/issue_comments_087214.json:
```json
{
    "body": "Changing priority from minor to blocker.",
    "created_at": "2010-07-05T21:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87214",
    "user": "https://github.com/rlmill"
}
```

Changing priority from minor to blocker.



---

archive/issue_events_022847.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-05T21:16:05Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9274#event-22847"
}
```



---

archive/issue_events_022848.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-05T21:16:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9274#event-22848"
}
```



---

archive/issue_comments_087215.json:
```json
{
    "body": "See the comment about Maxima needing to be reinstalled above. \n\nI don't know if that is supposed to be related to what changes are on this ticket or not. At first, I interpreted the reasons this ticket was needing work was because of this Maxima problem. Perhaps it was put to 'needs work' for some other reason. \n\n\nDave",
    "created_at": "2010-07-05T21:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87215",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

See the comment about Maxima needing to be reinstalled above. 

I don't know if that is supposed to be related to what changes are on this ticket or not. At first, I interpreted the reasons this ticket was needing work was because of this Maxima problem. Perhaps it was put to 'needs work' for some other reason. 


Dave



---

archive/issue_comments_087216.json:
```json
{
    "body": "Is this as good a place as any to work out dependencies for glpk?  (See [http://trac.sagemath.org/sage_trac/ticket/9312#comment:24](http://trac.sagemath.org/sage_trac/ticket/9312#comment:24).)",
    "created_at": "2010-07-06T00:09:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87216",
    "user": "https://github.com/jhpalmieri"
}
```

Is this as good a place as any to work out dependencies for glpk?  (See [http://trac.sagemath.org/sage_trac/ticket/9312#comment:24](http://trac.sagemath.org/sage_trac/ticket/9312#comment:24).)



---

archive/issue_comments_087217.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> Is this as good a place as any to work out dependencies for glpk?\n\nAs you're probably aware, this made it into sage-4.5.alpha3:\n\nhttp://sage.math.washington.edu/home/rlmill/release/sage-4.5.alpha3.tar\n\nCan the deps file here and the patch be rebased on top of alpha3? I promise this will be the last time.",
    "created_at": "2010-07-06T03:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87217",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:7 jhpalmieri]:
> Is this as good a place as any to work out dependencies for glpk?

As you're probably aware, this made it into sage-4.5.alpha3:

http://sage.math.washington.edu/home/rlmill/release/sage-4.5.alpha3.tar

Can the deps file here and the patch be rebased on top of alpha3? I promise this will be the last time.



---

archive/issue_comments_087218.json:
```json
{
    "body": "rebased against 4.5.alpha3",
    "created_at": "2010-07-06T03:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87218",
    "user": "https://github.com/jhpalmieri"
}
```

rebased against 4.5.alpha3



---

archive/issue_comments_087219.json:
```json
{
    "body": "Attachment [deps-new.diff](tarball://root/attachments/some-uuid/ticket9274/deps-new.diff) by @jhpalmieri created at 2010-07-06 03:44:10",
    "created_at": "2010-07-06T03:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87219",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [deps-new.diff](tarball://root/attachments/some-uuid/ticket9274/deps-new.diff) by @jhpalmieri created at 2010-07-06 03:44:10



---

archive/issue_comments_087220.json:
```json
{
    "body": "Here are rebased versions, and they also include making cython a prerequisite for glpk.",
    "created_at": "2010-07-06T03:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87220",
    "user": "https://github.com/jhpalmieri"
}
```

Here are rebased versions, and they also include making cython a prerequisite for glpk.



---

archive/issue_comments_087221.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-06T03:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87221",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087222.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-06T03:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87222",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022849.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-06T03:54:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9274#event-22849"
}
```



---

archive/issue_comments_087223.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-06T03:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87223",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_087224.json:
```json
{
    "body": "Make sure to merge \"deps-new\", not \"deps\".",
    "created_at": "2010-07-06T04:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87224",
    "user": "https://github.com/jhpalmieri"
}
```

Make sure to merge "deps-new", not "deps".



---

archive/issue_comments_087225.json:
```json
{
    "body": "Replying to [comment:13 jhpalmieri]:\n> Make sure to merge \"deps-new\", not \"deps\".\n> \n\nYep, that's what I merged. Thanks for the extra care.",
    "created_at": "2010-07-06T05:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87225",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:13 jhpalmieri]:
> Make sure to merge "deps-new", not "deps".
> 

Yep, that's what I merged. Thanks for the extra care.



---

archive/issue_comments_087226.json:
```json
{
    "body": "Hmmmm :-/\n\nI do not think it can hurt, though why should GLPK depend on Cython ? In the last version (the version embedded in alpha3), there is no setup.py file, no Cython code at all... Actually, there are only bash scripts and GLPK's own sources !!!\n\nSorry for not having brought this up earlier (I just woke up) :-/\n\nNathann",
    "created_at": "2010-07-06T06:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87226",
    "user": "https://github.com/nathanncohen"
}
```

Hmmmm :-/

I do not think it can hurt, though why should GLPK depend on Cython ? In the last version (the version embedded in alpha3), there is no setup.py file, no Cython code at all... Actually, there are only bash scripts and GLPK's own sources !!!

Sorry for not having brought this up earlier (I just woke up) :-/

Nathann



---

archive/issue_comments_087227.json:
```json
{
    "body": "Replying to [comment:15 ncohen]:\n> Hmmmm :-/\n> \n> I do not think it can hurt, though why should GLPK depend on Cython ? In the last version (the version embedded in alpha3), there is no setup.py file, no Cython code at all... Actually, there are only bash scripts and GLPK's own sources !!!\n> \n> Sorry for not having brought this up earlier (I just woke up) :-/\n> \n> Nathann\n\nAn interesting point. It can hurt for two reasons\n\n* It will slow parallel builds unnecessarily, as GLPK has to wait until Cython has built. That's not a major issue, as GLPK takes very little time to build. \n* The real reason people got a failure might be something else. \n\nThat's worth investigating.",
    "created_at": "2010-07-06T06:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87227",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:15 ncohen]:
> Hmmmm :-/
> 
> I do not think it can hurt, though why should GLPK depend on Cython ? In the last version (the version embedded in alpha3), there is no setup.py file, no Cython code at all... Actually, there are only bash scripts and GLPK's own sources !!!
> 
> Sorry for not having brought this up earlier (I just woke up) :-/
> 
> Nathann

An interesting point. It can hurt for two reasons

* It will slow parallel builds unnecessarily, as GLPK has to wait until Cython has built. That's not a major issue, as GLPK takes very little time to build. 
* The real reason people got a failure might be something else. 

That's worth investigating.



---

archive/issue_comments_087228.json:
```json
{
    "body": "I apologize for my late reply.\n\n* Off-topic, I admit:  Robert, what do you think about making new releases available in `/home/release` on `sage.math`?\n* I've been running test builds under `/scratch` on sage.math.\n* For what it's worth, I later sometimes experienced the same Maxima reinstallation problem when building an *unmodified* 4.5.alpha1 on sage.math --- with 4, 6, or 12 parallel jobs.\n* For the record, here are two errors representative of those fixed by reinstalling Maxima:\n\n```sh\n./sage -c 'print QQ[2^(1/3)]'\nTraceback (most recent call last):\n  File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/bin/sage-eval\", line 15, in <module>\n    eval(compile(s,'<cmdline>','exec'))\n  File \"<cmdline>\", line 1, in <module>\n  File \"ring.pyx\", line 205, in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2550)\n  File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py\", line 343, in PolynomialRing\n    R = _single_variate(base_ring, name, sparse, implementation)\n  File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py\", line 395, in _single_variate\n    name = normalize_names(1, name)\n  File \"parent_gens.pyx\", line 204, in sage.structure.parent_gens.normalize_names (sage/structure/parent_gens.c:2093)\n  File \"parent_gens.pyx\", line 145, in sage.structure.parent_gens._certify_names (sage/structure/parent_gens.c:1650)\nValueError: variable names must be alphanumeric, but one is '2^(1/3)' which is not.\n```\n\n  and\n\n```sh\n./sage -c \"var('x'); print solve(x, x)\"\nTraceback (most recent call last):\n  File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/bin/sage-eval\", line 15, in <module>\n    eval(compile(s,'<cmdline>','exec'))\n  File \"<cmdline>\", line 1, in <module>\n  File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/lib/python2.6/site-packages/sage/symbolic/relation.py\", line 619, in solve\n    ans = f.solve(*args,**kwds)\n  File \"expression.pyx\", line 6735, in sage.symbolic.expression.Expression.solve (sage/symbolic/expression.cpp:25171)\n  File \"expression.pyx\", line 433, in sage.symbolic.expression.Expression._maxima_ (sage/symbolic/expression.cpp:3382)\n  File \"sage_object.pyx\", line 386, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3501)\n  File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/lib/python2.6/site-packages/sage/interfaces/expect.py\", line 1032, in __call__\n    return cls(self, x, name=name)\n  File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/lib/python2.6/site-packages/sage/interfaces/expect.py\", line 1451, in __init__\n    raise TypeError, x\nTypeError: error evaluating \"load(to_poly_solver)\":\nError executing code in Maxima\nCODE:\n        load(to_poly_solver);\nMaxima ERROR:\n\nCould not find `to_poly_solver' using paths in file_search_maxima,file_search_lisp.\n -- an error. To debug this try: debugmode(true);\n```\n\n* Curiously:  Moving the build tree (renaming `SAGE_ROOT`) also fixes the errors, possibly because this forces `sage-location` to run.",
    "created_at": "2010-07-06T07:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9274#issuecomment-87228",
    "user": "https://github.com/qed777"
}
```

I apologize for my late reply.

* Off-topic, I admit:  Robert, what do you think about making new releases available in `/home/release` on `sage.math`?
* I've been running test builds under `/scratch` on sage.math.
* For what it's worth, I later sometimes experienced the same Maxima reinstallation problem when building an *unmodified* 4.5.alpha1 on sage.math --- with 4, 6, or 12 parallel jobs.
* For the record, here are two errors representative of those fixed by reinstalling Maxima:

```sh
./sage -c 'print QQ[2^(1/3)]'
Traceback (most recent call last):
  File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/bin/sage-eval", line 15, in <module>
    eval(compile(s,'<cmdline>','exec'))
  File "<cmdline>", line 1, in <module>
  File "ring.pyx", line 205, in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2550)
  File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 343, in PolynomialRing
    R = _single_variate(base_ring, name, sparse, implementation)
  File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 395, in _single_variate
    name = normalize_names(1, name)
  File "parent_gens.pyx", line 204, in sage.structure.parent_gens.normalize_names (sage/structure/parent_gens.c:2093)
  File "parent_gens.pyx", line 145, in sage.structure.parent_gens._certify_names (sage/structure/parent_gens.c:1650)
ValueError: variable names must be alphanumeric, but one is '2^(1/3)' which is not.
```

  and

```sh
./sage -c "var('x'); print solve(x, x)"
Traceback (most recent call last):
  File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/bin/sage-eval", line 15, in <module>
    eval(compile(s,'<cmdline>','exec'))
  File "<cmdline>", line 1, in <module>
  File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/lib/python2.6/site-packages/sage/symbolic/relation.py", line 619, in solve
    ans = f.solve(*args,**kwds)
  File "expression.pyx", line 6735, in sage.symbolic.expression.Expression.solve (sage/symbolic/expression.cpp:25171)
  File "expression.pyx", line 433, in sage.symbolic.expression.Expression._maxima_ (sage/symbolic/expression.cpp:3382)
  File "sage_object.pyx", line 386, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3501)
  File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/lib/python2.6/site-packages/sage/interfaces/expect.py", line 1032, in __call__
    return cls(self, x, name=name)
  File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha1-j12-par/local/lib/python2.6/site-packages/sage/interfaces/expect.py", line 1451, in __init__
    raise TypeError, x
TypeError: error evaluating "load(to_poly_solver)":
Error executing code in Maxima
CODE:
        load(to_poly_solver);
Maxima ERROR:

Could not find `to_poly_solver' using paths in file_search_maxima,file_search_lisp.
 -- an error. To debug this try: debugmode(true);
```

* Curiously:  Moving the build tree (renaming `SAGE_ROOT`) also fixes the errors, possibly because this forces `sage-location` to run.
