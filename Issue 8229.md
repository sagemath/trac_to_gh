# Issue 8229: gap_packages-4.4.12 updated

archive/issues_008229.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: GAP, GAP packages\n\nI created and tested, together with the \nupdated GAP to 4.4.12 --- see tickets #8150 and #8076 ---\ngap_packages-4.4.12_2.spkg, that is available at \nhttp://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg\nalong with  http://boxen.math.washington.edu/home/dima/packages/database_gap-4.4.12.spkg and\nhttp://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg\n\nplease test these (already tested OK on x86, x86_64, ia64, and OSX PPC 10.5)\ntogether, not forgetting to apply the patch \ntrack-8150 available at #8150, \nbut ignoring the other (obsolete) patches there and at #8076.\n\nThis ticket is issued in addition to #8150 and #8076\n\nIssue created by migration from https://trac.sagemath.org/ticket/8229\n\n",
    "created_at": "2010-02-10T14:31:01Z",
    "labels": [
        "component: packages",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "gap_packages-4.4.12 updated",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8229",
    "user": "https://github.com/dimpase"
}
```
Assignee: tbd

Keywords: GAP, GAP packages

I created and tested, together with the 
updated GAP to 4.4.12 --- see tickets #8150 and #8076 ---
gap_packages-4.4.12_2.spkg, that is available at 
http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
along with  http://boxen.math.washington.edu/home/dima/packages/database_gap-4.4.12.spkg and
http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg

please test these (already tested OK on x86, x86_64, ia64, and OSX PPC 10.5)
together, not forgetting to apply the patch 
track-8150 available at #8150, 
but ignoring the other (obsolete) patches there and at #8076.

This ticket is issued in addition to #8150 and #8076

Issue created by migration from https://trac.sagemath.org/ticket/8229





---

archive/issue_comments_072552.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-10T14:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72552",
    "user": "https://github.com/dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072553.json:
```json
{
    "body": "The patch 13702 from  #8076 failed to apply to 4.3.2.rc0. Is there a reason why? SHould I try 4.3.2 instead?",
    "created_at": "2010-02-10T15:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72553",
    "user": "https://github.com/wdjoyner"
}
```

The patch 13702 from  #8076 failed to apply to 4.3.2.rc0. Is there a reason why? SHould I try 4.3.2 instead?



---

archive/issue_comments_072554.json:
```json
{
    "body": "Replying to [comment:2 wdj]:\n> The patch 13702 from  #8076 failed to apply to 4.3.2.rc0. Is there a reason why? SHould I try 4.3.2 instead?\n\nThere is only one patch to apply, namely the one named trac-8150.\nThe other patches, named 13*..., are obsolete - I mention this somewhere\n(unfortunately I can't just delete these files from trac)",
    "created_at": "2010-02-10T16:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72554",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:2 wdj]:
> The patch 13702 from  #8076 failed to apply to 4.3.2.rc0. Is there a reason why? SHould I try 4.3.2 instead?

There is only one patch to apply, namely the one named trac-8150.
The other patches, named 13*..., are obsolete - I mention this somewhere
(unfortunately I can't just delete these files from trac)



---

archive/issue_comments_072555.json:
```json
{
    "body": "Replying to [comment:3 dimpase]:\n> Replying to [comment:2 wdj]:\n> > The patch 13702 from  #8076 failed to apply to 4.3.2.rc0. Is there a reason why? SHould I try 4.3.2 instead?\n> \n> There is only one patch to apply, namely the one named trac-8150.\n> The other patches, named 13*..., are obsolete - I mention this somewhere\n> (unfortunately I can't just delete these files from trac)\n\nThank you. Yes, you explained it and I misread what you wrote.\n\nI installed the patch and then gap-4.4.12 on sage-4.3.2.rc0, mac 10.6.2. This went fine.\n\nInstalling the GAP packages was a different matter:\n\n\n```\njeeves:sage-4.3.2.rc0 wdj$ ./sage -i http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg \nInstalling http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg\nCalling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg\nWarning: Attempted to overwrite SAGE_ROOT environment variable\ngap_packages-4.4.12_2\nMachine:\nDarwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386\nDeleting directories from past builds of previous/current versions of gap_packages-4.4.12_2\n/Users/wdj/sagefiles/sage-4.3.2.rc0/local/bin/sage-spkg: file gap_packages-4.4.12_2 does not exist\nAttempting to download it.\nhttp://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg --> gap_packages-4.4.12_2.spkg\n[..................................................]\nExtracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...\n-rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg\nFinished extraction\n****************************************************\nHost system\nuname -a:\nDarwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i686-apple-darwin10\nConfigured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10\nThread model: posix\ngcc version 4.2.1 (Apple Inc. build 5646) (dot 1)\n****************************************************\ngap-4.4.10.p13\n********************************************************************\nInstalling optional GAP packages, which may not be open source.\nInstalling GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. \nPlease see SPKG.txt for license details.\n********************************************************************\nmkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory\ncp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist\nError copying SPKG.txt\n\nreal    0m0.074s\nuser    0m0.008s\nsys     0m0.022s\nsage: An error occurred while installing gap_packages-4.4.12_2\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem yourself, *don't* just cd to\n/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.\nInstead, the following commands setup all environment variables\ncorrectly and load a subshell for you to debug the error:\n(cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)\nWhen you are done debugging, you can type \"exit\" to leave the\nsubshell.\n```\n\n\nDo you see what the problem is?",
    "created_at": "2010-02-10T16:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72555",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:3 dimpase]:
> Replying to [comment:2 wdj]:
> > The patch 13702 from  #8076 failed to apply to 4.3.2.rc0. Is there a reason why? SHould I try 4.3.2 instead?
> 
> There is only one patch to apply, namely the one named trac-8150.
> The other patches, named 13*..., are obsolete - I mention this somewhere
> (unfortunately I can't just delete these files from trac)

Thank you. Yes, you explained it and I misread what you wrote.

I installed the patch and then gap-4.4.12 on sage-4.3.2.rc0, mac 10.6.2. This went fine.

Installing the GAP packages was a different matter:


```
jeeves:sage-4.3.2.rc0 wdj$ ./sage -i http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
Installing http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Calling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Warning: Attempted to overwrite SAGE_ROOT environment variable
gap_packages-4.4.12_2
Machine:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
Deleting directories from past builds of previous/current versions of gap_packages-4.4.12_2
/Users/wdj/sagefiles/sage-4.3.2.rc0/local/bin/sage-spkg: file gap_packages-4.4.12_2 does not exist
Attempting to download it.
http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg --> gap_packages-4.4.12_2.spkg
[..................................................]
Extracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...
-rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg
Finished extraction
****************************************************
Host system
uname -a:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin10
Configured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5646) (dot 1)
****************************************************
gap-4.4.10.p13
********************************************************************
Installing optional GAP packages, which may not be open source.
Installing GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. 
Please see SPKG.txt for license details.
********************************************************************
mkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory
cp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist
Error copying SPKG.txt

real    0m0.074s
user    0m0.008s
sys     0m0.022s
sage: An error occurred while installing gap_packages-4.4.12_2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
```


Do you see what the problem is?



---

archive/issue_comments_072556.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n \n> Do you see what the problem is?\n\nI think you should do \nsage -f foo.spkg, \nand not \nsage -i foo.spkg\n\nit could  be that you installed gap-4.4.12.p2.spkg  using -i, and not -f,\nand this led to this problem --- the package gap did not change the version...",
    "created_at": "2010-02-10T17:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72556",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:4 wdj]:
 
> Do you see what the problem is?

I think you should do 
sage -f foo.spkg, 
and not 
sage -i foo.spkg

it could  be that you installed gap-4.4.12.p2.spkg  using -i, and not -f,
and this led to this problem --- the package gap did not change the version...



---

archive/issue_comments_072557.json:
```json
{
    "body": "I tried sage -f as well before posting the above message but didn't post the log since it was similar.\nHowever, since you asked for it, here it is!\n\n\n\n```\njeeves:sage-4.3.2.rc0 wdj$ ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg \nForce installing http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg\nCalling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg\nWarning: Attempted to overwrite SAGE_ROOT environment variable\ngap_packages-4.4.12_2\nMachine:\nDarwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386\nDeleting directories from past builds of previous/current versions of gap_packages-4.4.12_2\nExtracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...\n-rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg\nFinished extraction\n****************************************************\nHost system\nuname -a:\nDarwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i686-apple-darwin10\nConfigured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10\nThread model: posix\ngcc version 4.2.1 (Apple Inc. build 5646) (dot 1)\n****************************************************\ngap-4.4.10.p13\n********************************************************************\nInstalling optional GAP packages, which may not be open source.\nInstalling GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. \nPlease see SPKG.txt for license details.\n********************************************************************\nmkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory\ncp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist\nError copying SPKG.txt\n\nreal    0m0.027s\nuser    0m0.008s\nsys     0m0.019s\nsage: An error occurred while installing gap_packages-4.4.12_2\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem yourself, *don't* just cd to\n/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.\nInstead, the following commands setup all environment variables\ncorrectly and load a subshell for you to debug the error:\n(cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)\nWhen you are done debugging, you can type \"exit\" to leave the\nsubshell.\n```\n",
    "created_at": "2010-02-10T17:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72557",
    "user": "https://github.com/wdjoyner"
}
```

I tried sage -f as well before posting the above message but didn't post the log since it was similar.
However, since you asked for it, here it is!



```
jeeves:sage-4.3.2.rc0 wdj$ ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
Force installing http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Calling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Warning: Attempted to overwrite SAGE_ROOT environment variable
gap_packages-4.4.12_2
Machine:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
Deleting directories from past builds of previous/current versions of gap_packages-4.4.12_2
Extracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...
-rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg
Finished extraction
****************************************************
Host system
uname -a:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin10
Configured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5646) (dot 1)
****************************************************
gap-4.4.10.p13
********************************************************************
Installing optional GAP packages, which may not be open source.
Installing GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. 
Please see SPKG.txt for license details.
********************************************************************
mkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory
cp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist
Error copying SPKG.txt

real    0m0.027s
user    0m0.008s
sys     0m0.019s
sage: An error occurred while installing gap_packages-4.4.12_2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
```




---

archive/issue_comments_072558.json:
```json
{
    "body": "Replying to [comment:6 wdj]:\n> I tried sage -f as well before posting the above message but didn't post the log since it was similar.\n> However, since you asked for it, here it is!\n> \nbefore this, you should also do\nsage -f gap-4.4.12.p2.spkg    \n\nthe problem is that the version of gap package did not change, an this must be done during the installation of gap, not\nduring the installation of gap_packages",
    "created_at": "2010-02-10T22:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72558",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:6 wdj]:
> I tried sage -f as well before posting the above message but didn't post the log since it was similar.
> However, since you asked for it, here it is!
> 
before this, you should also do
sage -f gap-4.4.12.p2.spkg    

the problem is that the version of gap package did not change, an this must be done during the installation of gap, not
during the installation of gap_packages



---

archive/issue_comments_072559.json:
```json
{
    "body": "This seems reasonable. But when I did\n\n```\n ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg\n```\n\nfollowed by\n\n```\n./sage -b\n```\n\nand then\n\n```\n./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg \n```\n\nI got the same error as posted above:\n\n\n```\njeeves:sage-4.3.2.rc0 wdj$ ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg \nForce installing http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg\nCalling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg\nWarning: Attempted to overwrite SAGE_ROOT environment variable\ngap_packages-4.4.12_2\nMachine:\nDarwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386\nDeleting directories from past builds of previous/current versions of gap_packages-4.4.12_2\nExtracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...\n-rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg\nFinished extraction\n****************************************************\nHost system\nuname -a:\nDarwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i686-apple-darwin10\nConfigured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10\nThread model: posix\ngcc version 4.2.1 (Apple Inc. build 5646) (dot 1)\n****************************************************\ngap-4.4.10.p13\n********************************************************************\nInstalling optional GAP packages, which may not be open source.\nInstalling GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. \nPlease see SPKG.txt for license details.\n********************************************************************\nmkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory\ncp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist\nError copying SPKG.txt\n\nreal    0m0.032s\nuser    0m0.008s\nsys     0m0.020s\nsage: An error occurred while installing gap_packages-4.4.12_2\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem yourself, *don't* just cd to\n/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.\nInstead, the following commands setup all environment variables\ncorrectly and load a subshell for you to debug the error:\n(cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)\nWhen you are done debugging, you can type \"exit\" to leave the\nsubshell.\n```\n\n\nMoreover,\n\n\n```\njeeves:sage-4.3.2.rc0 wdj$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nLoading Sage library. Current Mercurial branch is: 6229-gap\nsage: gap_version()\n'4.4.12'\n```\n\nso sage thinks it is running gap-4.4.12.",
    "created_at": "2010-02-10T23:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72559",
    "user": "https://github.com/wdjoyner"
}
```

This seems reasonable. But when I did

```
 ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg
```

followed by

```
./sage -b
```

and then

```
./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
```

I got the same error as posted above:


```
jeeves:sage-4.3.2.rc0 wdj$ ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
Force installing http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Calling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Warning: Attempted to overwrite SAGE_ROOT environment variable
gap_packages-4.4.12_2
Machine:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
Deleting directories from past builds of previous/current versions of gap_packages-4.4.12_2
Extracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...
-rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg
Finished extraction
****************************************************
Host system
uname -a:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin10
Configured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5646) (dot 1)
****************************************************
gap-4.4.10.p13
********************************************************************
Installing optional GAP packages, which may not be open source.
Installing GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. 
Please see SPKG.txt for license details.
********************************************************************
mkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory
cp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist
Error copying SPKG.txt

real    0m0.032s
user    0m0.008s
sys     0m0.020s
sage: An error occurred while installing gap_packages-4.4.12_2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
```


Moreover,


```
jeeves:sage-4.3.2.rc0 wdj$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: 6229-gap
sage: gap_version()
'4.4.12'
```

so sage thinks it is running gap-4.4.12.



---

archive/issue_comments_072560.json:
```json
{
    "body": "Replying to [comment:8 wdj]:\n> This seems reasonable. But when I did\n> {{{\n>  ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg\n> }}}\n> followed by\n> {{{\n> ./sage -b\n> }}}\n> and then\n> {{{\n> ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg \n> }}}\n> I got the same error as posted above:\n> \n> {{{\n> jeeves:sage-4.3.2.rc0 wdj$ ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg \n> Force installing http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg\n> Calling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg\n> Warning: Attempted to overwrite SAGE_ROOT environment variable\n> gap_packages-4.4.12_2\n> Machine:\n> Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386\n> Deleting directories from past builds of previous/current versions of gap_packages-4.4.12_2\n> Extracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...\n> -rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg\n> Finished extraction\n> ****************************************************\n> Host system\n> uname -a:\n> Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386\n> ****************************************************\n> ****************************************************\n> CC Version\n> gcc -v\n> Using built-in specs.\n> Target: i686-apple-darwin10\n> Configured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/<sup>[cg][</sup>.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10\n> Thread model: posix\n> gcc version 4.2.1 (Apple Inc. build 5646) (dot 1)\n> ****************************************************\n> gap-4.4.10.p13\n> ********************************************************************\n> Installing optional GAP packages, which may not be open source.\n> Installing GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. \n> Please see SPKG.txt for license details.\n> ********************************************************************\n> mkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory\n> cp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist\n> Error copying SPKG.txt\n> \n> real    0m0.032s\n> user    0m0.008s\n> sys     0m0.020s\n> sage: An error occurred while installing gap_packages-4.4.12_2\n> Please email sage-devel http://groups.google.com/group/sage-devel\n> explaining the problem and send the relevant part of\n> of /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.\n> If you want to try to fix the problem yourself, *don't* just cd to\n> /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.\n> Instead, the following commands setup all environment variables\n> correctly and load a subshell for you to debug the error:\n> (cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)\n> When you are done debugging, you can type \"exit\" to leave the\n> subshell.\n> }}}\n> \n> Moreover,\n> \n> {{{\n> jeeves:sage-4.3.2.rc0 wdj$ ./sage\n> ----------------------------------------------------------------------\n> | Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |\n> | Type notebook() for the GUI, and license() for information.        |\n> ----------------------------------------------------------------------\n> **********************************************************************\n> *                                                                    *\n> * Warning: this is a prerelease version, and it may be unstable.     *\n> *                                                                    *\n> **********************************************************************\n> Loading Sage library. Current Mercurial branch is: 6229-gap\n> sage: gap_version()\n> '4.4.12'\n> }}}\n> so sage thinks it is running gap-4.4.12.\n\nI am unable reproduce this. \nCould you please  install a fresh sage-4.3.2  from source and then \ndo the above?\nThis worked on 5 different machines (well, not on OSX 10.6 Intel, but, in particular, on OSX 10.5 PPC).",
    "created_at": "2010-02-11T00:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72560",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:8 wdj]:
