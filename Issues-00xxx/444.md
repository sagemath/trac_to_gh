# Issue 444: [with patch, with positive review] solve the rubik's cube fast!

archive/issues_000444.json:
```json
{
    "body": "Assignee: @robertwb\n\nHi:\n\nTwo Rubik's cube programs have just been posted to\nhttp://sage.math.washington.edu/home/wdj/rubik/\nBoth one is GPL's (Michael Reid's) and the other is\nunder the MIT license (Dik Winter's). These programs\nhave been around for some time but have never\nbeen licensed until recently (and I thank both the\nauthors for kindly replying to my emails and agreeing\nto an open source license). The tarballs you will find there\nare identical to the author's version except that I have\nadded a license.txt following their email directions.\nNow that the semester has started, I lack the time to\ndo anything but am emailing the list in case anyone\nis interested and has the time to create Python\nwrappers for one (or both) of them. SAGE\ncurrently has a Rubik's cube solver which uses GAP\nand is quite slow and far from optimal. Maybe one of these\ncould be used instead one day?\n --- David Joyner\n\nIssue created by migration from https://trac.sagemath.org/ticket/444\n\n",
    "closed_at": "2007-12-15T11:23:27Z",
    "created_at": "2007-08-18T20:32:09Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch, with positive review] solve the rubik's cube fast!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/444",
    "user": "https://github.com/williamstein"
}
```
Assignee: @robertwb

Hi:

Two Rubik's cube programs have just been posted to
http://sage.math.washington.edu/home/wdj/rubik/
Both one is GPL's (Michael Reid's) and the other is
under the MIT license (Dik Winter's). These programs
have been around for some time but have never
been licensed until recently (and I thank both the
authors for kindly replying to my emails and agreeing
to an open source license). The tarballs you will find there
are identical to the author's version except that I have
added a license.txt following their email directions.
Now that the semester has started, I lack the time to
do anything but am emailing the list in case anyone
is interested and has the time to create Python
wrappers for one (or both) of them. SAGE
currently has a Rubik's cube solver which uses GAP
and is quite slow and far from optimal. Maybe one of these
could be used instead one day?
 --- David Joyner

Issue created by migration from https://trac.sagemath.org/ticket/444





---

archive/issue_events_001093.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-28T12:01:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1093"
}
```



---

archive/issue_comments_002208.json:
```json
{
    "body": "Here's an spkg of solvers, needs to be tested on lots of different computers. \n\nhttp://sage.math.washington.edu/home/robertwb/spkgs/",
    "created_at": "2007-09-12T09:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2208",
    "user": "https://github.com/robertwb"
}
```

Here's an spkg of solvers, needs to be tested on lots of different computers. 

http://sage.math.washington.edu/home/robertwb/spkgs/



---

archive/issue_comments_002209.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-12T09:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2209",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002210.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-09-12T09:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2210",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_002211.json:
```json
{
    "body": "Attachment [cube-solver.hg](tarball://root/attachments/some-uuid/ticket444/cube-solver.hg) by @robertwb created at 2007-09-12 10:00:10",
    "created_at": "2007-09-12T10:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2211",
    "user": "https://github.com/robertwb"
}
```

Attachment [cube-solver.hg](tarball://root/attachments/some-uuid/ticket444/cube-solver.hg) by @robertwb created at 2007-09-12 10:00:10



---

archive/issue_events_001094.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-19T18:33:44Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1094"
}
```



---

archive/issue_events_001095.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-19T18:33:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1095"
}
```



---

archive/issue_comments_002212.json:
```json
{
    "body": "Is this in or not? What should we do with this patch?\n\nCheers,\n\nMichael",
    "created_at": "2007-10-19T18:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2212",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Is this in or not? What should we do with this patch?

Cheers,

Michael



---

archive/issue_events_001096.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T19:07:23Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1096"
}
```



---

archive/issue_events_001097.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T19:07:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1097"
}
```



---

archive/issue_events_001098.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-20T19:09:44Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1098"
}
```



---

archive/issue_events_001099.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-20T19:09:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1099"
}
```



---

archive/issue_events_001100.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-25T01:08:10Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1100"
}
```



---

archive/issue_events_001101.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-25T01:08:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1101"
}
```



---

archive/issue_events_001102.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2007-10-26T04:26:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1102"
}
```



---

archive/issue_events_001103.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2007-10-26T04:26:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1103"
}
```



---

