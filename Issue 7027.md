# Issue 7027: f2c ignores CC and uses gcc anyway

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 11:40:58

Assignee: tbd

CC:  mjo

Using 

 * Solaris 10 update 7 on SPARC
 * sage-4.1.2.alpha2
 * Sun Studio 12.1
 * An updated configure script to allow the Sun compiler to be used.


```
f2c-20070816.p1/src/libf2c/._z_sqrt.c
f2c-20070816.p1/src/libf2c/z_sqrt.c
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
make[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/f2c-20070816.p1/src/libf2c'
gcc -c f77vers.c
gcc -c i77vers.c

```



f2c is far from the only program which ignores CC.


---

Comment by ohanar created at 2012-02-09 14:33:23

Changing status from new to needs_review.


---

Comment by mjo created at 2012-02-09 16:58:06

Can you do CFLAGS, too, while you're in there?


---

Comment by mjo created at 2012-02-09 17:26:18

Oh, and $MAKE!


---

Comment by ohanar created at 2012-02-10 09:54:53

Ok, updated with $MAKE and $CFLAGS.

There was a silly patch whose entire purpose was to make the f2c makefile respect global cflags, of course the spkg-install wouldn't respect those cflags :-/. I am now just passing the cflags at the end of the make line in spkg-install, rather than patching the makefile.


---

Comment by mjo created at 2012-02-11 04:14:05

I think there are some left-over files in there:


```
f2c-20070816.p3 $ sage -hg status
? ._.hg
? ._.hgignore
? ._SPKG.txt
? ._spkg-install
? patches/._f2c.makefile
```



---

Comment by mjo created at 2012-02-11 04:22:13

Why do we need both `patches/libf2c.makefile` and `patches/libf2c.makefile.patch`? It looks to me like the patch does the same thing as replacing the upstream makefile with libf2c.makefile:


```
$ diff -u src/libf2c/makefile patches/libf2c.makefile
--- src/libf2c/makefile	2007-08-14 21:26:15.000000000 -0400
+++ patches/libf2c.makefile	2012-02-10 04:31:00.000000000 -0500
`@``@` -70,10 +70,10 `@``@`
 ### If your system lacks ranlib, you don't need it; see README.
 
 f77vers.o: f77vers.c
-	$(CC) -c f77vers.c
+	$(CC) -c $(CFLAGS) f77vers.c
 
 i77vers.o: i77vers.c
-	$(CC) -c i77vers.c
+	$(CC) -c $(CFLAGS) i77vers.c
 
 # To get an "f2c.h" for use with "f2c -C++", first "make hadd"
 hadd: f2c.h0 f2ch.add
```



```
$ cat patches/libf2c.makefile.patch 
--- libf2c.makefile.orig	2009-01-20 00:22:57.000000000 -0800
+++ libf2c.makefile	2009-01-20 00:22:25.000000000 -0800
`@``@` -70,10 +70,10 `@``@`
 ### If your system lacks ranlib, you don't need it; see README.
 
 f77vers.o: f77vers.c
-	$(CC) -c f77vers.c
+	$(CC) -c $(CFLAGS) f77vers.c
 
 i77vers.o: i77vers.c
-	$(CC) -c i77vers.c
+	$(CC) -c $(CFLAGS) i77vers.c
 
 # To get an "f2c.h" for use with "f2c -C++", first "make hadd"
 hadd: f2c.h0 f2ch.add
```


Is there a reason to keep both around and not just the patch?


---

Comment by mjo created at 2012-02-11 04:22:13

Changing status from needs_review to needs_work.


---

Comment by ohanar created at 2012-02-11 04:42:12

Replying to [comment:5 mjo]:
> I think there are some left-over files in there:
> 
> {{{
> f2c-20070816.p3 $ sage -hg status
> ? ._.hg
> ? ._.hgignore
> ? ._SPKG.txt
> ? ._spkg-install
> ? patches/._f2c.makefile
> }}}

