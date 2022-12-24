# Issue 9966: Allow concurrent running/testing of multiple sage branches

archive/issues_009966.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @burcin @qed777 @jdemeyer @nexttime\n\nThis will be very useful for an automated testing framework (and testbed notebook). \n\nIssue created by migration from https://trac.sagemath.org/ticket/9967\n\n",
    "created_at": "2010-09-22T05:18:11Z",
    "labels": [
        "doctest",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Allow concurrent running/testing of multiple sage branches",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9966",
    "user": "@robertwb"
}
```
Assignee: mvngu

CC:  @burcin @qed777 @jdemeyer @nexttime

This will be very useful for an automated testing framework (and testbed notebook). 

Issue created by migration from https://trac.sagemath.org/ticket/9967





---

archive/issue_comments_099820.json:
```json
{
    "body": "Attachment [9967-concurrent-sagelib.patch](tarball://root/attachments/some-uuid/ticket9967/9967-concurrent-sagelib.patch) by @robertwb created at 2010-09-22 05:21:10",
    "created_at": "2010-09-22T05:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99820",
    "user": "@robertwb"
}
```

Attachment [9967-concurrent-sagelib.patch](tarball://root/attachments/some-uuid/ticket9967/9967-concurrent-sagelib.patch) by @robertwb created at 2010-09-22 05:21:10



---

archive/issue_comments_099821.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-22T05:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99821",
    "user": "@robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099822.json:
```json
{
    "body": "Attachment [9967-concurrent-sagescripts.patch](tarball://root/attachments/some-uuid/ticket9967/9967-concurrent-sagescripts.patch) by @dandrake created at 2010-10-21 06:33:18\n\nI'm looking at this because of the discussion on sage-devel (https://groups.google.com/group/sage-devel/browse_thread/thread/9dfadbdaf74a2eec)...and I don't understand this at all. How does it work? In what sense would you have concurrent branches? How does this help with automated testing? I'd like to help review this, but it's not at all clear what is going on here.",
    "created_at": "2010-10-21T06:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99822",
    "user": "@dandrake"
}
```

Attachment [9967-concurrent-sagescripts.patch](tarball://root/attachments/some-uuid/ticket9967/9967-concurrent-sagescripts.patch) by @dandrake created at 2010-10-21 06:33:18

I'm looking at this because of the discussion on sage-devel (https://groups.google.com/group/sage-devel/browse_thread/thread/9dfadbdaf74a2eec)...and I don't understand this at all. How does it work? In what sense would you have concurrent branches? How does this help with automated testing? I'd like to help review this, but it's not at all clear what is going on here.



---

archive/issue_comments_099823.json:
```json
{
    "body": "Currently, the branch of a Sage install is determined by where the devel/sage symlink points. This means that one cannot have one process running the version of Sage in devel/sage-foo while another runs the version of sage in devel/sage-blarg. This patch puts control of which branch to use into an environment variable (set from the symlink by default), so two branches can safely be run or tested at the same time out of the same install. \n\nWith this branch I can set one branch testing, and then switch branches and do something else while that's running in the background. More useful than testing, which could be done in bulk in parallel for a build bot, is being able to have a notebook where different worksheets are running off different branches. It will also make debugging easier, e.g. comparing sage-main to new behavior.",
    "created_at": "2010-10-21T07:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99823",
    "user": "@robertwb"
}
```

Currently, the branch of a Sage install is determined by where the devel/sage symlink points. This means that one cannot have one process running the version of Sage in devel/sage-foo while another runs the version of sage in devel/sage-blarg. This patch puts control of which branch to use into an environment variable (set from the symlink by default), so two branches can safely be run or tested at the same time out of the same install. 

With this branch I can set one branch testing, and then switch branches and do something else while that's running in the background. More useful than testing, which could be done in bulk in parallel for a build bot, is being able to have a notebook where different worksheets are running off different branches. It will also make debugging easier, e.g. comparing sage-main to new behavior.



---

archive/issue_comments_099824.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> Currently, the branch of a Sage install is determined by where the devel/sage symlink points. This means that one cannot have one process running the version of Sage in devel/sage-foo while another runs the version of sage in devel/sage-blarg. This patch puts control of which branch to use into an environment variable (set from the symlink by default), so two branches can safely be run or tested at the same time out of the same install.\n\nAh, okay. Thanks for the help. Doing \"`env SAGE_BRANCH=foo ./sage`\" to use a different branch is great. I'll test this and see how it works.\n\nAlso, I see that right now, we use os.popen to call \"ls -l\" and parse the resulting string to determine the branch. Yikes! This is way better.",
    "created_at": "2010-10-21T08:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99824",
    "user": "@dandrake"
}
```

Replying to [comment:4 robertwb]:
> Currently, the branch of a Sage install is determined by where the devel/sage symlink points. This means that one cannot have one process running the version of Sage in devel/sage-foo while another runs the version of sage in devel/sage-blarg. This patch puts control of which branch to use into an environment variable (set from the symlink by default), so two branches can safely be run or tested at the same time out of the same install.

Ah, okay. Thanks for the help. Doing "`env SAGE_BRANCH=foo ./sage`" to use a different branch is great. I'll test this and see how it works.

Also, I see that right now, we use os.popen to call "ls -l" and parse the resulting string to determine the branch. Yikes! This is way better.



---

archive/issue_comments_099825.json:
```json
{
    "body": "Changing assignee from mvngu to @dandrake.",
    "created_at": "2010-10-21T08:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99825",
    "user": "@dandrake"
}
```

Changing assignee from mvngu to @dandrake.



---

archive/issue_comments_099826.json:
```json
{
    "body": "Found a problem already with the patch to `misc.py`: in `branch_current_hg_notice` (line 1872), when using the default branch, the function gets passed the empty string and things blow up when it does `branch[-1]` on the empty string.\n\nHere's the traceback:\n\n```\nIndexError                                Traceback (most recent call last)\n\n/home/drake/s/sage-4.6.alpha3/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67 \n     68 \n\n/home/drake/s/sage-4.6.alpha3/ipy_profile_sage.py in <module>()\n     14     from sage.misc.interpreter import attached_files\n     15 \n---> 16     branch = sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg())\n     17     if branch:\n     18         print branch\n\n/home/drake/s/sage-4.6.alpha3/devel/sage-main/build/sage/misc/misc.pyc in branch_current_hg_notice(branch)\n   1890     \"\"\"\n   1891     print 'branch_hg_current_hg_notcie got: \"%s\"' % branch\n-> 1892     if branch[-1] == '/':\n   1893         branch = branch[:-1]\n   1894     if branch == 'main':\n\nIndexError: string index out of range\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\n\nAlso, the comment in `branch_current_hg_notice` seems wrong -- I can't see where that function gets called from sage-sage, which is a shell script, not a Python script.",
    "created_at": "2010-10-21T08:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99826",
    "user": "@dandrake"
}
```

Found a problem already with the patch to `misc.py`: in `branch_current_hg_notice` (line 1872), when using the default branch, the function gets passed the empty string and things blow up when it does `branch[-1]` on the empty string.

Here's the traceback:

```
IndexError                                Traceback (most recent call last)

