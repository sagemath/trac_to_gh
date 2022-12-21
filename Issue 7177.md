# Issue 7177: gap does not find getopt.h. getopt() defined in stdlib.h

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-10 08:51:20

Assignee: tbd

CC:  david.kirkby@onetel.ne dimpase

Keywords: HP-UX getopt

Apart from #7041 which I find *very* annoying about gap, it can't find getopt.h on HP-UX 11i. It's defined in stdlib.h, so can easily be *very* fixed by developers. 

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



---

Comment by drkirkby created at 2009-10-10 08:55:48

Changing priority from major to minor.


---

Comment by kcrisman created at 2011-02-16 22:33:40

Changing component from porting to AIX or HP-UX ports.


---

Comment by mkoeppe created at 2020-04-25 02:59:53

outdated, should be closed


---

Comment by mkoeppe created at 2020-04-25 03:00:07

Changing status from new to needs_review.


---

Comment by dimpase created at 2020-04-25 04:41:31

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-04-26 07:25:26

Resolution: invalid
