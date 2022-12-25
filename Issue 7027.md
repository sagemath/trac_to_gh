# Issue 7027: f2c ignores CC and uses gcc anyway

archive/issues_007027.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @orlitzky\n\nUsing \n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used.\n\n\n```\nf2c-20070816.p1/src/libf2c/._z_sqrt.c\nf2c-20070816.p1/src/libf2c/z_sqrt.c\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nmake[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/f2c-20070816.p1/src/libf2c'\ngcc -c f77vers.c\ngcc -c i77vers.c\n\n```\n\n\n\nf2c is far from the only program which ignores CC.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7027\n\n",
    "created_at": "2009-09-27T11:40:58Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "f2c ignores CC and uses gcc anyway",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7027",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @orlitzky

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

Issue created by migration from https://trac.sagemath.org/ticket/7027





---

archive/issue_comments_058077.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-02-09T14:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58077",
    "user": "https://github.com/ohanar"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058078.json:
```json
{
    "body": "Can you do CFLAGS, too, while you're in there?",
    "created_at": "2012-02-09T16:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58078",
    "user": "https://github.com/orlitzky"
}
```

Can you do CFLAGS, too, while you're in there?



---

archive/issue_comments_058079.json:
```json
{
    "body": "Oh, and $MAKE!",
    "created_at": "2012-02-09T17:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58079",
    "user": "https://github.com/orlitzky"
}
```

Oh, and $MAKE!



---

archive/issue_comments_058080.json:
```json
{
    "body": "Ok, updated with $MAKE and $CFLAGS.\n\nThere was a silly patch whose entire purpose was to make the f2c makefile respect global cflags, of course the spkg-install wouldn't respect those cflags :-/. I am now just passing the cflags at the end of the make line in spkg-install, rather than patching the makefile.",
    "created_at": "2012-02-10T09:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58080",
    "user": "https://github.com/ohanar"
}
```

Ok, updated with $MAKE and $CFLAGS.

There was a silly patch whose entire purpose was to make the f2c makefile respect global cflags, of course the spkg-install wouldn't respect those cflags :-/. I am now just passing the cflags at the end of the make line in spkg-install, rather than patching the makefile.



---

archive/issue_comments_058081.json:
```json
{
    "body": "I think there are some left-over files in there:\n\n\n```\nf2c-20070816.p3 $ sage -hg status\n? ._.hg\n? ._.hgignore\n? ._SPKG.txt\n? ._spkg-install\n? patches/._f2c.makefile\n```\n",
    "created_at": "2012-02-11T04:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58081",
    "user": "https://github.com/orlitzky"
}
```

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

archive/issue_comments_058082.json:
```json
{
    "body": "Why do we need both `patches/libf2c.makefile` and `patches/libf2c.makefile.patch`? It looks to me like the patch does the same thing as replacing the upstream makefile with libf2c.makefile:\n\n\n```\n$ diff -u src/libf2c/makefile patches/libf2c.makefile\n--- src/libf2c/makefile\t2007-08-14 21:26:15.000000000 -0400\n+++ patches/libf2c.makefile\t2012-02-10 04:31:00.000000000 -0500\n@@ -70,10 +70,10 @@\n ### If your system lacks ranlib, you don't need it; see README.\n \n f77vers.o: f77vers.c\n-\t$(CC) -c f77vers.c\n+\t$(CC) -c $(CFLAGS) f77vers.c\n \n i77vers.o: i77vers.c\n-\t$(CC) -c i77vers.c\n+\t$(CC) -c $(CFLAGS) i77vers.c\n \n # To get an \"f2c.h\" for use with \"f2c -C++\", first \"make hadd\"\n hadd: f2c.h0 f2ch.add\n```\n\n\n\n```\n$ cat patches/libf2c.makefile.patch \n--- libf2c.makefile.orig\t2009-01-20 00:22:57.000000000 -0800\n+++ libf2c.makefile\t2009-01-20 00:22:25.000000000 -0800\n@@ -70,10 +70,10 @@\n ### If your system lacks ranlib, you don't need it; see README.\n \n f77vers.o: f77vers.c\n-\t$(CC) -c f77vers.c\n+\t$(CC) -c $(CFLAGS) f77vers.c\n \n i77vers.o: i77vers.c\n-\t$(CC) -c i77vers.c\n+\t$(CC) -c $(CFLAGS) i77vers.c\n \n # To get an \"f2c.h\" for use with \"f2c -C++\", first \"make hadd\"\n hadd: f2c.h0 f2ch.add\n```\n\n\nIs there a reason to keep both around and not just the patch?",
    "created_at": "2012-02-11T04:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58082",
    "user": "https://github.com/orlitzky"
}
```

Why do we need both `patches/libf2c.makefile` and `patches/libf2c.makefile.patch`? It looks to me like the patch does the same thing as replacing the upstream makefile with libf2c.makefile:


```
$ diff -u src/libf2c/makefile patches/libf2c.makefile
--- src/libf2c/makefile	2007-08-14 21:26:15.000000000 -0400
+++ patches/libf2c.makefile	2012-02-10 04:31:00.000000000 -0500
@@ -70,10 +70,10 @@
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
@@ -70,10 +70,10 @@
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