/home/drake/s/sage-4.6.alpha3/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/home/drake/s/sage-4.6.alpha3/ipy_profile_sage.py in <module>()
     14     from sage.misc.interpreter import attached_files
     15 
---> 16     branch = sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg())
     17     if branch:
     18         print branch

/home/drake/s/sage-4.6.alpha3/devel/sage-main/build/sage/misc/misc.pyc in branch_current_hg_notice(branch)
   1890     """
   1891     print 'branch_hg_current_hg_notcie got: "%s"' % branch
-> 1892     if branch[-1] == '/':
   1893         branch = branch[:-1]
   1894     if branch == 'main':

IndexError: string index out of range
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```


Also, the comment in `branch_current_hg_notice` seems wrong -- I can't see where that function gets called from sage-sage, which is a shell script, not a Python script.



---

archive/issue_comments_099827.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-21T09:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99827",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099828.json:
```json
{
    "body": "[Written before seeing Dan's comment]\nI tried this.  The patches apply fine once I worked out where to apply the second one (on SAGE_ROOT/local/bin).\n\nI made a couple of clones, called test1 and test2 and tried just starting Sage with \n\n```\nenv SAGE_BRANCH=test1 sage\n```\n\nand similar.  But I had problems running the main branch.  Using SAGE_BRANCH=main did not work.  And now, with the symlink from sage to sage-main in place, running sage with no SAGE_BRANCH set also fails:\n\n```\nIndexError                                Traceback (most recent call last)\n\n/home/jec/sage-current/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67 \n     68 \n\n/home/jec/sage-4.6.alpha3/devel/ipy_profile_sage.py in <module>()\n     14     from sage.misc.interpreter import attached_files\n     15 \n---> 16     branch = sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg())\n     17     if branch:\n     18         print branch\n\n/home/jec/sage-current/devel/sage-main/build/sage/misc/misc.pyc in branch_current_hg_notice(branch)\n   1889        If the branch is main, then return an empty string.\n   1890     \"\"\"\n-> 1891     if branch[-1] == '/':\n   1892         branch = branch[:-1]\n   1893     if branch == 'main':\n\nIndexError: string index out of range\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\n\nSo I think a little more work is needed.",
    "created_at": "2010-10-21T09:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99828",
    "user": "@JohnCremona"
}
```

[Written before seeing Dan's comment]
I tried this.  The patches apply fine once I worked out where to apply the second one (on SAGE_ROOT/local/bin).

I made a couple of clones, called test1 and test2 and tried just starting Sage with 

```
env SAGE_BRANCH=test1 sage
```

and similar.  But I had problems running the main branch.  Using SAGE_BRANCH=main did not work.  And now, with the symlink from sage to sage-main in place, running sage with no SAGE_BRANCH set also fails:

```
IndexError                                Traceback (most recent call last)

/home/jec/sage-current/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/home/jec/sage-4.6.alpha3/devel/ipy_profile_sage.py in <module>()
     14     from sage.misc.interpreter import attached_files
     15 
---> 16     branch = sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg())
     17     if branch:
     18         print branch

/home/jec/sage-current/devel/sage-main/build/sage/misc/misc.pyc in branch_current_hg_notice(branch)
   1889        If the branch is main, then return an empty string.
   1890     """
-> 1891     if branch[-1] == '/':
   1892         branch = branch[:-1]
   1893     if branch == 'main':

