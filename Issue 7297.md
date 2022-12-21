# Issue 7297: spkg's for libogg and libtheora

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2009-10-25 15:47:27

Assignee: whuss

Keywords: video, animation

Packages for libogg and libtheora. The libtheora spkg installs the
command line tool "png2theora" which can be used to encode a series
of PNG images into a Theora video.

http://www.math.tugraz.at/~huss/spkg/libogg-1.1.4.spkg 

http://www.math.tugraz.at/~huss/spkg/libtheora-1.1.1.spkg




---

Comment by whuss created at 2009-10-25 15:47:54

Changing status from new to needs_review.


---

Comment by mhampton created at 2009-10-26 18:01:04

The end of my install for libtheora looks like this:

```
/bin/sh ./mkinstalldirs /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig
 /usr/bin/install -c -m 644 theora.pc /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig/theora.pc
 /usr/bin/install -c -m 644 theoradec.pc /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig/theoradec.pc
 /usr/bin/install -c -m 644 theoraenc.pc /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig/theoraenc.pc
cp: examples/.libs/png2theora: No such file or directory

real	0m32.161s
user	0m19.908s
sys	0m8.520s
sage: An error occurred while installing libtheora-1.1.1
```


Seems like things compiled OK though.  This is on an intel mac, 10.5.

-Marshall


---

Comment by mhampton created at 2009-10-26 18:47:17

As far as I can tell, there is no attempt to actually build png2theora, its not a failure.  But I am not sure how to edit the makefile to force this build.


---

Comment by whuss created at 2009-10-27 08:22:28

Is there the line


```
Build example code: ......... yes
```


at the end of configure?

Did it find libpng?

The option --enable-examples for configure should force the building of the examples.


---

Comment by mhampton created at 2009-10-27 17:59:44

I do see the "Build example code: ........... yes" string at the end of the configure output.

I don't see any indication of it looking for libpng, either a failure or success.

The only things that are being built inside of spkg/build/libtheora-1.1.1/src/examples are dump_video and dump_psnr.  

-Marshall


---

Comment by mhampton created at 2009-10-27 18:10:10

I think the problem might be that I installed libogg, but this is not being detected by the script "newest_version", which looks in the standard directory for the spkg, which is not copied over.


---

Comment by mhampton created at 2009-10-27 18:18:44

OK, I tried copying the libogg spkg into the spkg/standard directory, but then the configure script fails with:

checking for Ogg... no
*** Could not run Ogg test program, checking why...

-I'm not sure what to try now.


---

Comment by drkirkby created at 2009-12-24 00:16:38

Whats the point of 


```
unset RM
```

in the spkg-install of libogg-1.1.4 ? 

I'd either remove the line, or add a comment why it is needed.


---

Comment by drkirkby created at 2009-12-24 00:20:59

I would add 'set -e' before the 'cp' command in the spkg-install of libtheora-1.1.1. Then, if the copy fails, the spkg-install script will exit with a code of 1. Otherwise, this will appear to have installed correctly, even if the copy fails. 


```
set -e 
cp examples/.libs/png2theora $SAGE_LOCAL/bin
```



---

Comment by pang created at 2010-05-01 08:04:08

Changing status from needs_review to positive_review.


---

Comment by pang created at 2010-05-01 08:04:08

Everything looks fine to me. I also don't understand the "unset RM" line, but I don't think it can hurt in any way. Not an expert in the reviewing process, but I'm giving positive review.


---

Comment by mhansen created at 2010-06-07 05:06:31

Resolution: fixed


---

Comment by dimpase created at 2017-09-19 17:27:44

libtheora no longer builds; if it's not fixed, we'll have to remove it from optional packages...
