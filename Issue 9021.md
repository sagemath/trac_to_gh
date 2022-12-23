# Issue 9021: gdmodule not building on OpenSolaris x64.

archive/issues_009021.json:
```json
{
    "body": "Assignee: drkirkby\n\n## Build environment\n* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM\n* OpenSolaris 2009.06 snv_111b X86\n* Sage 4.4.2\n* gcc 4.4.4\n\n## How gcc 4.4.4 was configured\nSince the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. \n\n\n```\ndrkirkby@hawk:~/sage-4.4.2$ gcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.4.4 (GCC) \n```\n\n\ngcc 4.3.4 was failing to build iconv. \n\n## How the Sage build was attempted\n* 64-bit build. SAGE64 was set to \"yes\"\n* #9008 update zlib to latest upstream release to allow a 64-bit library to be built. \n* #9009 update mercurial spkg to build 64-bit.\n* #7982 update sage_fortran so it can build 64-bit binaries.\n\n## The problem\n\n\n```\n_gdmodule.c: In function \u2018image_stringup\u2019:\n_gdmodule.c:1022: warning: pointer targets in passing argument 5 of \u2018gdImageStringUp\u2019 differ in signedness\n/export/home/drkirkby/sage-4.4.2/local/include/gd.h:365: note: expected \u2018unsigned char *\u2019 but argument is of type \u2018char *\u2019\n_gdmodule.c: In function \u2018image_stringup16\u2019:\n_gdmodule.c:1037: warning: passing argument 5 of \u2018gdImageStringUp16\u2019 from incompatible pointer type\n/export/home/drkirkby/sage-4.4.2/local/include/gd.h:369: note: expected \u2018short unsigned int *\u2019 but argument is of type \u2018Py_UNICODE *\u2019\nerror: command 'gcc' failed with exit status 1\nFailure to build gdmodule\n\nreal\t0m0.134s\nuser\t0m0.098s\nsys\t0m0.032s\nsage: An error occurred while installing gdmodule-0.56.p7\n```\n\n\n## Likely Reason\nIt looks like a 32-bit build is being used, but it's not so obvious how to fix this - it is not the normal SAGE64/OS X issue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9021\n\n",
    "created_at": "2010-05-23T17:27:24Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "gdmodule not building on OpenSolaris x64.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9021",
    "user": "drkirkby"
}
```
Assignee: drkirkby

## Build environment
* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
* OpenSolaris 2009.06 snv_111b X86
* Sage 4.4.2
* gcc 4.4.4

## How gcc 4.4.4 was configured
Since the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. 


```
drkirkby@hawk:~/sage-4.4.2$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
```


gcc 4.3.4 was failing to build iconv. 

## How the Sage build was attempted
* 64-bit build. SAGE64 was set to "yes"
* #9008 update zlib to latest upstream release to allow a 64-bit library to be built. 
* #9009 update mercurial spkg to build 64-bit.
* #7982 update sage_fortran so it can build 64-bit binaries.

## The problem


```
_gdmodule.c: In function ‘image_stringup’:
_gdmodule.c:1022: warning: pointer targets in passing argument 5 of ‘gdImageStringUp’ differ in signedness
/export/home/drkirkby/sage-4.4.2/local/include/gd.h:365: note: expected ‘unsigned char *’ but argument is of type ‘char *’
_gdmodule.c: In function ‘image_stringup16’:
_gdmodule.c:1037: warning: passing argument 5 of ‘gdImageStringUp16’ from incompatible pointer type
/export/home/drkirkby/sage-4.4.2/local/include/gd.h:369: note: expected ‘short unsigned int *’ but argument is of type ‘Py_UNICODE *’
error: command 'gcc' failed with exit status 1
Failure to build gdmodule

real	0m0.134s
user	0m0.098s
sys	0m0.032s
sage: An error occurred while installing gdmodule-0.56.p7
```


## Likely Reason
It looks like a 32-bit build is being used, but it's not so obvious how to fix this - it is not the normal SAGE64/OS X issue.

Issue created by migration from https://trac.sagemath.org/ticket/9021





---

