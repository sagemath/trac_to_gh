# Issue 9264: Apply ALL relevent fixes to ECL 10.4.1

archive/issues_009264.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  was jhpalmieri mpatel leif jsp jason vbraun jdemeyer\n\nThere are a number of tickets active at the minute with patches to ECL\n\n* #8808\n* #9187\n* #8951\n* #8089\n\nnone have been merged, but the patches are not consistent across all or them. \n\n* The option --with-dffi=no  from #8089 has not been been missed which is very important. \n* Some other less important changes (such as removing an inaccurate, but innocuous mention of building a 32-bit version) are removed. \n* There is a 10.4.1.p0 package, despite no 10.4.1 has actually been merged. \n\nThe aim of this ticket is to update to the 10.4.1 source code, whilst ensuring all the relevant patches are applied. \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9264\n\n",
    "created_at": "2010-06-18T12:16:14Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Apply ALL relevent fixes to ECL 10.4.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9264",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  was jhpalmieri mpatel leif jsp jason vbraun jdemeyer

There are a number of tickets active at the minute with patches to ECL

* #8808
* #9187
* #8951
* #8089

none have been merged, but the patches are not consistent across all or them. 

* The option --with-dffi=no  from #8089 has not been been missed which is very important. 
* Some other less important changes (such as removing an inaccurate, but innocuous mention of building a 32-bit version) are removed. 
* There is a 10.4.1.p0 package, despite no 10.4.1 has actually been merged. 

The aim of this ticket is to update to the 10.4.1 source code, whilst ensuring all the relevant patches are applied. 

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9264





---

