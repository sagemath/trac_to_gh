# Issue 9379: is64-Linux binary fails "devel/sage/sage/plot/plot3d/tachyon.py"

archive/issues_009379.json:
```json
{
    "body": "Assignee: Mariah Lenox\n\nCC:  @jasongrout jeroen\n\nSage built on skynet/cleo (ia64-Linux-rhel) \nfails the following test when run on \nskynet/iras (ia64-Linux-suse):\n\n./sage -t -long \"devel/sage/sage/plot/plot3d/tachyon.py\"\n\nThe reason is because tachyon is being\nbuilt with cc rather than gcc.\n\nThe attached mercurial patch causes tachyon \nto be built with gcc rather than cc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9379\n\n",
    "created_at": "2010-06-29T19:18:51Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "is64-Linux binary fails \"devel/sage/sage/plot/plot3d/tachyon.py\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9379",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```
Assignee: Mariah Lenox

CC:  @jasongrout jeroen

Sage built on skynet/cleo (ia64-Linux-rhel) 
fails the following test when run on 
skynet/iras (ia64-Linux-suse):

./sage -t -long "devel/sage/sage/plot/plot3d/tachyon.py"

The reason is because tachyon is being
built with cc rather than gcc.

The attached mercurial patch causes tachyon 
to be built with gcc rather than cc.

Issue created by migration from https://trac.sagemath.org/ticket/9379





---

