# Issue 8049: libgfortran *must* get shipped with the Sage binaries

archive/issues_008049.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jdemeyer tmonteil\n\n\n```\nI'm suddenly very concerned that Sage binaries won't work at all on computers without libgfortran.so installed. Does Sage even start up on such a box?\n\nYep.  If I take one of the Sage build machines, remove libgfortran, then start Sage I get:\n\n$ sage\nBOOM!\n\n.... ImportError: libgfortran.so.3: cannot open shared object file: No such file or directory\n\n----------------\n\nNot good, since most Linux installs won't have libgfortran.  If I then reinstall gfortran, and copy libgfortran.so  to SAGE_ROOT/local/lib/, then uninstall gfortran, then Sage works fine again.\n\ncp /usr/lib/libgfortran.so.3.0.0 local/lib/libgfortran.so.3\n\nwstein@ubuntu910-64:/tmp/wstein/farm/sage-4.3.1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: import scipy.linalg\nsage:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8049\n\n",
    "created_at": "2010-01-24T02:22:18Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "libgfortran *must* get shipped with the Sage binaries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8049",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber

CC:  @jdemeyer tmonteil


```
I'm suddenly very concerned that Sage binaries won't work at all on computers without libgfortran.so installed. Does Sage even start up on such a box?

Yep.  If I take one of the Sage build machines, remove libgfortran, then start Sage I get:

$ sage
BOOM!

.... ImportError: libgfortran.so.3: cannot open shared object file: No such file or directory

----------------

Not good, since most Linux installs won't have libgfortran.  If I then reinstall gfortran, and copy libgfortran.so  to SAGE_ROOT/local/lib/, then uninstall gfortran, then Sage works fine again.

cp /usr/lib/libgfortran.so.3.0.0 local/lib/libgfortran.so.3

