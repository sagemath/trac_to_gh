# Issue 9592: Upgrade lcalc to pari 2.4.3

archive/issues_009592.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @JohnCremona\n\nAfter upgrading PARI/GP to version 2.4.3 (#9343), lcalc no longer compiles properly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9592\n\n",
    "created_at": "2010-07-24T11:57:12Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Upgrade lcalc to pari 2.4.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9592",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: tbd

CC:  @JohnCremona

After upgrading PARI/GP to version 2.4.3 (#9343), lcalc no longer compiles properly.

Issue created by migration from https://trac.sagemath.org/ticket/9592





---

archive/issue_comments_092624.json:
```json
{
    "body": "Attachment [lcalc-newpari.patch](tarball://root/attachments/some-uuid/ticket9592/lcalc-newpari.patch) by @jdemeyer created at 2010-07-24 13:07:50",
    "created_at": "2010-07-24T13:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92624",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [lcalc-newpari.patch](tarball://root/attachments/some-uuid/ticket9592/lcalc-newpari.patch) by @jdemeyer created at 2010-07-24 13:07:50



---

archive/issue_comments_092625.json:
```json
{
    "body": "Changing assignee from tbd to @jdemeyer.",
    "created_at": "2010-07-24T13:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92625",
    "user": "https://github.com/jdemeyer"
}
```

Changing assignee from tbd to @jdemeyer.



---

archive/issue_comments_092626.json:
```json
{
    "body": "New version which works with PARI 2.4.3: [http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p1.spkg](http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p1.spkg)\n\nI have also notified the upstream contact Michael Rubinstein and sent him the patch lcalc-newpari.patch",
    "created_at": "2010-07-24T13:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92626",
    "user": "https://github.com/jdemeyer"
}
```

New version which works with PARI 2.4.3: [http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p1.spkg](http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p1.spkg)

I have also notified the upstream contact Michael Rubinstein and sent him the patch lcalc-newpari.patch



---

archive/issue_events_023891.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-07-29T14:46:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9592#event-23891"
}
```



---

archive/issue_comments_092627.json:
```json
{
    "body": "The patch level for the new spkg should be 2, since we used p1 for #9665.  This should fix the \"already installed\" problem reported by John Cremona in [comment:ticket:9343:180 comment 180] at #9343.",
    "created_at": "2010-08-13T11:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92627",
    "user": "https://github.com/qed777"
}
```

The patch level for the new spkg should be 2, since we used p1 for #9665.  This should fix the "already installed" problem reported by John Cremona in [comment:ticket:9343:180 comment 180] at #9343.



---

archive/issue_comments_092628.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> The patch level for the new spkg should be 2, since we used p1 for #9665.  This should fix the \"already installed\" problem reported by John Cremona in [comment:ticket:9343:180 comment 180] at #9343.\n\n\nJust noticed that, too. :)\n\nThere are also post-merge comments at #9665, I don't know if they should be included here or if there's even a new ticket for these.",
    "created_at": "2010-08-13T11:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92628",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:5 mpatel]:
> The patch level for the new spkg should be 2, since we used p1 for #9665.  This should fix the "already installed" problem reported by John Cremona in [comment:ticket:9343:180 comment 180] at #9343.


Just noticed that, too. :)

There are also post-merge comments at #9665, I don't know if they should be included here or if there's even a new ticket for these.



---

archive/issue_comments_092629.json:
```json
{
    "body": "Jeroen, could you describe in more detail which failure(s) this ticket is intended to fix (including Sage version, operating system, processor etc.)?\n\nJohn Cremona has successfully installed and tested #9343 (unintentionally) **without** this new spkg, and I've also successfully installed the other to spkgs and applied the patches from #9343 on top of Sage 4.5.3.alpha0 + #9475 and #9717 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4).\n\nOf course lcalc wasn't (re)built in the above tests. (I'll try that later, currently running `ptestlong` without the lcalc package from here.)",
    "created_at": "2010-08-13T15:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92629",
    "user": "https://github.com/nexttime"
}
```

Jeroen, could you describe in more detail which failure(s) this ticket is intended to fix (including Sage version, operating system, processor etc.)?

