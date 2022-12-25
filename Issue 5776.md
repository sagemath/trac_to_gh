# Issue 5776: sage-location ought to rewrite loads of files in $SAGE_LOCAL/bin

archive/issues_005776.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @nexttime\n\nThe following is from a 3.4.1.rc3 build that was -bdisted from 3.4.1.rc2. There are **loads** of files that still have 3.4.1.rc2 in various config files:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3/local/bin$ grep -r \"sage-3.4.1.rc2\" *  | grep --invert-match Binary\nfreetype-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local\nfreetype-config:    major=`grep define /scratch/mabshoff/sage-3.4.1.rc2/local/include/freetype2/freetype/freetype.h \\\nfreetype-config:    minor=`grep define /scratch/mabshoff/sage-3.4.1.rc2/local/include/freetype2/freetype/freetype.h \\\nfreetype-config:    patch=`grep define /scratch/mabshoff/sage-3.4.1.rc2/local/include/freetype2/freetype/freetype.h \\\ngdlib-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local\ngdlib-config:\techo  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -Wl,--rpath -Wl,/scratch/mabshoff/sage-3.4.1.rc2/local/lib  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib \ngdlib-config:\techo \"ldflags:     -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -Wl,--rpath -Wl,/scratch/mabshoff/sage-3.4.1.rc2/local/lib  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib \"\nghmm-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local\ngivaro-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local\ngivaro-config:       \techo -I${includedir} -I/scratch/mabshoff/sage-3.4.1.rc2/local//include\ngivaro-config:       \techo -L${libdir} -lgivaro -L/scratch/mabshoff/sage-3.4.1.rc2/local//lib -lgmp \ngivaro-makefile:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local\ngivaro-makefile:OPTFLAGS = -I/scratch/mabshoff/sage-3.4.1.rc2/local//include  -fPIC -I\"/scratch/mabshoff/sage-3.4.1.rc2/local/include\"\ngivaro-makefile:GMP_CFLAGS = -I/scratch/mabshoff/sage-3.4.1.rc2/local//include\ngivaro-makefile:GMP_LIBS   = -L/scratch/mabshoff/sage-3.4.1.rc2/local//lib -lgmp\ngpg-error-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local\ngphelp:$datadir= \"/scratch/mabshoff/sage-3.4.1.rc2/local/share/pari\";\ngsl-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local\nlibgcrypt-config:prefix=\"/scratch/mabshoff/sage-3.4.1.rc2/local\"\nlibgcrypt-config:gpg_error_libs=\"-L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgpg-error\"\nlibgcrypt-config:gpg_error_cflags=\"-I/scratch/mabshoff/sage-3.4.1.rc2/local/include\"\nlibgnutls-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local\nlibgnutls-config:gnutls_libs=\"-L${exec_prefix}/lib -lgnutls  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -lgpg-error \"\nlibgnutls-config:gnutls_cflags=\"-I/scratch/mabshoff/sage-3.4.1.rc2/local/include  -I${prefix}/include\"\nlibgnutls-extra-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local\nlibgnutls-extra-config:gnutls_libs=\"-L${exec_prefix}/lib -lgnutls-extra -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lopencdk -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgpg-error -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lz -R/scratch/mabshoff/sage-3.4.1.rc2/local/lib  -L${exec_prefix}/lib -lgnutls  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -lgpg-error \"\nlibgnutls-extra-config:gnutls_cflags=\"-I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I${prefix}/include\"\nlibpng12-config:prefix=\"/scratch/mabshoff/sage-3.4.1.rc2/local\"\nlibpng-config:prefix=\"/scratch/mabshoff/sage-3.4.1.rc2/local\"\nlinbox-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local\nlinbox-config:       \techo -I${includedir} -I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I/scratch/mabshoff/sage-3.4.1.rc2/local/include   \nlinbox-config:       \techo -L${libdir} -llinbox   -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lntl -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgivaro  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgmpxx -lgmp -lcblas -latlas\nmaxima:  prefix=`unixize \"/scratch/mabshoff/sage-3.4.1.rc2/local\"`\nmaxima:  top_srcdir=`unixize \"/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/maxima-5.16.3/src\"`\nopencdk-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local\nopencdk-config:opencdk_libs=\"-L${exec_prefix}/lib -lopencdk -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -lgpg-error  -lz\"\nopencdk-config:opencdk_cflags=\"-I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I${prefix}/include\"\nqd-config:prefix=\"/scratch/mabshoff/sage-3.4.1.rc2/local\"\nqd-config:srcdir=\"/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/quaddouble-2.2.p9/src\"\nqd-config:builddir=\"/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/quaddouble-2.2.p9/src\"\nqd-config:configure_args=\" '--prefix=/scratch/mabshoff/sage-3.4.1.rc2/local' '--enable-fortran=no' 'CXX=g++' 'CXXFLAGS=-fPIC -O3 -Dx86' 'LDFLAGS=' 'CC=gcc'\"\nR:R_HOME_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R\nR:#R_HOME_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R\nR:R_SHARE_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R/share\nR:R_INCLUDE_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R/include\nR:R_DOC_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R/doc\nrmaxima:  MAXIMA_SHAREDIR=/scratch/mabshoff/sage-3.4.1.rc2/local/share/maxima/5.16.3/share\nrmaxima:  MAXIMA_SHAREDIR=/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/maxima-5.16.3/src/share\nxmaxima:set autoconf(prefix) \"/scratch/mabshoff/sage-3.4.1.rc2/local\"\nxmaxima:set autoconf(exec_prefix) \"/scratch/mabshoff/sage-3.4.1.rc2/local\"\nxmaxima:set autoconf(libdir) \"/scratch/mabshoff/sage-3.4.1.rc2/local/lib\"\nxmaxima:set autoconf(libexecdir) \"/scratch/mabshoff/sage-3.4.1.rc2/local/libexec\"\nxmaxima:set autoconf(datadir) \"/scratch/mabshoff/sage-3.4.1.rc2/local/share\"\nxmaxima:set autoconf(infodir) \"/scratch/mabshoff/sage-3.4.1.rc2/local/info\"\n```\n\n\nThis causes loads of odd bugs when installing/upgrading from a bdist build, i.e. the location to R_HOME is hardcoded which might be involved with #5246 and #5634.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5776\n\n",
    "created_at": "2009-04-13T07:55:44Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage-location ought to rewrite loads of files in $SAGE_LOCAL/bin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5776",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @nexttime