archive/issue_comments_058083.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-02-11T04:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58083",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_058084.json:
```json
{
    "body": "Replying to [comment:5 mjo]:\n> I think there are some left-over files in there:\n> \n> {{{\n> f2c-20070816.p3 $ sage -hg status\n> ? ._.hg\n> ? ._.hgignore\n> ? ._SPKG.txt\n> ? ._spkg-install\n> ? patches/._f2c.makefile\n> }}}\n\nFYI, these files were in the previous package, probably from someone working on OSX (it seems to like creating these files).",
    "created_at": "2012-02-11T04:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58084",
    "user": "https://github.com/ohanar"
}
```

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

archive/issue_comments_058085.json:
```json
{
    "body": "Replying to [comment:6 mjo]:\n> Why do we need both `patches/libf2c.makefile` and `patches/libf2c.makefile.patch`? It looks to me like the patch does the same thing as replacing the upstream makefile with libf2c.makefile:\n> \n> {{{\n> $ diff -u src/libf2c/makefile patches/libf2c.makefile\n> --- src/libf2c/makefile\t2007-08-14 21:26:15.000000000 -0400\n> +++ patches/libf2c.makefile\t2012-02-10 04:31:00.000000000 -0500\n> `@``@` -70,10 +70,10 `@``@`\n>  ### If your system lacks ranlib, you don't need it; see README.\n>  \n>  f77vers.o: f77vers.c\n> -\t$(CC) -c f77vers.c\n> +\t$(CC) -c $(CFLAGS) f77vers.c\n>  \n>  i77vers.o: i77vers.c\n> -\t$(CC) -c i77vers.c\n> +\t$(CC) -c $(CFLAGS) i77vers.c\n>  \n>  # To get an \"f2c.h\" for use with \"f2c -C++\", first \"make hadd\"\n>  hadd: f2c.h0 f2ch.add\n> }}}\n> \n> {{{\n> $ cat patches/libf2c.makefile.patch \n> --- libf2c.makefile.orig\t2009-01-20 00:22:57.000000000 -0800\n> +++ libf2c.makefile\t2009-01-20 00:22:25.000000000 -0800\n> `@``@` -70,10 +70,10 `@``@`\n>  ### If your system lacks ranlib, you don't need it; see README.\n>  \n>  f77vers.o: f77vers.c\n> -\t$(CC) -c f77vers.c\n> +\t$(CC) -c $(CFLAGS) f77vers.c\n>  \n>  i77vers.o: i77vers.c\n> -\t$(CC) -c i77vers.c\n> +\t$(CC) -c $(CFLAGS) i77vers.c\n>  \n>  # To get an \"f2c.h\" for use with \"f2c -C++\", first \"make hadd\"\n>  hadd: f2c.h0 f2ch.add\n> }}}\n> \n> Is there a reason to keep both around and not just the patch?\n\nNope, but that wasn't the initial goal of this ticket, that said I've changed the purpose/description.",
    "created_at": "2012-02-11T04:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58085",
    "user": "https://github.com/ohanar"
}
```

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

archive/issue_comments_058086.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-11T05:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58086",
    "user": "https://github.com/ohanar"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_058087.json:
```json
{
    "body": "ok, I've made those changes (plus cleaned up the source directory, which wasn't pristine)",
    "created_at": "2012-02-11T05:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58087",
    "user": "https://github.com/ohanar"
}
```

ok, I've made those changes (plus cleaned up the source directory, which wasn't pristine)



---

