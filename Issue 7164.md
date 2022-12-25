# Issue 7164: readline-6.0 fails to build on HP-UX 11i (PA-RISC)

archive/issues_007164.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  david.kirkby@onetel.net\n\nKeywords: HP-UX\n\nI decided to attempt a build of Sage on HP-UX. The setup is:\n\n* HP C3600 workstation\n* PS-RISC processor running at 552 MHz.\n* 1 GB RAM\n* 2 x 36 GB disks \n* HP-UK 11i \n \nThe first failure is readline-6.0\n\n \n\n```\n       gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='\"6.0\"' -O2  -g  -Wall  misc.c\nmisc.c: In function '_rl_revert_all_lines':\nmisc.c:456: warning: suggest parentheses around assignment used as truth value\n        rm -f compat.o\n        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='\"6.0\"' -O2  -g  -Wall  compat.c\n        rm -f xmalloc.o\n        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='\"6.0\"' -O2  -g  -Wall  xmalloc.c\n        rm -f history.o\n        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='\"6.0\"' -O2  -g  -Wall  history.c\n        rm -f histexpand.o\n        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='\"6.0\"' -O2  -g  -Wall  histexpand.c\nhistexpand.c: In function 'get_history_event':\nhistexpand.c:207: warning: suggest parentheses around assignment used as truth value\n        rm -f histfile.o\n        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='\"6.0\"' -O2  -g  -Wall  histfile.c\nhistfile.c: In function 'read_history_range':\nhistfile.c:251: warning: array subscript has type 'char'\nhistfile.c:268: warning: array subscript has type 'char'\nhistfile.c: In function 'history_truncate_file':\nhistfile.c:378: warning: array subscript has type 'char'\nhistfile.c:390: warning: array subscript has type 'char'\n        rm -f histsearch.o\n        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='\"6.0\"' -O2  -g  -Wall  histsearch.c\n        rm -f shell.o\n        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='\"6.0\"' -O2  -g  -Wall  shell.c\n        rm -f mbutil.o\n        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='\"6.0\"' -O2  -g  -Wall  mbutil.c\n        rm -f tilde.o\n        gcc -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='\"6.0\"' -O2  -g  -Wall  -DREADLINE_LIBRARY -c ./tilde.c\n./tilde.c: In function 'tilde_expand':\n./tilde.c:199: warning: suggest parentheses around assignment used as truth value\n        rm -f libreadline.a\n        ar cr libreadline.a readline.o vi_mode.o funmap.o keymaps.o parens.o search.o  rltty.o complete.o bind.o isearch.o display.o signals.o  util.o kill.o undo.o macro.o input.o callback.o terminal.o  text.o nls.o misc.o compat.o xmalloc.o history.o histexpand.o histfile.o histsearch.o shell.o mbutil.o tilde.o\n        test -n \"ranlib\" && ranlib libreadline.a\n        rm -f libhistory.a\n        ar cr libhistory.a history.o histexpand.o histfile.o histsearch.o shell.o mbutil.o xmalloc.o\n        test -n \"ranlib\" && ranlib libhistory.a\n        for f in readline.h chardefs.h keymaps.h history.h tilde.h  rlstdc.h rlconf.h rltypedefs.h; do \\\n                ./support/install.sh -c -m 644 ./$f /home/drkirkby/sage-4.1.2.rc0/local/include/readline ; \\\n        done\n        ( if test -d doc ; then \\\n                cd doc && \\\n                make b infodir=/home/drkirkby/sage-4.1.2.rc0/local/share/info DESTDIR= install; \\\n          fi )\nMake: Don't know how to make b.  Stop.\n*** Error exit code 1 (ignored)\n        test -d shlib || mkdir shlib\n        ( cd shlib ; make b all )\nMake: Don't know how to make b.  Stop.\n*** Error exit code 1 (ignored)\n        ( cd examples ; make b DESTDIR= install )\nMake: Don't know how to make b.  Stop.\n*** Error exit code 1 (ignored)\n        mv /home/drkirkby/sage-4.1.2.rc0/local/lib/libreadline.a /home/drkirkby/sage-4.1.2.rc0/local/lib/libreadline.old\nmv: /home/drkirkby/sage-4.1.2.rc0/local/lib/libreadline.a: cannot access: No such file or directory\n*** Error exit code 1 (ignored)\n        ./support/install.sh -c -m 644 libreadline.a /home/drkirkby/sage-4.1.2.rc0/local/lib/libreadline.a\n        test -n \"ranlib\" && ranlib /home/drkirkby/sage-4.1.2.rc0/local/lib/libreadline.a\n        mv /home/drkirkby/sage-4.1.2.rc0/local/lib/libhistory.a /home/drkirkby/sage-4.1.2.rc0/local/lib/libhistory.old\nmv: /home/drkirkby/sage-4.1.2.rc0/local/lib/libhistory.a: cannot access: No such file or directory\n*** Error exit code 1 (ignored)\n        ./support/install.sh -c -m 644 libhistory.a /home/drkirkby/sage-4.1.2.rc0/local/lib/libhistory.a\n        test -n \"ranlib\" && ranlib /home/drkirkby/sage-4.1.2.rc0/local/lib/libhistory.a\n        ( cd shlib ; make b DESTDIR= install )\nMake: Don't know how to make b.  Stop.\n*** Error exit code 1 (ignored)\nReadline's build claims to have finished, but files that should have been built weren't.\n\nreal    7m22.286s\nuser    1m7.990s\nsys     0m15.820s\nsage: An error occurred while installing readline-6.0\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7164\n\n",
    "created_at": "2009-10-08T21:33:02Z",
    "labels": [
        "component: porting",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "readline-6.0 fails to build on HP-UX 11i (PA-RISC)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7164",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  david.kirkby@onetel.net

Keywords: HP-UX

I decided to attempt a build of Sage on HP-UX. The setup is:

* HP C3600 workstation
* PS-RISC processor running at 552 MHz.
* 1 GB RAM
* 2 x 36 GB disks 
* HP-UK 11i 
 
The first failure is readline-6.0

 

```
       gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='"6.0"' -O2  -g  -Wall  misc.c