> This seems reasonable. But when I did
> {{{
>  ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg
> }}}
> followed by
> {{{
> ./sage -b
> }}}
> and then
> {{{
> ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
> }}}
> I got the same error as posted above:
> 
> {{{
> jeeves:sage-4.3.2.rc0 wdj$ ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
> Force installing http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
> Calling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
> Warning: Attempted to overwrite SAGE_ROOT environment variable
> gap_packages-4.4.12_2
> Machine:
> Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
> Deleting directories from past builds of previous/current versions of gap_packages-4.4.12_2
> Extracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...
> -rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg
> Finished extraction
> ****************************************************
> Host system
> uname -a:
> Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
> ****************************************************
> ****************************************************
> CC Version
> gcc -v
> Using built-in specs.
> Target: i686-apple-darwin10
> Configured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/<sup>[cg][</sup>.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10
> Thread model: posix
> gcc version 4.2.1 (Apple Inc. build 5646) (dot 1)
> ****************************************************
> gap-4.4.10.p13
> ********************************************************************
> Installing optional GAP packages, which may not be open source.
> Installing GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. 
> Please see SPKG.txt for license details.
> ********************************************************************
> mkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory
> cp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist
> Error copying SPKG.txt
> 
> real    0m0.032s
> user    0m0.008s
> sys     0m0.020s
> sage: An error occurred while installing gap_packages-4.4.12_2
> Please email sage-devel http://groups.google.com/group/sage-devel
> explaining the problem and send the relevant part of
> of /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.
> If you want to try to fix the problem yourself, *don't* just cd to
> /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.
> Instead, the following commands setup all environment variables
> correctly and load a subshell for you to debug the error:
> (cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)
> When you are done debugging, you can type "exit" to leave the
> subshell.
> }}}
> 
> Moreover,
> 
> {{{
> jeeves:sage-4.3.2.rc0 wdj$ ./sage
> ----------------------------------------------------------------------
> | Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> **********************************************************************
> *                                                                    *
> * Warning: this is a prerelease version, and it may be unstable.     *
> *                                                                    *
> **********************************************************************
> Loading Sage library. Current Mercurial branch is: 6229-gap
> sage: gap_version()
> '4.4.12'
> }}}
> so sage thinks it is running gap-4.4.12.

I am unable reproduce this. 
Could you please  install a fresh sage-4.3.2  from source and then 
do the above?
This worked on 5 different machines (well, not on OSX 10.6 Intel, but, in particular, on OSX 10.5 PPC).



---

archive/issue_comments_072561.json:
```json
{
    "body": "Replying to [comment:8 wdj]:\n\nI insist on a clean install, in another directory, as it seems that you have different instances of Sage lying around in the same directory, one clone of another, one still with gap-4.4.10, another \"updated\" to 4.4.12, and they appear to interfere with each other in some way.",
    "created_at": "2010-02-11T01:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72561",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:8 wdj]:

I insist on a clean install, in another directory, as it seems that you have different instances of Sage lying around in the same directory, one clone of another, one still with gap-4.4.10, another "updated" to 4.4.12, and they appear to interfere with each other in some way.



---

archive/issue_comments_072562.json:
```json
{
    "body": "I did it again on a fresh install. Same problem.",
    "created_at": "2010-02-11T02:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72562",
    "user": "https://github.com/wdjoyner"
}
```

I did it again on a fresh install. Same problem.



---

archive/issue_comments_072563.json:
```json
{
    "body": "Replying to [comment:11 wdj]:\n> I did it again on a fresh install. Same problem.\nomg...\n\nrename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg\n(I normally just erase them, so perhaps this might be the root of the problem for you)\n\nthen redo all the package installs:\nsage -f gap*...\n\nit can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage\n\nFailing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.",
    "created_at": "2010-02-11T02:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72563",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:11 wdj]:
> I did it again on a fresh install. Same problem.
omg...

rename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg
(I normally just erase them, so perhaps this might be the root of the problem for you)

then redo all the package installs:
sage -f gap*...

it can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage

Failing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.



---

archive/issue_comments_072564.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-11T02:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72564",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072565.json:
```json
{
    "body": "Replying to [comment:12 dimpase]:\n> Replying to [comment:11 wdj]:\n> > I did it again on a fresh install. Same problem.\n> omg...\n> \n> rename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg\n> (I normally just erase them, so perhaps this might be the root of the problem for you)\n\n\n???!!!!\nThis is not the correct way to build a package!\n\n\n> \n> then redo all the package installs:\n> sage -f gap*...\n> \n> it can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage\n> \n> Failing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.\n> \n\n\nI have tried your instructions on two different macs (both running 4.3.2 and 10.6.2) and a linux machine (running ubuntu 9.10).\nSame error on all machines. There is something wrong with\n\n(1) make clone\n(2) apply trac-8150\n(3) sage -f gap-4.4.12\n(4) sage -f gap_packages.\n\nThe last step is where the error occurs on every machine.\n\nAs far as I know, this is the way it is *supposed* to work. \n\nTo be as clear as I can, you are *not* supposed to ask people to delete gap-4.4.10 manually at any stage of the install. Maybe if this is not clear, it should be moved to sage-support or sage-devel?\n\nI am marking this as needs work.",
    "created_at": "2010-02-11T02:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72565",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:12 dimpase]:
> Replying to [comment:11 wdj]:
> > I did it again on a fresh install. Same problem.
> omg...
> 
> rename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg
> (I normally just erase them, so perhaps this might be the root of the problem for you)


???!!!!
This is not the correct way to build a package!


> 
> then redo all the package installs:
> sage -f gap*...
> 
> it can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage
> 
> Failing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.
> 


I have tried your instructions on two different macs (both running 4.3.2 and 10.6.2) and a linux machine (running ubuntu 9.10).
Same error on all machines. There is something wrong with

(1) make clone
(2) apply trac-8150
(3) sage -f gap-4.4.12
(4) sage -f gap_packages.

The last step is where the error occurs on every machine.

As far as I know, this is the way it is *supposed* to work. 

To be as clear as I can, you are *not* supposed to ask people to delete gap-4.4.10 manually at any stage of the install. Maybe if this is not clear, it should be moved to sage-support or sage-devel?

I am marking this as needs work.



---

archive/issue_comments_072566.json:
```json
{
    "body": "Replying to [comment:13 wdj]:\n\n\nI do not know what happens to the \n> Replying to [comment:12 dimpase]:\n> > Replying to [comment:11 wdj]:\n> > > I did it again on a fresh install. Same problem.\n> > omg...\n> > \n> > rename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg\n> > (I normally just erase them, so perhaps this might be the root of the problem for you)\n> \n> \n> ???!!!!\n> This is not the correct way to build a package!\n> \n> \n> > \n> > then redo all the package installs:\n> > sage -f gap*...\n> > \n> > it can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage\n> > \n> > Failing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.\n> > \n> \n> \n> I have tried your instructions on two different macs (both running 4.3.2 and 10.6.2) and a linux machine (running ubuntu 9.10).\n> Same error on all machines. There is something wrong with\n> \n> (1) make clone\n\nSorry, but I asked you to do it on a *clean install*, not on a clone...\n\n> (2) apply trac-8150\n> (3) sage -f gap-4.4.12\n> (4) sage -f gap_packages.\n> \n> The last step is where the error occurs on every machine.\n> \n> As far as I know, this is the way it is *supposed* to work. \n> \n> To be as clear as I can, you are *not* supposed to ask people to delete gap-4.4.10 manually at any stage of the install. Maybe if this is not clear, it should be moved to sage-support or sage-devel?\n> \n> I am marking this as needs work.",
    "created_at": "2010-02-11T02:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72566",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:13 wdj]:


I do not know what happens to the 
> Replying to [comment:12 dimpase]:
> > Replying to [comment:11 wdj]:
> > > I did it again on a fresh install. Same problem.
> > omg...
> > 
> > rename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg
> > (I normally just erase them, so perhaps this might be the root of the problem for you)
> 
> 
> ???!!!!
> This is not the correct way to build a package!
> 
> 
> > 
> > then redo all the package installs:
> > sage -f gap*...
> > 
> > it can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage
> > 
> > Failing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.
> > 
> 
> 
> I have tried your instructions on two different macs (both running 4.3.2 and 10.6.2) and a linux machine (running ubuntu 9.10).
> Same error on all machines. There is something wrong with
> 
> (1) make clone

Sorry, but I asked you to do it on a *clean install*, not on a clone...

> (2) apply trac-8150
> (3) sage -f gap-4.4.12
> (4) sage -f gap_packages.
> 
> The last step is where the error occurs on every machine.
> 
> As far as I know, this is the way it is *supposed* to work. 
> 
> To be as clear as I can, you are *not* supposed to ask people to delete gap-4.4.10 manually at any stage of the install. Maybe if this is not clear, it should be moved to sage-support or sage-devel?
> 
> I am marking this as needs work.



---

archive/issue_comments_072567.json:
```json
{
    "body": "Replying to [comment:13 wdj]:\n\nOK, I can reproduce your problem. Namely, I see this behaviour if I try to upgrade\na binary distribution of 4.3.2 (just tried it on boxen, and saw exactly the same thing as you did). But, I swear, it does work on a distribution built from source,\neven if I compile gap 4.4.10 and its packages in, and then do the regular upgrade\nwith -f, without removing old spkgs, it all goes smoothly.\n\nBut this is not a problem of our new packages, IMHO. At worst it would mean that 4.4.12 will not be compatible with older sage releases.\n\n\n> Replying to [comment:12 dimpase]:\n> > Replying to [comment:11 wdj]:\n> > > I did it again on a fresh install. Same problem.\n> > omg...\n> > \n> > rename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg\n> > (I normally just erase them, so perhaps this might be the root of the problem for you)\n> \n> \n> ???!!!!\n> This is not the correct way to build a package!\n\nWell, we were debugging a problem, OK? :-)\n\nWe need to understand how you get that 4.4.10 gets back at you\non a binary distro.\n\nWhen I said \"a fresh install\" I really meant it, not a clone...\n(cp -a <your-sageroot> <newsageroot> will do the job, but sage -clone won't !)\nMay I humbly request that you create a really new 4.3.2 install,\nfrom source (a binary download would NOT work --- I do not know why, but this is not the place fix this bug or feature --- I'll ask on sage-devel), \nand try the packages there.\nThanks in advance. \n \n> \n> \n> > \n> > then redo all the package installs:\n> > sage -f gap*...\n> > \n> > it can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage\n> > \n> > Failing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.\n> > \n> \n> \n> I have tried your instructions on two different macs (both running 4.3.2 and 10.6.2) and a linux machine (running ubuntu 9.10).\n> Same error on all machines. There is something wrong with\n> \n> (1) make clone\n> (2) apply trac-8150\n> (3) sage -f gap-4.4.12\n> (4) sage -f gap_packages.\n> \n> The last step is where the error occurs on every machine.\n\n\n> \n> As far as I know, this is the way it is *supposed* to work. \n> \n> To be as clear as I can, you are *not* supposed to ask people to delete gap-4.4.10 manually at any stage of the install. Maybe if this is not clear, it should be moved to sage-support or sage-devel?\n> \n> I am marking this as needs work.",
    "created_at": "2010-02-11T04:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72567",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:13 wdj]:

OK, I can reproduce your problem. Namely, I see this behaviour if I try to upgrade
a binary distribution of 4.3.2 (just tried it on boxen, and saw exactly the same thing as you did). But, I swear, it does work on a distribution built from source,
even if I compile gap 4.4.10 and its packages in, and then do the regular upgrade
with -f, without removing old spkgs, it all goes smoothly.

But this is not a problem of our new packages, IMHO. At worst it would mean that 4.4.12 will not be compatible with older sage releases.


> Replying to [comment:12 dimpase]:
> > Replying to [comment:11 wdj]:
> > > I did it again on a fresh install. Same problem.
> > omg...
> > 
> > rename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg
> > (I normally just erase them, so perhaps this might be the root of the problem for you)
> 
> 
> ???!!!!
> This is not the correct way to build a package!

Well, we were debugging a problem, OK? :-)

We need to understand how you get that 4.4.10 gets back at you
on a binary distro.

When I said "a fresh install" I really meant it, not a clone...
(cp -a <your-sageroot> <newsageroot> will do the job, but sage -clone won't !)
May I humbly request that you create a really new 4.3.2 install,
from source (a binary download would NOT work --- I do not know why, but this is not the place fix this bug or feature --- I'll ask on sage-devel), 
and try the packages there.
Thanks in advance. 
 
> 
> 
> > 
> > then redo all the package installs:
> > sage -f gap*...
> > 
> > it can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage
> > 
> > Failing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.
> > 
> 
> 
> I have tried your instructions on two different macs (both running 4.3.2 and 10.6.2) and a linux machine (running ubuntu 9.10).
> Same error on all machines. There is something wrong with
> 
> (1) make clone
> (2) apply trac-8150
> (3) sage -f gap-4.4.12
> (4) sage -f gap_packages.
> 
> The last step is where the error occurs on every machine.


> 
> As far as I know, this is the way it is *supposed* to work. 
> 
> To be as clear as I can, you are *not* supposed to ask people to delete gap-4.4.10 manually at any stage of the install. Maybe if this is not clear, it should be moved to sage-support or sage-devel?
> 
> I am marking this as needs work.



---

archive/issue_comments_072568.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-11T04:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72568",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072569.json:
```json
{
    "body": "Replying to [comment:15 dimpase]:\nI found where the problem lies: when you upgrade gap_packages,\nthe file gap-4.4.12.p2.spkg must be physically present in spkg/standard\n\nIf it is there, I can do sage -f gap_packages-...spkg\njust fine.\nThe file names are used by the script  spkg/standard/newest_version\nto get the version of the installed package.\n\nThis script is called in spkg-install of gap_packages spkg.\n\nSo it would not work if you do \nspkg -f http://....gap-4.4.12.p2.spkg\ninstead.\n\nThis is not our bug, I think. (spkg/standard/newest_version is a standard thing...)",
    "created_at": "2010-02-11T05:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72569",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:15 dimpase]:
I found where the problem lies: when you upgrade gap_packages,
the file gap-4.4.12.p2.spkg must be physically present in spkg/standard

If it is there, I can do sage -f gap_packages-...spkg
just fine.
The file names are used by the script  spkg/standard/newest_version
to get the version of the installed package.

This script is called in spkg-install of gap_packages spkg.

So it would not work if you do 
spkg -f http://....gap-4.4.12.p2.spkg
instead.

This is not our bug, I think. (spkg/standard/newest_version is a standard thing...)



---

archive/issue_comments_072570.json:
```json
{
    "body": "Okay, modulo the sage -f bug reported in http://trac.sagemath.org/sage_trac/ticket/8236, here is what I have done.\n\nOn a mac 10.6.2 machine running sage 4.3.2, I applied trac-8150, then sage -f gap-4.4.12, then sage -f gap_packages, then sage -f database_gap, as indicated in the instructions above. All went fine and sage -testall passes. I then ran sage -testall --optional. I could see only one related failure and it might or might not be minor. Apparently when the new gap_packages skpg was built, it was not set to compile and install the guava C code written by J Leon. This caused 2 failures. When I compiled the code (the traceback tells you how), that test passed. I tested the packages with some random GAP commands and everything else seems to be installed and working fine.\n\nIf this trac ticket is to judge only gap-4.4.12, then I give it a positive review. If it is to also include gap_packages then maybe I have some reservations (database_gap seems fine though). Since gap_packages is in the title of the ticket, I am hesitant to give this a positive review yet. I don't know if Leon's code is so old that it will not compile on some machines, in which case this is not a problem for this ticket. So, I am marking this as needs info.",
    "created_at": "2010-02-11T17:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72570",
    "user": "https://github.com/wdjoyner"
}
```

Okay, modulo the sage -f bug reported in http://trac.sagemath.org/sage_trac/ticket/8236, here is what I have done.

On a mac 10.6.2 machine running sage 4.3.2, I applied trac-8150, then sage -f gap-4.4.12, then sage -f gap_packages, then sage -f database_gap, as indicated in the instructions above. All went fine and sage -testall passes. I then ran sage -testall --optional. I could see only one related failure and it might or might not be minor. Apparently when the new gap_packages skpg was built, it was not set to compile and install the guava C code written by J Leon. This caused 2 failures. When I compiled the code (the traceback tells you how), that test passed. I tested the packages with some random GAP commands and everything else seems to be installed and working fine.

If this trac ticket is to judge only gap-4.4.12, then I give it a positive review. If it is to also include gap_packages then maybe I have some reservations (database_gap seems fine though). Since gap_packages is in the title of the ticket, I am hesitant to give this a positive review yet. I don't know if Leon's code is so old that it will not compile on some machines, in which case this is not a problem for this ticket. So, I am marking this as needs info.



---

archive/issue_comments_072571.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-11T17:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72571",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_072572.json:
```json
{
    "body": "Replying to [comment:18 wdj]:\n\nThanks!\n\ncould you please meanwhile give the positive review to \n#8076 - i.e. to the ticket on the gap-4.4.12 spkg?\n\nI suppose Leon's code is also in 4.4.10, so there should be no problem\nwith also compiling it on 4.4.12. I'll add this to spkg-install later today...\n\ndatabase_gap is just a copy you your latest 4.4.12 spkg, unless I forgot\nsomething... As far as I recall, no updates were necessary.\n\n\n\n\n> Okay, modulo the sage -f bug reported in http://trac.sagemath.org/sage_trac/ticket/8236, here is what I have done.\n> \n> On a mac 10.6.2 machine running sage 4.3.2, I applied trac-8150, then sage -f gap-4.4.12, then sage -f gap_packages, then sage -f database_gap, as indicated in the instructions above. All went fine and sage -testall passes. I then ran sage -testall --optional. I could see only one related failure and it might or might not be minor. Apparently when the new gap_packages skpg was built, it was not set to compile and install the guava C code written by J Leon. This caused 2 failures. When I compiled the code (the traceback tells you how), that test passed. I tested the packages with some random GAP commands and everything else seems to be installed and working fine.\n> \n> If this trac ticket is to judge only gap-4.4.12, then I give it a positive review. If it is to also include gap_packages then maybe I have some reservations (database_gap seems fine though). Since gap_packages is in the title of the ticket, I am hesitant to give this a positive review yet. I don't know if Leon's code is so old that it will not compile on some machines, in which case this is not a problem for this ticket. So, I am marking this as needs info.\n> \n> \n>",
    "created_at": "2010-02-12T10:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72572",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:18 wdj]:

Thanks!

could you please meanwhile give the positive review to 
#8076 - i.e. to the ticket on the gap-4.4.12 spkg?

I suppose Leon's code is also in 4.4.10, so there should be no problem
with also compiling it on 4.4.12. I'll add this to spkg-install later today...

database_gap is just a copy you your latest 4.4.12 spkg, unless I forgot
something... As far as I recall, no updates were necessary.




> Okay, modulo the sage -f bug reported in http://trac.sagemath.org/sage_trac/ticket/8236, here is what I have done.
> 
> On a mac 10.6.2 machine running sage 4.3.2, I applied trac-8150, then sage -f gap-4.4.12, then sage -f gap_packages, then sage -f database_gap, as indicated in the instructions above. All went fine and sage -testall passes. I then ran sage -testall --optional. I could see only one related failure and it might or might not be minor. Apparently when the new gap_packages skpg was built, it was not set to compile and install the guava C code written by J Leon. This caused 2 failures. When I compiled the code (the traceback tells you how), that test passed. I tested the packages with some random GAP commands and everything else seems to be installed and working fine.
> 
> If this trac ticket is to judge only gap-4.4.12, then I give it a positive review. If it is to also include gap_packages then maybe I have some reservations (database_gap seems fine though). Since gap_packages is in the title of the ticket, I am hesitant to give this a positive review yet. I don't know if Leon's code is so old that it will not compile on some machines, in which case this is not a problem for this ticket. So, I am marking this as needs info.
> 
> 
>



---

archive/issue_comments_072573.json:
```json
{
    "body": "Replying to [comment:19 dimpase]:\n \n> I suppose Leon's code is also in 4.4.10, so there should be no problem\n> with also compiling it on 4.4.12. I'll add this to spkg-install later today...\n> \n\nIn 4.4.10 Leon's code was compiled in gap spkg, not in gap_packages spkg.\nSo, when you created 1st versions of 4.4.12-spkg's, you (rightly) took out this compilation from gap spkg, but did not add it in  gap_packages spkg.\nThat's why it's missing at the moment.\nI will add it to gap_packages spkg.",
    "created_at": "2010-02-14T04:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72573",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:19 dimpase]:
 
> I suppose Leon's code is also in 4.4.10, so there should be no problem
> with also compiling it on 4.4.12. I'll add this to spkg-install later today...
> 

In 4.4.10 Leon's code was compiled in gap spkg, not in gap_packages spkg.
So, when you created 1st versions of 4.4.12-spkg's, you (rightly) took out this compilation from gap spkg, but did not add it in  gap_packages spkg.
That's why it's missing at the moment.
I will add it to gap_packages spkg.



---

archive/issue_comments_072574.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-14T06:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72574",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_072575.json:
```json
{
    "body": "Replying to [comment:18 wdj]:\n\nThere was a trivial typo in spkg-install that prevented all \nof guava from being compiled.\nI fixed it, and put the new version of the spkg here\n[http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg)\nPlease reinstall and test the relevant part.\nI tested on Linux that -t -optional passes on sage/coding/ after this fix.\nThanks,\nDima\n\n\n> Okay, modulo the sage -f bug reported in http://trac.sagemath.org/sage_trac/ticket/8236, here is what I have done.\n> \n> On a mac 10.6.2 machine running sage 4.3.2, I applied trac-8150, then sage -f gap-4.4.12, then sage -f gap_packages, then sage -f database_gap, as indicated in the instructions above. All went fine and sage -testall passes. I then ran sage -testall --optional. I could see only one related failure and it might or might not be minor. Apparently when the new gap_packages skpg was built, it was not set to compile and install the guava C code written by J Leon. This caused 2 failures. When I compiled the code (the traceback tells you how), that test passed. I tested the packages with some random GAP commands and everything else seems to be installed and working fine.\n> \n> If this trac ticket is to judge only gap-4.4.12, then I give it a positive review. If it is to also include gap_packages then maybe I have some reservations (database_gap seems fine though). Since gap_packages is in the title of the ticket, I am hesitant to give this a positive review yet. I don't know if Leon's code is so old that it will not compile on some machines, in which case this is not a problem for this ticket. So, I am marking this as needs info.\n> \n> \n>",
    "created_at": "2010-02-14T06:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72575",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:18 wdj]:

There was a trivial typo in spkg-install that prevented all 
of guava from being compiled.
I fixed it, and put the new version of the spkg here
[http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg)
Please reinstall and test the relevant part.
I tested on Linux that -t -optional passes on sage/coding/ after this fix.
Thanks,
Dima


> Okay, modulo the sage -f bug reported in http://trac.sagemath.org/sage_trac/ticket/8236, here is what I have done.
> 
> On a mac 10.6.2 machine running sage 4.3.2, I applied trac-8150, then sage -f gap-4.4.12, then sage -f gap_packages, then sage -f database_gap, as indicated in the instructions above. All went fine and sage -testall passes. I then ran sage -testall --optional. I could see only one related failure and it might or might not be minor. Apparently when the new gap_packages skpg was built, it was not set to compile and install the guava C code written by J Leon. This caused 2 failures. When I compiled the code (the traceback tells you how), that test passed. I tested the packages with some random GAP commands and everything else seems to be installed and working fine.
> 
> If this trac ticket is to judge only gap-4.4.12, then I give it a positive review. If it is to also include gap_packages then maybe I have some reservations (database_gap seems fine though). Since gap_packages is in the title of the ticket, I am hesitant to give this a positive review yet. I don't know if Leon's code is so old that it will not compile on some machines, in which case this is not a problem for this ticket. So, I am marking this as needs info.
> 
> 
>



---

archive/issue_comments_072576.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-14T12:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72576",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072577.json:
```json
{
    "body": "The binary from Leon's code did not compile for me the first time (installing via the internet). Then I downloaded the spkg and installed using sage -f and it worked. The sage -t --optional from last time passes now.\n\nI'm a little bit curious as to why I had to install it twice, though I think this should get a positive review since it seems that the package is fine but the internet installation method is not working as I expected. (BTW, my mac asks me before opening a file downloaded from the internet - I wonder if that is an issue?)\n\nStill, thanks very much Dima.",
    "created_at": "2010-02-14T12:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72577",
    "user": "https://github.com/wdjoyner"
}
```

The binary from Leon's code did not compile for me the first time (installing via the internet). Then I downloaded the spkg and installed using sage -f and it worked. The sage -t --optional from last time passes now.

I'm a little bit curious as to why I had to install it twice, though I think this should get a positive review since it seems that the package is fine but the internet installation method is not working as I expected. (BTW, my mac asks me before opening a file downloaded from the internet - I wonder if that is an issue?)

Still, thanks very much Dima.



---

archive/issue_comments_072578.json:
```json
{
    "body": "Changing component from packages to optional packages.",
    "created_at": "2010-02-17T05:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72578",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from packages to optional packages.



---

archive/issue_events_008430.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-02-17T21:23:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8229#event-8430"
}
```



---

archive/issue_comments_072579.json:
```json
{
    "body": "Merged [gap_packages-4.4.12_2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg) in the optional spkg repository. See\n\nhttp://www.sagemath.org/packages/optional/",
    "created_at": "2010-02-17T21:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72579",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [gap_packages-4.4.12_2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg) in the optional spkg repository. See

http://www.sagemath.org/packages/optional/



---

archive/issue_comments_072580.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T21:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8229#issuecomment-72580",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