archive/issue_comments_087178.json:
```json
{
    "body": "Your best chance is to see if you can give a positive review to\n#8645. The maxima spkg there:\n\n```\nhttp://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg\n```\n\nis the same maxima that is in sage now, with minimal changes applied to let maxima build under ECL 10.4.1.\n\nIf maxima.5.20.1.p1 on ecl.10.4.1 needs work, we might as well wait until maxima.5.21 is ready to be merged, because then the problem is ecl.10.4.1.\n\nWhen I tried, I couldn't get maxima to build properly under ecl.10.2 (its \"ASDF\" is too buggy)",
    "created_at": "2010-06-18T16:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87178",
    "user": "nbruin"
}
```

Your best chance is to see if you can give a positive review to
#8645. The maxima spkg there:

```
http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg
```

is the same maxima that is in sage now, with minimal changes applied to let maxima build under ECL 10.4.1.

If maxima.5.20.1.p1 on ecl.10.4.1 needs work, we might as well wait until maxima.5.21 is ready to be merged, because then the problem is ecl.10.4.1.

When I tried, I couldn't get maxima to build properly under ecl.10.2 (its "ASDF" is too buggy)



---

archive/issue_comments_087179.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-19T19:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87179",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087180.json:
```json
{
    "body": "I've created a new ECL package\n\nhttp://boxen.math.washington.edu/home/kirkby/revised-patches/ecl-10.4.1.spkg\n\nwhich has the following fixes applied:\n\n* Updates ECL to the latest upstream, 10.4.1\n* Applies a fix to stop ECL building in parallel, which is ticket #9187. This already has positive review. \n* Applies the fix from #8089 to disable the dynamic foreign function interface as advised by the ECL developer. This disables the use of assembly code on OpenSolaris x64, but no other platform.\n* Removes files from /tmp/ECL* as soon as they are no longer needed, as failure to do so can present problems on multi-user systems. \n\nAll changes have been checked with #8645, which has a change to Maxima which allows Maxima to build with the latest ECL. The patch on #8645 does **not** update Maxima to the latest version, as that creates problems which are non-trivial to solve. It does however fix a problem with Maxima not installing the library properly, and allows Maxima to build with the latest ECL>\n\nAs such, the attached ticket:\n \n* Allows Maxima to build the library properly whilst still working with the latest ECL. \n* Remove unwanted ECL tmp files. \n* Allows spkgs to build in parallel\n* Allow ECL to build on OpenSolaris x64. \n\nHere are the test results:\n\n == Testing on Solaris 10 SPARC in 32-bit mode. ==\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler) \n* Sage 4.4.4.alpha1\n\n\n```\n\tdone\nfor i in Copyright LGPL; do \\\n\t  /usr/bin/ginstall -c -m 644 /export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/ecl-10.4.1/src/src/../$i /export/home/drkirkby/sage-4.4.4.alpha1/local/lib/; \\\n\tdone\n/bin/sh /export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/ecl-10.4.1/src/src/gc/mkinstalldirs /export/home/drkirkby/sage-4.4.4.alpha1/local/share/man/man1\nfor i in doc/ecl.man doc/ecl-config.man; do \\\n\t    /usr/bin/ginstall -c -m 644 $i /export/home/drkirkby/sage-4.4.4.alpha1/local/share/man/man1/ecl.1; \\\n\tdone\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/ecl-10.4.1/src/build'\n\nreal\t1m26.075s\nuser\t1m17.655s\nsys\t0m7.531s\nSuccessfully installed ecl-10.4.1\n```\n \n\nHere is the Maxima 5.20.1.p1 installation from #8645\n\n\n```\ninstalling Maxima library as /export/home/drkirkby/sage-4.4.4.alpha1/local/lib/ecl//maxima.fas\n\nreal    22m32.432s\nuser    19m9.372s\nsys     2m51.674s\nSuccessfully installed maxima-5.20.1.p1\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/maxima-5.20.1.p1\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing maxima-5.20.1.p1.spkg\ndrkirkby@redstart:~/sage-4.4.4.alpha1$ \n```\n\n\n == Testing on OpenSolaris x64 06/2009 64-bit mode. ==\n* Sun Ultra 27\n* 2 x 3.33 GHz quad core Intel Xeon MHz\n* 12 GB RAM\n* OpenSolaris 06/2009 (Last release of OpenSolaris, updated to build 134)\n* gcc 4.4.4 (uses Sun linker and GNU assembler) \n* Sage 4.4.4.alpha1\n\n\n```\n/bin/sh /export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/ecl-10.4.1/src/src/gc/mkinstalldirs /export/home/drkirkby/sage-4.4.4.alpha1/local/share/man/man1\nfor i in doc/ecl.man doc/ecl-config.man; do \\\n\t    /usr/bin/ginstall -c -m 644 $i /export/home/drkirkby/sage-4.4.4.alpha1/local/share/man/man1/ecl.1; \\\n\tdone\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/ecl-10.4.1/src/build'\n\nreal\t1m26.075s\nuser\t1m17.655s\nsys\t0m7.531s\nSuccessfully installed ecl-10.4.1\n```\n\n\nMaxima 5.20.1.p1 will **not** build on this platform, but such a problem is not related to this ticket, and appears it might be an incorrect flag given in the source (-Wl,-G instead of -shared). This is documented at #9099\n\n## Testing on sage.math (Linux), 64-bit.\n\n```\nn/man1/ecl.1; \\\n\tdone\nmake[1]: Leaving directory `/home/kirkby/sage-4.4.3/spkg/build/ecl-10.4.1/src/build'\n\nreal\t2m16.904s\nuser\t1m44.990s\nsys\t0m14.980s\nSuccessfully installed ecl-10.4.1\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing ecl-10.4.1.spkg\n```\n\n\nWe can also see Maxima, and the library are ok now. \n\n\n```\n;;; \ninstalling Maxima library as /home/kirkby/sage-4.4.3/local/lib/ecl//maxima.fas\n\nreal\t4m41.594s\nuser\t3m14.160s\nsys\t0m46.000s\nSuccessfully installed maxima-5.20.1.p1\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing maxima-5.20.1.p1.spkg\n```\n\n\n## Note to Release manager\nThere are many tickets active at the minute for updates to Maxima and ECL. Once positively, this should be integrated with Maxima at #8645. At the time of writing, the use of the latest Maxima will cause problems with doctest failures, as Maxima's output is changed from the current version.",
    "created_at": "2010-06-19T19:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87180",
    "user": "drkirkby"
}
```

I've created a new ECL package

http://boxen.math.washington.edu/home/kirkby/revised-patches/ecl-10.4.1.spkg

which has the following fixes applied:

* Updates ECL to the latest upstream, 10.4.1
* Applies a fix to stop ECL building in parallel, which is ticket #9187. This already has positive review. 
* Applies the fix from #8089 to disable the dynamic foreign function interface as advised by the ECL developer. This disables the use of assembly code on OpenSolaris x64, but no other platform.
* Removes files from /tmp/ECL* as soon as they are no longer needed, as failure to do so can present problems on multi-user systems. 

All changes have been checked with #8645, which has a change to Maxima which allows Maxima to build with the latest ECL. The patch on #8645 does **not** update Maxima to the latest version, as that creates problems which are non-trivial to solve. It does however fix a problem with Maxima not installing the library properly, and allows Maxima to build with the latest ECL>

As such, the attached ticket:
 
* Allows Maxima to build the library properly whilst still working with the latest ECL. 
* Remove unwanted ECL tmp files. 
* Allows spkgs to build in parallel
* Allow ECL to build on OpenSolaris x64. 

Here are the test results:

 == Testing on Solaris 10 SPARC in 32-bit mode. ==
* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler) 
* Sage 4.4.4.alpha1


```
	done