archive/issue_comments_058088.json:
```json
{
    "body": "Replying to [comment:9 ohanar]:\n> ok, I've made those changes (plus cleaned up the source directory, which wasn't pristine)\n\nThanks for taking the time to do this, I didn't check the old SPKG for those files.\n\nI've compared the p2 and p3 `src` directories after patching; they look equivalent given the `spkg-install` changes.\n\nTo test the original issue, I've replaced `$CC` and `$CFLAGS` in both makefiles with junk. If I don't set my environment variables, the build crashes. If I export a real `$CC` and `$CFLAGS`, it builds fine.\n\nI built with `MAKE=make -j40` with no problems.",
    "created_at": "2012-02-11T14:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58088",
    "user": "https://github.com/orlitzky"
}
```

Replying to [comment:9 ohanar]:
> ok, I've made those changes (plus cleaned up the source directory, which wasn't pristine)

Thanks for taking the time to do this, I didn't check the old SPKG for those files.

I've compared the p2 and p3 `src` directories after patching; they look equivalent given the `spkg-install` changes.

To test the original issue, I've replaced `$CC` and `$CFLAGS` in both makefiles with junk. If I don't set my environment variables, the build crashes. If I export a real `$CC` and `$CFLAGS`, it builds fine.

I built with `MAKE=make -j40` with no problems.



---

archive/issue_comments_058089.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-11T14:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58089",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058090.json:
```json
{
    "body": "I would have thought it sensible to check the return value of 'patch'. Any changes in the package are could easily stop the patch applying cleanly, if at all, yet that is not tested. \n\nDave",
    "created_at": "2012-02-11T17:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58090",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I would have thought it sensible to check the return value of 'patch'. Any changes in the package are could easily stop the patch applying cleanly, if at all, yet that is not tested. 

Dave



---

archive/issue_comments_058091.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-02-11T17:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58091",
    "user": "https://github.com/ohanar"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_058092.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n> I would have thought it sensible to check the return value of 'patch'. Any changes in the package are could easily stop the patch applying cleanly, if at all, yet that is not tested. \n\nYup, I agree, I've uploaded a new spkg that adds a check.\n> \n> Dave",
    "created_at": "2012-02-11T17:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58092",
    "user": "https://github.com/ohanar"
}
```

Replying to [comment:11 drkirkby]:
> I would have thought it sensible to check the return value of 'patch'. Any changes in the package are could easily stop the patch applying cleanly, if at all, yet that is not tested. 

Yup, I agree, I've uploaded a new spkg that adds a check.
> 
> Dave



---