IndexError: string index out of range
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```


So I think a little more work is needed.



---

archive/issue_comments_099829.json:
```json
{
    "body": "Thanks for taking a look. I didn't do much testing with the -main branch, I'll look into the 'main' vs. empty string issues and post a new patch.",
    "created_at": "2010-10-21T20:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99829",
    "user": "@robertwb"
}
```

Thanks for taking a look. I didn't do much testing with the -main branch, I'll look into the 'main' vs. empty string issues and post a new patch.



---

archive/issue_comments_099830.json:
```json
{
    "body": "Attachment [9967-concurrent-sagelib.2.patch](tarball://root/attachments/some-uuid/ticket9967/9967-concurrent-sagelib.2.patch) by @robertwb created at 2010-10-22 04:56:36",
    "created_at": "2010-10-22T04:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99830",
    "user": "@robertwb"
}
```

Attachment [9967-concurrent-sagelib.2.patch](tarball://root/attachments/some-uuid/ticket9967/9967-concurrent-sagelib.2.patch) by @robertwb created at 2010-10-22 04:56:36



---

archive/issue_comments_099831.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-22T04:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99831",
    "user": "@robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099832.json:
```json
{
    "body": "OK, the new patch should work. The problem was that I implemented the function based on its docstring, rather than what it actually used to do :).",
    "created_at": "2010-10-22T04:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99832",
    "user": "@robertwb"
}
```

OK, the new patch should work. The problem was that I implemented the function based on its docstring, rather than what it actually used to do :).



---

archive/issue_comments_099833.json:
```json
{
    "body": "Replying to [comment:9 robertwb]:\n> OK, the new patch should work. The problem was that I implemented the function based on its docstring, rather than what it actually used to do :). \n\nHrm, with the new patch (sagelib2) I get a KeyError when starting if I don't set SAGE_BRANCH. I think you need either to (1) wrap the os.environ call in a \"try/except KeyError\" or (2) get one of the basic scripts to set SAGE_BRANCH if it isn't already set.",
    "created_at": "2010-10-22T05:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99833",
    "user": "@dandrake"
}
```

Replying to [comment:9 robertwb]:
> OK, the new patch should work. The problem was that I implemented the function based on its docstring, rather than what it actually used to do :). 

Hrm, with the new patch (sagelib2) I get a KeyError when starting if I don't set SAGE_BRANCH. I think you need either to (1) wrap the os.environ call in a "try/except KeyError" or (2) get one of the basic scripts to set SAGE_BRANCH if it isn't already set.



---

archive/issue_comments_099834.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-22T05:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99834",
    "user": "@dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099835.json:
```json
{
    "body": "Replying to [comment:10 ddrake]:\n> Hrm, with the new patch (sagelib2) I get a KeyError when starting if I don't set SAGE_BRANCH. I think you need either to (1) wrap the os.environ call in a \"try/except KeyError\" or (2) get one of the basic scripts to set SAGE_BRANCH if it isn't already set.\n\nWait! Never mind. I didn't `qpush` the patch in the scripts repo.\n\nI've tested this a bit and so far it seems like it works fine. I'll keep working on this and hopefully give this a positive review soon. (But others should also test this!)",
    "created_at": "2010-10-22T05:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99835",
    "user": "@dandrake"
}
```

Replying to [comment:10 ddrake]:
> Hrm, with the new patch (sagelib2) I get a KeyError when starting if I don't set SAGE_BRANCH. I think you need either to (1) wrap the os.environ call in a "try/except KeyError" or (2) get one of the basic scripts to set SAGE_BRANCH if it isn't already set.

Wait! Never mind. I didn't `qpush` the patch in the scripts repo.

I've tested this a bit and so far it seems like it works fine. I'll keep working on this and hopefully give this a positive review soon. (But others should also test this!)



---

archive/issue_comments_099836.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-22T05:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99836",
    "user": "@dandrake"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099837.json:
```json
{
    "body": "Here's an interesting doctest failure. My branches look like this:\n\n```\ndrake@sagenb:~/s/sage-4.6.alpha3$ ls devel/\ntotal 20\ndrwxr-xr-x 2 drake drake 4096 2010-10-10 01:40 old/\nlrwxrwxrwx 1 drake drake    8 2010-10-23 12:43 sage -> sage-foo/\ndrwxr-xr-x 7 drake drake 4096 2010-10-22 14:39 sage-bar/\ndrwxr-xr-x 7 drake drake 4096 2010-10-22 14:28 sage-foo/\ndrwxr-xr-x 7 drake drake 4096 2010-10-22 14:22 sage-main/\nlrwxrwxrwx 1 drake drake   11 2010-10-10 01:32 sagenb -> sagenb-main/\ndrwxr-xr-x 8 drake drake 4096 2010-10-10 01:32 sagenb-main/\n```\n\n\nAnd when I run -testall, I get this:\n\n```\ndrake@sagenb:~/s/sage-4.6.alpha3$ minnesota_nice ./sage -testall\nTesting of examples currently not implemented.\nsage -t  -force_lib \"devel/sage/doc/common/builder.py\"\n**********************************************************************\nFile \"/home/drake/s/sage-4.6.alpha3/devel/sage/doc/common/builder.py\", line 158:\n    sage: b._output_dir('html')   \nExpected:\n    '.../devel/sage/doc/output/html/en/tutorial'\nGot:\n    '/home/drake/s/sage-4.6.alpha3/devel/sage-foo/doc/output/html/en/tutorial'\n**********************************************************************\nFile \"/home/drake/s/sage-4.6.alpha3/devel/sage/doc/common/builder.py\", line 173:\n    sage: b._doctrees_dir()\nExpected:\n    '.../devel/sage/doc/output/doctrees/en/tutorial'\nGot:\n    '/home/drake/s/sage-4.6.alpha3/devel/sage-foo/doc/output/doctrees/en/tutoria\nl'\n**********************************************************************\n```\n\n\nSomeone there is not getting the memo about the current branch.",
    "created_at": "2010-10-23T05:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99837",
    "user": "@dandrake"
}
```

Here's an interesting doctest failure. My branches look like this:

```
drake@sagenb:~/s/sage-4.6.alpha3$ ls devel/
total 20
drwxr-xr-x 2 drake drake 4096 2010-10-10 01:40 old/
lrwxrwxrwx 1 drake drake    8 2010-10-23 12:43 sage -> sage-foo/
drwxr-xr-x 7 drake drake 4096 2010-10-22 14:39 sage-bar/
drwxr-xr-x 7 drake drake 4096 2010-10-22 14:28 sage-foo/
drwxr-xr-x 7 drake drake 4096 2010-10-22 14:22 sage-main/
lrwxrwxrwx 1 drake drake   11 2010-10-10 01:32 sagenb -> sagenb-main/
drwxr-xr-x 8 drake drake 4096 2010-10-10 01:32 sagenb-main/
```


And when I run -testall, I get this:

```
drake@sagenb:~/s/sage-4.6.alpha3$ minnesota_nice ./sage -testall
Testing of examples currently not implemented.
sage -t  -force_lib "devel/sage/doc/common/builder.py"
**********************************************************************
File "/home/drake/s/sage-4.6.alpha3/devel/sage/doc/common/builder.py", line 158:
    sage: b._output_dir('html')   
Expected:
    '.../devel/sage/doc/output/html/en/tutorial'
Got:
    '/home/drake/s/sage-4.6.alpha3/devel/sage-foo/doc/output/html/en/tutorial'
**********************************************************************
File "/home/drake/s/sage-4.6.alpha3/devel/sage/doc/common/builder.py", line 173:
    sage: b._doctrees_dir()
Expected:
    '.../devel/sage/doc/output/doctrees/en/tutorial'
Got:
    '/home/drake/s/sage-4.6.alpha3/devel/sage-foo/doc/output/doctrees/en/tutoria
