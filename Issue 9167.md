# Issue 9167: cygwin: importing sage.libs.ecl yields a "no such process" error

archive/issues_009167.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @mwhansen @dimpase jpflori @jdemeyer\n\nThough the C-library interface to ecl builds on cygwin, it does not work at all.  All tests fail:\n\n```\nsage: import sage.libs.ecl\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n\n/home/wstein/sage-4.4.3/<ipython console> in <module>()\n\nImportError: No such process\nsage: \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9167\n\n",
    "created_at": "2010-06-07T04:25:41Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.7",
    "title": "cygwin: importing sage.libs.ecl yields a \"no such process\" error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9167",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @mwhansen @dimpase jpflori @jdemeyer

Though the C-library interface to ecl builds on cygwin, it does not work at all.  All tests fail:

```
sage: import sage.libs.ecl
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/home/wstein/sage-4.4.3/<ipython console> in <module>()

ImportError: No such process
sage: 
```

Issue created by migration from https://trac.sagemath.org/ticket/9167





---

archive/issue_comments_085448.json:
```json
{
    "body": "I don't know if it's related, but gcc reports are couple of rather serious looking warning messages with ecl. \n\n```\n/export/home/drkirkby/sage-4.5.1/spkg/build/ecl-10.2.1.p1/src/src/c/dpp.c:678: warning: too few arguments for format\n/export/home/drkirkby/sage-4.5.1/spkg/build/ecl-10.2.1.p1/src/src/c/dpp.c:680: warning: too many arguments for format\n```\n\nI'm surprised that gcc does not reject such code and refuse to compile it. \n\nDave",
    "created_at": "2010-08-02T04:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85448",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I don't know if it's related, but gcc reports are couple of rather serious looking warning messages with ecl. 

```
/export/home/drkirkby/sage-4.5.1/spkg/build/ecl-10.2.1.p1/src/src/c/dpp.c:678: warning: too few arguments for format
/export/home/drkirkby/sage-4.5.1/spkg/build/ecl-10.2.1.p1/src/src/c/dpp.c:680: warning: too many arguments for format
```

I'm surprised that gcc does not reject such code and refuse to compile it. 

Dave



---

archive/issue_comments_085449.json:
```json
{
    "body": "I can confirm this on the most recent versions of everything at [the port wiki page](CygwinPort).    \n\nThat is bad, because now the default Maxima (and hence ECL) for calculus **is** the library one.",
    "created_at": "2011-08-01T16:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85449",
    "user": "https://github.com/kcrisman"
}
```

I can confirm this on the most recent versions of everything at [the port wiki page](CygwinPort).    

That is bad, because now the default Maxima (and hence ECL) for calculus **is** the library one.



---

archive/issue_comments_085450.json:
```json
{
    "body": "Two possibly irrelevant data points:\n* Tab-completion on `from sage.libs.[tab]` gives `sage.libs.ecl` on Mac, not on Cygwin (it also doesn't give `.libecm` or `.ratpoints`, though at least ratpoints works).\n* The directory `$SAGE_LOCAL/lib/python/site-packages/sage/libs/` DOES include `ecl.pyx` and `ecl.dll`, so the library seems to be there, if that is where such imports actually come from (which I'm not sure about).",
    "created_at": "2011-08-08T14:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85450",
    "user": "https://github.com/kcrisman"
}
```

Two possibly irrelevant data points:
* Tab-completion on `from sage.libs.[tab]` gives `sage.libs.ecl` on Mac, not on Cygwin (it also doesn't give `.libecm` or `.ratpoints`, though at least ratpoints works).
* The directory `$SAGE_LOCAL/lib/python/site-packages/sage/libs/` DOES include `ecl.pyx` and `ecl.dll`, so the library seems to be there, if that is where such imports actually come from (which I'm not sure about).



---

archive/issue_comments_085451.json:
```json
{
    "body": "A possibly useful explanation of something similar from the [Cygwin list](http://www.mail-archive.com/cygwin`@`cygwin.com/msg115538.html):\n\n```\nNow that they are in the cygwin dll, libgfortran doesn't need\n> to provide them anymore but this has the unfortunate side-effect of breaking\n> old executables, since on Windows an imported function reference in an\n> executable has to specify not just the function name but also the particular\n> DLL from which the import comes.\n>\n>  I imagine that on ELF platforms where the executable just has a list of\n> undefined functions and a list of shared libs to load and the dynamic linker\n> just satisfies an undefined symbol from whichever lib it first comes across a\n> definition of it, this probably works without anything needing changing.  But\n> we're stuck I'm afraid when exports move around like this.\n```",
    "created_at": "2011-08-08T15:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85451",
    "user": "https://github.com/kcrisman"
}
```

A possibly useful explanation of something similar from the [Cygwin list](http://www.mail-archive.com/cygwin`@`cygwin.com/msg115538.html):

```
Now that they are in the cygwin dll, libgfortran doesn't need
> to provide them anymore but this has the unfortunate side-effect of breaking
> old executables, since on Windows an imported function reference in an
> executable has to specify not just the function name but also the particular
> DLL from which the import comes.
>
>  I imagine that on ELF platforms where the executable just has a list of
> undefined functions and a list of shared libs to load and the dynamic linker
> just satisfies an undefined symbol from whichever lib it first comes across a
> definition of it, this probably works without anything needing changing.  But
> we're stuck I'm afraid when exports move around like this.
```



---

archive/issue_comments_085452.json:
```json
{
    "body": "[This stackoverflow question](http://stackoverflow.com/questions/2879246/psycopg2-on-cygwin-no-such-process) also might have a useful piece of information.  I don't know how to open/read dlls, though, nor exactly how to trace why it is that it's not finding things.",
    "created_at": "2011-08-08T15:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85452",
    "user": "https://github.com/kcrisman"
}
```

[This stackoverflow question](http://stackoverflow.com/questions/2879246/psycopg2-on-cygwin-no-such-process) also might have a useful piece of information.  I don't know how to open/read dlls, though, nor exactly how to trace why it is that it's not finding things.



---

archive/issue_comments_085453.json:
```json
{
    "body": "[Cygwin's cygcheck information](http://www.cygwin.com/cygwin-ug-net/using-utils.html) was much more helpful, and I find two things.\n* When looking at `$SAGE_LOCAL/libs/ecl.dll`, \n\n```\ncygcheck: track_down:  could not find cyggc-1.dll\n```\n   shows up a lot.   I have `cyggcc_s-1.dll`, `cyggcj-*`, `cyggcr-0.dll` and some others, but not this, in `/bin/`.\n* When looking at `devel/sage/build/lib.cygwin.../sage/libs/ecl.dll`, I find\n\n```\ncygcheck: track_down:  could not find csage.dll\n```\n   This file is in `devel/sage/c_lib` and `local/lib`, but maybe that's not enough?",
    "created_at": "2011-08-08T16:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85453",
    "user": "https://github.com/kcrisman"
}
```

[Cygwin's cygcheck information](http://www.cygwin.com/cygwin-ug-net/using-utils.html) was much more helpful, and I find two things.
* When looking at `$SAGE_LOCAL/libs/ecl.dll`, 

```
cygcheck: track_down:  could not find cyggc-1.dll
```
   shows up a lot.   I have `cyggcc_s-1.dll`, `cyggcj-*`, `cyggcr-0.dll` and some others, but not this, in `/bin/`.
* When looking at `devel/sage/build/lib.cygwin.../sage/libs/ecl.dll`, I find

```
cygcheck: track_down:  could not find csage.dll
```
   This file is in `devel/sage/c_lib` and `local/lib`, but maybe that's not enough?



---

archive/issue_comments_085454.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> [Cygwin's cygcheck information](http://www.cygwin.com/cygwin-ug-net/using-utils.html) was much more helpful, and I find two things.\n> * When looking at `$SAGE_LOCAL/libs/ecl.dll`, \n> \n> ```\n> cygcheck: track_down:  could not find cyggc-1.dll\n> ```\n>    shows up a lot.   I have `cyggcc_s-1.dll`, `cyggcj-*`, `cyggcr-0.dll` and some others, but not this, in `/bin/`.\n\n\nMine, at least, does NOT have `cyggc-1.dll` anywhere.  Apparently it does have libgc (this is a garbage collector) which I've seen connected to `cyggc-1.dll` on [the Cygwin list](http://www.mail-archive.com/cygwin-apps`@`cygwin.com/msg06654.html).  But I don't see how I could have `libgc` without `cyggc-1.dll` if that were the case... I guess the only thing to try is upgrading my libgc and adding libgc-devel, though I'm a little scared!",
    "created_at": "2011-08-08T16:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85454",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:6 kcrisman]:
> [Cygwin's cygcheck information](http://www.cygwin.com/cygwin-ug-net/using-utils.html) was much more helpful, and I find two things.
> * When looking at `$SAGE_LOCAL/libs/ecl.dll`, 
> 
> ```
> cygcheck: track_down:  could not find cyggc-1.dll
> ```
>    shows up a lot.   I have `cyggcc_s-1.dll`, `cyggcj-*`, `cyggcr-0.dll` and some others, but not this, in `/bin/`.


Mine, at least, does NOT have `cyggc-1.dll` anywhere.  Apparently it does have libgc (this is a garbage collector) which I've seen connected to `cyggc-1.dll` on [the Cygwin list](http://www.mail-archive.com/cygwin-apps`@`cygwin.com/msg06654.html).  But I don't see how I could have `libgc` without `cyggc-1.dll` if that were the case... I guess the only thing to try is upgrading my libgc and adding libgc-devel, though I'm a little scared!



---

archive/issue_comments_085455.json:
```json
{
    "body": "I can't even figure out where this is created!  Unless \n\n```\ncygwin* | mingw* | pw32*)\n  version_type=windows\n  need_version=no\n  need_lib_prefix=no\n  case $GCC,$host_os in\n  yes,cygwin*)\n    library_names_spec='$libname.dll.a'\n    soname_spec='`echo ${libname} | sed -e 's/^lib/cyg/'``echo ${release} | sed -e 's/[.]/-/g'`${versuffix}.dll'\n    postinstall_cmds='dlpath=`bash 2>&1 -c '\\''. $dir/${file}i;echo \\$dlname'\\''`~\n      dldir=$destdir/`dirname \\$dlpath`~\n      test -d \\$dldir || mkdir -p \\$dldir~\n      $install_prog .libs/$dlname \\$dldir/$dlname'\n    postuninstall_cmds='dldll=`bash 2>&1 -c '\\''. $file; echo \\$dlname'\\''`~\n      dlpath=$dir/\\$dldll~\n       $rm \\$dlpath'\n```\nand a few similar things in the configure and aclocal files.  I can't quite parse those sed things, though I am pretty sure this wouldn't produce that - but I'm not sure what `${release}` would be in this context.",
    "created_at": "2011-08-08T16:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85455",
    "user": "https://github.com/kcrisman"
}
```

I can't even figure out where this is created!  Unless 

```
cygwin* | mingw* | pw32*)
  version_type=windows
  need_version=no
  need_lib_prefix=no
  case $GCC,$host_os in
  yes,cygwin*)
    library_names_spec='$libname.dll.a'
    soname_spec='`echo ${libname} | sed -e 's/^lib/cyg/'``echo ${release} | sed -e 's/[.]/-/g'`${versuffix}.dll'
    postinstall_cmds='dlpath=`bash 2>&1 -c '\''. $dir/${file}i;echo \$dlname'\''`~
      dldir=$destdir/`dirname \$dlpath`~
      test -d \$dldir || mkdir -p \$dldir~
      $install_prog .libs/$dlname \$dldir/$dlname'
    postuninstall_cmds='dldll=`bash 2>&1 -c '\''. $file; echo \$dlname'\''`~
      dlpath=$dir/\$dldll~
       $rm \$dlpath'
```
and a few similar things in the configure and aclocal files.  I can't quite parse those sed things, though I am pretty sure this wouldn't produce that - but I'm not sure what `${release}` would be in this context.



---

