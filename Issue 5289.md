# Issue 5289: gdmodule fails to build on Linux/Solaris systems without a system wide libpng

archive/issues_005289.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is fallout from the libpng -> libpng12 transition and trivial to fix:\n\n```\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DHAVE_LIBGD -DHAVE_LIBZ -DHAVE_LIBFREETYPE -DHAVE_LIBPNG -I/home/mabshoff/build-3.3.rc1/sage-3.3.rc1-cicero-gcc-433/local/include -I/usr/include -I/home/mabshoff/build-3.3.rc1/sage-3.3.rc1-cicero-gcc-433/local/include/python2.5 -c _gdmodule.c -o build/temp.linux-i686-2.5/_gdmodule.o\n_gdmodule.c:152: warning: function declaration isn\u2019t a prototype\n_gdmodule.c:169: warning: function declaration isn\u2019t a prototype\n_gdmodule.c: In function \u2018image_string\u2019:\n_gdmodule.c:993: warning: pointer targets in passing argument 5 of \u2018gdImageString\u2019 differ in signedness\n_gdmodule.c: In function \u2018image_string16\u2019:\n_gdmodule.c:1008: warning: passing argument 5 of \u2018gdImageString16\u2019 from incompatible pointer type\n_gdmodule.c: In function \u2018image_stringup\u2019:\n_gdmodule.c:1022: warning: pointer targets in passing argument 5 of \u2018gdImageStringUp\u2019 differ in signedness\n_gdmodule.c: In function \u2018image_stringup16\u2019:\n_gdmodule.c:1037: warning: passing argument 5 of \u2018gdImageStringUp16\u2019 from incompatible pointer type\ngcc -pthread -shared build/temp.linux-i686-2.5/_gdmodule.o -L/home/mabshoff/build-3.3.rc1/sage-3.3.rc1-cicero-gcc-433/local/lib -L/usr/lib -lgd -lz -lfreetype -lpng -o build/lib.linux-i686-2.5/_gd.so\n/usr/local/binutils-2.19.1/x86-Linux-fc-gcc-4.3.3/bin/ld: cannot find -lpng\ncollect2: ld returned 1 exit status\nerror: command 'gcc' failed with exit status 1\nFailure to build gdmodule\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5289\n\n",
    "created_at": "2009-02-17T02:16:24Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "title": "gdmodule fails to build on Linux/Solaris systems without a system wide libpng",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5289",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This is fallout from the libpng -> libpng12 transition and trivial to fix:

```
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DHAVE_LIBGD -DHAVE_LIBZ -DHAVE_LIBFREETYPE -DHAVE_LIBPNG -I/home/mabshoff/build-3.3.rc1/sage-3.3.rc1-cicero-gcc-433/local/include -I/usr/include -I/home/mabshoff/build-3.3.rc1/sage-3.3.rc1-cicero-gcc-433/local/include/python2.5 -c _gdmodule.c -o build/temp.linux-i686-2.5/_gdmodule.o
_gdmodule.c:152: warning: function declaration isn’t a prototype
_gdmodule.c:169: warning: function declaration isn’t a prototype
_gdmodule.c: In function ‘image_string’:
_gdmodule.c:993: warning: pointer targets in passing argument 5 of ‘gdImageString’ differ in signedness
_gdmodule.c: In function ‘image_string16’:
_gdmodule.c:1008: warning: passing argument 5 of ‘gdImageString16’ from incompatible pointer type
_gdmodule.c: In function ‘image_stringup’:
_gdmodule.c:1022: warning: pointer targets in passing argument 5 of ‘gdImageStringUp’ differ in signedness
_gdmodule.c: In function ‘image_stringup16’:
_gdmodule.c:1037: warning: passing argument 5 of ‘gdImageStringUp16’ from incompatible pointer type
gcc -pthread -shared build/temp.linux-i686-2.5/_gdmodule.o -L/home/mabshoff/build-3.3.rc1/sage-3.3.rc1-cicero-gcc-433/local/lib -L/usr/lib -lgd -lz -lfreetype -lpng -o build/lib.linux-i686-2.5/_gd.so
/usr/local/binutils-2.19.1/x86-Linux-fc-gcc-4.3.3/bin/ld: cannot find -lpng
collect2: ld returned 1 exit status
error: command 'gcc' failed with exit status 1
Failure to build gdmodule
```


Issue created by migration from https://trac.sagemath.org/ticket/5289





---

archive/issue_comments_040645.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-17T02:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5289#issuecomment-40645",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040646.json:
```json
{
    "body": "Attachment\n\nThis is the fix I am applying inside the spkg - it will make it easier for the reviewer",
    "created_at": "2009-02-17T06:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5289#issuecomment-40646",
    "user": "mabshoff"
}
```

Attachment

This is the fix I am applying inside the spkg - it will make it easier for the reviewer



---

archive/issue_comments_040647.json:
```json
{
    "body": "The spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc2/gdmodule-0.56.p5.spkg\n\nFixes the issue and also cleans it up a great deal.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T07:24:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5289#issuecomment-40647",
    "user": "mabshoff"
}
```

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc2/gdmodule-0.56.p5.spkg

Fixes the issue and also cleans it up a great deal.

Cheers,

Michael



---

archive/issue_comments_040648.json:
```json
{
    "body": "Seems reasonable to me.",
    "created_at": "2009-02-17T13:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5289#issuecomment-40648",
    "user": "mhansen"
}
```

Seems reasonable to me.



---

archive/issue_comments_040649.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-17T18:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5289#issuecomment-40649",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040650.json:
```json
{
    "body": "Merged in Sage 3.3.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T18:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5289#issuecomment-40650",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc2.

Cheers,

Michael