l'
**********************************************************************
```


Someone there is not getting the memo about the current branch.



---

archive/issue_comments_099838.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-23T05:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99838",
    "user": "@dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099839.json:
```json
{
    "body": "Those doctests just need to be changed to '.../devel/sage-.../doc/output/html/en/tutorial' now that the path doesn't rely on the symlink.",
    "created_at": "2010-10-23T08:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99839",
    "user": "@robertwb"
}
```

Those doctests just need to be changed to '.../devel/sage-.../doc/output/html/en/tutorial' now that the path doesn't rely on the symlink.



---

archive/issue_comments_099840.json:
```json
{
    "body": "Attachment [9967-doc-doctests.patch](tarball://root/attachments/some-uuid/ticket9967/9967-doc-doctests.patch) by @robertwb created at 2010-10-24 03:25:00",
    "created_at": "2010-10-24T03:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99840",
    "user": "@robertwb"
}
```

Attachment [9967-doc-doctests.patch](tarball://root/attachments/some-uuid/ticket9967/9967-doc-doctests.patch) by @robertwb created at 2010-10-24 03:25:00



---

archive/issue_comments_099841.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-24T03:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99841",
    "user": "@robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099842.json:
```json
{
    "body": "I ran into a bit of a problem applying the doctests patch. The branch symlinks are set up just like my comment above. I decided to apply the doctest patch in the main branch, so I qimport'ed the patch there, pushed it, and back in SAGE_ROOT, did\n\n```\nenv SAGE_BRANCH=main ./sage -b\n```\n\nNothing related to doc/common/builder.py showed up, but I decided to try a test anyway:\n\n```\ndrake@sagenb:~/s/sage-4.6.alpha3$ env SAGE_BRANCH=main ./sage -testall\nTesting of examples currently not implemented.\nsage -t  -force_lib \"devel/sage/doc/common/builder.py\"\n**********************************************************************\nFile \"/home/drake/s/sage-4.6.alpha3/devel/sage/doc/common/builder.py\", line 158:\n    sage: b._output_dir('html')   \nExpected:\n    '.../devel/sage/doc/output/html/en/tutorial'\nGot:\n    '/home/drake/s/sage-4.6.alpha3/devel/sage-main/doc/output/html/en/tutorial'\n**********************************************************************\n```\n\n\nThe patch has been applied, but the test still failed. So I tried changing the symlink:\n\n```\ndrake@sagenb:~/s/sage-4.6.alpha3$ ./sage -b main\n  (usual output, no mention of builder.py)\ndrake@sagenb:~/s/sage-4.6.alpha3$ ./sage -testall\nTesting of examples currently not implemented.\nsage -t  -force_lib \"devel/sage/doc/common/builder.py\"\n         [5.9 s]\n```\n\n\nOkay, so things worked when the symlink is set as usual. I tried testing another branch, which should fail, since the patch hasn't been applied there:\n\n```\ndrake@sagenb:~/s/sage-4.6.alpha3$ env SAGE_BRANCH=foo ./sage -testall\nTesting of examples currently not implemented.\nsage -t  -force_lib \"devel/sage/doc/common/builder.py\"\n         [2.4 s]\n```\n\n\nThe sage-foo branch definitely doesn't have the doctest patch applied, so something for the doctest here is ignoring the env variable and using the symlink.\n\nI think the culprit is sage-maketest, which features:\n\n```\n\"$SAGE_ROOT\"/sage -t -sagenb \"$@\" \"$SAGE_ROOT\"/devel/sage/doc/common \"$SAGE_ROOT\"/devel/sage/doc/en \"$SAGE_ROOT\"/devel/sage/doc/fr  \"$SAGE_ROOT\"/devel/sage/sage 2>&1 | tee -a \"$SAGE_TEST_LOG\"\n```\n\nso that's ignoring the branch.\n\nI added this to sage-maketest:\n\n```\n# if SAGE_BRANCH is provided, prepend a dash; we'll use \n#   /sage\"$BRANCH\"/\n# below, which will automatically use the symlink if SAGE_BRANCH is\n# unset\nif [ -n \"$SAGE_BRANCH\" ]; then\n  BRANCH=-$SAGE_BRANCH\nfi\n```\n\n\nand changed the main testing line below that appropriately. It seems to work. Does that seem like the right thing to do?",
    "created_at": "2010-10-24T04:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99842",
    "user": "@dandrake"
}
```

I ran into a bit of a problem applying the doctests patch. The branch symlinks are set up just like my comment above. I decided to apply the doctest patch in the main branch, so I qimport'ed the patch there, pushed it, and back in SAGE_ROOT, did

```
env SAGE_BRANCH=main ./sage -b
```

Nothing related to doc/common/builder.py showed up, but I decided to try a test anyway:

```
drake@sagenb:~/s/sage-4.6.alpha3$ env SAGE_BRANCH=main ./sage -testall
Testing of examples currently not implemented.
sage -t  -force_lib "devel/sage/doc/common/builder.py"
**********************************************************************
File "/home/drake/s/sage-4.6.alpha3/devel/sage/doc/common/builder.py", line 158:
    sage: b._output_dir('html')   
Expected:
    '.../devel/sage/doc/output/html/en/tutorial'
Got:
    '/home/drake/s/sage-4.6.alpha3/devel/sage-main/doc/output/html/en/tutorial'
**********************************************************************
```


The patch has been applied, but the test still failed. So I tried changing the symlink:

```
drake@sagenb:~/s/sage-4.6.alpha3$ ./sage -b main
  (usual output, no mention of builder.py)
drake@sagenb:~/s/sage-4.6.alpha3$ ./sage -testall
Testing of examples currently not implemented.
sage -t  -force_lib "devel/sage/doc/common/builder.py"
         [5.9 s]
```


Okay, so things worked when the symlink is set as usual. I tried testing another branch, which should fail, since the patch hasn't been applied there:

```
drake@sagenb:~/s/sage-4.6.alpha3$ env SAGE_BRANCH=foo ./sage -testall
Testing of examples currently not implemented.
sage -t  -force_lib "devel/sage/doc/common/builder.py"
         [2.4 s]
```


The sage-foo branch definitely doesn't have the doctest patch applied, so something for the doctest here is ignoring the env variable and using the symlink.

I think the culprit is sage-maketest, which features:

```
"$SAGE_ROOT"/sage -t -sagenb "$@" "$SAGE_ROOT"/devel/sage/doc/common "$SAGE_ROOT"/devel/sage/doc/en "$SAGE_ROOT"/devel/sage/doc/fr  "$SAGE_ROOT"/devel/sage/sage 2>&1 | tee -a "$SAGE_TEST_LOG"
```

so that's ignoring the branch.

I added this to sage-maketest:

```
# if SAGE_BRANCH is provided, prepend a dash; we'll use 
#   /sage"$BRANCH"/
# below, which will automatically use the symlink if SAGE_BRANCH is
# unset
if [ -n "$SAGE_BRANCH" ]; then
  BRANCH=-$SAGE_BRANCH