John Cremona has successfully installed and tested #9343 (unintentionally) **without** this new spkg, and I've also successfully installed the other to spkgs and applied the patches from #9343 on top of Sage 4.5.3.alpha0 + #9475 and #9717 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4).

Of course lcalc wasn't (re)built in the above tests. (I'll try that later, currently running `ptestlong` without the lcalc package from here.)



---

archive/issue_comments_092630.json:
```json
{
    "body": "Just for the record: `SPKG.txt` currently lacks a *Dependencies* section, the package has no `spkg-check`, and `spkg-install` uses `make`, not `$MAKE`...",
    "created_at": "2010-08-13T15:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92630",
    "user": "https://github.com/nexttime"
}
```

Just for the record: `SPKG.txt` currently lacks a *Dependencies* section, the package has no `spkg-check`, and `spkg-install` uses `make`, not `$MAKE`...



---

archive/issue_comments_092631.json:
```json
{
    "body": "In addition, it contains at least two or three files that should be deleted: some `*.bak` file, a `*.swap.crap` file and some static library (`*.a`) I think we don't need (correct me if I'm wrong here).\n\n(In case Jeroen's patch here is now obsolete due to a meanwhile newer PARI version at #9343, which John Cremona is currently investigating, we could recycle this ticket to address the above mentioned issues.)",
    "created_at": "2010-08-13T16:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92631",
    "user": "https://github.com/nexttime"
}
```

In addition, it contains at least two or three files that should be deleted: some `*.bak` file, a `*.swap.crap` file and some static library (`*.a`) I think we don't need (correct me if I'm wrong here).