archive/issue_comments_058093.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-11T17:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58093",
    "user": "https://github.com/ohanar"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_058094.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-02-11T19:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58094",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_058095.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n> I would have thought it sensible to check the return value of 'patch'. Any changes in the package are could easily stop the patch applying cleanly, if at all, yet that is not tested. \n\nIf we want to go this route, we'll have to set the fuzz factor. Otherwise, GNU patch, at least, will happily return success:\n\n\n```\n$ emacs makefile\n$ patch -p0 < ../../patches/libf2c.makefile.patch \npatching file makefile\nHunk #1 succeeded at 73 with fuzz 1 (offset 3 lines).\n$ echo $?\n0\n```\n\n\nUsing `--fuzz=0` should catch that, but will still miss large offsets. I don't know if there's a way to catch those... `patch` is returning success here even for huge offsets:\n\n\n```\n$ patch --fuzz=0 -p0 < ../../patches/libf2c.makefile.patch \npatching file makefile\nHunk #1 succeeded at 111 (offset 41 lines).\n$ echo $?\n0\n```\n\n\nWhoever is upgrading the package would hopefully check for this, but maybe there's a smarter way that I haven't found yet.\n\nAnyway, these are back =)\n\n\n```\n$ sage -hg status\n? ._.hg\n? ._.hgignore\n? ._SPKG.txt\n? ._spkg-install\n? patches/._f2c.makefile\n```\n",
    "created_at": "2012-02-11T19:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58095",
    "user": "https://github.com/orlitzky"
}
```

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

archive/issue_comments_058096.json:
```json
{
    "body": "People updating packages, whilst not taking care of patches, has been a problem several times in Sage. Anything that could be done to reduce that would be good, but maybe it's not possible to do it very well. \n\nDave",
    "created_at": "2012-02-11T19:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58096",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

People updating packages, whilst not taking care of patches, has been a problem several times in Sage. Anything that could be done to reduce that would be good, but maybe it's not possible to do it very well. 

Dave



---

archive/issue_comments_058097.json:
```json
{
    "body": "Attachment [f2c-20070816.p3.patch](tarball://root/attachments/some-uuid/ticket7027/f2c-20070816.p3.patch) by @ohanar created at 2012-02-12 22:31:18\n\nfor review purposes",
    "created_at": "2012-02-12T22:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58097",
    "user": "https://github.com/ohanar"
}
```

Attachment [f2c-20070816.p3.patch](tarball://root/attachments/some-uuid/ticket7027/f2c-20070816.p3.patch) by @ohanar created at 2012-02-12 22:31:18

for review purposes



---

archive/issue_comments_058098.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-12T22:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58098",
    "user": "https://github.com/ohanar"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_058099.json:
```json
{
    "body": "Ok, new version, got rid of the `._` files again (which was my bad, since I restarted off of the p2 package). I've also made some more changes to spkg-install, added some comments, moved some stuff around, made it more uniform, as well as make a libf2c directory in patches, just to make it easy to add patches in the future, if they are ever needed.",
    "created_at": "2012-02-12T22:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58099",
    "user": "https://github.com/ohanar"
}
```

Ok, new version, got rid of the `._` files again (which was my bad, since I restarted off of the p2 package). I've also made some more changes to spkg-install, added some comments, moved some stuff around, made it more uniform, as well as make a libf2c directory in patches, just to make it easy to add patches in the future, if they are ever needed.



---

archive/issue_comments_058100.json:
```json
{
    "body": "This one looks good.\n\nFor future reference, we can probably drop the `-g` (debug) flag, and shouldn't install `libf2c` if building `f2c` fails, but those are minor and unrelated to this ticket.",
    "created_at": "2012-02-23T18:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58100",
    "user": "https://github.com/orlitzky"
}
```

This one looks good.

For future reference, we can probably drop the `-g` (debug) flag, and shouldn't install `libf2c` if building `f2c` fails, but those are minor and unrelated to this ticket.



---

archive/issue_comments_058101.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-23T18:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58101",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058102.json:
```json
{
    "body": "Replying to [comment:17 mjo]:\n> For future reference, we can probably drop the `-g` (debug) flag, \nYeah, I didn't know why we had this, but I didn't want to break anything, so I kept it for safe measure.",
    "created_at": "2012-02-23T18:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58102",
    "user": "https://github.com/ohanar"
}
```

Replying to [comment:17 mjo]:
> For future reference, we can probably drop the `-g` (debug) flag, 
Yeah, I didn't know why we had this, but I didn't want to break anything, so I kept it for safe measure.



---

archive/issue_comments_058103.json:
```json
{
    "body": "Replying to [comment:14 mjo]:\n> but will still miss large offsets. I don't know if there's a way to catch those... `patch` is returning success here even for huge offsets\nThose are pretty innocent and not a big deal in my opinion.  I have never seen a patch applied wrongly because of this.",
    "created_at": "2012-02-23T20:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58103",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:14 mjo]:
> but will still miss large offsets. I don't know if there's a way to catch those... `patch` is returning success here even for huge offsets
Those are pretty innocent and not a big deal in my opinion.  I have never seen a patch applied wrongly because of this.



---

archive/issue_comments_058104.json:
```json
{
    "body": "CC needs quoting:\n\n```\n$MAKE CC=\"$CC\" CFLAGS=\"${CFLAGS}\" \n```\n\n\nAlso, it would be good to mention the ticket number in `SPKG.txt`.\n\n(you can set back positive review yourself after making these trivial changes)",
    "created_at": "2012-02-23T20:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58104",
    "user": "https://github.com/jdemeyer"
}
```

CC needs quoting:

```
$MAKE CC="$CC" CFLAGS="${CFLAGS}" 
```


Also, it would be good to mention the ticket number in `SPKG.txt`.

(you can set back positive review yourself after making these trivial changes)



---

archive/issue_comments_058105.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-02-23T20:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58105",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_058106.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-02-23T20:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58106",
    "user": "https://github.com/ohanar"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_058107.json:
```json
{
    "body": "Replying to [comment:20 jdemeyer]:\n> CC needs quoting:\ndone\n> \n> Also, it would be good to mention the ticket number in `SPKG.txt`.\nand done",
    "created_at": "2012-02-23T20:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58107",
    "user": "https://github.com/ohanar"
}
```

Replying to [comment:20 jdemeyer]:
> CC needs quoting:
done
> 
> Also, it would be good to mention the ticket number in `SPKG.txt`.
and done



---

archive/issue_comments_058108.json:
```json
{
    "body": "I made `spkg-check` executable, as it should be.",
    "created_at": "2012-02-24T15:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58108",
    "user": "https://github.com/jdemeyer"
}
```

I made `spkg-check` executable, as it should be.



---

archive/issue_comments_058109.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-27T11:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7027#issuecomment-58109",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