FYI, these files were in the previous package, probably from someone working on OSX (it seems to like creating these files).


---

Comment by ohanar created at 2012-02-11 04:51:37

Replying to [comment:6 mjo]:
> Why do we need both `patches/libf2c.makefile` and `patches/libf2c.makefile.patch`? It looks to me like the patch does the same thing as replacing the upstream makefile with libf2c.makefile:
> 
> {{{
> $ diff -u src/libf2c/makefile patches/libf2c.makefile
> --- src/libf2c/makefile	2007-08-14 21:26:15.000000000 -0400
> +++ patches/libf2c.makefile	2012-02-10 04:31:00.000000000 -0500
> `@``@` -70,10 +70,10 `@``@`
>  ### If your system lacks ranlib, you don't need it; see README.
>  
>  f77vers.o: f77vers.c
> -	$(CC) -c f77vers.c
> +	$(CC) -c $(CFLAGS) f77vers.c
>  
>  i77vers.o: i77vers.c
> -	$(CC) -c i77vers.c
> +	$(CC) -c $(CFLAGS) i77vers.c
>  
>  # To get an "f2c.h" for use with "f2c -C++", first "make hadd"
>  hadd: f2c.h0 f2ch.add
> }}}
> 
> {{{
> $ cat patches/libf2c.makefile.patch 
> --- libf2c.makefile.orig	2009-01-20 00:22:57.000000000 -0800
> +++ libf2c.makefile	2009-01-20 00:22:25.000000000 -0800
> `@``@` -70,10 +70,10 `@``@`
>  ### If your system lacks ranlib, you don't need it; see README.
>  
>  f77vers.o: f77vers.c
> -	$(CC) -c f77vers.c
> +	$(CC) -c $(CFLAGS) f77vers.c
>  
>  i77vers.o: i77vers.c
> -	$(CC) -c i77vers.c
> +	$(CC) -c $(CFLAGS) i77vers.c
>  
>  # To get an "f2c.h" for use with "f2c -C++", first "make hadd"
>  hadd: f2c.h0 f2ch.add
> }}}
> 
> Is there a reason to keep both around and not just the patch?

Nope, but that wasn't the initial goal of this ticket, that said I've changed the purpose/description.


---

Comment by ohanar created at 2012-02-11 05:12:50

Changing status from needs_work to needs_review.


---

Comment by ohanar created at 2012-02-11 05:12:50

ok, I've made those changes (plus cleaned up the source directory, which wasn't pristine)


---

Comment by mjo created at 2012-02-11 14:47:06

Replying to [comment:9 ohanar]:
> ok, I've made those changes (plus cleaned up the source directory, which wasn't pristine)

Thanks for taking the time to do this, I didn't check the old SPKG for those files.

I've compared the p2 and p3 `src` directories after patching; they look equivalent given the `spkg-install` changes.

To test the original issue, I've replaced `$CC` and `$CFLAGS` in both makefiles with junk. If I don't set my environment variables, the build crashes. If I export a real `$CC` and `$CFLAGS`, it builds fine.

I built with `MAKE=make -j40` with no problems.


---

Comment by mjo created at 2012-02-11 14:47:06

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2012-02-11 17:03:06

I would have thought it sensible to check the return value of 'patch'. Any changes in the package are could easily stop the patch applying cleanly, if at all, yet that is not tested. 

Dave


---

Comment by ohanar created at 2012-02-11 17:25:42

Changing status from positive_review to needs_work.


---

Comment by ohanar created at 2012-02-11 17:25:42

Replying to [comment:11 drkirkby]:
> I would have thought it sensible to check the return value of 'patch'. Any changes in the package are could easily stop the patch applying cleanly, if at all, yet that is not tested. 

Yup, I agree, I've uploaded a new spkg that adds a check.
> 
> Dave


---

Comment by ohanar created at 2012-02-11 17:26:10

Changing status from needs_work to needs_review.


---

