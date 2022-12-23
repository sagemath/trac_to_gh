# Issue 8509: Ilegal 'grep -o' causes problems installing optional packages on Solaris

Issue created by migration from https://trac.sagemath.org/ticket/8509

Original creator: drkirkby

Original creation time: 2010-03-12 17:55:33

Assignee: drkirkby

CC:  jhpalmieri

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







---

Attachment

Revised sage-spkg removing the -o option


---

Comment by drkirkby created at 2010-03-13 18:23:46

Thanks to John Palmieri who suggested this solution, which does work.


---

Comment by drkirkby created at 2010-03-13 18:23:46

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-03-13 19:52:30

sage-spkg should be under revision control: either run Mercurial from the directory SAGE_ROOT/local/bin, or while running sage, use "hg_scripts" (instead of "hg_sage").


---

Comment by drkirkby created at 2010-03-13 22:07:02

Oops, my mistake. I was not aware of that. I'm attaching a Mercurial patch


---

Attachment

Mercurial patch (replaces the earlier one, which was just from 'diff')


---

Comment by dimpase created at 2010-03-15 07:31:53

Replying to [comment:3 drkirkby]:
> Oops, my mistake. I was not aware of that. I'm attaching a Mercurial patch

Dave, $SAGE_ROOT/local/bin is not under hg.
You should create a  patch for the corresponding source place, i.e. 
for a script in sage_scripts-4.3.4.alpha1.spkg

That's the only way to make it into the release, AFAIK.


---

Comment by dimpase created at 2010-03-15 07:31:53

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-03-15 14:40:19

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-03-15 14:40:19

Replying to [comment:4 dimpase]:
> Replying to [comment:3 drkirkby]:
> > Oops, my mistake. I was not aware of that. I'm attaching a Mercurial patch
> 
> Dave, $SAGE_ROOT/local/bin is not under hg.

It is, actually; as I said before, it's the "scripts" repository discussed [in the Sage developer's guide](http://www.sagemath.org/doc/developer/producing_patches.html#using-mercurial-with-other-sage-repositories).


---

Comment by drkirkby created at 2010-03-15 14:56:29

I created that while running Mercurial from $SAGE_ROOT/local/bin which is what you said John. I did not use 'hg_scripts'. (I tend to prefer using 'hg' as it means one can apply patches to Sage before even building it. 

I'll try use 'hg_scripts' later, but for now I need to do something more pressing. I'm in the middle of decorating and my wife will be coming home in a few days expecting to see it done. Like all these things, it takes a lot longer than one thinks. So this patch is going to have to wait a bit. 

If anyone want to replace my patch with one more suitable, feel free, but otherwise I'll sort this out when I've got the more important jobs out of the way. 

Dave


---

Comment by jhpalmieri created at 2010-03-15 17:41:42

Running "hg_scripts" from within Sage is, as far as I know, equivalent to running "hg" or "sage -hg" from the command line while in the directory $SAGE_ROOT/local/bin.  So you don't need to produce a new patch.


---

Comment by drkirkby created at 2010-03-15 18:55:24

Thank you John. 

That makes sense. I think I just need to put a note for the release manager to sage what repository it goes in, but apart from that, I think it will be ok. 

All we need now is someone to review it! Since it was your idea, and I tested and wrote it, then neither of us can review it. 

Dave


---

Comment by drkirkby created at 2010-03-15 18:58:56

* Note to the release manager - this patch is for the sage shell scripts repository.*


---

Comment by dimpase created at 2010-03-17 03:58:57

Replying to [comment:8 drkirkby]:

> 
> All we need now is someone to review it! Since it was your idea, and I tested and wrote it, then neither of us can review it. 
> 

Works on t2 (and on a Linux install, just to check it doesn't break anything badly). 
So, thumbs up!


---

Comment by dimpase created at 2010-03-17 03:58:57

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 17:29:45

Merged "sage-spkg.patch" into 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-16 17:29:45

Resolution: fixed
