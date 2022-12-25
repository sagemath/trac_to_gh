# Issue 6399: [with patch, needs review] Allow ATLAS to build on Solaris with Sun or GNU linker

archive/issues_006399.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: solaris atlas GNUism\n\nATLAS will currently not build on Solaris if the linker is the Sun linker in /usr/ccs/bin, as the flags in the Makefile used for building shared libraries are GNU-specific. \n\nThis patch uses 'sed' to change the flags in the Makefile. The flags charged are:\n\n```\n   -shared ==> -G\n   -soname ==> -h\n   --whole-archive ==>  -z allextract\n   --no-whole-archive ==> -z defaultextract\n```\n\nTests are performed on both the operating system and linker. The Makefile is only changed if both the OS is Solaris and the linker is not the GNU linker. (It's pretty safe to assume the Sun linker is used, if the linker is not the GNU one). The changes are to the file are in the file 'spkg-install-script' and essentially consist of:\n\n```\n        if [ `uname` = \"SunOS\" ]; then\n          if [ \"`ld  --version  2>&1  | grep GNU`\" = \"\" ]; then\n             echo \"The Makefile generated in ATLAS for building shared libraries\"\n             echo \"assumes the linker is the GNU linker, which it not true in\"\n             echo \"your setup. (It is generally considered better to use the\"\n             echo \"Sun linker in /usr/ccs/bin rather than the GNU linker from binutils)\"\n             echo \"The linker flags in `pwd`/Makefile will be changed. \"\n             echo \"'-shared' will be changed to '-G'\"\n             echo \"'-soname' will be changed to '-h'\"\n             echo \"'--whole-archive' will be changed to '-zallextract'\"\n             echo \"'--no-whole-archive' will be changed to '-zdefaultextract'\"\n             echo \"A copy of the original Makefile will be copied to Makefile.orig\"\n             cp Makefile Makefile.orig\n             sed 's/-shared/-G/g' Makefile > makefile\n             sed 's/-soname/-h/g' makefile > Makefile\n             sed 's/--whole-archive/-z allextract/g' Makefile > makefile\n             sed 's/--no-whole-archive/-z defaultextract/g' makefile > Makefile\n             rm makefile\n          else\n             echo \"WARNING You are using the GNU linker from 'binutils'\"\n             echo \"Generally it is considered better to use the Sun linker\"\n             echo \"but Sage has been built on Solaris using the GNU linker\"\n          fi\n        fi\n\n```\n\nPatch is at. \nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/atlas/\n\nIssue created by migration from https://trac.sagemath.org/ticket/6399\n\n",
    "created_at": "2009-06-24T23:49:38Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, needs review] Allow ATLAS to build on Solaris with Sun or GNU linker",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6399",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Keywords: solaris atlas GNUism

ATLAS will currently not build on Solaris if the linker is the Sun linker in /usr/ccs/bin, as the flags in the Makefile used for building shared libraries are GNU-specific. 

This patch uses 'sed' to change the flags in the Makefile. The flags charged are:

```
   -shared ==> -G
   -soname ==> -h
   --whole-archive ==>  -z allextract
   --no-whole-archive ==> -z defaultextract
```

Tests are performed on both the operating system and linker. The Makefile is only changed if both the OS is Solaris and the linker is not the GNU linker. (It's pretty safe to assume the Sun linker is used, if the linker is not the GNU one). The changes are to the file are in the file 'spkg-install-script' and essentially consist of:

```
        if [ `uname` = "SunOS" ]; then
          if [ "`ld  --version  2>&1  | grep GNU`" = "" ]; then
             echo "The Makefile generated in ATLAS for building shared libraries"
             echo "assumes the linker is the GNU linker, which it not true in"
             echo "your setup. (It is generally considered better to use the"
             echo "Sun linker in /usr/ccs/bin rather than the GNU linker from binutils)"
             echo "The linker flags in `pwd`/Makefile will be changed. "
             echo "'-shared' will be changed to '-G'"
             echo "'-soname' will be changed to '-h'"
             echo "'--whole-archive' will be changed to '-zallextract'"
             echo "'--no-whole-archive' will be changed to '-zdefaultextract'"
             echo "A copy of the original Makefile will be copied to Makefile.orig"
             cp Makefile Makefile.orig
             sed 's/-shared/-G/g' Makefile > makefile
             sed 's/-soname/-h/g' makefile > Makefile
             sed 's/--whole-archive/-z allextract/g' Makefile > makefile
             sed 's/--no-whole-archive/-z defaultextract/g' makefile > Makefile
             rm makefile
          else
             echo "WARNING You are using the GNU linker from 'binutils'"
             echo "Generally it is considered better to use the Sun linker"
             echo "but Sage has been built on Solaris using the GNU linker"
          fi
        fi

```

Patch is at. 
http://sage.math.washington.edu/home/kirkby/Solaris-fixes/atlas/

Issue created by migration from https://trac.sagemath.org/ticket/6399





---

archive/issue_comments_051302.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2009-06-24T23:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6399#issuecomment-51302",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_051303.json:
```json
{
    "body": "It's probably best to leave this for now, as 6276 was rejected by the merge scripts and this this patch was written based on the assumption that 6276, which had positive review, would be merged. \n\nI'll update when I know more about why 6276 was rejected. \n\nDave",
    "created_at": "2009-06-25T02:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6399#issuecomment-51303",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It's probably best to leave this for now, as 6276 was rejected by the merge scripts and this this patch was written based on the assumption that 6276, which had positive review, would be merged. 

I'll update when I know more about why 6276 was rejected. 

Dave



---

archive/issue_comments_051304.json:
```json
{
    "body": "The reason 6276 was rejected is because the version number clashed and needed to be updated. That was done, and the patch has been incorporated into the tree (marked as fixed now). \n\nSo can this now be reviewed? \n\n\nDave",
    "created_at": "2009-07-09T22:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6399#issuecomment-51304",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The reason 6276 was rejected is because the version number clashed and needed to be updated. That was done, and the patch has been incorporated into the tree (marked as fixed now). 

So can this now be reviewed? 


Dave



---

archive/issue_comments_051305.json:
```json
{
    "body": "I'm confused, this appears to have been incorporated in atlas-3.8.3.p5, so I think this can be classed as fixed. \n\nHere's the relavent bits of SPKG.txt \n\n## ChangeLog\n\n### atlas-3.8.3.p5 (David Kirkby, June 24th 2009)\n* Made a backup of ATLAS-build/lib/Makefile to ATLAS-build/lib/Makefile.orig\n* Alter the flags in ATLAS-build/lib/Makefile with those that will work if the linker\n  used is the Sun linker. The default Makefile makes use of the GNU linker's\n  flags, such as \"-shared\" which is not acceptable to the Sun linker.\n\n  The patch is only applied if the operating system is Solaris, and the\n  linker is not the GNU linker. The flags charged are:\n  -shared ==> -G\n  -soname ==> -h\n  --whole-archive ==>  -z allextract\n  --no-whole-archive ==> -z defaultextract\n\n   NOTES:\n   1) Sun have a tool which accepts gcc flags, but calls the Sun compiler.\n   This patch might mess things up if that is used. Having never used the tool\n   it's impossible to be 100% sure of this. Anyway, that will be some time in\n   the future, so this patch can be removed.\n\n   2) The fact the linker flags are GNU specific has been reported to the ATLAS\n   maintainer, so they may fix this problem. In which case the patch could be\n   removed at a later date.\n  * Fixed a minor spelling mistake in this file\n\n### atlas-3.8.3.p4 (David Kirkby, June 16th 2009)\n* Change GuessSmallNB() in src/tune/blas/gemm/mmsearch.c\n  as suggested by Clint Whaley to return 28\n  on Solaris. This is ONLY A TEMPORARY FIX and once the real problem\n  in the function is sorted out, this fix will need to be removed. But\n  for now it permits ATLAS to build on a Sun T5240 with gcc-4.4.0.",
    "created_at": "2009-07-09T22:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6399#issuecomment-51305",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm confused, this appears to have been incorporated in atlas-3.8.3.p5, so I think this can be classed as fixed. 

Here's the relavent bits of SPKG.txt 

## ChangeLog

### atlas-3.8.3.p5 (David Kirkby, June 24th 2009)
* Made a backup of ATLAS-build/lib/Makefile to ATLAS-build/lib/Makefile.orig
* Alter the flags in ATLAS-build/lib/Makefile with those that will work if the linker
  used is the Sun linker. The default Makefile makes use of the GNU linker's
  flags, such as "-shared" which is not acceptable to the Sun linker.

  The patch is only applied if the operating system is Solaris, and the
  linker is not the GNU linker. The flags charged are:
  -shared ==> -G
  -soname ==> -h
  --whole-archive ==>  -z allextract
  --no-whole-archive ==> -z defaultextract

   NOTES:
   1) Sun have a tool which accepts gcc flags, but calls the Sun compiler.
   This patch might mess things up if that is used. Having never used the tool
   it's impossible to be 100% sure of this. Anyway, that will be some time in
   the future, so this patch can be removed.

   2) The fact the linker flags are GNU specific has been reported to the ATLAS
   maintainer, so they may fix this problem. In which case the patch could be
   removed at a later date.
  * Fixed a minor spelling mistake in this file

### atlas-3.8.3.p4 (David Kirkby, June 16th 2009)
* Change GuessSmallNB() in src/tune/blas/gemm/mmsearch.c
  as suggested by Clint Whaley to return 28
  on Solaris. This is ONLY A TEMPORARY FIX and once the real problem
  in the function is sorted out, this fix will need to be removed. But
  for now it permits ATLAS to build on a Sun T5240 with gcc-4.4.0.



---

archive/issue_comments_051306.json:
```json
{
    "body": "I'm puzzled while this is shown as needing review, when it is already incorporated.",
    "created_at": "2009-07-13T23:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6399#issuecomment-51306",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm puzzled while this is shown as needing review, when it is already incorporated.



---

archive/issue_comments_051307.json:
```json
{
    "body": "I'm not sure who the reviewer was. And the milestone for this ticket should be 4.1, not 4.1.1.",
    "created_at": "2009-07-16T08:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6399#issuecomment-51307",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I'm not sure who the reviewer was. And the milestone for this ticket should be 4.1, not 4.1.1.



---

archive/issue_events_006645.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-07-17T07:45:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6399",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6399#event-6645"
}
```



---

archive/issue_comments_051308.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-17T07:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6399#issuecomment-51308",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_051309.json:
```json
{
    "body": "I was reviewing this while doing release management for 4.1. I must have accidentally closed the window before updating the ticket.",
    "created_at": "2009-07-17T17:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6399#issuecomment-51309",
    "user": "https://github.com/rlmill"
}
```

I was reviewing this while doing release management for 4.1. I must have accidentally closed the window before updating the ticket.