for i in Copyright LGPL; do \
	  /usr/bin/ginstall -c -m 644 /export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/ecl-10.4.1/src/src/../$i /export/home/drkirkby/sage-4.4.4.alpha1/local/lib/; \
	done
/bin/sh /export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/ecl-10.4.1/src/src/gc/mkinstalldirs /export/home/drkirkby/sage-4.4.4.alpha1/local/share/man/man1
for i in doc/ecl.man doc/ecl-config.man; do \
	    /usr/bin/ginstall -c -m 644 $i /export/home/drkirkby/sage-4.4.4.alpha1/local/share/man/man1/ecl.1; \
	done
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/ecl-10.4.1/src/build'

real	1m26.075s
user	1m17.655s
sys	0m7.531s
Successfully installed ecl-10.4.1
```
 

Here is the Maxima 5.20.1.p1 installation from #8645


```
installing Maxima library as /export/home/drkirkby/sage-4.4.4.alpha1/local/lib/ecl//maxima.fas

real    22m32.432s
user    19m9.372s
sys     2m51.674s
Successfully installed maxima-5.20.1.p1
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/maxima-5.20.1.p1
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing maxima-5.20.1.p1.spkg
drkirkby@redstart:~/sage-4.4.4.alpha1$ 
```


 == Testing on OpenSolaris x64 06/2009 64-bit mode. ==
* Sun Ultra 27
* 2 x 3.33 GHz quad core Intel Xeon MHz
* 12 GB RAM
* OpenSolaris 06/2009 (Last release of OpenSolaris, updated to build 134)
* gcc 4.4.4 (uses Sun linker and GNU assembler) 
* Sage 4.4.4.alpha1


```
/bin/sh /export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/ecl-10.4.1/src/src/gc/mkinstalldirs /export/home/drkirkby/sage-4.4.4.alpha1/local/share/man/man1
for i in doc/ecl.man doc/ecl-config.man; do \
	    /usr/bin/ginstall -c -m 644 $i /export/home/drkirkby/sage-4.4.4.alpha1/local/share/man/man1/ecl.1; \
	done
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/ecl-10.4.1/src/build'

real	1m26.075s
user	1m17.655s
sys	0m7.531s
Successfully installed ecl-10.4.1
```


Maxima 5.20.1.p1 will **not** build on this platform, but such a problem is not related to this ticket, and appears it might be an incorrect flag given in the source (-Wl,-G instead of -shared). This is documented at #9099

## Testing on sage.math (Linux), 64-bit.

```
n/man1/ecl.1; \
	done
make[1]: Leaving directory `/home/kirkby/sage-4.4.3/spkg/build/ecl-10.4.1/src/build'

real	2m16.904s
user	1m44.990s
sys	0m14.980s
Successfully installed ecl-10.4.1
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing ecl-10.4.1.spkg
```


We can also see Maxima, and the library are ok now. 


```
;;; 
installing Maxima library as /home/kirkby/sage-4.4.3/local/lib/ecl//maxima.fas

real	4m41.594s
user	3m14.160s
sys	0m46.000s
Successfully installed maxima-5.20.1.p1
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing maxima-5.20.1.p1.spkg
```


## Note to Release manager
There are many tickets active at the minute for updates to Maxima and ECL. Once positively, this should be integrated with Maxima at #8645. At the time of writing, the use of the latest Maxima will cause problems with doctest failures, as Maxima's output is changed from the current version.



---

archive/issue_comments_087181.json:
```json
{
    "body": "I have tested this ticket by building sage 4.4.3 with the following spkgs substituted:\nhttp://boxen.math.washington.edu/home/kirkby/revised-patches/ecl-10.4.1.spkg\nhttp://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg\nAll doctests pass on `sage.math.washington.edu`. Furthermore, the ecl-10.4.1 package looks like it does what it's supposed to. When I diff it with http://sage.math.washington.edu/home/nbruin/ecl-10.4.1.spkg there are some unexpected files and differences in binary files in the `.hg` subdir, but otherwise the packages agree.\n\nMerging this ticket should be a good stepping stone towards #8731 (assuming the issues there haven't been resolved by the time the next release merges are made). Merging this ticket would also resolve #8645, as well as all ECL related ticket referred to.",
    "created_at": "2010-06-21T06:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87181",
    "user": "nbruin"
}
```

