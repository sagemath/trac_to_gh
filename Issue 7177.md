# Issue 7177: gap does not find getopt.h. getopt() defined in stdlib.h

archive/issues_007177.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  david.kirkby@onetel.ne @dimpase\n\nKeywords: HP-UX getopt\n\nApart from #7041 which I find **very** annoying about gap, it can't find getopt.h on HP-UX 11i. It's defined in stdlib.h, so can easily be **very** fixed by developers. \n\nI would check for getopt.h in the configure script, then make sure not to look for it if the file is not found\n\n\n```\n        gcc -I. -I../.. -DCONFIG_H -Wall -g -O2  -o float.o -c ../../src/float.c\n        gcc -Wall -g -O2  -g  -o gap ariths.o blister.o bool.o c_meths1.o c_type1.o c_oper1.o c_filt1.o c_random.o calls.o code.o compiler.o compstat.o costab.o cyclotom.o dt.o dteval.o exprs.o finfield.o funcs.o gap.o gasman.o gvars.o integer.o intrprtr.o listfunc.o listoper.o lists.o objcftl.o objects.o objfgelm.o objpcgel.o objscoll.o objccoll.o opers.o permutat.o plist.o precord.o range.o rational.o read.o records.o saveload.o scanner.o sctable.o set.o stats.o streams.o string.o sysfiles.o system.o tietze.o vars.o vecgf2.o vec8bit.o vector.o vecffe.o weakptr.o iostream.o float.o   -lm\n        chmod +x bin/gap.sh\n        if ! grep darwin sysinfo.gap ; then ( cd bin/hppa2.0w-hp-hpux11.11-gcc ; strip gap) ; fi\n        ( test -d bin || mkdir bin; \\\n        test -d bin/hppa2.0w-hp-hpux11.11-gcc || mkdir bin/hppa2.0w-hp-hpux11.11-gcc; cd bin/hppa2.0w-hp-hpux11.11-gcc; \\\n        make -f ../../Makefile all2 CC=\"gcc\" CFLAGS=\"-O2\"; \\\n        cd ../../src/leon/src/../; ./configure; make; mkdir ../../bin/leon; \\\n        cp cent ../../bin/leon; cp cjrndper ../../bin/leon; \\\n        cp commut ../../bin/leon; cp compgrp ../../bin/leon; \\\n        cp desauto ../../bin/leon; cp fndelt ../../bin/leon; \\\n        cp generate ../../bin/leon; cp inter ../../bin/leon; \\\n        cp orbdes ../../bin/leon; cp orblist ../../bin/leon; \\\n        cp randobj ../../bin/leon; cp setstab ../../bin/leon; \\\n        cp wtdist ../../bin/leon; cp src/*.sh ../../bin/leon; \\\n        cp wtdist ../../bin; cp desauto ../../bin \\\n        cp wtdist ../../bin/hppa2.0w-hp-hpux11.11-gcc; cp desauto ../../bin/hppa2.0w-hp-hpux11.11-gcc \\\n        )\n        gcc -c -O2 -o leonconv.o -c ../../src/leonconv.c\n../../src/leonconv.c: In function 'main':\n../../src/leonconv.c:19: warning: incompatible implicit declaration of built-in function 'exit'\n../../src/leonconv.c:30: warning: incompatible implicit declaration of built-in function 'exit'\n../../src/leonconv.c: In function 'EquivalentToGuave':\n../../src/leonconv.c:123: warning: incompatible implicit declaration of built-in function 'exit'\n        gcc -O2 -o leonconv leonconv.o\n        gcc -c -O3 -Wall -I ../../src/ctjhai ../../src/ctjhai/minimum-weight.c\n../../src/ctjhai/minimum-weight.c:32:20: error: getopt.h: No such file or directory\n../../src/ctjhai/minimum-weight.c: In function 'main':\n../../src/ctjhai/minimum-weight.c:54: error: array type has incomplete element type\n../../src/ctjhai/minimum-weight.c:66: warning: implicit declaration of function 'getopt_long'\n../../src/ctjhai/minimum-weight.c:54: warning: unused variable 'long_options'\n*** Error exit code 1\n\nStop.\n*** Error exit code 1\n\nStop.\nError building Guava\n\nreal    6m58.243s\nuser    6m30.410s\nsys     0m19.410s\nsage: An error occurred while installing gap-4.4.10.p12\n```\n\n\nAnd here is where getopt is defined. \n\n\n```\n\n$ grep getopt /usr/include/*\n/usr/include/stdio.h:#      pragma HP_DEFINED_EXTERNAL getopt,cuserid\n/usr/include/stdio.h:#      pragma HP_NO_RELOCATION getopt,cuserid\n/usr/include/stdio.h:#      pragma HP_LONG_RETURN getopt,cuserid\n/usr/include/stdio.h:       extern int getopt(int, char * const [], const char *);\n/usr/include/stdio.h:       extern int getopt();\n/usr/include/stdlib.h:#      pragma HP_DEFINED_EXTERNAL clearenv,getopt,getpass\n/usr/include/stdlib.h:#      pragma HP_NO_RELOCATION clearenv,getopt,getpass\n/usr/include/stdlib.h:#      pragma HP_LONG_RETURN clearenv,getopt,getpass\n/usr/include/stdlib.h:       extern int getopt(int, char * const [], const char *);\n/usr/include/stdlib.h:       extern int getopt();\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7177\n\n",
    "created_at": "2009-10-10T08:51:20Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "gap does not find getopt.h. getopt() defined in stdlib.h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7177",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  david.kirkby@onetel.ne @dimpase

Keywords: HP-UX getopt

Apart from #7041 which I find **very** annoying about gap, it can't find getopt.h on HP-UX 11i. It's defined in stdlib.h, so can easily be **very** fixed by developers. 

