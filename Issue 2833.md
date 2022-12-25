# Issue 2833: Linbox build failure on OSX 10.4 intel

archive/issues_002833.json:
```json
{
    "body": "Assignee: @ClementPernet\n\nBuilding the sage 3.0.alpha1 tarball failed at linbox  on OSX 10.4 intel with gcc\nversion 4.0.1.\n\n\n\n\n```\n/bin/sh ./libtool --tag=CXX   --mode=compile g++ -DPACKAGE_NAME=\\\"liblinboxwrap\\\" -DPACKAGE_TARNAME=\\\"liblinboxwrap\\\" -DPACKAGE_VERSION=\\\"0.0.1\\\" -DPACKAGE_STRING=\\\"liblinboxwrap\\ 0.0.1\\\" -DPACKAGE_BUGREPORT=\\\"\\\" -DPACKAGE=\\\"liblinboxwrap\\\" -DVERSION=\\\"0.0.1\\\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_BLAS=1 -I.   -g -I\"/Users/kantor/sage-3.0.alpha1/local/include/linbox\" -I\"/Users/kantor/sage-3.0.alpha1/local\"/include  -g -fPIC -I\"/Users/kantor/sage-3.0.alpha1/local/include\" -I\"/Users/kantor/sage-3.0.alpha1/local/include/linbox\"  -L\"/Users/kantor/sage-3.0.alpha1/local/lib\" -MT linbox_wrap.lo -MD -MP -MF .deps/linbox_wrap.Tpo -c -o linbox_wrap.lo `test -f 'src/linbox_wrap.cpp' || echo './'`src/linbox_wrap.cpp\nmkdir .libs\n g++ -DPACKAGE_NAME=\\\"liblinboxwrap\\\" -DPACKAGE_TARNAME=\\\"liblinboxwrap\\\" -DPACKAGE_VERSION=\\\"0.0.1\\\" \"-DPACKAGE_STRING=\\\"liblinboxwrap 0.0.1\\\"\" -DPACKAGE_BUGREPORT=\\\"\\\" -DPACKAGE=\\\"liblinboxwrap\\\" -DVERSION=\\\"0.0.1\\\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_BLAS=1 -I. -g -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -I/Users/kantor/sage-3.0.alpha1/local/include -g -fPIC -I/Users/kantor/sage-3.0.alpha1/local/include -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -L/Users/kantor/sage-3.0.alpha1/local/lib -MT linbox_wrap.lo -MD -MP -MF .deps/linbox_wrap.Tpo -c src/linbox_wrap.cpp  -fno-common -DPIC -o .libs/linbox_wrap.o\n g++ -DPACKAGE_NAME=\\\"liblinboxwrap\\\" -DPACKAGE_TARNAME=\\\"liblinboxwrap\\\" -DPACKAGE_VERSION=\\\"0.0.1\\\" \"-DPACKAGE_STRING=\\\"liblinboxwrap 0.0.1\\\"\" -DPACKAGE_BUGREPORT=\\\"\\\" -DPACKAGE=\\\"liblinboxwrap\\\" -DVERSION=\\\"0.0.1\\\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_BLAS=1 -I. -g -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -I/Users/kantor/sage-3.0.alpha1/local/include -g -fPIC -I/Users/kantor/sage-3.0.alpha1/local/include -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -L/Users/kantor/sage-3.0.alpha1/local/lib -MT linbox_wrap.lo -MD -MP -MF .deps/linbox_wrap.Tpo -c src/linbox_wrap.cpp -o linbox_wrap.o >/dev/null 2>&1\nmv -f .deps/linbox_wrap.Tpo .deps/linbox_wrap.Plo\n/bin/sh ./libtool --tag=CXX   --mode=link g++  -g -fPIC -I\"/Users/kantor/sage-3.0.alpha1/local/include\" -I\"/Users/kantor/sage-3.0.alpha1/local/include/linbox\"  -L\"/Users/kantor/sage-3.0.alpha1/local/lib\" -version-info 0:0:0  -o liblinboxwrap.la -rpath /Users/kantor/sage-3.0.alpha1/local/lib linbox_wrap.lo -llinbox /usr/lib/libcblas.dylib \ng++ -dynamiclib -single_module ${wl}-flat_namespace ${wl}-undefined ${wl}suppress -o .libs/liblinboxwrap.0.0.0.dylib  .libs/linbox_wrap.o  -L/Users/kantor/sage-3.0.alpha1/local/lib /Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib  -install_name  /Users/kantor/sage-3.0.alpha1/local/lib/liblinboxwrap.0.dylib -Wl,-compatibility_version -Wl,1 -Wl,-current_version -Wl,1.0\nld: multiple definitions of symbol __ZN6LinBox11commentatorE\n.libs/linbox_wrap.o definition of __ZN6LinBox11commentatorE in section (__DATA,__common)\n/Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib(single module) definition of __ZN6LinBox11commentatorE\n/usr/bin/libtool: internal link edit command failed\nmake[2]: *** [liblinboxwrap.la] Error 1\nError building linboxwrap\n/bin/sh ./libtool --tag=CXX   --mode=link g++  -g -fPIC -I\"/Users/kantor/sage-3.0.alpha1/local/include\" -I\"/Users/kantor/sage-3.0.alpha1/local/include/linbox\"  -L\"/Users/kantor/sage-3.0.alpha1/local/lib\" -version-info 0:0:0  -o liblinboxwrap.la -rpath /Users/kantor/sage-3.0.alpha1/local/lib linbox_wrap.lo -llinbox /usr/lib/libcblas.dylib \ng++ -dynamiclib -single_module ${wl}-flat_namespace ${wl}-undefined ${wl}suppress -o .libs/liblinboxwrap.0.0.0.dylib  .libs/linbox_wrap.o  -L/Users/kantor/sage-3.0.alpha1/local/lib /Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib  -install_name  /Users/kantor/sage-3.0.alpha1/local/lib/liblinboxwrap.0.dylib -Wl,-compatibility_version -Wl,1 -Wl,-current_version -Wl,1.0\nld: multiple definitions of symbol __ZN6LinBox11commentatorE\n.libs/linbox_wrap.o definition of __ZN6LinBox11commentatorE in section (__DATA,__common)\n/Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib(single module) definition of __ZN6LinBox11commentatorE\n/usr/bin/libtool: internal link edit command failed\nmake[2]: *** [liblinboxwrap.la] Error 1\nError installing linboxwrap\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2833\n\n",
    "created_at": "2008-04-06T22:09:51Z",
    "labels": [
        "component: linbox",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Linbox build failure on OSX 10.4 intel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2833",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```
Assignee: @ClementPernet

Building the sage 3.0.alpha1 tarball failed at linbox  on OSX 10.4 intel with gcc
version 4.0.1.




```
/bin/sh ./libtool --tag=CXX   --mode=compile g++ -DPACKAGE_NAME=\"liblinboxwrap\" -DPACKAGE_TARNAME=\"liblinboxwrap\" -DPACKAGE_VERSION=\"0.0.1\" -DPACKAGE_STRING=\"liblinboxwrap\ 0.0.1\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"liblinboxwrap\" -DVERSION=\"0.0.1\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_BLAS=1 -I.   -g -I"/Users/kantor/sage-3.0.alpha1/local/include/linbox" -I"/Users/kantor/sage-3.0.alpha1/local"/include  -g -fPIC -I"/Users/kantor/sage-3.0.alpha1/local/include" -I"/Users/kantor/sage-3.0.alpha1/local/include/linbox"  -L"/Users/kantor/sage-3.0.alpha1/local/lib" -MT linbox_wrap.lo -MD -MP -MF .deps/linbox_wrap.Tpo -c -o linbox_wrap.lo `test -f 'src/linbox_wrap.cpp' || echo './'`src/linbox_wrap.cpp
mkdir .libs
 g++ -DPACKAGE_NAME=\"liblinboxwrap\" -DPACKAGE_TARNAME=\"liblinboxwrap\" -DPACKAGE_VERSION=\"0.0.1\" "-DPACKAGE_STRING=\"liblinboxwrap 0.0.1\"" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"liblinboxwrap\" -DVERSION=\"0.0.1\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_BLAS=1 -I. -g -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -I/Users/kantor/sage-3.0.alpha1/local/include -g -fPIC -I/Users/kantor/sage-3.0.alpha1/local/include -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -L/Users/kantor/sage-3.0.alpha1/local/lib -MT linbox_wrap.lo -MD -MP -MF .deps/linbox_wrap.Tpo -c src/linbox_wrap.cpp  -fno-common -DPIC -o .libs/linbox_wrap.o
 g++ -DPACKAGE_NAME=\"liblinboxwrap\" -DPACKAGE_TARNAME=\"liblinboxwrap\" -DPACKAGE_VERSION=\"0.0.1\" "-DPACKAGE_STRING=\"liblinboxwrap 0.0.1\"" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"liblinboxwrap\" -DVERSION=\"0.0.1\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_BLAS=1 -I. -g -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -I/Users/kantor/sage-3.0.alpha1/local/include -g -fPIC -I/Users/kantor/sage-3.0.alpha1/local/include -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -L/Users/kantor/sage-3.0.alpha1/local/lib -MT linbox_wrap.lo -MD -MP -MF .deps/linbox_wrap.Tpo -c src/linbox_wrap.cpp -o linbox_wrap.o >/dev/null 2>&1
mv -f .deps/linbox_wrap.Tpo .deps/linbox_wrap.Plo
/bin/sh ./libtool --tag=CXX   --mode=link g++  -g -fPIC -I"/Users/kantor/sage-3.0.alpha1/local/include" -I"/Users/kantor/sage-3.0.alpha1/local/include/linbox"  -L"/Users/kantor/sage-3.0.alpha1/local/lib" -version-info 0:0:0  -o liblinboxwrap.la -rpath /Users/kantor/sage-3.0.alpha1/local/lib linbox_wrap.lo -llinbox /usr/lib/libcblas.dylib 
g++ -dynamiclib -single_module ${wl}-flat_namespace ${wl}-undefined ${wl}suppress -o .libs/liblinboxwrap.0.0.0.dylib  .libs/linbox_wrap.o  -L/Users/kantor/sage-3.0.alpha1/local/lib /Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib  -install_name  /Users/kantor/sage-3.0.alpha1/local/lib/liblinboxwrap.0.dylib -Wl,-compatibility_version -Wl,1 -Wl,-current_version -Wl,1.0
ld: multiple definitions of symbol __ZN6LinBox11commentatorE
.libs/linbox_wrap.o definition of __ZN6LinBox11commentatorE in section (__DATA,__common)
/Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib(single module) definition of __ZN6LinBox11commentatorE
/usr/bin/libtool: internal link edit command failed
make[2]: *** [liblinboxwrap.la] Error 1
Error building linboxwrap
/bin/sh ./libtool --tag=CXX   --mode=link g++  -g -fPIC -I"/Users/kantor/sage-3.0.alpha1/local/include" -I"/Users/kantor/sage-3.0.alpha1/local/include/linbox"  -L"/Users/kantor/sage-3.0.alpha1/local/lib" -version-info 0:0:0  -o liblinboxwrap.la -rpath /Users/kantor/sage-3.0.alpha1/local/lib linbox_wrap.lo -llinbox /usr/lib/libcblas.dylib 
g++ -dynamiclib -single_module ${wl}-flat_namespace ${wl}-undefined ${wl}suppress -o .libs/liblinboxwrap.0.0.0.dylib  .libs/linbox_wrap.o  -L/Users/kantor/sage-3.0.alpha1/local/lib /Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib  -install_name  /Users/kantor/sage-3.0.alpha1/local/lib/liblinboxwrap.0.dylib -Wl,-compatibility_version -Wl,1 -Wl,-current_version -Wl,1.0
ld: multiple definitions of symbol __ZN6LinBox11commentatorE
.libs/linbox_wrap.o definition of __ZN6LinBox11commentatorE in section (__DATA,__common)
/Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib(single module) definition of __ZN6LinBox11commentatorE
/usr/bin/libtool: internal link edit command failed
make[2]: *** [liblinboxwrap.la] Error 1
Error installing linboxwrap
```


Issue created by migration from https://trac.sagemath.org/ticket/2833





---

archive/issue_comments_019400.json:
```json
{
    "body": "Proposed patch",
    "created_at": "2008-04-09T16:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2833#issuecomment-19400",
    "user": "https://github.com/ClementPernet"
}
```

Proposed patch



---

archive/issue_comments_019401.json:
```json
{
    "body": "Attachment [commentatorOSX10.4.patch](tarball://root/attachments/some-uuid/ticket2833/commentatorOSX10.4.patch) by @ClementPernet created at 2008-04-09 16:40:00\n\nI propose the attached patch. \nHowever, I still could not test it on a OS-X 10.4 since I only have access on 10.5 boxes.\nLet me know if it fixes the bug, and I will post the updated linbox spkg.",
    "created_at": "2008-04-09T16:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2833#issuecomment-19401",
    "user": "https://github.com/ClementPernet"
}
```

Attachment [commentatorOSX10.4.patch](tarball://root/attachments/some-uuid/ticket2833/commentatorOSX10.4.patch) by @ClementPernet created at 2008-04-09 16:40:00

I propose the attached patch. 
However, I still could not test it on a OS-X 10.4 since I only have access on 10.5 boxes.
Let me know if it fixes the bug, and I will post the updated linbox spkg.



---

archive/issue_comments_019402.json:
```json
{
    "body": "This patch fixes the problem for my machine. Therefore positive review.",
    "created_at": "2008-04-09T17:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2833#issuecomment-19402",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

This patch fixes the problem for my machine. Therefore positive review.



---

archive/issue_comments_019403.json:
```json
{
    "body": "An new spkg which incorporates Clement's fix is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha4/linbox-1.1.5p2.spkg\n\nIt builds fine on OSX 10.4, 10.5 and Linux.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-09T18:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2833#issuecomment-19403",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

An new spkg which incorporates Clement's fix is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha4/linbox-1.1.5p2.spkg

It builds fine on OSX 10.4, 10.5 and Linux.

Cheers,

Michael



---

archive/issue_comments_019404.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-09T18:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2833#issuecomment-19404",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_events_003023.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-09T18:39:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2833",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2833#event-3023"
}
```



---

archive/issue_comments_019405.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-09T18:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2833#issuecomment-19405",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
