# Issue 9913: Remove unused libraries from extension modules

Issue created by migration from https://trac.sagemath.org/ticket/9914

Original creator: leif

Original creation time: 2010-09-16 08:16:45

Assignee: leif

CC:  jhpalmieri mhansen mpatel kcrisman jpflori

Keywords: module_list.py

Many extension modules in `devel/sage/module_list.py` are linked against libraries they do not use, some at least not directly.

This is inefficient, isn't nice or at least confusing and can (actually does) cause trouble. 

See e.g. [this comment](http://trac.sagemath.org/sage_trac/ticket/9896#comment:18) for a discussion why.

This ticket will only address the removal of _some_ unnecessary libraries listed; there are most probably more.


---

Comment by leif created at 2010-09-16 10:44:36

Changing keywords from "module_list.py" to "module_list.py PARI ImportError newforms homspace mwrank upgrade update".


---

Comment by leif created at 2010-09-16 10:44:36

Changing status from new to needs_review.


---

Comment by leif created at 2010-09-16 10:44:36

I've attached a first patch that removes PARI from `libraries` of:
 * `sage.libs.cremona.homspace`
 * `sage.libs.cremona.newforms`
 * `sage.libs.mwrank.mwrank`

Hope this doesn't cause trouble on non-Unices (like e.g. Cygwin), otherwise we would have to add `uname_specific(...)` (which is defined in `module_list.py` for such purposes).

(This patch fixes _one_ of the upgrade issues discussed at #9896; these are in general not limited to MacOS X.)

Setting this to "needs review" to perhaps get it merged (early) into Sage 4.6.*, though more changes (to `module_list.py`) are desirable.


---

Comment by drkirkby created at 2010-09-16 13:04:43

Replying to [comment:1 leif]:

> Hope this doesn't cause trouble on non-Unices (like e.g. Cygwin),

I assume you tested this on Linux - that is a non-Unix! 

Solaris, recent OS X, AIX 5.3 or later and one of the more recent HP-UX releases are Unix. 

Even the {{{df}} command of Linux violates the Unix standard. 

Dave


---

Comment by leif created at 2010-09-16 13:13:10

Replying to [comment:2 drkirkby]:
> Replying to [comment:1 leif]:
> 
> > Hope this doesn't cause trouble on non-Unices (like e.g. Cygwin),
> 
> I assume you tested this on Linux

I did.

> - that is a non-Unix! 

U[nN][iI][xX] is a trademark, but also a stretchable term. ;-)

Should I say U**x-like OSs?


---

Comment by GeorgSWeber created at 2010-09-16 19:14:24

Sorry, but this will certainly break on Cygwin!

Just have a look at the Makefile for the "g0nntl" library (in the eclib spkg, see the file /src/g0n/Makefile, line 41):

NTLLFLAGS = -L$(NTLLIBDIR) -lntl -lgmp -lpari

This means that the g0nntl library has the pari library as a dependency. And on Cywgin (Windows in general), not only the "primary" libraries have to be declared as dependencies during compile time (i.e. for building e.g. an extension module) --- but *all* libraries, i.e. also the "secondary", "tertiary", and so on ... (one may consider this a bug, a deficiency, a nuisance, whatever --- we have to live with it)

I've changed the title of the ticket somewhat, to reflect this, and added a line to the description.

If this ticket is meant to fix some OS X specific issue (see the main ticket at trac #9896), I'd propose to use the "uname_specific" feature in such a way, that the change to the module_list.py affects Darwin --- and only Darwin.

Ensuring that the change is visible on only as few system as possible, as few systems as possible are affected of a possible breakage by such a change.


---

Comment by GeorgSWeber created at 2010-09-16 19:14:24

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-09-17 00:05:25

Replying to [comment:4 GeorgSWeber]:
> Sorry, but this will certainly break on Cygwin!

Did you read the comments here or at the other ticket? I explicitly asked if this is needed on Cygwin (twice), cc'ed Mike, and suggested to use `uname_specific()` in that case.

> Just have a look at the Makefile for the "g0nntl" library (in the eclib spkg, see the file /src/g0n/Makefile, line 41):
> 

> NTLLFLAGS = -L$(NTLLIBDIR) -lntl -lgmp -lpari

Bad example, since you can safely remove PARI there (too; and also from `NTLLFLAGS` in all other Makefiles); NTL uses GMP, but not PARI. (Only `procs/parifact.*` uses PARI, so PARI has to be linked to all executables and shared libraries that contain / use _that_, e.g. `libjcntl.{so,dylib,dll`}, which in turn is linked to `libg0nntl.*`.)

(Note that "pari" is *not* listed in the `libraries` of `sage.libs.cremona.mat`, though "jcntl" is, and "g0nntl", too.)

Even if e.g. `libg0nntl.so` directly depended on PARI, none of the extension modules whose `libraries` I've changed does.

There's a difference between dynamically and statically linking btw.

> I've changed the title of the ticket somewhat, to reflect this, and added a line to the description.

By _"removing ... from the extension modules"_ I meant removing the in fact (locally) unused libraries from the dynamic (dependencies) section, i.e. for example the `NEEDED` entries in ELF.

> If this ticket is meant to fix some OS X specific issue (see the main ticket at trac #9896), I'd propose to use the "uname_specific" feature in such a way, that the change to the module_list.py affects Darwin --- and only Darwin.

Again, as mentioned in my first comment here, and also at #9896, this is a _general_ problem which is unrelated to Darwin as the OS.

> Ensuring that the change is visible on only as few system as possible, as few systems as possible are affected of a possible breakage by such a change.

The opposite is closer to what is needed: if at all, PARI has to be listed in `libraries` _only on Cygwin_ (or MS Windows) if you're right (but see above); I'm not sure if it would be required on older Darwins as well.

So I'll update the patch to use `uname_specific()` (if that makes you happy ;-) - I'd really like to give it a try _as is_ on Cygwin), which then should be tested (also) on MacOS X 10.4 (Tiger).


---

Comment by GeorgSWeber created at 2010-09-17 10:36:19

Replying to [comment:5 leif]:
> 
> Even if e.g. `libg0nntl.so` directly depended on PARI, none of the extension modules whose `libraries` I've changed does.
> 

Even if the -lpari dependency in the build/compile call of the libg0nntl is technically superfluous, and/or none of the extension modules used libpari functionality in the end --- this parameter -lpari is *there* (in the Makefile line mentioned). This might be a bug in this eclib Makefile. Which probably doesn't matter on most systems, but might very well matter on Cygwin (and the presence of lpari in the module_list.py entries just a q'n'd workaround). Put in other words: the module_list.py patch might be incomplete without also updating (correcting?) this Makefile.

> 
> So I'll update the patch to use `uname_specific()` (if that makes you happy ;-) - I'd really like to give it a try _as is_ on Cygwin), which then should be tested (also) on MacOS X 10.4 (Tiger).

So both of us are kind of stuck here --- neither of us seems to have access to some Cygwin system, to do "real life" testing. Personally, I do have access to Mac OS X 10.4 systems (both MacIntel and MacPPC), but does that suffice to work on the ticket? I mean, wouldn't updating Sage-4.5.3 to Sage-4.6 still break on Cygwin (even if we fixed all other OS's)?

