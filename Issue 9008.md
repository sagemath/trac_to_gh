# Issue 9008: Update zlib to latest upstream, and clean up spkg-install

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-21 14:40:02

Assignee: GeorgSWeber

CC:  jsp

The zlib package building 32-bit on OpenSolaris (see #7128), and has various hacks to make it build 64-bit on OS X. The spkg-install has various hacks, which I think are better implemented other ways. 

1) 

```
-I\"$SAGE_LOCAL/include\""
```


seems better replaced by the command line option available on the configure script. 


```
--includedir="$SAGE_LOCAL/include" 
```


2) Adding 

```
-m64
}}} 
is not currently the correct way to make a 64-bit build - the option 

{{{
--64
}}}

is for that purpose. The developer (Mark Alder) was surprised hacks were needed for OS X, as that is his main development platform. 

3) The spkg-install adds 

{{{
-fPIC
}}}

which apparently is(was) needed on Debian on Itanium. It would seem more sensible to add that option just on that platform if it is a  problem specific to that platform. 

This package is much cleaner, but may not work on all platforms. It would be better to make the code cleaner, and fix what (if any) issues do actually still exist. 

Dave


---

Comment by drkirkby created at 2010-05-21 15:30:42

Here's a package. I've not committed the Mercurial repository, so have not marked it for review, but just for testing now. 


http://boxen.math.washington.edu/home/kirkby/patches/zlib-1.2.5/zlib-1.2.5.spkg


---

Comment by drkirkby created at 2010-05-21 15:30:42

Changing status from new to needs_info.


---

Comment by drkirkby created at 2010-05-28 21:52:47

I've now tested this on OpenSolaris, OS X and Linux. Setting SAGE64 to "yes" forces a 64-bit build. The binaries can be seen to be 64-bit when built with SAGE64=yes. 


```
drkirkby`@`hawk:~/sage-4.4.2$ file local/lib/libz.*
local/lib/libz.a:	current ar archive, not a dynamic executable or shared object
local/lib/libz.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
local/lib/libz.so.1:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
local/lib/libz.so.1.2.5:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
drkirkby`@`hawk:~/sage-4.4.2$ 
```


The -fPIC flag is added by the latest zlib source code, so there is no need for spkg-install to add it. 

As such, I do not envisage any problems with this package. It is now ready for review. Please get it from:

http://boxen.math.washington.edu/home/kirkby/patches/zlib-1.2.5/zlib-1.2.5.spkg

Dave


---

Comment by drkirkby created at 2010-05-28 21:52:47

Changing status from needs_info to needs_review.


---

Comment by mhansen created at 2010-06-02 19:52:14

The changes seem good to me; however this is failing to build in Cygwin with the following error:


```
cp libz.a /home/mhansen/sage-4.3.5/local/lib
cp  /home/mhansen/sage-4.3.5/local/lib
cp: missing destination file operand after `/home/mhansen/sage-4.3.5/local/lib'
Try `cp --help' for more information.
make: *** [install-libs] Error 1
Error installing zlib
```



---

Comment by drkirkby created at 2010-06-02 20:56:50

Thank you Mike for trying. 

Can you attach the output of the Makefile? The 'configure' script creates a Makefile, which has a section 'install'. When I grep 'cp' from that, I see:


```
#    cp contrib/asm?86/match.S ./match.S
	cp zlib.h zconf.h $(includedir)
	cp $(LIBS) $(libdir)
	cp zlib.3 $(man3dir)
	cp -p Makefile.in Makefile
	cp -p zconf.in.h zconf.h

```


In other words, there is nothing there with a empty destination. But of course, you will get a different Makefile to me. 

Dave


---

Attachment


---

Comment by mhansen created at 2010-06-02 21:01:50

I've attached the Makefile that was generated.


---

Comment by drkirkby created at 2010-06-02 21:28:50

Mike, 
when I grep 'cp' in the Makefile you posted, I see:


```
drkirkby`@`hawk:~$ grep cp zlib-cygwin-Makefile
#    cp contrib/asm?86/match.S ./match.S
	cp $(STATICLIB) $(DESTDIR)$(libdir)
	cp $(SHAREDLIBV) $(DESTDIR)$(sharedlibdir)
	cp zlib.3 $(DESTDIR)$(man3dir)
	cp zlib.pc $(DESTDIR)$(pkgconfigdir)
	cp zlib.h zconf.h $(DESTDIR)$(includedir)
	cp -p zconf.h.in zconf.h