archive/issue_comments_085456.json:
```json
{
    "body": "Replying to [comment:8 kcrisman]:\n>\n\n{{{\n...\n    soname_spec='`echo ${libname} | sed -e 's/^lib/cyg/'``echo ${release} | sed -e 's/[.]/-/g'`${versuffix}.dll'\n...\n}}}\n> and a few similar things in the configure and aclocal files.\n\n\nWhere does this come from? ECL?\n\nThis *might* be the cause of the problem, since the `sed` command also replaces the `lib` prefix by `cyg`.",
    "created_at": "2011-08-08T18:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85456",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:8 kcrisman]:
>

{{{
...
    soname_spec='`echo ${libname} | sed -e 's/^lib/cyg/'``echo ${release} | sed -e 's/[.]/-/g'`${versuffix}.dll'
...
}}}
> and a few similar things in the configure and aclocal files.


Where does this come from? ECL?

This *might* be the cause of the problem, since the `sed` command also replaces the `lib` prefix by `cyg`.



---

archive/issue_comments_085457.json:
```json
{
    "body": "P.S.:\n\nThe `nm` and `objdump` utilities from the GNU `binutils` package might be helpful to inspect libraries etc.\n\nI vaguely remember there was also `dlltool` (perhaps from the MinGW project though).",
    "created_at": "2011-08-08T19:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85457",
    "user": "https://github.com/nexttime"
}
```

P.S.:

The `nm` and `objdump` utilities from the GNU `binutils` package might be helpful to inspect libraries etc.

I vaguely remember there was also `dlltool` (perhaps from the MinGW project though).



---

archive/issue_comments_085458.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n> Replying to [comment:8 kcrisman]:\n> >\n\n> {{{\n> ...\n>     soname_spec='`echo ${libname} | sed -e 's/^lib/cyg/'``echo ${release} | sed -e 's/[.]/-/g'`${versuffix}.dll'\n> ...\n> }}}\n> > and a few similar things in the configure and aclocal files.\n\n> \n> Where does this come from? ECL?\n\n\nNo!  This is from the configure file for libgc-6.4.1 or so - the Boehm GC, ported to Cygwin.  I have libgc, just not cyggc.\n\n> This *might* be the cause of the problem, since the `sed` command also replaces the `lib` prefix by `cyg`.\n\n\nRight, that is why I pointed to it.  But it doesn't seem to replace the `-6.4.1` (or `-7.1.1`, now) with `-1`, as far as I could tell.  And I didn't have anything like `cyggc-*` on it.  \n\nI'm almost done upgrading and adding `libgc-devel` on my Cygwin - which meant upgrading basically every single Cygwin package, because this Cygwin hadn't been changed in a year or more.  Hopefully won't break anything else, but probably will :(\n\nAs to the tools, I think that cygcheck helped a lot, so for now I'm going to stick with that because I actually sort of understand it :)",
    "created_at": "2011-08-08T19:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85458",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:9 leif]:
> Replying to [comment:8 kcrisman]:
> >

> {{{
> ...
>     soname_spec='`echo ${libname} | sed -e 's/^lib/cyg/'``echo ${release} | sed -e 's/[.]/-/g'`${versuffix}.dll'
> ...
> }}}
> > and a few similar things in the configure and aclocal files.

> 
> Where does this come from? ECL?


No!  This is from the configure file for libgc-6.4.1 or so - the Boehm GC, ported to Cygwin.  I have libgc, just not cyggc.

> This *might* be the cause of the problem, since the `sed` command also replaces the `lib` prefix by `cyg`.


Right, that is why I pointed to it.  But it doesn't seem to replace the `-6.4.1` (or `-7.1.1`, now) with `-1`, as far as I could tell.  And I didn't have anything like `cyggc-*` on it.  

I'm almost done upgrading and adding `libgc-devel` on my Cygwin - which meant upgrading basically every single Cygwin package, because this Cygwin hadn't been changed in a year or more.  Hopefully won't break anything else, but probably will :(

As to the tools, I think that cygcheck helped a lot, so for now I'm going to stick with that because I actually sort of understand it :)



---

archive/issue_comments_085459.json:
```json
{
    "body": "> Right, that is why I pointed to it.  But it doesn't seem to replace the `-6.4.1` (or `-7.1.1`, now) with `-1`, as far as I could tell.  And I didn't have anything like `cyggc-*` on it.  \n> \n> I'm almost done upgrading and adding `libgc-devel` on my Cygwin - which meant upgrading basically every single Cygwin package, because this Cygwin hadn't been changed in a year or more.  Hopefully won't break anything else, but probably will :(\n\n\nI think that libgc-devel was what it took to get this file.  However, the upgrade upgraded too much - see [this Cygwin list thread](http://cygwin.com/ml/cygwin/2011-03/msg00750.html) - so I had to downgrade libgfortran as described there, and gcc, and ....  Not for the last time, I have to say that Cygwin definitely is a moving target.",
    "created_at": "2011-08-08T20:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85459",
    "user": "https://github.com/kcrisman"
}
```

> Right, that is why I pointed to it.  But it doesn't seem to replace the `-6.4.1` (or `-7.1.1`, now) with `-1`, as far as I could tell.  And I didn't have anything like `cyggc-*` on it.  
> 
> I'm almost done upgrading and adding `libgc-devel` on my Cygwin - which meant upgrading basically every single Cygwin package, because this Cygwin hadn't been changed in a year or more.  Hopefully won't break anything else, but probably will :(


I think that libgc-devel was what it took to get this file.  However, the upgrade upgraded too much - see [this Cygwin list thread](http://cygwin.com/ml/cygwin/2011-03/msg00750.html) - so I had to downgrade libgfortran as described there, and gcc, and ....  Not for the last time, I have to say that Cygwin definitely is a moving target.



---

archive/issue_comments_085460.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> \n> > Right, that is why I pointed to it.  But it doesn't seem to replace the `-6.4.1` (or `-7.1.1`, now) with `-1`, as far as I could tell.  And I didn't have anything like `cyggc-*` on it.  \n> > \n> > I'm almost done upgrading and adding `libgc-devel` on my Cygwin - which meant upgrading basically every single Cygwin package, because this Cygwin hadn't been changed in a year or more.  Hopefully won't break anything else, but probably will :(\n\n> \n> I think that libgc-devel was what it took to get this file.  However, the upgrade upgraded too much - see [this Cygwin list thread](http://cygwin.com/ml/cygwin/2011-03/msg00750.html) - so I had to downgrade libgfortran as described there, and gcc, and ...\n\n\n...and I managed to toast my Cygwin lapack.  As far as I can tell I downgraded everything necessary to the right version, rebuilt lapack, rebooted, but still no go.  \n\n```\n$ python\n>>> import numpy\nImportError <snip>\n```\nNuts.  Note that fixing this for the Cygwin Python should fix it for Sage, I think, since we use the same Fortran stuff and even lapack (?), certainly BLAS/ATLAS.",
    "created_at": "2011-08-08T21:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85460",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:12 kcrisman]:
> 
> > Right, that is why I pointed to it.  But it doesn't seem to replace the `-6.4.1` (or `-7.1.1`, now) with `-1`, as far as I could tell.  And I didn't have anything like `cyggc-*` on it.  
> > 
> > I'm almost done upgrading and adding `libgc-devel` on my Cygwin - which meant upgrading basically every single Cygwin package, because this Cygwin hadn't been changed in a year or more.  Hopefully won't break anything else, but probably will :(

> 
> I think that libgc-devel was what it took to get this file.  However, the upgrade upgraded too much - see [this Cygwin list thread](http://cygwin.com/ml/cygwin/2011-03/msg00750.html) - so I had to downgrade libgfortran as described there, and gcc, and ...


...and I managed to toast my Cygwin lapack.  As far as I can tell I downgraded everything necessary to the right version, rebuilt lapack, rebooted, but still no go.  

```
$ python
>>> import numpy
ImportError <snip>
```
Nuts.  Note that fixing this for the Cygwin Python should fix it for Sage, I think, since we use the same Fortran stuff and even lapack (?), certainly BLAS/ATLAS.



---

archive/issue_comments_085461.json:
```json
{
    "body": "After a **lot** of trouble managing to get Cygwin shell to find lapack again, I definitely have the right files now.    We definitely need as at least part of the fix to add `libgc-devel` as a dependency.\n\nHowever, there is also still a problem that `cygcheck` finds all the needed dlls for the `ecl.dll` in `local/lib` and `local/bin`, but not for the ones in `devel/sage/build/sage/libs/`.  It cannot find `ecl.dll` or `csage.dll`.  Which seems weird, since those files certainly exist.  \n\nThis might be a `PATH` problem, judging by some similar issues elsewhere.  Unfortunately, `./sage -gdb` is no help here, nor is `./sage -ipython`.",
    "created_at": "2011-08-09T01:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85461",
    "user": "https://github.com/kcrisman"
}
```

After a **lot** of trouble managing to get Cygwin shell to find lapack again, I definitely have the right files now.    We definitely need as at least part of the fix to add `libgc-devel` as a dependency.

However, there is also still a problem that `cygcheck` finds all the needed dlls for the `ecl.dll` in `local/lib` and `local/bin`, but not for the ones in `devel/sage/build/sage/libs/`.  It cannot find `ecl.dll` or `csage.dll`.  Which seems weird, since those files certainly exist.  

This might be a `PATH` problem, judging by some similar issues elsewhere.  Unfortunately, `./sage -gdb` is no help here, nor is `./sage -ipython`.



---

archive/issue_comments_085462.json:
```json
{
    "body": "> However, there is also still a problem that `cygcheck` finds all the needed dlls for the `ecl.dll` in `local/lib` and `local/bin`, but not for the ones in `devel/sage/build/sage/libs/`.  It cannot find `ecl.dll` or `csage.dll`.  Which seems weird, since those files certainly exist.  \n\n\nYeah, after a `./sage -br` it still looks like `csage.dll` is not being found for some reason.  Must be a path issue, I think.  Where do we set the Sage path?  It certainly doesn't include `local/lib`, but I don't know if that's really the problem.",
    "created_at": "2011-08-09T02:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85462",
    "user": "https://github.com/kcrisman"
}
```

> However, there is also still a problem that `cygcheck` finds all the needed dlls for the `ecl.dll` in `local/lib` and `local/bin`, but not for the ones in `devel/sage/build/sage/libs/`.  It cannot find `ecl.dll` or `csage.dll`.  Which seems weird, since those files certainly exist.  


Yeah, after a `./sage -br` it still looks like `csage.dll` is not being found for some reason.  Must be a path issue, I think.  Where do we set the Sage path?  It certainly doesn't include `local/lib`, but I don't know if that's really the problem.



---

archive/issue_comments_085463.json:
```json
{
    "body": "Replying to [comment:15 kcrisman]:\n> > However, there is also still a problem that `cygcheck` finds all the needed dlls for the `ecl.dll` in `local/lib` and `local/bin`, but not for the ones in `devel/sage/build/sage/libs/`.  It cannot find `ecl.dll` or `csage.dll`.  Which seems weird, since those files certainly exist.  \n\n> \n> Yeah, after a `./sage -br` it still looks like `csage.dll` is not being found for some reason.  Must be a path issue, I think.  Where do we set the Sage path?\n\n\nIn `local/bin/sage-env`. You could special-case Cygwin there and add all directories that contain DLLs, as Windows treats them as executables.\n\n> It certainly doesn't include `local/lib`, but I don't know if that's really the problem.\n\n\nWell, before editing `sage-env`, you could just try modifying your `PATH` from the shell accordingly.",
    "created_at": "2011-08-09T03:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85463",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:15 kcrisman]:
> > However, there is also still a problem that `cygcheck` finds all the needed dlls for the `ecl.dll` in `local/lib` and `local/bin`, but not for the ones in `devel/sage/build/sage/libs/`.  It cannot find `ecl.dll` or `csage.dll`.  Which seems weird, since those files certainly exist.  

> 
> Yeah, after a `./sage -br` it still looks like `csage.dll` is not being found for some reason.  Must be a path issue, I think.  Where do we set the Sage path?


In `local/bin/sage-env`. You could special-case Cygwin there and add all directories that contain DLLs, as Windows treats them as executables.

> It certainly doesn't include `local/lib`, but I don't know if that's really the problem.


Well, before editing `sage-env`, you could just try modifying your `PATH` from the shell accordingly.



---

archive/issue_comments_085464.json:
```json
{
    "body": "> > Yeah, after a `./sage -br` it still looks like `csage.dll` is not being found for some reason.  Must be a path issue, I think.  Where do we set the Sage path?\n\n> \n> In `local/bin/sage-env`. You could special-case Cygwin there and add all directories that contain DLLs, as Windows treats them as executables.\n> \n> > It certainly doesn't include `local/lib`, but I don't know if that's really the problem.\n\n\nWell, I have good news and bad news.  \n> Well, before editing `sage-env`, you could just try modifying your `PATH` from the shell accordingly.\n* Good news: editing `PATH` from the shell to include `local/lib` made cygcheck pass for these files.\n* News: `sage-env` includes\n\n```\nif [ \"$UNAME\" = \"CYGWIN\" ]; then\n    PATH=\"$PATH:$SAGE_LOCAL/lib\" && export PATH\nfi\n```\n* Bad news: even with this added to `PATH` *and* this being in the `sage-env`, I still have this problem.  I'm still pretty sure it's a path issue, but maybe they are in the wrong order or something?   I have no idea how complex this could get...",
    "created_at": "2011-08-09T13:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85464",
    "user": "https://github.com/kcrisman"
}
```

> > Yeah, after a `./sage -br` it still looks like `csage.dll` is not being found for some reason.  Must be a path issue, I think.  Where do we set the Sage path?

> 
> In `local/bin/sage-env`. You could special-case Cygwin there and add all directories that contain DLLs, as Windows treats them as executables.
> 
> > It certainly doesn't include `local/lib`, but I don't know if that's really the problem.


Well, I have good news and bad news.  
> Well, before editing `sage-env`, you could just try modifying your `PATH` from the shell accordingly.
* Good news: editing `PATH` from the shell to include `local/lib` made cygcheck pass for these files.
* News: `sage-env` includes

```
if [ "$UNAME" = "CYGWIN" ]; then
    PATH="$PATH:$SAGE_LOCAL/lib" && export PATH
fi
```
* Bad news: even with this added to `PATH` *and* this being in the `sage-env`, I still have this problem.  I'm still pretty sure it's a path issue, but maybe they are in the wrong order or something?   I have no idea how complex this could get...



---

archive/issue_comments_085465.json:
```json
{
    "body": ">  * News: `sage-env` includes\n \n{{{\nif [ \"$UNAME\" = \"CYGWIN\" ]; then\n    PATH=\"$PATH:$SAGE_LOCAL/lib\" && export PATH\nfi\n}}}\n>  * Bad news: even with this added to `PATH` *and* this being in the `sage-env`, I still have this problem.  I'm still pretty sure \n \nFor some reason this is not actually in Sage's path, gotten by `sys.path` in the Sage session.  And adding it to `sys.path` didn't help, either.  What the heck is going on?",
    "created_at": "2011-08-09T15:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85465",
    "user": "https://github.com/kcrisman"
}
```

>  * News: `sage-env` includes
 
{{{
if [ "$UNAME" = "CYGWIN" ]; then
    PATH="$PATH:$SAGE_LOCAL/lib" && export PATH
fi
}}}
>  * Bad news: even with this added to `PATH` *and* this being in the `sage-env`, I still have this problem.  I'm still pretty sure 
 
For some reason this is not actually in Sage's path, gotten by `sys.path` in the Sage session.  And adding it to `sys.path` didn't help, either.  What the heck is going on?



---

archive/issue_comments_085466.json:
```json
{
    "body": "Another possibility, suggested by [this thread](http://old.nabble.com/Re%3A-installing-pygtk-on-cygwin-td19560334.html#a20513293), is that there could be two of some file making things hard.  Interestingly, there are several ecl.dll's floating around (everywhere a libecl.{dylib,so} would live, I guess) and cygcheck gives different dependencies for each.",
    "created_at": "2011-08-09T15:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85466",
    "user": "https://github.com/kcrisman"
}
```

Another possibility, suggested by [this thread](http://old.nabble.com/Re%3A-installing-pygtk-on-cygwin-td19560334.html#a20513293), is that there could be two of some file making things hard.  Interestingly, there are several ecl.dll's floating around (everywhere a libecl.{dylib,so} would live, I guess) and cygcheck gives different dependencies for each.



---

archive/issue_comments_085467.json:
```json
{
    "body": "Replying to [comment:18 kcrisman]:\n> >  * News: `sage-env` includes\n \n{{{#!sh\nif [ \"$UNAME\" = \"CYGWIN\" ]; then\n    PATH=\"$PATH:$SAGE_LOCAL/lib\" && export PATH\nfi\n}}}\n\nYep, but this should IMHO be moved up in the file (including the definition of `UNAME`), in any case above\n\n```sh\nif [ \"$1\" = \"-short\" ]; then\n    return 0\nfi\n```\nand `$SAGE_LOCAL/lib` should be **pre**pended to pick up Sage's versions *first*.\n\n> For some reason this is not actually in Sage's path, gotten by `sys.path` in the Sage session.  And adding it to `sys.path` didn't help, either.  What the heck is going on?\n\n\nNo idea. What does `os.environ.get(\"PATH\")` give?\n\nI also don't know if we have to add some more or different things to `PYTHONPATH` on Cygwin.\n\nNote that e.g. `$SAGE_LOCAL/lib/python` (which is added to `PYTHONPATH` [if it is a directory] in `sage-env`) is a **symbolic link** on Linux etc. (pointing to `$SAGE_LOCAL/lib/python2.6`); I don't know if it is the real directory on Cygwin instead.",
    "created_at": "2011-08-09T17:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85467",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:18 kcrisman]:
> >  * News: `sage-env` includes
 
{{{#!sh
if [ "$UNAME" = "CYGWIN" ]; then
    PATH="$PATH:$SAGE_LOCAL/lib" && export PATH
fi
}}}