fi
```


and changed the main testing line below that appropriately. It seems to work. Does that seem like the right thing to do?



---

archive/issue_comments_099843.json:
```json
{
    "body": "In the root makefile, I see that SAGE_ROOT/devel/sage/ is hard-coded in TESTDIRS. (That is, it will always follow the symlink and use the default branch.) Should that be changed to include the branch? (We don't need to necessarily address that in this ticket, but I'd like to know what others think. Personally, I would like it to -- I want every \"entry point\" into doctests to use the SAGE_BRANCH environment variable if set.)",
    "created_at": "2010-10-24T06:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99843",
    "user": "@dandrake"
}
```

In the root makefile, I see that SAGE_ROOT/devel/sage/ is hard-coded in TESTDIRS. (That is, it will always follow the symlink and use the default branch.) Should that be changed to include the branch? (We don't need to necessarily address that in this ticket, but I'd like to know what others think. Personally, I would like it to -- I want every "entry point" into doctests to use the SAGE_BRANCH environment variable if set.)



---

archive/issue_comments_099844.json:
```json
{
    "body": "Another question: how does one rebuild a non-default branch? Let's say I have a session running in  the main branch, and on the side, I'm doing some testing in the \"test\" branch. I want to rebuild in sage-test, but I don't want to switch the symlink, because then the running session will get confused.\n\nAll of the various \"-b\" options say that they switch to a branch -- do we have to do that?\n\nMaybe another way to say this: I want at least one of these statements to be true:\n\n* \"a running session / set of doctests / etc will never get confused if the symlink gets switched around\"\n* \"you can rebuild a branch with something like `env SAGE_BRANCH=foo ./sage -b`\"\n\nDoes this seem reasonable?",
    "created_at": "2010-10-24T07:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99844",
    "user": "@dandrake"
}
```

Another question: how does one rebuild a non-default branch? Let's say I have a session running in  the main branch, and on the side, I'm doing some testing in the "test" branch. I want to rebuild in sage-test, but I don't want to switch the symlink, because then the running session will get confused.

All of the various "-b" options say that they switch to a branch -- do we have to do that?

Maybe another way to say this: I want at least one of these statements to be true:

* "a running session / set of doctests / etc will never get confused if the symlink gets switched around"
* "you can rebuild a branch with something like `env SAGE_BRANCH=foo ./sage -b`"

Does this seem reasonable?



---

archive/issue_comments_099845.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-25T08:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99845",
    "user": "@dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099846.json:
```json
{
    "body": "Replying to [comment:19 ddrake]:\n> Another question: how does one rebuild a non-default branch? Let's say I have a session running in  the main branch, and on the side, I'm doing some testing in the \"test\" branch. I want to rebuild in sage-test, but I don't want to switch the symlink, because then the running session will get confused.\n> \n> All of the various \"-b\" options say that they switch to a branch -- do we have to do that?\n\nIdeally we would support building stuff in parallel too, but that was beyond the scope of this ticket. The makefile is a bit trickier, as it creates the list before SAGE_BRANCH gets set. I think all the different testing entry points should be consolidated, probably into \"sage -testeall\" which could take various options. \n\n> Maybe another way to say this: I want at least one of these statements to be true:\n> \n>   * \"a running session / set of doctests / etc will never get confused if the symlink gets switched around\"\n\nThis should be true. On starting sage, SAGE_BRANCH gets set right away if it wasn't set before, so you shouldn't confuse a running/testing sage by swapping the symlink out from under it. (All sub-proceses will inherit the environment variable.) \n\n>   * \"you can rebuild a branch with something like `env SAGE_BRANCH=foo ./sage -b`\"\n> \n> Does this seem reasonable?\n\nI'd like both to be true, but at the moment the first is, which I think is the most valuable first step. OK, I've made a fix to sage-maketest. Note that SAGE_BRANCH will always be set at this point (whether by the user or by sage-env). Is there anything else that needs work on this?",
    "created_at": "2010-10-26T03:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99846",
    "user": "@robertwb"
}
```

Replying to [comment:19 ddrake]:
> Another question: how does one rebuild a non-default branch? Let's say I have a session running in  the main branch, and on the side, I'm doing some testing in the "test" branch. I want to rebuild in sage-test, but I don't want to switch the symlink, because then the running session will get confused.
> 
> All of the various "-b" options say that they switch to a branch -- do we have to do that?

Ideally we would support building stuff in parallel too, but that was beyond the scope of this ticket. The makefile is a bit trickier, as it creates the list before SAGE_BRANCH gets set. I think all the different testing entry points should be consolidated, probably into "sage -testeall" which could take various options. 

> Maybe another way to say this: I want at least one of these statements to be true:
> 
>   * "a running session / set of doctests / etc will never get confused if the symlink gets switched around"

This should be true. On starting sage, SAGE_BRANCH gets set right away if it wasn't set before, so you shouldn't confuse a running/testing sage by swapping the symlink out from under it. (All sub-proceses will inherit the environment variable.) 

>   * "you can rebuild a branch with something like `env SAGE_BRANCH=foo ./sage -b`"
> 
> Does this seem reasonable?

I'd like both to be true, but at the moment the first is, which I think is the most valuable first step. OK, I've made a fix to sage-maketest. Note that SAGE_BRANCH will always be set at this point (whether by the user or by sage-env). Is there anything else that needs work on this?



---

archive/issue_comments_099847.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-26T03:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99847",
    "user": "@robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099848.json:
```json
{
    "body": "Attachment [9967-sage-maketest.patch](tarball://root/attachments/some-uuid/ticket9967/9967-sage-maketest.patch) by @robertwb created at 2010-10-26 03:52:42",
    "created_at": "2010-10-26T03:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99848",
    "user": "@robertwb"
}
```

Attachment [9967-sage-maketest.patch](tarball://root/attachments/some-uuid/ticket9967/9967-sage-maketest.patch) by @robertwb created at 2010-10-26 03:52:42



---

archive/issue_comments_099849.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-27T02:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99849",
    "user": "@dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099850.json:
```json
{
    "body": "Replying to [comment:21 robertwb]:\n> >Maybe another way to say this: I want at least one of these statements to be true: * \"a running session / set of doctests / etc will never get confused if the symlink gets switched around\"\n> This should be true. On starting sage, SAGE_BRANCH gets set right away if it wasn't set before, so you shouldn't confuse a running/testing sage by swapping the symlink out from under it. (All sub-proceses will inherit the environment variable.) \n\nHmmm, I'm not sure this is true. Here's what I did:\n\n* switch to branch \"bar\" with \"sage -b\".\n* start some doctests in branch foo: `env SAGE_BRANCH=foo ./sage -tp 8 devel/sage-foo/sage/combinat`\n* do `rm -fr devel/sage-bar`\n\nThe doctests should continue running and not be effected by the bar branch being deleted...but they immediately start failing:\n\n\n```\nsage -t  devel/sage-foo/sage/combinat/q_analogues.py\nTraceback (most recent call last):\n  File \"/home/drake/.sage//tmp/q_analogues.py\", line 2, in <module>\n    from sage.all_cmdline import *;\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/all_cmdline.py\", line 14, in <module>\n    from sage.all import *\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/all.py\", line 83, in <module>\n    from sage.modular.all    import *\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/all.py\", line 9, in <module>\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/all.py\", line 7, in <module>\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/constructor.py\", line 22, in <module>\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/abvar_newform.py\", line 26, in <module>\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/abvar.py\", line 44, in <module>\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/all.py\", line 8, in <module>\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/perm_gps/all.py\", line 16, in <module>\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/perm_gps/cubegroup.py\", line 110, in <module>\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/plot/all.py\", line 1, in <module>\n  File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/plot/plot.py\", line 4157, in <module>\nImportError: No module named disk\n```\n\n\nand various other ImportErrors. So something is following local/lib/python/site-packages/sage and not going directly to the branch given by SAGE_BRANCH. \n\n> Is there anything else that needs work on this? \n\nWe're getting there. Sorry for being so picky!\n\nOne thing I see: `sage-sdist` uses `SAGE_ROOT/devel/sage/sage` -- it follows the symlink and packages up the default branch. That's fine, but that script calls `sage-make_devel_packages`, which uses `SAGE_ROOT/devel/sage-main`. This could cause some serious confusion! (Then again, setting `SAGE_BRANCH` won't affect this, and we've gone through who-knows-how-many releases with the scripts like this...so perhaps we can ignore that issue here.)",
    "created_at": "2010-10-27T02:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99850",
    "user": "@dandrake"
}
```

Replying to [comment:21 robertwb]:
> >Maybe another way to say this: I want at least one of these statements to be true: * "a running session / set of doctests / etc will never get confused if the symlink gets switched around"
> This should be true. On starting sage, SAGE_BRANCH gets set right away if it wasn't set before, so you shouldn't confuse a running/testing sage by swapping the symlink out from under it. (All sub-proceses will inherit the environment variable.) 

Hmmm, I'm not sure this is true. Here's what I did:

* switch to branch "bar" with "sage -b".
* start some doctests in branch foo: `env SAGE_BRANCH=foo ./sage -tp 8 devel/sage-foo/sage/combinat`
* do `rm -fr devel/sage-bar`

The doctests should continue running and not be effected by the bar branch being deleted...but they immediately start failing:


```
sage -t  devel/sage-foo/sage/combinat/q_analogues.py
Traceback (most recent call last):
  File "/home/drake/.sage//tmp/q_analogues.py", line 2, in <module>
    from sage.all_cmdline import *;
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/all.py", line 83, in <module>
    from sage.modular.all    import *
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/all.py", line 9, in <module>
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/all.py", line 7, in <module>
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/constructor.py", line 22, in <module>
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/abvar_newform.py", line 26, in <module>
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/abvar.py", line 44, in <module>
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/all.py", line 8, in <module>
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/perm_gps/all.py", line 16, in <module>
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/perm_gps/cubegroup.py", line 110, in <module>
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/plot/all.py", line 1, in <module>
  File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/plot/plot.py", line 4157, in <module>
