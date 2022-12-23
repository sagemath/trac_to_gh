# Issue 9167: cygwin: importing sage.libs.ecl yields a "no such process" error

Issue created by migration from https://trac.sagemath.org/ticket/9167

Original creator: was

Original creation time: 2010-06-07 04:25:41

Assignee: tbd

CC:  mhansen dimpase jpflori jdemeyer

Though the C-library interface to ecl builds on cygwin, it does not work at all.  All tests fail:


```
sage: import sage.libs.ecl
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/home/wstein/sage-4.4.3/<ipython console> in <module>()

ImportError: No such process
sage: 
```



---

Comment by drkirkby created at 2010-08-02 04:07:28

I don't know if it's related, but gcc reports are couple of rather serious looking warning messages with ecl. 


```
/export/home/drkirkby/sage-4.5.1/spkg/build/ecl-10.2.1.p1/src/src/c/dpp.c:678: warning: too few arguments for format
/export/home/drkirkby/sage-4.5.1/spkg/build/ecl-10.2.1.p1/src/src/c/dpp.c:680: warning: too many arguments for format
```


I'm surprised that gcc does not reject such code and refuse to compile it. 

Dave


---

Comment by kcrisman created at 2011-08-01 16:01:54

I can confirm this on the most recent versions of everything at [the port wiki page](CygwinPort).    

That is bad, because now the default Maxima (and hence ECL) for calculus *is* the library one.


---

Comment by kcrisman created at 2011-08-08 14:57:54

