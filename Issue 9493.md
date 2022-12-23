# Issue 9493: Remove extra baggage from ECL 10.2.1.p1 (again)

Issue created by migration from https://trac.sagemath.org/ticket/9493

Original creator: leif

Original creation time: 2010-07-13 23:19:35

Assignee: tbd

CC:  drkirkby kcrisman

Snippet from (my new) `SPKG.txt`:

```
## Dependencies

 * mpir
 * boehm_gc

## Special Update/Build Instructions
 * Delete the src/msvc directory
 * Delete the src/contrib/encodings directory.  So, do not build with
   --enable-unicode: See http://trac.sagemath.org/sage_trac/ticket/7732
 * TODO: Delete the src/src/gmp directory (13MB!), as we use MPIR
     - perhaps add --with-gmp-prefix=$SAGE_LOCAL to configure
       to make sure we use Sage's one (MPIR); this is independent
       of the deletion of src/src/gmp
     - needs copying src/src/gmp/install-sh to somewhere else or
       patching configure to use e.g. that one in src/src/gc
 * TODO: Make ECL use Sage's Boehm GC on MacOS X as well (but perhaps
   put some changes from ECL's into Sage's Boehm GC), then remove
   the src/src/gc directory, too

## Changelog

### ecl-10.2.1.p2 (Leif Leonhardy, 13th July 2010)
  * Removed src/msvc and src/contrib/encodings directories again.
  * Updated build/update instructions above.
```