ImportError: No module named disk
```


and various other ImportErrors. So something is following local/lib/python/site-packages/sage and not going directly to the branch given by SAGE_BRANCH. 

> Is there anything else that needs work on this? 

We're getting there. Sorry for being so picky!

One thing I see: `sage-sdist` uses `SAGE_ROOT/devel/sage/sage` -- it follows the symlink and packages up the default branch. That's fine, but that script calls `sage-make_devel_packages`, which uses `SAGE_ROOT/devel/sage-main`. This could cause some serious confusion! (Then again, setting `SAGE_BRANCH` won't affect this, and we've gone through who-knows-how-many releases with the scripts like this...so perhaps we can ignore that issue here.)



---

archive/issue_comments_099851.json:
```json
{
    "body": "Replying to [comment:22 ddrake]:\n> Replying to [comment:21 robertwb]:\n> > >Maybe another way to say this: I want at least one of these statements to be true: * \"a running session / set of doctests / etc will never get confused if the symlink gets switched around\"\n> > This should be true. On starting sage, SAGE_BRANCH gets set right away if it wasn't set before, so you shouldn't confuse a running/testing sage by swapping the symlink out from under it. (All sub-proceses will inherit the environment variable.) \n> \n> Hmmm, I'm not sure this is true. Here's what I did:\n> \n> * switch to branch \"bar\" with \"sage -b\".\n> * start some doctests in branch foo: `env SAGE_BRANCH=foo ./sage -tp 8 devel/sage-foo/sage/combinat`\n> * do `rm -fr devel/sage-bar`\n> \n> The doctests should continue running and not be effected by the bar branch being deleted...but they immediately start failing:\n> \n> {{{\n> sage -t  devel/sage-foo/sage/combinat/q_analogues.py\n> Traceback (most recent call last):\n>   File \"/home/drake/.sage//tmp/q_analogues.py\", line 2, in <module>\n>     from sage.all_cmdline import *;\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/all_cmdline.py\", line 14, in <module>\n>     from sage.all import *\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/all.py\", line 83, in <module>\n>     from sage.modular.all    import *\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/all.py\", line 9, in <module>\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/all.py\", line 7, in <module>\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/constructor.py\", line 22, in <module>\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/abvar_newform.py\", line 26, in <module>\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/abvar.py\", line 44, in <module>\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/all.py\", line 8, in <module>\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/perm_gps/all.py\", line 16, in <module>\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/perm_gps/cubegroup.py\", line 110, in <module>\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/plot/all.py\", line 1, in <module>\n>   File \"/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/plot/plot.py\", line 4157, in <module>\n> ImportError: No module named disk\n> }}}\n> \n> and various other ImportErrors. So something is following local/lib/python/site-packages/sage and not going directly to the branch given by SAGE_BRANCH. \n\nArgh, I thought I had tested this. Well, more work to be done then.\n\n> > Is there anything else that needs work on this? \n> \n> We're getting there. Sorry for being so picky!\n\nNo, it's good, something like this needs a thorough review.\n\n> One thing I see: `sage-sdist` uses `SAGE_ROOT/devel/sage/sage` -- it follows the symlink and packages up the default branch. That's fine, but that script calls `sage-make_devel_packages`, which uses `SAGE_ROOT/devel/sage-main`. This could cause some serious confusion! (Then again, setting `SAGE_BRANCH` won't affect this, and we've gone through who-knows-how-many releases with the scripts like this...so perhaps we can ignore that issue here.)\n\nI didn't touch any of the building/packaging stuff. I think a lot of this was written by people who just make a whole new copy of sage rather than using branches/clones...",
    "created_at": "2010-10-27T06:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99851",
    "user": "@robertwb"
}
```

Replying to [comment:22 ddrake]:
> Replying to [comment:21 robertwb]:
> > >Maybe another way to say this: I want at least one of these statements to be true: * "a running session / set of doctests / etc will never get confused if the symlink gets switched around"
> > This should be true. On starting sage, SAGE_BRANCH gets set right away if it wasn't set before, so you shouldn't confuse a running/testing sage by swapping the symlink out from under it. (All sub-proceses will inherit the environment variable.) 
> 
> Hmmm, I'm not sure this is true. Here's what I did:
> 
> * switch to branch "bar" with "sage -b".
> * start some doctests in branch foo: `env SAGE_BRANCH=foo ./sage -tp 8 devel/sage-foo/sage/combinat`
> * do `rm -fr devel/sage-bar`
> 
> The doctests should continue running and not be effected by the bar branch being deleted...but they immediately start failing:
> 
> {{{
> sage -t  devel/sage-foo/sage/combinat/q_analogues.py
> Traceback (most recent call last):
>   File "/home/drake/.sage//tmp/q_analogues.py", line 2, in <module>
>     from sage.all_cmdline import *;
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/all_cmdline.py", line 14, in <module>
>     from sage.all import *
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/all.py", line 83, in <module>
>     from sage.modular.all    import *
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/all.py", line 9, in <module>
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/all.py", line 7, in <module>
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/constructor.py", line 22, in <module>
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/abvar_newform.py", line 26, in <module>
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/modular/abvar/abvar.py", line 44, in <module>
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/all.py", line 8, in <module>
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/perm_gps/all.py", line 16, in <module>
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/groups/perm_gps/cubegroup.py", line 110, in <module>
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/plot/all.py", line 1, in <module>
>   File "/home/drake/s/sage-4.6.alpha3/local/lib/python/site-packages/sage/plot/plot.py", line 4157, in <module>
> ImportError: No module named disk
> }}}
> 
> and various other ImportErrors. So something is following local/lib/python/site-packages/sage and not going directly to the branch given by SAGE_BRANCH. 

Argh, I thought I had tested this. Well, more work to be done then.

> > Is there anything else that needs work on this? 
> 
> We're getting there. Sorry for being so picky!

No, it's good, something like this needs a thorough review.

> One thing I see: `sage-sdist` uses `SAGE_ROOT/devel/sage/sage` -- it follows the symlink and packages up the default branch. That's fine, but that script calls `sage-make_devel_packages`, which uses `SAGE_ROOT/devel/sage-main`. This could cause some serious confusion! (Then again, setting `SAGE_BRANCH` won't affect this, and we've gone through who-knows-how-many releases with the scripts like this...so perhaps we can ignore that issue here.)

I didn't touch any of the building/packaging stuff. I think a lot of this was written by people who just make a whole new copy of sage rather than using branches/clones...



---

archive/issue_comments_099852.json:
```json
{
    "body": "Here's a question: the new sage-env sets PYTHONPATH to include devel/sage-BRANCH/build, but we also have a symlink in local/lib/python/site-packages. How about just deleting that symlink? The PYTHONPATH stuff means that we find exactly the Sage library we want.\n\nI experimented with this a little bit and it seems to work. I need to look at it more, but this might be a very simple fix to the problem I reported above.",
    "created_at": "2010-10-27T12:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99852",
    "user": "@dandrake"
}
```

Here's a question: the new sage-env sets PYTHONPATH to include devel/sage-BRANCH/build, but we also have a symlink in local/lib/python/site-packages. How about just deleting that symlink? The PYTHONPATH stuff means that we find exactly the Sage library we want.

I experimented with this a little bit and it seems to work. I need to look at it more, but this might be a very simple fix to the problem I reported above.



---

archive/issue_comments_099853.json:
```json
{
    "body": "Replying to [comment:24 ddrake]:\n> Here's a question: the new sage-env sets PYTHONPATH to include devel/sage-BRANCH/build, but we also have a symlink in local/lib/python/site-packages. How about just deleting that symlink? The PYTHONPATH stuff means that we find exactly the Sage library we want.\n> \n> I experimented with this a little bit and it seems to work. I need to look at it more, but this might be a very simple fix to the problem I reported above.\n\nActually, I had moved my symlink out of the way--of course that didn't get checked in as part of the patch :). What I'm not sure about is if they it re-established anywhere. \n\n- Robert",
    "created_at": "2010-10-27T15:59:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99853",
    "user": "@robertwb"
}
```

Replying to [comment:24 ddrake]:
> Here's a question: the new sage-env sets PYTHONPATH to include devel/sage-BRANCH/build, but we also have a symlink in local/lib/python/site-packages. How about just deleting that symlink? The PYTHONPATH stuff means that we find exactly the Sage library we want.
> 
> I experimented with this a little bit and it seems to work. I need to look at it more, but this might be a very simple fix to the problem I reported above.

Actually, I had moved my symlink out of the way--of course that didn't get checked in as part of the patch :). What I'm not sure about is if they it re-established anywhere. 

- Robert



---

archive/issue_comments_099854.json:
```json
{
    "body": "Hrm, removing that symlink doesn't always work: I deleted it, edited devel/sage/setup.py to not create the link (line 65 or so), and rebuilt the branch. \n\nRunning Sage seems to work (I only have one branch at the moment, so no issues there), but if I try to run doctests, it fails with an ImportError -- it can't find sage.all_cmdline, which is ironic since I can run Sage at the commandline with no problem. \n\nsage-env is setting SAGE_BRANCH and PYTHONPATH appropriately, so there's still something that's not respecting those environment variables.",
    "created_at": "2010-10-27T23:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99854",
    "user": "@dandrake"
}
```

Hrm, removing that symlink doesn't always work: I deleted it, edited devel/sage/setup.py to not create the link (line 65 or so), and rebuilt the branch. 

Running Sage seems to work (I only have one branch at the moment, so no issues there), but if I try to run doctests, it fails with an ImportError -- it can't find sage.all_cmdline, which is ironic since I can run Sage at the commandline with no problem. 

sage-env is setting SAGE_BRANCH and PYTHONPATH appropriately, so there's still something that's not respecting those environment variables.



---

archive/issue_comments_099855.json:
```json
{
    "body": "Micro comment, just to say that I have been dreaming of that feature since I have started to use Sage. It would also be very useful when debugging, or doing research in parallel to reviewing patches.\n\nSo, thanks much in advance!",
    "created_at": "2010-10-29T12:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99855",
    "user": "@nthiery"
}
```

Micro comment, just to say that I have been dreaming of that feature since I have started to use Sage. It would also be very useful when debugging, or doing research in parallel to reviewing patches.

So, thanks much in advance!



---

archive/issue_comments_099856.json:
```json
{
    "body": "Ah, I think I found the problem with the doctesting: in `sage-doctest`, it overwrites $PYTHONPATH. I commented that out and running doctests works.\n\nI'll try to get a patch that incorporates my changes and upload that soon.",
    "created_at": "2010-11-02T03:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99856",
    "user": "@dandrake"
}
```

Ah, I think I found the problem with the doctesting: in `sage-doctest`, it overwrites $PYTHONPATH. I commented that out and running doctests works.

I'll try to get a patch that incorporates my changes and upload that soon.



---

archive/issue_comments_099857.json:
```json
{
    "body": "Attachment [9967-fix-sage-doctest.patch](tarball://root/attachments/some-uuid/ticket9967/9967-fix-sage-doctest.patch) by @dandrake created at 2010-11-02 08:18:35\n\napply to scripts repo",
    "created_at": "2010-11-02T08:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99857",
    "user": "@dandrake"
}
```

Attachment [9967-fix-sage-doctest.patch](tarball://root/attachments/some-uuid/ticket9967/9967-fix-sage-doctest.patch) by @dandrake created at 2010-11-02 08:18:35

apply to scripts repo



---

archive/issue_comments_099858.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-02T08:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99858",
    "user": "@dandrake"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099859.json:
```json
{
    "body": "Replying to [comment:27 nthiery]:\n> Micro comment, just to say that I have been dreaming of that feature since I have started to use Sage. It would also be very useful when debugging, or doing research in parallel to reviewing patches.\n\nIt would be great if you added a micro review to go along with your micro comment. :)\n\nThis patch needs a lot of testing, and it's close to being ready. So all you lurkers in the CC list, apply these patches and test!\n\nApply all the patches. The scripts repo gets:\n\n* 9967-concurrent-sagescripts.patch\n* 9967-sage-maketest.patch \n* 9967-fix-sage-doctest.patch \n\nand the rest go into the main library repo.",
    "created_at": "2010-11-02T08:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99859",
    "user": "@dandrake"
}
```

Replying to [comment:27 nthiery]:
> Micro comment, just to say that I have been dreaming of that feature since I have started to use Sage. It would also be very useful when debugging, or doing research in parallel to reviewing patches.

It would be great if you added a micro review to go along with your micro comment. :)

This patch needs a lot of testing, and it's close to being ready. So all you lurkers in the CC list, apply these patches and test!

Apply all the patches. The scripts repo gets:

* 9967-concurrent-sagescripts.patch
* 9967-sage-maketest.patch 
* 9967-fix-sage-doctest.patch 

and the rest go into the main library repo.



---

archive/issue_comments_099860.json:
```json
{
    "body": "Attachment [9967_sagelib_combined.patch](tarball://root/attachments/some-uuid/ticket9967/9967_sagelib_combined.patch) by @jdemeyer created at 2010-11-02 15:19:31\n\nCombined sagelib patch",
    "created_at": "2010-11-02T15:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99860",
    "user": "@jdemeyer"
}
```

Attachment [9967_sagelib_combined.patch](tarball://root/attachments/some-uuid/ticket9967/9967_sagelib_combined.patch) by @jdemeyer created at 2010-11-02 15:19:31

Combined sagelib patch



---

archive/issue_comments_099861.json:
```json
{
    "body": "Attachment [9967_scripts_combined.patch](tarball://root/attachments/some-uuid/ticket9967/9967_scripts_combined.patch) by @jdemeyer created at 2010-11-02 15:19:47\n\nCombined scripts patch",
    "created_at": "2010-11-02T15:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99861",
    "user": "@jdemeyer"
}
```

Attachment [9967_scripts_combined.patch](tarball://root/attachments/some-uuid/ticket9967/9967_scripts_combined.patch) by @jdemeyer created at 2010-11-02 15:19:47

Combined scripts patch



---

archive/issue_comments_099862.json:
```json
{
    "body": "Hrm, there's still a problem: when you do \"sage -b\", setup.py finds that there's no symlink in site-packages, and proceeds to put all the files there, instead of following the symlink. I'm trying to get it to go directly to sage-BRANCH/build/sage.",
    "created_at": "2010-11-03T02:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99862",
    "user": "@dandrake"
}
```

Hrm, there's still a problem: when you do "sage -b", setup.py finds that there's no symlink in site-packages, and proceeds to put all the files there, instead of following the symlink. I'm trying to get it to go directly to sage-BRANCH/build/sage.



---

archive/issue_comments_099863.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-03T02:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99863",
    "user": "@dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099864.json:
```json
{
    "body": "apply to Sage library",
    "created_at": "2010-11-04T02:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99864",
    "user": "@dandrake"
}
```

apply to Sage library



---

archive/issue_comments_099865.json:
```json
{
    "body": "Attachment [9967-no-site-packages-symlink.patch](tarball://root/attachments/some-uuid/ticket9967/9967-no-site-packages-symlink.patch) by @dandrake created at 2010-11-04 03:05:00\n\nThe patch I just uploaded still has some debugging statements but represents some progress.\n\nThere is still something in the doctesting framework that is using the symlink to the default branch and not using SAGE_BRANCH: if I doctest in the -main branch while -foo is the default, and delete the -foo branch, I get:\n\n\n```\nsage -t  devel/sage-main/sage/combinat/generator.py\nTraceback (most recent call last):\n  File \"/home/drake/.sage//tmp/generator.py\", line 2, in <module>\n    from sage.all_cmdline import *;\n  File \"/home/drake/s/sage-4.6.alpha3/devel/sage-main/build/sage/all_cmdline.py\", line 14, in <module>\n    from sage.all import *\n  File \"/home/drake/s/sage-4.6.alpha3/devel/sage-main/build/sage/all.py\", line 56, in <module>\n    from sage.rings.memory import pmem_malloc\nImportError: libcsage.so: cannot open shared object file: No such file or directory\n\n         [0.3 s]\n```\n\n\nThe ImportError occurs because whatever Python process is running that last line hasn't inherited our custom PYTHONPATH. (I think.)",
    "created_at": "2010-11-04T03:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99865",
    "user": "@dandrake"
}
```

Attachment [9967-no-site-packages-symlink.patch](tarball://root/attachments/some-uuid/ticket9967/9967-no-site-packages-symlink.patch) by @dandrake created at 2010-11-04 03:05:00

The patch I just uploaded still has some debugging statements but represents some progress.

There is still something in the doctesting framework that is using the symlink to the default branch and not using SAGE_BRANCH: if I doctest in the -main branch while -foo is the default, and delete the -foo branch, I get:


```
sage -t  devel/sage-main/sage/combinat/generator.py
Traceback (most recent call last):
  File "/home/drake/.sage//tmp/generator.py", line 2, in <module>
    from sage.all_cmdline import *;
  File "/home/drake/s/sage-4.6.alpha3/devel/sage-main/build/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/home/drake/s/sage-4.6.alpha3/devel/sage-main/build/sage/all.py", line 56, in <module>
    from sage.rings.memory import pmem_malloc