Comment by mjo created at 2012-02-11 19:38:50

Changing status from needs_review to needs_work.


---

Comment by mjo created at 2012-02-11 19:38:50

Replying to [comment:11 drkirkby]:
> I would have thought it sensible to check the return value of 'patch'. Any changes in the package are could easily stop the patch applying cleanly, if at all, yet that is not tested. 

If we want to go this route, we'll have to set the fuzz factor. Otherwise, GNU patch, at least, will happily return success:


```
$ emacs makefile
$ patch -p0 < ../../patches/libf2c.makefile.patch 
patching file makefile
Hunk #1 succeeded at 73 with fuzz 1 (offset 3 lines).
$ echo $?
0
```


Using `--fuzz=0` should catch that, but will still miss large offsets. I don't know if there's a way to catch those... `patch` is returning success here even for huge offsets:


```
$ patch --fuzz=0 -p0 < ../../patches/libf2c.makefile.patch 
patching file makefile
Hunk #1 succeeded at 111 (offset 41 lines).
$ echo $?
0
```


Whoever is upgrading the package would hopefully check for this, but maybe there's a smarter way that I haven't found yet.

Anyway, these are back =)


```
$ sage -hg status
? ._.hg
? ._.hgignore
? ._SPKG.txt
? ._spkg-install
? patches/._f2c.makefile
```



---

Comment by drkirkby created at 2012-02-11 19:53:04

People updating packages, whilst not taking care of patches, has been a problem several times in Sage. Anything that could be done to reduce that would be good, but maybe it's not possible to do it very well. 

Dave


---

Attachment

for review purposes


---

Comment by ohanar created at 2012-02-12 22:35:03

Changing status from needs_work to needs_review.


---

Comment by ohanar created at 2012-02-12 22:35:03

Ok, new version, got rid of the `._` files again (which was my bad, since I restarted off of the p2 package). I've also made some more changes to spkg-install, added some comments, moved some stuff around, made it more uniform, as well as make a libf2c directory in patches, just to make it easy to add patches in the future, if they are ever needed.


---

Comment by mjo created at 2012-02-23 18:24:32

This one looks good.

For future reference, we can probably drop the `-g` (debug) flag, and shouldn't install `libf2c` if building `f2c` fails, but those are minor and unrelated to this ticket.


---

Comment by mjo created at 2012-02-23 18:24:32

Changing status from needs_review to positive_review.


---

Comment by ohanar created at 2012-02-23 18:27:56

Replying to [comment:17 mjo]:
> For future reference, we can probably drop the `-g` (debug) flag, 
Yeah, I didn't know why we had this, but I didn't want to break anything, so I kept it for safe measure.


---

Comment by jdemeyer created at 2012-02-23 20:06:05

Replying to [comment:14 mjo]:
> but will still miss large offsets. I don't know if there's a way to catch those... `patch` is returning success here even for huge offsets
Those are pretty innocent and not a big deal in my opinion.  I have never seen a patch applied wrongly because of this.


---

Comment by jdemeyer created at 2012-02-23 20:11:34

CC needs quoting:

```
$MAKE CC="$CC" CFLAGS="${CFLAGS}" 
```


Also, it would be good to mention the ticket number in `SPKG.txt`.

(you can set back positive review yourself after making these trivial changes)


---

Comment by jdemeyer created at 2012-02-23 20:11:34

Changing status from positive_review to needs_work.


---

Comment by ohanar created at 2012-02-23 20:18:27

Changing status from needs_work to positive_review.


---

Comment by ohanar created at 2012-02-23 20:18:27

Replying to [comment:20 jdemeyer]:
> CC needs quoting:
done
> 
> Also, it would be good to mention the ticket number in `SPKG.txt`.
and done


---

Comment by jdemeyer created at 2012-02-24 15:46:07

I made `spkg-check` executable, as it should be.


---

Comment by jdemeyer created at 2012-02-27 11:19:29

Resolution: fixed
