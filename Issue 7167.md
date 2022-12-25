# Issue 7167: HP-UX issue, ECL fails to build properly

archive/issues_007167.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @fchapoton\n\nOn a HP C3600, running HP-UX 11i, I got the following failure. \n\n```\n/src/gc/include/new_gc_alloc.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/new_gc_alloc.h'\n /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_allocator.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_allocator.h'\n /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_backptr.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_backptr.h'\n /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_gcj.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_gcj.h'\n /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/leak_detector.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/leak_detector.h'\n /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_amiga_redirects.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_amiga_redirects.h'\n /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_pthread_redirects.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_pthread_redirects.h'\n /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_config_macros.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_config_macros.h'\n /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_tiny_fl.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_tiny_fl.h'\n /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/install-sh -c -m 644 '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/gc/include/gc_version.h' '/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build/ecl//gc/gc_version.h'\n        sed -e 's,@ecldir\\\\@,/home/drkirkby/sage-4.1.2.rc0/local/lib/ecl-9.8.4/,g' < lsp/config.pre > lsp/config.lsp\n        sed -e 's,@ecldir\\\\@,\"/home/drkirkby/sage-4.1.2.rc0/local/lib/ecl-9.8.4/\",g' \\\n            -e 's,@libdir\\\\@,\"/home/drkirkby/sage-4.1.2.rc0/local/lib/\",g' \\\n            -e 's,@includedir\\\\@,\"/home/drkirkby/sage-4.1.2.rc0/local/include/\",g' < cmp/cmpdefs.pre > cmp/cmpdefs.lsp\n        test -d c/ecl || mkdir c/ecl\n        sed 's,__declspec(dllimport),,g' /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/h/external.h > c/ecl/external.h\n        cp /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/h/*.h ecl/\n        cd c; make\n        cat /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/symbols_list.h | \\\n        sed -e 's%{\\([A-Z ]*.*\".*\"\\),[^,]*,[ ]*NULL,.*}%{\\1,NULL}%g' \\\n            -e 's%{\\([A-Z ]*.*\".*\"\\),[^,]*,[ ]*\\([^,]*\\),.*}%{\\1,\"\\2\"}%g' \\\n            -e 's%{NULL.*%{NULL,NULL}};%' > /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/symbols_list2.h\n        if test -f ../CROSS-DPP; then touch dpp; else \\\n        gcc -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build -I./ /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/dpp.c  -I/home/drkirkby/sage-4.1.2.rc0/local/include  -O2  -g  -Wall  -fPIC  -Dhpux11.11 -o ./dpp ; \\\n        fi\n<command-line>: warning: missing whitespace after the macro name\n/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/dpp.c: In function 'read_function':\n/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/dpp.c:336: warning: array subscript has type 'char'\n        if test -f ../CROSS-DPP ; then ../CROSS-DPP /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/main.d tmp.c ; else ./dpp /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/main.d tmp.c ; fi\ndpp: /home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c/main.d -> tmp.c\n\nUnknown symbol: mp::*current-process*\n\nUnknown symbol: mp::+load-compile-lock+\n\nUnknown symbol: mp::+load-compile-lock+\n        gcc -DECLDIR=\"\\\"/home/drkirkby/sage-4.1.2.rc0/local/lib/ecl-9.8.4\\\"\" -I. -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/build -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/ecl-9.8.4-20090913cvs.p1/src/src/c -I../ecl/gc -DECL_API -DECL_NO_LEGACY  -I/home/drkirkby/sage-4.1.2.rc0/local/include  -O2  -g  -Wall  -fPIC  -Dhpux11.11 -c  #         -Wall -W -Wfloat-equal -Wundef -Wendif-labels -Wpointer-arith -Wcast-align  #   -Wwrite-strings -Wconversion -Wsign-compare -Wmissing-prototypes -Wredundant-decls  #    -Wunreachable-code -Winline -o main.o tmp.c\ngcc: no input files\n*** Error exit code 1\n\nStop.\n*** Error exit code 1\n\nStop.\n*** Error exit code 1\n\nStop.\nFailed to build ECL ... exiting\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7167\n\n",
    "created_at": "2009-10-10T04:47:25Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "HP-UX issue, ECL fails to build properly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7167",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @fchapoton

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


Issue created by migration from https://trac.sagemath.org/ticket/7167





---

archive/issue_comments_059297.json:
```json
{
    "body": "Changing component from algebra to porting.",
    "created_at": "2009-10-24T22:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7167#issuecomment-59297",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from algebra to porting.



---

archive/issue_comments_059298.json:
```json
{
    "body": "Changing component from porting to AIX or HP-UX ports.",
    "created_at": "2011-02-16T22:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7167#issuecomment-59298",
    "user": "https://github.com/kcrisman"
}
```

Changing component from porting to AIX or HP-UX ports.



---

archive/issue_comments_059299.json:
```json
{
    "body": "This was with ECL 9.8.4. Sage now uses ECL 16.1.2.\n\nIs this still failing or has one of the ECL upgrades fixed it?",
    "created_at": "2019-01-14T22:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7167#issuecomment-59299",
    "user": "https://github.com/slel"
}
```

This was with ECL 9.8.4. Sage now uses ECL 16.1.2.

Is this still failing or has one of the ECL upgrades fixed it?



---

archive/issue_comments_059300.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7167#issuecomment-59300",
    "user": "https://github.com/mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_comments_059301.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7167#issuecomment-59301",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_events_016954.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-06-23T21:26:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7167",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7167#event-16954"
}
```



---

archive/issue_events_016955.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-06-24T06:28:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7167",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7167#event-16955"
}
```



---

archive/issue_comments_059302.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-24T06:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7167#issuecomment-59302",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
