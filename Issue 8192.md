# Issue 8192: Update PolyBoRi to newest upstream release

archive/issues_008192.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  polybori burcin\n\n* gat parser added\n  * Disabled keyboard interrupt handling (but re-raised)\n  * Fixed critical bug in normal form\n  * Naming convention: `minimalElements` -> `minimal_elements`\n  * has_constant_part for variable/monomial\n  * `lead/lex_lead/lead_deg/lex_lead_deg` also for Variable/Monomial\n  * iterator for literal factorization\n  * Added treatment of customizable settings for `BOOST_LIBRARY`,`SHCFLAGS`, `SHCCFLAGS`, and `SHCXXFLAGS`\n  * Improved Sun Studio compatibility\n  * Fix for hpux (CUDD needs `pwd.h`)\n}}}\n\nThis should be relatively straight forward then.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8192\n\n",
    "created_at": "2010-02-05T10:59:50Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "Update PolyBoRi to newest upstream release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8192",
    "user": "malb"
}
```
Assignee: tbd

CC:  polybori burcin

* gat parser added
  * Disabled keyboard interrupt handling (but re-raised)
  * Fixed critical bug in normal form
  * Naming convention: `minimalElements` -> `minimal_elements`
  * has_constant_part for variable/monomial
  * `lead/lex_lead/lead_deg/lex_lead_deg` also for Variable/Monomial
  * iterator for literal factorization
  * Added treatment of customizable settings for `BOOST_LIBRARY`,`SHCFLAGS`, `SHCCFLAGS`, and `SHCXXFLAGS`
  * Improved Sun Studio compatibility
  * Fix for hpux (CUDD needs `pwd.h`)
}}}

This should be relatively straight forward then.

Issue created by migration from https://trac.sagemath.org/ticket/8192





---

archive/issue_comments_072222.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-12T14:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72222",
    "user": "PolyBoRi"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072223.json:
```json
{
    "body": "Burcin and I prepared the Package:\n\nhttp://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4.spkg\n\nRegards,\n  Alexander Dreyer",
    "created_at": "2010-03-12T14:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72223",
    "user": "PolyBoRi"
}
```

Burcin and I prepared the Package:

http://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4.spkg

Regards,
  Alexander Dreyer



---

archive/issue_comments_072224.json:
```json
{
    "body": "Changing assignee from tbd to PolyBoRi.",
    "created_at": "2010-03-12T14:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72224",
    "user": "PolyBoRi"
}
```

Changing assignee from tbd to PolyBoRi.



---

archive/issue_comments_072225.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-04-05T19:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72225",
    "user": "malb"
}
```

Looks good.



---

archive/issue_comments_072226.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T19:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72226",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072227.json:
```json
{
    "body": "Do you know why the spkg is so small?\n\n```\npalmieri@sage:~$ ls -l /home/dreyer/spkg/polybori-0.6.4.spkg \n... 2040576 2010-03-12 06:13 /home/dreyer/spkg/polybori-0.6.4.spkg\npalmieri@sage:~$ ls -l /home/release/sage-4.3.5/sage-4.3.5/spkg/standard/polybori-0.6.3-20091028.spkg \n... 6825939 2010-02-11 08:56 /home/release/sage-4.3.5/sage-4.3.5/spkg/standard/polybori-0.6.3-20091028.spkg\n```\n\nI'm not complaining, but I'm curious.",
    "created_at": "2010-04-19T21:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72227",
    "user": "jhpalmieri"
}
```

Do you know why the spkg is so small?

```
palmieri@sage:~$ ls -l /home/dreyer/spkg/polybori-0.6.4.spkg 
... 2040576 2010-03-12 06:13 /home/dreyer/spkg/polybori-0.6.4.spkg
palmieri@sage:~$ ls -l /home/release/sage-4.3.5/sage-4.3.5/spkg/standard/polybori-0.6.3-20091028.spkg 
... 6825939 2010-02-11 08:56 /home/release/sage-4.3.5/sage-4.3.5/spkg/standard/polybori-0.6.3-20091028.spkg
```

I'm not complaining, but I'm curious.



---

