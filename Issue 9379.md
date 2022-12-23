# Issue 9379: is64-Linux binary fails "devel/sage/sage/plot/plot3d/tachyon.py"

Issue created by migration from https://trac.sagemath.org/ticket/9379

Original creator: mariah

Original creation time: 2010-06-29 19:18:51

Assignee: Mariah Lenox

CC:  jason jeroen

Sage built on skynet/cleo (ia64-Linux-rhel) 
fails the following test when run on 
skynet/iras (ia64-Linux-suse):

./sage -t -long "devel/sage/sage/plot/plot3d/tachyon.py"

The reason is because tachyon is being
built with cc rather than gcc.

The attached mercurial patch causes tachyon 
to be built with gcc rather than cc.


---

Attachment


---

Comment by mariah created at 2010-06-29 19:20:39

Changing status from new to needs_review.


---

Comment by was created at 2010-07-06 13:10:29

It might be better to somehow use the CC environment variable!

```

flat:~ wstein$ sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

Bypassing shell configuration files ...

/Users/wstein
sage subshell$ echo $CC
gcc
/Users/wstein
sage subshell$ 
```



---

Comment by drkirkby created at 2010-07-06 18:47:28

Replying to [comment:3 was]:
> It might be better to somehow use the CC environment variable!
> {{{
> 
> flat:~ wstein$ sage -sh
> 
> Starting subshell with Sage environment variables set.
> Be sure to exit when you are done and do not do anything
> with other copies of Sage!
> 
> Bypassing shell configuration files ...
> 
> /Users/wstein
> sage subshell$ echo $CC
> gcc
> /Users/wstein
> sage subshell$ 
> }}}


Yes, I would agree - using of the CC environment variable would be preferable. 

If $(CC) does not work, try ${CC}. The target does not have 'gcc' in the name, so there is no reason to hard-code gcc. 

Dave


---

Comment by drkirkby created at 2010-07-06 18:47:28

Changing status from needs_review to needs_work.


---

Comment by mariah created at 2010-07-15 17:06:09

Here is an updated patch [trac9377.patch](http://boxen.math.washington.edu/home/mariah/spkgs/trac9377.patch) and the corresponding [tachyon-0.98beta.p12.spkg](http://boxen.math.washington.edu/home/mariah/spkgs/tachyon-0.98beta.p12.spkg) spkg.


---

Comment by mariah created at 2010-07-15 17:06:09

Changing status from needs_work to needs_review.


---

Comment by wjp created at 2011-01-08 22:45:52

While testing this with `4.6.1.rc0` on cleo I ran into an internal compiler error building pari. A workaround is using the updated pari package at #10430. (Thanks to jdemeyer for the pointer.)


---

Comment by wjp created at 2011-01-09 04:35:00

This looks good to me, and I tested the spkg to confirm it fixed the issue.

Possibly it would be a good idea to remove some more of the `"CC=..."` statements (there are *many*) from `Make-arch`, but it's hard to say for which ones it would be useful. The only ones currently used by sage that set `CC` to `cc` instead of `gcc` are `macosx` and `macosx-64`, in any case.

Any opinions? (Remove all of them? Remove all the ones used by sage? Remove only those for macosx and macosx-64? Leave it as it is now?)


---

Comment by jdemeyer created at 2011-01-09 07:07:21

Changing status from needs_review to needs_info.


---

Comment by jdemeyer created at 2011-01-09 07:07:21

Replying to [ticket:9379 mariah]:
> Sage built on skynet/cleo (ia64-Linux-rhel) 
> fails the following test when run on 
> skynet/iras (ia64-Linux-suse):
> 
> ./sage -t -long "devel/sage/sage/plot/plot3d/tachyon.py"
> 
> The reason is because tachyon is being
> built with cc rather than gcc.

Is this really true?  I would like to know how using a different compiler can cause a doctest to fail.  What is the doctest error?  Maybe changing `cc` to `gcc` fixes the issue, but is that really the right fix?


---

Comment by wjp created at 2011-01-09 07:47:05

Running the tachyon built with cc on cleo causes a floating point exception on startup on iras. (Even when running tachyon without parameters to get the help.)

Incidentally 'cc' is also gcc on cleo, but a different one than the gcc in the PATH.


---

Comment by jdemeyer created at 2011-01-09 07:52:43

Any idea why the FPE only happens on iras and not on cleo itself?  Could it be that iras has a slightly incompatible processor in which case moving a binary from cleo to iras is simply something one shouldn't do?


---

Comment by vbraun created at 2011-01-10 17:45:23

From looking at the /proc/cpuinfo output, it seem that they have exactly the same processor (same stepping, even). The only difference is that iras runs a slightly older kernel that doesn't know yet a textual representation of family=32.


---

Comment by wjp created at 2011-01-10 18:28:10

The issue is that binaries compiled on cleo with cc contain a `.gnu.hash` ELF section (the "new" type), while the dynamic linker on iras only understands `.hash` ELF sections (the "old" type).

Compiling on cleo with cc and `-Wl,--hash-style=both` produces binaries that also work on iras.

But this is just background info, and not related to the real bug of overriding CC in tachyon's build system.


---

Comment by wjp created at 2011-01-10 18:28:48

Changing status from needs_info to needs_work.


---

Comment by wjp created at 2011-01-10 18:28:48

During the status reports for Sage Days 27 yesterday, we decided that we should probably not override CC on any platform.


---

Comment by vbraun created at 2011-01-11 09:01:33

I checked that tachyon is the only package that actually calls `cc` (by placing a non-working `cc` in the path). So thats good, at least only one place to clean up.

The gcc wrapper from #10572 automatically 
  1. calls gcc when cc is invoked, and
  1. adds the `--hash-style=both` option.
I double checked that this allows one to build `tachyon` on cleo, copy `tachyon` to iras, and successfully doctest on iras.

Nevertheless, we should fix the Tachyon `Make-arch` to not overwrite `$CC`. Its build system is somewhat baroque, but I made changed all GNU compiler targets to not override `$CC`, `$AR`, and `$RANLIB`. All of these variables are already provided in the Sage environment. For the record, I will attach a copy of `Make-arch` to this ticket.

But while we are at it, we should update to the newest upstream package. This ticket will be resolved by #5281.


---

Comment by vbraun created at 2011-01-11 09:01:33

Changing status from needs_work to needs_review.


---

Attachment

Patch to Make.arch that removed CC, AR, RANLIB overrides


---

Comment by drkirkby created at 2011-02-16 08:18:20

Replying to [comment:14 vbraun]:

> The gcc wrapper from #10572 automatically 
>   1. calls gcc when cc is invoked, and
>   1. adds the `--hash-style=both` option.
> I double checked that this allows one to build `tachyon` on cleo, copy `tachyon` to iras, and successfully doctest on iras.

Be careful. Both Intel and Sun/Oracle produce compilers for x86 that are not called 'gcc'. On other platforms compilers can have all manner of names - aCC is one I can think of.

Dave


---

Comment by vbraun created at 2011-02-16 09:49:07

This ticket has been fixed during the BugDays 27 in #5281. Release manager: please close. 

Re Dave's comment, the compiler wrapper now does nothing if compiled with anything else than gcc.


---

Comment by jdemeyer created at 2011-02-16 09:56:52

Resolution: duplicate
