# Issue 7987: Most extensions don't need to be listed in module_list

archive/issues_007987.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @williamstein @mwhansen @jasongrout @nexttime\n\nUnless special libraries or C flags are needed, we can auto-generate almost this whole list, which simplifies the making of new .pyx files in the standard library.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7987\n\n",
    "created_at": "2010-01-19T01:49:00Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Most extensions don't need to be listed in module_list",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7987",
    "user": "https://github.com/robertwb"
}
```
Assignee: GeorgSWeber

CC:  @williamstein @mwhansen @jasongrout @nexttime

Unless special libraries or C flags are needed, we can auto-generate almost this whole list, which simplifies the making of new .pyx files in the standard library.

Issue created by migration from https://trac.sagemath.org/ticket/7987





---

archive/issue_comments_069631.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T01:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69631",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069632.json:
```json
{
    "body": "Eventually, the library, include, and language information should be able to be pulled out of the files themselves by Cython...",
    "created_at": "2010-01-19T01:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69632",
    "user": "https://github.com/robertwb"
}
```

Eventually, the library, include, and language information should be able to be pulled out of the files themselves by Cython...



---

archive/issue_comments_069633.json:
```json
{
    "body": "Attachment [7987-module_list-cleanup.patch](tarball://root/attachments/some-uuid/ticket7987/7987-module_list-cleanup.patch) by @robertwb created at 2010-01-19 21:57:49",
    "created_at": "2010-01-19T21:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69633",
    "user": "https://github.com/robertwb"
}
```

Attachment [7987-module_list-cleanup.patch](tarball://root/attachments/some-uuid/ticket7987/7987-module_list-cleanup.patch) by @robertwb created at 2010-01-19 21:57:49



---

archive/issue_comments_069634.json:
```json
{
    "body": "Eventually, this should be part of Cython. Also, clang, clib, etc. should be allowed in .pxd files and be transitive (for example, everything using Pynac or NTL would automatically be C++ and get the right library).",
    "created_at": "2010-02-21T02:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69634",
    "user": "https://github.com/robertwb"
}
```

Eventually, this should be part of Cython. Also, clang, clib, etc. should be allowed in .pxd files and be transitive (for example, everything using Pynac or NTL would automatically be C++ and get the right library).



---

archive/issue_comments_069635.json:
```json
{
    "body": "I will probably implement something like this in Cython directly, though of course heavily inspired by what we want for Sage.",
    "created_at": "2010-04-25T06:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69635",
    "user": "https://github.com/robertwb"
}
```

I will probably implement something like this in Cython directly, though of course heavily inspired by what we want for Sage.



---

archive/issue_comments_069636.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-03T00:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69636",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069637.json:
```json
{
    "body": "Not surprising (see ticket description), the patches need to be rebased.\n\nThe merged Cygwin patch involved many changes to `module_list.py`, too.\n\nBtw, IMHO `libcsage` and `libstdcxx` should **not** be \"linked\" unconditionally (especially regardless of the module's `language`) to each and every module.\n(I recently started sorting out which modules really directly use `libcsage`, and did add `\"stdcxx\"` to `libraries` only if `language==\"c++\"`. Currently suspended work in progress...)",
    "created_at": "2010-06-03T00:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69637",
    "user": "https://github.com/nexttime"
}
```

Not surprising (see ticket description), the patches need to be rebased.

The merged Cygwin patch involved many changes to `module_list.py`, too.

Btw, IMHO `libcsage` and `libstdcxx` should **not** be "linked" unconditionally (especially regardless of the module's `language`) to each and every module.
(I recently started sorting out which modules really directly use `libcsage`, and did add `"stdcxx"` to `libraries` only if `language=="c++"`. Currently suspended work in progress...)



---

archive/issue_comments_069638.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n\n> Btw, IMHO `libcsage` and `libstdcxx` should **not** be \"linked\" unconditionally (especially regardless of the module's `language`) to each and every module.\n> (I recently started sorting out which modules really directly use `libcsage`, and did add `\"stdcxx\"` to `libraries` only if `language==\"c++\"`. Currently suspended work in progress...)\n\nFor sure, but I figured it'd be better to refractor and clean things up in separate steps (in case one or the other has unintended consequences). \n\nFor the record, I plan to add this functionality to Cython soon (including transitivity of library dependance), so that may make this patch invalid. Sorting what modules actually need what will be very useful though.",
    "created_at": "2010-06-03T00:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69638",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:7 leif]:

> Btw, IMHO `libcsage` and `libstdcxx` should **not** be "linked" unconditionally (especially regardless of the module's `language`) to each and every module.
> (I recently started sorting out which modules really directly use `libcsage`, and did add `"stdcxx"` to `libraries` only if `language=="c++"`. Currently suspended work in progress...)

For sure, but I figured it'd be better to refractor and clean things up in separate steps (in case one or the other has unintended consequences). 

For the record, I plan to add this functionality to Cython soon (including transitivity of library dependance), so that may make this patch invalid. Sorting what modules actually need what will be very useful though.



---

archive/issue_comments_069639.json:
```json
{
    "body": "Replying to [comment:8 robertwb]:\n> Replying to [comment:7 leif]:\n> \n> > Btw, IMHO `libcsage` and `libstdcxx` should **not** be \"linked\" unconditionally (especially regardless of the module's `language`) to each and every module.\n> > (I recently started sorting out which modules really directly use `libcsage`, and did add `\"stdcxx\"` to `libraries` only if `language==\"c++\"`. Currently suspended work in progress...)\n> \n> For sure, but I figured it'd be better to refractor and clean things up in separate steps (in case one or the other has unintended consequences).\n\nYes. The unconditional inclusion is anyhow performed in `setup.py`. \n\n> For the record, I plan to add this functionality to Cython soon (including transitivity of library dependance), so that may make this patch invalid. Sorting what modules actually need what will be very useful though. \n\nI just wanted to decrease the number of tickets needing review. ;-)\n\nP.S.: `s/stdcxx/stdc++/`",
    "created_at": "2010-06-03T01:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69639",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:8 robertwb]:
> Replying to [comment:7 leif]:
> 
> > Btw, IMHO `libcsage` and `libstdcxx` should **not** be "linked" unconditionally (especially regardless of the module's `language`) to each and every module.
> > (I recently started sorting out which modules really directly use `libcsage`, and did add `"stdcxx"` to `libraries` only if `language=="c++"`. Currently suspended work in progress...)
> 
> For sure, but I figured it'd be better to refractor and clean things up in separate steps (in case one or the other has unintended consequences).

Yes. The unconditional inclusion is anyhow performed in `setup.py`. 

> For the record, I plan to add this functionality to Cython soon (including transitivity of library dependance), so that may make this patch invalid. Sorting what modules actually need what will be very useful though. 

I just wanted to decrease the number of tickets needing review. ;-)

P.S.: `s/stdcxx/stdc++/`



---

archive/issue_comments_069640.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2013-03-15T09:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69640",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_069641.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2015-04-13T07:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69641",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_069642.json:
```json
{
    "body": "Replying to [ticket:7987 jdemeyer]:\n> See also #15140.\n\nSure?",
    "created_at": "2015-04-13T09:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69642",
    "user": "https://github.com/nexttime"
}
```

Replying to [ticket:7987 jdemeyer]:
> See also #15140.

Sure?



---

archive/issue_comments_069643.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2015-04-13T09:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69643",
    "user": "https://github.com/nexttime"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_069644.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2015-06-24T11:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69644",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_069645.json:
```json
{
    "body": "This is way too outdated to apply, it also incorrectly adds the libraries to `.pyx` files instead of `.pxd` files (see #18450) and several parts of this have already been done.",
    "created_at": "2015-06-24T11:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69645",
    "user": "https://github.com/jdemeyer"
}
```

This is way too outdated to apply, it also incorrectly adds the libraries to `.pyx` files instead of `.pxd` files (see #18450) and several parts of this have already been done.



---

archive/issue_events_008202.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2015-07-17T20:05:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7987#event-8202"
}
```



---

archive/issue_comments_069646.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-07-17T20:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7987#issuecomment-69646",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
