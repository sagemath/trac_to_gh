# Issue 9844: lcalc doesn't build on cygwin due to missing time.h include

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-09-01 02:17:51

Assignee: GeorgSWeber

CC:  rishi leif jdemeyer

One needs to add

```
#include <time.h> 
```

to `include/Lcommandline_numbertheory.h`
to get lcalc to build on cygwin.


---

Comment by was created at 2010-09-01 02:22:04

Changing status from new to needs_review.


---

Comment by was created at 2010-09-01 02:22:22

Spkg here: http://sage.math.washington.edu/home/wstein/patches/lcalc-20100428-1.23.p4.spkg


---

Comment by mhansen created at 2010-09-01 22:39:53

I've posted a new spkg at http://sage.math.washington.edu/home/mhansen/lcalc-20100428-1.23.p4.spkg which contains some of the fixes pointed out at #9775


---

Comment by leif created at 2010-09-02 00:12:56

Thanks for fixing much of what I mentioned at #9775.

I'm not sure if we should drop the usual "sanity check" at the top of `spkg-install`.
(Btw, you missed the "p2" in its top comment.)

The first comment regarding `SAGE_DEBUG` and the message in the `else` part aren't current.
(_"Unset SAGE_DEBUG ..."_ should read _"Set SAGE_DEBUG to yes ..."_. Though I'd prefer adding `-g` independently of that setting, since it doesn't influence performance, and most other spkgs do so.)

Replacing `-lmpir` by `-lgmp` is perhaps a minor issue; using `$MAKE` instead of `make` (`$(MAKE)` in Lcalc's Makefile itself, too) IMHO not. Unfortunately, the current `spkg/install` also uses `make` instead of `$MAKE` unless `SAGE_PARALLEL_SPKG_BUILD=yes`, which I consider a bug, since adding `-j` is not the only case in which one would set `MAKE`. One should never call `make` inside a Makefile or a script that's executed through _some_ "make", because it might be a different one.


---

Comment by leif created at 2010-09-02 00:41:32

P.S.:

```
all:
#       make print_vars
        make libLfunction.so
        make lcalc
        make examples
#       make find_L
#       make test
```

should simply (for our purposes) be

```
all:    libLfunction.so lcalc examples
```

or even just

```
all:    lcalc examples
```

but one has to add the proper dependency, i.e.:

```
examples: libLfunction.so
        $(CC) $(CCFLAGS) $(INCLUDEFILES) example_programs/example.cc libLfunction.so -o example_programs/example $(GMP_FLAGS)
```



---

Comment by leif created at 2010-09-02 21:37:17

Btw, the `-lmpir` (or `-lgmp`) is only needed if we build a _static_ version of `lcalc`, since only the also linked PARI library directly uses it.


---

Attachment

Diff between the p2 (#9592) and Mike's p4 spkg - for review/reference.


---

Comment by leif created at 2010-09-02 23:58:03

I've attached a diff between the lcalc-20100428-1.23.p2 spkg from #9592 and Mike's / William's lcalc-20100428-1.23.p4 for easier reviewing.

Note that #9592 also still needs review!
(We need this modified package for [upgrading PARI / Sage 4.6](http://wiki.sagemath.org/NewPARI).)


---

Comment by leif created at 2010-09-03 22:55:02

Also, the `dist/` (Debian) directory should be removed, cf. #5903.


---

Comment by mpatel created at 2010-09-18 08:15:57

Mike, are there Windows virtual machines running Cygwin available to potential reviewers?  (We could give access instructions off-trac.)  It would be great to reduce the number of remaining build tickets at [CygwinPort](http://trac.sagemath.org/sage_trac/wiki/CygwinPort).  And remote Cygwin access might help with #9914 (see [comment:ticket:9914:4 comment 4ff]).


---

Comment by jdemeyer created at 2010-09-19 16:04:34

Replying to [comment:10 mpatel]:
> Mike, are there Windows virtual machines running Cygwin available to potential reviewers?  (We could give access instructions off-trac.)

I wouldn't mind testing this if needed.


---

Comment by jdemeyer created at 2010-09-19 16:11:49

I have made a trivial change to spkg-install (removed the comment "# since 'success' relies on an exit code, call set +e before running it.").  I also removed the dist directory.

New spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p4.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p4.spkg)


---

Comment by jdemeyer created at 2010-09-19 16:32:42

I also made the other changes suggested by Leif.  New spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p5.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p5.spkg)


---

Attachment

ignore this file


---

Attachment

Diff between p4 and p5 - for review/reference.


---

Comment by leif created at 2010-09-19 19:02:31

Looks as if we no longer need `patches/Lcommandline_elliptic.cc.cygwin` (and `patches/Lcommandline_elliptic.cc.cygwin.diff`), since this patch isn't applied.

Mike (or Jeroen, if you can test this), is this Cygwin patch / addition obsolete:

```C
// SAGE -- used below -- needed for Cygwin.
#ifndef llrint
inline long long int llrint (double x)
{
    long long int llrintres;
    asm
    ("fistpll %0"
    : "=m" (llrintres) : "t" (x) : "st");
    return llrintres;
}
#endif
```


(It's _not_ included in the generic patch to `Lcommandline_elliptic.cc`, nor upstream.)

Apart from old typos, an obsolete comment regarding `SAGE_DEBUG`, and the recent changelog headings lacking the upstream (snapshot?) date (20100428), I'm quite happy with the new spkg (i.e., the Sage part; the patched Makefile is still suboptimal, but never mind). :)

If this spkg really contains an upstream snapshot, it is unclear from SPKG.txt when this was taken / actually put into the spkg.


---

Comment by leif created at 2010-09-19 19:16:45

The new p5 spkg successfully installed on Sage 4.6.alpha1 (with `MAKE="make -j32"`) and passed `ptestlong` on Ubuntu 10.04 x86_64, so I'm setting this to "positive review".

Feel free to revert this in case any errors occur on other systems.


---

Comment by leif created at 2010-09-19 19:16:45

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-19 23:45:26

Replying to [comment:15 leif]:
> The new p5 spkg successfully installed on Sage 4.6.alpha1 (with `MAKE="make -j32"`) and passed `ptestlong` on Ubuntu 10.04 x86_64, [...]

Same on Ubuntu 9.04 x86 (with `MAKE="make -j8"`).


---

Comment by mpatel created at 2010-09-29 08:39:47

Resolution: fixed