archive/issue_comments_083467.json:
```json
{
    "body": "If you're willing to accept a short informal \"inline\" patch, try adding something like\n\n```\nextra_args = [\"-m64\"] if os.environ.get(\"SAGE64\", \"no\")==\"yes\" else []\n```\n\nright after the Cygwin patch (at top level in `patches/Setup.py`, and add\n\n```\n            extra_compile_args=extra_args, extra_link_args=extra_args,\n```\n\nto the `Extension` constructor call below.\n\n-Leif\n\n\nSorry for the inconvenience, but I'm currently unable to create a patch...",
    "created_at": "2010-05-23T22:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9021#issuecomment-83467",
    "user": "leif"
}
```

If you're willing to accept a short informal "inline" patch, try adding something like

```
extra_args = ["-m64"] if os.environ.get("SAGE64", "no")=="yes" else []
```

right after the Cygwin patch (at top level in `patches/Setup.py`, and add

```
            extra_compile_args=extra_args, extra_link_args=extra_args,
```

to the `Extension` constructor call below.

-Leif


Sorry for the inconvenience, but I'm currently unable to create a patch...



---

archive/issue_comments_083468.json:
```json
{
    "body": "Oh, the \"usual\" method of setting/modifying `CFLAGS` et al. in `spkg-install` *should* work, too.",
    "created_at": "2010-05-23T23:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9021#issuecomment-83468",
    "user": "leif"
}
```

Oh, the "usual" method of setting/modifying `CFLAGS` et al. in `spkg-install` *should* work, too.



---

archive/issue_comments_083469.json:
```json
{
    "body": "Attachment\n\nModifies `patches/Setup.py` to honor `$SAGE64`. Testing is up to you!",
    "created_at": "2010-05-24T17:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9021#issuecomment-83469",
    "user": "leif"
}
```

Attachment

Modifies `patches/Setup.py` to honor `$SAGE64`. Testing is up to you!



---

archive/issue_comments_083470.json:
```json
{
    "body": "I've uploaded a Mercurial patch that modifies `patches/Setup.py` as suggested above.\n\nNote that `patches/Setup.py.patch` isn't used by `spkg-install`, so I haven't updated that.\n\nThe patch has to be tested before bumping to p8 (and updating `SPKG.txt`, which already lacks some modification history).",
    "created_at": "2010-05-24T18:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9021#issuecomment-83470",
    "user": "leif"
}
```

I've uploaded a Mercurial patch that modifies `patches/Setup.py` as suggested above.

Note that `patches/Setup.py.patch` isn't used by `spkg-install`, so I haven't updated that.

The patch has to be tested before bumping to p8 (and updating `SPKG.txt`, which already lacks some modification history).



---

archive/issue_comments_083471.json:
```json
{
    "body": "For other OpenSolaris issues, see #9026",
    "created_at": "2010-05-24T18:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9021#issuecomment-83471",
    "user": "drkirkby"
}
```

For other OpenSolaris issues, see #9026



---

archive/issue_comments_083472.json:
```json
{
    "body": "Replying to [comment:3 leif]:\n> I've uploaded a Mercurial patch that modifies `patches/Setup.py` as suggested above.\n> \n> Note that `patches/Setup.py.patch` isn't used by `spkg-install`, so I haven't updated that.\n> \n> The patch has to be tested before bumping to p8 (and updating `SPKG.txt`, which already lacks some modification history).\n\nThank you, I'll try this. \n\nDave",
    "created_at": "2010-06-05T22:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9021#issuecomment-83472",
    "user": "drkirkby"
}
```

Replying to [comment:3 leif]:
> I've uploaded a Mercurial patch that modifies `patches/Setup.py` as suggested above.
> 
> Note that `patches/Setup.py.patch` isn't used by `spkg-install`, so I haven't updated that.
> 
> The patch has to be tested before bumping to p8 (and updating `SPKG.txt`, which already lacks some modification history).

Thank you, I'll try this. 

Dave



---

archive/issue_comments_083473.json:
```json
{
    "body": "This can be closed as fixed. \n\nI don't have a clue where it was fixed. Despite this was reported against gdmodule-0.56.p7, the current version in Sage is still gdmodule-0.56.p7. The latest entry in SPKG.txt shows gdmodule-0.56.p5, so at least two updates have not been documented properly. \n\nDave",
    "created_at": "2011-04-02T13:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9021#issuecomment-83473",
    "user": "drkirkby"
}
```

This can be closed as fixed. 

I don't have a clue where it was fixed. Despite this was reported against gdmodule-0.56.p7, the current version in Sage is still gdmodule-0.56.p7. The latest entry in SPKG.txt shows gdmodule-0.56.p5, so at least two updates have not been documented properly. 

Dave



---

archive/issue_comments_083474.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2011-04-05T15:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9021#issuecomment-83474",
    "user": "jdemeyer"
}
```

Resolution: worksforme
