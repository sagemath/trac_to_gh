# Issue 6359: update to Python 2.6.2

archive/issues_006359.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  sage-combinat nthiery\n\nThis requires updating a few other spkgs as well as some fixes in the Sage library.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6359\n\n",
    "created_at": "2009-06-18T23:44:09Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "update to Python 2.6.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6359",
    "user": "mhansen"
}
```
Assignee: mabshoff

CC:  sage-combinat nthiery

This requires updating a few other spkgs as well as some fixes in the Sage library.

Issue created by migration from https://trac.sagemath.org/ticket/6359





---

archive/issue_comments_050850.json:
```json
{
    "body": "Attachment [trac_6359-scripts.patch](tarball://root/attachments/some-uuid/ticket6359/trac_6359-scripts.patch) by mhansen created at 2009-06-19 20:08:29",
    "created_at": "2009-06-19T20:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50850",
    "user": "mhansen"
}
```

Attachment [trac_6359-scripts.patch](tarball://root/attachments/some-uuid/ticket6359/trac_6359-scripts.patch) by mhansen created at 2009-06-19 20:08:29



---

archive/issue_comments_050851.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-06-19T20:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50851",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_050852.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-19T20:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50852",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050853.json:
```json
{
    "body": "Note:  In order to get things to work, I did the following:\n\n1) Took at 4.0.2 source tarball.\n\n2) Replaced the spkgs in the tarball with the ones above.\n\n3) Extracted the sage-*.spkg tarball, applied trac_6359-1.patch, and re \"sage -spkg\"'d it.\n\n4) It's not necessary to apply the other two patches to get things up and running.",
    "created_at": "2009-06-19T20:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50853",
    "user": "mhansen"
}
```

Note:  In order to get things to work, I did the following:

1) Took at 4.0.2 source tarball.

2) Replaced the spkgs in the tarball with the ones above.

3) Extracted the sage-*.spkg tarball, applied trac_6359-1.patch, and re "sage -spkg"'d it.

4) It's not necessary to apply the other two patches to get things up and running.



---

archive/issue_comments_050854.json:
```json
{
    "body": "Note to Nicolas: This changes some things in combinat/ and structure/.  Do you want to have a look at them to decide what to do?",
    "created_at": "2009-06-20T01:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50854",
    "user": "mhansen"
}
```

Note to Nicolas: This changes some things in combinat/ and structure/.  Do you want to have a look at them to decide what to do?



---

archive/issue_comments_050855.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> Note to Nicolas: This changes some things in combinat/ and structure/.  Do you want to have a look at them to decide what to do?\n\nThanks for the notice! Will do, but probably not before Monday!",
    "created_at": "2009-06-20T05:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50855",
    "user": "nthiery"
}
```

Replying to [comment:4 mhansen]:
> Note to Nicolas: This changes some things in combinat/ and structure/.  Do you want to have a look at them to decide what to do?

Thanks for the notice! Will do, but probably not before Monday!



---

archive/issue_comments_050856.json:
```json
{
    "body": "er... can I ask you to upload the python-2.6.2.spkg somewhere?",
    "created_at": "2009-06-20T21:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50856",
    "user": "boothby"
}
```

er... can I ask you to upload the python-2.6.2.spkg somewhere?



---

archive/issue_comments_050857.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> Note to Nicolas: This changes some things in combinat/ and structure/.  Do you want to have a look at them to decide what to do?\n\nThis commutes with the sage-combinat patches, so it's all good for me.",
    "created_at": "2009-06-22T19:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50857",
    "user": "nthiery"
}
```

Replying to [comment:4 mhansen]:
> Note to Nicolas: This changes some things in combinat/ and structure/.  Do you want to have a look at them to decide what to do?

This commutes with the sage-combinat patches, so it's all good for me.



---

archive/issue_comments_050858.json:
```json
{
    "body": "Nicolas: That's good to hear.  The changes were pretty minimal.\n\nI've updated the python-2.6.2.spkg to copy over site-packages from 2.5 to 2.6.  I think this should do okay on upgrades.  I also added the ipython spkg update which was needed.",
    "created_at": "2009-06-22T20:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50858",
    "user": "mhansen"
}
```

Nicolas: That's good to hear.  The changes were pretty minimal.

I've updated the python-2.6.2.spkg to copy over site-packages from 2.5 to 2.6.  I think this should do okay on upgrades.  I also added the ipython spkg update which was needed.



---

archive/issue_comments_050859.json:
```json
{
    "body": "Replying to [comment:8 mhansen]:\n> I've updated the python-2.6.2.spkg to copy over site-packages from 2.5 to 2.6.  I think this should do okay on upgrades.  I also added the ipython spkg update which was needed.\n\nWon't some packages need to have Python 2.6 actually do the installing? I am dubious that just copying over will work (although, of course, I wouldn't know).\n\nWell, on top of alpha0, trac_6359-1.patch fails to apply, although I can't tell why at all- when I went in to fix the rejects (which weren't produced in the working directory like hg said they were), everything looked exactly the same. So after fixing the rest of the patch by hand, I repackaged Sage and forced the above packages to build.\n\nTelling Sage to build very quickly fails, as it cannot find Jinja. So I force setuptools and jinja to build. The next problem is numpy. \nForcing numpy to build does not solve the problem, either:\n\n\n```\nTraceback (most recent call last):\n  File \"setup.py\", line 704, in <module>\n    queue = compile_command_list(ext_modules, deps)\n  File \"setup.py\", line 664, in compile_command_list\n    dep_file, dep_time = deps.newest_dep(f)\n  File \"setup.py\", line 579, in newest_dep\n    for f in self.all_deps(filename):\n  File \"setup.py\", line 560, in all_deps\n    for f in self.immediate_deps(filename):\n  File \"setup.py\", line 542, in immediate_deps\n    self._deps[filename] = self.parse_deps(filename)\n  File \"setup.py\", line 532, in parse_deps\n    raise IOError, \"could not find dependency %s included in %s.\"%(path, filename)\nIOError: could not find dependency sage/plot/numpy.pxd included in sage/plot/complex_plot.pyx.\nsage: There was an error installing modified sage library code.\n```\n\n\nDo we need to bump the version numbers for all the packages that go into site-packages (I can do this by hand if necessary)? This would make upgrading work for sure.\n\nAlso, your step 4) above is a bit lacking. What did you have to do, exactly, to get things up and running?",
    "created_at": "2009-06-25T01:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50859",
    "user": "rlm"
}
```

Replying to [comment:8 mhansen]:
> I've updated the python-2.6.2.spkg to copy over site-packages from 2.5 to 2.6.  I think this should do okay on upgrades.  I also added the ipython spkg update which was needed.

Won't some packages need to have Python 2.6 actually do the installing? I am dubious that just copying over will work (although, of course, I wouldn't know).

Well, on top of alpha0, trac_6359-1.patch fails to apply, although I can't tell why at all- when I went in to fix the rejects (which weren't produced in the working directory like hg said they were), everything looked exactly the same. So after fixing the rest of the patch by hand, I repackaged Sage and forced the above packages to build.

Telling Sage to build very quickly fails, as it cannot find Jinja. So I force setuptools and jinja to build. The next problem is numpy. 
Forcing numpy to build does not solve the problem, either:


```
Traceback (most recent call last):
  File "setup.py", line 704, in <module>
    queue = compile_command_list(ext_modules, deps)
  File "setup.py", line 664, in compile_command_list
    dep_file, dep_time = deps.newest_dep(f)
  File "setup.py", line 579, in newest_dep
    for f in self.all_deps(filename):
  File "setup.py", line 560, in all_deps
    for f in self.immediate_deps(filename):
  File "setup.py", line 542, in immediate_deps
    self._deps[filename] = self.parse_deps(filename)
  File "setup.py", line 532, in parse_deps
    raise IOError, "could not find dependency %s included in %s."%(path, filename)
