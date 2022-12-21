# Issue 7127: libgcrypt fails to build in 64-bit on Solaris SPARC with gcc

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-05 21:42:06

Assignee: tbd

Building on
 * Sun Blade 2000, Solaris 10 update 7
 * gcc 4.4.1
 * SAGE64 exported to 'yes'
 * Sage 4.1.2.rc0, which includes 
 * libgcrypt-1.4.3, as update at #7045.

The build failed with the errors below. 


```

-I/export/home/drkirkby/sage/gcc64-sage-4.1.2.rc0/local/include -O2 -m64 -g -Wall -MT mpih-add1-asm.lo -MD -MP -MF .deps/mpih-add1-asm.Tpo -c mpih-add1-asm.S  -fPIC -DPIC -o .libs/mpih-add1-asm.o
/usr/ccs/bin/as: "/var/tmp//ccySzxz6.s", line 31: error: detect global register use not covered .register pseudo-op
/usr/ccs/bin/as: "/var/tmp//ccySzxz6.s", line 34: error: detect global register use not covered .register pseudo-op
/usr/ccs/bin/as: "/var/tmp//ccySzxz6.s", line 45: error: detect global register use not covered .register pseudo-op
/usr/ccs/bin/as: "/var/tmp//ccySzxz6.s", line 49: error: detect global register use not covered .register pseudo-op
/usr/ccs/bin/as: "/var/tmp//ccySzxz6.s", line 205: error: detect global register use not covered .register pseudo-op
/usr/ccs/bin/as: "/var/tmp//ccySzxz6.s", line 206: error: detect global register use not covered .register pseudo-op
make[4]: *** [mpih-add1-asm.lo] Error 1
make[4]: Leaving directory `/export/home/drkirkby/sage/gcc64-sage-4.1.2.rc0/spkg/build/libgcrypt-1.4.4/src/mpi'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage/gcc64-sage-4.1.2.rc0/spkg/build/libgcrypt-1.4.4/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage/gcc64-sage-4.1.2.rc0/spkg/build/libgcrypt-1.4.4/src'
failed to build libgcrypt

real    1m53.930s
user    0m36.852s
sys     1m1.741s
sage: An error occurred while installing libgcrypt-1.4.4
```


A Google found this page on the gnupg-users mailing list. 

[gnupg compilation problems on Solaris 10 64 bit](http://www.mail-archive.com/gnupg-users`@`gnupg.org/msg09887.html) 

Someone suggested the person having the problem should use:



```
./configure with --disable-asm
```


That fixed the problem for him. 

So I changed the spkg-install so the assembly code was disabled on 64-bit Solaris. However, whilst the above problem did not display (I think the build got further this time), it did eventually fail with 


```
ld: fatal: file /export/home/drkirkby/sage/gcc64-sage-4.1.2.rc0/local/lib/libgpg-error.so: wrong ELF class: ELFCLASS32
```


It looks like some code is being built 32-bit, and other code 64-bit, which is the usual cause of this _wrong ELF class:_ message.

Hence there remains a bug to be fixed here. 

Dave


---

Comment by drkirkby created at 2009-10-05 22:16:16

The error is quite possibly not libgrypt's at all. Several libraries are being built as 32-bit in Sage, despite SAGE64 being set to 'yes'. Here is the result of 'file' on $SAGE_HOME/local/lib. As you can see, some are 32-bit, some are 64-bit. 



```
libbz2.a:       current ar archive, not a dynamic executable or shared object
libgpg-error.a: current ar archive, not a dynamic executable or shared object
libgpg-error.la:        commands text
libgpg-error.so:        ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libgpg-error.so.0:      ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libgpg-error.so.0.4.0:  ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libhistory.a:   current ar archive, not a dynamic executable or shared object
libhistory.so:  ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libhistory.so.6:        ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libreadline.a:  current ar archive, not a dynamic executable or shared object
libreadline.so: ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libreadline.so.6:       ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libsqlite3.a:   current ar archive, not a dynamic executable or shared object
libsqlite3.la:  commands text
libsqlite3.so:  ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libsqlite3.so.0:        ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libsqlite3.so.0.8.6:    ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libtermcap.a:   current ar archive, not a dynamic executable or shared object
libz.so:        ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libz.so.1:      ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libz.so.1.2.3:  ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
```



---

Comment by drkirkby created at 2011-04-02 13:07:12

This can be closed as fixed. I'm not exactly sure when the last time any 32-bit code was produced when the environment variable `SAGE64` was set to "yes", but it is a long time ago. A 64-bit Solaris port seems not too far off now. 

Dave


---

Comment by jdemeyer created at 2011-04-05 15:52:31

Resolution: worksforme