In general, such update problems are not new. The Sage build/update mechanisms have shortcomings that are well known. In the past, one had to (and did) give hints to them. I can't put my finger to a specific release or sage-devel thread right now, but the idea is as simple as powerful, I'll explain it at the example at hand.

Solution:

Just artificially bump up the version number of the eclib spkg.
(No real changes are done to its contents --- and often in the past, even the update of the SPKG.txt was forgotten, but that's another matter, one should do that always).

As a result, during an update, the eclib spkg *will* be built anew, and as a consequence, also during "sage -b" the mentioned extensions are rebuilt. Et voila.

Leif, I couldn't follow each and every of the recent threads on sage-devel and sage-release, let alone trac. Has this "old way" been discussed, or even considered (for Sage-4.6)? If not, should a message thread on sage-release be opened?

I think there's a very good chance to get the update from Sage-4.5.3 to Sage-4.6 working, just by artificially bumping up the version numbers of a handful spkg's (in the sense I described above). 

Cheers,

Georg


---

Comment by leif created at 2010-09-17 14:56:57

Replying to [comment:6 GeorgSWeber]:
> Solution:
> 
> Just artificially bump up the version number of the eclib spkg.
> (No real changes are done to its contents --- and often in the past, even the update of the SPKG.txt was forgotten, but that's another matter, one should do that always).
> 
> As a result, during an update, the eclib spkg *will* be built anew, and as a consequence, also during "sage -b" the mentioned extensions are rebuilt. Et voila.

This doesn't work either, see http://trac.sagemath.org/sage_trac/ticket/9896#comment:16. (Bumping the patch level is equivalent to doing `./sage -f ...`.)


> I think there's a very good chance to get the update from Sage-4.5.3 to Sage-4.6 working, just by artificially bumping up the version numbers of a handful spkg's (in the sense I described above). 

Nevertheless, imagine upgrading MPIR (#8664). Do you want to bump the version numbers of dozens of packages? Changing `sage-spkg` to `sage-spkg -f` in `spkg/standard/deps` avoids this, but doesn't solve all problems we have with (re)building the Sage library.

Robert B. wanted to make Cython smarter such that more of what's manually provided in `module_list.py` gets deduced automatically from the Cython source files (through pragmas), but the new Cython 0.13 doesn't yet support these enhancements.

So unfortunately we currently have to keep hacking `module_list.py` and `setup.py` to get around subtle dependency issues...

We might as an alternative add `depends = [ ... ]` to these extension modules to get them updated when ECLIB gets (I think in general not a bad idea), but this doesn't really address the PARI issue, i.e. that the library should IMHO not be listed there.

There are or have been btw. other weird things like `libcsage` and `libstdc++` being linked to each and every module, regardless of the language or if the module referenced symbols from there at all.

I started cleaning up `module_list.py` month ago (which is quite tedious), but then Robert said we'd have a better solution in the near future...


---

Comment by leif created at 2010-09-17 14:56:57

Changing status from needs_work to needs_info.


---

Comment by mpatel created at 2010-09-22 23:40:30

Mike, do you think the changes above will cause problems on Cygwin?


---

Comment by leif created at 2010-10-26 22:34:02

Incidentally there came up a related discussion in an otherwise unrelated [sage-devel thread](http://groups.google.com/group/sage-devel/msg/28dedefe6d85eaa3).


---

Comment by mhansen created at 2010-11-10 18:33:51

These (three) changes don't cause any problem on Cygwin with Sage 4.6.


---

Comment by GeorgSWeber created at 2010-11-13 20:20:58

Changing status from needs_info to needs_review.


---

Comment by GeorgSWeber created at 2010-11-13 20:20:58

Good to know,

sorry that I was wrong, Leif: please accept my apologies!


Cheers,
Georg


---

Attachment

I've added a rebased patch.

Apply trac_9914.patch

Assuming tests pass, I'll give this a positive review.


---

Comment by leif created at 2012-04-05 22:05:31

The original title was _"Remove unused libraries from extension modules"_. ;-)

(Wasn't me who changed that.)


---

Comment by jdemeyer created at 2012-04-07 06:58:51

Changing status from needs_review to needs_info.


---

Comment by jdemeyer created at 2012-04-07 06:58:51

Please explain the rationale for this patch.  [The comment you linked to](http://trac.sagemath.org/sage_trac/ticket/9896#comment:18) does not explain this.  And the following sentence is also very vague: "
> This is inefficient, isn't nice or at least confusing and can (actually does) cause trouble.


---

Comment by jdemeyer created at 2012-04-07 06:59:28

The modules you are removing "-lpari" from are actually linked against pari, so I think "pari" should be kept.

The following have been built with this patch applied:

```
(sage-sh) jdemeyer@boxen:lib.linux-x86_64-2.7$ ldd sage/libs/mwrank/mwrank.so
        linux-vdso.so.1 =>  (0x00007ffff6dfd000)
        libcsage.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libcsage.so (0x00007febee7b5000)
        libcurvesntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libcurvesntl.so (0x00007febee49a000)
        libg0nntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libg0nntl.so (0x00007febee23c000)
        libjcntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libjcntl.so (0x00007febedf3b000)
        librankntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/librankntl.so (0x00007febedc8a000)
        libntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libntl.so (0x00007febed8a5000)
        libgmp.so.7 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libgmp.so.7 (0x00007febed62d000)
        libgmpxx.so.1 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libgmpxx.so.1 (0x00007febed426000)
        libstdc++.so.6 => /home/jdemeyer/local/lib64/libstdc++.so.6 (0x00007febed121000)
        libpython2.7.so.1.0 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libpython2.7.so.1.0 (0x00007febecd4d000)
        libm.so.6 => /lib/libm.so.6 (0x00007febecab7000)
        libgcc_s.so.1 => /home/jdemeyer/local/lib64/libgcc_s.so.1 (0x00007febec8a2000)
        libpthread.so.0 => /lib/libpthread.so.0 (0x00007febec686000)
        libc.so.6 => /lib/libc.so.6 (0x00007febec323000)
        libpari-gmp.so.3 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libpari-gmp.so.3 (0x00007febebc61000)
        /lib64/ld-linux-x86-64.so.2 (0x00007febeebf0000)
        libdl.so.2 => /lib/libdl.so.2 (0x00007febeba5c000)
        libutil.so.1 => /lib/libutil.so.1 (0x00007febeb859000)
```



```
(sage-sh) jdemeyer@boxen:lib.linux-x86_64-2.7$ ldd sage/libs/cremona/homspace.so
        linux-vdso.so.1 =>  (0x00007fff8adfd000)
        libcsage.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libcsage.so (0x00007fa382917000)
        libg0nntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libg0nntl.so (0x00007fa3826b8000)
        libjcntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libjcntl.so (0x00007fa3823b7000)
        libgmpxx.so.1 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libgmpxx.so.1 (0x00007fa3821b1000)
        libntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libntl.so (0x00007fa381dcb000)
        libgmp.so.7 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libgmp.so.7 (0x00007fa381b53000)
        libstdc++.so.6 => /home/jdemeyer/local/lib64/libstdc++.so.6 (0x00007fa38184e000)
        libcurvesntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libcurvesntl.so (0x00007fa381533000)
        libpython2.7.so.1.0 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libpython2.7.so.1.0 (0x00007fa38115f000)
        libm.so.6 => /lib/libm.so.6 (0x00007fa380eca000)
        libgcc_s.so.1 => /home/jdemeyer/local/lib64/libgcc_s.so.1 (0x00007fa380cb4000)
        libpthread.so.0 => /lib/libpthread.so.0 (0x00007fa380a98000)
        libc.so.6 => /lib/libc.so.6 (0x00007fa380736000)
        libpari-gmp.so.3 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libpari-gmp.so.3 (0x00007fa380073000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fa382d38000)
        libdl.so.2 => /lib/libdl.so.2 (0x00007fa37fe6f000)
        libutil.so.1 => /lib/libutil.so.1 (0x00007fa37fc6b000)
```



```
(sage-sh) jdemeyer@boxen:lib.linux-x86_64-2.7$ ldd sage/libs/cremona/newforms.so
        linux-vdso.so.1 =>  (0x00007fff60bfd000)
        libcsage.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libcsage.so (0x00007fcc585fb000)
        libg0nntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libg0nntl.so (0x00007fcc5839c000)
        libjcntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libjcntl.so (0x00007fcc5809b000)
        libgmpxx.so.1 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libgmpxx.so.1 (0x00007fcc57e95000)
        libntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libntl.so (0x00007fcc57aaf000)
        libgmp.so.7 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libgmp.so.7 (0x00007fcc57837000)
        libstdc++.so.6 => /home/jdemeyer/local/lib64/libstdc++.so.6 (0x00007fcc57532000)
        libcurvesntl.so => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libcurvesntl.so (0x00007fcc57217000)
        libpython2.7.so.1.0 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libpython2.7.so.1.0 (0x00007fcc56e43000)
        libm.so.6 => /lib/libm.so.6 (0x00007fcc56bae000)
        libgcc_s.so.1 => /home/jdemeyer/local/lib64/libgcc_s.so.1 (0x00007fcc56998000)
        libpthread.so.0 => /lib/libpthread.so.0 (0x00007fcc5677c000)
        libc.so.6 => /lib/libc.so.6 (0x00007fcc5641a000)
        libpari-gmp.so.3 => /padic/scratch/jdemeyer/merger/sage-5.0.beta14/local/lib/libpari-gmp.so.3 (0x00007fcc55d57000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fcc58a1e000)
        libdl.so.2 => /lib/libdl.so.2 (0x00007fcc55b53000)
        libutil.so.1 => /lib/libutil.so.1 (0x00007fcc5594f000)
```



---

Comment by leif created at 2012-04-07 08:13:00

Changing status from needs_info to needs_review.


---

Comment by leif created at 2012-04-07 08:13:00

Replying to [comment:15 jdemeyer]:
> Please explain the rationale for this patch.

Is this so hard to understand?

> [The comment you linked to](http://trac.sagemath.org/sage_trac/ticket/9896#comment:18) does not explain this.

It does, as does the further discussion on this ticket (and #9896).

> And the following sentence is also very vague: "
> > This is inefficient, isn't nice or at least confusing and can (actually does) cause trouble.

Why specify libraries to link to if they aren't used / needed at all?

This *is* simply confusing, obviously inefficient, and causes trouble if the (unused) libraries the extension modules (i.e., their `.so`s) refer to get updated, since they'll still pull in the old, obsolete ones (which may also have already been deleted, in which case at least less weird errors are raised), for no reason.

As mentioned earlier and elsewhere, the eclib spkg is a special case anyway (also regarding the list of libraries its modules are linked to; cf. [comment:5 my comment above]).


---

Comment by leif created at 2012-04-07 08:16:26

Replying to [comment:16 jdemeyer]:
> The modules you are removing "-lpari" from are actually linked against pari, so I think "pari" should be kept.

??? If you can safely remove `-lpari` in `module_list.py`, what's the problem?

Your `ldd` dumps just show that eclib's modules also have the PARI library in their NEEDED tags, so what?  (Doesn't matter here whether they really need / use them or not.)


---

Comment by jdemeyer created at 2012-04-07 08:26:24

I still don't see the problem...  anyway, has this patch been tested on Cygwin?


---

Comment by leif created at 2012-04-07 09:04:47

Replying to [comment:17 leif]:
> Replying to [comment:15 jdemeyer]:
> > Please explain the rationale for this patch.
> > And the following sentence is also very vague: "
> > > This is inefficient, isn't nice or at least confusing and can (actually does) cause trouble.
> 
> Why specify libraries to link to if they aren't used / needed at all?
> 
> This *is* simply confusing, obviously inefficient, and causes trouble if the (unused) libraries the extension modules (i.e., their `.so`s) refer to get updated, since they'll still pull in the old, obsolete ones (which may also have already been deleted, in which case at least less weird errors are raised), for no reason.


```sh
# This is your (unused) library:
echo "void foo(){}" > foo.c
gcc -c foo.c
gcc -shared -o libfoo.so.1 -Wl,-soname,libfoo.so.1 foo.o
ln -sf libfoo.so.1 libfoo.so

# Now build your "extension module" bar (which doesn't *need* libfoo):
echo "int main(){}" > bar.c
gcc -o bar bar.c -L. -lfoo

# "Load" it:
LD_LIBRARY_PATH=. ./bar # fine

# Now update the unused foo library:
rm -f libfoo.so*
# Don't have to recompile foo.c, but one usually would of course.
gcc -shared -o libfoo.so.2 -Wl,-soname,libfoo.so.2 foo.o
ln -sf libfoo.so.2 libfoo.so

# Now load / run your "extension module" again:
LD_LIBRARY_PATH=. ./bar # boom
```



---

Comment by leif created at 2012-04-07 09:08:40

Ooops, missed the last lines:

```sh
# (You'll certainly agree that rebuilding bar doesn't make sense
# since it doesn't really use / need libfoo at all.)

# Things get weirder if you use bar (as a module / library) and have
# another module baz which actually uses libfoo, and refers to the new
# version.  If the old libfoo.so.1 wasn't deleted, you'll most probably
# get name clashs, or baz tries to use symbols the obsolete libfoo
# doesn't have, but bar pulled in the older version. 
```


:-)


---

Comment by leif created at 2012-04-07 09:14:42

Replying to [comment:19 jdemeyer]:
> anyway, has this patch been tested on Cygwin?

Yes, it used to work on Cygwin as well; see [comment:10 Mike's 17 months old comment above].


---

Comment by jdemeyer created at 2013-03-06 15:01:27

Changing status from needs_review to needs_info.


---

Comment by jdemeyer created at 2013-03-06 15:01:27

Replying to [comment:18 leif]:
> Your `ldd` dumps just show that eclib's modules also have the PARI library in their NEEDED tags, so what?  (Doesn't matter here whether they really need / use them or not.)
eclib actually uses PARI.

Given that the modules link against `-lpari` anyway, the issue mentioned in [comment:20] can still happen.

Therefore, I see absolutely no problem.


---

Comment by jdemeyer created at 2014-02-04 08:10:47

Changing status from needs_info to positive_review.


---

Comment by jdemeyer created at 2014-02-04 08:10:47

I still see no problem here and didn't get a reply to my last question => close as "wontfix".


---

Comment by vbraun created at 2014-02-04 21:10:19

Resolution: wontfix