Two possibly irrelevant data points:
 * Tab-completion on `from sage.libs.[tab]` gives `sage.libs.ecl` on Mac, not on Cygwin (it also doesn't give `.libecm` or `.ratpoints`, though at least ratpoints works).
 * The directory `$SAGE_LOCAL/lib/python/site-packages/sage/libs/` DOES include `ecl.pyx` and `ecl.dll`, so the library seems to be there, if that is where such imports actually come from (which I'm not sure about).


---

Comment by kcrisman created at 2011-08-08 15:42:18

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

Comment by kcrisman created at 2011-08-08 15:46:16

[This stackoverflow question](http://stackoverflow.com/questions/2879246/psycopg2-on-cygwin-no-such-process) also might have a useful piece of information.  I don't know how to open/read dlls, though, nor exactly how to trace why it is that it's not finding things.


---

Comment by kcrisman created at 2011-08-08 16:02:21

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

Comment by kcrisman created at 2011-08-08 16:29:31

Replying to [comment:6 kcrisman]:
> [Cygwin's cygcheck information](http://www.cygwin.com/cygwin-ug-net/using-utils.html) was much more helpful, and I find two things.
>  * When looking at `$SAGE_LOCAL/libs/ecl.dll`, 
> {{{
> cygcheck: track_down:  could not find cyggc-1.dll
> }}}
>    shows up a lot.   I have `cyggcc_s-1.dll`, `cyggcj-*`, `cyggcr-0.dll` and some others, but not this, in `/bin/`.

Mine, at least, does NOT have `cyggc-1.dll` anywhere.  Apparently it does have libgc (this is a garbage collector) which I've seen connected to `cyggc-1.dll` on [the Cygwin list](http://www.mail-archive.com/cygwin-apps`@`cygwin.com/msg06654.html).  But I don't see how I could have `libgc` without `cyggc-1.dll` if that were the case... I guess the only thing to try is upgrading my libgc and adding libgc-devel, though I'm a little scared!


---

Comment by kcrisman created at 2011-08-08 16:57:08

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

Comment by leif created at 2011-08-08 18:56:14

Replying to [comment:8 kcrisman]:
>

```
...
    soname_spec='`echo ${libname} | sed -e 's/^lib/cyg/'``echo ${release} | sed -e 's/[.]/-/g'`${versuffix}.dll'
...
```

> and a few similar things in the configure and aclocal files.

Where does this come from? ECL?

This _might_ be the cause of the problem, since the `sed` command also replaces the `lib` prefix by `cyg`.


---

Comment by leif created at 2011-08-08 19:02:43

P.S.:

The `nm` and `objdump` utilities from the GNU `binutils` package might be helpful to inspect libraries etc.

I vaguely remember there was also `dlltool` (perhaps from the MinGW project though).


---

Comment by kcrisman created at 2011-08-08 19:09:03

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

> This _might_ be the cause of the problem, since the `sed` command also replaces the `lib` prefix by `cyg`.

Right, that is why I pointed to it.  But it doesn't seem to replace the `-6.4.1` (or `-7.1.1`, now) with `-1`, as far as I could tell.  And I didn't have anything like `cyggc-*` on it.  

I'm almost done upgrading and adding `libgc-devel` on my Cygwin - which meant upgrading basically every single Cygwin package, because this Cygwin hadn't been changed in a year or more.  Hopefully won't break anything else, but probably will :(

As to the tools, I think that cygcheck helped a lot, so for now I'm going to stick with that because I actually sort of understand it :)


---

Comment by kcrisman created at 2011-08-08 20:21:51

> Right, that is why I pointed to it.  But it doesn't seem to replace the `-6.4.1` (or `-7.1.1`, now) with `-1`, as far as I could tell.  And I didn't have anything like `cyggc-*` on it.  
> 
> I'm almost done upgrading and adding `libgc-devel` on my Cygwin - which meant upgrading basically every single Cygwin package, because this Cygwin hadn't been changed in a year or more.  Hopefully won't break anything else, but probably will :(

I think that libgc-devel was what it took to get this file.  However, the upgrade upgraded too much - see [this Cygwin list thread](http://cygwin.com/ml/cygwin/2011-03/msg00750.html) - so I had to downgrade libgfortran as described there, and gcc, and ....  Not for the last time, I have to say that Cygwin definitely is a moving target.


---

Comment by kcrisman created at 2011-08-08 21:31:50

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

Comment by kcrisman created at 2011-08-09 01:54:19

After a *lot* of trouble managing to get Cygwin shell to find lapack again, I definitely have the right files now.    We definitely need as at least part of the fix to add `libgc-devel` as a dependency.

However, there is also still a problem that `cygcheck` finds all the needed dlls for the `ecl.dll` in `local/lib` and `local/bin`, but not for the ones in `devel/sage/build/sage/libs/`.  It cannot find `ecl.dll` or `csage.dll`.  Which seems weird, since those files certainly exist.  

This might be a `PATH` problem, judging by some similar issues elsewhere.  Unfortunately, `./sage -gdb` is no help here, nor is `./sage -ipython`.


---

Comment by kcrisman created at 2011-08-09 02:54:23

> However, there is also still a problem that `cygcheck` finds all the needed dlls for the `ecl.dll` in `local/lib` and `local/bin`, but not for the ones in `devel/sage/build/sage/libs/`.  It cannot find `ecl.dll` or `csage.dll`.  Which seems weird, since those files certainly exist.  

Yeah, after a `./sage -br` it still looks like `csage.dll` is not being found for some reason.  Must be a path issue, I think.  Where do we set the Sage path?  It certainly doesn't include `local/lib`, but I don't know if that's really the problem.


---

Comment by leif created at 2011-08-09 03:36:34

Replying to [comment:15 kcrisman]:
> > However, there is also still a problem that `cygcheck` finds all the needed dlls for the `ecl.dll` in `local/lib` and `local/bin`, but not for the ones in `devel/sage/build/sage/libs/`.  It cannot find `ecl.dll` or `csage.dll`.  Which seems weird, since those files certainly exist.  
> 
> Yeah, after a `./sage -br` it still looks like `csage.dll` is not being found for some reason.  Must be a path issue, I think.  Where do we set the Sage path?

In `local/bin/sage-env`. You could special-case Cygwin there and add all directories that contain DLLs, as Windows treats them as executables.

> It certainly doesn't include `local/lib`, but I don't know if that's really the problem.

Well, before editing `sage-env`, you could just try modifying your `PATH` from the shell accordingly.


---

Comment by kcrisman created at 2011-08-09 13:10:41

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

 * Bad news: even with this added to `PATH` _and_ this being in the `sage-env`, I still have this problem.  I'm still pretty sure it's a path issue, but maybe they are in the wrong order or something?   I have no idea how complex this could get...


---

Comment by kcrisman created at 2011-08-09 15:05:37

>  * News: `sage-env` includes

```
if [ "$UNAME" = "CYGWIN" ]; then
    PATH="$PATH:$SAGE_LOCAL/lib" && export PATH
fi
```

>  * Bad news: even with this added to `PATH` _and_ this being in the `sage-env`, I still have this problem.  I'm still pretty sure 
For some reason this is not actually in Sage's path, gotten by `sys.path` in the Sage session.  And adding it to `sys.path` didn't help, either.  What the heck is going on?


---

Comment by kcrisman created at 2011-08-09 15:52:24

Another possibility, suggested by [this thread](http://old.nabble.com/Re%3A-installing-pygtk-on-cygwin-td19560334.html#a20513293), is that there could be two of some file making things hard.  Interestingly, there are several ecl.dll's floating around (everywhere a libecl.{dylib,so} would live, I guess) and cygcheck gives different dependencies for each.


---

Comment by leif created at 2011-08-09 17:36:53

Replying to [comment:18 kcrisman]:
> >  * News: `sage-env` includes

```sh
if [ "$UNAME" = "CYGWIN" ]; then
    PATH="$PATH:$SAGE_LOCAL/lib" && export PATH
fi
```


Yep, but this should IMHO be moved up in the file (including the definition of `UNAME`), in any case above

```sh
if [ "$1" = "-short" ]; then
    return 0
fi
```

and `$SAGE_LOCAL/lib` should be *pre*pended to pick up Sage's versions _first_.

> For some reason this is not actually in Sage's path, gotten by `sys.path` in the Sage session.  And adding it to `sys.path` didn't help, either.  What the heck is going on?

No idea. What does `os.environ.get("PATH")` give?

I also don't know if we have to add some more or different things to `PYTHONPATH` on Cygwin.

Note that e.g. `$SAGE_LOCAL/lib/python` (which is added to `PYTHONPATH` [if it is a directory] in `sage-env`) is a *symbolic link* on Linux etc. (pointing to `$SAGE_LOCAL/lib/python2.6`); I don't know if it is the real directory on Cygwin instead.


---

Comment by kcrisman created at 2011-08-09 20:13:45

> and `$SAGE_LOCAL/lib` should be *pre*pended to pick up Sage's versions _first_.
That sounds like a good idea.  But should it be before `$SAGE_ROOT` and `$SAGE_LOCAL/bin`?
> > For some reason this is not actually in Sage's path, gotten by `sys.path` in the Sage session.  And adding it to `sys.path` didn't help, either.  What the heck is going on?
> 
> No idea. What does `os.environ.get("PATH")` give?
This gives what I would expect - Sage root, Sage local bin, usr/bin, some Cygwin stuff, a Lapack thing I had to add due to my carelessness, and then Sage local lib.
> I also don't know if we have to add some more or different things to `PYTHONPATH` on Cygwin.
This is very sparse.  It is just the directory below.
> Note that e.g. `$SAGE_LOCAL/lib/python` (which is added to `PYTHONPATH` [if it is a directory] in `sage-env`) is a *symbolic link* on Linux etc. (pointing to `$SAGE_LOCAL/lib/python2.6`); I don't know if it is the real directory on Cygwin instead.
It looks like it's the same on Cygwin.

Another interesting thing is that there are libntl.dll files in /local/bin and /local/lib.  Moving just one doesn't seem to do much - note that the bin one is the one imported usually, as in your comment above.  Furthermore, apparently only the ecl.dll in devel/sage/build/sage/libs needs libntl.dll and cyggmp, while the one in local/{bin,lib} just wants cyggmp-3.dll.

Anyway, I guess I can move files around all day but I'm not getting any nearer.


---

Comment by kcrisman created at 2011-12-07 15:54:44

Question for Dima or others; is it possible that we have _too many_ copies of the dlls?  Either that the ecl.dll files are in too many places - local/lib and local/bin - or that the extra libntl.dll files also are causing problems?  See #11635 for where this started - perhaps this is the cause of all the trouble?


---

Comment by dimpase created at 2011-12-14 02:45:05

Replying to [comment:22 kcrisman]:
> Question for Dima or others; is it possible that we have _too many_ copies of the dlls?  Either that the ecl.dll files are in too many places - local/lib and local/bin - or that the extra libntl.dll files also are causing problems?  See #11635 for where this started - perhaps this is the cause of all the trouble?  


for the record, 2 different copies of ecl.dll in SAGE_ROOT/local/ are created; one in local/lib (and/or local/bin), created from ecl spkg, the other in local/lib/python2.6/site-packages/sage/libs/, which contains Sage/Python interface to ecl (I don't know details about how and when it is built).


---

Comment by kcrisman created at 2011-12-14 02:50:37

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

Comment by kcrisman created at 2011-12-14 02:59:00

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

Comment by kcrisman created at 2011-12-14 03:30:13

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

Comment by dimpase created at 2011-12-14 04:00:53

Replying to [comment:26 kcrisman]:
> Scratch that - in private comm. Dima points out that we should be in the subshell.

still, we need to know details of Sage/Python extension implementation on Cygwin to solve this. It could be just an artefact of broken Python/Cython (fork() failures when running sage -b are a pain...)


---

Comment by jpflori created at 2012-08-05 13:57:18

Just for info, on my Cygwin 1.7.16/Sage 5.2 install cygchecking all the ecl.* things shows no problem.
So the problem looks more subtle...


---

Comment by jpflori created at 2012-08-07 13:15:20

I found it quite strange that the problematic ecl.dll links to itself.
Maybe it's wanting the other ecl.dll, but gets itself because of the name clash.

I'll try to rename ecl.pyx to ecl_blah.pyx, regenerate it and import it to see what happens.


---

Comment by jpflori created at 2012-08-07 13:22:26

No problem importing ecl_blah (after removing the former ecl.dll in the same directory sage/libs/)!


---

Comment by jpflori created at 2012-08-07 13:35:59

And the question is now, why do we get ecl.dll in local/lib/ rather than libecl.dll.


---

Comment by dimpase created at 2012-08-07 14:04:21

Replying to [comment:32 jpflori]:
> And the question is now, why do we get ecl.dll in local/lib/ rather than libecl.dll.
the following [Cygwin doc](http://cygwin.com/cygwin-ug-net/dll.html#dll-build) seems to imply that  `lib` prefix is merely a matter of convenience; it recommends that there should be no `libecl.dll`; it should rather be `cygecl.dll` and `libecl.dll.a`.


---

Comment by jpflori created at 2012-08-07 14:07:14

Ok, that's because in ecl build system, the shared library is named
${SHAREDPREFIX}ecl.${SHAREDEXT}
and these two variables are set to '' and 'dll' by configure on Cygwin.


---

Comment by jpflori created at 2012-08-07 14:08:13

Replying to [comment:33 dimpase]:
> Replying to [comment:32 jpflori]:
> > And the question is now, why do we get ecl.dll in local/lib/ rather than libecl.dll.
> the following [Cygwin doc](http://cygwin.com/cygwin-ug-net/dll.html#dll-build) seems to imply that  `lib` prefix is merely a matter of convenience; it recommends that there should be no `libecl.dll`; it should rather be `cygecl.dll` and `libecl.dll.a`.
I agree with you.
The question is now if it's trivial enough to modify the build of the shared library on Cygwin.
Unfortunately, ecl does not use libtool.


---

Comment by jpflori created at 2012-08-07 14:12:27

I think the changes could be quite easy, I'll give it a try.


---

Comment by jpflori created at 2012-08-07 15:52:26

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

Comment by jpflori created at 2012-08-07 16:59:17

Changing keywords from "" to "cygwin spkg ecl".


---

Comment by jpflori created at 2012-08-07 16:59:17

Proposed spkg at http://perso.telecom-paristech.fr/~flori/sage/ecl-11.1.2.cvs20111120.p3.spkg


---

Comment by jpflori created at 2012-08-07 16:59:17

Changing status from new to needs_review.


---

Comment by leif created at 2012-08-07 17:22:03

Replying to [comment:37 jpflori]:
> As I had to run autoconf which modified a lot of data in config*, the patch included and the hg history will be quite big ...

You may try to use the exact same versions of `automake` and `autoconf`... ;-)

> Another solution would be to included a patched src directory in the spkg, but I can already hear people ranting.

Well, I'm personally ok with just "autoreconfing" `src/`, but such disturbes the move to git.

> Or directly patch configure in a minimal way, but I'm not so inclined to doing so.

If the patch isn't that large, that's perhaps the best solution until upstream includes a fix.  If they quickly include it into some devel version, we could try to upgrade to that.


---

Comment by jpflori created at 2012-08-07 17:25:00

Replying to [comment:39 leif]:
> If the patch isn't that large, that's perhaps the best solution until upstream includes a fix.  If they quickly include it into some devel version, we could try to upgrade to that.
> 
I agree with both these ideas, see also https://groups.google.com/d/topic/sage-devel/Ikwfh6PXJnQ/discussion .

The problem with patching configure directly is that it needs more dirty work and I'm lazy to do it.


---

Comment by jpflori created at 2012-08-07 17:26:47

And the problem with the upstream solution is that upstream is quite far away from our version and that would also need much more work (if things break, which can be expected).


---

Comment by dimpase created at 2012-08-08 04:29:45

Changing status from needs_review to needs_work.


---

Comment by dimpase created at 2012-08-08 04:29:45

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

Comment by dimpase created at 2012-08-08 05:40:12

Replying to [comment:43 dimpase]:
> the new spkg installs OK, but gives the following linking error during the build of various Sage dlls:

please aslo see [Redhat's docs](http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/4/html/Using_ld_the_GNU_Linker/win32.html) for more details on linking on Cygwin. It seems that we might misunderstand the need for and the purpose of `libecl.dll.a`


---

Comment by jpflori created at 2012-08-08 07:26:19

The purpose of libecl.dll.a is to be able to link to Cygwin dlls from outside of the Cygwin world, with the Windows linker for example.
So for Sage on Cygwin, this is not needed.

The point here was to use a more generic installation for ECL, which would also work for linking from outside Cygwin, and which would as a side effect solves the name clash problem of this ticket.

The link problem is myabe something with that we do not -L$SAGE_LOCAL/bin when building/linking?
Libraries generated with libtool do not have this problem because libtool also creates a .la file, which is just a text file containing some info, and in particular where to look for the real shared library file, which is usually in ../cyg<libname>-<version info>.dll


---

Comment by jpflori created at 2012-08-08 08:36:06

What's strange is that copying back bin/cygecl.dll to lib/[lib]ecl.dll does not solve the problem.
And that bin/ecl.exe which links to cygecl.dll works fine.

I may have broken something while tweaking the Makefile...


---

Comment by jpflori created at 2012-08-08 09:06:55

Running nm on both libraries from this spkg and the previous one shows the same symbols exactly, but with a different address base.


---

Comment by dimpase created at 2012-08-08 10:12:26

Replying to [comment:47 jpflori]:
> Running nm on both libraries from this spkg and the previous one shows the same symbols exactly, but with a different address base.

the culprit is the new libecl.dll.a, which gets picked up by the linker first, what which is not what is needed (as this is for other purposes).
And this makes perfect sense, that's exactly what happens according to the Redhat docs cited above.

I have overcome this by moving libecl.dll.a out of SAGELOCAL/lib, and creating there a symbolic link named cygecl.dll 
to ../bin/cygecl.dll

Hopefully will get Sage that can at least start up some time soon...


---

Comment by jpflori created at 2012-08-08 10:22:02

I don't agree with the point that libecl.dll.a cshould not be picked up by the linker.
It is not necessary and you can directly link to cygecl.dll, that I agree with, but it should be possible to go through libecl.dll.a as well.
Of course, there might be a problem with the produced libecl.dll.a, but using import files should not be impossible.

Or then I don't understand how any piece of Sage can link with MPIR, MPFR and any other library which uses libtool and which generates as well import files and put them into SAGE_LOCAL/lib/ where they get picked up before anything else.
And I don't think we have any piece of code which makes sure these dll.a files are not used.


---

Comment by dimpase created at 2012-08-08 10:41:12

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

Comment by jpflori created at 2012-08-08 10:44:50

I don't think the .la files are used by ld at all, but I might be wrong.

The dllexport thing might be the problem, I'll check that.


---

Comment by jpflori created at 2012-08-08 12:03:38

The dll.a file is indeed broken.
Running nm on it should return much more symbols.

Maybe the dll[import|export] magic is broken.

For the dllimport this is sure.
In config.h, the dllimport maic is turned on if cygwin is defined, whereas gcc on cygwin defines _ _ CYGWIN _ _.

For the dllexport magic, I'm not sure.
During the build process there is indeed a cygwin variable defined which triggers the use of dllexport (or seems to do).


---

Comment by jpflori created at 2012-08-08 12:19:48

And I'm able to generate a correct dll.a file using nm and dlltool.
So the linking command which generates the dll.a file must be problematic.


---

Comment by jpflori created at 2012-08-08 13:08:55

Ok, think I got it.

I've put the implid stuff into LDFLAGS which are used several times, so libecl.dll.a keeps being regenerated which various stuff in it.


---

Comment by jpflori created at 2012-08-08 15:15:01

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2012-08-08 15:15:01

The spkg should be fixed now.

Nothing is committed yet, but please give it a try!


---

Comment by dimpase created at 2012-08-08 15:36:43

well, I have finished the previous build, but then Sage was refusing to start, throwing the usual fork() problems, even after repeated rebasealls and reboots. I've decided to update Cygwin and uninstall as much as possible of unneeded parts of Cygwin, in hope that it will help. But I am not optimistic.


---

Comment by jpflori created at 2012-08-09 08:55:50

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2012-08-09 09:00:37

See discussion at https://groups.google.com/d/topic/sage-devel/Ikwfh6PXJnQ/discussion for autotools regeneration issue.


---

Comment by dimpase created at 2012-08-10 04:06:07

Replying to [comment:56 dimpase]:
> well, I have finished the previous build, but then Sage was refusing to start, throwing the usual fork() problems, even after repeated rebasealls and reboots. I've decided to update Cygwin and uninstall as much as possible of unneeded parts of Cygwin, in hope that it will help. But I am not optimistic. 

no, still no luck. I start to suspect that 2GB of RAM are not enough on 32-bit Windows 7 to run Sage. When I examine the location of Sage dlls which produce these fork() failures, I see that 
  their preferred base addresses (set up by rebaseall) have nothing to do with the actual places they are allocated;

  these actual places may be already used by Win32 system dlls.

It could also be that it's just the 32-bit system is to blame, not the relatively low by modern standards amount of RAM. It's pathetic that on Linux 0.5GB of RAM are enough to have a well-running Sage, while here 2GB are not enough.


---

Comment by jpflori created at 2012-08-20 15:12:11

I've upped an upgraded spkg based on 12.7.1.p0 spkg from #13324 at
http://perso.telecom-paristech.fr/~flori/sage/ecl-12.7.1.p1.spkg
using the autotools stuff from #13357.

Nothing committed or tagged yet, nor retested on Cygwin.

Upstream is ready to include a similar patch if it does not break anything on any Windows port... which will need some more thorough testing before I can submit such a patch.
As far as Sage on Cygwin is concerned, everything seems fine (as much as possible...) so far.


---

Comment by jpflori created at 2012-08-20 15:12:11

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2012-08-20 16:14:40

I lost part of my changes during the update to 12.7.1...


---

Comment by jpflori created at 2012-08-20 16:14:40

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2012-08-20 16:26:24

Should be fixed now, patched aclocal.m4 is back and patches are correctly tracked.


---

Comment by jpflori created at 2012-08-20 16:26:24

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2012-08-20 16:53:45

Spkg diff, for review only. Not committed in spkg.


---

Attachment


---

Comment by dimpase created at 2012-10-03 17:39:06

I asked our sysadmins to get me a 64-bit Win7 system (VM), so that I have a chance to get a working Sage on Cygwin. It will take few days to get it up and properly running.


---

Comment by kcrisman created at 2012-10-05 16:41:18

This works on Cygwin on XP!  Great solution - I was just not quite knowledgeable about this stuff to help, though I spent far too long on it.

I won't have time to look at the spkg itself until Monday, but definitely positive review from actual practice!


---

Comment by jpflori created at 2012-10-05 23:36:06

Thanx for testing this, but anyway I don't think the package here should get merge, let's just wait for upstream to include something similar (which means action from my side, but should happen in a finite amount of time, we first have to deal with other strange things happening with ECL last stable version potentially ignoring signals).

The spkg here is nonetheless useful to get a somehow more useful build on Cygwin!


---

Comment by jpflori created at 2012-12-03 22:35:12

The issue is now discussed upstream at http://sourceforge.net/p/ecls/feature-requests/15/ (after some exchanges on the ecl-devel list).

The spkg here are outdated (although functional) and should be rebased on top of #13324.

The bug mentioned reported here:
http://sourceforge.net/p/ecls/bugs/222/
should as well be integrated here or at #13324.


---

Comment by kcrisman created at 2012-12-06 16:39:55

This is only a little bit off from being based on #13324, cosmetic stuff mostly.


---

Comment by kcrisman created at 2012-12-06 16:51:59

Not quite ready for prime-time, but [this spkg](http://sage.math.washington.edu/home/kcrisman/ecl-12.7.1.p1.spkg) with the above diff.  This is just naively porting JP's diff.  Somehow I mixed up something, and also there is the problem with the weird tarring... but an attempt, anyway.


---

Comment by kcrisman created at 2012-12-06 17:01:12

For review only - based on JP's spkg


---

Attachment

> Not quite ready for prime-time, but [this spkg](http://sage.math.washington.edu/home/kcrisman/ecl-12.7.1.p1.spkg) with the above diff.  This is just naively porting JP's diff.  Somehow I mixed up something, and also there is the problem with the weird tarring... but an attempt, anyway.

Okay, I see what I did wrong.  I still have the weird unknown extended keyword thing while untarring, but at least the patches apply now!  Waiting on the build, hopefully all will be well on Cygwin.


---

Comment by kcrisman created at 2012-12-06 17:30:38

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-12-06 17:30:38

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

Comment by kcrisman created at 2012-12-06 17:46:47

Eh, and it didn't even work on Cygwin for some reason (that is, same import errors).  I'm going to try JP's again.


---

Comment by kcrisman created at 2012-12-06 18:14:15

> Eh, and it didn't even work on Cygwin for some reason (that is, same import errors).  I'm going to try JP's again.
And now I get the same bad behavior (Mac and Cygwin).  I have a feeling that previous ECL stuff isn't properly destroyed when one does `sage -f ecl-x.y.z.spkg`.  But whatever.


---

Comment by jpflori created at 2012-12-10 13:05:49

That's strange, I guess you've rebuilt Maxima as well.


---

Comment by kcrisman created at 2012-12-10 17:42:15

> That's strange, I guess you've rebuilt Maxima as well.
Yes.  I think there were just leftover pieces around, I don't know how.  I think it's due to my own bad creation of the spkg.

So if you can provide an update to this spkg based on #13324, incorporating the same essential changes in the Cygwin-only case - no need to do anything fancy, just the same stuff - I would love to get that in.  The spkg you provided here earlier does still work on Cygwin, just checked a brand-new 5.5.rc0 build.


---

Comment by jpflori created at 2012-12-18 17:13:52

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2012-12-18 17:13:52

New spkg at
http://boxen.math.washington.edu/home/jpflori/ecl-12.12.1.p1.spkg

The upstream feature request is
http://sourceforge.net/p/ecls/feature-requests/15/


---

Comment by jpflori created at 2012-12-18 17:14:23

Patch to upstream build system.


---

Attachment

I guess I should have used a matching version of autoconf to generate a smaller diff.


---

Comment by jpflori created at 2012-12-18 17:16:23

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-12-18 20:40:11

XP report:

I almost forgot to `./sage -b`!  But it *does* fix the problem, based off of the p0 spkg.  Yes!

And before rebuilding Maxima I get the usual "don't know how to require Maxima" problem, but afterward, with the spkg from #13364, all is well.  Yay!  So all is well as far as I'm concerned.


---

Comment by kcrisman created at 2012-12-19 14:45:49

By the way, could this be upgraded irrespective of upgrading Maxima?  (I mean for Sage proper.)  If all we need is to change the location of the Maxima library, maybe we could avoid having to track down the doctest issues in #13364 right now, by providing a minimal Maxima spkg change here.


---

Comment by leif created at 2012-12-19 15:53:32

Replying to [comment:80 kcrisman]:
> By the way, could this be upgraded irrespective of upgrading Maxima?  (I mean for Sage proper.)  If all we need is to change the location of the Maxima library, maybe we could avoid having to track down the doctest issues in #13364 right now, by providing a minimal Maxima spkg change here.

To ease things, I'd then not hard-code the (new) name, but test whether `maxima.system.fasb` is present, and if so, copy that, otherwise (try to) copy `maxima.fasb`, or bail out if none of these is present.

(Something we should probably do at #13364 as well.)


---

Comment by dimpase created at 2012-12-19 16:33:57

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

Comment by jpflori created at 2012-12-19 16:51:04

Feel free to do so in another ticket, change dependencies here, update #13364 to be based on this new ticket, and remove dependency on this ECL ticket form #13364.


---

Comment by dimpase created at 2012-12-19 17:32:12

Replying to [comment:83 jpflori]:
> Feel free to do so in another ticket, change dependencies here, update #13364 to be based on this new ticket, and remove dependency on this ECL ticket form #13364.

I'd rather see this ticket brought to completion. I imagine it's just a small autoconf fix, right?
I'm adding to the ticket description a link to updated maxima 5.26 spkg.

Can one close #13324 as a duplicate?


---

Comment by dimpase created at 2012-12-19 17:32:12

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2012-12-19 17:32:23

Changing status from needs_review to needs_info.


---

Comment by jpflori created at 2012-12-19 17:43:35

I think that #13324 still needs_review and potential firther changes (no feedback from upstream yet on the uncaught segfault issue).

Closing #13324 would be similar to what I wanted to do for #12115 and #13137 except for the fact that #12115 was kind of trivial and got merged into #13137, whereas here we would merge a big (almost functional?) ticket into a simpler (but potentially more controversial) one.

Furthermore, as this one is only needed on Cygwin, I'm even more inclined to think it might be better to wait for #13324 to be properly merged, and then go with this one.
If you really want to use it, just download it and do so.

And I still think the change to Maxima spkg-install script should be done in an independent (and quite trivial) ticket called something like "let Maxima spkg properly install with different version of ECL", it would be merged really quicly, and then rebase #13364 to update Maxima on top of that new ticket.

With this approach people could just drop in different versions of ECl and ply with them.

Generally I feel that keeping issues, or even "independent" changes, into separated tickets is a good idea.


---

Comment by jpflori created at 2012-12-19 17:44:21

Yeah, and Jeroen ranted when I asked to close #12115 and merge it within #13137 and I understand his point :)


---

Comment by dimpase created at 2012-12-19 17:57:49

Replying to [comment:86 jpflori]:
> I think that #13324 still needs_review and potential firther changes (no feedback from upstream yet on the uncaught segfault issue).
> 
> Closing #13324 would be similar to what I wanted to do for #12115 and #13137 except for the fact that #12115 was kind of trivial and got merged into #13137, whereas here we would merge a big (almost functional?) ticket into a simpler (but potentially more controversial) one.

#13324 is partially duplicating #13364. The segfault one sees with Maxima is due to an infinite recursion in some Maxima code, as
is acknowledged on [maxima bug tracker, bug 2520](https://sourceforge.net/p/maxima/bugs/2520/). I am not sure ECL can be blamed for crashing on this.


---

Comment by jpflori created at 2012-12-19 18:01:30

As was demonstrated, other Lisp interpreters catch the error more gracefully.
I must say I don't really care, especially that when Maxima is fixed, there should be nothing to catch anymore, but if a fix is possible and is devised, we could include it in #13324 or a further ECL update where it belongs.


---

Comment by leif created at 2012-12-19 20:21:31

Replying to [comment:86 jpflori]:
> And I still think the change to Maxima spkg-install script should be done in an independent (and quite trivial) ticket called something like "let Maxima spkg properly install with different version of ECL", it would be merged really quicly, and then rebase #13364 to update Maxima on top of that new ticket.

Yep, that's what I was thinking of as well.  (Unless the Maxima guys [and probably we, too] are super-quick and fix all issues within the next few days...)


> With this approach people could just drop in different versions of ECl and ply with them.

Although I occasionally hear the contrary (e.g. "Why let LCalc build with different versions of PARI?"), we shouldn't establish unnecessary dependencies, so yes.




> Generally I feel that keeping issues, or even "independent" changes, into separated tickets is a good idea.

_Generally._  Unfortunately often N developers touch the "same" code (or spkgs) such that at least N-1 developers have to rebase their changes M<sub>N</sub> times, or the fixes just rotten and never get merged.


---

Comment by dimpase created at 2012-12-23 08:31:57

Replying to [comment:81 leif]:
> Replying to [comment:80 kcrisman]:
> > By the way, could this be upgraded irrespective of upgrading Maxima?  (I mean for Sage proper.)  If all we need is to change the location of the Maxima library, maybe we could avoid having to track down the doctest issues in #13364 right now, by providing a minimal Maxima spkg change here.
> 
> To ease things, I'd then not hard-code the (new) name, but test whether `maxima.system.fasb` is present, and if so, copy that, otherwise (try to) copy `maxima.fasb`, or bail out if none of these is present.

OK, this is now #13860

Please review!


---

Comment by kcrisman created at 2012-12-29 03:54:12

> OK, this is now #13860
> 
> Please review!

Apparently that has positive review now.  JP, do we really need to generate a smaller patch with "use matching autoconf", or is that unnecessary?  This ticket is currently "needs info" but it isn't clear to me what info is needed.  Is it really sage-pending on #13324, or is there something else we're trying to get feedback on?  Thanks.


---

Comment by jpflori created at 2013-01-04 10:53:40

Replying to [comment:93 kcrisman]:
> > OK, this is now #13860
> > 
> > Please review!
> 
> Apparently that has positive review now.  JP, do we really need to generate a smaller patch with "use matching autoconf", or is that unnecessary?  This ticket is currently "needs info" but it isn't clear to me what info is needed.  Is it really sage-pending on #13324, or is there something else we're trying to get feedback on?  Thanks.
I'd like to get upstream feedback on the import library changes and include an official patch rather mine.
I guess we'll have to wait for the end of the holidays for that :)


---

Comment by jpflori created at 2013-01-04 10:54:02

And inbetween we can already get #13324 merged...


---

Comment by kcrisman created at 2013-01-04 14:31:05

> And inbetween we can already get #13324 merged...
And maybe even #13364...


---

Comment by kcrisman created at 2013-01-14 17:08:50

> I'd like to get upstream feedback on the import library changes and include an official patch rather mine.
> I guess we'll have to wait for the end of the holidays for that :)
My holidays are done :)  And it does look like there has been some activity on the ECL list again.  But I think that's not important and we can all take a break, because...

Really I think there is no reason to wait on upstream; Sage does contribute upstream, but we still take care of our own.  Is there anything _else_ you would want to change here?  even the whole "generate smaller patch" thing seems less significant.  As far as I'm concerned, the current spkg is fine especially since the "dependencies" in Maxima and ECL are in/positive review.


---

Comment by kcrisman created at 2013-01-14 17:08:50

Changing status from needs_info to needs_review.


---

Comment by jpflori created at 2013-01-15 08:24:52

That's fair, I'll check the spkg is clean cause I don't really remember right now and report back here so someone motivated can put this as positive review (I guess you could as this is really only Cygwin (and MinGW) related and should have no effect on any other system).


---

Comment by jpflori created at 2013-01-15 08:35:46

Just a reminder for me, I should add a simple hack to take care of http://sourceforge.net/p/ecls/bugs/222/ in order to produce cleaner libs as well.


---

Comment by kcrisman created at 2013-01-15 14:29:46

> Just a reminder for me, I should add a simple hack to take care of http://sourceforge.net/p/ecls/bugs/222/ in order to produce cleaner libs as well.
Maybe that _can_ wait for upstream; I don't think it's necessary here and I don't know if I'll have the chance to test things as much now.


---

Comment by jpflori created at 2013-01-18 09:02:20

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

Comment by jdemeyer created at 2013-01-18 09:16:18

Replying to [comment:103 jpflori]:
> What would be your strategy Jeroen?
The plan is certainly to merge #13324 in sage-5.7.beta0.  Of course, unexpected problems can always appear, but so far the new ECL has passed all buildbot tests.

I don't quite understand how this ticket relates to #13324, as that is also about Cygwin...


---

Comment by jpflori created at 2013-01-18 09:49:07

#13324 was only about building ecl on Cygwin.
This ticket is about resolving a conflict between the main ecl library being called ecl.dll and the one for the ecl interface in Sage having the same name.
Indeed Windows cannot deal will that: the latter one should link to the former one but at runtime it resolves this dependency by linking back to itself because of the name collision...


---

Comment by jdemeyer created at 2013-01-18 10:24:27

Ideally, the `hg` history would be preserved so I prefer a proper rebase to #13324.  But let's wait until sage-5.7.beta0 is released.

In any case, this ticket still needs to be reviewed (without worrying about rebasing for now).


---

Comment by jdemeyer created at 2013-01-18 10:28:39

Concerning "autoconf": the autotools optional package should solve that problem.  Install that package in some Sage version (this doesn't have to be Cygwin), run a Sage shell and then run autoconf/automake/autowhatever from within that Sage shell.


---

Comment by jpflori created at 2013-01-18 10:31:01

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2013-01-18 10:31:01

Yeah I'm aware of that... and you just made me realize that's what I originally intended to do and forgot to do this morning although it's written evreywhere in this ticket.


---

Comment by jpflori created at 2013-01-18 10:40:19

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2013-01-18 10:40:19

Done (I'm aware about the not changed date in SPKG.txt but whatever).


---

Comment by jdemeyer created at 2013-01-18 10:45:53

Beware with timestamps when patching `configure`!

You must ensure that the timestamp of `configure` is more recent than that of the various `.in` files, otherwise `make` might want to rerun `autoconf`, leading to potential failures.

One solution is to edit the patch file such that `configure` comes last, as `patch` processes files in order.  Or manually `touch configure` afterwards.


---

Comment by jpflori created at 2013-01-18 10:49:47

True indeed, doing that now, sorry for being that lame on this one.


---

Comment by jpflori created at 2013-01-18 10:53:53

Should be ok now (I've even taken the time to actually try to build it (on Linux)).


---

Attachment

Spkg diff, for review only.


---

Comment by kcrisman created at 2013-01-18 13:21:53

Grmph, the train's wifi cut me off...

Short version: is there anything actually different from the previous spkg that did work?  I also can't see any configure changes in the patch, maybe that's a good thing.


---

Comment by kcrisman created at 2013-01-22 16:49:30

Okay, all relevant tests pass with this (and a rebuilt Maxima) on Mac.  I say positive review, assuming JP clarifies my dumb comment about configure and he confirms that he fixed the timestamp issue (I think he is saying that he did in comment:112).


---

Comment by jpflori created at 2013-01-23 09:54:22

The implib.patch I posted here only touches the autotools file (you then need to somehow regenerate the build system, let's say autoreconf -i).

I've done this for the spkg, so the one included in the spkg (and in the diff posted here) is the same plus the changes to the build system (after runing autoreconf -i using matching versions of autotools).

And I've indeed reordered the spkg's patch hunks so that autotools files are patched before the build system one to ensure that autotools does not decide to regenerate everything on the fly.


---

Comment by kcrisman created at 2013-01-24 19:27:29

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-01-24 19:27:29

I can no longer check this due to horrible BLODA issues but my comment:115 stands, and if Jeroen agrees that these are stamped in the correct order, then let's get this in, since it does work.


---

Comment by kcrisman created at 2013-01-24 21:07:21

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

Comment by jpflori created at 2013-01-24 23:32:53

That's expected, the first patch from http://trac.sagemath.org/sage_trac/ticket/13324 should fix that.


---

Comment by kcrisman created at 2013-01-25 01:20:26

Hmm, that sounds familiar.  Great.


---

Comment by jdemeyer created at 2013-01-26 09:52:37

Resolution: fixed


---

Comment by dimpase created at 2016-03-21 12:03:25

How did you report this?
it ought to be reported here: https://gitlab.com/embeddable-common-lisp/ecl/issues


---

Comment by jpflori created at 2016-03-21 12:06:34

IIRC this was reported on sourceforge.net where ECL used to be hosted.


---

Comment by dimpase created at 2016-03-21 12:18:42

well, yes, but it seems to be lost...


---

Comment by jpflori created at 2016-03-21 12:27:37

At least there is a copy of the discussion on the former ECL list here:
* https://www.mail-archive.com/ecls-list`@`lists.sourceforge.net/msg01978.html
(and one in my mailbox...)


---

Comment by jdemeyer created at 2016-03-21 12:48:16

Could you repost that bug report to upstream?


---

Comment by jpflori created at 2016-03-21 13:01:28

Done:
* https://gitlab.com/embeddable-common-lisp/ecl/issues/235
