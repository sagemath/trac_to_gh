# Issue 7164: readline-6.0 fails to build on HP-UX 11i (PA-RISC)

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-08 21:33:02

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



---

Comment by drkirkby created at 2009-11-21 18:18:35

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

Comment by drkirkby created at 2009-11-21 18:18:35

Changing status from new to needs_review.


---

Comment by malb created at 2009-12-08 13:56:35

There isn't much I can referee since I don't use HP-UX at all. As far as I can see the patch is fine.


---

Comment by malb created at 2009-12-08 13:56:35

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-08 18:26:22

The spkg here doesn't have the changes checked in: http://sage.math.washington.edu/home/kirkby/HP-UX-fixes/readline-6.0.p0/

Otherwise, this is as safe as a bank vault, so I'm fine with it going in.


---

Comment by was created at 2009-12-08 18:26:46

Mhansen -- if you merge this, be sure to fix the spkg, which doesn't have the hg repo checked in!


---

Comment by malb created at 2009-12-08 18:31:43

Doh! I will write "I will check the hg repo" 100 times now on my blackboard.


---

Comment by mhansen created at 2009-12-09 02:35:03

I've merged  http://sage.math.washington.edu/home/mhansen/readline-6.0.p1.spkg which has these changes along with the ones at #7610..


---

Comment by mhansen created at 2009-12-09 02:35:03

Resolution: fixed