(In case Jeroen's patch here is now obsolete due to a meanwhile newer PARI version at #9343, which John Cremona is currently investigating, we could recycle this ticket to address the above mentioned issues.)



---

archive/issue_comments_092632.json:
```json
{
    "body": "Updated spkg: [http://www.warwick.ac.uk/staff/J.E.Cremona/lcalc-20100428-1.23.p2.spkg](http://www.warwick.ac.uk/staff/J.E.Cremona/lcalc-20100428-1.23.p2.spkg)\n\n(This version is based on lcalc-20100428-1.23.p1.spkg as merged in 4.5.2)\n\nI made this before seeing the recent comments here.  Feel free to add the Dependencies section etc  -- I will not have time to do that for at least a day.",
    "created_at": "2010-08-13T16:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92632",
    "user": "https://github.com/JohnCremona"
}
```

Updated spkg: [http://www.warwick.ac.uk/staff/J.E.Cremona/lcalc-20100428-1.23.p2.spkg](http://www.warwick.ac.uk/staff/J.E.Cremona/lcalc-20100428-1.23.p2.spkg)

(This version is based on lcalc-20100428-1.23.p1.spkg as merged in 4.5.2)

I made this before seeing the recent comments here.  Feel free to add the Dependencies section etc  -- I will not have time to do that for at least a day.



---

archive/issue_comments_092633.json:
```json
{
    "body": "Replying to [comment:6 leif]:\n> There are also post-merge comments at #9665, I don't know if they should be included here or if there's even a new ticket for these.\n\n\nI've added a note at #9665 about this ticket.",
    "created_at": "2010-08-13T21:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92633",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:6 leif]:
> There are also post-merge comments at #9665, I don't know if they should be included here or if there's even a new ticket for these.


I've added a note at #9665 about this ticket.



---

archive/issue_comments_092634.json:
```json
{
    "body": "I've changed the title and description a bit, to reflect the fact that #9343 is **not** Pari 2.4.3. \n\nNot even Pari 2.4.2 has ever been released - there is only an alpha of that available. \n\nDave",
    "created_at": "2010-08-13T23:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92634",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've changed the title and description a bit, to reflect the fact that #9343 is **not** Pari 2.4.3. 

Not even Pari 2.4.2 has ever been released - there is only an alpha of that available. 

Dave



---

archive/issue_comments_092635.json:
```json
{
    "body": "Replying to [comment:12 drkirkby]:\n> I've changed the title and description a bit, to reflect the fact that #9343 is **not** Pari 2.4.3. \n\n\nYou should perhaps have updated the spkg link to point to John Cremona's new p2 spkg, too. ;-)",
    "created_at": "2010-08-13T23:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92635",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:12 drkirkby]:
> I've changed the title and description a bit, to reflect the fact that #9343 is **not** Pari 2.4.3. 


You should perhaps have updated the spkg link to point to John Cremona's new p2 spkg, too. ;-)



---

archive/issue_comments_092636.json:
```json
{
    "body": "Replying to [comment:14 leif]:\n> Replying to [comment:12 drkirkby]:\n> > I've changed the title and description a bit, to reflect the fact that #9343 is **not** Pari 2.4.3. \n\n> \n> You should perhaps have updated the spkg link to point to John Cremona's new p2 spkg, too. ;-) \n\nI don't know where it is. In any case, it should not be a .p2, since the current one in Sage is lcalc-20100428-1.23.p0.spkg, to a revision should be called lcalc-20100428-1.23.p1.spkg. \n\nI hope the \n\n`gcc -Wa,-W` \n\n(to suppress warnings from the assembler), has not got back in, as -W is not recognised by the Sun assembler and it creates an error. \n\nDave",
    "created_at": "2010-08-14T00:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92636",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:14 leif]:
> Replying to [comment:12 drkirkby]:
> > I've changed the title and description a bit, to reflect the fact that #9343 is **not** Pari 2.4.3. 

> 
> You should perhaps have updated the spkg link to point to John Cremona's new p2 spkg, too. ;-) 

I don't know where it is. In any case, it should not be a .p2, since the current one in Sage is lcalc-20100428-1.23.p0.spkg, to a revision should be called lcalc-20100428-1.23.p1.spkg. 

I hope the 

`gcc -Wa,-W` 

(to suppress warnings from the assembler), has not got back in, as -W is not recognised by the Sun assembler and it creates an error. 

Dave



---

archive/issue_comments_092637.json:
```json
{
    "body": "Replying to [comment:15 drkirkby]:\n> Replying to [comment:14 leif]:\n> > Replying to [comment:12 drkirkby]:\n> > > I've changed the title and description a bit, to reflect the fact that #9343 is **not** Pari 2.4.3. \n\n> > \n> > You should perhaps have updated the spkg link to point to John Cremona's new p2 spkg, too. ;-) \n\n> I don't know where it is. In any case, it should not be a .p2, since the current one in Sage is lcalc-20100428-1.23.p0.spkg, to a revision should be called lcalc-20100428-1.23.p1.spkg.\n\nBrowser cache issue?\n\nSee http://trac.sagemath.org/sage_trac/ticket/9592#comment:10 (where)\n\nand http://trac.sagemath.org/sage_trac/ticket/9592#comment:5 (why).\n\n(lcalc-20100428-1.23.p1.spkg from #9665 was merged into Sage 4.5.2.rc1)",
    "created_at": "2010-08-14T00:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92637",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:15 drkirkby]:
> Replying to [comment:14 leif]:
> > Replying to [comment:12 drkirkby]:
> > > I've changed the title and description a bit, to reflect the fact that #9343 is **not** Pari 2.4.3. 

> > 
> > You should perhaps have updated the spkg link to point to John Cremona's new p2 spkg, too. ;-) 

> I don't know where it is. In any case, it should not be a .p2, since the current one in Sage is lcalc-20100428-1.23.p0.spkg, to a revision should be called lcalc-20100428-1.23.p1.spkg.

Browser cache issue?

See http://trac.sagemath.org/sage_trac/ticket/9592#comment:10 (where)

and http://trac.sagemath.org/sage_trac/ticket/9592#comment:5 (why).

(lcalc-20100428-1.23.p1.spkg from #9665 was merged into Sage 4.5.2.rc1)



---

archive/issue_comments_092638.json:
```json
{
    "body": "I removed some .DS_Store and ._.DS_Store files from John's spkg and uploaded the result to [http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg](http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg)",
    "created_at": "2010-08-14T10:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92638",
    "user": "https://github.com/jdemeyer"
}
```

I removed some .DS_Store and ._.DS_Store files from John's spkg and uploaded the result to [http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg](http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg)



---

archive/issue_comments_092639.json:
```json
{
    "body": "I can see that this spkg does not depend on the upgrade to the new pari. This can be included before the latest version of pari is accepted. In couple of month, I will try to get Mike to use autotools for building. This will eliminate a lot of problems with spkg as of now. I am changing the status to needs review if it is ok with you.",
    "created_at": "2010-08-14T12:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92639",
    "user": "https://github.com/rishikesha"
}
```

I can see that this spkg does not depend on the upgrade to the new pari. This can be included before the latest version of pari is accepted. In couple of month, I will try to get Mike to use autotools for building. This will eliminate a lot of problems with spkg as of now. I am changing the status to needs review if it is ok with you.



---

archive/issue_comments_092640.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-14T12:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92640",
    "user": "https://github.com/rishikesha"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092641.json:
```json
{
    "body": "Following suggestion of Mitesh, I have small some small cleaning up of unnecessary files in patches and few lines in spkg-install over the changes of jdemeyer.\n\nhttp://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p2.spkg",
    "created_at": "2010-08-14T12:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92641",
    "user": "https://github.com/rishikesha"
}
```

Following suggestion of Mitesh, I have small some small cleaning up of unnecessary files in patches and few lines in spkg-install over the changes of jdemeyer.

http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p2.spkg



---

archive/issue_comments_092642.json:
```json
{
    "body": "Replying to [comment:19 rishi]:\n> I can see that this spkg does not depend on the upgrade to the new pari. This can be included before the latest version of pari is accepted. In couple of month, I will try to get Mike to use autotools for building. This will eliminate a lot of problems with spkg as of now. I am changing the status to needs review if it is ok with you.\n\n\nPerhaps do some of the clean-up I [suggested above](http://trac.sagemath.org/sage_trac/ticket/9592#comment:8)?\n\nThere are further minor things (like the date/version at the top of `spkg-install`; `SAGE_DEBUG=yes` usually disables optimization, unquoted environment variables, etc.).\n\nI wonder if we should add (a) further patch(es) to get rid of some of the annoying warnings (cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:191 ff.), but we probably shouldn't do too much at this ticket.\n\nI'm not sure if Cygwin support is required yet... ;-)",
    "created_at": "2010-08-14T12:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92642",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:19 rishi]:
> I can see that this spkg does not depend on the upgrade to the new pari. This can be included before the latest version of pari is accepted. In couple of month, I will try to get Mike to use autotools for building. This will eliminate a lot of problems with spkg as of now. I am changing the status to needs review if it is ok with you.


Perhaps do some of the clean-up I [suggested above](http://trac.sagemath.org/sage_trac/ticket/9592#comment:8)?

There are further minor things (like the date/version at the top of `spkg-install`; `SAGE_DEBUG=yes` usually disables optimization, unquoted environment variables, etc.).

I wonder if we should add (a) further patch(es) to get rid of some of the annoying warnings (cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:191 ff.), but we probably shouldn't do too much at this ticket.

I'm not sure if Cygwin support is required yet... ;-)



---

archive/issue_comments_092643.json:
```json
{
    "body": "Replying to [comment:20 rishi]:\n> Following suggestion of Mitesh, I have small some small cleaning up of unnecessary files in patches and few lines in spkg-install over the changes of jdemeyer.\n> \n> http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p2.spkg\n\n\nCould you upload an spkg patch for your changes (except file deletions) here?\n\nIt's a bit more convenient for reviewing and adding further changes...",
    "created_at": "2010-08-14T12:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92643",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:20 rishi]:
> Following suggestion of Mitesh, I have small some small cleaning up of unnecessary files in patches and few lines in spkg-install over the changes of jdemeyer.
> 
> http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p2.spkg


Could you upload an spkg patch for your changes (except file deletions) here?

It's a bit more convenient for reviewing and adding further changes...



---

archive/issue_comments_092644.json:
```json
{
    "body": "Replying to [comment:20 rishi]:\n> Following suggestion of Mitesh, I have small some small cleaning up of unnecessary files in patches and few lines in spkg-install over the changes of jdemeyer.\n> \n> http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p2.spkg\n\n\nI copied your spkg to [http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg](http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg) (like this, I don't have to update the descriptions of #9343 and #9592).",
    "created_at": "2010-08-14T12:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92644",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:20 rishi]:
> Following suggestion of Mitesh, I have small some small cleaning up of unnecessary files in patches and few lines in spkg-install over the changes of jdemeyer.
> 
> http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p2.spkg


I copied your spkg to [http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg](http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg) (like this, I don't have to update the descriptions of #9343 and #9592).



---

archive/issue_comments_092645.json:
```json
{
    "body": "Attachment [spkg-install.diff](tarball://root/attachments/some-uuid/ticket9592/spkg-install.diff) by @rishikesha created at 2010-08-14 13:15:56\n\nI am not sure what you want to be done. Can you make the changes and attach it here.\n\nReplying to [comment:21 leif]:\n> Replying to [comment:19 rishi]:\n> > I can see that this spkg does not depend on the upgrade to the new pari. This can be included before the latest version of pari is accepted. In couple of month, I will try to get Mike to use autotools for building. This will eliminate a lot of problems with spkg as of now. I am changing the status to needs review if it is ok with you.\n\n> \n> Perhaps do some of the clean-up I [suggested above](http://trac.sagemath.org/sage_trac/ticket/9592#comment:8)?\n> \n> There are further minor things (like the date/version at the top of `spkg-install`; `SAGE_DEBUG=yes` usually disables optimization, unquoted environment variables, etc.).\n> \n> I wonder if we should add (a) further patch(es) to get rid of some of the annoying warnings (cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:191 ff.), but we probably shouldn't do too much at this ticket.\n> \n> I'm not sure if Cygwin support is required yet... ;-)",
    "created_at": "2010-08-14T13:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92645",
    "user": "https://github.com/rishikesha"
}
```

Attachment [spkg-install.diff](tarball://root/attachments/some-uuid/ticket9592/spkg-install.diff) by @rishikesha created at 2010-08-14 13:15:56

I am not sure what you want to be done. Can you make the changes and attach it here.

Replying to [comment:21 leif]:
> Replying to [comment:19 rishi]:
> > I can see that this spkg does not depend on the upgrade to the new pari. This can be included before the latest version of pari is accepted. In couple of month, I will try to get Mike to use autotools for building. This will eliminate a lot of problems with spkg as of now. I am changing the status to needs review if it is ok with you.

> 
> Perhaps do some of the clean-up I [suggested above](http://trac.sagemath.org/sage_trac/ticket/9592#comment:8)?
> 
> There are further minor things (like the date/version at the top of `spkg-install`; `SAGE_DEBUG=yes` usually disables optimization, unquoted environment variables, etc.).
> 
> I wonder if we should add (a) further patch(es) to get rid of some of the annoying warnings (cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:191 ff.), but we probably shouldn't do too much at this ticket.
> 
> I'm not sure if Cygwin support is required yet... ;-)



---

archive/issue_comments_092646.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-08-19T11:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92646",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_092647.json:
```json
{
    "body": "Attachment [lcalc-spkg.patch](tarball://root/attachments/some-uuid/ticket9592/lcalc-spkg.patch) by @jdemeyer created at 2010-08-21 12:44:27\n\nComplete spkg patch (for reference)",
    "created_at": "2010-08-21T12:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92647",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [lcalc-spkg.patch](tarball://root/attachments/some-uuid/ticket9592/lcalc-spkg.patch) by @jdemeyer created at 2010-08-21 12:44:27

Complete spkg patch (for reference)



---

archive/issue_comments_092648.json:
```json
{
    "body": "I've made an spkg that builds on Cygwin at #9775 based on the one here.  It might make more sense to make any additional changes to the SPKG there.",
    "created_at": "2010-08-21T18:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92648",
    "user": "https://github.com/mwhansen"
}
```

I've made an spkg that builds on Cygwin at #9775 based on the one here.  It might make more sense to make any additional changes to the SPKG there.



---

archive/issue_comments_092649.json:
```json
{
    "body": "Replying to [comment:27 mhansen]:\n> I've made an spkg that builds on Cygwin at #9775 based on the one here.  It might make more sense to make any additional changes to the SPKG there.\n\n\nSee #9845, too.",
    "created_at": "2010-09-02T10:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92649",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:27 mhansen]:
> I've made an spkg that builds on Cygwin at #9775 based on the one here.  It might make more sense to make any additional changes to the SPKG there.


See #9845, too.



---

archive/issue_comments_092650.json:
```json
{
    "body": "Rishi, do Jeroen's changes look good to you?  If they are, I suggest that we leave further changes for other tickets.",
    "created_at": "2010-09-02T10:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92650",
    "user": "https://github.com/qed777"
}
```

Rishi, do Jeroen's changes look good to you?  If they are, I suggest that we leave further changes for other tickets.



---

archive/issue_comments_092651.json:
```json
{
    "body": "Also, the `dist/` (Debian) directory should be removed, cf. #5903.",
    "created_at": "2010-09-03T22:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92651",
    "user": "https://github.com/nexttime"
}
```

Also, the `dist/` (Debian) directory should be removed, cf. #5903.



---

archive/issue_comments_092652.json:
```json
{
    "body": "Replying to [comment:31 leif]:\n> Also, the `dist/` (Debian) directory should be removed, cf. #5903.\n\n\nI suggest that we do this at #9845, unless we otherwise need to update the package here.",
    "created_at": "2010-09-04T07:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92652",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:31 leif]:
> Also, the `dist/` (Debian) directory should be removed, cf. #5903.


I suggest that we do this at #9845, unless we otherwise need to update the package here.



---

archive/issue_comments_092653.json:
```json
{
    "body": "Replying to [comment:32 mpatel]:\n> Replying to [comment:31 leif]:\n> > Also, the `dist/` (Debian) directory should be removed, cf. #5903.\n\n> \n> I suggest that we do this at #9845, unless we otherwise need to update the package here.\n\n\nYes; hopefully #9845 gets reviewed soon s.t. this ticket won't get merged at all (positively reviewed though), since the former contains all changes from here.",
    "created_at": "2010-09-04T09:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92653",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:32 mpatel]:
> Replying to [comment:31 leif]:
> > Also, the `dist/` (Debian) directory should be removed, cf. #5903.

> 
> I suggest that we do this at #9845, unless we otherwise need to update the package here.


Yes; hopefully #9845 gets reviewed soon s.t. this ticket won't get merged at all (positively reviewed though), since the former contains all changes from here.



---

archive/issue_comments_092654.json:
```json
{
    "body": "Do we have a positive review here?",
    "created_at": "2010-09-09T11:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92654",
    "user": "https://github.com/qed777"
}
```

Do we have a positive review here?



---

archive/issue_comments_092655.json:
```json
{
    "body": "Doesn't bother **me**, but should we keep\n\n```sh\n# disable Cygwin build for now\nif [ \"$UNAME\" = \"CYGWIN\" ]; then\n#    cp ../../patches/Lcommandline_elliptic.cc .\n    echo \"Sorry, the lcalc build is currently broken\"\n    echo 1\nfi\n```\n**?** (In case I by luck have looked at the current `.p2` / its current patches/diffs.)\n\nFortunately there's a follow-up ticket to address the rest...",
    "created_at": "2010-09-09T12:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92655",
    "user": "https://github.com/nexttime"
}
```

Doesn't bother **me**, but should we keep

```sh
# disable Cygwin build for now
if [ "$UNAME" = "CYGWIN" ]; then
#    cp ../../patches/Lcommandline_elliptic.cc .
    echo "Sorry, the lcalc build is currently broken"
    echo 1
fi
```
**?** (In case I by luck have looked at the current `.p2` / its current patches/diffs.)

Fortunately there's a follow-up ticket to address the rest...



---

archive/issue_comments_092656.json:
```json
{
    "body": "Is `patches/Lcommandline_elliptic.cc.cygwin.diff` up to date?  Do we still use `patches/Lcommandline_elliptic.cc.cygwin.*`.  Let's do any necessary updates at #9845.",
    "created_at": "2010-09-10T11:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92656",
    "user": "https://github.com/qed777"
}
```

Is `patches/Lcommandline_elliptic.cc.cygwin.diff` up to date?  Do we still use `patches/Lcommandline_elliptic.cc.cygwin.*`.  Let's do any necessary updates at #9845.



---

archive/issue_comments_092657.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-10T11:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92657",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092658.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-10T11:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9592#issuecomment-92658",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_023892.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-10T11:19:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9592",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9592#event-23892"
}
```