The following is from a 3.4.1.rc3 build that was -bdisted from 3.4.1.rc2. There are **loads** of files that still have 3.4.1.rc2 in various config files:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3/local/bin$ grep -r "sage-3.4.1.rc2" *  | grep --invert-match Binary
freetype-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
freetype-config:    major=`grep define /scratch/mabshoff/sage-3.4.1.rc2/local/include/freetype2/freetype/freetype.h \
freetype-config:    minor=`grep define /scratch/mabshoff/sage-3.4.1.rc2/local/include/freetype2/freetype/freetype.h \
freetype-config:    patch=`grep define /scratch/mabshoff/sage-3.4.1.rc2/local/include/freetype2/freetype/freetype.h \
gdlib-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
gdlib-config:	echo  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -Wl,--rpath -Wl,/scratch/mabshoff/sage-3.4.1.rc2/local/lib  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib 
gdlib-config:	echo "ldflags:     -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -Wl,--rpath -Wl,/scratch/mabshoff/sage-3.4.1.rc2/local/lib  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib "
ghmm-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
givaro-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
givaro-config:       	echo -I${includedir} -I/scratch/mabshoff/sage-3.4.1.rc2/local//include
givaro-config:       	echo -L${libdir} -lgivaro -L/scratch/mabshoff/sage-3.4.1.rc2/local//lib -lgmp 
givaro-makefile:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
givaro-makefile:OPTFLAGS = -I/scratch/mabshoff/sage-3.4.1.rc2/local//include  -fPIC -I"/scratch/mabshoff/sage-3.4.1.rc2/local/include"
givaro-makefile:GMP_CFLAGS = -I/scratch/mabshoff/sage-3.4.1.rc2/local//include
givaro-makefile:GMP_LIBS   = -L/scratch/mabshoff/sage-3.4.1.rc2/local//lib -lgmp
gpg-error-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
gphelp:$datadir= "/scratch/mabshoff/sage-3.4.1.rc2/local/share/pari";
gsl-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
libgcrypt-config:prefix="/scratch/mabshoff/sage-3.4.1.rc2/local"
libgcrypt-config:gpg_error_libs="-L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgpg-error"
libgcrypt-config:gpg_error_cflags="-I/scratch/mabshoff/sage-3.4.1.rc2/local/include"
libgnutls-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
libgnutls-config:gnutls_libs="-L${exec_prefix}/lib -lgnutls  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -lgpg-error "
libgnutls-config:gnutls_cflags="-I/scratch/mabshoff/sage-3.4.1.rc2/local/include  -I${prefix}/include"
libgnutls-extra-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
libgnutls-extra-config:gnutls_libs="-L${exec_prefix}/lib -lgnutls-extra -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lopencdk -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgpg-error -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lz -R/scratch/mabshoff/sage-3.4.1.rc2/local/lib  -L${exec_prefix}/lib -lgnutls  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -lgpg-error "
libgnutls-extra-config:gnutls_cflags="-I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I${prefix}/include"
libpng12-config:prefix="/scratch/mabshoff/sage-3.4.1.rc2/local"
libpng-config:prefix="/scratch/mabshoff/sage-3.4.1.rc2/local"
linbox-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
linbox-config:       	echo -I${includedir} -I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I/scratch/mabshoff/sage-3.4.1.rc2/local/include   
linbox-config:       	echo -L${libdir} -llinbox   -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lntl -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgivaro  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgmpxx -lgmp -lcblas -latlas
maxima:  prefix=`unixize "/scratch/mabshoff/sage-3.4.1.rc2/local"`
maxima:  top_srcdir=`unixize "/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/maxima-5.16.3/src"`
opencdk-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
opencdk-config:opencdk_libs="-L${exec_prefix}/lib -lopencdk -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -lgpg-error  -lz"
opencdk-config:opencdk_cflags="-I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I${prefix}/include"
qd-config:prefix="/scratch/mabshoff/sage-3.4.1.rc2/local"
qd-config:srcdir="/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/quaddouble-2.2.p9/src"
qd-config:builddir="/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/quaddouble-2.2.p9/src"
qd-config:configure_args=" '--prefix=/scratch/mabshoff/sage-3.4.1.rc2/local' '--enable-fortran=no' 'CXX=g++' 'CXXFLAGS=-fPIC -O3 -Dx86' 'LDFLAGS=' 'CC=gcc'"
R:R_HOME_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R
R:#R_HOME_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R
R:R_SHARE_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R/share
R:R_INCLUDE_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R/include
R:R_DOC_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R/doc
rmaxima:  MAXIMA_SHAREDIR=/scratch/mabshoff/sage-3.4.1.rc2/local/share/maxima/5.16.3/share
rmaxima:  MAXIMA_SHAREDIR=/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/maxima-5.16.3/src/share
xmaxima:set autoconf(prefix) "/scratch/mabshoff/sage-3.4.1.rc2/local"
xmaxima:set autoconf(exec_prefix) "/scratch/mabshoff/sage-3.4.1.rc2/local"
xmaxima:set autoconf(libdir) "/scratch/mabshoff/sage-3.4.1.rc2/local/lib"
xmaxima:set autoconf(libexecdir) "/scratch/mabshoff/sage-3.4.1.rc2/local/libexec"
xmaxima:set autoconf(datadir) "/scratch/mabshoff/sage-3.4.1.rc2/local/share"
xmaxima:set autoconf(infodir) "/scratch/mabshoff/sage-3.4.1.rc2/local/info"
```


