# Issue 1261: parallel "sage -br"

archive/issues_001261.json:
```json
{
    "body": "Assignee: was*\n\nIt would be very desirable for \"sage -br\" to take advantage of multi-processor and multi-core machines automatically.\n\nThe following irc session describes an idea for a way to easily implement this.\nThe main idea is to use the dry_run option to setup(...) in setup.py, capture\nthe output of the dry_run, then run those commands in parallel.\n\n\n```\n[9:21pm] was_: When \"sage -br\" runs we first (with custom code I wrote) run cython on a bunch of files -- for this the order is probably important.\n[9:21pm] was_: (??)\n[9:22pm] was_: Anyway, after that, distutils runs gcc or g++ on a large number of files.  I think for that the order doesn't matter much.\n[9:22pm] cwitty: The order of running Cython should not be important.\n[9:22pm] was_: Are you sure?\n[9:22pm] mabshoff: ok\n[9:22pm] was_: There is a dry_run option to the setup function in devel/sage/setup.py.\n[9:22pm] cwitty: (Cython depends on source files, like .pxd; but I'm pretty sure it doesn't depend on the generated .c or .cpp files.)\n[9:23pm] was_: cwitty -- I think you're right.\n[9:23pm] mabshoff: each file cython compiles is a dynmaic library?\n[9:23pm] was_: Definitely things are easier if you are.\n[9:23pm] cwitty: mabshoff, yes.\n[9:23pm] was_: cython just makes .c/.cpp/.h files as output; that's it.\n[9:23pm] was_: And everything is dynamic.\n[9:23pm] mabshoff: Then it shouldn't have compile time dependencies.\n[9:23pm] was_: Anyway, back to my idea.\n[9:23pm] mabshoff: link time at import, but that doesn't matter.\n[9:23pm] was_: (There are possibly some mild dependencies since multiple files are combined to make one dynamic library in some cases.)\n[9:24pm] was_: Anyway, back to my idea.\n[9:24pm] was_: If you look at devel/sage/setup.py, and put dry_run=True as the last option to the huge setup(...) function,\n[9:24pm] was_: then distutils will simply print out all the gcc commands it *would* run.\n[9:24pm] was_: But it doesn't run thme.\n[9:24pm] mabshoff: I see where you are going \n[9:25pm] was_: So my crazy idea is to run setup once as a dry_run, capture all the output, divide it up, do the gcc's in parallel, then run distutils again with dry_run=False,\n[9:25pm] was_: which will be fast.\n[9:25pm] mabshoff:\n[9:25pm] mabshoff: Let's hope it works.\n[9:25pm] was_: I have no idea if it would really work.\n[9:25pm] mabshoff: Even then we could also create a makefile from cython info and run parallel make on that.\n[9:26pm] was_: If we wanted, though it seems hardly necessary.\n[9:26pm] mabshoff: KISS\n[9:26pm] was_: yep.\n[9:26pm] was_: Make is pretty KISS though, at least the way we're thinking of using it.\n[9:26pm] was_: KISS was why the spkg build system uses make.\n[9:27pm] mabshoff:\n[9:27pm] mabshoff: I just got a timeout with -long running doctests.\n[9:27pm] mabshoff: Maybe we should disable TIMEOUT with -long\n[9:27pm] was_: There should be a timeout but it should be way longer.\n[9:27pm] mabshoff: ok\n[9:27pm] was_: E.g., David Joyner put an annoying #long doctest in once that took *days* to run.\n[9:27pm] was_: Very annoying.\n[9:27pm] was_: It was good that there was a timeout.\n[9:28pm] was_: I asked him about it and he said it was a \"record breaking\" computation...\n[9:28pm] mabshoff:\n[9:28pm] mabshoff: I think the doctest finishes, but then python realises that the TIMEOUT was exceeded.\n[9:29pm] was_: that sounds dumb.\n[9:29pm] mabshoff:\n[9:29pm] mabshoff: I set my timeout to 30 minutes for now on my copy.\n[9:29pm] was_: I just did some tests with my parallel \"sage -br\" above and it looks very promising.\n[9:30pm] mabshoff: Is it going in 2.8.14? *ducks*\n[9:30pm] was_: no\n[9:30pm] was_: I want to release 2.8.14 in an hour.\n[9:30pm] mabshoff: I thought so.\n[9:33pm] was_: For smaller files running cython takes longer than gcc.\n[9:33pm] was_: E.g., I just tested on sage/libs/cremona/*.pyx, and it takes < 4 seconds to run GCC and nearly 12 seconds to run Cython.\n[9:33pm] mabshoff: ok\n[9:33pm] was_: Maybe we should write Cython in Cython (ducks)\n[9:34pm] mabshoff: my thoughts exactly.\n[9:34pm] mabshoff: For 10% of the code it would probably be worth it for performance reasons.\n[9:34pm] mabshoff: Maybe you should suggest it to Robert.\n[9:34pm] was_: But from the point of view of parallel sage -br, it just means we need to do that in parallel too...\n[9:34pm] was_: I.e., both are worth doing.\n[9:35pm] mabshoff: Yep,.\n[9:35pm] was_: First should be the gcc code.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1261\n\n",
    "created_at": "2007-11-25T05:39:18Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "parallel \"sage -br\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1261",
    "user": "was"
}
```
Assignee: was*

It would be very desirable for "sage -br" to take advantage of multi-processor and multi-core machines automatically.

The following irc session describes an idea for a way to easily implement this.
The main idea is to use the dry_run option to setup(...) in setup.py, capture
the output of the dry_run, then run those commands in parallel.


```
[9:21pm] was_: When "sage -br" runs we first (with custom code I wrote) run cython on a bunch of files -- for this the order is probably important.
[9:21pm] was_: (??)
[9:22pm] was_: Anyway, after that, distutils runs gcc or g++ on a large number of files.  I think for that the order doesn't matter much.
[9:22pm] cwitty: The order of running Cython should not be important.
[9:22pm] was_: Are you sure?
[9:22pm] mabshoff: ok
[9:22pm] was_: There is a dry_run option to the setup function in devel/sage/setup.py.
[9:22pm] cwitty: (Cython depends on source files, like .pxd; but I'm pretty sure it doesn't depend on the generated .c or .cpp files.)
[9:23pm] was_: cwitty -- I think you're right.
[9:23pm] mabshoff: each file cython compiles is a dynmaic library?
[9:23pm] was_: Definitely things are easier if you are.
[9:23pm] cwitty: mabshoff, yes.
[9:23pm] was_: cython just makes .c/.cpp/.h files as output; that's it.
[9:23pm] was_: And everything is dynamic.
[9:23pm] mabshoff: Then it shouldn't have compile time dependencies.
[9:23pm] was_: Anyway, back to my idea.
[9:23pm] mabshoff: link time at import, but that doesn't matter.
[9:23pm] was_: (There are possibly some mild dependencies since multiple files are combined to make one dynamic library in some cases.)
[9:24pm] was_: Anyway, back to my idea.
[9:24pm] was_: If you look at devel/sage/setup.py, and put dry_run=True as the last option to the huge setup(...) function,
[9:24pm] was_: then distutils will simply print out all the gcc commands it *would* run.
[9:24pm] was_: But it doesn't run thme.
[9:24pm] mabshoff: I see where you are going 
[9:25pm] was_: So my crazy idea is to run setup once as a dry_run, capture all the output, divide it up, do the gcc's in parallel, then run distutils again with dry_run=False,
[9:25pm] was_: which will be fast.
[9:25pm] mabshoff:
[9:25pm] mabshoff: Let's hope it works.
[9:25pm] was_: I have no idea if it would really work.
[9:25pm] mabshoff: Even then we could also create a makefile from cython info and run parallel make on that.
[9:26pm] was_: If we wanted, though it seems hardly necessary.
[9:26pm] mabshoff: KISS
[9:26pm] was_: yep.
[9:26pm] was_: Make is pretty KISS though, at least the way we're thinking of using it.
[9:26pm] was_: KISS was why the spkg build system uses make.
[9:27pm] mabshoff:
[9:27pm] mabshoff: I just got a timeout with -long running doctests.
[9:27pm] mabshoff: Maybe we should disable TIMEOUT with -long
[9:27pm] was_: There should be a timeout but it should be way longer.
[9:27pm] mabshoff: ok
[9:27pm] was_: E.g., David Joyner put an annoying #long doctest in once that took *days* to run.
[9:27pm] was_: Very annoying.
[9:27pm] was_: It was good that there was a timeout.
[9:28pm] was_: I asked him about it and he said it was a "record breaking" computation...
[9:28pm] mabshoff:
[9:28pm] mabshoff: I think the doctest finishes, but then python realises that the TIMEOUT was exceeded.
[9:29pm] was_: that sounds dumb.
[9:29pm] mabshoff:
[9:29pm] mabshoff: I set my timeout to 30 minutes for now on my copy.
[9:29pm] was_: I just did some tests with my parallel "sage -br" above and it looks very promising.
[9:30pm] mabshoff: Is it going in 2.8.14? *ducks*
[9:30pm] was_: no
[9:30pm] was_: I want to release 2.8.14 in an hour.
[9:30pm] mabshoff: I thought so.
[9:33pm] was_: For smaller files running cython takes longer than gcc.
[9:33pm] was_: E.g., I just tested on sage/libs/cremona/*.pyx, and it takes < 4 seconds to run GCC and nearly 12 seconds to run Cython.
[9:33pm] mabshoff: ok
[9:33pm] was_: Maybe we should write Cython in Cython (ducks)
[9:34pm] mabshoff: my thoughts exactly.
[9:34pm] mabshoff: For 10% of the code it would probably be worth it for performance reasons.
[9:34pm] mabshoff: Maybe you should suggest it to Robert.
[9:34pm] was_: But from the point of view of parallel sage -br, it just means we need to do that in parallel too...
[9:34pm] was_: I.e., both are worth doing.
[9:35pm] mabshoff: Yep,.
[9:35pm] was_: First should be the gcc code.
```


Issue created by migration from https://trac.sagemath.org/ticket/1261





---

archive/issue_comments_007882.json:
```json
{
    "body": "Changing assignee from was* to gfurnish.",
    "created_at": "2008-03-03T02:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7882",
    "user": "gfurnish"
}
```

Changing assignee from was* to gfurnish.



---

archive/issue_comments_007883.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-03T02:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7883",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007884.json:
```json
{
    "body": "The plan is to replace python distutils with scons for cython, etc.",
    "created_at": "2008-03-03T08:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7884",
    "user": "gfurnish"
}
```

The plan is to replace python distutils with scons for cython, etc.



---

archive/issue_comments_007885.json:
```json
{
    "body": "I built a new build system for this as scons was inadequate.  An alpha version is available that does parallel build all (so it is a full rebuild every time).  Set SAGE_BUILD_THREADS to set the number of threads, which defaults to 4.  Download at: http://sage.math.washington.edu/home/gfurnish/misc/build.tar",
    "created_at": "2008-03-17T02:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7885",
    "user": "gfurnish"
}
```

I built a new build system for this as scons was inadequate.  An alpha version is available that does parallel build all (so it is a full rebuild every time).  Set SAGE_BUILD_THREADS to set the number of threads, which defaults to 4.  Download at: http://sage.math.washington.edu/home/gfurnish/misc/build.tar



---

archive/issue_comments_007886.json:
```json
{
    "body": "Attachment [trac_1261_extcode.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode.patch) by gfurnish created at 2008-03-23 11:59:42\n\nPbuild extcode repo",
    "created_at": "2008-03-23T11:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7886",
    "user": "gfurnish"
}
```

Attachment [trac_1261_extcode.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode.patch) by gfurnish created at 2008-03-23 11:59:42

Pbuild extcode repo



---

archive/issue_comments_007887.json:
```json
{
    "body": "PBuild for extcode requires glib to work correctly.  Obtain at #2436.",
    "created_at": "2008-03-23T12:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7887",
    "user": "gfurnish"
}
```

PBuild for extcode requires glib to work correctly.  Obtain at #2436.



---

archive/issue_comments_007888.json:
```json
{
    "body": "Attachment [trac_1261_extcode_2.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_2.patch) by gfurnish created at 2008-03-23 17:32:15\n\nThis file is to be applied on top of the first patch.",
    "created_at": "2008-03-23T17:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7888",
    "user": "gfurnish"
}
```

Attachment [trac_1261_extcode_2.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_2.patch) by gfurnish created at 2008-03-23 17:32:15

This file is to be applied on top of the first patch.



---

archive/issue_comments_007889.json:
```json
{
    "body": "Attachment [trac_1261_extcode_3.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_3.patch) by gfurnish created at 2008-03-23 19:20:06\n\nApply on top of the 2nd patch",
    "created_at": "2008-03-23T19:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7889",
    "user": "gfurnish"
}
```

Attachment [trac_1261_extcode_3.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_3.patch) by gfurnish created at 2008-03-23 19:20:06

Apply on top of the 2nd patch



---

archive/issue_comments_007890.json:
```json
{
    "body": "A couple remarks:\n\n* the CPUID asm code is x86 specific\n* I don't understand what the option parsing code has to do in the build system? \n* class enviroment ought to be class environment\n* there ought to be spaces between defs \n* documentation in general is missing, but we agreed that it would be added past the review\n* how much code duplication is going on here with code like ptest?\n\nI need to take a closer look to see what the code actually does.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-23T20:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7890",
    "user": "mabshoff"
}
```

A couple remarks:

* the CPUID asm code is x86 specific
* I don't understand what the option parsing code has to do in the build system? 
* class enviroment ought to be class environment
* there ought to be spaces between defs 
* documentation in general is missing, but we agreed that it would be added past the review
* how much code duplication is going on here with code like ptest?

I need to take a closer look to see what the code actually does.

Cheers,

Michael



---

archive/issue_comments_007891.json:
```json
{
    "body": "1) I fully realize the CPUID asm code is x86 specific, which is why its not fully implemented yet (or used anywhere)\n2) The option parsing code doesn't have much to do with the build system other then I needed an option parser and this seemed like a good place to put it.  It doesn't have any dependencies, so we could easily remove it.  I envision a whole suite here though replacing sage-sage and friends, but maybe thats a bad idea?\n3) Will run search and replace\n4) Agreed\n5) Right\n6) There is a fair ammount of code duplication in ptest, which is why I plan on eventually removing ptest and building it into the build suite.",
    "created_at": "2008-03-23T21:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7891",
    "user": "gfurnish"
}
```

1) I fully realize the CPUID asm code is x86 specific, which is why its not fully implemented yet (or used anywhere)
2) The option parsing code doesn't have much to do with the build system other then I needed an option parser and this seemed like a good place to put it.  It doesn't have any dependencies, so we could easily remove it.  I envision a whole suite here though replacing sage-sage and friends, but maybe thats a bad idea?
3) Will run search and replace
4) Agreed
5) Right
6) There is a fair ammount of code duplication in ptest, which is why I plan on eventually removing ptest and building it into the build suite.



---

archive/issue_comments_007892.json:
```json
{
    "body": "re option parser: sure, but that code ought to go into local/bin and then when you build code it should call the build system, not the other way around. It is also debatable how much of sage-sage can be written in python since Python is not a dependency of Sage.\n\nre code duplication: eventually we need to factor out common code, but that is post-merge if you ask me.\n\nre cpuid: yeah, I figured that much. DSage actually does some CPUID, too, via python's build in functions. So maybe there can be some common ground, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-23T22:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7892",
    "user": "mabshoff"
}
```

re option parser: sure, but that code ought to go into local/bin and then when you build code it should call the build system, not the other way around. It is also debatable how much of sage-sage can be written in python since Python is not a dependency of Sage.

re code duplication: eventually we need to factor out common code, but that is post-merge if you ask me.

re cpuid: yeah, I figured that much. DSage actually does some CPUID, too, via python's build in functions. So maybe there can be some common ground, too.

Cheers,

Michael



---

archive/issue_comments_007893.json:
```json
{
    "body": "apply over 3rd patch",
    "created_at": "2008-03-24T00:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7893",
    "user": "gfurnish"
}
```

apply over 3rd patch



---

archive/issue_comments_007894.json:
```json
{
    "body": "Attachment [trac_1261_extcode_4.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_4.patch) by mabshoff created at 2008-03-28 18:04:17\n\nMerged trac_1261_extcode.patch, trac_1261_extcode_2.patch, trac_1261_extcode_3.patch and trac_1261_extcode_4.patch in Sage 2.11.alpha1. Those patches are to the extcode repo and are still subject to review. \n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T18:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7894",
    "user": "mabshoff"
}
```

Attachment [trac_1261_extcode_4.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_4.patch) by mabshoff created at 2008-03-28 18:04:17

Merged trac_1261_extcode.patch, trac_1261_extcode_2.patch, trac_1261_extcode_3.patch and trac_1261_extcode_4.patch in Sage 2.11.alpha1. Those patches are to the extcode repo and are still subject to review. 

Cheers,

Michael



---

archive/issue_comments_007895.json:
```json
{
    "body": "Attachment [trac_1261_extcode_5.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_5.patch) by mabshoff created at 2008-03-29 21:27:47\n\ntrac_1261_extcode_5.patch looks good. Merged in Sage 2.11.rc0\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T21:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7895",
    "user": "mabshoff"
}
```

Attachment [trac_1261_extcode_5.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_5.patch) by mabshoff created at 2008-03-29 21:27:47

trac_1261_extcode_5.patch looks good. Merged in Sage 2.11.rc0

Cheers,

Michael



---

archive/issue_comments_007896.json:
```json
{
    "body": "Linker trouble on OSX 10.5:\n\n```\ncython --embed-positions --incref-local-binop -I. -o sage/matrix/matrix_rational_sparse.c \nsage/matrix/matrix_rational_sparse.pyx\nUndefined symbols:\n  \"_PyType_IsSubtype\", referenced from:\n      _mpz_set_pylong in mpz_pylong.o\n  \"_PyExc_KeyboardInterrupt\", referenced from:\n      _PyExc_KeyboardInterrupt$non_lazy_ptr in interrupt.o\n  \"_PyErr_SetString\", referenced from:\n      _sig_handle_sigfpe in interrupt.o\n      _sig_handle_sigbus in interrupt.o\n      _sig_handle_sigsegv in interrupt.o\n      _sage_signal_handler in interrupt.o\n      _sage_signal_handler in interrupt.o\n      _sage_signal_handler in interrupt.o\n      _sage_signal_handler in interrupt.o\n  \"_PyTuple_New\", referenced from:\n      _init_global_empty_tuple in stdsage.o\n  \"_PyInt_FromLong\", referenced from:\n      _mpz_get_pyintlong in mpz_pylong.o\n  \"_PyObject_InitVar\", referenced from:\n      _mpz_get_pylong in mpz_pylong.o\n  \"_PyExc_RuntimeError\", referenced from:\n      _PyExc_RuntimeError$non_lazy_ptr in interrupt.o\n  \"__PyErr_BadInternalCall\", referenced from:\n      _mpz_set_pylong in mpz_pylong.o\n  \"_main\", referenced from:\n      start in crt1.10.5.o\n  \"_PyObject_Malloc\", referenced from:\n      _mpz_get_pylong in mpz_pylong.o\n  \"_PyLong_Type\", referenced from:\n      _PyLong_Type$non_lazy_ptr in mpz_pylong.o\nld: symbol(s) not found\ncollect2: ld returned 1 exit status\ngcc /Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/mpn_pylong.o \n/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/convert.o \n/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/stdsage.o \n/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/ntl_wrap.o \n/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/gmp_globals.o \n/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/interrupt.o \n/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/ZZ_pylong.o \n/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/mpz_pylong.o \n-O2 -g -shared -fno-strict-aliasing -L/Users/mabshoff/sage-3.0.alpha1/local/lib  \n-lcsage  -lntl  -lgmp  -lpari  -lstdc++  -lntl  -o \n/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/libcsage.so\ncython --embed-positions --incref-local-binop -I. -o sage/libs/ntl/ntl_GF2X.c \nsage/libs/ntl/ntl_GF2X.pyx\n```\n\n\nThe output should not be called \"libcsage.so\", but \"libcsage.dylib\" on OSX. You also seem be be missing libpython.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-05T18:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7896",
    "user": "mabshoff"
}
```

Linker trouble on OSX 10.5:

```
cython --embed-positions --incref-local-binop -I. -o sage/matrix/matrix_rational_sparse.c 
sage/matrix/matrix_rational_sparse.pyx
Undefined symbols:
  "_PyType_IsSubtype", referenced from:
      _mpz_set_pylong in mpz_pylong.o
  "_PyExc_KeyboardInterrupt", referenced from:
      _PyExc_KeyboardInterrupt$non_lazy_ptr in interrupt.o
  "_PyErr_SetString", referenced from:
      _sig_handle_sigfpe in interrupt.o
      _sig_handle_sigbus in interrupt.o
      _sig_handle_sigsegv in interrupt.o
      _sage_signal_handler in interrupt.o
      _sage_signal_handler in interrupt.o
      _sage_signal_handler in interrupt.o
      _sage_signal_handler in interrupt.o
  "_PyTuple_New", referenced from:
      _init_global_empty_tuple in stdsage.o
  "_PyInt_FromLong", referenced from:
      _mpz_get_pyintlong in mpz_pylong.o
  "_PyObject_InitVar", referenced from:
      _mpz_get_pylong in mpz_pylong.o
  "_PyExc_RuntimeError", referenced from:
      _PyExc_RuntimeError$non_lazy_ptr in interrupt.o
  "__PyErr_BadInternalCall", referenced from:
      _mpz_set_pylong in mpz_pylong.o
  "_main", referenced from:
      start in crt1.10.5.o
  "_PyObject_Malloc", referenced from:
      _mpz_get_pylong in mpz_pylong.o
  "_PyLong_Type", referenced from:
      _PyLong_Type$non_lazy_ptr in mpz_pylong.o
ld: symbol(s) not found
collect2: ld returned 1 exit status
gcc /Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/mpn_pylong.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/convert.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/stdsage.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/ntl_wrap.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/gmp_globals.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/interrupt.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/ZZ_pylong.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/mpz_pylong.o 
-O2 -g -shared -fno-strict-aliasing -L/Users/mabshoff/sage-3.0.alpha1/local/lib  
-lcsage  -lntl  -lgmp  -lpari  -lstdc++  -lntl  -o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/libcsage.so
cython --embed-positions --incref-local-binop -I. -o sage/libs/ntl/ntl_GF2X.c 
sage/libs/ntl/ntl_GF2X.pyx
```


The output should not be called "libcsage.so", but "libcsage.dylib" on OSX. You also seem be be missing libpython.

Cheers,

Michael



---

archive/issue_comments_007897.json:
```json
{
    "body": "darwin",
    "created_at": "2008-04-06T04:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7897",
    "user": "gfurnish"
}
```

darwin



---

archive/issue_comments_007898.json:
```json
{
    "body": "Attachment [trac_1261_extcode_6.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_6.patch) by mabshoff created at 2008-04-06 05:03:40\n\ntrac_1261_extcode_6.patch looks good to me. Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T05:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7898",
    "user": "mabshoff"
}
```

Attachment [trac_1261_extcode_6.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_6.patch) by mabshoff created at 2008-04-06 05:03:40

trac_1261_extcode_6.patch looks good to me. Merged in Sage 3.0.alpha2



---

archive/issue_comments_007899.json:
```json
{
    "body": "#2346 touches setup.py:\n\n```\ndiff -r 767784c4ad52 -r 4f98891c4496 setup.py\n--- a/setup.py  Sat Apr 05 22:40:57 2008 -0500\n+++ b/setup.py  Sat Apr 05 22:55:32 2008 -0700\n@@ -1391,6 +1391,7 @@ code = setup(name        = 'sage',\n                      'sage.schemes.hyperelliptic_curves',\n\n                      'sage.server',\n+                     'sage.server.simple',\n                      'sage.server.server1',\n                      'sage.server.notebook',\n                      'sage.server.notebook.compress',\n```\n\nBut since this is only packages I guess pbuild is not affected.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T06:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7899",
    "user": "mabshoff"
}
```

#2346 touches setup.py:

```
diff -r 767784c4ad52 -r 4f98891c4496 setup.py
--- a/setup.py  Sat Apr 05 22:40:57 2008 -0500
+++ b/setup.py  Sat Apr 05 22:55:32 2008 -0700
@@ -1391,6 +1391,7 @@ code = setup(name        = 'sage',
                      'sage.schemes.hyperelliptic_curves',

                      'sage.server',
+                     'sage.server.simple',
                      'sage.server.server1',
                      'sage.server.notebook',
                      'sage.server.notebook.compress',
```

But since this is only packages I guess pbuild is not affected.

Cheers,

Michael



---

archive/issue_comments_007900.json:
```json
{
    "body": "Attachment [trac_1261_extcode_8.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_8.patch) by gfurnish created at 2008-04-08 09:10:12",
    "created_at": "2008-04-08T09:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7900",
    "user": "gfurnish"
}
```

Attachment [trac_1261_extcode_8.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_8.patch) by gfurnish created at 2008-04-08 09:10:12



---

archive/issue_comments_007901.json:
```json
{
    "body": "Merged trac_1261_extcode_7b.patch and trac_1261_extcode_8.patch into Sage 3.0.alpha3",
    "created_at": "2008-04-08T10:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7901",
    "user": "mabshoff"
}
```

Merged trac_1261_extcode_7b.patch and trac_1261_extcode_8.patch into Sage 3.0.alpha3



---

archive/issue_comments_007902.json:
```json
{
    "body": "trac_1261_local_1b.patch is no good as is. I will also not switch the default build system to pbuild without\n\n* some more testing\n* any documentation since people who add extensions do need to know how to do it\n\nCheers,\n\nMichael",
    "created_at": "2008-04-08T10:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7902",
    "user": "mabshoff"
}
```

trac_1261_local_1b.patch is no good as is. I will also not switch the default build system to pbuild without

* some more testing
* any documentation since people who add extensions do need to know how to do it

Cheers,

Michael



---

archive/issue_comments_007903.json:
```json
{
    "body": "Attachment [trac_1261_extcode_9.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_9.patch) by mabshoff created at 2008-04-08 10:38:53\n\nMerged trac_1261_extcode_9.patch in Sage 3.0.alpha3",
    "created_at": "2008-04-08T10:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7903",
    "user": "mabshoff"
}
```

Attachment [trac_1261_extcode_9.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_9.patch) by mabshoff created at 2008-04-08 10:38:53

Merged trac_1261_extcode_9.patch in Sage 3.0.alpha3



---

archive/issue_comments_007904.json:
```json
{
    "body": "Attachment [trac_1261_extcode_10.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_10.patch) by gfurnish created at 2008-04-10 06:16:22",
    "created_at": "2008-04-10T06:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7904",
    "user": "gfurnish"
}
```

Attachment [trac_1261_extcode_10.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_10.patch) by gfurnish created at 2008-04-10 06:16:22



---

archive/issue_comments_007905.json:
```json
{
    "body": "Attachment [trac_1261_local_2.2.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_local_2.2.patch) by gfurnish created at 2008-04-10 07:02:08",
    "created_at": "2008-04-10T07:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7905",
    "user": "gfurnish"
}
```

Attachment [trac_1261_local_2.2.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_local_2.2.patch) by gfurnish created at 2008-04-10 07:02:08



---

archive/issue_comments_007906.json:
```json
{
    "body": "Ignore the duplicate local_2 patch",
    "created_at": "2008-04-10T07:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7906",
    "user": "gfurnish"
}
```

Ignore the duplicate local_2 patch



---

archive/issue_comments_007907.json:
```json
{
    "body": "FYI: #2394 add a new extension to setup.py\n\nCheers,\n\nMichael",
    "created_at": "2008-04-11T23:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7907",
    "user": "mabshoff"
}
```

FYI: #2394 add a new extension to setup.py

Cheers,

Michael



---

archive/issue_comments_007908.json:
```json
{
    "body": "Merged trac_1261_extcode_10.patch in Sage 3.0.rc0",
    "created_at": "2008-04-20T05:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7908",
    "user": "mabshoff"
}
```

Merged trac_1261_extcode_10.patch in Sage 3.0.rc0



---

archive/issue_comments_007909.json:
```json
{
    "body": "Attachment [trac_1261_extcode_11.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_11.patch) by gfurnish created at 2008-04-27 01:19:46",
    "created_at": "2008-04-27T01:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7909",
    "user": "gfurnish"
}
```

Attachment [trac_1261_extcode_11.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_extcode_11.patch) by gfurnish created at 2008-04-27 01:19:46



---

archive/issue_comments_007910.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-27T03:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7910",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007911.json:
```json
{
    "body": "Merged trac_1261_extcode_11.patch in Sage 3.0.1.alpha1",
    "created_at": "2008-04-27T03:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7911",
    "user": "mabshoff"
}
```

Merged trac_1261_extcode_11.patch in Sage 3.0.1.alpha1



---

archive/issue_comments_007912.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-04-27T03:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7912",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_007913.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-04-27T03:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7913",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_007914.json:
```json
{
    "body": "oops, I didn't mean to close this ;(",
    "created_at": "2008-04-27T03:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7914",
    "user": "mabshoff"
}
```

oops, I didn't mean to close this ;(



---

archive/issue_comments_007915.json:
```json
{
    "body": "Attachment [trac_1261_local1.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_local1.patch) by gfurnish created at 2008-04-27 23:33:37\n\nSAGE_PBUILD OPTION",
    "created_at": "2008-04-27T23:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7915",
    "user": "gfurnish"
}
```

Attachment [trac_1261_local1.patch](tarball://root/attachments/some-uuid/ticket1261/trac_1261_local1.patch) by gfurnish created at 2008-04-27 23:33:37

SAGE_PBUILD OPTION



---

archive/issue_comments_007916.json:
```json
{
    "body": "Merged trac_1261_local1.patch in Sage 3.0.1.alpha1. \"sage -b\" in its various versions as well as \"sage -clone\" keeps working with SAGE_PBUILD=no, so more testing with SAGE_PBUILD=yes is needed.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-30T06:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7916",
    "user": "mabshoff"
}
```

Merged trac_1261_local1.patch in Sage 3.0.1.alpha1. "sage -b" in its various versions as well as "sage -clone" keeps working with SAGE_PBUILD=no, so more testing with SAGE_PBUILD=yes is needed.

Cheers,

Michael



---

archive/issue_comments_007917.json:
```json
{
    "body": "The patch set works for me. While there are still potential issues with more exotic, but not yet supported arches this is good to go. Positive review. Follow up will be more documentation, but since this ticket is already so crowded those will be new tickets.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-01T10:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7917",
    "user": "mabshoff"
}
```

The patch set works for me. While there are still potential issues with more exotic, but not yet supported arches this is good to go. Positive review. Follow up will be more documentation, but since this ticket is already so crowded those will be new tickets.

Cheers,

Michael



---

archive/issue_comments_007918.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-01T10:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7918",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007919.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-05-01T10:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1261#issuecomment-7919",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha1