archive/issue_comments_088999.json:
```json
{
    "body": "Attachment [tachyon-ia64-gcc.patch](tarball://root/attachments/some-uuid/ticket9379/tachyon-ia64-gcc.patch) by mariah created at 2010-06-29 19:19:35",
    "created_at": "2010-06-29T19:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-88999",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Attachment [tachyon-ia64-gcc.patch](tarball://root/attachments/some-uuid/ticket9379/tachyon-ia64-gcc.patch) by mariah created at 2010-06-29 19:19:35



---

archive/issue_comments_089000.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-29T19:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89000",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089001.json:
```json
{
    "body": "It might be better to somehow use the CC environment variable!\n\n```\n\nflat:~ wstein$ sage -sh\n\nStarting subshell with Sage environment variables set.\nBe sure to exit when you are done and do not do anything\nwith other copies of Sage!\n\nBypassing shell configuration files ...\n\n/Users/wstein\nsage subshell$ echo $CC\ngcc\n/Users/wstein\nsage subshell$ \n```\n",
    "created_at": "2010-07-06T13:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89001",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_089002.json:
```json
{
    "body": "Replying to [comment:3 was]:\n> It might be better to somehow use the CC environment variable!\n> {{{\n> \n> flat:~ wstein$ sage -sh\n> \n> Starting subshell with Sage environment variables set.\n> Be sure to exit when you are done and do not do anything\n> with other copies of Sage!\n> \n> Bypassing shell configuration files ...\n> \n> /Users/wstein\n> sage subshell$ echo $CC\n> gcc\n> /Users/wstein\n> sage subshell$ \n> }}}\n\n\nYes, I would agree - using of the CC environment variable would be preferable. \n\nIf $(CC) does not work, try ${CC}. The target does not have 'gcc' in the name, so there is no reason to hard-code gcc. \n\nDave",
    "created_at": "2010-07-06T18:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89002",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

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

archive/issue_comments_089003.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-06T18:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89003",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089004.json:
```json
{
    "body": "Here is an updated patch [trac9377.patch](http://boxen.math.washington.edu/home/mariah/spkgs/trac9377.patch) and the corresponding [tachyon-0.98beta.p12.spkg](http://boxen.math.washington.edu/home/mariah/spkgs/tachyon-0.98beta.p12.spkg) spkg.",
    "created_at": "2010-07-15T17:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89004",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Here is an updated patch [trac9377.patch](http://boxen.math.washington.edu/home/mariah/spkgs/trac9377.patch) and the corresponding [tachyon-0.98beta.p12.spkg](http://boxen.math.washington.edu/home/mariah/spkgs/tachyon-0.98beta.p12.spkg) spkg.



---

archive/issue_comments_089005.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-15T17:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89005",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089006.json:
```json
{
    "body": "While testing this with `4.6.1.rc0` on cleo I ran into an internal compiler error building pari. A workaround is using the updated pari package at #10430. (Thanks to jdemeyer for the pointer.)",
    "created_at": "2011-01-08T22:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89006",
    "user": "https://github.com/wjp"
}
```

While testing this with `4.6.1.rc0` on cleo I ran into an internal compiler error building pari. A workaround is using the updated pari package at #10430. (Thanks to jdemeyer for the pointer.)



---

archive/issue_comments_089007.json:
```json
{
    "body": "This looks good to me, and I tested the spkg to confirm it fixed the issue.\n\nPossibly it would be a good idea to remove some more of the `\"CC=...\"` statements (there are *many*) from `Make-arch`, but it's hard to say for which ones it would be useful. The only ones currently used by sage that set `CC` to `cc` instead of `gcc` are `macosx` and `macosx-64`, in any case.\n\nAny opinions? (Remove all of them? Remove all the ones used by sage? Remove only those for macosx and macosx-64? Leave it as it is now?)",
    "created_at": "2011-01-09T04:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89007",
    "user": "https://github.com/wjp"
}
```

This looks good to me, and I tested the spkg to confirm it fixed the issue.

Possibly it would be a good idea to remove some more of the `"CC=..."` statements (there are *many*) from `Make-arch`, but it's hard to say for which ones it would be useful. The only ones currently used by sage that set `CC` to `cc` instead of `gcc` are `macosx` and `macosx-64`, in any case.

Any opinions? (Remove all of them? Remove all the ones used by sage? Remove only those for macosx and macosx-64? Leave it as it is now?)



---

archive/issue_comments_089008.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-01-09T07:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89008",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_089009.json:
```json
{
    "body": "Replying to [ticket:9379 mariah]:\n> Sage built on skynet/cleo (ia64-Linux-rhel) \n> fails the following test when run on \n> skynet/iras (ia64-Linux-suse):\n> \n> ./sage -t -long \"devel/sage/sage/plot/plot3d/tachyon.py\"\n> \n> The reason is because tachyon is being\n> built with cc rather than gcc.\n\nIs this really true?  I would like to know how using a different compiler can cause a doctest to fail.  What is the doctest error?  Maybe changing `cc` to `gcc` fixes the issue, but is that really the right fix?",
    "created_at": "2011-01-09T07:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89009",
    "user": "https://github.com/jdemeyer"
}
```

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

archive/issue_comments_089010.json:
```json
{
    "body": "Running the tachyon built with cc on cleo causes a floating point exception on startup on iras. (Even when running tachyon without parameters to get the help.)\n\nIncidentally 'cc' is also gcc on cleo, but a different one than the gcc in the PATH.",
    "created_at": "2011-01-09T07:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89010",
    "user": "https://github.com/wjp"
}
```

Running the tachyon built with cc on cleo causes a floating point exception on startup on iras. (Even when running tachyon without parameters to get the help.)

Incidentally 'cc' is also gcc on cleo, but a different one than the gcc in the PATH.



---

archive/issue_comments_089011.json:
```json
{
    "body": "Any idea why the FPE only happens on iras and not on cleo itself?  Could it be that iras has a slightly incompatible processor in which case moving a binary from cleo to iras is simply something one shouldn't do?",
    "created_at": "2011-01-09T07:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89011",
    "user": "https://github.com/jdemeyer"
}
```

Any idea why the FPE only happens on iras and not on cleo itself?  Could it be that iras has a slightly incompatible processor in which case moving a binary from cleo to iras is simply something one shouldn't do?



---

archive/issue_comments_089012.json:
```json
{
    "body": "From looking at the /proc/cpuinfo output, it seem that they have exactly the same processor (same stepping, even). The only difference is that iras runs a slightly older kernel that doesn't know yet a textual representation of family=32.",
    "created_at": "2011-01-10T17:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89012",
    "user": "https://github.com/vbraun"
}
```

From looking at the /proc/cpuinfo output, it seem that they have exactly the same processor (same stepping, even). The only difference is that iras runs a slightly older kernel that doesn't know yet a textual representation of family=32.



---

archive/issue_comments_089013.json:
```json
{
    "body": "The issue is that binaries compiled on cleo with cc contain a `.gnu.hash` ELF section (the \"new\" type), while the dynamic linker on iras only understands `.hash` ELF sections (the \"old\" type).\n\nCompiling on cleo with cc and `-Wl,--hash-style=both` produces binaries that also work on iras.\n\nBut this is just background info, and not related to the real bug of overriding CC in tachyon's build system.",
    "created_at": "2011-01-10T18:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89013",
    "user": "https://github.com/wjp"
}
```

The issue is that binaries compiled on cleo with cc contain a `.gnu.hash` ELF section (the "new" type), while the dynamic linker on iras only understands `.hash` ELF sections (the "old" type).

Compiling on cleo with cc and `-Wl,--hash-style=both` produces binaries that also work on iras.

But this is just background info, and not related to the real bug of overriding CC in tachyon's build system.



---

archive/issue_comments_089014.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2011-01-10T18:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89014",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_089015.json:
```json
{
    "body": "During the status reports for Sage Days 27 yesterday, we decided that we should probably not override CC on any platform.",
    "created_at": "2011-01-10T18:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89015",
    "user": "https://github.com/wjp"
}
```

During the status reports for Sage Days 27 yesterday, we decided that we should probably not override CC on any platform.



---

archive/issue_comments_089016.json:
```json
{
    "body": "I checked that tachyon is the only package that actually calls `cc` (by placing a non-working `cc` in the path). So thats good, at least only one place to clean up.\n\nThe gcc wrapper from #10572 automatically \n1. calls gcc when cc is invoked, and\n2. adds the `--hash-style=both` option.\nI double checked that this allows one to build `tachyon` on cleo, copy `tachyon` to iras, and successfully doctest on iras.\n\nNevertheless, we should fix the Tachyon `Make-arch` to not overwrite `$CC`. Its build system is somewhat baroque, but I made changed all GNU compiler targets to not override `$CC`, `$AR`, and `$RANLIB`. All of these variables are already provided in the Sage environment. For the record, I will attach a copy of `Make-arch` to this ticket.\n\nBut while we are at it, we should update to the newest upstream package. This ticket will be resolved by #5281.",
    "created_at": "2011-01-11T09:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89016",
    "user": "https://github.com/vbraun"
}
```

I checked that tachyon is the only package that actually calls `cc` (by placing a non-working `cc` in the path). So thats good, at least only one place to clean up.

The gcc wrapper from #10572 automatically 
1. calls gcc when cc is invoked, and
2. adds the `--hash-style=both` option.
I double checked that this allows one to build `tachyon` on cleo, copy `tachyon` to iras, and successfully doctest on iras.

Nevertheless, we should fix the Tachyon `Make-arch` to not overwrite `$CC`. Its build system is somewhat baroque, but I made changed all GNU compiler targets to not override `$CC`, `$AR`, and `$RANLIB`. All of these variables are already provided in the Sage environment. For the record, I will attach a copy of `Make-arch` to this ticket.

But while we are at it, we should update to the newest upstream package. This ticket will be resolved by #5281.



---

archive/issue_comments_089017.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-11T09:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89017",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089018.json:
```json
{
    "body": "Attachment [Make-arch.patch](tarball://root/attachments/some-uuid/ticket9379/Make-arch.patch) by @vbraun created at 2011-01-11 09:06:15\n\nPatch to Make.arch that removed CC, AR, RANLIB overrides",
    "created_at": "2011-01-11T09:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89018",
    "user": "https://github.com/vbraun"
}
```

Attachment [Make-arch.patch](tarball://root/attachments/some-uuid/ticket9379/Make-arch.patch) by @vbraun created at 2011-01-11 09:06:15

Patch to Make.arch that removed CC, AR, RANLIB overrides



---

archive/issue_comments_089019.json:
```json
{
    "body": "Replying to [comment:14 vbraun]:\n\n> The gcc wrapper from #10572 automatically \n>   1. calls gcc when cc is invoked, and\n>   1. adds the `--hash-style=both` option.\n> I double checked that this allows one to build `tachyon` on cleo, copy `tachyon` to iras, and successfully doctest on iras.\n\nBe careful. Both Intel and Sun/Oracle produce compilers for x86 that are not called 'gcc'. On other platforms compilers can have all manner of names - aCC is one I can think of.\n\nDave",
    "created_at": "2011-02-16T08:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89019",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:14 vbraun]:

> The gcc wrapper from #10572 automatically 
>   1. calls gcc when cc is invoked, and
>   1. adds the `--hash-style=both` option.
> I double checked that this allows one to build `tachyon` on cleo, copy `tachyon` to iras, and successfully doctest on iras.

Be careful. Both Intel and Sun/Oracle produce compilers for x86 that are not called 'gcc'. On other platforms compilers can have all manner of names - aCC is one I can think of.

Dave



---

archive/issue_comments_089020.json:
```json
{
    "body": "This ticket has been fixed during the BugDays 27 in #5281. Release manager: please close. \n\nRe Dave's comment, the compiler wrapper now does nothing if compiled with anything else than gcc.",
    "created_at": "2011-02-16T09:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89020",
    "user": "https://github.com/vbraun"
}
```

This ticket has been fixed during the BugDays 27 in #5281. Release manager: please close. 

Re Dave's comment, the compiler wrapper now does nothing if compiled with anything else than gcc.



---

archive/issue_comments_089021.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-02-16T09:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9379#issuecomment-89021",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_009534.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-02-16T09:56:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9379",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9379#event-9534"
}
```