archive/issue_comments_072228.json:
```json
{
    "body": "Indeed, the polybori-0-6-3*spkg's contain a clone of PolyBoRi's mercurial repository as well a a mercurial repository of the Sage-related patches,  The polybori-0-6-4.spkg only has the patch repo. \n\nWhat is Sage's policy here?\n\nBest regards,\n  Alexander",
    "created_at": "2010-04-20T08:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72228",
    "user": "PolyBoRi"
}
```

Indeed, the polybori-0-6-3*spkg's contain a clone of PolyBoRi's mercurial repository as well a a mercurial repository of the Sage-related patches,  The polybori-0-6-4.spkg only has the patch repo. 

What is Sage's policy here?

Best regards,
  Alexander



---

archive/issue_comments_072229.json:
```json
{
    "body": "I don't think there is a policy, but it seems to be okay to delete an upstream mercurial repository like this.",
    "created_at": "2010-04-21T16:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72229",
    "user": "jhpalmieri"
}
```

I don't think there is a policy, but it seems to be okay to delete an upstream mercurial repository like this.



---

archive/issue_comments_072230.json:
```json
{
    "body": "This does not build on Cygwin due to missing libpng12 and libz.  I've posted an spkg which fixes this at\n\nhttp://sage.math.washington.edu/home/mhansen/cygwin_port/polybori-0.6.4.spkg\n\nCould someone review my changes?  Otherwise, I can make a new ticket for this.",
    "created_at": "2010-04-27T07:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72230",
    "user": "mhansen"
}
```

This does not build on Cygwin due to missing libpng12 and libz.  I've posted an spkg which fixes this at

http://sage.math.washington.edu/home/mhansen/cygwin_port/polybori-0.6.4.spkg

Could someone review my changes?  Otherwise, I can make a new ticket for this.



---

archive/issue_comments_072231.json:
```json
{
    "body": "Hi Mike,\n\nI'm afraid your SPKG will need a new ticket since this one was merged in 4.4 already. \n\nYour SPKG builds fine on sage.math, however I get\n\n\n```\nExiting Sage (CPU time 0m0.06s, Wall time 0m0.88s).\n*** glibc detected *** python: corrupted double-linked list: 0x000000000329b9c0 ***\n======= Backtrace: =========\n/lib/libc.so.6[0x7fccf4577663]\n/lib/libc.so.6[0x7fccf4578ea1]\n/lib/libc.so.6(cfree+0x8c)[0x7fccf457cc1c]\n/lib/libc.so.6(exit+0xe0)[0x7fccf453a110]\npython[0x4baac3]\npython(PyErr_PrintEx+0x19a)[0x4bacca]\npython(PyRun_SimpleFileExFlags+0x116)[0x4bb926]\npython(Py_Main+0x984)[0x416354]\n/lib/libc.so.6(__libc_start_main+0xf4)[0x7fccf45231c4]\npython[0x415629]\n```\n\n\nwhich is likely unrelated to your SPKG? I will build a fresh 4.4 to check.",
    "created_at": "2010-04-27T17:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72231",
    "user": "malb"
}
```

Hi Mike,

I'm afraid your SPKG will need a new ticket since this one was merged in 4.4 already. 

Your SPKG builds fine on sage.math, however I get


```
Exiting Sage (CPU time 0m0.06s, Wall time 0m0.88s).
*** glibc detected *** python: corrupted double-linked list: 0x000000000329b9c0 ***
======= Backtrace: =========
/lib/libc.so.6[0x7fccf4577663]
/lib/libc.so.6[0x7fccf4578ea1]
/lib/libc.so.6(cfree+0x8c)[0x7fccf457cc1c]
/lib/libc.so.6(exit+0xe0)[0x7fccf453a110]
python[0x4baac3]
python(PyErr_PrintEx+0x19a)[0x4bacca]
python(PyRun_SimpleFileExFlags+0x116)[0x4bb926]
python(Py_Main+0x984)[0x416354]
/lib/libc.so.6(__libc_start_main+0xf4)[0x7fccf45231c4]
python[0x415629]
```


which is likely unrelated to your SPKG? I will build a fresh 4.4 to check.



---

archive/issue_comments_072232.json:
```json
{
    "body": "Okay, I'll open a new ticket. Shouldn't this ticket have been closed when it was merged into 4.4?",
    "created_at": "2010-04-27T17:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72232",
    "user": "mhansen"
}
```

