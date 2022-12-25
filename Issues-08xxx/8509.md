# Issue 8509: Ilegal 'grep -o' causes problems installing optional packages on Solaris

archive/issues_008509.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jhpalmieri\n\n## Hardware\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs.\n* 2 GB RAM\n \n == Software ==\n* Solaris 10 03/2005 (the first release)\n* Sage 4.3.4.alpha1 (The first Sage release to build and pass all doctests on Solaris)\n\n## The problem\n\nDespite the fact that Sage builds and pass all doctests (including the long ones), installing optional packages is problematic, as it would appear something is calling 'grep' with the '-o' option which is not POSIX compatible\n\nhttp://www.opengroup.org/onlinepubs/9699919799/utilities/grep.html\n\nThis causes the problems below:\n\n```\nsage: for X in optional_packages()[1]:  install_package(X)\n....: \nForce installing ace-5.0.p0\nCalling sage-spkg on ace-5.0.p0\nWarning: Attempted to overwrite SAGE_ROOT environment variable\nace-5.0.p0\nMachine:\nSunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000\nDeleting directories from past builds of previous/current versions of ace-5.0.p0\n/export/home/drkirkby/sage-4.3.4.alpha1/local/bin/sage-spkg: file ace-5.0.p0 does not exist\nAttempting to download it.\ngrep: illegal option -- o\nUsage: grep -hblcnsviw pattern file . . .\nSearching for latest version of ace-5.0.p0\nCould not find a version for ace-5.0.p0.\n\nForce installing biopython-1.53.p0\nCalling sage-spkg on biopython-1.53.p0\nWarning: Attempted to overwrite SAGE_ROOT environment variable\nbiopython-1.53.p0\nMachine:\nSunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000\nDeleting directories from past builds of previous/current versions of biopython-1.53.p0\n/export/home/drkirkby/sage-4.3.4.alpha1/local/bin/sage-spkg: file biopython-1.53.p0 does not exist\nAttempting to download it.\ngrep: illegal option -- o\nUsage: grep -hblcnsviw pattern file . . .\nSearching for latest version of biopython-1.53.p0\nCould not find a version for biopython-1.53.p0.\n```\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8509\n\n",
    "closed_at": "2010-04-16T17:29:45Z",
    "created_at": "2010-03-12T17:55:33Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Ilegal 'grep -o' causes problems installing optional packages on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8509",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jhpalmieri

## Hardware
* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs.
* 2 GB RAM
 
 == Software ==
* Solaris 10 03/2005 (the first release)
* Sage 4.3.4.alpha1 (The first Sage release to build and pass all doctests on Solaris)

## The problem

Despite the fact that Sage builds and pass all doctests (including the long ones), installing optional packages is problematic, as it would appear something is calling 'grep' with the '-o' option which is not POSIX compatible

http://www.opengroup.org/onlinepubs/9699919799/utilities/grep.html

This causes the problems below:

```
sage: for X in optional_packages()[1]:  install_package(X)
....: 
Force installing ace-5.0.p0
Calling sage-spkg on ace-5.0.p0
Warning: Attempted to overwrite SAGE_ROOT environment variable
ace-5.0.p0
Machine:
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
Deleting directories from past builds of previous/current versions of ace-5.0.p0
/export/home/drkirkby/sage-4.3.4.alpha1/local/bin/sage-spkg: file ace-5.0.p0 does not exist
Attempting to download it.
grep: illegal option -- o
Usage: grep -hblcnsviw pattern file . . .
Searching for latest version of ace-5.0.p0
Could not find a version for ace-5.0.p0.

Force installing biopython-1.53.p0
Calling sage-spkg on biopython-1.53.p0
Warning: Attempted to overwrite SAGE_ROOT environment variable
biopython-1.53.p0
Machine:
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
Deleting directories from past builds of previous/current versions of biopython-1.53.p0
/export/home/drkirkby/sage-4.3.4.alpha1/local/bin/sage-spkg: file biopython-1.53.p0 does not exist
Attempting to download it.
grep: illegal option -- o
Usage: grep -hblcnsviw pattern file . . .
Searching for latest version of biopython-1.53.p0
Could not find a version for biopython-1.53.p0.
```