I have tested this ticket by building sage 4.4.3 with the following spkgs substituted:
http://boxen.math.washington.edu/home/kirkby/revised-patches/ecl-10.4.1.spkg
http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg
All doctests pass on `sage.math.washington.edu`. Furthermore, the ecl-10.4.1 package looks like it does what it's supposed to. When I diff it with http://sage.math.washington.edu/home/nbruin/ecl-10.4.1.spkg there are some unexpected files and differences in binary files in the `.hg` subdir, but otherwise the packages agree.

Merging this ticket should be a good stepping stone towards #8731 (assuming the issues there haven't been resolved by the time the next release merges are made). Merging this ticket would also resolve #8645, as well as all ECL related ticket referred to.



---

archive/issue_comments_087182.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-21T06:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87182",
    "user": "nbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087183.json:
```json
{
    "body": "I just noticed a small inaccuracy in the description of the hardware used to test this on OpenSolaris. It does not affect the validity of the ticket, but it is sensible to correct the error. \n\nThe section marked *Testing on OpenSolaris x64 06/2009 64-bit mode.* states the processors are:\n\n* 2 x 3.33 GHz quad core Intel Xeon MHz \n\nwhich is incorrect. Unfortunately, the Sun Ultra 27 does not support more than one CPU. A more accurate description of the hardware/software used to test this ECL package on OpenSolaris is:\n\n## Testing on OpenSolaris x64 06/2009 64-bit mode.\n* [Sun Ultra 27 workstation](http://www.sun.com/desktop/workstation/ultra27/)\n* 1 x 3.33 GHz 64-bit [Intel Xeon W3580](http://ark.intel.com/Product.aspx?id=39723) CPU (4 cores, 8 threads, 8 MB cache). \n* 12 GB RAM\n* [OpenSolaris](http://www.opensolaris.com/) 06/2009 (Last release of OpenSolaris, updated to build 134)\n* [gcc 4.4.4](http://gcc.gnu.org/gcc-4.4/changes.html) (uses Sun linker and GNU assembler)\n* Sage 4.4.4.alpha1 \n\nDave",
    "created_at": "2010-06-25T12:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87183",
    "user": "drkirkby"
}
```

I just noticed a small inaccuracy in the description of the hardware used to test this on OpenSolaris. It does not affect the validity of the ticket, but it is sensible to correct the error. 

The section marked *Testing on OpenSolaris x64 06/2009 64-bit mode.* states the processors are:

* 2 x 3.33 GHz quad core Intel Xeon MHz 

which is incorrect. Unfortunately, the Sun Ultra 27 does not support more than one CPU. A more accurate description of the hardware/software used to test this ECL package on OpenSolaris is:

## Testing on OpenSolaris x64 06/2009 64-bit mode.
* [Sun Ultra 27 workstation](http://www.sun.com/desktop/workstation/ultra27/)
* 1 x 3.33 GHz 64-bit [Intel Xeon W3580](http://ark.intel.com/Product.aspx?id=39723) CPU (4 cores, 8 threads, 8 MB cache). 
* 12 GB RAM
* [OpenSolaris](http://www.opensolaris.com/) 06/2009 (Last release of OpenSolaris, updated to build 134)
* [gcc 4.4.4](http://gcc.gnu.org/gcc-4.4/changes.html) (uses Sun linker and GNU assembler)
* Sage 4.4.4.alpha1 

Dave



---

archive/issue_comments_087184.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87184",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_087185.json:
```json
{
    "body": "Applied http://boxen.math.washington.edu/home/kirkby/revised-patches/ecl-10.4.1.spkg",
    "created_at": "2010-06-25T15:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87185",
    "user": "rlm"
}
```

Applied http://boxen.math.washington.edu/home/kirkby/revised-patches/ecl-10.4.1.spkg



---

archive/issue_comments_087186.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-07-11T19:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87186",
    "user": "rlm"
}
```

Changing status from closed to new.



---

archive/issue_comments_087187.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-07-11T19:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87187",
    "user": "rlm"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_087188.json:
```json
{
    "body": "ecl-10.2.1.p3 does not compile on Fedora 14:\n\n```\nlibeclmin.a(sequence.o): In function `cl_sublis':\n/home/vbraun/Code/ecl/src/c/sequence.d:106: multiple definition of `cl_sublis'\nlibeclmin.a(list.o):/home/vbraun/Code/ecl/src/c/list.d:778: first defined here\nc/all_symbols.o:(.data.rel+0x9b20): undefined reference to `cl_subseq'\nlibeclmin.a(string.o): In function `string_trim0':\n/home/vbraun/Code/ecl/src/c/string.d:756: undefined reference to `cl_subseq'\nlibeclmin.a(sequence.o): In function `cl_copy_seq':\ntmp.c:(.text+0x4c0): undefined reference to `cl_subseq'\nlibeclmin.a(pathname.o): In function `make_one':\n/home/vbraun/Code/ecl/src/c/pathname.d:234: undefined reference to `cl_subseq'\n/home/vbraun/Code/ecl/src/c/pathname.d:234: undefined reference to `cl_subseq'\ncollect2: ld returned 1 exit status\nmake[1]: *** [ecl_min] Error 1\n```\n\nThe current ecl-10.4.1 compiles fine. Given that Fedora 14 is scheduled to be released next Monday, is there any chance we can update ecl? Ideally in the next Sage (4.6.1) release...",
    "created_at": "2010-10-29T01:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87188",
    "user": "vbraun"
}
```

ecl-10.2.1.p3 does not compile on Fedora 14:

```
libeclmin.a(sequence.o): In function `cl_sublis':
/home/vbraun/Code/ecl/src/c/sequence.d:106: multiple definition of `cl_sublis'
libeclmin.a(list.o):/home/vbraun/Code/ecl/src/c/list.d:778: first defined here
c/all_symbols.o:(.data.rel+0x9b20): undefined reference to `cl_subseq'
libeclmin.a(string.o): In function `string_trim0':
/home/vbraun/Code/ecl/src/c/string.d:756: undefined reference to `cl_subseq'
libeclmin.a(sequence.o): In function `cl_copy_seq':
tmp.c:(.text+0x4c0): undefined reference to `cl_subseq'
libeclmin.a(pathname.o): In function `make_one':
/home/vbraun/Code/ecl/src/c/pathname.d:234: undefined reference to `cl_subseq'
/home/vbraun/Code/ecl/src/c/pathname.d:234: undefined reference to `cl_subseq'
collect2: ld returned 1 exit status
make[1]: *** [ecl_min] Error 1
```

The current ecl-10.4.1 compiles fine. Given that Fedora 14 is scheduled to be released next Monday, is there any chance we can update ecl? Ideally in the next Sage (4.6.1) release...



---

archive/issue_comments_087189.json:
```json
{
    "body": "You should open a new trac ticket for this. \n\nDave",
    "created_at": "2010-10-29T02:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87189",
    "user": "drkirkby"
}
```

You should open a new trac ticket for this. 

Dave



---

archive/issue_comments_087190.json:
```json
{
    "body": "I've created a new trac ticket for you - see #10185.",
    "created_at": "2010-10-29T03:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87190",
    "user": "drkirkby"
}
```

I've created a new trac ticket for you - see #10185.



---

archive/issue_comments_087191.json:
```json
{
    "body": "I realise this ticket was still open, but I still think the Fedora issue should go on a ticket of its own. The package I made for this ticket is not the latest ECL, so if we do update ECL, we will probably end up using a later version of it. The version here does not have some fixes which are in the current ECL in Sage. In particular, #9917 has fixes which are not in my package referenced here.",
    "created_at": "2010-10-29T03:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87191",
    "user": "drkirkby"
}
```

I realise this ticket was still open, but I still think the Fedora issue should go on a ticket of its own. The package I made for this ticket is not the latest ECL, so if we do update ECL, we will probably end up using a later version of it. The version here does not have some fixes which are in the current ECL in Sage. In particular, #9917 has fixes which are not in my package referenced here.



---

archive/issue_comments_087192.json:
```json
{
    "body": "I went through `./src/src/c/dpp.c` in your ecl-10.4.1 spkg (http://boxen.math.washington.edu/home/kirkby/revised-patches/ecl-10.4.1.spkg) and checked that all `fprint()`s have the right number of arguments. So upstream fixed #9917 and we don't have to patch it any more.\n\nI removed the included gmp as discussed in #9493.\n\nAre there any other outstanding patches? I've looked through trac and there seem to be many overlapping discussions. But I could not find any outstanding bugs.\n\nThe new ecl requires also a new maxima (5.22.1 is newest upstream release), so we have to update both at the same time. I've created #10187 for a simultaneous ecl+maxima update.",
    "created_at": "2010-10-29T13:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87192",
    "user": "vbraun"
}
```

I went through `./src/src/c/dpp.c` in your ecl-10.4.1 spkg (http://boxen.math.washington.edu/home/kirkby/revised-patches/ecl-10.4.1.spkg) and checked that all `fprint()`s have the right number of arguments. So upstream fixed #9917 and we don't have to patch it any more.

I removed the included gmp as discussed in #9493.

Are there any other outstanding patches? I've looked through trac and there seem to be many overlapping discussions. But I could not find any outstanding bugs.

The new ecl requires also a new maxima (5.22.1 is newest upstream release), so we have to update both at the same time. I've created #10187 for a simultaneous ecl+maxima update.



---

archive/issue_comments_087193.json:
```json
{
    "body": "This ticket can be closed as we did update to ecl-10.4.1 a while ago.",
    "created_at": "2011-02-19T13:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87193",
    "user": "vbraun"
}
```

This ticket can be closed as we did update to ecl-10.4.1 a while ago.



---

archive/issue_comments_087194.json:
```json
{
    "body": "In fact, now ECL is at version 11.1.1 in Sage.  #9493 is still open for the GMP removal, otherwise this ticket can be closed.",
    "created_at": "2011-06-28T16:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87194",
    "user": "kcrisman"
}
```

In fact, now ECL is at version 11.1.1 in Sage.  #9493 is still open for the GMP removal, otherwise this ticket can be closed.



---

archive/issue_comments_087195.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-28T16:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87195",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087196.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-28T16:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87196",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087197.json:
```json
{
    "body": "Replying to [comment:15 kcrisman]:\n> In fact, now ECL is at version 11.1.1 in Sage.  #9493 is still open for the GMP removal, otherwise this ticket can be closed.\n\nI wonder if at least my *Special Update / Build Instructions* from there went into the ECL spkg... 8)",
    "created_at": "2011-06-28T16:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87197",
    "user": "leif"
}
```

Replying to [comment:15 kcrisman]:
> In fact, now ECL is at version 11.1.1 in Sage.  #9493 is still open for the GMP removal, otherwise this ticket can be closed.

I wonder if at least my *Special Update / Build Instructions* from there went into the ECL spkg... 8)



---

archive/issue_comments_087198.json:
```json
{
    "body": "Well, unpack ecl-11.1.1.p1.spkg and find out.  At any rate, that is on the ticket description at #9493 still, so this ticket should be closed.",
    "created_at": "2011-06-28T16:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87198",
    "user": "kcrisman"
}
```

Well, unpack ecl-11.1.1.p1.spkg and find out.  At any rate, that is on the ticket description at #9493 still, so this ticket should be closed.



---

archive/issue_comments_087199.json:
```json
{
    "body": "Replying to [comment:18 kcrisman]:\n> Well, unpack ecl-11.1.1.p1.spkg and find out.  At any rate, that is on the ticket description at #9493 still, so this ticket should be closed.\nNo offense intended, by the way - it just seems more relevant to discuss this at that ticket.",
    "created_at": "2011-06-28T16:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87199",
    "user": "kcrisman"
}
```

Replying to [comment:18 kcrisman]:
> Well, unpack ecl-11.1.1.p1.spkg and find out.  At any rate, that is on the ticket description at #9493 still, so this ticket should be closed.
No offense intended, by the way - it just seems more relevant to discuss this at that ticket.



---

archive/issue_comments_087200.json:
```json
{
    "body": "Replying to [comment:18 kcrisman]:\n> Well, unpack ecl-11.1.1.p1.spkg and find out.  At any rate, that is on the ticket description at #9493 still, so this ticket should be closed.\n\nCould be the first time I ever use `sage -info ...` (which ought to dump `SPKG.txt` to the screen, but unfortunately currently doesn't: #11021). :D",
    "created_at": "2011-06-28T16:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87200",
    "user": "leif"
}
```

Replying to [comment:18 kcrisman]:
> Well, unpack ecl-11.1.1.p1.spkg and find out.  At any rate, that is on the ticket description at #9493 still, so this ticket should be closed.

Could be the first time I ever use `sage -info ...` (which ought to dump `SPKG.txt` to the screen, but unfortunately currently doesn't: #11021). :D



---

archive/issue_comments_087201.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-07-05T10:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9264#issuecomment-87201",
    "user": "jdemeyer"
}
```

Resolution: duplicate