Okay, I'll open a new ticket. Shouldn't this ticket have been closed when it was merged into 4.4?



---

archive/issue_comments_072233.json:
```json
{
    "body": "Argh, I mixed it up. No it isn't merged, so no new ticket needed.",
    "created_at": "2010-04-27T17:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72233",
    "user": "malb"
}
```

Argh, I mixed it up. No it isn't merged, so no new ticket needed.



---

archive/issue_comments_072234.json:
```json
{
    "body": "SPKG looks good, the bug reported above had nothing to do with the SPKG. Running doctests now, if they pass this should be a positive review.",
    "created_at": "2010-04-27T17:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72234",
    "user": "malb"
}
```

SPKG looks good, the bug reported above had nothing to do with the SPKG. Running doctests now, if they pass this should be a positive review.



---

archive/issue_comments_072235.json:
```json
{
    "body": "Thanks!",
    "created_at": "2010-04-27T17:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72235",
    "user": "mhansen"
}
```

Thanks!



---

archive/issue_comments_072236.json:
```json
{
    "body": "Mhh, can you try your SPKG on sage.math? It seems it does produce a fair amount of segfaults.",
    "created_at": "2010-04-27T19:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72236",
    "user": "malb"
}
```

Mhh, can you try your SPKG on sage.math? It seems it does produce a fair amount of segfaults.



---

archive/issue_comments_072237.json:
```json
{
    "body": "Sure.",
    "created_at": "2010-04-27T19:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72237",
    "user": "mhansen"
}
```

Sure.



---

archive/issue_comments_072238.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-28T19:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72238",
    "user": "was"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_072239.json:
```json
{
    "body": "given the report of segfaults above, I'm changing this to needs work!",
    "created_at": "2010-04-28T19:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72239",
    "user": "was"
}
```

given the report of segfaults above, I'm changing this to needs work!



---

archive/issue_comments_072240.json:
```json
{
    "body": "Replying to [comment:18 was]:\n> given the report of segfaults above, I'm changing this to needs work!\n\nOr you could merge the package which got a positive review and we move the Cygwin problems to a different ticket.\n\nhttp://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4.spkg",
    "created_at": "2010-04-28T19:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72240",
    "user": "burcin"
}
```

Replying to [comment:18 was]:
> given the report of segfaults above, I'm changing this to needs work!

Or you could merge the package which got a positive review and we move the Cygwin problems to a different ticket.

http://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4.spkg



---

archive/issue_comments_072241.json:
```json
{
    "body": "Yep, I think using that one would be fine for now.  I'll look into these segfaults and make a new ticket.",
    "created_at": "2010-04-28T21:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72241",
    "user": "mhansen"
}
```

Yep, I think using that one would be fine for now.  I'll look into these segfaults and make a new ticket.



---

archive/issue_comments_072242.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-28T21:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72242",
    "user": "mhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072243.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-28T21:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72243",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072244.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T00:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72244",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_072245.json:
```json
{
    "body": "Both the 0.6.4.spkgs here give those crashes reported above, but only once in every 10-15 runs.\n\nValgrind shows invalid reads/writes on exit pointing to polybori:\n\n\n```\n==14880== Invalid read of size 4\n==14880==    at 0x30CE3642: __tcf_1 (sp_counted_base_gcc_x86.hpp:50)\n==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)\n==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)\n==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)\n==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)\n==14880==    by 0x4164C4: Py_Main (main.c:142)\n==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)\n==14880==  Address 0x3225a538 is not stack'd, malloc'd or (recently) free'd\n==14880== \n==14880== Invalid read of size 8\n==14880==    at 0x30CE365C: __tcf_1 (CCuddCore.h:208)\n==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)\n==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)\n==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)\n==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)\n==14880==    by 0x4164C4: Py_Main (main.c:142)\n==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)\n==14880==  Address 0x31a599e8 is 8 bytes inside a block of size 64 free'd\n==14880==    at 0x4C2216E: operator delete(void*) (vg_replace_malloc.c:346)\n==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)\n==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)\n==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)\n==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)\n==14880==    by 0x4164C4: Py_Main (main.c:142)\n==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)\n==14880== \n==14880== Invalid write of size 8\n==14880==    at 0x30CE3667: __tcf_1 (CCuddCore.h:208)\n==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)\n==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)\n==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)\n==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)\n==14880==    by 0x4164C4: Py_Main (main.c:142)\n==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)\n==14880==  Address 0x31a599e8 is 8 bytes inside a block of size 64 free'd\n==14880==    at 0x4C2216E: operator delete(void*) (vg_replace_malloc.c:346)\n==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)\n==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)\n==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)\n==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)\n==14880==    by 0x4164C4: Py_Main (main.c:142)\n==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)\n```\n",
    "created_at": "2010-04-29T12:41:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72245",
    "user": "wjp"
}
```

Both the 0.6.4.spkgs here give those crashes reported above, but only once in every 10-15 runs.

Valgrind shows invalid reads/writes on exit pointing to polybori:


```
==14880== Invalid read of size 4
==14880==    at 0x30CE3642: __tcf_1 (sp_counted_base_gcc_x86.hpp:50)
==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)
==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)
==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)
==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)
==14880==    by 0x4164C4: Py_Main (main.c:142)
==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)
==14880==  Address 0x3225a538 is not stack'd, malloc'd or (recently) free'd
==14880== 
==14880== Invalid read of size 8
==14880==    at 0x30CE365C: __tcf_1 (CCuddCore.h:208)
==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)
==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)
==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)
==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)
==14880==    by 0x4164C4: Py_Main (main.c:142)
==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)
==14880==  Address 0x31a599e8 is 8 bytes inside a block of size 64 free'd
==14880==    at 0x4C2216E: operator delete(void*) (vg_replace_malloc.c:346)
==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)
==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)
==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)
==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)
==14880==    by 0x4164C4: Py_Main (main.c:142)
==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)
==14880== 
==14880== Invalid write of size 8
==14880==    at 0x30CE3667: __tcf_1 (CCuddCore.h:208)
==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)
==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)
==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)
==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)
==14880==    by 0x4164C4: Py_Main (main.c:142)
==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)
==14880==  Address 0x31a599e8 is 8 bytes inside a block of size 64 free'd
==14880==    at 0x4C2216E: operator delete(void*) (vg_replace_malloc.c:346)
==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)
==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)
==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)
==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)
==14880==    by 0x4164C4: Py_Main (main.c:142)
==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)
```




---

archive/issue_comments_072246.json:
```json
{
    "body": "Hi Willem Jan,\n\nThe crashes are probably caused by the fact that I disabled the code that statically links polybori in the new package. IIRC, we were doing that exactly because of these double free errors. We tested the new package on different platforms, and didn't see the crashes, so we assumed the problem was fixed.\n\nI don't have time to reproduce the problem, or test new packages at the moment. Can you try enabling the static build and try again?\n\nFrom the diff of the changes (of an earlier version of the package in Alexander Dreyer's home dir), this looks like the relevant change:\n\n\n```\ndiff --git a/patches/SConstruct b/patches/SConstruct\n--- a/patches/SConstruct\n+++ b/patches/SConstruct\n@@ -561,7 +581,7 @@\n gb_src = [GBPath('src', source) for source in gb_src]\n if not(external_m4ri):\n    gb_src += m4ri\n-gb=env.StaticLibrary(GBPath('groebner'), gb_src+[libpb])\n+gb=env.StaticLibrary(GBPath('groebner'), gb_src)#+[libpb])\n \n #print \"gb:\", gb, dir(gb)\n #sometimes l seems to be boxed by a list\n```\n\n\n\nBTW, this also looks suspect to me:\n\n\n```\ndiff --git a/patches/SConstruct b/patches/SConstruct\n--- a/patches/SConstruct\n+++ b/patches/SConstruct\n@@ -327,7 +350,7 @@\n Help(opts.GenerateHelpText(env))\n \n have_l2h = have_t4h = False\n-external_m4ri = True\n+external_m4ri = False\n \n if not env.GetOption('clean'):\n     conf = Configure(env)\n```\n\n\nMany thanks for looking into this.",
    "created_at": "2010-04-29T13:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72246",
    "user": "burcin"
}
```

Hi Willem Jan,

The crashes are probably caused by the fact that I disabled the code that statically links polybori in the new package. IIRC, we were doing that exactly because of these double free errors. We tested the new package on different platforms, and didn't see the crashes, so we assumed the problem was fixed.

I don't have time to reproduce the problem, or test new packages at the moment. Can you try enabling the static build and try again?

From the diff of the changes (of an earlier version of the package in Alexander Dreyer's home dir), this looks like the relevant change:


```
diff --git a/patches/SConstruct b/patches/SConstruct
--- a/patches/SConstruct
+++ b/patches/SConstruct
@@ -561,7 +581,7 @@
 gb_src = [GBPath('src', source) for source in gb_src]
 if not(external_m4ri):
    gb_src += m4ri