archive/issue_comments_002213.json:
```json
{
    "body": "I tried the spkg and the associated patch; they worked fine (on 32-bit x86 Linux; Debian testing).  However, I don't think the solvers belong as a standard spkg (adding a third of a megabyte to every Sage download); I think they should be optional.  And if the spkg is optional, then the patch has some problems: it turns a working-by-default (if slow) method into a method which raises an exception when the spkg is not installed.\n\nI think the patch should be modified to either leave the original GAP algorithm as the default, or to change the default but automatically fall back to GAP if the solvers are not installed.\n\nAlso, there should be at least one doctest for each solver.\n\nI'm removing \"[with patch]\" from the summary for now; anybody who supplies a revised patch should reinstate it (or, I guess, you could reinstate it if you want to argue that the solvers should be a standard Sage package).",
    "created_at": "2007-10-26T04:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2213",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I tried the spkg and the associated patch; they worked fine (on 32-bit x86 Linux; Debian testing).  However, I don't think the solvers belong as a standard spkg (adding a third of a megabyte to every Sage download); I think they should be optional.  And if the spkg is optional, then the patch has some problems: it turns a working-by-default (if slow) method into a method which raises an exception when the spkg is not installed.

I think the patch should be modified to either leave the original GAP algorithm as the default, or to change the default but automatically fall back to GAP if the solvers are not installed.

Also, there should be at least one doctest for each solver.

I'm removing "[with patch]" from the summary for now; anybody who supplies a revised patch should reinstate it (or, I guess, you could reinstate it if you want to argue that the solvers should be a standard Sage package).



---

archive/issue_comments_002214.json:
```json
{
    "body": "Attachment [rubiks-doctest.patch](tarball://root/attachments/some-uuid/ticket444/rubiks-doctest.patch) by @robertwb created at 2007-11-27 11:28:48",
    "created_at": "2007-11-27T11:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2214",
    "user": "https://github.com/robertwb"
}
```

Attachment [rubiks-doctest.patch](tarball://root/attachments/some-uuid/ticket444/rubiks-doctest.patch) by @robertwb created at 2007-11-27 11:28:48



---

archive/issue_events_001104.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2007-11-27T11:39:08Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1104"
}
```



---

archive/issue_events_001105.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2007-11-27T11:39:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1105"
}
```



---

archive/issue_comments_002215.json:
```json
{
    "body": "In light of David Joyner's re-release of his book on Solving the Rubiks cube (using Sage) I think a fast solver is important to include even if just for marketing purposes. The GAP implementation isn't just a little bit slow, it's almost unusable (especially compared to nearly instantaneous solutions provided by the other packages). \n\nAlso I think 370K is really a quite small, 0.2% of the size of Sage itself, compared to the provided functionality. \n\nI did, however, add doctests for the solvers.",
    "created_at": "2007-11-27T11:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2215",
    "user": "https://github.com/robertwb"
}
```

In light of David Joyner's re-release of his book on Solving the Rubiks cube (using Sage) I think a fast solver is important to include even if just for marketing purposes. The GAP implementation isn't just a little bit slow, it's almost unusable (especially compared to nearly instantaneous solutions provided by the other packages). 

Also I think 370K is really a quite small, 0.2% of the size of Sage itself, compared to the provided functionality. 

I did, however, add doctests for the solvers.



---

archive/issue_comments_002216.json:
```json
{
    "body": "Attachment [cubegroup-cleanup1.patch](tarball://root/attachments/some-uuid/ticket444/cubegroup-cleanup1.patch) by @robertwb created at 2007-11-28 20:04:16",
    "created_at": "2007-11-28T20:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2216",
    "user": "https://github.com/robertwb"
}
```

Attachment [cubegroup-cleanup1.patch](tarball://root/attachments/some-uuid/ticket444/cubegroup-cleanup1.patch) by @robertwb created at 2007-11-28 20:04:16



---

archive/issue_comments_002217.json:
```json
{
    "body": "Attachment [cubegroup-cleanup2.patch](tarball://root/attachments/some-uuid/ticket444/cubegroup-cleanup2.patch) by @robertwb created at 2007-11-28 20:06:12",
    "created_at": "2007-11-28T20:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2217",
    "user": "https://github.com/robertwb"
}
```

Attachment [cubegroup-cleanup2.patch](tarball://root/attachments/some-uuid/ticket444/cubegroup-cleanup2.patch) by @robertwb created at 2007-11-28 20:06:12



---

archive/issue_events_001106.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-04T14:11:10Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1106"
}
```



---

archive/issue_events_001107.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-04T14:11:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1107"
}
```



---

archive/issue_comments_002218.json:
```json
{
    "body": "OK, assuming the rubik solvers are to become a standard part of Sage, then this patch set looks good to me.\n\nTo install:\nadd http://sage.math.washington.edu/home/robertwb/spkgs/rubiks-20070912.spkg as a standard spkg,\nthen apply all 4 attachments to this bug (one bundle, and 3 patches) in order.",
    "created_at": "2007-12-15T05:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2218",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

OK, assuming the rubik solvers are to become a standard part of Sage, then this patch set looks good to me.

To install:
add http://sage.math.washington.edu/home/robertwb/spkgs/rubiks-20070912.spkg as a standard spkg,
then apply all 4 attachments to this bug (one bundle, and 3 patches) in order.



---

archive/issue_events_001108.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T11:23:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/444#event-1108"
}
```



---

archive/issue_comments_002219.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T11:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2219",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002220.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T11:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/444#issuecomment-2220",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.
