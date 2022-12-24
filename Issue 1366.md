# Issue 1366: speed up "sage -br" -- make it cache the dependency diagram instead of computing it every time

archive/issues_001366.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf you do \"sage -br\" on a very very fast machine, it still takes nearly\n10 seconds.  This is in a sense a bug, because it should take < 0.4 seconds.\nIt takes a long time, since the entire dependency graph for all .pyx files\nis being computed every single time.  This information should somehow be cached,\nwhich would vastly speed things up. \n\nI consider this a bug since the performance is so bad as to make \"sage -br\"\nvery painful. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1366\n\n",
    "created_at": "2007-12-02T06:15:13Z",
    "labels": [
        "user interface",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "speed up \"sage -br\" -- make it cache the dependency diagram instead of computing it every time",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1366",
    "user": "@williamstein"
}
```
Assignee: @williamstein

If you do "sage -br" on a very very fast machine, it still takes nearly
10 seconds.  This is in a sense a bug, because it should take < 0.4 seconds.
It takes a long time, since the entire dependency graph for all .pyx files
is being computed every single time.  This information should somehow be cached,
which would vastly speed things up. 

I consider this a bug since the performance is so bad as to make "sage -br"
very painful. 

Issue created by migration from https://trac.sagemath.org/ticket/1366





---

archive/issue_comments_008748.json:
```json
{
    "body": "I modified setup.py to cache dependency information. It would be nice to get some people who are modifying a lot of cython code right now to test it out and report any bugs; the modifications seem to work for me but they need to be tested a bunch.",
    "created_at": "2007-12-03T05:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8748",
    "user": "@bobmoretti"
}
```

I modified setup.py to cache dependency information. It would be nice to get some people who are modifying a lot of cython code right now to test it out and report any bugs; the modifications seem to work for me but they need to be tested a bunch.



---

archive/issue_comments_008749.json:
```json
{
    "body": "(the information is cached in SAGE_DEVEL/sage/.cython_dependencies)",
    "created_at": "2007-12-03T05:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8749",
    "user": "@bobmoretti"
}
```

(the information is cached in SAGE_DEVEL/sage/.cython_dependencies)



---

archive/issue_comments_008750.json:
```json
{
    "body": "the actual patch",
    "created_at": "2007-12-03T06:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8750",
    "user": "@bobmoretti"
}
```

the actual patch



---

archive/issue_comments_008751.json:
```json
{
    "body": "Attachment [deps.patch](tarball://root/attachments/some-uuid/ticket1366/deps.patch) by @bobmoretti created at 2007-12-03 07:05:23\n\nnote - there are lots of bugs with the current version. I will work on fixing them on 12/3, but probably not before.\n-Bobby",
    "created_at": "2007-12-03T07:05:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8751",
    "user": "@bobmoretti"
}
```

Attachment [deps.patch](tarball://root/attachments/some-uuid/ticket1366/deps.patch) by @bobmoretti created at 2007-12-03 07:05:23

note - there are lots of bugs with the current version. I will work on fixing them on 12/3, but probably not before.
-Bobby



---

archive/issue_comments_008752.json:
```json
{
    "body": "Attachment [deps.hg](tarball://root/attachments/some-uuid/ticket1366/deps.hg) by @williamstein created at 2007-12-06 14:27:36\n\nIgnore the deps* stuff that bobby posted above, and just use this patch (or later ones?)",
    "created_at": "2007-12-06T14:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8752",
    "user": "@williamstein"
}
```

Attachment [deps.hg](tarball://root/attachments/some-uuid/ticket1366/deps.hg) by @williamstein created at 2007-12-06 14:27:36

Ignore the deps* stuff that bobby posted above, and just use this patch (or later ones?)



---

archive/issue_comments_008753.json:
```json
{
    "body": "Attachment [trac1366.patch](tarball://root/attachments/some-uuid/ticket1366/trac1366.patch) by @williamstein created at 2007-12-06 14:40:21",
    "created_at": "2007-12-06T14:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8753",
    "user": "@williamstein"
}
```

Attachment [trac1366.patch](tarball://root/attachments/some-uuid/ticket1366/trac1366.patch) by @williamstein created at 2007-12-06 14:40:21



---

archive/issue_comments_008754.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-10T05:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8754",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008755.json:
```json
{
    "body": "Merged trac1366.patch in 2.9.alpha3.",
    "created_at": "2007-12-10T05:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8755",
    "user": "mabshoff"
}
```

Merged trac1366.patch in 2.9.alpha3.



---

archive/issue_comments_008756.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-10T23:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8756",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_008757.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-10T23:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8757",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_008758.json:
```json
{
    "body": "This patch has two issues:\n\n* adding new files breaks it (fixed by #1453)\n* sage -ba is broken, probably because time stamps on files are not considered.\n\nThis is out for 2.9, but please resubmit after fixing in the next round.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-10T23:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8758",
    "user": "mabshoff"
}
```

This patch has two issues:

* adding new files breaks it (fixed by #1453)
* sage -ba is broken, probably because time stamps on files are not considered.

This is out for 2.9, but please resubmit after fixing in the next round.

Cheers,

Michael



---

archive/issue_comments_008759.json:
```json
{
    "body": "I reimplemented this from the ground up, hopefully correctly this time. There is still room for improvement, but the dependency graph computation happens nearly instantly now (on my laptop).",
    "created_at": "2008-02-08T02:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8759",
    "user": "@bobmoretti"
}
```

I reimplemented this from the ground up, hopefully correctly this time. There is still room for improvement, but the dependency graph computation happens nearly instantly now (on my laptop).



---

archive/issue_comments_008760.json:
```json
{
    "body": "The patch in deps2.hg seems to ignore .pxi files.  (I modified sage/rings/mpfi.pxi, and then did \"sage -b\", and nothing got recompiled.)",
    "created_at": "2008-02-08T02:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8760",
    "user": "cwitty"
}
```

The patch in deps2.hg seems to ignore .pxi files.  (I modified sage/rings/mpfi.pxi, and then did "sage -b", and nothing got recompiled.)



---

archive/issue_comments_008761.json:
```json
{
    "body": "Changed the status so the bugfix could get a review.",
    "created_at": "2008-02-08T04:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8761",
    "user": "@bobmoretti"
}
```

Changed the status so the bugfix could get a review.



---

archive/issue_comments_008762.json:
```json
{
    "body": "The same testcase still fails (but in a different way now).  When I touch sage/rings/mpfi.pxi, and then run \"sage -b\", it now dumps me into a debugger.  Then, when I press Ctrl-D to exit the debugger, I get a backtrace.\n\n```\ncwitty@magnetar:~/sage-2.10.1$ ./sage -b\n\n----------------------------------------------------------\nsage: Building and installing modified SAGE library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\n> /home/cwitty/sage-2.10.1/devel/sage-review2/setup.py(1040)search_all_includes()\n-> C = [x.strip() for x in S if 'cimport' in x]\n(Pdb) \nTraceback (most recent call last):\n  File \"setup.py\", line 1155, in <module>\n    deps = create_deps(ext_modules)\n  File \"setup.py\", line 1146, in create_deps\n    deps_graph(deps, f, visited)\n  File \"setup.py\", line 1113, in deps_graph\n    this_deps = search_all_includes(f)\n  File \"setup.py\", line 1040, in search_all_includes\n    C = [x.strip() for x in S if 'cimport' in x]\n  File \"setup.py\", line 1040, in search_all_includes\n    C = [x.strip() for x in S if 'cimport' in x]\n  File \"/home/cwitty/sage-2.10.1/local/lib/python2.5/bdb.py\", line 48, in trace_dispatch\n    return self.dispatch_line(frame)\n  File \"/home/cwitty/sage-2.10.1/local/lib/python2.5/bdb.py\", line 67, in dispatch_line\n    if self.quitting: raise BdbQuit\nbdb.BdbQuit\nsage: There was an error installing modified sage library code.\n```\n",
    "created_at": "2008-02-08T04:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8762",
    "user": "cwitty"
}
```

The same testcase still fails (but in a different way now).  When I touch sage/rings/mpfi.pxi, and then run "sage -b", it now dumps me into a debugger.  Then, when I press Ctrl-D to exit the debugger, I get a backtrace.

```
cwitty@magnetar:~/sage-2.10.1$ ./sage -b

