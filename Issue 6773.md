# Issue 6773: Freetype hides warning messages by sending output to /dev/null

archive/issues_006773.json:
```json
{
    "body": "Assignee: tbd\n\nI've not no idea why anyone would want to do this, but freetype (along with lcalc) is one of the guilty parties. \n\n /opt/sunstudio12.1/bin/cc -I/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/objs -I./builds/unix -I/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/include -c -g -DFT_CONFIG_OPTION_SYSTEM_ZLIB \"-DFT_CONFIG_CONFIG_H=<ftconfig.h>\" -DFT2_BUILD_LIBRARY \"-DFT_CONFIG_MODULES_H=<ftmodule.h>\" -I/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/src/pshinter /export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/src/pshinter/pshinter.c -o /export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/objs/pshinter.o >/dev/null 2>&1\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6773\n\n",
    "created_at": "2009-08-17T10:11:21Z",
    "labels": [
        "build",
        "major",
        "enhancement"
    ],
    "title": "Freetype hides warning messages by sending output to /dev/null",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6773",
    "user": "drkirkby"
}
```
Assignee: tbd

I've not no idea why anyone would want to do this, but freetype (along with lcalc) is one of the guilty parties. 

 /opt/sunstudio12.1/bin/cc -I/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/objs -I./builds/unix -I/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/include -c -g -DFT_CONFIG_OPTION_SYSTEM_ZLIB "-DFT_CONFIG_CONFIG_H=<ftconfig.h>" -DFT2_BUILD_LIBRARY "-DFT_CONFIG_MODULES_H=<ftmodule.h>" -I/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/src/pshinter /export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/src/pshinter/pshinter.c -o /export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/objs/pshinter.o >/dev/null 2>&1



Issue created by migration from https://trac.sagemath.org/ticket/6773





---

archive/issue_comments_055770.json:
```json
{
    "body": "This has now been submitted upstream as a bug. \n\nhttp://savannah.nongnu.org/bugs/index.php?28153",
    "created_at": "2009-12-03T04:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6773#issuecomment-55770",
    "user": "drkirkby"
}
```

This has now been submitted upstream as a bug. 

http://savannah.nongnu.org/bugs/index.php?28153



---

archive/issue_comments_055771.json:
```json
{
    "body": "Changing component from build to packages: standard.",
    "created_at": "2015-09-08T12:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6773#issuecomment-55771",
    "user": "@jdemeyer"
}
```

Changing component from build to packages: standard.