Issue created by migration from https://trac.sagemath.org/ticket/8509





---

archive/issue_comments_076702.json:
```json
{
    "body": "Attachment [sage-spkg](tarball://root/attachments/some-uuid/ticket8509/sage-spkg) by drkirkby created at 2010-03-13 18:18:21\n\nRevised sage-spkg removing the -o option",
    "created_at": "2010-03-13T18:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76702",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [sage-spkg](tarball://root/attachments/some-uuid/ticket8509/sage-spkg) by drkirkby created at 2010-03-13 18:18:21

Revised sage-spkg removing the -o option



---

archive/issue_comments_076703.json:
```json
{
    "body": "Thanks to John Palmieri who suggested this solution, which does work.",
    "created_at": "2010-03-13T18:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76703",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thanks to John Palmieri who suggested this solution, which does work.



---

archive/issue_comments_076704.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-13T18:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76704",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076705.json:
```json
{
    "body": "sage-spkg should be under revision control: either run Mercurial from the directory SAGE_ROOT/local/bin, or while running sage, use \"hg_scripts\" (instead of \"hg_sage\").",
    "created_at": "2010-03-13T19:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76705",
    "user": "https://github.com/jhpalmieri"
}
```

sage-spkg should be under revision control: either run Mercurial from the directory SAGE_ROOT/local/bin, or while running sage, use "hg_scripts" (instead of "hg_sage").



---

archive/issue_comments_076706.json:
```json
{
    "body": "Oops, my mistake. I was not aware of that. I'm attaching a Mercurial patch",
    "created_at": "2010-03-13T22:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76706",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Oops, my mistake. I was not aware of that. I'm attaching a Mercurial patch



---

archive/issue_comments_076707.json:
```json
{
    "body": "Attachment [sage-spkg.patch](tarball://root/attachments/some-uuid/ticket8509/sage-spkg.patch) by drkirkby created at 2010-03-13 22:08:36\n\nMercurial patch (replaces the earlier one, which was just from 'diff')",
    "created_at": "2010-03-13T22:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76707",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [sage-spkg.patch](tarball://root/attachments/some-uuid/ticket8509/sage-spkg.patch) by drkirkby created at 2010-03-13 22:08:36

Mercurial patch (replaces the earlier one, which was just from 'diff')



---

archive/issue_comments_076708.json:
```json
{
    "body": "Replying to [comment:3 drkirkby]:\n> Oops, my mistake. I was not aware of that. I'm attaching a Mercurial patch\n\n\nDave, $SAGE_ROOT/local/bin is not under hg.\nYou should create a  patch for the corresponding source place, i.e. \nfor a script in sage_scripts-4.3.4.alpha1.spkg\n\nThat's the only way to make it into the release, AFAIK.",
    "created_at": "2010-03-15T07:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76708",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:3 drkirkby]:
> Oops, my mistake. I was not aware of that. I'm attaching a Mercurial patch


Dave, $SAGE_ROOT/local/bin is not under hg.
You should create a  patch for the corresponding source place, i.e. 
for a script in sage_scripts-4.3.4.alpha1.spkg

That's the only way to make it into the release, AFAIK.



---

archive/issue_comments_076709.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-15T07:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76709",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076710.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-15T14:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76710",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076711.json:
```json
{
    "body": "Replying to [comment:4 dimpase]:\n> Replying to [comment:3 drkirkby]:\n> > Oops, my mistake. I was not aware of that. I'm attaching a Mercurial patch\n\n> \n> Dave, $SAGE_ROOT/local/bin is not under hg.\n\n\nIt is, actually; as I said before, it's the \"scripts\" repository discussed [in the Sage developer's guide](http://www.sagemath.org/doc/developer/producing_patches.html#using-mercurial-with-other-sage-repositories).",
    "created_at": "2010-03-15T14:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76711",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:4 dimpase]:
> Replying to [comment:3 drkirkby]:
> > Oops, my mistake. I was not aware of that. I'm attaching a Mercurial patch

> 
> Dave, $SAGE_ROOT/local/bin is not under hg.


It is, actually; as I said before, it's the "scripts" repository discussed [in the Sage developer's guide](http://www.sagemath.org/doc/developer/producing_patches.html#using-mercurial-with-other-sage-repositories).



---

archive/issue_comments_076712.json:
```json
{
    "body": "I created that while running Mercurial from $SAGE_ROOT/local/bin which is what you said John. I did not use 'hg_scripts'. (I tend to prefer using 'hg' as it means one can apply patches to Sage before even building it. \n\nI'll try use 'hg_scripts' later, but for now I need to do something more pressing. I'm in the middle of decorating and my wife will be coming home in a few days expecting to see it done. Like all these things, it takes a lot longer than one thinks. So this patch is going to have to wait a bit. \n\nIf anyone want to replace my patch with one more suitable, feel free, but otherwise I'll sort this out when I've got the more important jobs out of the way. \n\nDave",
    "created_at": "2010-03-15T14:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76712",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I created that while running Mercurial from $SAGE_ROOT/local/bin which is what you said John. I did not use 'hg_scripts'. (I tend to prefer using 'hg' as it means one can apply patches to Sage before even building it. 

I'll try use 'hg_scripts' later, but for now I need to do something more pressing. I'm in the middle of decorating and my wife will be coming home in a few days expecting to see it done. Like all these things, it takes a lot longer than one thinks. So this patch is going to have to wait a bit. 

If anyone want to replace my patch with one more suitable, feel free, but otherwise I'll sort this out when I've got the more important jobs out of the way. 

Dave



---

archive/issue_comments_076713.json:
```json
{
    "body": "Running \"hg_scripts\" from within Sage is, as far as I know, equivalent to running \"hg\" or \"sage -hg\" from the command line while in the directory $SAGE_ROOT/local/bin.  So you don't need to produce a new patch.",
    "created_at": "2010-03-15T17:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76713",
    "user": "https://github.com/jhpalmieri"
}
```

Running "hg_scripts" from within Sage is, as far as I know, equivalent to running "hg" or "sage -hg" from the command line while in the directory $SAGE_ROOT/local/bin.  So you don't need to produce a new patch.



---

archive/issue_comments_076714.json:
```json
{
    "body": "Thank you John. \n\nThat makes sense. I think I just need to put a note for the release manager to sage what repository it goes in, but apart from that, I think it will be ok. \n\nAll we need now is someone to review it! Since it was your idea, and I tested and wrote it, then neither of us can review it. \n\nDave",
    "created_at": "2010-03-15T18:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76714",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thank you John. 

That makes sense. I think I just need to put a note for the release manager to sage what repository it goes in, but apart from that, I think it will be ok. 

All we need now is someone to review it! Since it was your idea, and I tested and wrote it, then neither of us can review it. 

Dave



---

archive/issue_comments_076715.json:
```json
{
    "body": "** Note to the release manager - this patch is for the sage shell scripts repository.**",
    "created_at": "2010-03-15T18:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76715",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

** Note to the release manager - this patch is for the sage shell scripts repository.**



---

archive/issue_comments_076716.json:
```json
{
    "body": "Replying to [comment:8 drkirkby]:\n\n> \n> All we need now is someone to review it! Since it was your idea, and I tested and wrote it, then neither of us can review it. \n> \n\n\nWorks on t2 (and on a Linux install, just to check it doesn't break anything badly). \nSo, thumbs up!",
    "created_at": "2010-03-17T03:58:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76716",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:8 drkirkby]:

> 
> All we need now is someone to review it! Since it was your idea, and I tested and wrote it, then neither of us can review it. 
> 


Works on t2 (and on a Linux install, just to check it doesn't break anything badly). 
So, thumbs up!



---

archive/issue_comments_076717.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-17T03:58:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76717",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076718.json:
```json
{
    "body": "Merged \"sage-spkg.patch\" into 4.4.alpha0.",
    "created_at": "2010-04-16T17:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76718",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "sage-spkg.patch" into 4.4.alpha0.



---

archive/issue_events_020433.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T17:29:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8509#event-20433"
}
```



---

archive/issue_comments_076719.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T17:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8509#issuecomment-76719",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
