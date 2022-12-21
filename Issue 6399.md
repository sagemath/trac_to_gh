# Issue 6399: [with patch, needs review] Allow ATLAS to build on Solaris with Sun or GNU linker

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-06-24 23:49:38

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


---

Comment by drkirkby created at 2009-06-24 23:50:06

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2009-06-25 02:54:40

It's probably best to leave this for now, as 6276 was rejected by the merge scripts and this this patch was written based on the assumption that 6276, which had positive review, would be merged. 

I'll update when I know more about why 6276 was rejected. 

Dave


---

Comment by drkirkby created at 2009-07-09 22:00:17

The reason 6276 was rejected is because the version number clashed and needed to be updated. That was done, and the patch has been incorporated into the tree (marked as fixed now). 

So can this now be reviewed? 


Dave


---

Comment by drkirkby created at 2009-07-09 22:21:32

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

Comment by drkirkby created at 2009-07-13 23:53:46

I'm puzzled while this is shown as needing review, when it is already incorporated.


---

Comment by mvngu created at 2009-07-16 08:27:49

I'm not sure who the reviewer was. And the milestone for this ticket should be 4.1, not 4.1.1.


---

Comment by mvngu created at 2009-07-17 07:45:48

Resolution: fixed


---

Comment by rlm created at 2009-07-17 17:07:58

I was reviewing this while doing release management for 4.1. I must have accidentally closed the window before updating the ticket.