I would check for getopt.h in the configure script, then make sure not to look for it if the file is not found


```
        gcc -I. -I../.. -DCONFIG_H -Wall -g -O2  -o float.o -c ../../src/float.c
        gcc -Wall -g -O2  -g  -o gap ariths.o blister.o bool.o c_meths1.o c_type1.o c_oper1.o c_filt1.o c_random.o calls.o code.o compiler.o compstat.o costab.o cyclotom.o dt.o dteval.o exprs.o finfield.o funcs.o gap.o gasman.o gvars.o integer.o intrprtr.o listfunc.o listoper.o lists.o objcftl.o objects.o objfgelm.o objpcgel.o objscoll.o objccoll.o opers.o permutat.o plist.o precord.o range.o rational.o read.o records.o saveload.o scanner.o sctable.o set.o stats.o streams.o string.o sysfiles.o system.o tietze.o vars.o vecgf2.o vec8bit.o vector.o vecffe.o weakptr.o iostream.o float.o   -lm
        chmod +x bin/gap.sh
        if ! grep darwin sysinfo.gap ; then ( cd bin/hppa2.0w-hp-hpux11.11-gcc ; strip gap) ; fi
        ( test -d bin || mkdir bin; \
        test -d bin/hppa2.0w-hp-hpux11.11-gcc || mkdir bin/hppa2.0w-hp-hpux11.11-gcc; cd bin/hppa2.0w-hp-hpux11.11-gcc; \
        make -f ../../Makefile all2 CC="gcc" CFLAGS="-O2"; \
        cd ../../src/leon/src/../; ./configure; make; mkdir ../../bin/leon; \
        cp cent ../../bin/leon; cp cjrndper ../../bin/leon; \
        cp commut ../../bin/leon; cp compgrp ../../bin/leon; \
        cp desauto ../../bin/leon; cp fndelt ../../bin/leon; \
        cp generate ../../bin/leon; cp inter ../../bin/leon; \
        cp orbdes ../../bin/leon; cp orblist ../../bin/leon; \
        cp randobj ../../bin/leon; cp setstab ../../bin/leon; \
        cp wtdist ../../bin/leon; cp src/*.sh ../../bin/leon; \
        cp wtdist ../../bin; cp desauto ../../bin \
        cp wtdist ../../bin/hppa2.0w-hp-hpux11.11-gcc; cp desauto ../../bin/hppa2.0w-hp-hpux11.11-gcc \
        )
        gcc -c -O2 -o leonconv.o -c ../../src/leonconv.c
../../src/leonconv.c: In function 'main':
../../src/leonconv.c:19: warning: incompatible implicit declaration of built-in function 'exit'
../../src/leonconv.c:30: warning: incompatible implicit declaration of built-in function 'exit'
../../src/leonconv.c: In function 'EquivalentToGuave':
../../src/leonconv.c:123: warning: incompatible implicit declaration of built-in function 'exit'
        gcc -O2 -o leonconv leonconv.o
        gcc -c -O3 -Wall -I ../../src/ctjhai ../../src/ctjhai/minimum-weight.c
../../src/ctjhai/minimum-weight.c:32:20: error: getopt.h: No such file or directory
../../src/ctjhai/minimum-weight.c: In function 'main':
../../src/ctjhai/minimum-weight.c:54: error: array type has incomplete element type
../../src/ctjhai/minimum-weight.c:66: warning: implicit declaration of function 'getopt_long'
../../src/ctjhai/minimum-weight.c:54: warning: unused variable 'long_options'
*** Error exit code 1

Stop.
*** Error exit code 1

Stop.
Error building Guava

real    6m58.243s
user    6m30.410s
sys     0m19.410s
sage: An error occurred while installing gap-4.4.10.p12
```


And here is where getopt is defined. 


```

$ grep getopt /usr/include/*
/usr/include/stdio.h:#      pragma HP_DEFINED_EXTERNAL getopt,cuserid
/usr/include/stdio.h:#      pragma HP_NO_RELOCATION getopt,cuserid
/usr/include/stdio.h:#      pragma HP_LONG_RETURN getopt,cuserid
/usr/include/stdio.h:       extern int getopt(int, char * const [], const char *);
/usr/include/stdio.h:       extern int getopt();
/usr/include/stdlib.h:#      pragma HP_DEFINED_EXTERNAL clearenv,getopt,getpass
/usr/include/stdlib.h:#      pragma HP_NO_RELOCATION clearenv,getopt,getpass
/usr/include/stdlib.h:#      pragma HP_LONG_RETURN clearenv,getopt,getpass
/usr/include/stdlib.h:       extern int getopt(int, char * const [], const char *);
/usr/include/stdlib.h:       extern int getopt();

```


Issue created by migration from https://trac.sagemath.org/ticket/7177





---

archive/issue_comments_059455.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-10-10T08:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7177#issuecomment-59455",
    "user": "drkirkby"
}
```

Changing priority from major to minor.



---

archive/issue_comments_059456.json:
```json
{
    "body": "Changing component from porting to AIX or HP-UX ports.",
    "created_at": "2011-02-16T22:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7177#issuecomment-59456",
    "user": "@kcrisman"
}
```

Changing component from porting to AIX or HP-UX ports.



---

archive/issue_comments_059457.json:
```json
{
    "body": "outdated, should be closed",
    "created_at": "2020-04-25T02:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7177#issuecomment-59457",
    "user": "@mkoeppe"
}
```

outdated, should be closed



---

archive/issue_comments_059458.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-04-25T03:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7177#issuecomment-59458",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059459.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-04-25T04:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7177#issuecomment-59459",
    "user": "@dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059460.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-04-26T07:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7177#issuecomment-59460",
    "user": "@fchapoton"
}
```

Resolution: invalid