misc.c: In function '_rl_revert_all_lines':
misc.c:456: warning: suggest parentheses around assignment used as truth value
        rm -f compat.o
        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='"6.0"' -O2  -g  -Wall  compat.c
        rm -f xmalloc.o
        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='"6.0"' -O2  -g  -Wall  xmalloc.c
        rm -f history.o
        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='"6.0"' -O2  -g  -Wall  history.c
        rm -f histexpand.o
        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='"6.0"' -O2  -g  -Wall  histexpand.c
histexpand.c: In function 'get_history_event':
histexpand.c:207: warning: suggest parentheses around assignment used as truth value
        rm -f histfile.o
        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='"6.0"' -O2  -g  -Wall  histfile.c
histfile.c: In function 'read_history_range':
histfile.c:251: warning: array subscript has type 'char'
histfile.c:268: warning: array subscript has type 'char'
histfile.c: In function 'history_truncate_file':
histfile.c:378: warning: array subscript has type 'char'
histfile.c:390: warning: array subscript has type 'char'
        rm -f histsearch.o
        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='"6.0"' -O2  -g  -Wall  histsearch.c
        rm -f shell.o
        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='"6.0"' -O2  -g  -Wall  shell.c
        rm -f mbutil.o
        gcc -c -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='"6.0"' -O2  -g  -Wall  mbutil.c
        rm -f tilde.o
        gcc -DHAVE_CONFIG_H    -I. -I. -DRL_LIBRARY_VERSION='"6.0"' -O2  -g  -Wall  -DREADLINE_LIBRARY -c ./tilde.c
