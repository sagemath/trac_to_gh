# Issue 4865: dvipng optional spkg fails to build on sage.math (our main devel machine)

archive/issues_004865.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  dimpase\n\n\n```\nsage: install_package('dvipng-1.8')\n...\ngcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o vf.o vf.c\ngcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o ft.o ft.c\ngcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o enc.o enc.c\ngcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o fontmap.o fontmap.c\ngcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o tfm.o tfm.c\ngcc -L/usr/local/sage/local/lib dvipng.o color.o draw.o dvi.o font.o misc.o pk.o set.o special.o papersiz.o ppagelist.o vf.o  ft.o enc.o fontmap.o tfm.o -o dvipng -L/usr/local/sage/local/lib -Wl,--rpath -Wl,/usr/local/sage/local/lib -lfreetype -lkpathsea -lgd -lpng -lz -lm  \nspecial.o: In function `SetSpecial':\nspecial.c:(.text+0x13ac): undefined reference to `gdImageCreateFromJpeg'\ncollect2: ld returned 1 exit status\nmake: *** [dvipng] Error 1\nError building dvipng.\n\nreal\t0m5.119s\nuser\t0m2.720s\nsys\t0m2.300s\nsage: An error occurred while installing dvipng-1.8\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /usr/local/sage/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/usr/local/sage/spkg/build/dvipng-1.8 and type 'make'.\nInstead type \"/usr/local/sage/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/usr/local/sage/spkg/build/dvipng-1.8\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\n```\n\n\nI installed  libkpathsea-dev in order to get as far as the above:\n\n```\nroot@sage:/usr/local/sage# apt-get install libkpathsea-dev\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4865\n\n",
    "created_at": "2008-12-24T05:18:46Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "dvipng optional spkg fails to build on sage.math (our main devel machine)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4865",
    "user": "was"
}
```
Assignee: mabshoff

CC:  dimpase


```
sage: install_package('dvipng-1.8')
...
gcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o vf.o vf.c
gcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o ft.o ft.c
gcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o enc.o enc.c
gcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o fontmap.o fontmap.c
gcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o tfm.o tfm.c
gcc -L/usr/local/sage/local/lib dvipng.o color.o draw.o dvi.o font.o misc.o pk.o set.o special.o papersiz.o ppagelist.o vf.o  ft.o enc.o fontmap.o tfm.o -o dvipng -L/usr/local/sage/local/lib -Wl,--rpath -Wl,/usr/local/sage/local/lib -lfreetype -lkpathsea -lgd -lpng -lz -lm  
special.o: In function `SetSpecial':
special.c:(.text+0x13ac): undefined reference to `gdImageCreateFromJpeg'
collect2: ld returned 1 exit status
make: *** [dvipng] Error 1
Error building dvipng.

real	0m5.119s
user	0m2.720s
sys	0m2.300s
sage: An error occurred while installing dvipng-1.8
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /usr/local/sage/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/usr/local/sage/spkg/build/dvipng-1.8 and type 'make'.
Instead type "/usr/local/sage/sage -sh"
in order to set all environment variables correctly, then cd to
/usr/local/sage/spkg/build/dvipng-1.8
(When you are done debugging, you can type "exit" to leave the
subshell.)
```


I installed  libkpathsea-dev in order to get as far as the above:

```
root@sage:/usr/local/sage# apt-get install libkpathsea-dev
```


Issue created by migration from https://trac.sagemath.org/ticket/4865





---

archive/issue_comments_036866.json:
```json
{
    "body": "Is this still relevant since we removed the dvipng spkg?\n\nCheers,\n\nMichael",
    "created_at": "2009-01-12T02:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4865#issuecomment-36866",
    "user": "mabshoff"
}
```

Is this still relevant since we removed the dvipng spkg?

Cheers,

Michael



---

archive/issue_comments_036867.json:
```json
{
    "body": "Outdated spkg or build system ticket, should be closed",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4865#issuecomment-36867",
    "user": "mkoeppe"
}
```

Outdated spkg or build system ticket, should be closed



---

archive/issue_comments_036868.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4865#issuecomment-36868",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036869.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-22T07:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4865#issuecomment-36869",
    "user": "slelievre"
}
```

Resolution: invalid