Yep, but this should IMHO be moved up in the file (including the definition of `UNAME`), in any case above

```sh
if [ "$1" = "-short" ]; then
    return 0
fi
```
and `$SAGE_LOCAL/lib` should be **pre**pended to pick up Sage's versions *first*.

> For some reason this is not actually in Sage's path, gotten by `sys.path` in the Sage session.  And adding it to `sys.path` didn't help, either.  What the heck is going on?


No idea. What does `os.environ.get("PATH")` give?

I also don't know if we have to add some more or different things to `PYTHONPATH` on Cygwin.

Note that e.g. `$SAGE_LOCAL/lib/python` (which is added to `PYTHONPATH` [if it is a directory] in `sage-env`) is a **symbolic link** on Linux etc. (pointing to `$SAGE_LOCAL/lib/python2.6`); I don't know if it is the real directory on Cygwin instead.



---

archive/issue_comments_085468.json:
```json
{
    "body": "> and `$SAGE_LOCAL/lib` should be **pre**pended to pick up Sage's versions *first*.\n\nThat sounds like a good idea.  But should it be before `$SAGE_ROOT` and `$SAGE_LOCAL/bin`?\n> > For some reason this is not actually in Sage's path, gotten by `sys.path` in the Sage session.  And adding it to `sys.path` didn't help, either.  What the heck is going on?\n\n> \n> No idea. What does `os.environ.get(\"PATH\")` give?\n\nThis gives what I would expect - Sage root, Sage local bin, usr/bin, some Cygwin stuff, a Lapack thing I had to add due to my carelessness, and then Sage local lib.\n> I also don't know if we have to add some more or different things to `PYTHONPATH` on Cygwin.\n\nThis is very sparse.  It is just the directory below.\n> Note that e.g. `$SAGE_LOCAL/lib/python` (which is added to `PYTHONPATH` [if it is a directory] in `sage-env`) is a **symbolic link** on Linux etc. (pointing to `$SAGE_LOCAL/lib/python2.6`); I don't know if it is the real directory on Cygwin instead.\n\nIt looks like it's the same on Cygwin.\n\nAnother interesting thing is that there are libntl.dll files in /local/bin and /local/lib.  Moving just one doesn't seem to do much - note that the bin one is the one imported usually, as in your comment above.  Furthermore, apparently only the ecl.dll in devel/sage/build/sage/libs needs libntl.dll and cyggmp, while the one in local/{bin,lib} just wants cyggmp-3.dll.\n\nAnyway, I guess I can move files around all day but I'm not getting any nearer.",
    "created_at": "2011-08-09T20:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85468",
    "user": "https://github.com/kcrisman"
}
```

> and `$SAGE_LOCAL/lib` should be **pre**pended to pick up Sage's versions *first*.

That sounds like a good idea.  But should it be before `$SAGE_ROOT` and `$SAGE_LOCAL/bin`?
> > For some reason this is not actually in Sage's path, gotten by `sys.path` in the Sage session.  And adding it to `sys.path` didn't help, either.  What the heck is going on?

> 
> No idea. What does `os.environ.get("PATH")` give?

This gives what I would expect - Sage root, Sage local bin, usr/bin, some Cygwin stuff, a Lapack thing I had to add due to my carelessness, and then Sage local lib.
> I also don't know if we have to add some more or different things to `PYTHONPATH` on Cygwin.

This is very sparse.  It is just the directory below.
> Note that e.g. `$SAGE_LOCAL/lib/python` (which is added to `PYTHONPATH` [if it is a directory] in `sage-env`) is a **symbolic link** on Linux etc. (pointing to `$SAGE_LOCAL/lib/python2.6`); I don't know if it is the real directory on Cygwin instead.

It looks like it's the same on Cygwin.

Another interesting thing is that there are libntl.dll files in /local/bin and /local/lib.  Moving just one doesn't seem to do much - note that the bin one is the one imported usually, as in your comment above.  Furthermore, apparently only the ecl.dll in devel/sage/build/sage/libs needs libntl.dll and cyggmp, while the one in local/{bin,lib} just wants cyggmp-3.dll.

Anyway, I guess I can move files around all day but I'm not getting any nearer.



---

archive/issue_comments_085469.json:
```json
{
    "body": "Question for Dima or others; is it possible that we have *too many* copies of the dlls?  Either that the ecl.dll files are in too many places - local/lib and local/bin - or that the extra libntl.dll files also are causing problems?  See #11635 for where this started - perhaps this is the cause of all the trouble?",
    "created_at": "2011-12-07T15:54:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85469",
    "user": "https://github.com/kcrisman"
}
```

Question for Dima or others; is it possible that we have *too many* copies of the dlls?  Either that the ecl.dll files are in too many places - local/lib and local/bin - or that the extra libntl.dll files also are causing problems?  See #11635 for where this started - perhaps this is the cause of all the trouble?



---

archive/issue_comments_085470.json:
```json
{
    "body": "Replying to [comment:22 kcrisman]:\n> Question for Dima or others; is it possible that we have *too many* copies of the dlls?  Either that the ecl.dll files are in too many places - local/lib and local/bin - or that the extra libntl.dll files also are causing problems?  See #11635 for where this started - perhaps this is the cause of all the trouble?  \n\n\n\nfor the record, 2 different copies of ecl.dll in SAGE_ROOT/local/ are created; one in local/lib (and/or local/bin), created from ecl spkg, the other in local/lib/python2.6/site-packages/sage/libs/, which contains Sage/Python interface to ecl (I don't know details about how and when it is built).",
    "created_at": "2011-12-14T02:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85470",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:22 kcrisman]:
> Question for Dima or others; is it possible that we have *too many* copies of the dlls?  Either that the ecl.dll files are in too many places - local/lib and local/bin - or that the extra libntl.dll files also are causing problems?  See #11635 for where this started - perhaps this is the cause of all the trouble?  