./tilde.c: In function 'tilde_expand':
./tilde.c:199: warning: suggest parentheses around assignment used as truth value
        rm -f libreadline.a
        ar cr libreadline.a readline.o vi_mode.o funmap.o keymaps.o parens.o search.o  rltty.o complete.o bind.o isearch.o display.o signals.o  util.o kill.o undo.o macro.o input.o callback.o terminal.o  text.o nls.o misc.o compat.o xmalloc.o history.o histexpand.o histfile.o histsearch.o shell.o mbutil.o tilde.o
        test -n "ranlib" && ranlib libreadline.a
        rm -f libhistory.a
        ar cr libhistory.a history.o histexpand.o histfile.o histsearch.o shell.o mbutil.o xmalloc.o
        test -n "ranlib" && ranlib libhistory.a
        for f in readline.h chardefs.h keymaps.h history.h tilde.h  rlstdc.h rlconf.h rltypedefs.h; do \
                ./support/install.sh -c -m 644 ./$f /home/drkirkby/sage-4.1.2.rc0/local/include/readline ; \
        done
        ( if test -d doc ; then \
                cd doc && \
                make b infodir=/home/drkirkby/sage-4.1.2.rc0/local/share/info DESTDIR= install; \
          fi )
Make: Don't know how to make b.  Stop.
*** Error exit code 1 (ignored)
        test -d shlib || mkdir shlib
        ( cd shlib ; make b all )
Make: Don't know how to make b.  Stop.
*** Error exit code 1 (ignored)
        ( cd examples ; make b DESTDIR= install )
Make: Don't know how to make b.  Stop.
*** Error exit code 1 (ignored)
        mv /home/drkirkby/sage-4.1.2.rc0/local/lib/libreadline.a /home/drkirkby/sage-4.1.2.rc0/local/lib/libreadline.old
mv: /home/drkirkby/sage-4.1.2.rc0/local/lib/libreadline.a: cannot access: No such file or directory
*** Error exit code 1 (ignored)
        ./support/install.sh -c -m 644 libreadline.a /home/drkirkby/sage-4.1.2.rc0/local/lib/libreadline.a
        test -n "ranlib" && ranlib /home/drkirkby/sage-4.1.2.rc0/local/lib/libreadline.a
        mv /home/drkirkby/sage-4.1.2.rc0/local/lib/libhistory.a /home/drkirkby/sage-4.1.2.rc0/local/lib/libhistory.old
mv: /home/drkirkby/sage-4.1.2.rc0/local/lib/libhistory.a: cannot access: No such file or directory
*** Error exit code 1 (ignored)
        ./support/install.sh -c -m 644 libhistory.a /home/drkirkby/sage-4.1.2.rc0/local/lib/libhistory.a
        test -n "ranlib" && ranlib /home/drkirkby/sage-4.1.2.rc0/local/lib/libhistory.a
        ( cd shlib ; make b DESTDIR= install )
Make: Don't know how to make b.  Stop.
*** Error exit code 1 (ignored)
Readline's build claims to have finished, but files that should have been built weren't.

real    7m22.286s
user    1m7.990s
sys     0m15.820s
sage: An error occurred while installing readline-6.0