-gb=env.StaticLibrary(GBPath('groebner'), gb_src+[libpb])
+gb=env.StaticLibrary(GBPath('groebner'), gb_src)#+[libpb])
 
 #print "gb:", gb, dir(gb)
 #sometimes l seems to be boxed by a list
```



BTW, this also looks suspect to me:


```
diff --git a/patches/SConstruct b/patches/SConstruct
--- a/patches/SConstruct
+++ b/patches/SConstruct
@@ -327,7 +350,7 @@
 Help(opts.GenerateHelpText(env))
 
 have_l2h = have_t4h = False
-external_m4ri = True
+external_m4ri = False
 
 if not env.GetOption('clean'):
     conf = Configure(env)
```


Many thanks for looking into this.



---

archive/issue_comments_072247.json:
```json
{
    "body": "Hi Burcin,\n\nI think, we removed  the call of` remove_dylib`\u00a0 from `spkg-install`. So reintroducing `remove_dylib` may fit it already.\n\nRegards,\n\n\u00a0 Alexander Dreyer",
    "created_at": "2010-04-29T13:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72247",
    "user": "PolyBoRi"
}
```

Hi Burcin,

I think, we removed  the call of` remove_dylib`  from `spkg-install`. So reintroducing `remove_dylib` may fit it already.

Regards,

  Alexander Dreyer



---

archive/issue_comments_072248.json:
```json
{
    "body": "> BTW, this also looks suspect to me:\n> \n> {{{\n> diff --git a/patches/SConstruct b/patches/SConstruct\n> --- a/patches/SConstruct\n> +++ b/patches/SConstruct\n> `@``@` -327,7 +350,7 `@``@`\n>  Help(opts.GenerateHelpText(env))\n>  \n>  have_l2h = have_t4h = False\n> -external_m4ri = True\n> +external_m4ri = False\n>  \n>  if not env.GetOption('clean'):\n>      conf = Configure(env)\n> }}}\n\nI agree, that this wrong and should be reverted (we really want the external M4RI)",
    "created_at": "2010-04-29T13:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72248",
    "user": "malb"
}
```

> BTW, this also looks suspect to me:
> 
> {{{
> diff --git a/patches/SConstruct b/patches/SConstruct
> --- a/patches/SConstruct
> +++ b/patches/SConstruct
> `@``@` -327,7 +350,7 `@``@`
>  Help(opts.GenerateHelpText(env))
>  
>  have_l2h = have_t4h = False
> -external_m4ri = True
> +external_m4ri = False
>  
>  if not env.GetOption('clean'):
>      conf = Configure(env)
> }}}

I agree, that this wrong and should be reverted (we really want the external M4RI)



---

archive/issue_comments_072249.json:
```json
{
    "body": "Hi malb,\n\nright, but this is only the inital value of an internal variable. Later in the Sconstruct file, external_m4ri will be set to True, if the library is found.\n\nRegards,\n\n\u00a0 Alexander Dreyer",
    "created_at": "2010-04-29T13:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72249",
    "user": "PolyBoRi"
}
```

Hi malb,

right, but this is only the inital value of an internal variable. Later in the Sconstruct file, external_m4ri will be set to True, if the library is found.

Regards,

  Alexander Dreyer



---

archive/issue_comments_072250.json:
```json
{
    "body": "I don't have time to extensively test right now, so I tried both reverting the patch that Burcin gave above and reintroducing remove_dylib at the same time. That fixed the problems.\n\nSo you're definitely on the right track, but I'll leave it to you to figure out what exactly needs to be changed for a new spkg :-)",
    "created_at": "2010-04-29T14:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72250",
    "user": "wjp"
}
```

I don't have time to extensively test right now, so I tried both reverting the patch that Burcin gave above and reintroducing remove_dylib at the same time. That fixed the problems.

So you're definitely on the right track, but I'll leave it to you to figure out what exactly needs to be changed for a new spkg :-)



---

archive/issue_comments_072251.json:
```json
{
    "body": "Hi Willem Jan,\n\nI changed than remove_dynlib only at:\n\n!http://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4-p1.spkg\n\nIs this enough to fix the problem?\n\nSince I was not able to reproduce the problem: Can you test it? (How do you run it?)\n\nBest regards,\n\n\n  Alexander Dreyer",
    "created_at": "2010-04-29T14:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72251",
    "user": "PolyBoRi"
}
```

Hi Willem Jan,

I changed than remove_dynlib only at:

!http://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4-p1.spkg

Is this enough to fix the problem?

Since I was not able to reproduce the problem: Can you test it? (How do you run it?)

Best regards,


  Alexander Dreyer



---

archive/issue_comments_072252.json:
```json
{
    "body": "Hi Alexander,\n\nYes, I don't get the errors anymore with that package. (After renaming the spkg to polybori-0.6.4.p1.spkg and the directory inside it to match the spkg filename.)\n\nI test it by running sage through valgrind and seeing if there are any errors on exit in polybori files, since the actual crashes happen here only once every 10-15 runs or so.\n\n\nStill I can't help but wonder if there's something subtle going wrong with sage's interface to polybori or in polybori itself on exit to require static linking. Maybe something like multiple libraries sharing a global memory manager and each of them trying to clean up global structures on quit or something similar...\n\n\nThanks!\n-Willem Jan",
    "created_at": "2010-04-29T15:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72252",
    "user": "wjp"
}
```

Hi Alexander,

Yes, I don't get the errors anymore with that package. (After renaming the spkg to polybori-0.6.4.p1.spkg and the directory inside it to match the spkg filename.)

I test it by running sage through valgrind and seeing if there are any errors on exit in polybori files, since the actual crashes happen here only once every 10-15 runs or so.


Still I can't help but wonder if there's something subtle going wrong with sage's interface to polybori or in polybori itself on exit to require static linking. Maybe something like multiple libraries sharing a global memory manager and each of them trying to clean up global structures on quit or something similar...


Thanks!
-Willem Jan



---

archive/issue_comments_072253.json:
```json
{
    "body": "From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ff294013a41ea05c):\n\n\n\nSage 4.4.1.alpha2 contains two PolyBoRi spkg's:\n\n* polybori-0.6.3-20091028.spkg\n* polybori-0.6.4.spkg\n\nI think polybori-0.6.4.spkg is the newer one, so I deleted the other one from `SAGE_ROOT/spkg/standard/`. Here's a diff between the `spkg-install` of polybori-0.6.3-20091028.spkg and polybori-0.6.4.spkg:\n\n\n```diff\n[mvngu@sage mvngu]$ diff -Naur polybori-0.6.3-20091028/spkg-install polybori-0.6.4.p0/spkg-install \n--- polybori-0.6.3-20091028/spkg-install\t2009-05-17 10:31:16.000000000 -0700\n+++ polybori-0.6.4.p0/spkg-install\t2010-04-29 07:10:46.000000000 -0700\n@@ -6,14 +6,14 @@\n    exit 1\n fi\n \n-PBDIR=polybori-0.6\n+PBDIR=polybori-0.6.4\n WORKDIR=${PWD}/src\n SCONS=scons\n \n # For some strange reason the installed boost in $SAGE_LOCAL causes \n # make install failures, so copy it over. \n-mkdir src/boost_1_34_1.cropped\n-cp -r $SAGE_LOCAL/include/boost src/boost_1_34_1.cropped\n+#mkdir src/boost_1_34_1.cropped\n+#cp -r $SAGE_LOCAL/include/boost src/boost_1_34_1.cropped\n BOOSTDIR=boost_1_34_1.cropped\n \n patch() \n@@ -26,9 +26,6 @@\n \n     cp patches/SConstruct src/${PBDIR}/SConstruct\n     cp patches/PyPolyBoRi.py src/${PBDIR}/pyroot/polybori\n-\n-    # workaround so will build on cygwin\n-    cp patches/cpu_stats.c src/${PBDIR}/Cudd/util/cpu_stats.c\n }\n \n \n@@ -68,7 +65,7 @@\n \n remove_dylib()\n {\n-    # linking dynmic libraries causes segfaults at exit (see #2822)\n+    # linking dynamic libraries causes segfaults at exit (see #2822)\n     if [ `uname` = \"Darwin\" ]; then\n         rm -f $SAGE_LOCAL/lib/libpolybori.dylib\n         rm -f $SAGE_LOCAL/lib/libpboriCudd.dylib\n@@ -101,9 +98,3 @@\n echo \"Removing dynamic libraries...\"\n remove_dylib\n echo \"Done removing dynamic libraries.\"\n-\n-# force a rebuild of the PolyBoRi extension\n-if [ -f $SAGE_ROOT/devel/sage/sage/rings/polynomial/pbori.pyx ]; then\n-    touch $SAGE_ROOT/devel/sage/sage/rings/polynomial/pbori.pyx\n-fi\n-\n```\n\n\nI replaced polybori-0.6.4.spkg with\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/polybori/polybori-0.6.4.p0.spkg\n\nThe latter spkg restores the command \"remove_dynlib\". I then built Sage 4.4.1.alpha2 from scratch on sage.math with polybori-0.6.4.p0.spkg. Doctesting resulted in the following failure:\n\n\n```sh\n[mvngu@sage sage-4.4.1.alpha2]$ ./sage -t -long local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/misc.py\nsage -t -long \"local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/misc.py\"\n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/misc.py\", line 109:\n    sage: print \"ignore this\";  sage.server.misc.find_next_available_port('', 9000, verbose=False)   # random output -- depends on network\nException raised:\n    Traceback (most recent call last):\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[2]>\", line 1, in <module>\n        print \"ignore this\";  sage.server.misc.find_next_available_port('', Integer(9000), verbose=False)   # random output -- depends on network###line 109:\n    sage: print \"ignore this\";  sage.server.misc.find_next_available_port('', 9000, verbose=False)   # random output -- depends on network\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/lib/python/site-packages/sage/server/misc.py\", line 105, in find_next_available_port\n        for port in range(start, start+max_tries+1):\n      File \"element.pyx\", line 1271, in sage.structure.element.RingElement.__add__ (sage/structure/element.c:10830)\n      File \"coerce.pyx\", line 765, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)\n    TypeError: unsupported operand parent(s) for '+': '<type 'str'>' and 'Integer Ring'\n```\n\n\nI have wrapped up a sage.math binary of this patched version of Sage 4.4.1.alpha2. You can find it at\n\nhttp://sage.math.washington.edu/home/mvngu/sage.math-bin/sage-4.4.1.alpha2-patched-sage.math.washington.edu-x86_64-Linux.tar.gz\n\nI removed the directory\n\n`SAGE_ROOT/devel/sage-main/doc/en/thematic_tutorials/`\n\nand wrapped up a source distribution, which can be found at\n\nhttp://sage.math.washington.edu/home/mvngu/sage-src/sage-4.4.1.alpha2-patched.tar",
    "created_at": "2010-04-29T19:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72253",
    "user": "mvngu"
}
```

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ff294013a41ea05c):



Sage 4.4.1.alpha2 contains two PolyBoRi spkg's:

* polybori-0.6.3-20091028.spkg
* polybori-0.6.4.spkg

I think polybori-0.6.4.spkg is the newer one, so I deleted the other one from `SAGE_ROOT/spkg/standard/`. Here's a diff between the `spkg-install` of polybori-0.6.3-20091028.spkg and polybori-0.6.4.spkg:


```diff
[mvngu@sage mvngu]$ diff -Naur polybori-0.6.3-20091028/spkg-install polybori-0.6.4.p0/spkg-install 
--- polybori-0.6.3-20091028/spkg-install	2009-05-17 10:31:16.000000000 -0700
+++ polybori-0.6.4.p0/spkg-install	2010-04-29 07:10:46.000000000 -0700
@@ -6,14 +6,14 @@
    exit 1
 fi
 