IOError: could not find dependency sage/plot/numpy.pxd included in sage/plot/complex_plot.pyx.
sage: There was an error installing modified sage library code.
```


Do we need to bump the version numbers for all the packages that go into site-packages (I can do this by hand if necessary)? This would make upgrading work for sure.

Also, your step 4) above is a bit lacking. What did you have to do, exactly, to get things up and running?



---

archive/issue_comments_050860.json:
```json
{
    "body": "Attachment [trac_6359-1.patch](tarball://root/attachments/some-uuid/ticket6359/trac_6359-1.patch) by mhansen created at 2009-06-25 01:19:28",
    "created_at": "2009-06-25T01:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50860",
    "user": "mhansen"
}
```

Attachment [trac_6359-1.patch](tarball://root/attachments/some-uuid/ticket6359/trac_6359-1.patch) by mhansen created at 2009-06-25 01:19:28



---

archive/issue_comments_050861.json:
```json
{
    "body": "Attachment [trac_6359-2.patch](tarball://root/attachments/some-uuid/ticket6359/trac_6359-2.patch) by mhansen created at 2009-06-25 01:19:46",
    "created_at": "2009-06-25T01:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50861",
    "user": "mhansen"
}
```

Attachment [trac_6359-2.patch](tarball://root/attachments/some-uuid/ticket6359/trac_6359-2.patch) by mhansen created at 2009-06-25 01:19:46



---

archive/issue_comments_050862.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-06-25T08:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50862",
    "user": "rlm"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_050863.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-25T08:44:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50863",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_050864.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-06-25T09:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50864",
    "user": "rlm"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_050865.json:
```json
{
    "body": "With the new Python spkg installed, `import _ssl` fails.\n\nThis is relevant:\n\nhttp://www.webtop.com.au/compiling-python-with-ssl-support\n\nOne problem is that `Modules/_ssl.c` uses a lot more of OpenSSL than it used to, and much of what is used is not provided by the gnutls compatibility layer.",
    "created_at": "2009-06-25T09:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50865",
    "user": "rlm"
}
```

With the new Python spkg installed, `import _ssl` fails.

This is relevant:

http://www.webtop.com.au/compiling-python-with-ssl-support

One problem is that `Modules/_ssl.c` uses a lot more of OpenSSL than it used to, and much of what is used is not provided by the gnutls compatibility layer.



---

archive/issue_comments_050866.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-06-25T09:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50866",
    "user": "rlm"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_050867.json:
```json
{
    "body": "For example, `SSL_ERROR_WANT_X509_LOOKUP` is implemented by OpenSSL but not supported by gnutls. There are a ton of others, too.",
    "created_at": "2009-06-25T10:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50867",
    "user": "rlm"
}
```

For example, `SSL_ERROR_WANT_X509_LOOKUP` is implemented by OpenSSL but not supported by gnutls. There are a ton of others, too.



---

archive/issue_comments_050868.json:
```json
{
    "body": "I meant to say, for example, ..., and is used by `Modules/_ssl.c` in Python 2.6.2.",
    "created_at": "2009-06-25T10:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50868",
    "user": "rlm"
}
```

I meant to say, for example, ..., and is used by `Modules/_ssl.c` in Python 2.6.2.



---

archive/issue_comments_050869.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-25T17:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6359#issuecomment-50869",
    "user": "rlm"
}
```

Resolution: fixed
