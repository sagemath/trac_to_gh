# Issue 9760: Adjust spkg/standard/deps to build Python before zn_poly

archive/issues_009760.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  drkirkby leif pjeremy\n\nZn_poly's `spkg-install` is not a Python script (cf. #9507), but its build system calls a Python script `zn_poly-*/src/makemakefile.py`.  Updating `spkg/standard/deps` to ensure that Python is built first should prevent build errors in which `spkg/logs/zn_poly-*.log` ends with\n\n```\ngcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu4)\n****************************************************\npython: error while loading shared libraries: libpython2.6.so.1.0: cannot open shared object file: No such file or directory\nmake[2]: Entering directory `/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3.alpha1-ldd/spkg/build/zn_poly-0.9.p5/src'\nmake[2]: warning: jobserver unavailable: using -j1.  Add `+' to parent make rule.\nmake[2]: Nothing to be done for `tune'.\nmake[2]: Leaving directory `/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3.alpha1-ldd/spkg/build/zn_poly-0.9.p5/src'\n./spkg-install: line 59: tune/tune: No such file or directory\nError running tune program.\n\nreal    0m0.014s\nuser    0m0.010s\nsys     0m0.000s\nsage: An error occurred while installing zn_poly-0.9.p5\n[...]\n```\n\n\nRelated: [comment:ticket:9368:14 Comment 14ff] at #9368.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9761\n\n",
    "created_at": "2010-08-18T07:54:01Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Adjust spkg/standard/deps to build Python before zn_poly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9760",
    "user": "mpatel"
}
```
Assignee: GeorgSWeber

CC:  drkirkby leif pjeremy

Zn_poly's `spkg-install` is not a Python script (cf. #9507), but its build system calls a Python script `zn_poly-*/src/makemakefile.py`.  Updating `spkg/standard/deps` to ensure that Python is built first should prevent build errors in which `spkg/logs/zn_poly-*.log` ends with

```
gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu4)
****************************************************
python: error while loading shared libraries: libpython2.6.so.1.0: cannot open shared object file: No such file or directory
make[2]: Entering directory `/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3.alpha1-ldd/spkg/build/zn_poly-0.9.p5/src'
make[2]: warning: jobserver unavailable: using -j1.  Add `+' to parent make rule.
make[2]: Nothing to be done for `tune'.
make[2]: Leaving directory `/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3.alpha1-ldd/spkg/build/zn_poly-0.9.p5/src'
./spkg-install: line 59: tune/tune: No such file or directory
Error running tune program.

real    0m0.014s
user    0m0.010s
sys     0m0.000s
sage: An error occurred while installing zn_poly-0.9.p5
[...]
```


Related: [comment:ticket:9368:14 Comment 14ff] at #9368.

Issue created by migration from https://trac.sagemath.org/ticket/9761





---

