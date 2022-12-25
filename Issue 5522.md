# Issue 5522: [with patch; needs work] Fix segfault if libsingular.so can't be found

archive/issues_005522.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  georgsweber\n\nIf for some reason libsingular.so doesn't exist, Sage will segfault when trying to call dlerror() when dlopen() was never called.\n\nI've attached a patch which avoids doing so.\n\nWith this patch, however, Sage then segfaults sometime after trying to raise the ImportError on the next line.\n\nI don't have time to investigate further, but it is easy to reproduce the condition by just moving aside the libsingular.so and trying to start sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5522\n\n",
    "created_at": "2009-03-15T00:21:22Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "[with patch; needs work] Fix segfault if libsingular.so can't be found",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5522",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

CC:  georgsweber

If for some reason libsingular.so doesn't exist, Sage will segfault when trying to call dlerror() when dlopen() was never called.

I've attached a patch which avoids doing so.

With this patch, however, Sage then segfaults sometime after trying to raise the ImportError on the next line.

I don't have time to investigate further, but it is easy to reproduce the condition by just moving aside the libsingular.so and trying to start sage.

Issue created by migration from https://trac.sagemath.org/ticket/5522





---

archive/issue_comments_042862.json:
```json
{
    "body": "Attachment [sage-libsingular-nocrash.patch](tarball://root/attachments/some-uuid/ticket5522/sage-libsingular-nocrash.patch) by GeorgSWeber created at 2009-03-25 23:36:49\n\nHi,\n\nright after\n\n```\nif handle == NULL\n```\n\none could do\n\n```\nprint \"cannot load libSINGULAR library\"\n```\n\nand only then try to call dlerror() or raise ImportError or whatsoever. If then the SegFault (sometimes) occurs, the user still knows why. With this change, I would consider this such an enhancement over the current situation, that I would vote to have it in.",
    "created_at": "2009-03-25T23:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42862",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [sage-libsingular-nocrash.patch](tarball://root/attachments/some-uuid/ticket5522/sage-libsingular-nocrash.patch) by GeorgSWeber created at 2009-03-25 23:36:49

Hi,

right after

```
if handle == NULL
```

one could do

```
print "cannot load libSINGULAR library"
```

and only then try to call dlerror() or raise ImportError or whatsoever. If then the SegFault (sometimes) occurs, the user still knows why. With this change, I would consider this such an enhancement over the current situation, that I would vote to have it in.



---

archive/issue_comments_042863.json:
```json
{
    "body": "The attached patch doesn't apply, and the corresponding code in src/sage/libs/singular/singular.pyx looks like the target code already, so I'm putting that bug up as \"needs review\" with the proposition to just close it as obsolete!",
    "created_at": "2015-02-07T09:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42863",
    "user": "https://trac.sagemath.org/admin/accounts/users/Snark"
}
```

The attached patch doesn't apply, and the corresponding code in src/sage/libs/singular/singular.pyx looks like the target code already, so I'm putting that bug up as "needs review" with the proposition to just close it as obsolete!



---

archive/issue_comments_042864.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-02-07T09:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42864",
    "user": "https://trac.sagemath.org/admin/accounts/users/Snark"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042865.json:
```json
{
    "body": "Replying to [comment:6 Snark]:\n> the corresponding code in `src/sage/libs/singular/singular.pyx` looks like the target code already\n\nThis statement is completely false.\n\nNevertheless, the patch might not be needed, I'll check.",
    "created_at": "2015-02-07T10:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42865",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:6 Snark]:
> the corresponding code in `src/sage/libs/singular/singular.pyx` looks like the target code already

This statement is completely false.

Nevertheless, the patch might not be needed, I'll check.



---

archive/issue_comments_042866.json:
```json
{
    "body": "Uh... indeed, I had \"applied\" the patch by hand yesterday and forgot about it overnight, so it's no surprise it was looking the same :-(\n\nI'll provide the adapted patch when I'll have checked its correctness.",
    "created_at": "2015-02-07T10:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42866",
    "user": "https://trac.sagemath.org/admin/accounts/users/Snark"
}
```

Uh... indeed, I had "applied" the patch by hand yesterday and forgot about it overnight, so it's no surprise it was looking the same :-(

I'll provide the adapted patch when I'll have checked its correctness.



---

archive/issue_comments_042867.json:
```json
{
    "body": "I would prefer to move the error inside the `for` loop, like\n\n```\nhandle = ...\nif not handle:\n    dlerror(...)\n```\n\n\nI think that's the simplest solution",
    "created_at": "2015-02-07T10:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42867",
    "user": "https://github.com/jdemeyer"
}
```

I would prefer to move the error inside the `for` loop, like

```
handle = ...
if not handle:
    dlerror(...)
```


I think that's the simplest solution



---

archive/issue_comments_042868.json:
```json
{
    "body": "It avoids the flag variable. Good idea.",
    "created_at": "2015-02-07T11:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42868",
    "user": "https://trac.sagemath.org/admin/accounts/users/Snark"
}
```

It avoids the flag variable. Good idea.



---

archive/issue_comments_042869.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-02-07T12:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42869",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_042870.json:
```json
{
    "body": "I pushed the branch because it looked nice, but then I tested what happens without the patch... and the result is in fact the same! Indeed, if libsingular.so isn't available, we already have an ImportError because of missing symbols:\n\n```\n   /home/jpuydt/sage-6.5.beta5/local/lib/python2.7/site-packages/sage/libs/singular/__init__.py in <module>()\n   ---->\n   1 from sage.libs.singular.function import singular_function, lib\n        global sage.libs.singular.function = undefined\n        global singular_function = undefined\n        global lib = undefined\n      2 \n      3 from sage.libs.singular.function_factory import SingularFunctionFactory\n      4 \n      5 ff = SingularFunctionFactory()\n      6 \n\nsage/rings/polynomial/plural.pxd in init sage.libs.singular.function (build/cythonized/sage/libs/singular/function.cpp:18713)()\n\nsage/rings/polynomial/plural.pyx in init sage.rings.polynomial.plural (build/cythonized/sage/rings/polynomial/plural.cpp:24145)()\n\nsage/libs/singular/polynomial.pyx in init sage.libs.singular.polynomial (build/cythonized/sage/libs/singular/polynomial.cpp:6414)()\n\nImportError: /home/jpuydt/sage-6.5.beta5/local/lib/python2.7/site-packages/sage/libs/singular/singular.so: undefined symbol: _Z6naInitlP9sip_sring\n\n```\n\n----\nNew commits:",
    "created_at": "2015-02-07T12:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42870",
    "user": "https://trac.sagemath.org/admin/accounts/users/Snark"
}
```

I pushed the branch because it looked nice, but then I tested what happens without the patch... and the result is in fact the same! Indeed, if libsingular.so isn't available, we already have an ImportError because of missing symbols:

```
   /home/jpuydt/sage-6.5.beta5/local/lib/python2.7/site-packages/sage/libs/singular/__init__.py in <module>()
   ---->
   1 from sage.libs.singular.function import singular_function, lib
        global sage.libs.singular.function = undefined
        global singular_function = undefined
        global lib = undefined
      2 
      3 from sage.libs.singular.function_factory import SingularFunctionFactory
      4 
      5 ff = SingularFunctionFactory()
      6 

sage/rings/polynomial/plural.pxd in init sage.libs.singular.function (build/cythonized/sage/libs/singular/function.cpp:18713)()

sage/rings/polynomial/plural.pyx in init sage.rings.polynomial.plural (build/cythonized/sage/rings/polynomial/plural.cpp:24145)()

sage/libs/singular/polynomial.pyx in init sage.libs.singular.polynomial (build/cythonized/sage/libs/singular/polynomial.cpp:6414)()

ImportError: /home/jpuydt/sage-6.5.beta5/local/lib/python2.7/site-packages/sage/libs/singular/singular.so: undefined symbol: _Z6naInitlP9sip_sring

```

----
New commits:



---

archive/issue_comments_042871.json:
```json
{
    "body": "Hi, I would suggest to improve the error handling for loading libSingular even further as in \n\nhttp://git.sagemath.org/sage.git/commit/?id=1e847897b9fce54fa25f1b91dea78f9e225ad0c9\nsee ticket #17254 (upgrade to Singular 4.0.1)\n\n\nThis issue puzzled me for two days, since the error handling was not clean,\nand I failed to interpret the crash messages.\n\n\nAttention: do not pick \n\n```\nlib = os.environ['SAGE_LOCAL']+\"/lib/libSingular.\"+extension # libsingular renamed to libSingular\n```\n\nsince this is only for upgrade to Singular 4.0.1 (libsingular renamed to libSingular)",
    "created_at": "2015-02-07T12:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42871",
    "user": "https://trac.sagemath.org/admin/accounts/users/jakobkroeker"
}
```

Hi, I would suggest to improve the error handling for loading libSingular even further as in 

http://git.sagemath.org/sage.git/commit/?id=1e847897b9fce54fa25f1b91dea78f9e225ad0c9
see ticket #17254 (upgrade to Singular 4.0.1)


This issue puzzled me for two days, since the error handling was not clean,
and I failed to interpret the crash messages.


Attention: do not pick 

```
lib = os.environ['SAGE_LOCAL']+"/lib/libSingular."+extension # libsingular renamed to libSingular
```

since this is only for upgrade to Singular 4.0.1 (libsingular renamed to libSingular)



---

archive/issue_comments_042872.json:
```json
{
    "body": "Replying to [comment:14 jakobkroeker]:\n> Hi, I would suggest to improve the error handling for loading libSingular even further as in \n> \n> http://git.sagemath.org/sage.git/commit/?id=1e847897b9fce54fa25f1b91dea78f9e225ad0c9\n> see ticket #17254 (upgrade to Singular 4.0.1)\n\n\nDid you check that this patch was of any use?\n\nIf libsingular.so can't be loaded, then that file can't either. So any error handling within that file won't ever run, because the missing library will already have triggered an ImportError.\n\nThat is my point in comment:13.",
    "created_at": "2015-02-07T13:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42872",
    "user": "https://trac.sagemath.org/admin/accounts/users/Snark"
}
```

Replying to [comment:14 jakobkroeker]:
> Hi, I would suggest to improve the error handling for loading libSingular even further as in 
> 
> http://git.sagemath.org/sage.git/commit/?id=1e847897b9fce54fa25f1b91dea78f9e225ad0c9
> see ticket #17254 (upgrade to Singular 4.0.1)


Did you check that this patch was of any use?

If libsingular.so can't be loaded, then that file can't either. So any error handling within that file won't ever run, because the missing library will already have triggered an ImportError.

That is my point in comment:13.



---

archive/issue_comments_042873.json:
```json
{
    "body": "> Did you check that this patch was of any use?\n\nI do not exactly understand, what you mean.\n\nMy point is that an error message should be descriptive as possible,\nso if a file cannot be found it should be \n\n```\n   raise OSError, \"did not find libsingular file!\"\n```\n\n\nand if dlopen fails ,it should be something like (I improved the message)\n\n```\n        raise ImportError, \" failed to dlopen \" + lib + \" \"\n```\n\n\nBefore your or mine patch it was even worse,\n(a SIGSEGV because dlerror() is NULL in that case) and that \npuzzled me, since because of the compiled cython stuff I could not exactly see what happened.",
    "created_at": "2015-02-07T13:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42873",
    "user": "https://trac.sagemath.org/admin/accounts/users/jakobkroeker"
}
```

> Did you check that this patch was of any use?

I do not exactly understand, what you mean.

My point is that an error message should be descriptive as possible,
so if a file cannot be found it should be 

```
   raise OSError, "did not find libsingular file!"
```


and if dlopen fails ,it should be something like (I improved the message)

```
        raise ImportError, " failed to dlopen " + lib + " "
```


Before your or mine patch it was even worse,
(a SIGSEGV because dlerror() is NULL in that case) and that 
puzzled me, since because of the compiled cython stuff I could not exactly see what happened.



---

archive/issue_comments_042874.json:
```json
{
    "body": "> That is my point in comment:13.\n\nThat is a different issue. I recall that hit similar errors and for me './sage -ba' solved them, so I guess this are caching issues or  mixing c with c++ issues.\n\nIn case libsingular.so was missing, for me it usually ended in \na SIGSEGV.",
    "created_at": "2015-02-07T13:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42874",
    "user": "https://trac.sagemath.org/admin/accounts/users/jakobkroeker"
}
```

> That is my point in comment:13.

That is a different issue. I recall that hit similar errors and for me './sage -ba' solved them, so I guess this are caching issues or  mixing c with c++ issues.

In case libsingular.so was missing, for me it usually ended in 
a SIGSEGV.



---

archive/issue_comments_042875.json:
```json
{
    "body": "> That is my point in comment:13.\n\nThat is a different issue. I recall that I hit similar errors and for me './sage -ba' solved them, so I guess this are caching issues or  mixing C with C++ issues.\n\nIn case libsingular.so was missing, for me it usually ended in \na SIGSEGV or other strange crashes",
    "created_at": "2015-02-07T13:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42875",
    "user": "https://trac.sagemath.org/admin/accounts/users/jakobkroeker"
}
```

> That is my point in comment:13.

That is a different issue. I recall that I hit similar errors and for me './sage -ba' solved them, so I guess this are caching issues or  mixing C with C++ issues.

In case libsingular.so was missing, for me it usually ended in 
a SIGSEGV or other strange crashes



---

archive/issue_comments_042876.json:
```json
{
    "body": "I'm happy with this patch (would set to positive_review) but I don't quite understand the issues raised above.",
    "created_at": "2015-02-07T13:45:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42876",
    "user": "https://github.com/jdemeyer"
}
```

I'm happy with this patch (would set to positive_review) but I don't quite understand the issues raised above.



---

archive/issue_comments_042877.json:
```json
{
    "body": "> I'm happy with this patch\n\nI'm not happy yet with this patch",
    "created_at": "2015-02-07T14:41:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42877",
    "user": "https://trac.sagemath.org/admin/accounts/users/jakobkroeker"
}
```

> I'm happy with this patch

I'm not happy yet with this patch



---

archive/issue_comments_042878.json:
```json
{
    "body": "I have compiled sage from scratch without my patch, moved libsingular.so, tried to launch sage, got a nice backtrace.\n\nI have compiled sage from scratch with my patch, moved libsingular.so, tried to launch sage, got the same nice backtrace.\n\nThis rules out the case where \"./sage -ba\" would have made things better.\n\nI reiterate my point of comment:13 : that piece of code doesn't get executed if it can't even be loaded itself because libsingular is missing.\n\nI think the correct way to use the dl* functions is with dlsym : you dlopen a library, use dlsym to get the symbol you want, then call it (and you can check every step). That way you don't link-depend on the symbol you want. The current code tries to explicitly load the library, but since it uses directly the functions it wants, it can come into memory only if the linker already opened the lib and found those functions, so playing with dl* is pointless.",
    "created_at": "2015-02-09T07:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42878",
    "user": "https://trac.sagemath.org/admin/accounts/users/Snark"
}
```

I have compiled sage from scratch without my patch, moved libsingular.so, tried to launch sage, got a nice backtrace.

I have compiled sage from scratch with my patch, moved libsingular.so, tried to launch sage, got the same nice backtrace.

This rules out the case where "./sage -ba" would have made things better.

I reiterate my point of comment:13 : that piece of code doesn't get executed if it can't even be loaded itself because libsingular is missing.

I think the correct way to use the dl* functions is with dlsym : you dlopen a library, use dlsym to get the symbol you want, then call it (and you can check every step). That way you don't link-depend on the symbol you want. The current code tries to explicitly load the library, but since it uses directly the functions it wants, it can come into memory only if the linker already opened the lib and found those functions, so playing with dl* is pointless.



---

archive/issue_comments_042879.json:
```json
{
    "body": "> This rules out the case where `./sage -ba` would have made things better.\n\nThe issue happened to me when I tried to update Singular (from 3.1.7 to 4.0.1) in a working branch\n(and will of course not happen if you compile from scratch!; that is equivalent to\n`make distclean` and implies `./sage -ba`\n\nHere are some more hints and  I hope it is reproducible\n\n- Compile from scratch the develop branch  (in doubt use commit d27f8497dcd19d70ec08155888e6fec9c74b839a)\n- merge in changes from http://git.sagemath.org/sage.git/commit/?id=221c5d63e02d7f1d7fdc57cf6c819677553dd262 \n- rename \"/lib/libSingular.\" tp \"/lib/libsingular.\" in singular.pyx\n- build (parallelized) again with `make build -j 6` or something similar;\n\nThen I predict that you may hit something you did hit in comment:13.\nIn fact, I have no idea, how you managed to trigger an `ImportError` as in comment:13\n``\n> so playing with dl* is pointless.\n\nare you sidetracking? I issued something different, namely that an error message should be as descriptive as possible;\nespecially when a file is missing a developer would be happy to see that a file is missing and not an `ImportError` or a SIGSEGV as before",
    "created_at": "2015-02-09T12:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42879",
    "user": "https://trac.sagemath.org/admin/accounts/users/jakobkroeker"
}
```

> This rules out the case where `./sage -ba` would have made things better.

The issue happened to me when I tried to update Singular (from 3.1.7 to 4.0.1) in a working branch
(and will of course not happen if you compile from scratch!; that is equivalent to
`make distclean` and implies `./sage -ba`

Here are some more hints and  I hope it is reproducible

- Compile from scratch the develop branch  (in doubt use commit d27f8497dcd19d70ec08155888e6fec9c74b839a)
- merge in changes from http://git.sagemath.org/sage.git/commit/?id=221c5d63e02d7f1d7fdc57cf6c819677553dd262 
- rename "/lib/libSingular." tp "/lib/libsingular." in singular.pyx
- build (parallelized) again with `make build -j 6` or something similar;

Then I predict that you may hit something you did hit in comment:13.
In fact, I have no idea, how you managed to trigger an `ImportError` as in comment:13
``
> so playing with dl* is pointless.

are you sidetracking? I issued something different, namely that an error message should be as descriptive as possible;
especially when a file is missing a developer would be happy to see that a file is missing and not an `ImportError` or a SIGSEGV as before



---

archive/issue_comments_042880.json:
```json
{
    "body": "`@`Snark\nit is likely that I cannot exactly recall, how I triggered  ImportError ,\nmaybe it was by removing the shared library and only keeping the static one.\nI hope that it does not matter anyway.",
    "created_at": "2015-02-09T15:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42880",
    "user": "https://trac.sagemath.org/admin/accounts/users/jakobkroeker"
}
```

`@`Snark
it is likely that I cannot exactly recall, how I triggered  ImportError ,
maybe it was by removing the shared library and only keeping the static one.
I hope that it does not matter anyway.



---

archive/issue_comments_042881.json:
```json
{
    "body": "Deleted post to try the issue reported in \nhttps://groups.google.com/d/msg/sage-devel/IpeIDqTo4mE/hzs3cLA3N_YJ",
    "created_at": "2015-02-10T01:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42881",
    "user": "https://github.com/vbraun"
}
```

Deleted post to try the issue reported in 
https://groups.google.com/d/msg/sage-devel/IpeIDqTo4mE/hzs3cLA3N_YJ



---

archive/issue_comments_042882.json:
```json
{
    "body": "I'm a little at loss as to how I'll improve the patch : I don't exactly know how to reproduce the issue.\n\nIndeed, what kind of error will that code detect? It will only trigger when the library will have been loaded in memory (because it links to it), but for some reason cannot be reloaded with the new RTLD_* flags!",
    "created_at": "2015-02-18T10:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42882",
    "user": "https://trac.sagemath.org/admin/accounts/users/Snark"
}
```

I'm a little at loss as to how I'll improve the patch : I don't exactly know how to reproduce the issue.

Indeed, what kind of error will that code detect? It will only trigger when the library will have been loaded in memory (because it links to it), but for some reason cannot be reloaded with the new RTLD_* flags!



---

archive/issue_comments_042883.json:
```json
{
    "body": "> Indeed, what kind of error will that code detect?\n> It will only trigger when the library will have been loaded in memory (because it links to it)\n\nI'm not sure, but it seems you can't see the case I described, because you are too focused on the scenario you have in mind. Try to think \"what may happen\", not \"what do we want to achieve\"\n``\nCase 1: \n The name of the library is _hardcoded_ in 'singular.pyx', so we might get an issue if there is a typo or the name of the library changed. That happened in Singular 4.0.1, so I was able to compile sage, but then dlopen tried to open a file which did not exist.\n\ncase 2: \n> It will only trigger when the library will have been loaded in memory (because it links to it), but for some reason cannot be reloaded with the new RTLD_* flags!\nExactly. Who knows why dlopen() may fail, so better catch it and watch out for dlerror() == NULL",
    "created_at": "2015-02-18T11:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42883",
    "user": "https://trac.sagemath.org/admin/accounts/users/jakobkroeker"
}
```

> Indeed, what kind of error will that code detect?
> It will only trigger when the library will have been loaded in memory (because it links to it)

I'm not sure, but it seems you can't see the case I described, because you are too focused on the scenario you have in mind. Try to think "what may happen", not "what do we want to achieve"
``
Case 1: 
 The name of the library is _hardcoded_ in 'singular.pyx', so we might get an issue if there is a typo or the name of the library changed. That happened in Singular 4.0.1, so I was able to compile sage, but then dlopen tried to open a file which did not exist.

case 2: 
> It will only trigger when the library will have been loaded in memory (because it links to it), but for some reason cannot be reloaded with the new RTLD_* flags!
Exactly. Who knows why dlopen() may fail, so better catch it and watch out for dlerror() == NULL



---

archive/issue_comments_042884.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-14T07:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42884",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_042885.json:
```json
{
    "body": "Ok, I tried to rebase my branch and make a better change.",
    "created_at": "2015-03-14T07:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42885",
    "user": "https://trac.sagemath.org/admin/accounts/users/Snark"
}
```

Ok, I tried to rebase my branch and make a better change.



---

archive/issue_comments_042886.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-03-14T07:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42886",
    "user": "https://trac.sagemath.org/admin/accounts/users/Snark"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042887.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-03-23T18:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42887",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_005772.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-03-24T10:48:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5522#event-5772"
}
```



---

archive/issue_comments_042888.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-03-24T10:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5522#issuecomment-42888",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