for the record, 2 different copies of ecl.dll in SAGE_ROOT/local/ are created; one in local/lib (and/or local/bin), created from ecl spkg, the other in local/lib/python2.6/site-packages/sage/libs/, which contains Sage/Python interface to ecl (I don't know details about how and when it is built).



---

archive/issue_comments_085471.json:
```json
{
    "body": "> for the record, 2 different copies of ecl.dll in SAGE_ROOT/local/ are created; one in local/lib (and/or local/bin), created from ecl spkg, the other in local/lib/python2.6/site-packages/sage/libs/, which contains Sage/Python interface to ecl (I don't know details about how and when it is built).\n\nRight, and the third one is the one which which yields \"No such process\".  \n\nAlthough just by chance I tried (in `./sage -ipython`) \n\n```\nfrom sage.matrix import matrix_integer_dense_hnf\nNameError: ZZ\n```\nfrom the import from `sage.libs.ntl.ntl_ZZ` even though\n\n```\nfrom sage.libs.ntl import *\nntl_ZZ\n```\nworks fine.  Still going to take a while to track all this down, sigh...\n\nWhat do you think about the possibility that it's just a path problem suggested above?  I just don't know enough about how all this works to be sure.",
    "created_at": "2011-12-14T02:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85471",
    "user": "https://github.com/kcrisman"
}
```

> for the record, 2 different copies of ecl.dll in SAGE_ROOT/local/ are created; one in local/lib (and/or local/bin), created from ecl spkg, the other in local/lib/python2.6/site-packages/sage/libs/, which contains Sage/Python interface to ecl (I don't know details about how and when it is built).

Right, and the third one is the one which which yields "No such process".  

Although just by chance I tried (in `./sage -ipython`) 

```
from sage.matrix import matrix_integer_dense_hnf
NameError: ZZ
```
from the import from `sage.libs.ntl.ntl_ZZ` even though

```
from sage.libs.ntl import *
ntl_ZZ
```
works fine.  Still going to take a while to track all this down, sigh...

What do you think about the possibility that it's just a path problem suggested above?  I just don't know enough about how all this works to be sure.



---

archive/issue_comments_085472.json:
```json
{
    "body": "Here's something interesting.\n\n```\nUser 1@GC02635 /home/SageUser/sage-4.7.2\n$ cygcheck local/bin/ecl.dll\nC:\\cygwin\\home\\SageUser\\sage-4.7.2\\local\\bin\\ecl.dll\n  C:\\cygwin\\bin\\cyggc-1.dll\n    C:\\cygwin\\bin\\cygwin1.dll\n      C:\\WINDOWS\\system32\\ADVAPI32.DLL\n        C:\\WINDOWS\\system32\\KERNEL32.dll\n          C:\\WINDOWS\\system32\\ntdll.dll\n        C:\\WINDOWS\\system32\\RPCRT4.dll\n          C:\\WINDOWS\\system32\\Secur32.dll\n    C:\\cygwin\\bin\\cyggcc_s-1.dll\n  C:\\cygwin\\bin\\cyggmp-3.dll\n  C:\\cygwin\\bin\\cygffi-4.dll\n\nUser 1@GC02635 /home/SageUser/sage-4.7.2\n$ cygcheck local/bin/ecl.exe\nC:\\cygwin\\home\\SageUser\\sage-4.7.2\\local\\bin\\ecl.exe\n  C:\\cygwin\\bin\\cygwin1.dll\n    C:\\WINDOWS\\system32\\ADVAPI32.DLL\n      C:\\WINDOWS\\system32\\KERNEL32.dll\n        C:\\WINDOWS\\system32\\ntdll.dll\n      C:\\WINDOWS\\system32\\RPCRT4.dll\n        C:\\WINDOWS\\system32\\Secur32.dll\ncygcheck: track_down: could not find ecl.dll\n\n```\nOr maybe it's boring.  At any rate, I find this weird.\n\nAnd here is the cygcheck for the offending dll.\n\n```\nUser 1@GC02635 /home/SageUser/sage-4.7.2/local/lib/python2.6/site-packages/sage/libs\n$ cygcheck ./ecl.dll\nC:\\cygwin\\home\\SageUser\\sage-4.7.2\\devel\\sage-main\\build\\sage\\libs\\ecl.dll\n  C:\\cygwin\\bin\\cygwin1.dll\n    C:\\WINDOWS\\system32\\ADVAPI32.DLL\n      C:\\WINDOWS\\system32\\KERNEL32.dll\n        C:\\WINDOWS\\system32\\ntdll.dll\n      C:\\WINDOWS\\system32\\RPCRT4.dll\n        C:\\WINDOWS\\system32\\Secur32.dll\n  C:\\cygwin\\home\\SageUser\\sage-4.7.2\\devel\\sage-main\\build\\sage\\libs\\ecl.dll\ncygcheck: track_down: could not find libpython2.6.dll\n\ncygcheck: track_down: could not find libpython2.6.dll\n\ncygcheck: track_down: could not find csage.dll\n\ncygcheck: track_down: could not find csage.dll\n\n```\nThat's a lot of things not to find.",
    "created_at": "2011-12-14T02:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85472",
    "user": "https://github.com/kcrisman"
}
```

Here's something interesting.

```
User 1@GC02635 /home/SageUser/sage-4.7.2
$ cygcheck local/bin/ecl.dll
C:\cygwin\home\SageUser\sage-4.7.2\local\bin\ecl.dll
  C:\cygwin\bin\cyggc-1.dll
    C:\cygwin\bin\cygwin1.dll
      C:\WINDOWS\system32\ADVAPI32.DLL
        C:\WINDOWS\system32\KERNEL32.dll
          C:\WINDOWS\system32\ntdll.dll
        C:\WINDOWS\system32\RPCRT4.dll
          C:\WINDOWS\system32\Secur32.dll
    C:\cygwin\bin\cyggcc_s-1.dll
  C:\cygwin\bin\cyggmp-3.dll
  C:\cygwin\bin\cygffi-4.dll

User 1@GC02635 /home/SageUser/sage-4.7.2
$ cygcheck local/bin/ecl.exe
C:\cygwin\home\SageUser\sage-4.7.2\local\bin\ecl.exe
  C:\cygwin\bin\cygwin1.dll
    C:\WINDOWS\system32\ADVAPI32.DLL
      C:\WINDOWS\system32\KERNEL32.dll
        C:\WINDOWS\system32\ntdll.dll
      C:\WINDOWS\system32\RPCRT4.dll
        C:\WINDOWS\system32\Secur32.dll
cygcheck: track_down: could not find ecl.dll

```
Or maybe it's boring.  At any rate, I find this weird.

And here is the cygcheck for the offending dll.

```
User 1@GC02635 /home/SageUser/sage-4.7.2/local/lib/python2.6/site-packages/sage/libs
$ cygcheck ./ecl.dll
C:\cygwin\home\SageUser\sage-4.7.2\devel\sage-main\build\sage\libs\ecl.dll
  C:\cygwin\bin\cygwin1.dll
    C:\WINDOWS\system32\ADVAPI32.DLL
      C:\WINDOWS\system32\KERNEL32.dll
        C:\WINDOWS\system32\ntdll.dll
      C:\WINDOWS\system32\RPCRT4.dll
        C:\WINDOWS\system32\Secur32.dll
  C:\cygwin\home\SageUser\sage-4.7.2\devel\sage-main\build\sage\libs\ecl.dll
cygcheck: track_down: could not find libpython2.6.dll

cygcheck: track_down: could not find libpython2.6.dll

cygcheck: track_down: could not find csage.dll

cygcheck: track_down: could not find csage.dll

```
That's a lot of things not to find.



---

archive/issue_comments_085473.json:
```json
{
    "body": "Scratch that - in private comm. Dima points out that we should be in the subshell.\n\n```\nSAGE_ROOT=/home/SageUser/sage-4.7.2\n(sage subshell) GC02635:sage-4.7.2 User 1$ cd local/lib/python2.6/site-packages/sage/libs/\nSAGE_ROOT=/home/SageUser/sage-4.7.2\n(sage subshell) GC02635:libs User 1$ cygcheck ./ecl.dll\nC:\\cygwin\\home\\SageUser\\sage-4.7.2\\devel\\sage-main\\build\\sage\\libs\\ecl.dll\n  C:\\cygwin\\home\\SageUser\\sage-4.7.2\\local\\bin\\libpython2.6.dll\n    C:\\cygwin\\bin\\cygwin1.dll\n      C:\\WINDOWS\\system32\\ADVAPI32.DLL\n        C:\\WINDOWS\\system32\\KERNEL32.dll\n          C:\\WINDOWS\\system32\\ntdll.dll\n        C:\\WINDOWS\\system32\\RPCRT4.dll\n          C:\\WINDOWS\\system32\\Secur32.dll\n  C:\\cygwin\\home\\SageUser\\sage-4.7.2\\devel\\sage-main\\build\\sage\\libs\\ecl.dll\n    C:\\cygwin\\home\\SageUser\\sage-4.7.2\\local\\lib\\csage.dll\n      C:\\cygwin\\home\\SageUser\\sage-4.7.2\\local\\bin\\cyggmp-3.dll\n      C:\\cygwin\\bin\\cyggcc_s-1.dll\n      C:\\cygwin\\bin\\cygstdc++-6.dll\n      C:\\cygwin\\home\\SageUser\\sage-4.7.2\\local\\lib\\libntl.dll\nSAGE_ROOT=/home/SageUser/sage-4.7.2\n```\nBut doing it outside its own directory yields the same \"could not find\" message as before.  It only finds it if I'm already in site-packages/sage/.",
    "created_at": "2011-12-14T03:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85473",
    "user": "https://github.com/kcrisman"
}
```

Scratch that - in private comm. Dima points out that we should be in the subshell.

```
SAGE_ROOT=/home/SageUser/sage-4.7.2
(sage subshell) GC02635:sage-4.7.2 User 1$ cd local/lib/python2.6/site-packages/sage/libs/
SAGE_ROOT=/home/SageUser/sage-4.7.2
(sage subshell) GC02635:libs User 1$ cygcheck ./ecl.dll
C:\cygwin\home\SageUser\sage-4.7.2\devel\sage-main\build\sage\libs\ecl.dll
  C:\cygwin\home\SageUser\sage-4.7.2\local\bin\libpython2.6.dll
    C:\cygwin\bin\cygwin1.dll
      C:\WINDOWS\system32\ADVAPI32.DLL
        C:\WINDOWS\system32\KERNEL32.dll
          C:\WINDOWS\system32\ntdll.dll
        C:\WINDOWS\system32\RPCRT4.dll
          C:\WINDOWS\system32\Secur32.dll
  C:\cygwin\home\SageUser\sage-4.7.2\devel\sage-main\build\sage\libs\ecl.dll
    C:\cygwin\home\SageUser\sage-4.7.2\local\lib\csage.dll
      C:\cygwin\home\SageUser\sage-4.7.2\local\bin\cyggmp-3.dll
      C:\cygwin\bin\cyggcc_s-1.dll
      C:\cygwin\bin\cygstdc++-6.dll
      C:\cygwin\home\SageUser\sage-4.7.2\local\lib\libntl.dll
SAGE_ROOT=/home/SageUser/sage-4.7.2
```
But doing it outside its own directory yields the same "could not find" message as before.  It only finds it if I'm already in site-packages/sage/.



---

archive/issue_comments_085474.json:
```json
{
    "body": "Replying to [comment:26 kcrisman]:\n> Scratch that - in private comm. Dima points out that we should be in the subshell.\n\n\nstill, we need to know details of Sage/Python extension implementation on Cygwin to solve this. It could be just an artefact of broken Python/Cython (fork() failures when running sage -b are a pain...)",
    "created_at": "2011-12-14T04:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85474",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:26 kcrisman]:
> Scratch that - in private comm. Dima points out that we should be in the subshell.


still, we need to know details of Sage/Python extension implementation on Cygwin to solve this. It could be just an artefact of broken Python/Cython (fork() failures when running sage -b are a pain...)



---

archive/issue_comments_085475.json:
```json
{
    "body": "Just for info, on my Cygwin 1.7.16/Sage 5.2 install cygchecking all the ecl.* things shows no problem.\nSo the problem looks more subtle...",
    "created_at": "2012-08-05T13:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85475",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Just for info, on my Cygwin 1.7.16/Sage 5.2 install cygchecking all the ecl.* things shows no problem.
So the problem looks more subtle...



---

archive/issue_comments_085476.json:
```json
{
    "body": "I found it quite strange that the problematic ecl.dll links to itself.\nMaybe it's wanting the other ecl.dll, but gets itself because of the name clash.\n\nI'll try to rename ecl.pyx to ecl_blah.pyx, regenerate it and import it to see what happens.",
    "created_at": "2012-08-07T13:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85476",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I found it quite strange that the problematic ecl.dll links to itself.
Maybe it's wanting the other ecl.dll, but gets itself because of the name clash.

I'll try to rename ecl.pyx to ecl_blah.pyx, regenerate it and import it to see what happens.



---

archive/issue_comments_085477.json:
```json
{
    "body": "No problem importing ecl_blah (after removing the former ecl.dll in the same directory sage/libs/)!",
    "created_at": "2012-08-07T13:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85477",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

No problem importing ecl_blah (after removing the former ecl.dll in the same directory sage/libs/)!



---

archive/issue_comments_085478.json:
```json
{
    "body": "And the question is now, why do we get ecl.dll in local/lib/ rather than libecl.dll.",
    "created_at": "2012-08-07T13:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85478",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

And the question is now, why do we get ecl.dll in local/lib/ rather than libecl.dll.



---

archive/issue_comments_085479.json:
```json
{
    "body": "Replying to [comment:32 jpflori]:\n> And the question is now, why do we get ecl.dll in local/lib/ rather than libecl.dll.\n\nthe following [Cygwin doc](http://cygwin.com/cygwin-ug-net/dll.html#dll-build) seems to imply that  `lib` prefix is merely a matter of convenience; it recommends that there should be no `libecl.dll`; it should rather be `cygecl.dll` and `libecl.dll.a`.",
    "created_at": "2012-08-07T14:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85479",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:32 jpflori]:
> And the question is now, why do we get ecl.dll in local/lib/ rather than libecl.dll.

the following [Cygwin doc](http://cygwin.com/cygwin-ug-net/dll.html#dll-build) seems to imply that  `lib` prefix is merely a matter of convenience; it recommends that there should be no `libecl.dll`; it should rather be `cygecl.dll` and `libecl.dll.a`.



---

archive/issue_comments_085480.json:
```json
{
    "body": "Ok, that's because in ecl build system, the shared library is named\n${SHAREDPREFIX}ecl.${SHAREDEXT}\nand these two variables are set to '' and 'dll' by configure on Cygwin.",
    "created_at": "2012-08-07T14:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85480",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Ok, that's because in ecl build system, the shared library is named
${SHAREDPREFIX}ecl.${SHAREDEXT}
and these two variables are set to '' and 'dll' by configure on Cygwin.



---

archive/issue_comments_085481.json:
```json
{
    "body": "Replying to [comment:33 dimpase]:\n> Replying to [comment:32 jpflori]:\n> > And the question is now, why do we get ecl.dll in local/lib/ rather than libecl.dll.\n\n> the following [Cygwin doc](http://cygwin.com/cygwin-ug-net/dll.html#dll-build) seems to imply that  `lib` prefix is merely a matter of convenience; it recommends that there should be no `libecl.dll`; it should rather be `cygecl.dll` and `libecl.dll.a`.\nI agree with you.\nThe question is now if it's trivial enough to modify the build of the shared library on Cygwin.\nUnfortunately, ecl does not use libtool.",
    "created_at": "2012-08-07T14:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85481",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Replying to [comment:33 dimpase]:
> Replying to [comment:32 jpflori]:
> > And the question is now, why do we get ecl.dll in local/lib/ rather than libecl.dll.

> the following [Cygwin doc](http://cygwin.com/cygwin-ug-net/dll.html#dll-build) seems to imply that  `lib` prefix is merely a matter of convenience; it recommends that there should be no `libecl.dll`; it should rather be `cygecl.dll` and `libecl.dll.a`.
I agree with you.
The question is now if it's trivial enough to modify the build of the shared library on Cygwin.
Unfortunately, ecl does not use libtool.



---

archive/issue_comments_085482.json:
```json
{
    "body": "I think the changes could be quite easy, I'll give it a try.",
    "created_at": "2012-08-07T14:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85482",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I think the changes could be quite easy, I'll give it a try.



---

archive/issue_comments_085483.json:
```json
{
    "body": "I based my patch on the two following naming schemes:\nhttp://www.mingw.org/wiki/sampleDLL for MinGW\nand:\nhttp://cygwin.com/cygwin-ug-net/dll.html#dll-build for CYGWIN\nI'll report that upstream.\n\nAs I had to run autoconf which modified a lot of data in config*, the patch included and the hg history will be quite big, so it would be better to update to an upstream release including such modifications (if upstream thinks its a good idea of course).\nUnfortunately, we are quite behind, and I'm not really ready to do both an update and having this fix at the same time.\nAnother solution would be to included a patched src directory in the spkg, but I can already hear people ranting.\nOr directly patch configure in a minimal way, but I'm not so inclined to doing so.",
    "created_at": "2012-08-07T15:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85483",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I based my patch on the two following naming schemes:
http://www.mingw.org/wiki/sampleDLL for MinGW
and:
http://cygwin.com/cygwin-ug-net/dll.html#dll-build for CYGWIN
I'll report that upstream.

As I had to run autoconf which modified a lot of data in config*, the patch included and the hg history will be quite big, so it would be better to update to an upstream release including such modifications (if upstream thinks its a good idea of course).
Unfortunately, we are quite behind, and I'm not really ready to do both an update and having this fix at the same time.
Another solution would be to included a patched src directory in the spkg, but I can already hear people ranting.
Or directly patch configure in a minimal way, but I'm not so inclined to doing so.



---

archive/issue_comments_085484.json:
```json
{
    "body": "Changing keywords from \"\" to \"cygwin spkg ecl\".",
    "created_at": "2012-08-07T16:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85484",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing keywords from "" to "cygwin spkg ecl".



---

archive/issue_comments_085485.json:
```json
{
    "body": "Proposed spkg at http://perso.telecom-paristech.fr/~flori/sage/ecl-11.1.2.cvs20111120.p3.spkg",
    "created_at": "2012-08-07T16:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85485",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Proposed spkg at http://perso.telecom-paristech.fr/~flori/sage/ecl-11.1.2.cvs20111120.p3.spkg



---

archive/issue_comments_085486.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-08-07T16:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85486",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085487.json:
```json
{
    "body": "Replying to [comment:37 jpflori]:\n> As I had to run autoconf which modified a lot of data in config*, the patch included and the hg history will be quite big ...\n\n\nYou may try to use the exact same versions of `automake` and `autoconf`... ;-)\n\n> Another solution would be to included a patched src directory in the spkg, but I can already hear people ranting.\n\n\nWell, I'm personally ok with just \"autoreconfing\" `src/`, but such disturbes the move to git.\n\n> Or directly patch configure in a minimal way, but I'm not so inclined to doing so.\n\n\nIf the patch isn't that large, that's perhaps the best solution until upstream includes a fix.  If they quickly include it into some devel version, we could try to upgrade to that.",
    "created_at": "2012-08-07T17:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85487",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:37 jpflori]:
> As I had to run autoconf which modified a lot of data in config*, the patch included and the hg history will be quite big ...


You may try to use the exact same versions of `automake` and `autoconf`... ;-)

> Another solution would be to included a patched src directory in the spkg, but I can already hear people ranting.


Well, I'm personally ok with just "autoreconfing" `src/`, but such disturbes the move to git.

> Or directly patch configure in a minimal way, but I'm not so inclined to doing so.


If the patch isn't that large, that's perhaps the best solution until upstream includes a fix.  If they quickly include it into some devel version, we could try to upgrade to that.



---

archive/issue_comments_085488.json:
```json
{
    "body": "Replying to [comment:39 leif]:\n> If the patch isn't that large, that's perhaps the best solution until upstream includes a fix.  If they quickly include it into some devel version, we could try to upgrade to that.\n> \n\nI agree with both these ideas, see also https://groups.google.com/d/topic/sage-devel/Ikwfh6PXJnQ/discussion .\n\nThe problem with patching configure directly is that it needs more dirty work and I'm lazy to do it.",
    "created_at": "2012-08-07T17:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85488",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Replying to [comment:39 leif]:
> If the patch isn't that large, that's perhaps the best solution until upstream includes a fix.  If they quickly include it into some devel version, we could try to upgrade to that.
> 

I agree with both these ideas, see also https://groups.google.com/d/topic/sage-devel/Ikwfh6PXJnQ/discussion .

The problem with patching configure directly is that it needs more dirty work and I'm lazy to do it.



---

archive/issue_comments_085489.json:
```json
{
    "body": "And the problem with the upstream solution is that upstream is quite far away from our version and that would also need much more work (if things break, which can be expected).",
    "created_at": "2012-08-07T17:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85489",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

And the problem with the upstream solution is that upstream is quite far away from our version and that would also need much more work (if things break, which can be expected).



---

archive/issue_comments_085490.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-08-08T04:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85490",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085491.json:
```json
{
    "body": "the new spkg installs OK, but gives the following linking error during the build of various Sage dlls:\n \n```\n...\ngcc -I/usr/include/ncurses -fno-strict-aliasing -fwrapv -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/usr/local/src/sage/sage-5.2/local/include/ecl/ -I/usr/local/src/sage/sage-5.2/local/include -I/usr/local/src/sage/sage-5.2/local/include/csage -I/usr/local/src/sage/sage-5.2/devel/sage/sage/ext -I/usr/local/src/sage/sage-5.2/local/include/python2.7 -c sage/libs/ecl.c -o build/temp.cygwin-1.7.16-i686-2.7/sage/libs/ecl.o -w\ngcc -shared -Wl,--enable-auto-image-base -L/usr/local/src/sage/sage-5.2/local/lib build/temp.cygwin-1.7.16-i686-2.7/sage/libs/ecl.o -L/usr/local/src/sage/sage-5.2/local/lib -L/usr/local/src/sage/sage-5.2/local/lib/python2.7/config -lcsage -lecl -lgmp -lstdc++ -lntl -lpython2.7 -o build/lib.cygwin-1.7.16-i686-2.7/sage/libs/ecl.dll\nbuild/temp.cygwin-1.7.16-i686-2.7/sage/libs/ecl.o: In function `__pyx_pf_4sage_4libs_3ecl_4shutdown_ecl':\n/usr/local/src/sage/sage-5.2/devel/sage/sage/libs/ecl.c:3134: undefined reference to `_cl_shutdown'\nbuild/temp.cygwin-1.7.16-i686-2.7/sage/libs/ecl.o: In function `__pyx_pf_4sage_4libs_3ecl_9EclObject_12__hash__':\n/usr/local/src/sage/sage-5.2/devel/sage/sage/libs/ecl.c:4906: undefined reference to `_cl_sxhash'\n.....and lots of siimilar errors...........\n```",
    "created_at": "2012-08-08T04:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85491",
    "user": "https://github.com/dimpase"
}
```

the new spkg installs OK, but gives the following linking error during the build of various Sage dlls:
 
```
...
gcc -I/usr/include/ncurses -fno-strict-aliasing -fwrapv -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/usr/local/src/sage/sage-5.2/local/include/ecl/ -I/usr/local/src/sage/sage-5.2/local/include -I/usr/local/src/sage/sage-5.2/local/include/csage -I/usr/local/src/sage/sage-5.2/devel/sage/sage/ext -I/usr/local/src/sage/sage-5.2/local/include/python2.7 -c sage/libs/ecl.c -o build/temp.cygwin-1.7.16-i686-2.7/sage/libs/ecl.o -w
gcc -shared -Wl,--enable-auto-image-base -L/usr/local/src/sage/sage-5.2/local/lib build/temp.cygwin-1.7.16-i686-2.7/sage/libs/ecl.o -L/usr/local/src/sage/sage-5.2/local/lib -L/usr/local/src/sage/sage-5.2/local/lib/python2.7/config -lcsage -lecl -lgmp -lstdc++ -lntl -lpython2.7 -o build/lib.cygwin-1.7.16-i686-2.7/sage/libs/ecl.dll
build/temp.cygwin-1.7.16-i686-2.7/sage/libs/ecl.o: In function `__pyx_pf_4sage_4libs_3ecl_4shutdown_ecl':
/usr/local/src/sage/sage-5.2/devel/sage/sage/libs/ecl.c:3134: undefined reference to `_cl_shutdown'
build/temp.cygwin-1.7.16-i686-2.7/sage/libs/ecl.o: In function `__pyx_pf_4sage_4libs_3ecl_9EclObject_12__hash__':
/usr/local/src/sage/sage-5.2/devel/sage/sage/libs/ecl.c:4906: undefined reference to `_cl_sxhash'
.....and lots of siimilar errors...........
```



---

archive/issue_comments_085492.json:
```json
{
    "body": "Replying to [comment:43 dimpase]:\n> the new spkg installs OK, but gives the following linking error during the build of various Sage dlls:\n\n\nplease aslo see [Redhat's docs](http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/4/html/Using_ld_the_GNU_Linker/win32.html) for more details on linking on Cygwin. It seems that we might misunderstand the need for and the purpose of `libecl.dll.a`",
    "created_at": "2012-08-08T05:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85492",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:43 dimpase]:
> the new spkg installs OK, but gives the following linking error during the build of various Sage dlls:


please aslo see [Redhat's docs](http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/4/html/Using_ld_the_GNU_Linker/win32.html) for more details on linking on Cygwin. It seems that we might misunderstand the need for and the purpose of `libecl.dll.a`



---

archive/issue_comments_085493.json:
```json
{
    "body": "The purpose of libecl.dll.a is to be able to link to Cygwin dlls from outside of the Cygwin world, with the Windows linker for example.\nSo for Sage on Cygwin, this is not needed.\n\nThe point here was to use a more generic installation for ECL, which would also work for linking from outside Cygwin, and which would as a side effect solves the name clash problem of this ticket.\n\nThe link problem is myabe something with that we do not -L$SAGE_LOCAL/bin when building/linking?\nLibraries generated with libtool do not have this problem because libtool also creates a .la file, which is just a text file containing some info, and in particular where to look for the real shared library file, which is usually in ../cyg<libname>-<version info>.dll",
    "created_at": "2012-08-08T07:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85493",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

The purpose of libecl.dll.a is to be able to link to Cygwin dlls from outside of the Cygwin world, with the Windows linker for example.
So for Sage on Cygwin, this is not needed.

The point here was to use a more generic installation for ECL, which would also work for linking from outside Cygwin, and which would as a side effect solves the name clash problem of this ticket.

The link problem is myabe something with that we do not -L$SAGE_LOCAL/bin when building/linking?
Libraries generated with libtool do not have this problem because libtool also creates a .la file, which is just a text file containing some info, and in particular where to look for the real shared library file, which is usually in ../cyg<libname>-<version info>.dll



---

archive/issue_comments_085494.json:
```json
{
    "body": "What's strange is that copying back bin/cygecl.dll to lib/[lib]ecl.dll does not solve the problem.\nAnd that bin/ecl.exe which links to cygecl.dll works fine.\n\nI may have broken something while tweaking the Makefile...",
    "created_at": "2012-08-08T08:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85494",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

What's strange is that copying back bin/cygecl.dll to lib/[lib]ecl.dll does not solve the problem.
And that bin/ecl.exe which links to cygecl.dll works fine.

I may have broken something while tweaking the Makefile...



---

archive/issue_comments_085495.json:
```json
{
    "body": "Running nm on both libraries from this spkg and the previous one shows the same symbols exactly, but with a different address base.",
    "created_at": "2012-08-08T09:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85495",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Running nm on both libraries from this spkg and the previous one shows the same symbols exactly, but with a different address base.



---

archive/issue_comments_085496.json:
```json
{
    "body": "Replying to [comment:47 jpflori]:\n> Running nm on both libraries from this spkg and the previous one shows the same symbols exactly, but with a different address base.\n\n\nthe culprit is the new libecl.dll.a, which gets picked up by the linker first, what which is not what is needed (as this is for other purposes).\nAnd this makes perfect sense, that's exactly what happens according to the Redhat docs cited above.\n\nI have overcome this by moving libecl.dll.a out of SAGELOCAL/lib, and creating there a symbolic link named cygecl.dll \nto ../bin/cygecl.dll\n\nHopefully will get Sage that can at least start up some time soon...",
    "created_at": "2012-08-08T10:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85496",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:47 jpflori]:
> Running nm on both libraries from this spkg and the previous one shows the same symbols exactly, but with a different address base.


the culprit is the new libecl.dll.a, which gets picked up by the linker first, what which is not what is needed (as this is for other purposes).
And this makes perfect sense, that's exactly what happens according to the Redhat docs cited above.

I have overcome this by moving libecl.dll.a out of SAGELOCAL/lib, and creating there a symbolic link named cygecl.dll 
to ../bin/cygecl.dll

Hopefully will get Sage that can at least start up some time soon...



---

archive/issue_comments_085497.json:
```json
{
    "body": "I don't agree with the point that libecl.dll.a cshould not be picked up by the linker.\nIt is not necessary and you can directly link to cygecl.dll, that I agree with, but it should be possible to go through libecl.dll.a as well.\nOf course, there might be a problem with the produced libecl.dll.a, but using import files should not be impossible.\n\nOr then I don't understand how any piece of Sage can link with MPIR, MPFR and any other library which uses libtool and which generates as well import files and put them into SAGE_LOCAL/lib/ where they get picked up before anything else.\nAnd I don't think we have any piece of code which makes sure these dll.a files are not used.",
    "created_at": "2012-08-08T10:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85497",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I don't agree with the point that libecl.dll.a cshould not be picked up by the linker.
It is not necessary and you can directly link to cygecl.dll, that I agree with, but it should be possible to go through libecl.dll.a as well.
Of course, there might be a problem with the produced libecl.dll.a, but using import files should not be impossible.

Or then I don't understand how any piece of Sage can link with MPIR, MPFR and any other library which uses libtool and which generates as well import files and put them into SAGE_LOCAL/lib/ where they get picked up before anything else.
And I don't think we have any piece of code which makes sure these dll.a files are not used.



---

archive/issue_comments_085498.json:
```json
{
    "body": "Replying to [comment:49 jpflori]:\n> I don't agree with the point that libecl.dll.a cshould not be picked up by the linker.\n> It is not necessary and you can directly link to cygecl.dll, that I agree with, but it should be possible to go through libecl.dll.a as well.\n\n\nRedhat docs recommend direct linking over the import library linking, as more efficient.\nFurther than that, no Idea. I don't have much (positive :-)) experience with Win32 dlls.\n\n> Of course, there might be a problem with the produced libecl.dll.a, \n> \n\n\nthis could well be the case, e.g. `__declspec(dllexport)` declarations missing in the source when compiling.\n(and there are arcane rules about using -export-all-symbols and the above declarations at the same time)\n Or some options to the linker are wrong/missing?\n\n> but using import files should not be impossible.\n> Or then I don't understand how any piece of Sage can link with MPIR, MPFR and any other library which uses libtool and which generates as well import files and put them into SAGE_LOCAL/lib/ where they get picked up before anything else.\n\n\nnote that there are also these .la files produced along the way in the case the libtool is used.\n\n\n> And I don't think we have any piece of code which makes sure these dll.a files are not used.",
    "created_at": "2012-08-08T10:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85498",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:49 jpflori]:
> I don't agree with the point that libecl.dll.a cshould not be picked up by the linker.
> It is not necessary and you can directly link to cygecl.dll, that I agree with, but it should be possible to go through libecl.dll.a as well.


Redhat docs recommend direct linking over the import library linking, as more efficient.
Further than that, no Idea. I don't have much (positive :-)) experience with Win32 dlls.

> Of course, there might be a problem with the produced libecl.dll.a, 
> 


this could well be the case, e.g. `__declspec(dllexport)` declarations missing in the source when compiling.
(and there are arcane rules about using -export-all-symbols and the above declarations at the same time)
 Or some options to the linker are wrong/missing?

> but using import files should not be impossible.
> Or then I don't understand how any piece of Sage can link with MPIR, MPFR and any other library which uses libtool and which generates as well import files and put them into SAGE_LOCAL/lib/ where they get picked up before anything else.


note that there are also these .la files produced along the way in the case the libtool is used.


> And I don't think we have any piece of code which makes sure these dll.a files are not used.



---

archive/issue_comments_085499.json:
```json
{
    "body": "I don't think the .la files are used by ld at all, but I might be wrong.\n\nThe dllexport thing might be the problem, I'll check that.",
    "created_at": "2012-08-08T10:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85499",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I don't think the .la files are used by ld at all, but I might be wrong.

The dllexport thing might be the problem, I'll check that.



---

archive/issue_comments_085500.json:
```json
{
    "body": "The dll.a file is indeed broken.\nRunning nm on it should return much more symbols.\n\nMaybe the dll[import|export] magic is broken.\n\nFor the dllimport this is sure.\nIn config.h, the dllimport maic is turned on if cygwin is defined, whereas gcc on cygwin defines _ _ CYGWIN _ _.\n\nFor the dllexport magic, I'm not sure.\nDuring the build process there is indeed a cygwin variable defined which triggers the use of dllexport (or seems to do).",
    "created_at": "2012-08-08T12:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85500",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

The dll.a file is indeed broken.
Running nm on it should return much more symbols.

Maybe the dll[import|export] magic is broken.

For the dllimport this is sure.
In config.h, the dllimport maic is turned on if cygwin is defined, whereas gcc on cygwin defines _ _ CYGWIN _ _.

For the dllexport magic, I'm not sure.
During the build process there is indeed a cygwin variable defined which triggers the use of dllexport (or seems to do).



---

archive/issue_comments_085501.json:
```json
{
    "body": "And I'm able to generate a correct dll.a file using nm and dlltool.\nSo the linking command which generates the dll.a file must be problematic.",
    "created_at": "2012-08-08T12:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85501",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

And I'm able to generate a correct dll.a file using nm and dlltool.
So the linking command which generates the dll.a file must be problematic.



---

archive/issue_comments_085502.json:
```json
{
    "body": "Ok, think I got it.\n\nI've put the implid stuff into LDFLAGS which are used several times, so libecl.dll.a keeps being regenerated which various stuff in it.",
    "created_at": "2012-08-08T13:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85502",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Ok, think I got it.

I've put the implid stuff into LDFLAGS which are used several times, so libecl.dll.a keeps being regenerated which various stuff in it.



---

archive/issue_comments_085503.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-08T15:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85503",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085504.json:
```json
{
    "body": "The spkg should be fixed now.\n\nNothing is committed yet, but please give it a try!",
    "created_at": "2012-08-08T15:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85504",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

The spkg should be fixed now.

Nothing is committed yet, but please give it a try!



---

archive/issue_comments_085505.json:
```json
{
    "body": "well, I have finished the previous build, but then Sage was refusing to start, throwing the usual fork() problems, even after repeated rebasealls and reboots. I've decided to update Cygwin and uninstall as much as possible of unneeded parts of Cygwin, in hope that it will help. But I am not optimistic.",
    "created_at": "2012-08-08T15:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85505",
    "user": "https://github.com/dimpase"
}
```

well, I have finished the previous build, but then Sage was refusing to start, throwing the usual fork() problems, even after repeated rebasealls and reboots. I've decided to update Cygwin and uninstall as much as possible of unneeded parts of Cygwin, in hope that it will help. But I am not optimistic.



---

archive/issue_comments_085506.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-08-09T08:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85506",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085507.json:
```json
{
    "body": "See discussion at https://groups.google.com/d/topic/sage-devel/Ikwfh6PXJnQ/discussion for autotools regeneration issue.",
    "created_at": "2012-08-09T09:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85507",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

See discussion at https://groups.google.com/d/topic/sage-devel/Ikwfh6PXJnQ/discussion for autotools regeneration issue.



---

archive/issue_comments_085508.json:
```json
{
    "body": "Replying to [comment:56 dimpase]:\n> well, I have finished the previous build, but then Sage was refusing to start, throwing the usual fork() problems, even after repeated rebasealls and reboots. I've decided to update Cygwin and uninstall as much as possible of unneeded parts of Cygwin, in hope that it will help. But I am not optimistic. \n\n\nno, still no luck. I start to suspect that 2GB of RAM are not enough on 32-bit Windows 7 to run Sage. When I examine the location of Sage dlls which produce these fork() failures, I see that \n  their preferred base addresses (set up by rebaseall) have nothing to do with the actual places they are allocated;\n\n  these actual places may be already used by Win32 system dlls.\n\nIt could also be that it's just the 32-bit system is to blame, not the relatively low by modern standards amount of RAM. It's pathetic that on Linux 0.5GB of RAM are enough to have a well-running Sage, while here 2GB are not enough.",
    "created_at": "2012-08-10T04:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85508",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:56 dimpase]:
> well, I have finished the previous build, but then Sage was refusing to start, throwing the usual fork() problems, even after repeated rebasealls and reboots. I've decided to update Cygwin and uninstall as much as possible of unneeded parts of Cygwin, in hope that it will help. But I am not optimistic. 


no, still no luck. I start to suspect that 2GB of RAM are not enough on 32-bit Windows 7 to run Sage. When I examine the location of Sage dlls which produce these fork() failures, I see that 
  their preferred base addresses (set up by rebaseall) have nothing to do with the actual places they are allocated;

  these actual places may be already used by Win32 system dlls.

It could also be that it's just the 32-bit system is to blame, not the relatively low by modern standards amount of RAM. It's pathetic that on Linux 0.5GB of RAM are enough to have a well-running Sage, while here 2GB are not enough.



---

archive/issue_comments_085509.json:
```json
{
    "body": "I've upped an upgraded spkg based on 12.7.1.p0 spkg from #13324 at\nhttp://perso.telecom-paristech.fr/~flori/sage/ecl-12.7.1.p1.spkg\nusing the autotools stuff from #13357.\n\nNothing committed or tagged yet, nor retested on Cygwin.\n\nUpstream is ready to include a similar patch if it does not break anything on any Windows port... which will need some more thorough testing before I can submit such a patch.\nAs far as Sage on Cygwin is concerned, everything seems fine (as much as possible...) so far.",
    "created_at": "2012-08-20T15:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85509",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I've upped an upgraded spkg based on 12.7.1.p0 spkg from #13324 at
http://perso.telecom-paristech.fr/~flori/sage/ecl-12.7.1.p1.spkg
using the autotools stuff from #13357.

Nothing committed or tagged yet, nor retested on Cygwin.

Upstream is ready to include a similar patch if it does not break anything on any Windows port... which will need some more thorough testing before I can submit such a patch.
As far as Sage on Cygwin is concerned, everything seems fine (as much as possible...) so far.



---

archive/issue_comments_085510.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-20T15:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85510",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085511.json:
```json
{
    "body": "I lost part of my changes during the update to 12.7.1...",
    "created_at": "2012-08-20T16:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85511",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I lost part of my changes during the update to 12.7.1...



---

archive/issue_comments_085512.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-08-20T16:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85512",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085513.json:
```json
{
    "body": "Should be fixed now, patched aclocal.m4 is back and patches are correctly tracked.",
    "created_at": "2012-08-20T16:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85513",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Should be fixed now, patched aclocal.m4 is back and patches are correctly tracked.



---

archive/issue_comments_085514.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-20T16:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85514",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085515.json:
```json
{
    "body": "Spkg diff, for review only. Not committed in spkg.",
    "created_at": "2012-08-20T16:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85515",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Spkg diff, for review only. Not committed in spkg.



---

archive/issue_comments_085516.json:
```json
{
    "body": "Attachment [spkg.diff](tarball://root/attachments/some-uuid/ticket9167/spkg.diff) by jpflori created at 2012-10-02 20:15:48",
    "created_at": "2012-10-02T20:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85516",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Attachment [spkg.diff](tarball://root/attachments/some-uuid/ticket9167/spkg.diff) by jpflori created at 2012-10-02 20:15:48



---

archive/issue_comments_085517.json:
```json
{
    "body": "I asked our sysadmins to get me a 64-bit Win7 system (VM), so that I have a chance to get a working Sage on Cygwin. It will take few days to get it up and properly running.",
    "created_at": "2012-10-03T17:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85517",
    "user": "https://github.com/dimpase"
}
```

I asked our sysadmins to get me a 64-bit Win7 system (VM), so that I have a chance to get a working Sage on Cygwin. It will take few days to get it up and properly running.



---

archive/issue_comments_085518.json:
```json
{
    "body": "This works on Cygwin on XP!  Great solution - I was just not quite knowledgeable about this stuff to help, though I spent far too long on it.\n\nI won't have time to look at the spkg itself until Monday, but definitely positive review from actual practice!",
    "created_at": "2012-10-05T16:41:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85518",
    "user": "https://github.com/kcrisman"
}
```

This works on Cygwin on XP!  Great solution - I was just not quite knowledgeable about this stuff to help, though I spent far too long on it.

I won't have time to look at the spkg itself until Monday, but definitely positive review from actual practice!



---

archive/issue_comments_085519.json:
```json
{
    "body": "Thanx for testing this, but anyway I don't think the package here should get merge, let's just wait for upstream to include something similar (which means action from my side, but should happen in a finite amount of time, we first have to deal with other strange things happening with ECL last stable version potentially ignoring signals).\n\nThe spkg here is nonetheless useful to get a somehow more useful build on Cygwin!",
    "created_at": "2012-10-05T23:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85519",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Thanx for testing this, but anyway I don't think the package here should get merge, let's just wait for upstream to include something similar (which means action from my side, but should happen in a finite amount of time, we first have to deal with other strange things happening with ECL last stable version potentially ignoring signals).

The spkg here is nonetheless useful to get a somehow more useful build on Cygwin!



---

archive/issue_comments_085520.json:
```json
{
    "body": "The issue is now discussed upstream at http://sourceforge.net/p/ecls/feature-requests/15/ (after some exchanges on the ecl-devel list).\n\nThe spkg here are outdated (although functional) and should be rebased on top of #13324.\n\nThe bug mentioned reported here:\nhttp://sourceforge.net/p/ecls/bugs/222/\nshould as well be integrated here or at #13324.",
    "created_at": "2012-12-03T22:35:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85520",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

The issue is now discussed upstream at http://sourceforge.net/p/ecls/feature-requests/15/ (after some exchanges on the ecl-devel list).

The spkg here are outdated (although functional) and should be rebased on top of #13324.

The bug mentioned reported here:
http://sourceforge.net/p/ecls/bugs/222/
should as well be integrated here or at #13324.



---

archive/issue_comments_085521.json:
```json
{
    "body": "This is only a little bit off from being based on #13324, cosmetic stuff mostly.",
    "created_at": "2012-12-06T16:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85521",
    "user": "https://github.com/kcrisman"
}
```

This is only a little bit off from being based on #13324, cosmetic stuff mostly.



---

archive/issue_comments_085522.json:
```json
{
    "body": "Not quite ready for prime-time, but [this spkg](http://sage.math.washington.edu/home/kcrisman/ecl-12.7.1.p1.spkg) with the above diff.  This is just naively porting JP's diff.  Somehow I mixed up something, and also there is the problem with the weird tarring... but an attempt, anyway.",
    "created_at": "2012-12-06T16:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85522",
    "user": "https://github.com/kcrisman"
}
```

Not quite ready for prime-time, but [this spkg](http://sage.math.washington.edu/home/kcrisman/ecl-12.7.1.p1.spkg) with the above diff.  This is just naively porting JP's diff.  Somehow I mixed up something, and also there is the problem with the weird tarring... but an attempt, anyway.



---

archive/issue_comments_085523.json:
```json
{
    "body": "For review only - based on JP's spkg",
    "created_at": "2012-12-06T17:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85523",
    "user": "https://github.com/kcrisman"
}
```

For review only - based on JP's spkg



---

archive/issue_comments_085524.json:
```json
{
    "body": "Attachment [spkg-take2.diff](tarball://root/attachments/some-uuid/ticket9167/spkg-take2.diff) by @kcrisman created at 2012-12-06 17:03:11\n\n> Not quite ready for prime-time, but [this spkg](http://sage.math.washington.edu/home/kcrisman/ecl-12.7.1.p1.spkg) with the above diff.  This is just naively porting JP's diff.  Somehow I mixed up something, and also there is the problem with the weird tarring... but an attempt, anyway.\n\n\nOkay, I see what I did wrong.  I still have the weird unknown extended keyword thing while untarring, but at least the patches apply now!  Waiting on the build, hopefully all will be well on Cygwin.",
    "created_at": "2012-12-06T17:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85524",
    "user": "https://github.com/kcrisman"
}
```

Attachment [spkg-take2.diff](tarball://root/attachments/some-uuid/ticket9167/spkg-take2.diff) by @kcrisman created at 2012-12-06 17:03:11

> Not quite ready for prime-time, but [this spkg](http://sage.math.washington.edu/home/kcrisman/ecl-12.7.1.p1.spkg) with the above diff.  This is just naively porting JP's diff.  Somehow I mixed up something, and also there is the problem with the weird tarring... but an attempt, anyway.


Okay, I see what I did wrong.  I still have the weird unknown extended keyword thing while untarring, but at least the patches apply now!  Waiting on the build, hopefully all will be well on Cygwin.



---

archive/issue_comments_085525.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-12-06T17:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85525",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085526.json:
```json
{
    "body": "After rebuilding the Maxima package, I get weird things on Mac.  They pretty much all look like this.\n\n```\nFile \"/Users/.../sage-5.4.rc2/devel/sage-main/sage/functions/piecewise.py\", line 396:\n    sage: f.integral(definite=True)\nException raised:\n<snip>\n        ecl_eval(\"(require 'maxima)\")\n      File \"ecl.pyx\", line 1236, in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:6990)\n      File \"ecl.pyx\", line 1251, in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:6927)\n      File \"ecl.pyx\", line 257, in sage.libs.ecl.ecl_safe_eval (sage/libs/ecl.c:2805)\n    RuntimeError: ECL says: Detected access to an invalid or protected memory address.\n```\nSo definitely not ready.  JP, did I miss something obvious?",
    "created_at": "2012-12-06T17:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85526",
    "user": "https://github.com/kcrisman"
}
```

After rebuilding the Maxima package, I get weird things on Mac.  They pretty much all look like this.

```
File "/Users/.../sage-5.4.rc2/devel/sage-main/sage/functions/piecewise.py", line 396:
    sage: f.integral(definite=True)
Exception raised:
<snip>
        ecl_eval("(require 'maxima)")
      File "ecl.pyx", line 1236, in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:6990)
      File "ecl.pyx", line 1251, in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:6927)
      File "ecl.pyx", line 257, in sage.libs.ecl.ecl_safe_eval (sage/libs/ecl.c:2805)
    RuntimeError: ECL says: Detected access to an invalid or protected memory address.
```
So definitely not ready.  JP, did I miss something obvious?



---

archive/issue_comments_085527.json:
```json
{
    "body": "Eh, and it didn't even work on Cygwin for some reason (that is, same import errors).  I'm going to try JP's again.",
    "created_at": "2012-12-06T17:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85527",
    "user": "https://github.com/kcrisman"
}
```

Eh, and it didn't even work on Cygwin for some reason (that is, same import errors).  I'm going to try JP's again.



---

archive/issue_comments_085528.json:
```json
{
    "body": "> Eh, and it didn't even work on Cygwin for some reason (that is, same import errors).  I'm going to try JP's again.\n\nAnd now I get the same bad behavior (Mac and Cygwin).  I have a feeling that previous ECL stuff isn't properly destroyed when one does `sage -f ecl-x.y.z.spkg`.  But whatever.",
    "created_at": "2012-12-06T18:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85528",
    "user": "https://github.com/kcrisman"
}
```

> Eh, and it didn't even work on Cygwin for some reason (that is, same import errors).  I'm going to try JP's again.

And now I get the same bad behavior (Mac and Cygwin).  I have a feeling that previous ECL stuff isn't properly destroyed when one does `sage -f ecl-x.y.z.spkg`.  But whatever.



---

archive/issue_comments_085529.json:
```json
{
    "body": "That's strange, I guess you've rebuilt Maxima as well.",
    "created_at": "2012-12-10T13:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85529",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

That's strange, I guess you've rebuilt Maxima as well.



---

archive/issue_comments_085530.json:
```json
{
    "body": "> That's strange, I guess you've rebuilt Maxima as well.\nYes.  I think there were just leftover pieces around, I don't know how.  I think it's due to my own bad creation of the spkg.\n\nSo if you can provide an update to this spkg based on #13324, incorporating the same essential changes in the Cygwin-only case - no need to do anything fancy, just the same stuff - I would love to get that in.  The spkg you provided here earlier does still work on Cygwin, just checked a brand-new 5.5.rc0 build.",
    "created_at": "2012-12-10T17:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85530",
    "user": "https://github.com/kcrisman"
}
```

> That's strange, I guess you've rebuilt Maxima as well.
Yes.  I think there were just leftover pieces around, I don't know how.  I think it's due to my own bad creation of the spkg.

So if you can provide an update to this spkg based on #13324, incorporating the same essential changes in the Cygwin-only case - no need to do anything fancy, just the same stuff - I would love to get that in.  The spkg you provided here earlier does still work on Cygwin, just checked a brand-new 5.5.rc0 build.



---

archive/issue_comments_085531.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-12-18T17:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85531",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085532.json:
```json
{
    "body": "New spkg at\nhttp://boxen.math.washington.edu/home/jpflori/ecl-12.12.1.p1.spkg\n\nThe upstream feature request is\nhttp://sourceforge.net/p/ecls/feature-requests/15/",
    "created_at": "2012-12-18T17:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85532",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

New spkg at
http://boxen.math.washington.edu/home/jpflori/ecl-12.12.1.p1.spkg

The upstream feature request is
http://sourceforge.net/p/ecls/feature-requests/15/



---

archive/issue_comments_085533.json:
```json
{
    "body": "Patch to upstream build system.",
    "created_at": "2012-12-18T17:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85533",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Patch to upstream build system.



---

archive/issue_comments_085534.json:
```json
{
    "body": "Attachment [implib.patch](tarball://root/attachments/some-uuid/ticket9167/implib.patch) by jpflori created at 2012-12-18 17:16:23\n\nI guess I should have used a matching version of autoconf to generate a smaller diff.",
    "created_at": "2012-12-18T17:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85534",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Attachment [implib.patch](tarball://root/attachments/some-uuid/ticket9167/implib.patch) by jpflori created at 2012-12-18 17:16:23

I guess I should have used a matching version of autoconf to generate a smaller diff.



---

archive/issue_comments_085535.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-12-18T17:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85535",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085536.json:
```json
{
    "body": "XP report:\n\nI almost forgot to `./sage -b`!  But it **does** fix the problem, based off of the p0 spkg.  Yes!\n\nAnd before rebuilding Maxima I get the usual \"don't know how to require Maxima\" problem, but afterward, with the spkg from #13364, all is well.  Yay!  So all is well as far as I'm concerned.",
    "created_at": "2012-12-18T20:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85536",
    "user": "https://github.com/kcrisman"
}
```

XP report:

I almost forgot to `./sage -b`!  But it **does** fix the problem, based off of the p0 spkg.  Yes!

And before rebuilding Maxima I get the usual "don't know how to require Maxima" problem, but afterward, with the spkg from #13364, all is well.  Yay!  So all is well as far as I'm concerned.



---

archive/issue_comments_085537.json:
```json
{
    "body": "By the way, could this be upgraded irrespective of upgrading Maxima?  (I mean for Sage proper.)  If all we need is to change the location of the Maxima library, maybe we could avoid having to track down the doctest issues in #13364 right now, by providing a minimal Maxima spkg change here.",
    "created_at": "2012-12-19T14:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85537",
    "user": "https://github.com/kcrisman"
}
```

By the way, could this be upgraded irrespective of upgrading Maxima?  (I mean for Sage proper.)  If all we need is to change the location of the Maxima library, maybe we could avoid having to track down the doctest issues in #13364 right now, by providing a minimal Maxima spkg change here.



---

archive/issue_comments_085538.json:
```json
{
    "body": "Replying to [comment:80 kcrisman]:\n> By the way, could this be upgraded irrespective of upgrading Maxima?  (I mean for Sage proper.)  If all we need is to change the location of the Maxima library, maybe we could avoid having to track down the doctest issues in #13364 right now, by providing a minimal Maxima spkg change here.\n\n\nTo ease things, I'd then not hard-code the (new) name, but test whether `maxima.system.fasb` is present, and if so, copy that, otherwise (try to) copy `maxima.fasb`, or bail out if none of these is present.\n\n(Something we should probably do at #13364 as well.)",
    "created_at": "2012-12-19T15:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85538",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:80 kcrisman]:
> By the way, could this be upgraded irrespective of upgrading Maxima?  (I mean for Sage proper.)  If all we need is to change the location of the Maxima library, maybe we could avoid having to track down the doctest issues in #13364 right now, by providing a minimal Maxima spkg change here.


To ease things, I'd then not hard-code the (new) name, but test whether `maxima.system.fasb` is present, and if so, copy that, otherwise (try to) copy `maxima.fasb`, or bail out if none of these is present.

(Something we should probably do at #13364 as well.)



---

archive/issue_comments_085539.json:
```json
{
    "body": "Replying to [comment:81 leif]:\n> Replying to [comment:80 kcrisman]:\n> > By the way, could this be upgraded irrespective of upgrading Maxima?  (I mean for Sage proper.)  If all we need is to change the location of the Maxima library, maybe we could avoid having to track down the doctest issues in #13364 right now, by providing a minimal Maxima spkg change here.\n\n\nindeed, this can and should be done.\n\n> \n> To ease things, I'd then not hard-code the (new) name, but test whether `maxima.system.fasb` is present, and if so, copy that, otherwise (try to) copy `maxima.fasb`, or bail out if none of these is present.\n\n\ngood idea!\n\n> \n> (Something we should probably do at #13364 as well.)\n\n>",
    "created_at": "2012-12-19T16:33:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85539",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:81 leif]:
> Replying to [comment:80 kcrisman]:
> > By the way, could this be upgraded irrespective of upgrading Maxima?  (I mean for Sage proper.)  If all we need is to change the location of the Maxima library, maybe we could avoid having to track down the doctest issues in #13364 right now, by providing a minimal Maxima spkg change here.


indeed, this can and should be done.

> 
> To ease things, I'd then not hard-code the (new) name, but test whether `maxima.system.fasb` is present, and if so, copy that, otherwise (try to) copy `maxima.fasb`, or bail out if none of these is present.


good idea!

> 
> (Something we should probably do at #13364 as well.)

>



---

archive/issue_comments_085540.json:
```json
{
    "body": "Feel free to do so in another ticket, change dependencies here, update #13364 to be based on this new ticket, and remove dependency on this ECL ticket form #13364.",
    "created_at": "2012-12-19T16:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85540",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Feel free to do so in another ticket, change dependencies here, update #13364 to be based on this new ticket, and remove dependency on this ECL ticket form #13364.



---

archive/issue_comments_085541.json:
```json
{
    "body": "Replying to [comment:83 jpflori]:\n> Feel free to do so in another ticket, change dependencies here, update #13364 to be based on this new ticket, and remove dependency on this ECL ticket form #13364.\n\n\nI'd rather see this ticket brought to completion. I imagine it's just a small autoconf fix, right?\nI'm adding to the ticket description a link to updated maxima 5.26 spkg.\n\nCan one close #13324 as a duplicate?",
    "created_at": "2012-12-19T17:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85541",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:83 jpflori]:
> Feel free to do so in another ticket, change dependencies here, update #13364 to be based on this new ticket, and remove dependency on this ECL ticket form #13364.


I'd rather see this ticket brought to completion. I imagine it's just a small autoconf fix, right?
I'm adding to the ticket description a link to updated maxima 5.26 spkg.

Can one close #13324 as a duplicate?



---

archive/issue_comments_085542.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-12-19T17:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85542",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085543.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2012-12-19T17:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85543",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_085544.json:
```json
{
    "body": "I think that #13324 still needs_review and potential firther changes (no feedback from upstream yet on the uncaught segfault issue).\n\nClosing #13324 would be similar to what I wanted to do for #12115 and #13137 except for the fact that #12115 was kind of trivial and got merged into #13137, whereas here we would merge a big (almost functional?) ticket into a simpler (but potentially more controversial) one.\n\nFurthermore, as this one is only needed on Cygwin, I'm even more inclined to think it might be better to wait for #13324 to be properly merged, and then go with this one.\nIf you really want to use it, just download it and do so.\n\nAnd I still think the change to Maxima spkg-install script should be done in an independent (and quite trivial) ticket called something like \"let Maxima spkg properly install with different version of ECL\", it would be merged really quicly, and then rebase #13364 to update Maxima on top of that new ticket.\n\nWith this approach people could just drop in different versions of ECl and ply with them.\n\nGenerally I feel that keeping issues, or even \"independent\" changes, into separated tickets is a good idea.",
    "created_at": "2012-12-19T17:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85544",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I think that #13324 still needs_review and potential firther changes (no feedback from upstream yet on the uncaught segfault issue).

Closing #13324 would be similar to what I wanted to do for #12115 and #13137 except for the fact that #12115 was kind of trivial and got merged into #13137, whereas here we would merge a big (almost functional?) ticket into a simpler (but potentially more controversial) one.

Furthermore, as this one is only needed on Cygwin, I'm even more inclined to think it might be better to wait for #13324 to be properly merged, and then go with this one.
If you really want to use it, just download it and do so.

And I still think the change to Maxima spkg-install script should be done in an independent (and quite trivial) ticket called something like "let Maxima spkg properly install with different version of ECL", it would be merged really quicly, and then rebase #13364 to update Maxima on top of that new ticket.

With this approach people could just drop in different versions of ECl and ply with them.

Generally I feel that keeping issues, or even "independent" changes, into separated tickets is a good idea.



---

archive/issue_comments_085545.json:
```json
{
    "body": "Yeah, and Jeroen ranted when I asked to close #12115 and merge it within #13137 and I understand his point :)",
    "created_at": "2012-12-19T17:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85545",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Yeah, and Jeroen ranted when I asked to close #12115 and merge it within #13137 and I understand his point :)



---

archive/issue_comments_085546.json:
```json
{
    "body": "Replying to [comment:86 jpflori]:\n> I think that #13324 still needs_review and potential firther changes (no feedback from upstream yet on the uncaught segfault issue).\n> \n> Closing #13324 would be similar to what I wanted to do for #12115 and #13137 except for the fact that #12115 was kind of trivial and got merged into #13137, whereas here we would merge a big (almost functional?) ticket into a simpler (but potentially more controversial) one.\n\n\n#13324 is partially duplicating #13364. The segfault one sees with Maxima is due to an infinite recursion in some Maxima code, as\nis acknowledged on [maxima bug tracker, bug 2520](https://sourceforge.net/p/maxima/bugs/2520/). I am not sure ECL can be blamed for crashing on this.",
    "created_at": "2012-12-19T17:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85546",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:86 jpflori]:
> I think that #13324 still needs_review and potential firther changes (no feedback from upstream yet on the uncaught segfault issue).
> 
> Closing #13324 would be similar to what I wanted to do for #12115 and #13137 except for the fact that #12115 was kind of trivial and got merged into #13137, whereas here we would merge a big (almost functional?) ticket into a simpler (but potentially more controversial) one.


#13324 is partially duplicating #13364. The segfault one sees with Maxima is due to an infinite recursion in some Maxima code, as
is acknowledged on [maxima bug tracker, bug 2520](https://sourceforge.net/p/maxima/bugs/2520/). I am not sure ECL can be blamed for crashing on this.



---

archive/issue_comments_085547.json:
```json
{
    "body": "As was demonstrated, other Lisp interpreters catch the error more gracefully.\nI must say I don't really care, especially that when Maxima is fixed, there should be nothing to catch anymore, but if a fix is possible and is devised, we could include it in #13324 or a further ECL update where it belongs.",
    "created_at": "2012-12-19T18:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85547",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

As was demonstrated, other Lisp interpreters catch the error more gracefully.
I must say I don't really care, especially that when Maxima is fixed, there should be nothing to catch anymore, but if a fix is possible and is devised, we could include it in #13324 or a further ECL update where it belongs.



---

archive/issue_comments_085548.json:
```json
{
    "body": "Replying to [comment:86 jpflori]:\n> And I still think the change to Maxima spkg-install script should be done in an independent (and quite trivial) ticket called something like \"let Maxima spkg properly install with different version of ECL\", it would be merged really quicly, and then rebase #13364 to update Maxima on top of that new ticket.\n\n\nYep, that's what I was thinking of as well.  (Unless the Maxima guys [and probably we, too] are super-quick and fix all issues within the next few days...)\n\n\n> With this approach people could just drop in different versions of ECl and ply with them.\n\n\nAlthough I occasionally hear the contrary (e.g. \"Why let LCalc build with different versions of PARI?\"), we shouldn't establish unnecessary dependencies, so yes.\n\n\n\n\n> Generally I feel that keeping issues, or even \"independent\" changes, into separated tickets is a good idea.\n\n\n*Generally.*  Unfortunately often N developers touch the \"same\" code (or spkgs) such that at least N-1 developers have to rebase their changes M<sub>N</sub> times, or the fixes just rotten and never get merged.",
    "created_at": "2012-12-19T20:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85548",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:86 jpflori]:
> And I still think the change to Maxima spkg-install script should be done in an independent (and quite trivial) ticket called something like "let Maxima spkg properly install with different version of ECL", it would be merged really quicly, and then rebase #13364 to update Maxima on top of that new ticket.


Yep, that's what I was thinking of as well.  (Unless the Maxima guys [and probably we, too] are super-quick and fix all issues within the next few days...)


> With this approach people could just drop in different versions of ECl and ply with them.


Although I occasionally hear the contrary (e.g. "Why let LCalc build with different versions of PARI?"), we shouldn't establish unnecessary dependencies, so yes.




> Generally I feel that keeping issues, or even "independent" changes, into separated tickets is a good idea.


*Generally.*  Unfortunately often N developers touch the "same" code (or spkgs) such that at least N-1 developers have to rebase their changes M<sub>N</sub> times, or the fixes just rotten and never get merged.



---

archive/issue_comments_085549.json:
```json
{
    "body": "Replying to [comment:81 leif]:\n> Replying to [comment:80 kcrisman]:\n> > By the way, could this be upgraded irrespective of upgrading Maxima?  (I mean for Sage proper.)  If all we need is to change the location of the Maxima library, maybe we could avoid having to track down the doctest issues in #13364 right now, by providing a minimal Maxima spkg change here.\n\n> \n> To ease things, I'd then not hard-code the (new) name, but test whether `maxima.system.fasb` is present, and if so, copy that, otherwise (try to) copy `maxima.fasb`, or bail out if none of these is present.\n\n\nOK, this is now #13860\n\nPlease review!",
    "created_at": "2012-12-23T08:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85549",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:81 leif]:
> Replying to [comment:80 kcrisman]:
> > By the way, could this be upgraded irrespective of upgrading Maxima?  (I mean for Sage proper.)  If all we need is to change the location of the Maxima library, maybe we could avoid having to track down the doctest issues in #13364 right now, by providing a minimal Maxima spkg change here.

> 
> To ease things, I'd then not hard-code the (new) name, but test whether `maxima.system.fasb` is present, and if so, copy that, otherwise (try to) copy `maxima.fasb`, or bail out if none of these is present.


OK, this is now #13860

Please review!



---

archive/issue_comments_085550.json:
```json
{
    "body": "> OK, this is now #13860\n> \n> Please review!\n\n\nApparently that has positive review now.  JP, do we really need to generate a smaller patch with \"use matching autoconf\", or is that unnecessary?  This ticket is currently \"needs info\" but it isn't clear to me what info is needed.  Is it really sage-pending on #13324, or is there something else we're trying to get feedback on?  Thanks.",
    "created_at": "2012-12-29T03:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85550",
    "user": "https://github.com/kcrisman"
}
```

> OK, this is now #13860
> 
> Please review!


Apparently that has positive review now.  JP, do we really need to generate a smaller patch with "use matching autoconf", or is that unnecessary?  This ticket is currently "needs info" but it isn't clear to me what info is needed.  Is it really sage-pending on #13324, or is there something else we're trying to get feedback on?  Thanks.



---

archive/issue_comments_085551.json:
```json
{
    "body": "Replying to [comment:93 kcrisman]:\n> > OK, this is now #13860\n> > \n> > Please review!\n\n> \n> Apparently that has positive review now.  JP, do we really need to generate a smaller patch with \"use matching autoconf\", or is that unnecessary?  This ticket is currently \"needs info\" but it isn't clear to me what info is needed.  Is it really sage-pending on #13324, or is there something else we're trying to get feedback on?  Thanks.\n\nI'd like to get upstream feedback on the import library changes and include an official patch rather mine.\nI guess we'll have to wait for the end of the holidays for that :)",
    "created_at": "2013-01-04T10:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85551",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Replying to [comment:93 kcrisman]:
> > OK, this is now #13860
> > 
> > Please review!

> 
> Apparently that has positive review now.  JP, do we really need to generate a smaller patch with "use matching autoconf", or is that unnecessary?  This ticket is currently "needs info" but it isn't clear to me what info is needed.  Is it really sage-pending on #13324, or is there something else we're trying to get feedback on?  Thanks.

I'd like to get upstream feedback on the import library changes and include an official patch rather mine.
I guess we'll have to wait for the end of the holidays for that :)



---

archive/issue_comments_085552.json:
```json
{
    "body": "And inbetween we can already get #13324 merged...",
    "created_at": "2013-01-04T10:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85552",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

And inbetween we can already get #13324 merged...



---

archive/issue_comments_085553.json:
```json
{
    "body": "> And inbetween we can already get #13324 merged...\n\nAnd maybe even #13364...",
    "created_at": "2013-01-04T14:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85553",
    "user": "https://github.com/kcrisman"
}
```

> And inbetween we can already get #13324 merged...

And maybe even #13364...



---

archive/issue_comments_085554.json:
```json
{
    "body": "> I'd like to get upstream feedback on the import library changes and include an official patch rather mine.\n> I guess we'll have to wait for the end of the holidays for that :)\n\nMy holidays are done :)  And it does look like there has been some activity on the ECL list again.  But I think that's not important and we can all take a break, because...\n\nReally I think there is no reason to wait on upstream; Sage does contribute upstream, but we still take care of our own.  Is there anything *else* you would want to change here?  even the whole \"generate smaller patch\" thing seems less significant.  As far as I'm concerned, the current spkg is fine especially since the \"dependencies\" in Maxima and ECL are in/positive review.",
    "created_at": "2013-01-14T17:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85554",
    "user": "https://github.com/kcrisman"
}
```

> I'd like to get upstream feedback on the import library changes and include an official patch rather mine.
> I guess we'll have to wait for the end of the holidays for that :)

My holidays are done :)  And it does look like there has been some activity on the ECL list again.  But I think that's not important and we can all take a break, because...

Really I think there is no reason to wait on upstream; Sage does contribute upstream, but we still take care of our own.  Is there anything *else* you would want to change here?  even the whole "generate smaller patch" thing seems less significant.  As far as I'm concerned, the current spkg is fine especially since the "dependencies" in Maxima and ECL are in/positive review.



---

archive/issue_comments_085555.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-01-14T17:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85555",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_085556.json:
```json
{
    "body": "That's fair, I'll check the spkg is clean cause I don't really remember right now and report back here so someone motivated can put this as positive review (I guess you could as this is really only Cygwin (and MinGW) related and should have no effect on any other system).",
    "created_at": "2013-01-15T08:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85556",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

That's fair, I'll check the spkg is clean cause I don't really remember right now and report back here so someone motivated can put this as positive review (I guess you could as this is really only Cygwin (and MinGW) related and should have no effect on any other system).



---

archive/issue_comments_085557.json:
```json
{
    "body": "Just a reminder for me, I should add a simple hack to take care of http://sourceforge.net/p/ecls/bugs/222/ in order to produce cleaner libs as well.",
    "created_at": "2013-01-15T08:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85557",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Just a reminder for me, I should add a simple hack to take care of http://sourceforge.net/p/ecls/bugs/222/ in order to produce cleaner libs as well.



---

archive/issue_comments_085558.json:
```json
{
    "body": "> Just a reminder for me, I should add a simple hack to take care of http://sourceforge.net/p/ecls/bugs/222/ in order to produce cleaner libs as well.\n\nMaybe that *can* wait for upstream; I don't think it's necessary here and I don't know if I'll have the chance to test things as much now.",
    "created_at": "2013-01-15T14:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85558",
    "user": "https://github.com/kcrisman"
}
```

> Just a reminder for me, I should add a simple hack to take care of http://sourceforge.net/p/ecls/bugs/222/ in order to produce cleaner libs as well.

Maybe that *can* wait for upstream; I don't think it's necessary here and I don't know if I'll have the chance to test things as much now.



---

archive/issue_comments_085559.json:
```json
{
    "body": "Ok, I've looked back at the spkg and it looks clean in fact.\nAs you suggested I won't include additional (and not absolutely necessary) fixes.\n\nSo if you feel inclined, please put this as positive review.\nThe main points I guess are to:\n* check it works as expected on Cygwin (and makes something somehow sensible),\n* look at the patch to make sure it does not do anything on other platforms,\n* check the spkg is clean.\n\nIf #13324 goes in in a previous release, I guess we'll have to properly rebase it because of hg history and tags?\nBut I feel it is not necessary if this ticket and #13324 get merged at once in 5.7, is that right?\nWhat would be your strategy Jeroen?",
    "created_at": "2013-01-18T09:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85559",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Ok, I've looked back at the spkg and it looks clean in fact.
As you suggested I won't include additional (and not absolutely necessary) fixes.

So if you feel inclined, please put this as positive review.
The main points I guess are to:
* check it works as expected on Cygwin (and makes something somehow sensible),
* look at the patch to make sure it does not do anything on other platforms,
* check the spkg is clean.

If #13324 goes in in a previous release, I guess we'll have to properly rebase it because of hg history and tags?
But I feel it is not necessary if this ticket and #13324 get merged at once in 5.7, is that right?
What would be your strategy Jeroen?



---

archive/issue_comments_085560.json:
```json
{
    "body": "Replying to [comment:103 jpflori]:\n> What would be your strategy Jeroen?\n\nThe plan is certainly to merge #13324 in sage-5.7.beta0.  Of course, unexpected problems can always appear, but so far the new ECL has passed all buildbot tests.\n\nI don't quite understand how this ticket relates to #13324, as that is also about Cygwin...",
    "created_at": "2013-01-18T09:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85560",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:103 jpflori]:
> What would be your strategy Jeroen?

The plan is certainly to merge #13324 in sage-5.7.beta0.  Of course, unexpected problems can always appear, but so far the new ECL has passed all buildbot tests.

I don't quite understand how this ticket relates to #13324, as that is also about Cygwin...



---

archive/issue_comments_085561.json:
```json
{
    "body": "#13324 was only about building ecl on Cygwin.\nThis ticket is about resolving a conflict between the main ecl library being called ecl.dll and the one for the ecl interface in Sage having the same name.\nIndeed Windows cannot deal will that: the latter one should link to the former one but at runtime it resolves this dependency by linking back to itself because of the name collision...",
    "created_at": "2013-01-18T09:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85561",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

#13324 was only about building ecl on Cygwin.
This ticket is about resolving a conflict between the main ecl library being called ecl.dll and the one for the ecl interface in Sage having the same name.
Indeed Windows cannot deal will that: the latter one should link to the former one but at runtime it resolves this dependency by linking back to itself because of the name collision...



---

archive/issue_comments_085562.json:
```json
{
    "body": "Ideally, the `hg` history would be preserved so I prefer a proper rebase to #13324.  But let's wait until sage-5.7.beta0 is released.\n\nIn any case, this ticket still needs to be reviewed (without worrying about rebasing for now).",
    "created_at": "2013-01-18T10:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85562",
    "user": "https://github.com/jdemeyer"
}
```

Ideally, the `hg` history would be preserved so I prefer a proper rebase to #13324.  But let's wait until sage-5.7.beta0 is released.

In any case, this ticket still needs to be reviewed (without worrying about rebasing for now).



---

archive/issue_comments_085563.json:
```json
{
    "body": "Concerning \"autoconf\": the autotools optional package should solve that problem.  Install that package in some Sage version (this doesn't have to be Cygwin), run a Sage shell and then run autoconf/automake/autowhatever from within that Sage shell.",
    "created_at": "2013-01-18T10:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85563",
    "user": "https://github.com/jdemeyer"
}
```

Concerning "autoconf": the autotools optional package should solve that problem.  Install that package in some Sage version (this doesn't have to be Cygwin), run a Sage shell and then run autoconf/automake/autowhatever from within that Sage shell.



---

archive/issue_comments_085564.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-01-18T10:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85564",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085565.json:
```json
{
    "body": "Yeah I'm aware of that... and you just made me realize that's what I originally intended to do and forgot to do this morning although it's written evreywhere in this ticket.",
    "created_at": "2013-01-18T10:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85565",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Yeah I'm aware of that... and you just made me realize that's what I originally intended to do and forgot to do this morning although it's written evreywhere in this ticket.



---

archive/issue_comments_085566.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-18T10:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85566",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085567.json:
```json
{
    "body": "Done (I'm aware about the not changed date in SPKG.txt but whatever).",
    "created_at": "2013-01-18T10:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85567",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Done (I'm aware about the not changed date in SPKG.txt but whatever).



---

archive/issue_comments_085568.json:
```json
{
    "body": "Beware with timestamps when patching `configure`!\n\nYou must ensure that the timestamp of `configure` is more recent than that of the various `.in` files, otherwise `make` might want to rerun `autoconf`, leading to potential failures.\n\nOne solution is to edit the patch file such that `configure` comes last, as `patch` processes files in order.  Or manually `touch configure` afterwards.",
    "created_at": "2013-01-18T10:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85568",
    "user": "https://github.com/jdemeyer"
}
```

Beware with timestamps when patching `configure`!

You must ensure that the timestamp of `configure` is more recent than that of the various `.in` files, otherwise `make` might want to rerun `autoconf`, leading to potential failures.

One solution is to edit the patch file such that `configure` comes last, as `patch` processes files in order.  Or manually `touch configure` afterwards.



---

archive/issue_comments_085569.json:
```json
{
    "body": "True indeed, doing that now, sorry for being that lame on this one.",
    "created_at": "2013-01-18T10:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85569",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

True indeed, doing that now, sorry for being that lame on this one.



---

archive/issue_comments_085570.json:
```json
{
    "body": "Should be ok now (I've even taken the time to actually try to build it (on Linux)).",
    "created_at": "2013-01-18T10:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85570",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Should be ok now (I've even taken the time to actually try to build it (on Linux)).



---

archive/issue_comments_085571.json:
```json
{
    "body": "Attachment [ecl-12.12.1.p1.diff](tarball://root/attachments/some-uuid/ticket9167/ecl-12.12.1.p1.diff) by jpflori created at 2013-01-18 10:54:08\n\nSpkg diff, for review only.",
    "created_at": "2013-01-18T10:54:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85571",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Attachment [ecl-12.12.1.p1.diff](tarball://root/attachments/some-uuid/ticket9167/ecl-12.12.1.p1.diff) by jpflori created at 2013-01-18 10:54:08

Spkg diff, for review only.



---

archive/issue_comments_085572.json:
```json
{
    "body": "Grmph, the train's wifi cut me off...\n\nShort version: is there anything actually different from the previous spkg that did work?  I also can't see any configure changes in the patch, maybe that's a good thing.",
    "created_at": "2013-01-18T13:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85572",
    "user": "https://github.com/kcrisman"
}
```

Grmph, the train's wifi cut me off...

Short version: is there anything actually different from the previous spkg that did work?  I also can't see any configure changes in the patch, maybe that's a good thing.



---

archive/issue_comments_085573.json:
```json
{
    "body": "Okay, all relevant tests pass with this (and a rebuilt Maxima) on Mac.  I say positive review, assuming JP clarifies my dumb comment about configure and he confirms that he fixed the timestamp issue (I think he is saying that he did in comment:112).",
    "created_at": "2013-01-22T16:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85573",
    "user": "https://github.com/kcrisman"
}
```

Okay, all relevant tests pass with this (and a rebuilt Maxima) on Mac.  I say positive review, assuming JP clarifies my dumb comment about configure and he confirms that he fixed the timestamp issue (I think he is saying that he did in comment:112).



---

archive/issue_comments_085574.json:
```json
{
    "body": "The implib.patch I posted here only touches the autotools file (you then need to somehow regenerate the build system, let's say autoreconf -i).\n\nI've done this for the spkg, so the one included in the spkg (and in the diff posted here) is the same plus the changes to the build system (after runing autoreconf -i using matching versions of autotools).\n\nAnd I've indeed reordered the spkg's patch hunks so that autotools files are patched before the build system one to ensure that autotools does not decide to regenerate everything on the fly.",
    "created_at": "2013-01-23T09:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85574",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

The implib.patch I posted here only touches the autotools file (you then need to somehow regenerate the build system, let's say autoreconf -i).

I've done this for the spkg, so the one included in the spkg (and in the diff posted here) is the same plus the changes to the build system (after runing autoreconf -i using matching versions of autotools).

And I've indeed reordered the spkg's patch hunks so that autotools files are patched before the build system one to ensure that autotools does not decide to regenerate everything on the fly.



---

archive/issue_comments_085575.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-24T19:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85575",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085576.json:
```json
{
    "body": "I can no longer check this due to horrible BLODA issues but my comment:115 stands, and if Jeroen agrees that these are stamped in the correct order, then let's get this in, since it does work.",
    "created_at": "2013-01-24T19:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85576",
    "user": "https://github.com/kcrisman"
}
```

I can no longer check this due to horrible BLODA issues but my comment:115 stands, and if Jeroen agrees that these are stamped in the correct order, then let's get this in, since it does work.



---

archive/issue_comments_085577.json:
```json
{
    "body": "Is it possible one might get a doctest error on this?  I did a weird upgrade where I already had this ticket, from 5.6.rc0 to 5.6, and then got this.\n\n```\nFile \"/Users/karl.crisman/Downloads/sage-5.6/devel/sage/sage/libs/ecl.pyx\", line 247:\n    sage: inf_loop()\nExpected:\n    Traceback (most recent call last):\n    ...\n    RuntimeError: ECL says: Console interrupt\nGot:\n    Traceback (most recent call last):\n      File \"/Users/karl.crisman/Downloads/sage-5.6/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/karl.crisman/Downloads/sage-5.6/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/karl.crisman/Downloads/sage-5.6/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[7]>\", line 1, in <module>\n        inf_loop()###line 247:\n    sage: inf_loop()\n      File \"ecl.pyx\", line 704, in sage.libs.ecl.EclObject.__call__ (sage/libs/ecl.c:5038)\n      File \"ecl.pyx\", line 280, in sage.libs.ecl.ecl_safe_apply (sage/libs/ecl.c:3049)\n    RuntimeError: ECL says: Console interrupt.\n```\nNote the one-character difference (on Mac, anyway).  Can someone check this?  I think it might be due to my having done the upgrade and thus not important.",
    "created_at": "2013-01-24T21:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85577",
    "user": "https://github.com/kcrisman"
}
```

Is it possible one might get a doctest error on this?  I did a weird upgrade where I already had this ticket, from 5.6.rc0 to 5.6, and then got this.

```
File "/Users/karl.crisman/Downloads/sage-5.6/devel/sage/sage/libs/ecl.pyx", line 247:
    sage: inf_loop()
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: ECL says: Console interrupt
Got:
    Traceback (most recent call last):
      File "/Users/karl.crisman/Downloads/sage-5.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/karl.crisman/Downloads/sage-5.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/karl.crisman/Downloads/sage-5.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[7]>", line 1, in <module>
        inf_loop()###line 247:
    sage: inf_loop()
      File "ecl.pyx", line 704, in sage.libs.ecl.EclObject.__call__ (sage/libs/ecl.c:5038)
      File "ecl.pyx", line 280, in sage.libs.ecl.ecl_safe_apply (sage/libs/ecl.c:3049)
    RuntimeError: ECL says: Console interrupt.
```
Note the one-character difference (on Mac, anyway).  Can someone check this?  I think it might be due to my having done the upgrade and thus not important.



---

archive/issue_comments_085578.json:
```json
{
    "body": "That's expected, the first patch from http://trac.sagemath.org/sage_trac/ticket/13324 should fix that.",
    "created_at": "2013-01-24T23:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85578",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

That's expected, the first patch from http://trac.sagemath.org/sage_trac/ticket/13324 should fix that.



---

archive/issue_comments_085579.json:
```json
{
    "body": "Hmm, that sounds familiar.  Great.",
    "created_at": "2013-01-25T01:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85579",
    "user": "https://github.com/kcrisman"
}
```

Hmm, that sounds familiar.  Great.



---

archive/issue_comments_085580.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-01-26T09:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85580",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_022553.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-26T09:52:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9167#event-22553"
}
```



---

archive/issue_comments_085581.json:
```json
{
    "body": "How did you report this?\nit ought to be reported here: https://gitlab.com/embeddable-common-lisp/ecl/issues",
    "created_at": "2016-03-21T12:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85581",
    "user": "https://github.com/dimpase"
}
```

How did you report this?
it ought to be reported here: https://gitlab.com/embeddable-common-lisp/ecl/issues



---

archive/issue_comments_085582.json:
```json
{
    "body": "IIRC this was reported on sourceforge.net where ECL used to be hosted.",
    "created_at": "2016-03-21T12:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85582",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

IIRC this was reported on sourceforge.net where ECL used to be hosted.



---

archive/issue_comments_085583.json:
```json
{
    "body": "well, yes, but it seems to be lost...",
    "created_at": "2016-03-21T12:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85583",
    "user": "https://github.com/dimpase"
}
```

well, yes, but it seems to be lost...



---

archive/issue_comments_085584.json:
```json
{
    "body": "At least there is a copy of the discussion on the former ECL list here:\n* https://www.mail-archive.com/ecls-list`@`lists.sourceforge.net/msg01978.html\n(and one in my mailbox...)",
    "created_at": "2016-03-21T12:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85584",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

At least there is a copy of the discussion on the former ECL list here:
* https://www.mail-archive.com/ecls-list`@`lists.sourceforge.net/msg01978.html
(and one in my mailbox...)



---

archive/issue_comments_085585.json:
```json
{
    "body": "Could you repost that bug report to upstream?",
    "created_at": "2016-03-21T12:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85585",
    "user": "https://github.com/jdemeyer"
}
```

Could you repost that bug report to upstream?



---

archive/issue_comments_085586.json:
```json
{
    "body": "Done:\n* https://gitlab.com/embeddable-common-lisp/ecl/issues/235",
    "created_at": "2016-03-21T13:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9167#issuecomment-85586",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Done:
* https://gitlab.com/embeddable-common-lisp/ecl/issues/235