-PBDIR=polybori-0.6
+PBDIR=polybori-0.6.4
 WORKDIR=${PWD}/src
 SCONS=scons
 
 # For some strange reason the installed boost in $SAGE_LOCAL causes 
 # make install failures, so copy it over. 
-mkdir src/boost_1_34_1.cropped
-cp -r $SAGE_LOCAL/include/boost src/boost_1_34_1.cropped
+#mkdir src/boost_1_34_1.cropped
+#cp -r $SAGE_LOCAL/include/boost src/boost_1_34_1.cropped
 BOOSTDIR=boost_1_34_1.cropped
 
 patch() 
@@ -26,9 +26,6 @@
 
     cp patches/SConstruct src/${PBDIR}/SConstruct
     cp patches/PyPolyBoRi.py src/${PBDIR}/pyroot/polybori
-
-    # workaround so will build on cygwin
-    cp patches/cpu_stats.c src/${PBDIR}/Cudd/util/cpu_stats.c
 }
 
 
@@ -68,7 +65,7 @@
 
 remove_dylib()
 {
-    # linking dynmic libraries causes segfaults at exit (see #2822)
+    # linking dynamic libraries causes segfaults at exit (see #2822)
     if [ `uname` = "Darwin" ]; then
         rm -f $SAGE_LOCAL/lib/libpolybori.dylib
         rm -f $SAGE_LOCAL/lib/libpboriCudd.dylib
@@ -101,9 +98,3 @@
 echo "Removing dynamic libraries..."
 remove_dylib
 echo "Done removing dynamic libraries."
-
-# force a rebuild of the PolyBoRi extension
-if [ -f $SAGE_ROOT/devel/sage/sage/rings/polynomial/pbori.pyx ]; then
-    touch $SAGE_ROOT/devel/sage/sage/rings/polynomial/pbori.pyx
-fi
-
```


I replaced polybori-0.6.4.spkg with

http://sage.math.washington.edu/home/mvngu/spkg/standard/polybori/polybori-0.6.4.p0.spkg

The latter spkg restores the command "remove_dynlib". I then built Sage 4.4.1.alpha2 from scratch on sage.math with polybori-0.6.4.p0.spkg. Doctesting resulted in the following failure:


```sh
[mvngu@sage sage-4.4.1.alpha2]$ ./sage -t -long local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/misc.py
sage -t -long "local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/misc.py"
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/misc.py", line 109:
    sage: print "ignore this";  sage.server.misc.find_next_available_port('', 9000, verbose=False)   # random output -- depends on network
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        print "ignore this";  sage.server.misc.find_next_available_port('', Integer(9000), verbose=False)   # random output -- depends on network###line 109:
    sage: print "ignore this";  sage.server.misc.find_next_available_port('', 9000, verbose=False)   # random output -- depends on network
      File "/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/lib/python/site-packages/sage/server/misc.py", line 105, in find_next_available_port
        for port in range(start, start+max_tries+1):
      File "element.pyx", line 1271, in sage.structure.element.RingElement.__add__ (sage/structure/element.c:10830)
      File "coerce.pyx", line 765, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)
    TypeError: unsupported operand parent(s) for '+': '<type 'str'>' and 'Integer Ring'
```


I have wrapped up a sage.math binary of this patched version of Sage 4.4.1.alpha2. You can find it at

http://sage.math.washington.edu/home/mvngu/sage.math-bin/sage-4.4.1.alpha2-patched-sage.math.washington.edu-x86_64-Linux.tar.gz

I removed the directory

`SAGE_ROOT/devel/sage-main/doc/en/thematic_tutorials/`

and wrapped up a source distribution, which can be found at

http://sage.math.washington.edu/home/mvngu/sage-src/sage-4.4.1.alpha2-patched.tar



---

archive/issue_comments_072254.json:
```json
{
    "body": "I'm wondering if we should create a new ticket for this new polybori p0 spkg.\nIn any case, I tested it, and it works fine for me.",
    "created_at": "2010-04-30T12:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72254",
    "user": "wjp"
}
```

I'm wondering if we should create a new ticket for this new polybori p0 spkg.
In any case, I tested it, and it works fine for me.



---

archive/issue_comments_072255.json:
```json
{
    "body": "I created ticket #8830 for the p0 spkg.",
    "created_at": "2010-04-30T12:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8192#issuecomment-72255",
    "user": "wjp"
}
```

I created ticket #8830 for the p0 spkg.
