# Issue 8097: termcap fails to build in Open Solaris x64 as 64 bit

Issue created by migration from https://trac.sagemath.org/ticket/8097

Original creator: jsp

Original creation time: 2010-01-27 20:55:21

Assignee: drkirkby

With no CFLAGS set the build is 32 bit



```
gcc -std=gnu99 -O2 -g -m64 -D_REENTRANT -D_THREAD_SAFE -I/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include -O2 -g -m64 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o .libs/certtool certtool-gaa.o certtool.o prime.o certtool-cfg.o cfg+.o cfgfile.o cmdline.o parse.o props.o shared.o dynfgets.o strctype.o strdyn.o strplus.o  ../lib/.libs/libgnutls.so -L/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib -lz ../gl/.libs/libgnu.a /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib/libgcrypt.so /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib/libgpg-error.so -lreadline -ltermcap -lnsl -lsocket  -R/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib
ld: warning: file /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib/libtermcap.a(termcap.o): wrong ELF class: ELFCLASS32

```



A patch is ready.

Jaap




---

Attachment


---

Comment by jsp created at 2010-01-27 21:05:21

The spkgs can be found here:



```
http://boxen.math.washington.edu/home/jsp/ports/termcap-1.3.1.p1.spkg
```



Jaap


---

Comment by jsp created at 2010-01-27 21:05:21

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-28 08:51:48

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-01-28 08:51:48

The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris.

A more accurate comment would be. 

 * #8097 Ensures the compiler flag -m64 is added at any time SAGE64 was set to "yes" - previously this was only happening on OS X. This should aid building 64-bit on any platform, although it has only been tested on Open Solaris. 

It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. 

It would be good to see some evidence the patch actually works. Such as by showing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and for others, adding it does not generate 64-bit binaries. 

For zlib, adding -m64 stops the build of shared libraries. 

Dave


---

Comment by jsp created at 2010-01-28 11:13:38

Replying to [comment:2 drkirkby]:

> 
> It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. 
> 
> It would be good to see some evidence the patch actually works. Such as by showing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and for others, adding it does not generate 64-bit binaries. 
> 
> For zlib, adding -m64 stops the build of shared libraries. 
> 

I really don't like those cut and paste comments.


Jaap


---

Comment by drkirkby created at 2010-01-28 12:00:14

Sorry, I did not mean to offend by putting the same comment more than once.


---

Attachment

Changed SPKG.txt to reflect the comments from David.

No change of patch level applied.

[http://boxen.math.washington.edu/home/jsp/ports/termcap-1.3.1.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/termcap-1.3.1.p1.spkg)

termcap only builds a static library local/lib/libtermcap.a containing

64 bit *.o files (I double checked that).

Jaap


---

Comment by jsp created at 2010-01-28 13:49:30

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-01-28 13:53:22

Agreed. Positive review.


---

Comment by drkirkby created at 2010-01-28 13:53:22

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-01-28 14:15:29

Chacking static libraries:



```
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ ar -x local/lib/libtermcap.a 
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ ls
COPYING.txt  install.log  local     README.txt	sage-python	     spkg	tmp	  version.o
data	     ipython	  makefile  sage	sage-README-osx.txt  termcap.o	tparam.o
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ file *.o
termcap.o:	ELF 64-bit LSB relocatable AMD64 Version 1
tparam.o:	ELF 64-bit LSB relocatable AMD64 Version 1
version.o:	ELF 64-bit LSB relocatable AMD64 Version 1

```



Jaap


---

Comment by mpatel created at 2010-02-11 15:13:08

Resolution: fixed
