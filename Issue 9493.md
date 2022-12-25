# Issue 9493: Remove extra baggage from ECL 10.2.1.p1 (again)

archive/issues_009493.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  drkirkby @kcrisman\n\nSnippet from (my new) `SPKG.txt`:\n\n```\n## Dependencies\n\n * mpir\n * boehm_gc\n\n## Special Update/Build Instructions\n * Delete the src/msvc directory\n * Delete the src/contrib/encodings directory.  So, do not build with\n   --enable-unicode: See http://trac.sagemath.org/sage_trac/ticket/7732\n * TODO: Delete the src/src/gmp directory (13MB!), as we use MPIR\n     - perhaps add --with-gmp-prefix=$SAGE_LOCAL to configure\n       to make sure we use Sage's one (MPIR); this is independent\n       of the deletion of src/src/gmp\n     - needs copying src/src/gmp/install-sh to somewhere else or\n       patching configure to use e.g. that one in src/src/gc\n * TODO: Make ECL use Sage's Boehm GC on MacOS X as well (but perhaps\n   put some changes from ECL's into Sage's Boehm GC), then remove\n   the src/src/gc directory, too\n\n## Changelog\n\n### ecl-10.2.1.p2 (Leif Leonhardy, 13th July 2010)\n  * Removed src/msvc and src/contrib/encodings directories again.\n  * Updated build/update instructions above.\n```\n(See also [this comment](http://trac.sagemath.org/sage_trac/ticket/9187#comment:29) ff. at #9187)\n\nMore worth is removing the GMP source tree, too:\n\n```\n$ ls -l ecl-stripped-v?/*.spkg\n-rw-r--r-- 1 leif64 leif64 3976609 Jul 14 00:42 ecl-stripped-v1/ecl-10.2.1.p2.spkg\n-rw-r--r-- 1 leif64 leif64 2379135 Jul 14 00:02 ecl-stripped-v2/ecl-10.2.1.p2.spkg\n```\n(v2 with in addition GMP removed is less than half the size!)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9493\n\n",
    "created_at": "2010-07-13T23:19:35Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "Remove extra baggage from ECL 10.2.1.p1 (again)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9493",
    "user": "https://github.com/nexttime"
}
```
Assignee: tbd

CC:  drkirkby @kcrisman

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

Issue created by migration from https://trac.sagemath.org/ticket/9493





---

archive/issue_comments_090973.json:
```json
{
    "body": "Minimal patch to `configure` to allow `rm -r src/src/gmp`:\n\n```patch\n--- src/src/configure\t2010-02-13 20:04:32.000000000 +0100\n+++ patches/src.src.configure\t2010-07-14 01:29:39.000000000 +0200\n@@ -1987,7 +1987,7 @@\n \n \n ac_aux_dir=\n-for ac_dir in ${srcdir}/gmp \"$srcdir\"/${srcdir}/gmp; do\n+for ac_dir in ${srcdir}/gmp \"$srcdir\"/${srcdir}/gmp ${srcdir}/gc; do\n   if test -f \"$ac_dir/install-sh\"; then\n     ac_aux_dir=$ac_dir\n     ac_install_sh=\"$ac_aux_dir/install-sh -c\"\n```\n(Tested with 4.5.rc0 on a 32-bit Linux, with `--with-gmp-prefix=$SAGE_LOCAL` added to `./configure` in `spkg-install`, but *should* work as fine without that.)\n\nThough we should in mid-term remove (Boehm) gc as well, because Sage ships with its own copy of it. (ECL's boehm_gc is only used on MacOS X, and just because ECL unconditionally thinks an already installed version there can only be Fink's broken one.) But this is worth another ticket.\n\nAnother simple solution is just leaving `install-sh` in `src/src/gmp` (untested) or just copying it to `${srcdir} ` and adding *that* directory to the `for` list.",
    "created_at": "2010-07-14T00:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90973",
    "user": "https://github.com/nexttime"
}
```

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
(Tested with 4.5.rc0 on a 32-bit Linux, with `--with-gmp-prefix=$SAGE_LOCAL` added to `./configure` in `spkg-install`, but *should* work as fine without that.)

Though we should in mid-term remove (Boehm) gc as well, because Sage ships with its own copy of it. (ECL's boehm_gc is only used on MacOS X, and just because ECL unconditionally thinks an already installed version there can only be Fink's broken one.) But this is worth another ticket.

Another simple solution is just leaving `install-sh` in `src/src/gmp` (untested) or just copying it to `${srcdir} ` and adding *that* directory to the `for` list.



---

archive/issue_comments_090974.json:
```json
{
    "body": "Modified `spkg-install` to allow removal of GMP (suggestion):\n\n```patch\n--- ecl-stripped-v1/ecl-10.2.1.p2/spkg-install\t2010-07-12 05:22:11.000000000 +0200\n+++ ecl-stripped-v2/ecl-10.2.1.p2/spkg-install\t2010-07-14 02:21:22.000000000 +0200\n@@ -154,6 +154,15 @@\n # We clear MAKEFLAGS to fix building multiple spkgs in parallel on OS X.\n export MAKEFLAGS=\n \n+if [ -d patches ] && [ `ls patches` != \"\" ]; then\n+  echo \"Applying patches...\"\n+\n+    test -f patches/src.src.configure && cp -pv patches/src.src.configure src/src/configure\n+\n+  echo \"Finished applying patches.\"\n+  echo \" \"\n+fi\n+\n set +e\n \n cd src\n@@ -165,9 +174,9 @@\n    # 1) OpenSolaris (SunOS 5.11)\n    # 2) Intel or AMD CPU \n    # 3) 64-bit build\n-   ./configure --prefix=$SAGE_LOCAL --with-dffi=no\n+   ./configure --prefix=$SAGE_LOCAL --with-dffi=no --with-gmp-prefix=$SAGE_LOCAL\n else\n-   ./configure --prefix=$SAGE_LOCAL \n+   ./configure --prefix=$SAGE_LOCAL --with-gmp-prefix=$SAGE_LOCAL\n fi\n \n if [ $? -ne 0 ]; then\n```\n(v1's `spkg-install` is unchanged w.r.t. ECL 10.2.1.p1.)",
    "created_at": "2010-07-14T00:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90974",
    "user": "https://github.com/nexttime"
}
```

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

archive/issue_comments_090975.json:
```json
{
    "body": "Get rid of the '-v' option to 'cp'. It's not a POSIX option\n\nhttp://www.opengroup.org/onlinepubs/009695399/utilities/cp.html\n\nand will certainly fail on Solaris or OpenSolaris\n\nDave",
    "created_at": "2010-07-14T01:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90975",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Get rid of the '-v' option to 'cp'. It's not a POSIX option

http://www.opengroup.org/onlinepubs/009695399/utilities/cp.html

and will certainly fail on Solaris or OpenSolaris

Dave



---

archive/issue_comments_090976.json:
```json
{
    "body": "What about\n\n```sh\ncopy-patch()\n{\n  if [ -f patches/$1 ] ; then\n    echo \"  Patching \"$2\n    cp -p patches/$1 $2\n  fi\n}\n```\nand (e.g.)\n\n```sh\nif [ -d patches ] && [ `ls patches` != \"\" ]; then\n  echo \"Applying patches...\" \n\n  copy-patch \"src.src.configure\" \"src/src/configure\"\n\n  echo \"Finished applying patches.\" \n  echo \" \" \nfi      \n```\n?",
    "created_at": "2010-07-14T02:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90976",
    "user": "https://github.com/nexttime"
}
```

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

archive/issue_comments_090977.json:
```json
{
    "body": "I don't think \n\n```\nif [ -d patches ] && [ `ls patches` != \"\" ]; then\n```\n\nis safe. I don't think the order is guaranteed, so the second part could be evaluated before the first. Testing on \"\" is bad practice. \n\nDave",
    "created_at": "2010-10-29T13:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90977",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I don't think 

```
if [ -d patches ] && [ `ls patches` != "" ]; then
```

is safe. I don't think the order is guaranteed, so the second part could be evaluated before the first. Testing on "" is bad practice. 

Dave



---

archive/issue_comments_090978.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n> I don't think \n> \n\n{{{\nif [ -d patches ] && [ `ls patches` != \"\" ]; then\n}}}\n> \n> is safe. I don't think the order is guaranteed, so the second part could be evaluated before the first.\n\n\n(Even if it was, it doesn't make a difference, but...)\n\nLike in C, the second expression is only evaluated if needed (same for `||`), such that\n\n```sh\nfoo && bar || baz\n``` \nis equivalent to\n\n```sh\nif foo; then\n    bar\nelse\n    baz\nfi\n```\n\n\nHowever, the `[ `ls patches` != \"\" ]` is suboptimal. The whole line could be\n\n```sh\nif ls patches/* >/dev/null 2>/dev/null; then\n```\n\n(One could substitute `ls` by e.g. `cat`, too.)  It was just one suggestion anyway.",
    "created_at": "2010-10-29T23:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90978",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:5 drkirkby]:
> I don't think 
> 

{{{
if [ -d patches ] && [ `ls patches` != "" ]; then
}}}
> 
> is safe. I don't think the order is guaranteed, so the second part could be evaluated before the first.


(Even if it was, it doesn't make a difference, but...)

Like in C, the second expression is only evaluated if needed (same for `||`), such that

```sh
foo && bar || baz
``` 
is equivalent to

```sh
if foo; then
    bar
else
    baz
fi
```


However, the `[ `ls patches` != "" ]` is suboptimal. The whole line could be

```sh
if ls patches/* >/dev/null 2>/dev/null; then
```

(One could substitute `ls` by e.g. `cat`, too.)  It was just one suggestion anyway.



---

archive/issue_comments_090979.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n> I don't think the order is guaranteed, so the second part could be evaluated before the first. Testing on \"\" is bad practice. \n\n\nThe order of evaluation and the shortcutting is guaranteed by POSIX:\n\nhttp://www.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_03",
    "created_at": "2010-10-29T23:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90979",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:5 drkirkby]:
> I don't think the order is guaranteed, so the second part could be evaluated before the first. Testing on "" is bad practice. 


The order of evaluation and the shortcutting is guaranteed by POSIX:

http://www.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_03



---

archive/issue_comments_090980.json:
```json
{
    "body": "I believe this should be closed, and if further cleanups are required, a new ticket is opened. \n\nECL will be updated in Sage 4.6.1 to 10.4.1 in #10187. Most of the changes on this ticket are incorporated into #10187 anyway. \n\nDave",
    "created_at": "2010-12-03T00:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90980",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I believe this should be closed, and if further cleanups are required, a new ticket is opened. 

ECL will be updated in Sage 4.6.1 to 10.4.1 in #10187. Most of the changes on this ticket are incorporated into #10187 anyway. 

Dave



---

archive/issue_comments_090981.json:
```json
{
    "body": "Replying to [comment:8 drkirkby]:\n> I believe this should be closed, and if further cleanups are required, a new ticket is opened. \n> \n> ECL will be updated in Sage 4.6.1 to 10.4.1 in #10187. Most of the changes on this ticket are incorporated into #10187 anyway. \n\n\nNothing of the TODOs mentioned in the description have been done on #10187; removing the other parts was just the correction of a regression.\n\nSo IMHO this ticket should be kept open.",
    "created_at": "2010-12-03T00:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90981",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:8 drkirkby]:
> I believe this should be closed, and if further cleanups are required, a new ticket is opened. 
> 
> ECL will be updated in Sage 4.6.1 to 10.4.1 in #10187. Most of the changes on this ticket are incorporated into #10187 anyway. 


Nothing of the TODOs mentioned in the description have been done on #10187; removing the other parts was just the correction of a regression.

So IMHO this ticket should be kept open.



---

archive/issue_comments_090982.json:
```json
{
    "body": "Replying to [comment:1 leif]:\n> Minimal patch to `configure` to allow `rm -r src/src/gmp`:\n> \n> ```\n> #!patch\n> --- src/src/configure\t2010-02-13 20:04:32.000000000 +0100\n> +++ patches/src.src.configure\t2010-07-14 01:29:39.000000000 +0200\n> @@ -1987,7 +1987,7 @@\n>  \n>  \n>  ac_aux_dir=\n> -for ac_dir in ${srcdir}/gmp \"$srcdir\"/${srcdir}/gmp; do\n> +for ac_dir in ${srcdir}/gmp \"$srcdir\"/${srcdir}/gmp ${srcdir}/gc; do\n>    if test -f \"$ac_dir/install-sh\"; then\n>      ac_aux_dir=$ac_dir\n>      ac_install_sh=\"$ac_aux_dir/install-sh -c\"\n> ```\n\n\nNo idea whether that's at all still necessary (when removing the unused GMP source tree) -- we're meanwhile at ECL 12.12.1...\n\n> Another simple solution is just leaving `install-sh` in `src/src/gmp` (untested) or just copying it to `${srcdir} ` and adding *that* directory to the `for` list.",
    "created_at": "2013-06-21T20:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90982",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:1 leif]:
> Minimal patch to `configure` to allow `rm -r src/src/gmp`:
> 
> ```
> #!patch
> --- src/src/configure	2010-02-13 20:04:32.000000000 +0100
> +++ patches/src.src.configure	2010-07-14 01:29:39.000000000 +0200
> @@ -1987,7 +1987,7 @@
>  
>  
>  ac_aux_dir=
> -for ac_dir in ${srcdir}/gmp "$srcdir"/${srcdir}/gmp; do
> +for ac_dir in ${srcdir}/gmp "$srcdir"/${srcdir}/gmp ${srcdir}/gc; do
>    if test -f "$ac_dir/install-sh"; then
>      ac_aux_dir=$ac_dir
>      ac_install_sh="$ac_aux_dir/install-sh -c"
> ```


No idea whether that's at all still necessary (when removing the unused GMP source tree) -- we're meanwhile at ECL 12.12.1...

> Another simple solution is just leaving `install-sh` in `src/src/gmp` (untested) or just copying it to `${srcdir} ` and adding *that* directory to the `for` list.



---

archive/issue_comments_090983.json:
```json
{
    "body": "Ooops, just noticed:\n\n```sh\n$ tar tvjf spkg/standard/ecl-* | grep gmp\ntar: Record size = 8 blocks\ndrwxr-xr-x jdemeyer/jdemeyer      0 2013-04-08 13:05 ecl-12.12.1.p4/src/src/gmp/\n-rwxr-xr-x jdemeyer/jdemeyer   4105 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/config.sub\n-rwxr-xr-x jdemeyer/jdemeyer  31164 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/configfsf.sub\n-rwxr-xr-x jdemeyer/jdemeyer  23041 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/config.guess\n-rwxr-xr-x jdemeyer/jdemeyer   9505 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/install-sh\n-rwxr-xr-x jdemeyer/jdemeyer  43636 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/configfsf.guess\n-rw-r--r-- jdemeyer/jdemeyer  15353 2012-12-07 22:01 ecl-12.12.1.p4/src/src/gmp/config.in\n```\n\nSo there's meanwhile not much of GMP left (in our spkg), but its `config*` files still disturb: #14648\n\nHence the `install-sh` fix above should still be valid (and useful) ...",
    "created_at": "2013-06-21T20:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90983",
    "user": "https://github.com/nexttime"
}
```

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

archive/issue_events_023559.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9493#event-23559"
}
```



---

archive/issue_events_023560.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9493#event-23560"
}
```



---

archive/issue_events_023561.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9493#event-23561"
}
```



---

archive/issue_comments_090984.json:
```json
{
    "body": "Let's get rid of the gmp subdirectory.\n\n---\nNew commits:",
    "created_at": "2014-04-13T19:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90984",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Let's get rid of the gmp subdirectory.

---
New commits:



---

archive/issue_comments_090985.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-04-13T19:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90985",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090986.json:
```json
{
    "body": "Changing keywords from \"\" to \"ecl gmp cygwin spkg\".",
    "created_at": "2014-04-13T19:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90986",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing keywords from "" to "ecl gmp cygwin spkg".



---

archive/issue_comments_090987.json:
```json
{
    "body": "I think the previously rmoved encoding stuff is actually planned to be used, so I did not change its inclusion.",
    "created_at": "2014-04-13T19:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90987",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I think the previously rmoved encoding stuff is actually planned to be used, so I did not change its inclusion.



---

archive/issue_comments_090988.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-14T09:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90988",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090989.json:
```json
{
    "body": "IMHO if we already make our own tarball then we should just regenerate auto-files.",
    "created_at": "2014-04-14T22:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90989",
    "user": "https://github.com/vbraun"
}
```

IMHO if we already make our own tarball then we should just regenerate auto-files.



---

archive/issue_comments_090990.json:
```json
{
    "body": "I'm not sure that will much cleaner as we patch the auto-files as well, so `spkg-src` should first patch then regenerate vs copy two files and then patch...\n\nI don't have strong feeling though.",
    "created_at": "2014-04-15T08:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90990",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I'm not sure that will much cleaner as we patch the auto-files as well, so `spkg-src` should first patch then regenerate vs copy two files and then patch...

I don't have strong feeling though.



---

archive/issue_comments_090991.json:
```json
{
    "body": "Ugh, once again somebody went the extra mile to show that you can't reasonably build shared libraries without libtool. \n\nSince ECL seems to have a maintainer again, did you try to push the `implib.patch` upstream?",
    "created_at": "2014-04-15T10:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90991",
    "user": "https://github.com/vbraun"
}
```

Ugh, once again somebody went the extra mile to show that you can't reasonably build shared libraries without libtool. 

Since ECL seems to have a maintainer again, did you try to push the `implib.patch` upstream?



---

archive/issue_comments_090992.json:
```json
{
    "body": "Yes, see http://sourceforge.net/p/ecls/feature-requests/15/",
    "created_at": "2014-04-15T12:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90992",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Yes, see http://sourceforge.net/p/ecls/feature-requests/15/



---

archive/issue_comments_090993.json:
```json
{
    "body": "Note that the implib patch is not part of this ticket.\nBut for what it's worth note that I used to communicate with the ECL dev and got a bunch of patches into ECL but not that one and now he's no longer maintaining ECL.\nNot sure if anyone is actually actively maintaining ECL anymore...\nOnce there is someone clearly identified we could just bump the request to get that in as at least from my point of view it perfectly makes sense to build shared lib this way on Cygwin.",
    "created_at": "2014-04-15T16:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90993",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Note that the implib patch is not part of this ticket.
But for what it's worth note that I used to communicate with the ECL dev and got a bunch of patches into ECL but not that one and now he's no longer maintaining ECL.
Not sure if anyone is actually actively maintaining ECL anymore...
Once there is someone clearly identified we could just bump the request to get that in as at least from my point of view it perfectly makes sense to build shared lib this way on Cygwin.



---

archive/issue_events_023562.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9493#event-23562"
}
```



---

archive/issue_events_023563.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9493#event-23563"
}
```



---

archive/issue_comments_090994.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-05-15T22:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90994",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090995.json:
```json
{
    "body": "The changes look good to me, and the new version of the package built without problems.  After reinstalling Maxima (I did not use `SAGE_UPGRADING`), all doctests passed.",
    "created_at": "2014-05-15T22:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90995",
    "user": "https://github.com/pjbruin"
}
```

The changes look good to me, and the new version of the package built without problems.  After reinstalling Maxima (I did not use `SAGE_UPGRADING`), all doctests passed.



---

archive/issue_events_023564.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-05-21T15:33:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9493#event-23564"
}
```



---

archive/issue_comments_090996.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-05-21T15:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9493#issuecomment-90996",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
