# Issue 7167: HP-UX issue, ECL fails to build properly

Issue created by migration from https://trac.sagemath.org/ticket/7167

Original creator: drkirkby

Original creation time: 2009-10-10 04:47:25

Assignee: tbd

CC:  chapoton

On a HP C3600, running HP-UX 11i, I got the following failure. 


```
/src/gc/include/new_gc_alloc.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/new_gc_alloc.h'
 /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_allocator.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_allocator.h'
 /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_backptr.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_backptr.h'
 /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_gcj.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_gcj.h'
 /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/leak_detector.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/leak_detector.h'
 /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_amiga_redirects.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_amiga_redirects.h'
 /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_pthread_redirects.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_pthread_redirects.h'
 /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_config_macros.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_config_macros.h'
 /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_tiny_fl.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_tiny_fl.h'
 /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_version.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_version.h'
        sed -e 's,@ecldir\\@,/home/drkirkby/sage-4.1.2.rc0/local/lib/ecl-9.8.4/,g' < lsp/config.pre > lsp/config.lsp
        sed -e 's,@ecldir\\@,"/home/drkirkby/sage-4.1.2.rc0/local/lib/ecl-9.8.4/",g' \
            -e 's,@libdir\\@,"/home/drkirkby/sage-4.1.2.rc0/local/lib/",g' \
            -e 's,@includedir\\@,"/home/drkirkby/sage-4.1.2.rc0/local/include/",g' < cmp/cmpdefs.pre > cmp/cmpdefs.lsp
        test -d c/ecl || mkdir c/ecl
        sed 's,__declspec(dllimport),,g' /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/h/external.h > c/ecl/external.h
        cp /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/h/*.h ecl/
        cd c; make
        cat /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/symbols_list.h | \
        sed -e 's%{\([A-Z ]*.*".*"\),[^,]*,[ ]*NULL,.*}%{\1,NULL}%g' \
            -e 's%{\([A-Z ]*.*".*"\),[^,]*,[ ]*\([^,]*\),.*}%{\1,"\2"}%g' \
            -e 's%{NULL.*%{NULL,NULL}};%' > /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/symbols_list2.h
        if test -f ../CROSS-DPP; then touch dpp; else \
        gcc -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build -I./ /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/dpp.c  -I/home/drkirkby/sage-4.1.2.rc0/local/include  -O2  -g  -Wall  -fPIC  -Dhpux11.11 -o ./dpp ; \
        fi
<command-line>: warning: missing whitespace after the macro name
/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/dpp.c: In function 'read_function':
/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/dpp.c:336: warning: array subscript has type 'char'
        if test -f ../CROSS-DPP ; then ../CROSS-DPP /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/main.d tmp.c ; else ./dpp /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/main.d tmp.c ; fi
dpp: /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/main.d -> tmp.c

Unknown symbol: mp::*current-process*

Unknown symbol: mp::+load-compile-lock+

Unknown symbol: mp::+load-compile-lock+
        gcc -DECLDIR="\"/home/drkirkby/sage-4.1.2.rc0/local/lib/ecl-9.8.4\"" -I. -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c -I../ecl/gc -DECL_API -DECL_NO_LEGACY  -I/home/drkirkby/sage-4.1.2.rc0/local/include  -O2  -g  -Wall  -fPIC  -Dhpux11.11 -c  #         -Wall -W -Wfloat-equal -Wundef -Wendif-labels -Wpointer-arith -Wcast-align  #   -Wwrite-strings -Wconversion -Wsign-compare -Wmissing-prototypes -Wredundant-decls  #    -Wunreachable-code -Winline -o main.o tmp.c
gcc: no input files
*** Error exit code 1

Stop.
*** Error exit code 1

Stop.
*** Error exit code 1

Stop.
Failed to build ECL ... exiting

```




---

Comment by drkirkby created at 2009-10-24 22:07:39

Changing component from algebra to porting.


---

Comment by kcrisman created at 2011-02-16 22:33:08

Changing component from porting to AIX or HP-UX ports.


---

Comment by slelievre created at 2019-01-14 22:54:41

This was with ECL 9.8.4. Sage now uses ECL 16.1.2.

Is this still failing or has one of the ECL upgrades fixed it?


---

Comment by mkoeppe created at 2020-06-23 21:26:55

We should close this ticket as outdated.


---

Comment by mkoeppe created at 2020-06-23 21:26:55

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-06-24 06:28:19

Resolution: invalid