This causes loads of odd bugs when installing/upgrading from a bdist build, i.e. the location to R_HOME is hardcoded which might be involved with #5246 and #5634.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5776





---

archive/issue_comments_045079.json:
```json
{
    "body": "If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5776#issuecomment-45079",
    "user": "https://github.com/williamstein"
}
```

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_045080.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5776#issuecomment-45080",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_045081.json:
```json
{
    "body": "See #9210 for a rewrite of sage-location that takes care of resetting pkg-config files.",
    "created_at": "2010-06-11T06:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5776#issuecomment-45081",
    "user": "https://github.com/jasongrout"
}
```

See #9210 for a rewrite of sage-location that takes care of resetting pkg-config files.



---

archive/issue_comments_045082.json:
```json
{
    "body": "See http://blogs.sun.com/dipol/entry/dynamic_libraries_rpath_and_mac for some suggestions on how to make things relocateable.",
    "created_at": "2010-06-11T19:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5776#issuecomment-45082",
    "user": "https://github.com/jasongrout"
}
```

See http://blogs.sun.com/dipol/entry/dynamic_libraries_rpath_and_mac for some suggestions on how to make things relocateable.



---

archive/issue_comments_045083.json:
```json
{
    "body": "Changing keywords from \"\" to \"relocation move moving SAGE_ROOT\".",
    "created_at": "2010-10-20T12:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5776#issuecomment-45083",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "" to "relocation move moving SAGE_ROOT".



---

archive/issue_comments_045084.json:
```json
{
    "body": "Remove assignee mabshoff.",
    "created_at": "2010-10-20T12:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5776#issuecomment-45084",
    "user": "https://github.com/nexttime"
}
```

Remove assignee mabshoff.



---

archive/issue_comments_045085.json:
```json
{
    "body": "Is this ticket still necessary?  It might be helpful to break this into tickets by spkg or something.\n\nR is already probably on the docket - se #8274 and #10967, for instance.",
    "created_at": "2011-06-21T14:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5776#issuecomment-45085",
    "user": "https://github.com/kcrisman"
}
```

Is this ticket still necessary?  It might be helpful to break this into tickets by spkg or something.

R is already probably on the docket - se #8274 and #10967, for instance.



---

archive/issue_events_013550.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5776#event-13550"
}
```



---

archive/issue_events_013551.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5776#event-13551"
}
```



---

archive/issue_events_013552.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5776#event-13552"
}
```



---

archive/issue_events_013553.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5776#event-13553"
}
```



---

archive/issue_events_013554.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5776#event-13554"
}
```



---

archive/issue_events_013555.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5776#event-13555"
}
```



---

archive/issue_events_013556.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5776#event-13556"
}
```



---

archive/issue_comments_045086.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-04-11T09:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5776#issuecomment-45086",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_045087.json:
```json
{
    "body": "`sage-location` is obsolete",
    "created_at": "2016-04-11T09:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5776#issuecomment-45087",
    "user": "https://github.com/jdemeyer"
}
```

`sage-location` is obsolete



---

archive/issue_comments_045088.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-04-11T09:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5776#issuecomment-45088",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_013557.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2016-04-11T09:52:35Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5776#event-13557"
}
```



---

archive/issue_events_013558.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2016-04-11T09:52:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5776#event-13558"
}
```



---

archive/issue_comments_045089.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5776#issuecomment-45089",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_013559.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-06-12T12:02:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5776",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5776#event-13559"
}
```