wstein@ubuntu910-64:/tmp/wstein/farm/sage-4.3.1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: import scipy.linalg
sage:
```


Issue created by migration from https://trac.sagemath.org/ticket/8049





---

archive/issue_comments_070242.json:
```json
{
    "body": "I made the point the other day, that the library should be included in the binary, along with C++ library. \n\nDave",
    "created_at": "2010-01-24T02:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70242",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I made the point the other day, that the library should be included in the binary, along with C++ library. 

Dave



---

archive/issue_comments_070243.json:
```json
{
    "body": "Actually, I think the C library too. The C library is very small anyway. If Sage is linked with a new library, and someone has an older one on their system, it could be a problem. \n\n'ldd' might be useful to get the location on Solaris, Linux or HP-UX, but not on OS X. Perhaps there is a more widely supported command, but I don't know of it. \n\nThe configure script for gcc has these options. \n\n\n```\nFine tuning of the installation directories:\n  --bindir=DIR           user executables [EPREFIX/bin]\n  --libdir=DIR           object code libraries [EPREFIX/lib]\n```\n\n\nso while one could guess at the location of libraries from the location of the gfortran binary, it is not guaranteed to be right. \n\nOn Solaris, in 64-bit mode, it will be in a subdirectory too\n\n\n```\ndrkirkby@hawk:~$ find /usr/local -name libgfortran.so\n/usr/local/gcc-4.3.4/lib/amd64/libgfortran.so\n/usr/local/gcc-4.3.4/lib/libgfortran.so\n/usr/local/gcc-4.5-20100114/lib/amd64/libgfortran.so\n/usr/local/gcc-4.5-20100114/lib/libgfortran.so\n/usr/local/lib/amd64/libgfortran.so\n/usr/local/lib/libgfortran.so\n/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/libgfortran.so\n/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/amd64/libgfortran.so\n```\n\n\nDave",
    "created_at": "2010-01-24T03:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70243",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Actually, I think the C library too. The C library is very small anyway. If Sage is linked with a new library, and someone has an older one on their system, it could be a problem. 

'ldd' might be useful to get the location on Solaris, Linux or HP-UX, but not on OS X. Perhaps there is a more widely supported command, but I don't know of it. 

The configure script for gcc has these options. 


```
Fine tuning of the installation directories:
  --bindir=DIR           user executables [EPREFIX/bin]
  --libdir=DIR           object code libraries [EPREFIX/lib]
```


so while one could guess at the location of libraries from the location of the gfortran binary, it is not guaranteed to be right. 

On Solaris, in 64-bit mode, it will be in a subdirectory too


```
drkirkby@hawk:~$ find /usr/local -name libgfortran.so
/usr/local/gcc-4.3.4/lib/amd64/libgfortran.so
/usr/local/gcc-4.3.4/lib/libgfortran.so
/usr/local/gcc-4.5-20100114/lib/amd64/libgfortran.so
/usr/local/gcc-4.5-20100114/lib/libgfortran.so
/usr/local/lib/amd64/libgfortran.so
/usr/local/lib/libgfortran.so
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/libgfortran.so
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/amd64/libgfortran.so
```


Dave



---

archive/issue_comments_070244.json:
```json
{
    "body": "Replying to [comment:2 drkirkby]:\n> Actually, I think the C library too. The C library is very small anyway. If Sage is linked with a new library, and someone has an older one on their system, it could be a problem. \n> \n> 'ldd' might be useful to get the location on Solaris, Linux or HP-UX, but not on OS X. Perhaps there is a more widely supported command, but I don't know of it. \n>\n\nThe OSX analog of ldd is called otool (otool -L), to be precise: \n{{\n$ otool -L liblinboxsage.dylib\nliblinboxsage.dylib:\n\t/tmp/sage-4.3.1/local/lib/liblinboxsage.0.dylib (compatibility version 1.0.0, current version 1.0.0)\n\tlibntl.dylib (compatibility version 0.0.0, current version 0.0.0)\n\t/tmp/sage-4.3.1/local/lib/libgmpxx.3.dylib (compatibility version 5.0.0, current version 5.6.0)\n\t/tmp/sage-4.3.1/local/lib/libgmp.3.dylib (compatibility version 8.0.0, current version 8.6.0)\n\t/tmp/sage-4.3.1/local/lib/libgivaro.0.dylib (compatibility version 1.0.0, current version 1.2.0)\n\t/usr/lib/libstdc++.6.dylib (compatibility version 7.0.0, current version 7.4.0)\n\t/usr/lib/libgcc_s.1.dylib (compatibility version 1.0.0, current version 1.0.0)\n\t/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 111.1.4)\n}}\n\nJust in case,\nDima",
    "created_at": "2010-02-05T03:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70244",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:2 drkirkby]:
> Actually, I think the C library too. The C library is very small anyway. If Sage is linked with a new library, and someone has an older one on their system, it could be a problem. 
> 
> 'ldd' might be useful to get the location on Solaris, Linux or HP-UX, but not on OS X. Perhaps there is a more widely supported command, but I don't know of it. 
>

The OSX analog of ldd is called otool (otool -L), to be precise: 
{{
$ otool -L liblinboxsage.dylib
liblinboxsage.dylib:
	/tmp/sage-4.3.1/local/lib/liblinboxsage.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	libntl.dylib (compatibility version 0.0.0, current version 0.0.0)
	/tmp/sage-4.3.1/local/lib/libgmpxx.3.dylib (compatibility version 5.0.0, current version 5.6.0)
	/tmp/sage-4.3.1/local/lib/libgmp.3.dylib (compatibility version 8.0.0, current version 8.6.0)
	/tmp/sage-4.3.1/local/lib/libgivaro.0.dylib (compatibility version 1.0.0, current version 1.2.0)
	/usr/lib/libstdc++.6.dylib (compatibility version 7.0.0, current version 7.4.0)
	/usr/lib/libgcc_s.1.dylib (compatibility version 1.0.0, current version 1.0.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 111.1.4)
}}

Just in case,
Dima



---

archive/issue_comments_070245.json:
```json
{
    "body": "I fixed this by writing a custom dist script that I use for building binaries.",
    "created_at": "2010-02-13T00:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70245",
    "user": "https://github.com/williamstein"
}
```

I fixed this by writing a custom dist script that I use for building binaries.



---

archive/issue_comments_070246.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-13T00:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70246",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_070247.json:
```json
{
    "body": "Does this do C and C++, or just Fortran? You can be 100% sure that the user needs the C and C++ libraries. You might well get away with it on most linux distros if gcc is installed. You certainly can't get away with it on Solaris, where a recent gcc is not installed unless someone has taken the steps to do so. \n\nDave",
    "created_at": "2010-02-13T00:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70247",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Does this do C and C++, or just Fortran? You can be 100% sure that the user needs the C and C++ libraries. You might well get away with it on most linux distros if gcc is installed. You certainly can't get away with it on Solaris, where a recent gcc is not installed unless someone has taken the steps to do so. 

Dave



---

archive/issue_comments_070248.json:
```json
{
    "body": "Hi, this is my first ticket, I just joined trac.  I have the following error when I try to import numpy:\n\n\n```\nImportError: libgfortran.so.3: cannot open shared object file: No such file or directory\n```\n\n\nI have the latest releasted Sage Binary (5.3) installed on my linux machine, running Xubuntu.",
    "created_at": "2012-09-24T04:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70248",
    "user": "https://trac.sagemath.org/admin/accounts/users/startakovsky"
}
```

Hi, this is my first ticket, I just joined trac.  I have the following error when I try to import numpy:


```
ImportError: libgfortran.so.3: cannot open shared object file: No such file or directory
```


I have the latest releasted Sage Binary (5.3) installed on my linux machine, running Xubuntu.



---

archive/issue_comments_070249.json:
```json
{
    "body": "Replying to [comment:6 startakovsky]:\n> Hi, this is my first ticket, I just joined trac.  I have the following error when I try to import numpy:\n> \n> {{{\n> ImportError: libgfortran.so.3: cannot open shared object file: No such file or directory\n> }}}\n> \n> I have the latest releasted Sage Binary (5.3) installed on my linux machine, running Xubuntu. \n\nTo help your particular installation, you can just do \n\n```\nsudo apt-get install libgfortran3\n```\n\n\nWe'll have to look into this more carefully, though.",
    "created_at": "2012-09-24T04:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70249",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:6 startakovsky]:
> Hi, this is my first ticket, I just joined trac.  I have the following error when I try to import numpy:
> 
> {{{
> ImportError: libgfortran.so.3: cannot open shared object file: No such file or directory
> }}}
> 
> I have the latest releasted Sage Binary (5.3) installed on my linux machine, running Xubuntu. 

To help your particular installation, you can just do 

```
sudo apt-get install libgfortran3
```


We'll have to look into this more carefully, though.



---

archive/issue_comments_070250.json:
```json
{
    "body": "It would be interesting to know whether this problem already occurred in sage 4.8 . The last thing I know that changed in relation to fortran is #12369  where the gcc package was added and the old fortran package removed. I think it would be good to open a new ticket for this issue, leaving this ticket as an \"archive\" for the old issue.",
    "created_at": "2012-09-24T06:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70250",
    "user": "https://github.com/koffie"
}
```

It would be interesting to know whether this problem already occurred in sage 4.8 . The last thing I know that changed in relation to fortran is #12369  where the gcc package was added and the old fortran package removed. I think it would be good to open a new ticket for this issue, leaving this ticket as an "archive" for the old issue.



---

archive/issue_comments_070251.json:
```json
{
    "body": "Changing keywords from \"\" to \"days43\".",
    "created_at": "2012-10-28T15:24:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70251",
    "user": "https://trac.sagemath.org/admin/accounts/users/tmonteil"
}
```

Changing keywords from "" to "days43".



---

archive/issue_comments_070252.json:
```json
{
    "body": "Hi, is it possible to re-open this ticket ? Currently, libgfortran is not shipped with Sage.",
    "created_at": "2012-10-28T15:24:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70252",
    "user": "https://trac.sagemath.org/admin/accounts/users/tmonteil"
}
```

Hi, is it possible to re-open this ticket ? Currently, libgfortran is not shipped with Sage.



---

archive/issue_comments_070253.json:
```json
{
    "body": "Replying to [comment:9 tmonteil]:\n> Hi, is it possible to re-open this ticket ?\nIt is certainly possible to re-open this ticket, but you should specify in more detail why.\n\nIn sage-5.3, libgfortran is shipped with the official Sage binaries, except for Ubuntu 12.04.  In sage-5.4, libgfortran will also be shipped with the Ubuntu 12.04 binaries, see #13515.",
    "created_at": "2012-10-29T08:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70253",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:9 tmonteil]:
> Hi, is it possible to re-open this ticket ?
It is certainly possible to re-open this ticket, but you should specify in more detail why.

In sage-5.3, libgfortran is shipped with the official Sage binaries, except for Ubuntu 12.04.  In sage-5.4, libgfortran will also be shipped with the Ubuntu 12.04 binaries, see #13515.



---

archive/issue_comments_070254.json:
```json
{
    "body": "Correct me if this issue has been superseded, but I just installed this binary\n\nhttp://boxen.math.washington.edu/home/sagemath/sage-mirror/linux/64bit/sage-6.3-x86_64-Linux-Ubuntu_10.04_x86_64.tar.gz\n\nand it appears not to include libgfortran.\n\nI obtained the same ImportError as above when attempting to import numpy, and installing libgfortran3 fixed the problem.",
    "created_at": "2014-08-30T07:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70254",
    "user": "https://trac.sagemath.org/admin/accounts/users/tcoffee"
}
```

Correct me if this issue has been superseded, but I just installed this binary

http://boxen.math.washington.edu/home/sagemath/sage-mirror/linux/64bit/sage-6.3-x86_64-Linux-Ubuntu_10.04_x86_64.tar.gz

and it appears not to include libgfortran.

I obtained the same ImportError as above when attempting to import numpy, and installing libgfortran3 fixed the problem.



---

archive/issue_comments_070255.json:
```json
{
    "body": "Replying to [comment:11 tcoffee]:\n> Correct me if this issue has been superseded, but I just installed this binary\n> \n> http://boxen.math.washington.edu/home/sagemath/sage-mirror/linux/64bit/sage-6.3-x86_64-Linux-Ubuntu_10.04_x86_64.tar.gz\n> \n> and it appears not to include libgfortran.\n\nI imagine libgfortran comes from the gcc spkg nowadays, and this binary has no trace of gcc in it.",
    "created_at": "2014-08-30T08:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70255",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:11 tcoffee]:
> Correct me if this issue has been superseded, but I just installed this binary
> 
> http://boxen.math.washington.edu/home/sagemath/sage-mirror/linux/64bit/sage-6.3-x86_64-Linux-Ubuntu_10.04_x86_64.tar.gz
> 
> and it appears not to include libgfortran.

I imagine libgfortran comes from the gcc spkg nowadays, and this binary has no trace of gcc in it.



---

archive/issue_comments_070256.json:
```json
{
    "body": "Yes, binaries *should* be built with `SAGE_INSTALL_GCC=yes`, but apparently that's not the case.",
    "created_at": "2014-08-30T08:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70256",
    "user": "https://github.com/jdemeyer"
}
```

Yes, binaries *should* be built with `SAGE_INSTALL_GCC=yes`, but apparently that's not the case.



---

archive/issue_comments_070257.json:
```json
{
    "body": "Replying to [comment:13 jdemeyer]:\n> Yes, binaries *should* be built with `SAGE_INSTALL_GCC=yes`, but apparently that's not the case.\n\nDoes that make sense for distros with a more recent toolchain than Sage currently ships?",
    "created_at": "2014-08-30T11:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70257",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:13 jdemeyer]:
> Yes, binaries *should* be built with `SAGE_INSTALL_GCC=yes`, but apparently that's not the case.

Does that make sense for distros with a more recent toolchain than Sage currently ships?



---

archive/issue_comments_070258.json:
```json
{
    "body": "Replying to [comment:14 leif]:\n> Does that make sense for distros with a more recent toolchain than Sage currently ships?\nYes, because you need to ship the libraries that you link against, such as `libgfortran.so`.",
    "created_at": "2014-08-30T11:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70258",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:14 leif]:
> Does that make sense for distros with a more recent toolchain than Sage currently ships?
Yes, because you need to ship the libraries that you link against, such as `libgfortran.so`.



---

archive/issue_comments_070259.json:
```json
{
    "body": "Replying to [comment:15 jdemeyer]:\n> Replying to [comment:14 leif]:\n> > Does that make sense for distros with a more recent toolchain than Sage currently ships?\n> Yes, because you need to ship the libraries that you link against, such as `libgfortran.so`.\n\nWell, these should be the \"native\" ones from the distro the binary was built on (and for).\n\nSo unless the distro's toolchain is exceptionally outdated or broken (I also wouldn't say Lucid's is), I think we shouldn't `SAGE_INSTALL_GCC`.\n\nIf we ship older libraries than the distro by default comes with / uses, we're IMHO just asking for trouble.  (Not all of them are properly versioned w.r.t. dynamically loading the \"correct\" one, IIRC.  So running other applications from within the Sage environment might fail.)\n\n\n\n\nRequiring the user installing a Sage binary to eventually also install some stuff with the distro's package manager first isn't too much to ask for, provided that's sufficiently documented and/or a (start-up) script tells her/him to do so...\n\nAfter all, the whole point of building binaries for *specific* distros is that we know  which, or can expect that such and such (versions of) libraries and programs are present (or at least available through the package manager).",
    "created_at": "2014-08-30T12:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70259",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:15 jdemeyer]:
> Replying to [comment:14 leif]:
> > Does that make sense for distros with a more recent toolchain than Sage currently ships?
> Yes, because you need to ship the libraries that you link against, such as `libgfortran.so`.

Well, these should be the "native" ones from the distro the binary was built on (and for).

So unless the distro's toolchain is exceptionally outdated or broken (I also wouldn't say Lucid's is), I think we shouldn't `SAGE_INSTALL_GCC`.

If we ship older libraries than the distro by default comes with / uses, we're IMHO just asking for trouble.  (Not all of them are properly versioned w.r.t. dynamically loading the "correct" one, IIRC.  So running other applications from within the Sage environment might fail.)




Requiring the user installing a Sage binary to eventually also install some stuff with the distro's package manager first isn't too much to ask for, provided that's sufficiently documented and/or a (start-up) script tells her/him to do so...

After all, the whole point of building binaries for *specific* distros is that we know  which, or can expect that such and such (versions of) libraries and programs are present (or at least available through the package manager).



---

archive/issue_comments_070260.json:
```json
{
    "body": "Replying to [comment:16 leif]:\n> or at least available through the package manager\nThat's exactly the whole point here, this isn't about versions. We *do not want* that users need to install something with their package manager. Sage binaries should work \"out of the box\".",
    "created_at": "2014-08-30T12:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70260",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:16 leif]:
> or at least available through the package manager
That's exactly the whole point here, this isn't about versions. We *do not want* that users need to install something with their package manager. Sage binaries should work "out of the box".



---

archive/issue_comments_070261.json:
```json
{
    "body": "Replying to [comment:17 jdemeyer]:\n> Replying to [comment:16 leif]:\n> > or at least available through the package manager\n> That's exactly the whole point here, this isn't about versions. We *do not want* that users need to install something with their package manager. Sage binaries should work \"out of the box\".\n\n\"Installing [with the distro's package manager]\" (usually) doesn't mean building/compiling something, which is the point of bdists.\n\nThe Sage binary for Foonux 17.12 shouldn't contain any *part of that* distro, because that'd just be redundant (not to mention potentially bypassing security updates etc.).\n\nBut my main point was that *using Sage's GCC* for building bdists in general is not the same as shipping *the distro's* libraries -- the former may cause further (or different) trouble.  So if you think we should ship libgfortran, just copy the system's one into `$SAGE_LOCAL/lib`; no need to install Sage's GCC just for that reason, whose libgfortran might (or typically will) be even older than the system's.",
    "created_at": "2014-08-30T12:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70261",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:17 jdemeyer]:
> Replying to [comment:16 leif]:
> > or at least available through the package manager
> That's exactly the whole point here, this isn't about versions. We *do not want* that users need to install something with their package manager. Sage binaries should work "out of the box".

"Installing [with the distro's package manager]" (usually) doesn't mean building/compiling something, which is the point of bdists.

The Sage binary for Foonux 17.12 shouldn't contain any *part of that* distro, because that'd just be redundant (not to mention potentially bypassing security updates etc.).

But my main point was that *using Sage's GCC* for building bdists in general is not the same as shipping *the distro's* libraries -- the former may cause further (or different) trouble.  So if you think we should ship libgfortran, just copy the system's one into `$SAGE_LOCAL/lib`; no need to install Sage's GCC just for that reason, whose libgfortran might (or typically will) be even older than the system's.



---

archive/issue_comments_070262.json:
```json
{
    "body": "P.S.:  If you want to run Sage really \"out of the box\", use one of the Live CDs (or probably the VirtualBox image), or SMC... ;-)\n\nThe only flaw with the bdists currently is that Sage apparently doesn't check on (first) start-up whether its prerequisites are present, instead a probably mysterious or hard to understand error might(!) occur.  That's the bug.",
    "created_at": "2014-08-30T13:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70262",
    "user": "https://github.com/nexttime"
}
```

P.S.:  If you want to run Sage really "out of the box", use one of the Live CDs (or probably the VirtualBox image), or SMC... ;-)

The only flaw with the bdists currently is that Sage apparently doesn't check on (first) start-up whether its prerequisites are present, instead a probably mysterious or hard to understand error might(!) occur.  That's the bug.



---

archive/issue_comments_070263.json:
```json
{
    "body": "Replying to [comment:18 leif]:\n> \"Installing [with the distro's package manager]\" (usually) doesn't mean building/compiling something, which is the point of bdists.\n> \n> The Sage binary for Foonux 17.12 shouldn't contain any *part of that* distro, because that'd just be redundant (not to mention potentially bypassing security updates etc.).\n> \n> But my main point was that *using Sage's GCC* for building bdists in general is not the same as shipping *the distro's* libraries -- the former may cause further (or different) trouble.  So if you think we should ship libgfortran, just copy the system's one into `$SAGE_LOCAL/lib`; no need to install Sage's GCC just for that reason, whose libgfortran might (or typically will) be even older than the system's.\n\nThis discussion should really be moved to `sage-release` instead of this ticket.",
    "created_at": "2014-08-30T13:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70263",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:18 leif]:
> "Installing [with the distro's package manager]" (usually) doesn't mean building/compiling something, which is the point of bdists.
> 
> The Sage binary for Foonux 17.12 shouldn't contain any *part of that* distro, because that'd just be redundant (not to mention potentially bypassing security updates etc.).
> 
> But my main point was that *using Sage's GCC* for building bdists in general is not the same as shipping *the distro's* libraries -- the former may cause further (or different) trouble.  So if you think we should ship libgfortran, just copy the system's one into `$SAGE_LOCAL/lib`; no need to install Sage's GCC just for that reason, whose libgfortran might (or typically will) be even older than the system's.

This discussion should really be moved to `sage-release` instead of this ticket.



---

archive/issue_comments_070264.json:
```json
{
    "body": "Replying to [comment:20 jdemeyer]:\n> This discussion should really be moved to `sage-release` instead of this ticket.\n\nI was thinking of replying there, but thought it was more on topic (or had the right audience) here.\n\nWe should probably invite fbissey, Snark and Jan Groenewald et al. to the party, in case they're not already cc'ed (haven't checked).",
    "created_at": "2014-08-30T13:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70264",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:20 jdemeyer]:
> This discussion should really be moved to `sage-release` instead of this ticket.

I was thinking of replying there, but thought it was more on topic (or had the right audience) here.

We should probably invite fbissey, Snark and Jan Groenewald et al. to the party, in case they're not already cc'ed (haven't checked).



---

archive/issue_comments_070265.json:
```json
{
    "body": "Once again, lack of fortran or lapack or something causes trouble - see [this discussion](https://groups.google.com/forum/#!topic/sage-support/2BrsaLxkRIk), which references this ticket.",
    "created_at": "2014-09-09T12:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70265",
    "user": "https://github.com/kcrisman"
}
```

Once again, lack of fortran or lapack or something causes trouble - see [this discussion](https://groups.google.com/forum/#!topic/sage-support/2BrsaLxkRIk), which references this ticket.



---

archive/issue_comments_070266.json:
```json
{
    "body": "Replying to [comment:22 kcrisman]:\n> Once again, lack of fortran or lapack or something causes trouble - see [this discussion](https://groups.google.com/forum/#!topic/sage-support/2BrsaLxkRIk), which references this ticket.\nNot once again, it's the same issue as [comment:13]. It has been fixed in the sense that the next binaries which will be released will not have this problem.",
    "created_at": "2014-09-09T12:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70266",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:22 kcrisman]:
> Once again, lack of fortran or lapack or something causes trouble - see [this discussion](https://groups.google.com/forum/#!topic/sage-support/2BrsaLxkRIk), which references this ticket.
Not once again, it's the same issue as [comment:13]. It has been fixed in the sense that the next binaries which will be released will not have this problem.



---

archive/issue_comments_070267.json:
```json
{
    "body": "See also [this recent question on ask.sagemath.org](http://ask.sagemath.org/question/24286/cant-get-plotting-to-work/) showing that the problem still exists with 6.3 Ubuntu binary.",
    "created_at": "2014-09-27T11:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70267",
    "user": "https://trac.sagemath.org/admin/accounts/users/tmonteil"
}
```

See also [this recent question on ask.sagemath.org](http://ask.sagemath.org/question/24286/cant-get-plotting-to-work/) showing that the problem still exists with 6.3 Ubuntu binary.



---

archive/issue_comments_070268.json:
```json
{
    "body": "Replying to [comment:24 tmonteil]:\n> See also [this recent question on ask.sagemath.org](http://ask.sagemath.org/question/24286/cant-get-plotting-to-work/) showing that the problem still exists with 6.3 Ubuntu binary.\nYes of course it does, in case you haven't read the recent comments: It has been fixed in the sense that the **next binaries** which will be released will not have this problem.",
    "created_at": "2014-09-27T20:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8049#issuecomment-70268",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:24 tmonteil]:
> See also [this recent question on ask.sagemath.org](http://ask.sagemath.org/question/24286/cant-get-plotting-to-work/) showing that the problem still exists with 6.3 Ubuntu binary.
Yes of course it does, in case you haven't read the recent comments: It has been fixed in the sense that the **next binaries** which will be released will not have this problem.
