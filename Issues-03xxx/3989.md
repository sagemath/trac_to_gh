# Issue 3989: [with spkg, with positive review] autotools issues with gd-2.0.35

archive/issues_003989.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe new hg package has various issues and we need to run a bunch of autohell and libtool commands to create proper sources. The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/gd-2.0.35.p1.spkg\n\nfixes that issue. It builds on the Itanium boxen that up to now failed.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3989\n\n",
    "closed_at": "2008-08-29T09:11:14Z",
    "created_at": "2008-08-29T08:54:08Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, with positive review] autotools issues with gd-2.0.35",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3989",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The new hg package has various issues and we need to run a bunch of autohell and libtool commands to create proper sources. The spkg at

http://sage.math.washington.edu/home/mabshoff/gd-2.0.35.p1.spkg

fixes that issue. It builds on the Itanium boxen that up to now failed.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3989





---

archive/issue_comments_028620.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-29T08:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3989#issuecomment-28620",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028621.json:
```json
{
    "body": "The problem is the following with gd *2.0.35*:\n\n```\n\n** Configuration summary for gd 2.0.34:\n\n   Support for PNG library:          yes\n   Support for JPEG library:         no\n   Support for Freetype 2.x library: yes\n   Support for Fontconfig library:   no\n   Support for Xpm library:          no\n   Support for pthreads:             yes\n\nconfigure: creating ./config.status\nconfig.status: creating Makefile\nconfig.status: creating config/Makefile\nconfig.status: creating config/gdlib-config\nconfig.status: creating test/Makefile\nconfig.status: creating config.h\nconfig.status: executing depfiles commands\nmake[2]: Entering directory `/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src'\ncd . && /bin/sh /scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src/config/missing --run aclocal-1.9 -I config\ncd . && /bin/sh /scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src/config/missing --run autoconf\n cd . && /bin/sh /scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src/config/missing --run automake-1.9 --foreign \n/bin/sh ./config.status --recheck\nrunning CONFIG_SHELL=/bin/sh /bin/sh ./configure  --prefix=/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local --without-jpeg --without-x --with-zlib=/scratch/mabs\nhoff/release-cycle/sage-3.1.2.alpha1/local --with-freetype2=/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local CC=gcc CFLAGS= -fPIC -g -I\"/scratch/mabshoff/releas\ne-cycle/sage-3.1.2.alpha1/local/include\" -I/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/include/freetype2/ LDFLAGS= CXX=g++  --no-create --no-recursion\nchecking\n```\nWith the fix:\n\n```\n** Configuration summary for gd 2.0.35:\n\n   Support for PNG library:          yes\n   Support for JPEG library:         no\n   Support for Freetype 2.x library: yes\n   Support for Fontconfig library:   no\n   Support for Xpm library:          no\n   Support for pthreads:             yes\n\nconfigure: creating ./config.status\nconfig.status: creating Makefile\nconfig.status: creating config/Makefile\nconfig.status: creating config/gdlib-config\nconfig.status: creating test/Makefile\nconfig.status: creating config.h\nconfig.status: executing depfiles commands\nmake[2]: Entering directory `/home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/spkg/build/gd-2.0.35.p1/src'\ncd . && /bin/sh /home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/spkg/build/gd-2.0.35.p1/src/config/missing --run autoheader\n/home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/spkg/build/gd-2.0.35.p1/src/config/missing: line 46: autoheader: command not found\nWARNING: `autoheader' is missing on your system.  You should only need it if\n         you modified `acconfig.h' or `configure.ac'.  You might want\n         to install the `Autoconf' and `GNU m4' packages.  Grab them\n         from any GNU archive site.\nrm -f stamp-h1\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-08-29T08:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3989#issuecomment-28621",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The problem is the following with gd *2.0.35*:

```

** Configuration summary for gd 2.0.34:

   Support for PNG library:          yes
   Support for JPEG library:         no
   Support for Freetype 2.x library: yes
   Support for Fontconfig library:   no
   Support for Xpm library:          no
   Support for pthreads:             yes

configure: creating ./config.status
config.status: creating Makefile
config.status: creating config/Makefile
config.status: creating config/gdlib-config
config.status: creating test/Makefile
config.status: creating config.h
config.status: executing depfiles commands
make[2]: Entering directory `/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src'
cd . && /bin/sh /scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src/config/missing --run aclocal-1.9 -I config
cd . && /bin/sh /scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src/config/missing --run autoconf
 cd . && /bin/sh /scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src/config/missing --run automake-1.9 --foreign 
/bin/sh ./config.status --recheck
running CONFIG_SHELL=/bin/sh /bin/sh ./configure  --prefix=/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local --without-jpeg --without-x --with-zlib=/scratch/mabs
hoff/release-cycle/sage-3.1.2.alpha1/local --with-freetype2=/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local CC=gcc CFLAGS= -fPIC -g -I"/scratch/mabshoff/releas
e-cycle/sage-3.1.2.alpha1/local/include" -I/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/include/freetype2/ LDFLAGS= CXX=g++  --no-create --no-recursion
checking
```
With the fix:

```
** Configuration summary for gd 2.0.35:

   Support for PNG library:          yes
   Support for JPEG library:         no
   Support for Freetype 2.x library: yes
   Support for Fontconfig library:   no
   Support for Xpm library:          no
   Support for pthreads:             yes

configure: creating ./config.status
config.status: creating Makefile
config.status: creating config/Makefile
config.status: creating config/gdlib-config
config.status: creating test/Makefile
config.status: creating config.h
config.status: executing depfiles commands
make[2]: Entering directory `/home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/spkg/build/gd-2.0.35.p1/src'
cd . && /bin/sh /home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/spkg/build/gd-2.0.35.p1/src/config/missing --run autoheader
/home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/spkg/build/gd-2.0.35.p1/src/config/missing: line 46: autoheader: command not found
WARNING: `autoheader' is missing on your system.  You should only need it if
         you modified `acconfig.h' or `configure.ac'.  You might want
         to install the `Autoconf' and `GNU m4' packages.  Grab them
         from any GNU archive site.
rm -f stamp-h1
```

Cheers,

Michael



---

archive/issue_comments_028622.json:
```json
{
    "body": "Looks good. I don't have an Itanium to test on, but Michael assures me that it works on the machine where it had previously failed. I also looked at the only change in the spkg, which seems reasonable, and built it on my machine, which doesn't seem to cause any trouble.",
    "created_at": "2008-08-29T09:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3989#issuecomment-28622",
    "user": "https://github.com/craigcitro"
}
```

Looks good. I don't have an Itanium to test on, but Michael assures me that it works on the machine where it had previously failed. I also looked at the only change in the spkg, which seems reasonable, and built it on my machine, which doesn't seem to cause any trouble.



---

archive/issue_events_009139.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-29T09:11:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3989",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3989#event-9139"
}
```



---

archive/issue_comments_028623.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-29T09:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3989#issuecomment-28623",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha2



---

archive/issue_comments_028624.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-29T09:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3989#issuecomment-28624",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
