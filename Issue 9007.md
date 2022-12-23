# Issue 9007: iconv not building properly on OpenSolaris

archive/issues_009007.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jsp\n\nThe following problem is observed with Sage 4.4.2\n\n\n```\n/bin/sh ../libtool --mode=link gcc  -m64 -fvisibility=hidden -o libiconv.la -rpath /export/home/drkirkby/sage-4.4.2/local/lib -version-info 7:0:5 -no-undefined iconv.lo localcharset.lo relocatable.lo  \nlibtool: link: gcc -shared -Wl,-z -Wl,text -Wl,-h -Wl,libiconv.so.2 -o .libs/libiconv.so.2.5.0  .libs/iconv.o .libs/localcharset.o .libs/relocatable.o   -lc  -m64  \nText relocation remains                 \treferenced\n    against symbol\t\t    offset\tin file\naliases_lookup                      0x1b818   \t.libs/iconv.o\naliases_lookup                      0x1b9be   \t.libs/iconv.o\naliases_lookup                      0x1bec7   \t.libs/iconv.o\naliases_lookup                      0x1c06d   \t.libs/iconv.o\naliases_lookup                      0x1c932   \t.libs/iconv.o\nld: fatal: relocations remain against allocatable but non-writable sections\ncollect2: ld returned 1 exit status\nmake[3]: *** [libiconv.la] Error 1\nmake[3]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/iconv-1.13.1.p2/src/lib'\nmake[2]: *** [all] Error 2\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/iconv-1.13.1.p2/src'\nError making iconv\n\nreal\t0m11.098s\nuser\t0m5.345s\nsys\t0m4.733s\nsage: An error occurred while installing iconv-1.13.1.p2\n```\n\n\nI've tried building the source outside of Sage, both 32 and 64-bit, and neither work. A Google shows using the GNU linker will probably solve it, but that is not an acceptable solution, as the GNU linker will create its own set of problems in other packages. It is better that the issue is resolved properly. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9007\n\n",
    "created_at": "2010-05-21T12:37:18Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "iconv not building properly on OpenSolaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9007",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  jsp

The following problem is observed with Sage 4.4.2


```
/bin/sh ../libtool --mode=link gcc  -m64 -fvisibility=hidden -o libiconv.la -rpath /export/home/drkirkby/sage-4.4.2/local/lib -version-info 7:0:5 -no-undefined iconv.lo localcharset.lo relocatable.lo  
libtool: link: gcc -shared -Wl,-z -Wl,text -Wl,-h -Wl,libiconv.so.2 -o .libs/libiconv.so.2.5.0  .libs/iconv.o .libs/localcharset.o .libs/relocatable.o   -lc  -m64  
Text relocation remains                 	referenced
    against symbol		    offset	in file
aliases_lookup                      0x1b818   	.libs/iconv.o
aliases_lookup                      0x1b9be   	.libs/iconv.o
aliases_lookup                      0x1bec7   	.libs/iconv.o
aliases_lookup                      0x1c06d   	.libs/iconv.o
aliases_lookup                      0x1c932   	.libs/iconv.o
ld: fatal: relocations remain against allocatable but non-writable sections
collect2: ld returned 1 exit status
make[3]: *** [libiconv.la] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/iconv-1.13.1.p2/src/lib'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/iconv-1.13.1.p2/src'
Error making iconv

real	0m11.098s
user	0m5.345s
sys	0m4.733s
sage: An error occurred while installing iconv-1.13.1.p2
```


I've tried building the source outside of Sage, both 32 and 64-bit, and neither work. A Google shows using the GNU linker will probably solve it, but that is not an acceptable solution, as the GNU linker will create its own set of problems in other packages. It is better that the issue is resolved properly. 

Issue created by migration from https://trac.sagemath.org/ticket/9007





---

archive/issue_comments_083314.json:
```json
{
    "body": "This appears to be a bug in gcc 4.3.4. At the suggestion of the iconv developers, I used another version of gcc. I used 4.4.4 which seems to build this ok. \n\nThis ticket can be closed.",
    "created_at": "2010-05-22T08:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9007#issuecomment-83314",
    "user": "drkirkby"
}
```

This appears to be a bug in gcc 4.3.4. At the suggestion of the iconv developers, I used another version of gcc. I used 4.4.4 which seems to build this ok. 

This ticket can be closed.



---

archive/issue_comments_083315.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-05-22T08:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9007#issuecomment-83315",
    "user": "dimpase"
}
```

Resolution: wontfix