----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
scons: `install' is up to date.
> /home/cwitty/sage-2.10.1/devel/sage-review2/setup.py(1040)search_all_includes()
-> C = [x.strip() for x in S if 'cimport' in x]
(Pdb) 
Traceback (most recent call last):
  File "setup.py", line 1155, in <module>
    deps = create_deps(ext_modules)
  File "setup.py", line 1146, in create_deps
    deps_graph(deps, f, visited)
  File "setup.py", line 1113, in deps_graph
    this_deps = search_all_includes(f)
  File "setup.py", line 1040, in search_all_includes
    C = [x.strip() for x in S if 'cimport' in x]
  File "setup.py", line 1040, in search_all_includes
    C = [x.strip() for x in S if 'cimport' in x]
  File "/home/cwitty/sage-2.10.1/local/lib/python2.5/bdb.py", line 48, in trace_dispatch
    return self.dispatch_line(frame)
  File "/home/cwitty/sage-2.10.1/local/lib/python2.5/bdb.py", line 67, in dispatch_line
    if self.quitting: raise BdbQuit
bdb.BdbQuit
sage: There was an error installing modified sage library code.
```




---

archive/issue_comments_008763.json:
```json
{
    "body": "removed debug statements :)",
    "created_at": "2008-02-08T05:49:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8763",
    "user": "@bobmoretti"
}
```

removed debug statements :)



---

archive/issue_comments_008764.json:
```json
{
    "body": "Attachment [deps2.hg](tarball://root/attachments/some-uuid/ticket1366/deps2.hg) by @bobmoretti created at 2008-02-08 05:50:38",
    "created_at": "2008-02-08T05:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8764",
    "user": "@bobmoretti"
}
```

Attachment [deps2.hg](tarball://root/attachments/some-uuid/ticket1366/deps2.hg) by @bobmoretti created at 2008-02-08 05:50:38



---

archive/issue_comments_008765.json:
```json
{
    "body": "Looks good.\n\nI tried the following tests: touch a .pxi file, then rebuild; touch a .pxd file, then rebuild; touch a .pyx file, then rebuild; rebuild everything with \"sage -ba\"; create a new .pyx file, then rebuild.  All of these tests passed.\n\nApply only deps2.hg",
    "created_at": "2008-02-09T21:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8765",
    "user": "cwitty"
}
```

Looks good.

I tried the following tests: touch a .pxi file, then rebuild; touch a .pxd file, then rebuild; touch a .pyx file, then rebuild; rebuild everything with "sage -ba"; create a new .pyx file, then rebuild.  All of these tests passed.

Apply only deps2.hg



---

archive/issue_comments_008766.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-10T01:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8766",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008767.json:
```json
{
    "body": "Merged deps2.hg in Sage 2.10.2.alpha0",
    "created_at": "2008-02-10T01:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1366#issuecomment-8767",
    "user": "mabshoff"
}
```

Merged deps2.hg in Sage 2.10.2.alpha0