(See also [this comment](http://trac.sagemath.org/sage_trac/ticket/9187#comment:29) ff. at #9187)

More worth is removing the GMP source tree, too:

```
$ ls -l ecl-stripped-v?/*.spkg
-rw-r--r-- 1 leif64 leif64 3976609 Jul 14 00:42 ecl-stripped-v1/ecl-10.2.1.p2.spkg
-rw-r--r-- 1 leif64 leif64 2379135 Jul 14 00:02 ecl-stripped-v2/ecl-10.2.1.p2.spkg
```

(v2 with in addition GMP removed is less than half the size!)


---

Comment by leif created at 2010-07-14 00:01:40

Minimal patch to `configure` to allow `rm -r src/src/gmp`:

```patch
--- src/src/configure	2010-02-13 20:04:32.000000000 +0100
+++ patches/src.src.configure	2010-07-14 01:29:39.000000000 +0200
@@ -1987,7 +1987,7 @@
 
 
 ac_aux_dir=
-for ac_dir in ${srcdir}/gmp "$srcdir"/${srcdir}/gmp; do
+for ac_dir in ${srcdir}/gmp "$srcdir"/${srcdir}/gmp ${srcdir}/gc; do
   if test -f "$ac_dir/install-sh"; then
     ac_aux_dir=$ac_dir
     ac_install_sh="$ac_aux_dir/install-sh -c"
```

(Tested with 4.5.rc0 on a 32-bit Linux, with `--with-gmp-prefix=$SAGE_LOCAL` added to `./configure` in `spkg-install`, but _should_ work as fine without that.)

Though we should in mid-term remove (Boehm) gc as well, because Sage ships with its own copy of it. (ECL's boehm_gc is only used on MacOS X, and just because ECL unconditionally thinks an already installed version there can only be Fink's broken one.) But this is worth another ticket.

Another simple solution is just leaving `install-sh` in `src/src/gmp` (untested) or just copying it to `${srcdir} ` and adding _that_ directory to the `for` list.


---

Comment by leif created at 2010-07-14 00:28:38

Modified `spkg-install` to allow removal of GMP (suggestion):

```patch
--- ecl-stripped-v1/ecl-10.2.1.p2/spkg-install	2010-07-12 05:22:11.000000000 +0200
+++ ecl-stripped-v2/ecl-10.2.1.p2/spkg-install	2010-07-14 02:21:22.000000000 +0200
@@ -154,6 +154,15 @@
 # We clear MAKEFLAGS to fix building multiple spkgs in parallel on OS X.
 export MAKEFLAGS=
 
+if [ -d patches ] && [ `ls patches` != "" ]; then
+  echo "Applying patches..."
+
+    test -f patches/src.src.configure && cp -pv patches/src.src.configure src/src/configure
+
+  echo "Finished applying patches."
+  echo " "
+fi
+
 set +e
 
 cd src
@@ -165,9 +174,9 @@
    # 1) OpenSolaris (SunOS 5.11)
    # 2) Intel or AMD CPU 
    # 3) 64-bit build
-   ./configure --prefix=$SAGE_LOCAL --with-dffi=no
+   ./configure --prefix=$SAGE_LOCAL --with-dffi=no --with-gmp-prefix=$SAGE_LOCAL
 else
-   ./configure --prefix=$SAGE_LOCAL 
+   ./configure --prefix=$SAGE_LOCAL --with-gmp-prefix=$SAGE_LOCAL
 fi
 
 if [ $? -ne 0 ]; then
```

(v1's `spkg-install` is unchanged w.r.t. ECL 10.2.1.p1.)


---

Comment by drkirkby created at 2010-07-14 01:17:02

Get rid of the '-v' option to 'cp'. It's not a POSIX option

http://www.opengroup.org/onlinepubs/009695399/utilities/cp.html

and will certainly fail on Solaris or OpenSolaris

Dave


---

Comment by leif created at 2010-07-14 02:09:26

What about

```sh
copy-patch()
{
  if [ -f patches/$1 ] ; then
    echo "  Patching "$2
    cp -p patches/$1 $2
  fi
}
```

and (e.g.)

```sh
if [ -d patches ] && [ `ls patches` != "" ]; then
  echo "Applying patches..." 

  copy-patch "src.src.configure" "src/src/configure"

  echo "Finished applying patches." 
  echo " " 
fi      
```

?


---

Comment by drkirkby created at 2010-10-29 13:52:07

I don't think 


```
if [ -d patches ] && [ `ls patches` != "" ]; then
```


is safe. I don't think the order is guaranteed, so the second part could be evaluated before the first. Testing on "" is bad practice. 

Dave


---

Comment by leif created at 2010-10-29 23:18:06

Replying to [comment:5 drkirkby]:
> I don't think 
> 

```
if [ -d patches ] && [ `ls patches` != "" ]; then
```

> 
> is safe. I don't think the order is guaranteed, so the second part could be evaluated before the first.

(Even if it was, it doesn't make a difference, but...)

Like in C, the second expression is only evaluated if needed (same for `||`), such that


```sh
foo && bar || baz
}}} 
is equivalent to
{{{#!sh
if foo; then
    bar
else
    baz
fi
}}}


However, the `[ `ls patches` != "" ]` is suboptimal. The whole line could be
{{{#!sh
if ls patches/* >/dev/null 2>/dev/null; then
}}}

(One could substitute `ls` by e.g. `cat`, too.)  It was just one suggestion anyway.


---

Comment by nbruin created at 2010-10-29 23:21:15

Replying to [comment:5 drkirkby]:
> I don't think the order is guaranteed, so the second part could be evaluated before the first. Testing on "" is bad practice. 

The order of evaluation and the shortcutting is guaranteed by POSIX:

http://www.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_03


---

Comment by drkirkby created at 2010-12-03 00:29:37

I believe this should be closed, and if further cleanups are required, a new ticket is opened. 

ECL will be updated in Sage 4.6.1 to 10.4.1 in #10187. Most of the changes on this ticket are incorporated into #10187 anyway. 

Dave


---

Comment by leif created at 2010-12-03 00:50:13

Replying to [comment:8 drkirkby]:
> I believe this should be closed, and if further cleanups are required, a new ticket is opened. 
> 
> ECL will be updated in Sage 4.6.1 to 10.4.1 in #10187. Most of the changes on this ticket are incorporated into #10187 anyway. 

Nothing of the TODOs mentioned in the description have been done on #10187; removing the other parts was just the correction of a regression.

So IMHO this ticket should be kept open.


---

Comment by leif created at 2013-06-21 20:02:41

Replying to [comment:1 leif]:
> Minimal patch to `configure` to allow `rm -r src/src/gmp`:
> {{{
> #!patch
> --- src/src/configure	2010-02-13 20:04:32.000000000 +0100
> +++ patches/src.src.configure	2010-07-14 01:29:39.000000000 +0200
> `@``@` -1987,7 +1987,7 `@``@`
>  
>  
>  ac_aux_dir=
> -for ac_dir in ${srcdir}/gmp "$srcdir"/${srcdir}/gmp; do
> +for ac_dir in ${srcdir}/gmp "$srcdir"/${srcdir}/gmp ${srcdir}/gc; do
>    if test -f "$ac_dir/install-sh"; then
>      ac_aux_dir=$ac_dir
>      ac_install_sh="$ac_aux_dir/install-sh -c"
> }}}

No idea whether that's at all still necessary (when removing the unused GMP source tree) -- we're meanwhile at ECL 12.12.1...

> Another simple solution is just leaving `install-sh` in `src/src/gmp` (untested) or just copying it to `${srcdir} ` and adding _that_ directory to the `for` list.


---

Comment by leif created at 2013-06-21 20:18:30

Ooops, just noticed:

```sh
$ tar tvjf spkg/standard/ecl-* | grep gmp
tar: Record size = 8 blocks
drwxr-xr-x jdemeyer/jdemeyer      0 2013-04-08 13:05 ecl-12.12.1.p4/src/src/gmp/
-rwxr-xr-x jdemeyer/jdemeyer   4105 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/config.sub
-rwxr-xr-x jdemeyer/jdemeyer  31164 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/configfsf.sub
-rwxr-xr-x jdemeyer/jdemeyer  23041 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/config.guess
-rwxr-xr-x jdemeyer/jdemeyer   9505 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/install-sh
-rwxr-xr-x jdemeyer/jdemeyer  43636 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/configfsf.guess
-rw-r--r-- jdemeyer/jdemeyer  15353 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/config.in
```


So there's meanwhile not much of GMP left (in our spkg), but its `config*` files still disturb: #14648

Hence the `install-sh` fix above should still be valid (and useful) ...


---

Comment by jpflori created at 2014-04-13 19:27:00

Let's get rid of the gmp subdirectory.
----
New commits:


---

Comment by jpflori created at 2014-04-13 19:27:00

Changing status from new to needs_review.


---

Comment by jpflori created at 2014-04-13 19:27:00

Changing keywords from "" to "ecl gmp cygwin spkg".


---

Comment by jpflori created at 2014-04-13 19:28:55

I think the previously rmoved encoding stuff is actually planned to be used, so I did not change its inclusion.


---

Comment by git created at 2014-04-14 09:47:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vbraun created at 2014-04-14 22:34:37

IMHO if we already make our own tarball then we should just regenerate auto-files.


---

Comment by jpflori created at 2014-04-15 08:47:47

I'm not sure that will much cleaner as we patch the auto-files as well, so `spkg-src` should first patch then regenerate vs copy two files and then patch...

I don't have strong feeling though.


---

Comment by vbraun created at 2014-04-15 10:06:46

Ugh, once again somebody went the extra mile to show that you can't reasonably build shared libraries without libtool. 

Since ECL seems to have a maintainer again, did you try to push the `implib.patch` upstream?


---

Comment by jpflori created at 2014-04-15 12:20:16

Yes, see http://sourceforge.net/p/ecls/feature-requests/15/


---

Comment by jpflori created at 2014-04-15 16:50:35

Note that the implib patch is not part of this ticket.
But for what it's worth note that I used to communicate with the ECL dev and got a bunch of patches into ECL but not that one and now he's no longer maintaining ECL.
Not sure if anyone is actually actively maintaining ECL anymore...
Once there is someone clearly identified we could just bump the request to get that in as at least from my point of view it perfectly makes sense to build shared lib this way on Cygwin.


---

Comment by pbruin created at 2014-05-15 22:28:43

Changing status from needs_review to positive_review.


---

Comment by pbruin created at 2014-05-15 22:28:43

The changes look good to me, and the new version of the package built without problems.  After reinstalling Maxima (I did not use `SAGE_UPGRADING`), all doctests passed.


---

Comment by vbraun created at 2014-05-21 15:33:43

Resolution: fixed