archive/issue_comments_095611.json:
```json
{
    "body": "Actually, the error message above appears to stem from my having a `SAGE_LOCAL/bin` in the `PATH` but not a corresponding `SAGE_LOCAL/lib` in the `LD_LIBRARY_PATH`.  I've fixed this by keeping `SAGE_LOCAL/*` out of both path variables.\n\nAnyway, if an existing [system-wide] Python installation is not a Sage build requirement, I think we should still update `deps`.  Or am I mistaken?",
    "created_at": "2010-08-18T08:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95611",
    "user": "mpatel"
}
```

Actually, the error message above appears to stem from my having a `SAGE_LOCAL/bin` in the `PATH` but not a corresponding `SAGE_LOCAL/lib` in the `LD_LIBRARY_PATH`.  I've fixed this by keeping `SAGE_LOCAL/*` out of both path variables.

Anyway, if an existing [system-wide] Python installation is not a Sage build requirement, I think we should still update `deps`.  Or am I mistaken?



---

archive/issue_comments_095612.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> Actually, the error message above appears to stem from my having a `SAGE_LOCAL/bin` in the `PATH` but not a corresponding `SAGE_LOCAL/lib` in the `LD_LIBRARY_PATH`.  I've fixed this by keeping `SAGE_LOCAL/*` out of both path variables.\n> \n> Anyway, if an existing [system-wide] Python installation is not a Sage build requirement, I think we should still update `deps`.  Or am I mistaken?\n\nI agree with you 100%. If zn_poly requires Python then we must ensure Python is built first. \n\nI think this should be a blocker myself, but you are the release manager, so downgrade it if you wish. There are a number of reports of a system Python causing build problems, so in some cases actually disabling Python is necessary (see #9209).\n\nThere are two other very trivial fixes to deps which are more cosmetic than anything else, but worth adding, as they aid clarity. These are #9637 and #9464 and we might as well fix all three at once. \n\nAlso, SPKG.txt for zn_poly should be updated to reflect the fact there is a dependency on Python. That's a minor issue, but one worth addressing. That is now #9762. \n\nI could make all these changes by around 0100 GMT on Thursday 19th August if you wanted, or could review them sooner if someone else did them. But I've got a lot to do this afternoon, and don't have time to fix them right now. I'm not at home, so don't have my workstation by me, which makes testing things a bit more difficult. \n\nDave",
    "created_at": "2010-08-18T11:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95612",
    "user": "drkirkby"
}
```

Replying to [comment:1 mpatel]:
> Actually, the error message above appears to stem from my having a `SAGE_LOCAL/bin` in the `PATH` but not a corresponding `SAGE_LOCAL/lib` in the `LD_LIBRARY_PATH`.  I've fixed this by keeping `SAGE_LOCAL/*` out of both path variables.
> 
> Anyway, if an existing [system-wide] Python installation is not a Sage build requirement, I think we should still update `deps`.  Or am I mistaken?

I agree with you 100%. If zn_poly requires Python then we must ensure Python is built first. 

I think this should be a blocker myself, but you are the release manager, so downgrade it if you wish. There are a number of reports of a system Python causing build problems, so in some cases actually disabling Python is necessary (see #9209).

There are two other very trivial fixes to deps which are more cosmetic than anything else, but worth adding, as they aid clarity. These are #9637 and #9464 and we might as well fix all three at once. 

Also, SPKG.txt for zn_poly should be updated to reflect the fact there is a dependency on Python. That's a minor issue, but one worth addressing. That is now #9762. 

I could make all these changes by around 0100 GMT on Thursday 19th August if you wanted, or could review them sooner if someone else did them. But I've got a lot to do this afternoon, and don't have time to fix them right now. I'm not at home, so don't have my workstation by me, which makes testing things a bit more difficult. 

Dave



---

archive/issue_comments_095613.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-08-18T11:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95613",
    "user": "drkirkby"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_095614.json:
```json
{
    "body": "Is this documented in zn_poly's `SPKG.txt`?\n\nIf zn_poly('s build system) depends on Python, `spkg/standard/deps` should of course reflect this; we could in addition ensure in its `spkg-install` that the current Sage's Python is already available; but see below (w.r.t. *Sage's*).\n\nI though don't like making packages depend on Python just because some developers appear to be unable or unwilling to write shell scripts instead; the Fortran spkg here is IMHO an especially odd example, since on most systems it's a dummy package, but other packages have to wait until Sage's Python is ready to actually do nothing. (I would completely drop it from the standard distribution; shipping binary executables - in a *source* tarball! - isn't nice either.)\n\nBtw, William's Fortran problem on bsd.math was (also) due to a *broken* Python installation/misconfigured environment.\n\nThe long-term solution to such should be to *generate* the Makefile (including deps) in/after Sage's configure. Then we could omit some dependencies (e.g. because a system-wide Python is usable, too), drop [the build of] spkgs like Cephes completely on all systems but Cygwin, and remove ugly things like `$PIPESTATUS`.\nSo we should take care not to make changes to lots of spkgs we would later have to revert/change, e.g. checking for `$SAGE_LOCAL/bin/python`; we could use properly set environment variables instead.\n\nAlso, `spkg/standard/deps` (or a file it is generated from, which I'd prefer) should be under revision control.",
    "created_at": "2010-08-18T12:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95614",
    "user": "leif"
}
```

Is this documented in zn_poly's `SPKG.txt`?

If zn_poly('s build system) depends on Python, `spkg/standard/deps` should of course reflect this; we could in addition ensure in its `spkg-install` that the current Sage's Python is already available; but see below (w.r.t. *Sage's*).

I though don't like making packages depend on Python just because some developers appear to be unable or unwilling to write shell scripts instead; the Fortran spkg here is IMHO an especially odd example, since on most systems it's a dummy package, but other packages have to wait until Sage's Python is ready to actually do nothing. (I would completely drop it from the standard distribution; shipping binary executables - in a *source* tarball! - isn't nice either.)

Btw, William's Fortran problem on bsd.math was (also) due to a *broken* Python installation/misconfigured environment.

The long-term solution to such should be to *generate* the Makefile (including deps) in/after Sage's configure. Then we could omit some dependencies (e.g. because a system-wide Python is usable, too), drop [the build of] spkgs like Cephes completely on all systems but Cygwin, and remove ugly things like `$PIPESTATUS`.
So we should take care not to make changes to lots of spkgs we would later have to revert/change, e.g. checking for `$SAGE_LOCAL/bin/python`; we could use properly set environment variables instead.

Also, `spkg/standard/deps` (or a file it is generated from, which I'd prefer) should be under revision control.



---

archive/issue_comments_095615.json:
```json
{
    "body": "Concurrent posting... :)\n\nYes Dave, perhaps create a meta ticket for missing dependencies, (currently) referencing all three changes, and providing a cumulative patch to `deps`, such that only one ticket has to be merged (the others afterwards closed as \"duplicates\").",
    "created_at": "2010-08-18T12:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95615",
    "user": "leif"
}
```

Concurrent posting... :)

Yes Dave, perhaps create a meta ticket for missing dependencies, (currently) referencing all three changes, and providing a cumulative patch to `deps`, such that only one ticket has to be merged (the others afterwards closed as "duplicates").



---

archive/issue_comments_095616.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> Is this documented in zn_poly's `SPKG.txt`?\n\nNo, but I've created a ticket for that - #9762. That's a low-priority issue. \n\n> I though don't like making packages depend on Python just because some developers appear to be unable or unwilling to write shell scripts instead; \n\nI agree. But this is not a spkg-install that depends on Python - it is the upstream source code in a file well hidden. So short of patching the upstream source (which would unwise IMHO), we can't avoid it. \n\nIn the case of ATLAS for example, there's a trivial Python spkg-install which calls a huge bash script. I'd like to see that trivial bit of Python converted to a shell script, then we could remove the Python dependency. But the zn_poly issue is different. \n\n> Btw, William's Fortran problem on bsd.math was (also) due to a *broken* Python installation/misconfigured environment.\n\nWilliam seems quite happy to make Python a perquisite for building Sage - something I personally find rather unwise, but he leads the project. I hope enough of us can convince him this is unwise!\n\n> Also, `spkg/standard/deps` (or a file it is generated from, which I'd prefer) should be under revision control.\n\nAgreed. There's a ticket for that I believe. \n\nAnyway, I think the Python dependency should be added to zn_poly. But given there are two other very safe /trivial changes to deps, it would be sensible to do them all at once. We can do it on this ticket I feel. I just don't have time for another 12 hours or so, but can review it if someone else makes the changes. \n\nDave",
    "created_at": "2010-08-18T12:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95616",
    "user": "drkirkby"
}
```

Replying to [comment:4 leif]:
> Is this documented in zn_poly's `SPKG.txt`?

No, but I've created a ticket for that - #9762. That's a low-priority issue. 

> I though don't like making packages depend on Python just because some developers appear to be unable or unwilling to write shell scripts instead; 

I agree. But this is not a spkg-install that depends on Python - it is the upstream source code in a file well hidden. So short of patching the upstream source (which would unwise IMHO), we can't avoid it. 

In the case of ATLAS for example, there's a trivial Python spkg-install which calls a huge bash script. I'd like to see that trivial bit of Python converted to a shell script, then we could remove the Python dependency. But the zn_poly issue is different. 

> Btw, William's Fortran problem on bsd.math was (also) due to a *broken* Python installation/misconfigured environment.

William seems quite happy to make Python a perquisite for building Sage - something I personally find rather unwise, but he leads the project. I hope enough of us can convince him this is unwise!

> Also, `spkg/standard/deps` (or a file it is generated from, which I'd prefer) should be under revision control.

Agreed. There's a ticket for that I believe. 

Anyway, I think the Python dependency should be added to zn_poly. But given there are two other very safe /trivial changes to deps, it would be sensible to do them all at once. We can do it on this ticket I feel. I just don't have time for another 12 hours or so, but can review it if someone else makes the changes. 

Dave



---

archive/issue_comments_095617.json:
```json
{
    "body": "I'd suggest adding a target `SOME_PYTHON` (which currently depends on Sage's Python), and make zn_poly and Fortran depend on **that**.\n\nThis should clarify that (some) Python is needed during the spkg's build process, but not necessarily Sage's one, as opposed to spkgs that really install something into Sage's Python installation, or have to reference it (hard-coded) for later use.",
    "created_at": "2010-08-18T12:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95617",
    "user": "leif"
}
```

I'd suggest adding a target `SOME_PYTHON` (which currently depends on Sage's Python), and make zn_poly and Fortran depend on **that**.

This should clarify that (some) Python is needed during the spkg's build process, but not necessarily Sage's one, as opposed to spkgs that really install something into Sage's Python installation, or have to reference it (hard-coded) for later use.



---

archive/issue_comments_095618.json:
```json
{
    "body": "I'm not sure that this should be a blocker, since the problem could be viewed as a misconfigured PATH.  Furthermore, as Dave says, William is in favor of making a system-wide Python perhaps a prerequisite for building Sage.  I think this question should be settled at some point in sage-devel.  Then if people decide that Python should be a prerequisite, it should be tested for in prereqs and it should be documented somewhere.\n\nFor now, though, I don't think it hurts making zn_poly depend on python.\n\n> I though don't like making packages depend on Python just because some developers appear to be unable or unwilling to write shell scripts instead.\n\nWhy not? I don't like arbitrarily deciding that people shouldn't write Python scripts. For me, writing, reading, and debugging Python scripts is much easier than doing the same for shell scripts, and I'll probably do a better job working in Python.  Why put up barriers for people to contribute, especially when so many contributors are mathematicians who don't particularly want to learn to write shell scripts and who can't remember, for example, whether to use \"-a\" or \"&&\"?",
    "created_at": "2010-08-18T14:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95618",
    "user": "jhpalmieri"
}
```

I'm not sure that this should be a blocker, since the problem could be viewed as a misconfigured PATH.  Furthermore, as Dave says, William is in favor of making a system-wide Python perhaps a prerequisite for building Sage.  I think this question should be settled at some point in sage-devel.  Then if people decide that Python should be a prerequisite, it should be tested for in prereqs and it should be documented somewhere.

For now, though, I don't think it hurts making zn_poly depend on python.

> I though don't like making packages depend on Python just because some developers appear to be unable or unwilling to write shell scripts instead.

Why not? I don't like arbitrarily deciding that people shouldn't write Python scripts. For me, writing, reading, and debugging Python scripts is much easier than doing the same for shell scripts, and I'll probably do a better job working in Python.  Why put up barriers for people to contribute, especially when so many contributors are mathematicians who don't particularly want to learn to write shell scripts and who can't remember, for example, whether to use "-a" or "&&"?



---

archive/issue_comments_095619.json:
```json
{
    "body": "`src/configure` is nice:\n\n```sh\n#!/bin/sh\n\n#\n# This script just calls makemakefile.py.\n# See that file for the real configure script.\n#\n\nif test $# -ne 0\nthen\n   python makemakefile.py \"$@\" > makefile\nelse\n   python makemakefile.py > makefile\nfi\n```\n\n\nLooking at that Python script:\n\n```sh\n~/Sage/spkgs/zn_poly-0.9.p5$ wc -l src/makemakefile.py \n274 src/makemakefile.py\n~/Sage/spkgs/zn_poly-0.9.p5$ grep -c print src/makemakefile.py \n119\n~/Sage/spkgs/zn_poly-0.9.p5$ grep -c \"^#\" src/makemakefile.py \n31\n~/Sage/spkgs/zn_poly-0.9.p5$ grep -c \"^$\" src/makemakefile.py \n47\n```\n\n\nMuch of the rest just defines lists of strings (filenames), and afterwards prepends some directory/path to each of the list elements. Then some strings are concatenated, partly with case distinctions. (Ok, option parsing is another job done, but most of it should be in a `Makefile.in`.)\n\nI wonder if we could simply replace this by (making use of) a pregenerated file for the purpose of Sage, using some shell variables. IMHO requiring Python here is like requiring autotools to be present.\n\nBtw, from `spkg-install` it is pretty clear that this package requires Python:\n\n```sh\n$ grep makemake spkg-install \n   cp patches/makemakefile.py src/makemakefile.py\n   sed 's/-soname/-h/g' src/makemakefile.py > /tmp/makemakefile.py.$$\n   mv /tmp/makemakefile.py.$$ src/makemakefile.py \n```\n\n\nJust my needless 2 cents...",
    "created_at": "2010-08-18T14:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95619",
    "user": "leif"
}
```

`src/configure` is nice:

```sh
#!/bin/sh

#
# This script just calls makemakefile.py.
# See that file for the real configure script.
#

if test $# -ne 0
then
   python makemakefile.py "$@" > makefile
else
   python makemakefile.py > makefile
fi
```


Looking at that Python script:

```sh
~/Sage/spkgs/zn_poly-0.9.p5$ wc -l src/makemakefile.py 
274 src/makemakefile.py
~/Sage/spkgs/zn_poly-0.9.p5$ grep -c print src/makemakefile.py 
119
~/Sage/spkgs/zn_poly-0.9.p5$ grep -c "^#" src/makemakefile.py 
31
~/Sage/spkgs/zn_poly-0.9.p5$ grep -c "^$" src/makemakefile.py 
47
```


Much of the rest just defines lists of strings (filenames), and afterwards prepends some directory/path to each of the list elements. Then some strings are concatenated, partly with case distinctions. (Ok, option parsing is another job done, but most of it should be in a `Makefile.in`.)

I wonder if we could simply replace this by (making use of) a pregenerated file for the purpose of Sage, using some shell variables. IMHO requiring Python here is like requiring autotools to be present.

Btw, from `spkg-install` it is pretty clear that this package requires Python:

```sh
$ grep makemake spkg-install 
   cp patches/makemakefile.py src/makemakefile.py
   sed 's/-soname/-h/g' src/makemakefile.py > /tmp/makemakefile.py.$$
   mv /tmp/makemakefile.py.$$ src/makemakefile.py 
```


Just my needless 2 cents...



---

archive/issue_comments_095620.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> I'm not sure that this should be a blocker, since the problem could be viewed as a misconfigured PATH.\n\nWell, if *no* system Python was available, the build would (or could) break, too.\n\n> Furthermore, as Dave says, William is in favor of making a system-wide Python perhaps a prerequisite for building Sage.\n\nI wouldn't mind, or perhaps even appreciate that. Like gcc requiring a C compiler to build...\n(I though wonder if we could then drop the Python package from Sage, at least if a *suitable* version is already present.)\n\n> > I though don't like making packages depend on Python just because some developers appear to be unable or unwilling to write shell scripts instead.\n> \n> Why not? \n\nBecause - currently - Python is **not** a prerequisite for building Sage.\n\n> I don't like arbitrarily deciding that people shouldn't write Python scripts. For me, writing, reading, and debugging Python scripts is much easier than doing the same for shell scripts, and I'll probably do a better job working in Python.\n\nI didn't mean that; in this case, the build process, IMHO one should use tools that are designed for the specific purpose.\n\n> Why put up barriers for people to contribute, especially when so many contributors are mathematicians who don't particularly want to learn to write shell scripts and who can't remember, for example, whether to use \"-a\" or \"&&\"?\n\nThere are some Sage developers that aren't mathematicians; hopefully these could give help with the non-mathematical parts. (Collaboration between different disciplines seems to be a never-ending problem...)\n\nIt's easier to read Makefiles (and for me, e.g. `configure` scripts, too) than arbitrary Python/Ruby/Perl/BASIC?/... scripts, especially when people feel they have to reinvent their own wheel, i.e., not even using libraries or packages that already achieve the same in a more standard way (though I'm personally not very happy with e.g. SCons).\n\nOnce Sage has \"boot-strapped\", everybody is free to do arbitrary things in the languages Sage supports...",
    "created_at": "2010-08-18T15:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95620",
    "user": "leif"
}
```

Replying to [comment:8 jhpalmieri]:
> I'm not sure that this should be a blocker, since the problem could be viewed as a misconfigured PATH.

Well, if *no* system Python was available, the build would (or could) break, too.

> Furthermore, as Dave says, William is in favor of making a system-wide Python perhaps a prerequisite for building Sage.

I wouldn't mind, or perhaps even appreciate that. Like gcc requiring a C compiler to build...
(I though wonder if we could then drop the Python package from Sage, at least if a *suitable* version is already present.)

> > I though don't like making packages depend on Python just because some developers appear to be unable or unwilling to write shell scripts instead.
> 
> Why not? 

Because - currently - Python is **not** a prerequisite for building Sage.

> I don't like arbitrarily deciding that people shouldn't write Python scripts. For me, writing, reading, and debugging Python scripts is much easier than doing the same for shell scripts, and I'll probably do a better job working in Python.

I didn't mean that; in this case, the build process, IMHO one should use tools that are designed for the specific purpose.

> Why put up barriers for people to contribute, especially when so many contributors are mathematicians who don't particularly want to learn to write shell scripts and who can't remember, for example, whether to use "-a" or "&&"?

There are some Sage developers that aren't mathematicians; hopefully these could give help with the non-mathematical parts. (Collaboration between different disciplines seems to be a never-ending problem...)

It's easier to read Makefiles (and for me, e.g. `configure` scripts, too) than arbitrary Python/Ruby/Perl/BASIC?/... scripts, especially when people feel they have to reinvent their own wheel, i.e., not even using libraries or packages that already achieve the same in a more standard way (though I'm personally not very happy with e.g. SCons).

Once Sage has "boot-strapped", everybody is free to do arbitrary things in the languages Sage supports...



---

archive/issue_comments_095621.json:
```json
{
    "body": "Replying to [comment:6 drkirkby]:\n> In the case of ATLAS for example, there's a trivial Python spkg-install which calls a huge bash script. I'd like to see that trivial bit of Python converted to a shell script, then we could remove the Python dependency.\n\nOuch... \n\nI believe I've never before looked at Sage's *ATLAS* build scripts. (I did not even know the repetition of build attempts originated from Sage itself.) There are *three* Python and some (sub-)shell scripts, and there's even a Perl script. 8|\n\nThis should **really** be cleaned up, IMHO by completely rewriting `spkg-install` from scratch, as a plain shell script.",
    "created_at": "2010-08-18T16:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95621",
    "user": "leif"
}
```

Replying to [comment:6 drkirkby]:
> In the case of ATLAS for example, there's a trivial Python spkg-install which calls a huge bash script. I'd like to see that trivial bit of Python converted to a shell script, then we could remove the Python dependency.

Ouch... 

I believe I've never before looked at Sage's *ATLAS* build scripts. (I did not even know the repetition of build attempts originated from Sage itself.) There are *three* Python and some (sub-)shell scripts, and there's even a Perl script. 8|

This should **really** be cleaned up, IMHO by completely rewriting `spkg-install` from scratch, as a plain shell script.



---

archive/issue_comments_095622.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> I'm not sure that this should be a blocker, since the problem could be viewed as a misconfigured PATH. \n\nI'm writing this quick - due in a meeting soon. \n\nI believe it should be a blocker as Python is not listed as a prequisite for building Sage. So zn_poly could fail if Python is not installed. That, in my opinion is good enough reason. \n\nOther reasons are\n* It's a trivial fix.\n* Mis-configured Pythons do exist - William's on bsd.math was one example. \n* I also happen to be aware of cases where having a Python in /usr/local can cause Sage to mis-behave. I think I have posted a link to the ticket on here, where this is documented. Both myself and a Linux user has seen this.\n\nBut the main reason is simply that Python is not a perquisite. All other issues are secondary in comparison to that. \n\nDave",
    "created_at": "2010-08-18T16:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95622",
    "user": "drkirkby"
}
```

Replying to [comment:8 jhpalmieri]:
> I'm not sure that this should be a blocker, since the problem could be viewed as a misconfigured PATH. 

I'm writing this quick - due in a meeting soon. 

I believe it should be a blocker as Python is not listed as a prequisite for building Sage. So zn_poly could fail if Python is not installed. That, in my opinion is good enough reason. 

Other reasons are
* It's a trivial fix.
* Mis-configured Pythons do exist - William's on bsd.math was one example. 
* I also happen to be aware of cases where having a Python in /usr/local can cause Sage to mis-behave. I think I have posted a link to the ticket on here, where this is documented. Both myself and a Linux user has seen this.

But the main reason is simply that Python is not a perquisite. All other issues are secondary in comparison to that. 

Dave



---

archive/issue_comments_095623.json:
```json
{
    "body": "Let's keep \"adding Python to zn_poly's build dependencies\" as a 4.5.3 blocker.  Rolling #9637 and #9464 into a `deps` patch here is OK with me.\n\nJust to check on #9464: Are we generally going to be explicit about all dependencies or just potential sources of confusion?",
    "created_at": "2010-08-18T22:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95623",
    "user": "mpatel"
}
```

Let's keep "adding Python to zn_poly's build dependencies" as a 4.5.3 blocker.  Rolling #9637 and #9464 into a `deps` patch here is OK with me.

Just to check on #9464: Are we generally going to be explicit about all dependencies or just potential sources of confusion?



---

archive/issue_comments_095624.json:
```json
{
    "body": "I'm attaching a patch (unified diff, not Mercurial), which addresses three issues. \n\n* Makes ZNPOLY dependent on PYTHON - the point of this ticket. \n* Makes SAGETEX depend on BASE. Not strictly necessary, but its the only package which does not list BASE specifically. This is #9637\n* Make R depend on FORTRAN. This is not strictly necessary, as it is implied by a very convoluted chain rule, but this makes it more obvious. This is #9464\n\nIf this gets merged, both #9637 and #9464 can be closed.\n\nSince `spkg/standard/deps` is not under revision control, this will have to be merged manually. \n\nTo answer John's point, I don't have a strong view on that either way, but certainly if there is any potential for confusion, then I think we should list them explicitly. \n\nDave",
    "created_at": "2010-08-18T23:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95624",
    "user": "drkirkby"
}
```

I'm attaching a patch (unified diff, not Mercurial), which addresses three issues. 

* Makes ZNPOLY dependent on PYTHON - the point of this ticket. 
* Makes SAGETEX depend on BASE. Not strictly necessary, but its the only package which does not list BASE specifically. This is #9637
* Make R depend on FORTRAN. This is not strictly necessary, as it is implied by a very convoluted chain rule, but this makes it more obvious. This is #9464

If this gets merged, both #9637 and #9464 can be closed.

Since `spkg/standard/deps` is not under revision control, this will have to be merged manually. 

To answer John's point, I don't have a strong view on that either way, but certainly if there is any potential for confusion, then I think we should list them explicitly. 

Dave



---

archive/issue_comments_095625.json:
```json
{
    "body": "New spkg/standard/deps, which resolves this ticket and two minor issues",
    "created_at": "2010-08-18T23:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95625",
    "user": "drkirkby"
}
```

New spkg/standard/deps, which resolves this ticket and two minor issues



---

archive/issue_comments_095626.json:
```json
{
    "body": "Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9761/deps.diff) by drkirkby created at 2010-08-18 23:10:31\n\nDifferences between the new 'deps' file and that in sage-4.5.3.alpha1",
    "created_at": "2010-08-18T23:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95626",
    "user": "drkirkby"
}
```

Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9761/deps.diff) by drkirkby created at 2010-08-18 23:10:31

Differences between the new 'deps' file and that in sage-4.5.3.alpha1



---

archive/issue_comments_095627.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-18T23:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95627",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095628.json:
```json
{
    "body": "Replying to [comment:13 mpatel]:\n> Just to check on #9464: Are we generally going to be explicit about all dependencies or just potential sources of confusion?\n\nI'd say making direct dependencies explicit is not a bad idea. In addition, as said above, I'd prefer differentiating between tools/packages etc. needed during build and those that are necessary for later operation, at least e.g. for Python.\n\nOf course this could be subdivided further, but does not yet make many sense.\n\n(All standard packages currently depend on `$BASE` rather than a set of the actually required things; this is also not very informative, but I wouldn't change that at the moment.)",
    "created_at": "2010-08-18T23:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95628",
    "user": "leif"
}
```

Replying to [comment:13 mpatel]:
> Just to check on #9464: Are we generally going to be explicit about all dependencies or just potential sources of confusion?

I'd say making direct dependencies explicit is not a bad idea. In addition, as said above, I'd prefer differentiating between tools/packages etc. needed during build and those that are necessary for later operation, at least e.g. for Python.

Of course this could be subdivided further, but does not yet make many sense.

(All standard packages currently depend on `$BASE` rather than a set of the actually required things; this is also not very informative, but I wouldn't change that at the moment.)



---

archive/issue_comments_095629.json:
```json
{
    "body": "Sorry, \n\nI see it was Mitesh's point about whether we should generally be explicit about all dependencies or just potential sources of confusion - not John's. \n\nI'm unsure what to say about that one. I supposed putting them all in would avoid confusion. It makes the file bigger, and the mere fact of making the changes could introduce a bug.\n\nA difficult one - I'll *sit on the fence*!\n\nDave",
    "created_at": "2010-08-18T23:24:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95629",
    "user": "drkirkby"
}
```

Sorry, 

I see it was Mitesh's point about whether we should generally be explicit about all dependencies or just potential sources of confusion - not John's. 

I'm unsure what to say about that one. I supposed putting them all in would avoid confusion. It makes the file bigger, and the mere fact of making the changes could introduce a bug.

A difficult one - I'll *sit on the fence*!

Dave



---

archive/issue_comments_095630.json:
```json
{
    "body": "I would have liked a `SOME_PYTHON` target, but the comment on zn_poly's rule should be enough for the moment.\n\nI've verified that the attached `deps` file is actually 4.5.3.alpha1's with `deps.diff`'s changes applied, so **positive review**.",
    "created_at": "2010-08-18T23:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95630",
    "user": "leif"
}
```

I would have liked a `SOME_PYTHON` target, but the comment on zn_poly's rule should be enough for the moment.

I've verified that the attached `deps` file is actually 4.5.3.alpha1's with `deps.diff`'s changes applied, so **positive review**.



---

archive/issue_comments_095631.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-18T23:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95631",
    "user": "leif"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095632.json:
```json
{
    "body": "Replying to [comment:19 leif]:\n> I would have liked a `SOME_PYTHON` target, but the comment on zn_poly's rule should be enough for the moment.\n\nI'm not sure a `SOME_PYTHON` target is a good idea myself. But anyway, that is **far** outside the scope of this ticket. Such a change needs discussion on sage-devel - not a trac ticket. \n\n> I've verified that the attached `deps` file is actually 4.5.3.alpha1's with `deps.diff`'s changes applied, so **positive review**.\n\nThank you for the positive review Leif. \n\nIs there any chance you could complete your review of #9603? In return, I'll fix #9762, which you clearly thought was more important than me! Then we both get some changes we want. \n\nDave",
    "created_at": "2010-08-19T00:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95632",
    "user": "drkirkby"
}
```

Replying to [comment:19 leif]:
> I would have liked a `SOME_PYTHON` target, but the comment on zn_poly's rule should be enough for the moment.

I'm not sure a `SOME_PYTHON` target is a good idea myself. But anyway, that is **far** outside the scope of this ticket. Such a change needs discussion on sage-devel - not a trac ticket. 

> I've verified that the attached `deps` file is actually 4.5.3.alpha1's with `deps.diff`'s changes applied, so **positive review**.

Thank you for the positive review Leif. 

Is there any chance you could complete your review of #9603? In return, I'll fix #9762, which you clearly thought was more important than me! Then we both get some changes we want. 

Dave



---

archive/issue_comments_095633.json:
```json
{
    "body": "Replying to [comment:21 drkirkby]:\n> Replying to [comment:19 leif]:\n> > I would have liked a `SOME_PYTHON` target, but the comment on zn_poly's rule should be enough for the moment.\n> \n> I'm not sure a `SOME_PYTHON` target is a good idea myself. But anyway, that is **far** outside the scope of this ticket. Such a change needs discussion on sage-devel - not a trac ticket. \n\nFor now, I just meant:\n\n```diff\n--- deps.orig\t2010-08-19 01:30:33.000000000 +0200\n+++ deps\t2010-08-19 03:00:48.000000000 +0200\n@@ -129,6 +129,12 @@\n \t\t\t $(INST)/$(DIR)\n \t$(INSTALL) \"$(SAGE_SPKG) $(SAGE_SCRIPTS) 2>&1\" \"tee -a $(SAGE_LOGS)/$(SAGE_SCRIPTS).log\"\n \n+# A (perhaps system-wide) Python that's only used for scripting\n+# in the build process of a Sage package:\n+some_python: $(INST)/$(PYTHON)\n+\t# We currently only use Sage's Python, even if another\n+\t# (functional) Python is already present.\n+\n ########################################\n # Building normal packages\n ########################################\n@@ -374,7 +380,7 @@\n \n # zn_poly really does depend on Python, despite this is far from obvious.\n # The 'configure' script in zn_poly calls Python to make a 'makefile'\n-$(INST)/$(ZNPOLY): $(BASE) $(INST)/$(MPIR) $(INST)/$(PYTHON)\n+$(INST)/$(ZNPOLY): $(BASE) $(INST)/$(MPIR) some_python\n \t$(INSTALL) \"$(SAGE_SPKG) $(ZNPOLY) 2>&1\" \"tee -a $(SAGE_LOGS)/$(ZNPOLY).log\"\n \n # setuptools forgets to update easy-install.pth during parallel\n@@ -468,7 +474,7 @@\n \t$(INSTALL) \"$(SAGE_SPKG) $(SAGE) 2>&1\" \"tee -a $(SAGE_LOGS)/$(SAGE).log\"\n \n # Do not remove PYTHON below -- see trac 9368\n-$(INST)/$(FORTRAN): $(BASE)  $(INST)/$(PYTHON)\n+$(INST)/$(FORTRAN): $(BASE) some_python\n \t$(INSTALL) \"$(SAGE_SPKG) $(FORTRAN) 2>&1\" \"tee -a $(SAGE_LOGS)/$(FORTRAN).log\"\n \n $(INST)/$(F2C): $(BASE) $(INST)/$(FORTRAN)\n```\n\n\nThis makes the *reason* for the dependency more clear - even without further comments, and the rule for `some_python` can simply be changed in the future to actually make use of another Python - without the need for changing other rules.\n\nAnd it's formal, not prose.\n\n----\n\n> I'll fix #9762, which you clearly thought was more important than me!\n\nQA says it should definitely be a blocker. ;-)",
    "created_at": "2010-08-19T01:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95633",
    "user": "leif"
}
```

Replying to [comment:21 drkirkby]:
> Replying to [comment:19 leif]:
> > I would have liked a `SOME_PYTHON` target, but the comment on zn_poly's rule should be enough for the moment.
> 
> I'm not sure a `SOME_PYTHON` target is a good idea myself. But anyway, that is **far** outside the scope of this ticket. Such a change needs discussion on sage-devel - not a trac ticket. 

For now, I just meant:

```diff
--- deps.orig	2010-08-19 01:30:33.000000000 +0200
+++ deps	2010-08-19 03:00:48.000000000 +0200
@@ -129,6 +129,12 @@
 			 $(INST)/$(DIR)
 	$(INSTALL) "$(SAGE_SPKG) $(SAGE_SCRIPTS) 2>&1" "tee -a $(SAGE_LOGS)/$(SAGE_SCRIPTS).log"
 
+# A (perhaps system-wide) Python that's only used for scripting
+# in the build process of a Sage package:
+some_python: $(INST)/$(PYTHON)
+	# We currently only use Sage's Python, even if another
+	# (functional) Python is already present.
+
 ########################################
 # Building normal packages
 ########################################
@@ -374,7 +380,7 @@
 
 # zn_poly really does depend on Python, despite this is far from obvious.
 # The 'configure' script in zn_poly calls Python to make a 'makefile'
-$(INST)/$(ZNPOLY): $(BASE) $(INST)/$(MPIR) $(INST)/$(PYTHON)
+$(INST)/$(ZNPOLY): $(BASE) $(INST)/$(MPIR) some_python
 	$(INSTALL) "$(SAGE_SPKG) $(ZNPOLY) 2>&1" "tee -a $(SAGE_LOGS)/$(ZNPOLY).log"
 
 # setuptools forgets to update easy-install.pth during parallel
@@ -468,7 +474,7 @@
 	$(INSTALL) "$(SAGE_SPKG) $(SAGE) 2>&1" "tee -a $(SAGE_LOGS)/$(SAGE).log"
 
 # Do not remove PYTHON below -- see trac 9368
-$(INST)/$(FORTRAN): $(BASE)  $(INST)/$(PYTHON)
+$(INST)/$(FORTRAN): $(BASE) some_python
 	$(INSTALL) "$(SAGE_SPKG) $(FORTRAN) 2>&1" "tee -a $(SAGE_LOGS)/$(FORTRAN).log"
 
 $(INST)/$(F2C): $(BASE) $(INST)/$(FORTRAN)
```


This makes the *reason* for the dependency more clear - even without further comments, and the rule for `some_python` can simply be changed in the future to actually make use of another Python - without the need for changing other rules.

And it's formal, not prose.

----

> I'll fix #9762, which you clearly thought was more important than me!

QA says it should definitely be a blocker. ;-)



---

archive/issue_comments_095634.json:
```json
{
    "body": "Replying to [comment:17 leif]:\n> Replying to [comment:13 mpatel]:\n> > Just to check on #9464: Are we generally going to be explicit about all dependencies or just potential sources of confusion?\n> \n> I'd say making direct dependencies explicit is not a bad idea.\n\nI've just thought of a reason why it is a good idea to be explicit about all dependencies. Whilst before I was *sitting on the fence* over this, I now believe there are advantages in listing every dependency directly, for the reasons stated below. \n\nI wanted to start a build of Sage, without building ATLAS, so I copied the ATLAS libraries & headers from a previous Sage build, into a directory and touched `spkg/installed/atlas-3.8.3.p14.` Now, when I start to build Sage, neither Fortran, lapack or python are built.  \n\nBut something that required Fortran, lapack or Python, but only listed ATLAS as a dependency, could then fail to build. \n\nLike it or not, people do sometimes copy parts of one build to another, in order to save time. (Especially with ATLAS). That is more risky if `spkg/standard/deps` does not explicitly list each and every dependency. \n\n\nDave",
    "created_at": "2010-08-19T03:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95634",
    "user": "drkirkby"
}
```

Replying to [comment:17 leif]:
> Replying to [comment:13 mpatel]:
> > Just to check on #9464: Are we generally going to be explicit about all dependencies or just potential sources of confusion?
> 
> I'd say making direct dependencies explicit is not a bad idea.

I've just thought of a reason why it is a good idea to be explicit about all dependencies. Whilst before I was *sitting on the fence* over this, I now believe there are advantages in listing every dependency directly, for the reasons stated below. 

I wanted to start a build of Sage, without building ATLAS, so I copied the ATLAS libraries & headers from a previous Sage build, into a directory and touched `spkg/installed/atlas-3.8.3.p14.` Now, when I start to build Sage, neither Fortran, lapack or python are built.  

But something that required Fortran, lapack or Python, but only listed ATLAS as a dependency, could then fail to build. 

Like it or not, people do sometimes copy parts of one build to another, in order to save time. (Especially with ATLAS). That is more risky if `spkg/standard/deps` does not explicitly list each and every dependency. 


Dave



---

archive/issue_comments_095635.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-24T02:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9760#issuecomment-95635",
    "user": "mpatel"
}
```

Resolution: fixed