```



When I do a recursive grep of 'DESTDIR' in the package, I find there is no such text anywhere in the package. So it looks to me like DESTDIR is being passed to the configure script - it's not a variable used in the original source code of zlib, or in spkg-install. Note even 'DEST' is used in either spkg-install or the zlib source code. 

It seems *very* strange I must admit. 

Dave 

Dave


---

Comment by drkirkby created at 2010-06-02 21:28:50

Changing assignee from GeorgSWeber to drkirkby.


---

Comment by drkirkby created at 2010-06-02 21:35:35

Replying to [comment:7 drkirkby]:
> Note even 'DEST' is used in either spkg-install or the zlib source code. 
> 
> It seems *very* strange I must admit. 
> 
> Dave 

That was supposed to be *not* even DEST is used. If DESTDIR is not used in Sage (and I don't recall seeing it) and it's not used in zlib, where can it come from? 

Dave


---

Comment by drkirkby created at 2010-06-02 21:51:06

Looking further, I see the text "DESTDIR" is used in the top-level Sage makefile. 


```
drkirkby`@`redstart:~/sage-4.4.3.alpha1$ grep DESTDIR makefile
	if [ "$(DESTDIR)" = "" ]; then \
		echo "Set DESTDIR"; \
	mkdir -p $(DESTDIR)
	mkdir -p $(DESTDIR)/sage
	mkdir -p $(DESTDIR)/bin/
	cp -rpv * $(DESTDIR)/sage/
	python local/bin/sage-hardcode_sage_root $(DESTDIR)/sage/sage "$(DESTDIR)"/sage
	cp $(DESTDIR)/sage/sage $(DESTDIR)/bin/
	cd $(DESTDIR)/bin/; ./sage -c
drkirkby`@`redstart:~/sage-4.4.3.alpha1$
```


It looks like somehow that is being passed as text to the zlib package, and not substituted for something more useful, such as a path. 

Dave


---

Comment by drkirkby created at 2010-06-12 02:15:31

Mike, 

can you try this. 


http://boxen.math.washington.edu/home/kirkby/patches/zlib-1.2.5.spkg

It seems zlib was not building the shared library for you, so the 'cp' command tried to copy the non-existant shared library to the directory /home/mhansen/sage-4.3.5/local/lib. The error message was a bit confusing


```
cp: missing destination file operand after `/home/mhansen/sage-4.3.5/local/lib'
```

was probably better replaced by:

```
cp: missing source file operand before `/home/mhansen/sage-4.3.5/local/lib'
```


I've put this file in a different location to the previous one. Hopefully this will build the shared library too now.


---

Comment by mhansen created at 2010-06-12 04:11:13

Nope, that doesn't work.


```
Checking for shared library support...
Tested gcc -w -c -O3 -fPIC ztest3692.c
Tested -O3 -fPIC -o ztest3692.so ztest3692.o
./configure: line 245: -O3: command not found
No shared library support; try without defining CC and CFLAGS
Building static library libz.a version 1.2.5 with gcc.
```


It seems that the configure script / Makefile is quite messed up for Cygwin.  I've put a new spkg at

http://sage.math.washington.edu/home/mhansen/zlib-1.2.5.spkg

which uses the win32/Makefile.gcc and skips the configure step.  Your changes seem good to me so it's just mine that need to be looked at.


---

Comment by jsp created at 2010-06-12 16:35:03

Mike, Dave,

I think you have done the job.

zlib now builds 64 bit on OpenSolaris out of the box.



```
Successfully installed zlib-1.2.5
You can safely delete the temporary build directory
/export/home/jaap/sage_port/sage-4.4.3/spkg/build/zlib-1.2.5
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing zlib-1.2.5.spkg
-bash-4.0$ ls -l local/lib/libz*
-rw-r--r-- 1 jaap other 133600 2010-06-12 17:28 local/lib/libz.a
lrwxrwxrwx 1 jaap other     13 2010-06-12 17:28 local/lib/libz.so -> libz.so.1.2.5
lrwxrwxrwx 1 jaap other     13 2010-06-12 17:28 local/lib/libz.so.1 -> libz.so.1.2.5
-rwxr-xr-x 1 jaap other 162568 2010-06-10 16:52 local/lib/libz.so.1.2.3
-rwxr-xr-x 1 jaap other 113736 2010-06-12 17:28 local/lib/libz.so.1.2.5
-bash-4.0$ file local/lib/libz*
local/lib/libz.a:       current ar archive, not a dynamic executable or shared object
local/lib/libz.so:      ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
local/lib/libz.so.1:    ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
local/lib/libz.so.1.2.3:        ELF 32-bit LSB dynamic lib 80386 Version 1, dynamically linked, not stripped
local/lib/libz.so.1.2.5:        ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
-bash-4.0$ 

```


Let's give this a positive review.

Jaap


---

Comment by jsp created at 2010-06-12 16:35:03

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-20 14:17:46

Changing priority from major to blocker.


---

Comment by drkirkby created at 2010-06-20 14:17:46

I'm updating this to blocker, as it is a very fundamental file in Sage and is the first one which fails to build properly whilst attempting a 64-bit build on platforms which do not default to 64-bit. It removes some nasty OS X hacks too. 

Dave


---

Comment by rlm created at 2010-06-25 15:38:14

Resolution: fixed