ImportError: libcsage.so: cannot open shared object file: No such file or directory

         [0.3 s]
```


The ImportError occurs because whatever Python process is running that last line hasn't inherited our custom PYTHONPATH. (I think.)



---

archive/issue_comments_099866.json:
```json
{
    "body": "Replying to [comment:32 ddrake]:\n> The ImportError occurs because whatever Python process is running that last line hasn't inherited our custom PYTHONPATH. (I think.) \n\nNope, I checked and the doctest script gets the environment variables right. It's finding Sage's Python modules just fine. Why can't it find libcsage.so?\n\nI am pretty much out of ideas at this point. Someone who understands this better than I needs to step in here. I started out refereeing this ticket, and now I find myself implementing it by myself.",
    "created_at": "2010-11-04T15:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99866",
    "user": "@dandrake"
}
```

Replying to [comment:32 ddrake]:
> The ImportError occurs because whatever Python process is running that last line hasn't inherited our custom PYTHONPATH. (I think.) 

Nope, I checked and the doctest script gets the environment variables right. It's finding Sage's Python modules just fine. Why can't it find libcsage.so?

I am pretty much out of ideas at this point. Someone who understands this better than I needs to step in here. I started out refereeing this ticket, and now I find myself implementing it by myself.



---

archive/issue_comments_099867.json:
```json
{
    "body": "Thanks all for looking at this. I'm just now catching up on the thread--I'll see if I can figure out what's going on here.",
    "created_at": "2010-11-04T17:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99867",
    "user": "@robertwb"
}
```

Thanks all for looking at this. I'm just now catching up on the thread--I'll see if I can figure out what's going on here.



---

archive/issue_comments_099868.json:
```json
{
    "body": "Last comment's anniversary!",
    "created_at": "2011-11-04T08:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99868",
    "user": "@nexttime"
}
```

Last comment's anniversary!



---

archive/issue_comments_099869.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2011-11-04T08:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99869",
    "user": "@nexttime"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_099870.json:
```json
{
    "body": "Changing component from doctest to doctest framework.",
    "created_at": "2013-03-28T22:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99870",
    "user": "@roed314"
}
```

Changing component from doctest to doctest framework.



---

archive/issue_comments_099871.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-01-28T16:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99871",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_099872.json:
```json
{
    "body": "Obsoleted by the new workflow I guess...",
    "created_at": "2014-01-28T16:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99872",
    "user": "@jdemeyer"
}
```

Obsoleted by the new workflow I guess...



---

archive/issue_comments_099873.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-01-30T13:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9966#issuecomment-99873",
    "user": "@vbraun"
}
```

Resolution: fixed