```


Issue created by migration from https://trac.sagemath.org/ticket/7164





---

archive/issue_comments_059273.json:
```json
{
    "body": "This fix to this was very simple. The spkg-install contains a long list of different names for the library on different platforms\n\n\n```\nif [ $UNAME = \"Darwin\" ]; then\n  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.dylib\nelif [ $UNAME = \"CYGWIN\" ]; then\n  # It is of course very lame that readline names the file .dll.a, but that's what it does.\n  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.dll.a\nelif [ \"$UNAME\" = \"OpenBSD\" ]; then\n  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.so.6.0\nelif [ \"$UNAME\" = \"FreeBSD\" ]; then\n  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.so.6\nelse\n  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.so\nfi\n```\n\n\nAll I needed to do was to add the appropriate two lines for HP-UX. \n\n\n```\nelif [ \"$UNAME\" = \"HP-UX\" ]; then\n  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.sl.6\n```\n\n\nHP use the extenstion 'sl' for shared libraries on HP-UX. \n\nThe updated spkg, along with the SPKG.txt and spkg-install can be found here. \nhttp://sage.math.washington.edu/home/kirkby/HP-UX-fixes/readline-6.0.p0/",
    "created_at": "2009-11-21T18:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7164#issuecomment-59273",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This fix to this was very simple. The spkg-install contains a long list of different names for the library on different platforms


```
if [ $UNAME = "Darwin" ]; then
  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.dylib
elif [ $UNAME = "CYGWIN" ]; then
  # It is of course very lame that readline names the file .dll.a, but that's what it does.
  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.dll.a
elif [ "$UNAME" = "OpenBSD" ]; then
  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.so.6.0
elif [ "$UNAME" = "FreeBSD" ]; then
  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.so.6
else
  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.so
fi
```


All I needed to do was to add the appropriate two lines for HP-UX. 


```
elif [ "$UNAME" = "HP-UX" ]; then
  DYLIB_NAME=$SAGE_LOCAL/lib/libreadline.sl.6
```


HP use the extenstion 'sl' for shared libraries on HP-UX. 

The updated spkg, along with the SPKG.txt and spkg-install can be found here. 
http://sage.math.washington.edu/home/kirkby/HP-UX-fixes/readline-6.0.p0/



---

archive/issue_comments_059274.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-21T18:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7164#issuecomment-59274",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059275.json:
```json
{
    "body": "There isn't much I can referee since I don't use HP-UX at all. As far as I can see the patch is fine.",
    "created_at": "2009-12-08T13:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7164#issuecomment-59275",
    "user": "https://github.com/malb"
}
```

There isn't much I can referee since I don't use HP-UX at all. As far as I can see the patch is fine.



---

archive/issue_comments_059276.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T13:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7164#issuecomment-59276",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059277.json:
```json
{
    "body": "The spkg here doesn't have the changes checked in: http://sage.math.washington.edu/home/kirkby/HP-UX-fixes/readline-6.0.p0/\n\nOtherwise, this is as safe as a bank vault, so I'm fine with it going in.",
    "created_at": "2009-12-08T18:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7164#issuecomment-59277",
    "user": "https://github.com/williamstein"
}
```

The spkg here doesn't have the changes checked in: http://sage.math.washington.edu/home/kirkby/HP-UX-fixes/readline-6.0.p0/

Otherwise, this is as safe as a bank vault, so I'm fine with it going in.



---

archive/issue_comments_059278.json:
```json
{
    "body": "Mhansen -- if you merge this, be sure to fix the spkg, which doesn't have the hg repo checked in!",
    "created_at": "2009-12-08T18:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7164#issuecomment-59278",
    "user": "https://github.com/williamstein"
}
```

Mhansen -- if you merge this, be sure to fix the spkg, which doesn't have the hg repo checked in!



---

archive/issue_comments_059279.json:
```json
{
    "body": "Doh! I will write \"I will check the hg repo\" 100 times now on my blackboard.",
    "created_at": "2009-12-08T18:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7164#issuecomment-59279",
    "user": "https://github.com/malb"
}
```

Doh! I will write "I will check the hg repo" 100 times now on my blackboard.



---

archive/issue_comments_059280.json:
```json
{
    "body": "I've merged  http://sage.math.washington.edu/home/mhansen/readline-6.0.p1.spkg which has these changes along with the ones at #7610..",
    "created_at": "2009-12-09T02:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7164#issuecomment-59280",
    "user": "https://github.com/mwhansen"
}
```

I've merged  http://sage.math.washington.edu/home/mhansen/readline-6.0.p1.spkg which has these changes along with the ones at #7610..



---

archive/issue_comments_059281.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T02:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7164#issuecomment-59281",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
