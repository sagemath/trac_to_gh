# Issue 378: User-specified path for load and attach

archive/issues_000378.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  rossk\n\nThe patch allows\n\n```python\nsage: load_attach_path()\n['.']\nsage: load_attach_path('/path/to/my/sage/scripts')\nsage: load_attach_path()\n['.', '/path/to/my/sage/scripts']\nsage: attach('nifty_script1.sage')\nsage: attached_files()\n['/path/to/my/sage/scripts/nifty_script1.sage']\n```\nYou can also set an environment variable:\n\n```sh\n$ export SAGE_LOAD_ATTACH_PATH=\"$HOME/foo:$HOME/bar\"\n$ sage\nsage: load_attach_path()\n['.', '/home/mpatel/foo', '/home/mpatel/bar']\n```\nNote:  We now use the full path in the attached files dictionary.\n\nIssue created by migration from https://trac.sagemath.org/ticket/378\n\n",
    "closed_at": "2010-11-10T22:19:14Z",
    "created_at": "2007-05-25T16:28:34Z",
    "labels": [
        "component: user interface"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "User-specified path for load and attach",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/378",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  rossk

The patch allows

```python
sage: load_attach_path()
['.']
sage: load_attach_path('/path/to/my/sage/scripts')
sage: load_attach_path()
['.', '/path/to/my/sage/scripts']
sage: attach('nifty_script1.sage')
sage: attached_files()
['/path/to/my/sage/scripts/nifty_script1.sage']
```
You can also set an environment variable:

```sh
$ export SAGE_LOAD_ATTACH_PATH="$HOME/foo:$HOME/bar"
$ sage
sage: load_attach_path()
['.', '/home/mpatel/foo', '/home/mpatel/bar']
```
Note:  We now use the full path in the attached files dictionary.

Issue created by migration from https://trac.sagemath.org/ticket/378





---

archive/issue_comments_001792.json:
```json
{
    "body": "#1484 is related.",
    "created_at": "2010-01-20T11:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1792",
    "user": "https://github.com/qed777"
}
```

#1484 is related.



---

archive/issue_comments_001793.json:
```json
{
    "body": "So is #516.",
    "created_at": "2010-01-22T04:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1793",
    "user": "https://github.com/qed777"
}
```

So is #516.



---

archive/issue_comments_001794.json:
```json
{
    "body": "That should be #5169.",
    "created_at": "2010-01-22T04:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1794",
    "user": "https://github.com/qed777"
}
```

That should be #5169.



---

archive/issue_comments_001795.json:
```json
{
    "body": "First take on load / attach path.  sage repo.",
    "created_at": "2010-02-16T00:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1795",
    "user": "https://github.com/qed777"
}
```

First take on load / attach path.  sage repo.



---

archive/issue_comments_001796.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-16T00:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1796",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_001797.json:
```json
{
    "body": "Attachment [trac_378-load_attach_path.patch](tarball://root/attachments/some-uuid/ticket378/trac_378-load_attach_path.patch) by @qed777 created at 2010-02-16 00:22:23\n\nFeel free to improve the patch!",
    "created_at": "2010-02-16T00:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1797",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_378-load_attach_path.patch](tarball://root/attachments/some-uuid/ticket378/trac_378-load_attach_path.patch) by @qed777 created at 2010-02-16 00:22:23

Feel free to improve the patch!



---

archive/issue_comments_001798.json:
```json
{
    "body": "We should skip the search, if the given filename is an absolute path.",
    "created_at": "2010-02-18T02:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1798",
    "user": "https://github.com/qed777"
}
```

We should skip the search, if the given filename is an absolute path.



---

archive/issue_comments_001799.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-18T02:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1799",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_001800.json:
```json
{
    "body": "Should we add an option (`recurse=False`?) that makes `load` and `attach` search the entire directory tree under each search path?",
    "created_at": "2010-02-18T03:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1800",
    "user": "https://github.com/qed777"
}
```

Should we add an option (`recurse=False`?) that makes `load` and `attach` search the entire directory tree under each search path?



---

archive/issue_comments_001801.json:
```json
{
    "body": "Attachment [trac_378-load_attach_path.2.patch](tarball://root/attachments/some-uuid/ticket378/trac_378-load_attach_path.2.patch) by @qed777 created at 2010-02-20 23:49:33\n\nMore examples.  Handle absolute paths.  Replaces previous.",
    "created_at": "2010-02-20T23:49:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1801",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_378-load_attach_path.2.patch](tarball://root/attachments/some-uuid/ticket378/trac_378-load_attach_path.2.patch) by @qed777 created at 2010-02-20 23:49:33

More examples.  Handle absolute paths.  Replaces previous.



---

archive/issue_comments_001802.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-20T23:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1802",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_001803.json:
```json
{
    "body": "With V2,\u00a0we skip the search if given an absolute path.  I've also added some examples.",
    "created_at": "2010-02-20T23:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1803",
    "user": "https://github.com/qed777"
}
```

With V2, we skip the search if given an absolute path.  I've also added some examples.



---

archive/issue_comments_001804.json:
```json
{
    "body": "Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append(\"~/foo\"). What do you think?",
    "created_at": "2010-04-17T18:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1804",
    "user": "https://github.com/TimDumol"
}
```

Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append("~/foo"). What do you think?



---

archive/issue_comments_001805.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-06-05T00:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1805",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_001806.json:
```json
{
    "body": "Replying to [comment:10 timdumol]:\n> Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append(\"~/foo\"). What do you think?\n\n\nBoth ideas sound great.  I can't make the changes immediately, but I'll try to attach a new patch soon.",
    "created_at": "2010-06-23T01:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1806",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:10 timdumol]:
> Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append("~/foo"). What do you think?


Both ideas sound great.  I can't make the changes immediately, but I'll try to attach a new patch soon.



---

archive/issue_comments_001807.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-06-23T01:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1807",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_001808.json:
```json
{
    "body": "Available as another reviewer if you need one.",
    "created_at": "2010-07-10T04:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1808",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Available as another reviewer if you need one.



---

archive/issue_comments_001809.json:
```json
{
    "body": "Is this still alive? I found myself in need of this functionality today and was surprised it is not there; how does anyone use the notebook locally without it?\n\nAnyway, I'd like to help out fixing or reviewing if necessary.\nI've only glanced at the current patch but found this anomaly: Shouldn't line 1399 be changed to \n\n```\nwhile '' in _load_attach_path:\n```\nso as to remove any number of empty entries (e.g. if user wrote SAGE_LOAD_ATTACH_PATH = \":::::foo::\")\n\nCheers, Johan",
    "created_at": "2010-10-21T09:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1809",
    "user": "https://github.com/johanrosenkilde"
}
```

Is this still alive? I found myself in need of this functionality today and was surprised it is not there; how does anyone use the notebook locally without it?

Anyway, I'd like to help out fixing or reviewing if necessary.
I've only glanced at the current patch but found this anomaly: Shouldn't line 1399 be changed to 

```
while '' in _load_attach_path:
```
so as to remove any number of empty entries (e.g. if user wrote SAGE_LOAD_ATTACH_PATH = ":::::foo::")

Cheers, Johan



---

archive/issue_comments_001810.json:
```json
{
    "body": "Thanks for the interest!  Unfortunately, I've been busy with other tasks (Sage and non-Sage) and haven't had the time to rework the patch to incorporate Tim's suggestions.  Is anyone willing to do that?",
    "created_at": "2010-10-21T09:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1810",
    "user": "https://github.com/qed777"
}
```

Thanks for the interest!  Unfortunately, I've been busy with other tasks (Sage and non-Sage) and haven't had the time to rework the patch to incorporate Tim's suggestions.  Is anyone willing to do that?



---

archive/issue_comments_001811.json:
```json
{
    "body": "Replying to [comment:10 timdumol]:\n> Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append(\"~/foo\"). What do you think?\n\n\nI've had a bit of a hack at exposing the array itself, but there are problems making it sufficiently global.  `sys.path` works for the stdlib because `path` is a variable in the `sys` module.  The logical thing to do here is to create a `load_attach_path` variable in the preparser module, but following the stdlib analogy this would require the user to edit `sage.misc.preparser.load_attach_path`, which is not very user friendly.\n\nFailing this, it looks like the best you can do is a `from sage.misc.preparser import load_attach_path`, but this is a fragile state of affairs: if you reassign `load_attach_path` anywhere, either from sage's command line or by calling some function like `sage.misc.preparser.reset_load_attach_path()`, you end up with a situation where `load_attach_path` and `sage.misc.preparser.load_attach_path` are different objects.\n\nThis requires caution on the part of the user and the programmer.  For example, `reset_load_attach_path()` can't include\n\n```\nload_attach_path = ['.']\n```\n\ninstead it has to do\n\n```\nwhile load_attach_path != []:\n    load_attach_path.pop()\nload_attach_path.append('.')\n```\n\nIf the user accidentally reassigns `load_attach_path` in the command line, they'll have to re-run `from sage.misc.preparser import load_attach_path`.  I don't think that this step can be included in a `reset_load_attach_path()` function due to the different scopes.\n\nSo it's possible to expose the `load_attach_path` array to the user, and I've written most of a patch that does this, but there's lots of things that could go wrong so I'd suggest sticking to the existing patch's approach of hiding behind a function.  If others think that the pros outweigh the cons then I'll tidy up the patch and upload it.\n\nThoughts?",
    "created_at": "2010-11-04T05:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1811",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Replying to [comment:10 timdumol]:
> Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append("~/foo"). What do you think?


I've had a bit of a hack at exposing the array itself, but there are problems making it sufficiently global.  `sys.path` works for the stdlib because `path` is a variable in the `sys` module.  The logical thing to do here is to create a `load_attach_path` variable in the preparser module, but following the stdlib analogy this would require the user to edit `sage.misc.preparser.load_attach_path`, which is not very user friendly.

Failing this, it looks like the best you can do is a `from sage.misc.preparser import load_attach_path`, but this is a fragile state of affairs: if you reassign `load_attach_path` anywhere, either from sage's command line or by calling some function like `sage.misc.preparser.reset_load_attach_path()`, you end up with a situation where `load_attach_path` and `sage.misc.preparser.load_attach_path` are different objects.

This requires caution on the part of the user and the programmer.  For example, `reset_load_attach_path()` can't include

```
load_attach_path = ['.']
```

instead it has to do

```
while load_attach_path != []:
    load_attach_path.pop()
load_attach_path.append('.')
```

If the user accidentally reassigns `load_attach_path` in the command line, they'll have to re-run `from sage.misc.preparser import load_attach_path`.  I don't think that this step can be included in a `reset_load_attach_path()` function due to the different scopes.

So it's possible to expose the `load_attach_path` array to the user, and I've written most of a patch that does this, but there's lots of things that could go wrong so I'd suggest sticking to the existing patch's approach of hiding behind a function.  If others think that the pros outweigh the cons then I'll tidy up the patch and upload it.

Thoughts?



---

archive/issue_comments_001812.json:
```json
{
    "body": "Attachment [trac_378-load_attach_path.2.1.patch](tarball://root/attachments/some-uuid/ticket378/trac_378-load_attach_path.2.1.patch) by flawrence created at 2010-11-04 06:14:08\n\nuse os.path.userexpand on load, separate reset function, also use paths for detach. replaces previous.",
    "created_at": "2010-11-04T06:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1812",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Attachment [trac_378-load_attach_path.2.1.patch](tarball://root/attachments/some-uuid/ticket378/trac_378-load_attach_path.2.1.patch) by flawrence created at 2010-11-04 06:14:08

use os.path.userexpand on load, separate reset function, also use paths for detach. replaces previous.



---

archive/issue_comments_001813.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-04T06:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1813",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_001814.json:
```json
{
    "body": "Assuming that no-one comes up with a robust and convenient way to expose the array, I've uploaded a patch that addresses Tim's other idea, Johan's comment, and two other main changes:\n\n* You can now use paths with `detach`\n\n* `reset_load_attach_path` is now a function on its own, which gets called upon startup.  Note that it now resets the path to '.' plus the contents of the path environment variable `SAGE_LOAD_ATTACH_PATH`, rather than to '.' alone.",
    "created_at": "2010-11-04T06:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1814",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Assuming that no-one comes up with a robust and convenient way to expose the array, I've uploaded a patch that addresses Tim's other idea, Johan's comment, and two other main changes:

* You can now use paths with `detach`

* `reset_load_attach_path` is now a function on its own, which gets called upon startup.  Note that it now resets the path to '.' plus the contents of the path environment variable `SAGE_LOAD_ATTACH_PATH`, rather than to '.' alone.



---

archive/issue_comments_001815.json:
```json
{
    "body": "Reviewing this on 4.6.1.alpha1 - should I be using 4.6?\n\n```\n/scratch/rossk/sage-4.6.1/devel/sage$ hg qpush\napplying trac_378-load_attach_path.2.1.patch\npatching file sage/misc/all.py\nHunk #1 FAILED at 57\n1 out of 1 hunks FAILED -- saving rejects to file sage/misc/all.py.rej\npatching file sage/misc/preparser.py\nHunk #1 FAILED at 1390\nHunk #2 FAILED at 1488\nHunk #3 FAILED at 1497\nHunk #4 FAILED at 1533\nHunk #5 FAILED at 1568\nHunk #6 FAILED at 1582\nHunk #7 FAILED at 1593\nHunk #8 FAILED at 1608\nHunk #9 FAILED at 1618\nHunk #10 FAILED at 1771\n10 out of 10 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_378-load_attach_path.2.1.patch\n```",
    "created_at": "2010-11-05T02:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1815",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Reviewing this on 4.6.1.alpha1 - should I be using 4.6?

```
/scratch/rossk/sage-4.6.1/devel/sage$ hg qpush
applying trac_378-load_attach_path.2.1.patch
patching file sage/misc/all.py
Hunk #1 FAILED at 57
1 out of 1 hunks FAILED -- saving rejects to file sage/misc/all.py.rej
patching file sage/misc/preparser.py
Hunk #1 FAILED at 1390
Hunk #2 FAILED at 1488
Hunk #3 FAILED at 1497
Hunk #4 FAILED at 1533
Hunk #5 FAILED at 1568
Hunk #6 FAILED at 1582
Hunk #7 FAILED at 1593
Hunk #8 FAILED at 1608
Hunk #9 FAILED at 1618
Hunk #10 FAILED at 1771
10 out of 10 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_378-load_attach_path.2.1.patch
```



---

archive/issue_comments_001816.json:
```json
{
    "body": "Attachment [trac_387-load_attach_path.2.1.patch](tarball://root/attachments/some-uuid/ticket378/trac_387-load_attach_path.2.1.patch) by flawrence created at 2010-11-05 02:46:38\n\nuse os.path.userexpand on load, separate reset function, also use paths for detach. actually replaces previous this time..",
    "created_at": "2010-11-05T02:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1816",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Attachment [trac_387-load_attach_path.2.1.patch](tarball://root/attachments/some-uuid/ticket378/trac_387-load_attach_path.2.1.patch) by flawrence created at 2010-11-05 02:46:38

use os.path.userexpand on load, separate reset function, also use paths for detach. actually replaces previous this time..



---

archive/issue_comments_001817.json:
```json
{
    "body": "Sorry, I'm new to mercurial queues and stuffed up the patch (it did rely on the other patch after all).  The new patch I just uploaded should work on 4.6 without mpatel's patch, and hopefully 4.6.alpha1 too.",
    "created_at": "2010-11-05T02:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1817",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Sorry, I'm new to mercurial queues and stuffed up the patch (it did rely on the other patch after all).  The new patch I just uploaded should work on 4.6 without mpatel's patch, and hopefully 4.6.alpha1 too.



---

archive/issue_comments_001818.json:
```json
{
    "body": "Replying to [comment:19 flawrence]:\n> Sorry, I'm new to mercurial queues and stuffed up the patch (it did rely on the other patch after all).  The new patch I just uploaded should work on 4.6 without mpatel's patch, and hopefully 4.6.alpha1 too.\n\n\nIm new to mercurial queues too (and much more :-). Thought youd like to know your new patch was error free. (Ill test over the weekend and report back when I can - sorry it cant be sooner).",
    "created_at": "2010-11-05T08:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1818",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Replying to [comment:19 flawrence]:
> Sorry, I'm new to mercurial queues and stuffed up the patch (it did rely on the other patch after all).  The new patch I just uploaded should work on 4.6 without mpatel's patch, and hopefully 4.6.alpha1 too.


Im new to mercurial queues too (and much more :-). Thought youd like to know your new patch was error free. (Ill test over the weekend and report back when I can - sorry it cant be sooner).



---

archive/issue_comments_001819.json:
```json
{
    "body": "Replying to [comment:16 flawrence]:\n> Replying to [comment:10 timdumol]:\n> > Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append(\"~/foo\"). What do you think?\n\n> \n> I've had a bit of a hack at exposing the array itself, but there are problems making it sufficiently global.  `sys.path` works for the stdlib because `path` is a variable in the `sys` module.  The logical thing to do here is to create a `load_attach_path` variable in the preparser module, but following the stdlib analogy this would require the user to edit `sage.misc.preparser.load_attach_path`, which is not very user friendly.\n> \n> Failing this, it looks like the best you can do is a `from sage.misc.preparser import load_attach_path`, but this is a fragile state of affairs: if you reassign `load_attach_path` anywhere, either from sage's command line or by calling some function like `sage.misc.preparser.reset_load_attach_path()`, you end up with a situation where `load_attach_path` and `sage.misc.preparser.load_attach_path` are different objects.\n> \n> This requires caution on the part of the user and the programmer.  For example, `reset_load_attach_path()` can't include\n> \n> ```\n> load_attach_path = ['.']\n> ```\n> \n> instead it has to do\n> \n> ```\n> while load_attach_path != []:\n>     load_attach_path.pop()\n> load_attach_path.append('.')\n> ```\n> \n> If the user accidentally reassigns `load_attach_path` in the command line, they'll have to re-run `from sage.misc.preparser import load_attach_path`.  I don't think that this step can be included in a `reset_load_attach_path()` function due to the different scopes.\n> \n> So it's possible to expose the `load_attach_path` array to the user, and I've written most of a patch that does this, but there's lots of things that could go wrong so I'd suggest sticking to the existing patch's approach of hiding behind a function.  If others think that the pros outweigh the cons then I'll tidy up the patch and upload it.\n> \n> Thoughts?\n\n \nVery astute! I was almost finished with my own patch, falling into all the same holes as you describe :-) Your concern at least begs the question on whether this is what we want to do, as it might fool some users. However, a possible usage pattern - in case load_attach_path is fully exposed - is the following\n\n```\n   import sage.misc.preparser as pre\n   pre.load_attach_path = [ ... ]\n```\n\nStill, this is not very nice, and doesn't really fit into the \"import sage.all\" scheme. A third possibility is to \"decide\" that we might very well need such global variables in other places, stemming from various other foundational modules, and therefore introduce a new module sage.misc.globals to hold these. When Sage launches, it imports this module as \"globals\", and so, for any global variable - say load_attach_path -, the user would access it and modify it as globals.load_attach_path. I don't think that would be unnatural at all. However, it might be overkill if load_attach_path is the _only_ such conceivable global value, but for some reason (perhaps the sheer size of Sage), I can't really think it is.\n\nIf none of these sound compelling, then I vote yes on the current form (I haven't tested the patch, that is). My only comment on the current patch, is that maybe there should be a TODO (or a fix ;-) ) in reset_load_attach_path(), which notes that probably the elements of SAGE_LOAD_ATTACH_PATH should be uniquified while preserving the order (thus, list(set(_load_attach_path)) is no good). After that the while could be reverted to an if again when removing the empty element.\n\nOtherwise good work. I'm looking forward to this patch in Sage, whatever the format :-)\nCheers, Johan",
    "created_at": "2010-11-05T08:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1819",
    "user": "https://github.com/johanrosenkilde"
}
```

Replying to [comment:16 flawrence]:
> Replying to [comment:10 timdumol]:
> > Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append("~/foo"). What do you think?

> 
> I've had a bit of a hack at exposing the array itself, but there are problems making it sufficiently global.  `sys.path` works for the stdlib because `path` is a variable in the `sys` module.  The logical thing to do here is to create a `load_attach_path` variable in the preparser module, but following the stdlib analogy this would require the user to edit `sage.misc.preparser.load_attach_path`, which is not very user friendly.
> 
> Failing this, it looks like the best you can do is a `from sage.misc.preparser import load_attach_path`, but this is a fragile state of affairs: if you reassign `load_attach_path` anywhere, either from sage's command line or by calling some function like `sage.misc.preparser.reset_load_attach_path()`, you end up with a situation where `load_attach_path` and `sage.misc.preparser.load_attach_path` are different objects.
> 
> This requires caution on the part of the user and the programmer.  For example, `reset_load_attach_path()` can't include
> 
> ```
> load_attach_path = ['.']
> ```
> 
> instead it has to do
> 
> ```
> while load_attach_path != []:
>     load_attach_path.pop()
> load_attach_path.append('.')
> ```
> 
> If the user accidentally reassigns `load_attach_path` in the command line, they'll have to re-run `from sage.misc.preparser import load_attach_path`.  I don't think that this step can be included in a `reset_load_attach_path()` function due to the different scopes.
> 
> So it's possible to expose the `load_attach_path` array to the user, and I've written most of a patch that does this, but there's lots of things that could go wrong so I'd suggest sticking to the existing patch's approach of hiding behind a function.  If others think that the pros outweigh the cons then I'll tidy up the patch and upload it.
> 
> Thoughts?

 
Very astute! I was almost finished with my own patch, falling into all the same holes as you describe :-) Your concern at least begs the question on whether this is what we want to do, as it might fool some users. However, a possible usage pattern - in case load_attach_path is fully exposed - is the following

```
   import sage.misc.preparser as pre
   pre.load_attach_path = [ ... ]
```

Still, this is not very nice, and doesn't really fit into the "import sage.all" scheme. A third possibility is to "decide" that we might very well need such global variables in other places, stemming from various other foundational modules, and therefore introduce a new module sage.misc.globals to hold these. When Sage launches, it imports this module as "globals", and so, for any global variable - say load_attach_path -, the user would access it and modify it as globals.load_attach_path. I don't think that would be unnatural at all. However, it might be overkill if load_attach_path is the _only_ such conceivable global value, but for some reason (perhaps the sheer size of Sage), I can't really think it is.

If none of these sound compelling, then I vote yes on the current form (I haven't tested the patch, that is). My only comment on the current patch, is that maybe there should be a TODO (or a fix ;-) ) in reset_load_attach_path(), which notes that probably the elements of SAGE_LOAD_ATTACH_PATH should be uniquified while preserving the order (thus, list(set(_load_attach_path)) is no good). After that the while could be reverted to an if again when removing the empty element.

Otherwise good work. I'm looking forward to this patch in Sage, whatever the format :-)
Cheers, Johan



---

archive/issue_comments_001820.json:
```json
{
    "body": "Thanks to everyone for working on this ticket!\n\nOne question that may relate to how/whether we \"expose\" the path list:  Would users want Sage to search some paths recursively for files to load or attach?  How would we store this information?  Perhaps as\n\n```python\n['/some/path', ('/a/path/to/search/recursively', True), '/another/path']\n```\n?  Of course, this needn't hold up this ticket.",
    "created_at": "2010-11-05T10:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1820",
    "user": "https://github.com/qed777"
}
```

Thanks to everyone for working on this ticket!

One question that may relate to how/whether we "expose" the path list:  Would users want Sage to search some paths recursively for files to load or attach?  How would we store this information?  Perhaps as

```python
['/some/path', ('/a/path/to/search/recursively', True), '/another/path']
```
?  Of course, this needn't hold up this ticket.



---

archive/issue_comments_001821.json:
```json
{
    "body": "Replying to [comment:21 jsrn]:\n\n>  My only comment on the current patch, is that maybe there should be a TODO (or a fix ;-) ) in reset_load_attach_path(), which notes that probably the elements of SAGE_LOAD_ATTACH_PATH should be uniquified while preserving the order (thus, list(set(_load_attach_path)) is no good). After that the while could be reverted to an if again when removing the empty element.\n\n\nDo we really need to test for uniqueness at all? It's the user's fault if they get it wrong, and the only negative consequence I see is that attaching/loading files (not the sort of operation that sits deep in a loop) a tiny tiny bit slower.  Python doesn't check for uniqueness in sys.path, BASH doesn't check for uniqueness in $PATH.  AFAIK the main argument for uniqueness is aesthetics; perhaps we can leave this to the user rather than try to tidy up after them (and perhaps do something unexpected in the process)?\n\nReplying to [comment:22 mpatel]:\n>One question that may relate to how/whether we \"expose\" the path list: Would users want Sage to search some paths recursively for files to load or attach? How would we store this information?\n\n\nThis is an interesting question.  I think it would be a nice feature.  Since we don't actually expose the path array, it would be easy to add such features later, so it's probably best as a new ticket.\n\n\nI also noticed that I was fat-fingered typing the name of the new patch - 387 instead of 378.  *sigh*",
    "created_at": "2010-11-05T14:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1821",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Replying to [comment:21 jsrn]:

>  My only comment on the current patch, is that maybe there should be a TODO (or a fix ;-) ) in reset_load_attach_path(), which notes that probably the elements of SAGE_LOAD_ATTACH_PATH should be uniquified while preserving the order (thus, list(set(_load_attach_path)) is no good). After that the while could be reverted to an if again when removing the empty element.


Do we really need to test for uniqueness at all? It's the user's fault if they get it wrong, and the only negative consequence I see is that attaching/loading files (not the sort of operation that sits deep in a loop) a tiny tiny bit slower.  Python doesn't check for uniqueness in sys.path, BASH doesn't check for uniqueness in $PATH.  AFAIK the main argument for uniqueness is aesthetics; perhaps we can leave this to the user rather than try to tidy up after them (and perhaps do something unexpected in the process)?

Replying to [comment:22 mpatel]:
>One question that may relate to how/whether we "expose" the path list: Would users want Sage to search some paths recursively for files to load or attach? How would we store this information?


This is an interesting question.  I think it would be a nice feature.  Since we don't actually expose the path array, it would be easy to add such features later, so it's probably best as a new ticket.


I also noticed that I was fat-fingered typing the name of the new patch - 387 instead of 378.  *sigh*



---

archive/issue_comments_001822.json:
```json
{
    "body": "Quick question: attached_files() works without an import but load_attach_path() is unknown (raises a \"NameError\" exception when called). Are we supposed to import it in order to use it?",
    "created_at": "2010-11-06T03:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1822",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Quick question: attached_files() works without an import but load_attach_path() is unknown (raises a "NameError" exception when called). Are we supposed to import it in order to use it?



---

archive/issue_comments_001823.json:
```json
{
    "body": "You shouldn't have to import `load_attach_path()` manually.  Applying the patch and rebuilding on 4.6 worked for me.  Maybe you forgot to rebuild sage after applying the most recent patch?",
    "created_at": "2010-11-06T04:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1823",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

You shouldn't have to import `load_attach_path()` manually.  Applying the patch and rebuilding on 4.6 worked for me.  Maybe you forgot to rebuild sage after applying the most recent patch?



---

archive/issue_comments_001824.json:
```json
{
    "body": "Replying to [comment:25 flawrence]:\n> You shouldn't have to import `load_attach_path()` manually.  Applying the patch and rebuilding on 4.6 worked for me.  Maybe you forgot to rebuild sage after applying the most recent patch?\n\n\nDoh! Certainly did forget and rebuilding worked - thanks!",
    "created_at": "2010-11-06T05:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1824",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Replying to [comment:25 flawrence]:
> You shouldn't have to import `load_attach_path()` manually.  Applying the patch and rebuilding on 4.6 worked for me.  Maybe you forgot to rebuild sage after applying the most recent patch?


Doh! Certainly did forget and rebuilding worked - thanks!



---

archive/issue_comments_001825.json:
```json
{
    "body": "I exercised this reasonably well and the functionality is great. After it passed all the tests I could think of, I renamed the folder that had the attached file (to see what would happen). The error was not unexpected: \"OSError: [Errno 2] No such file or directory: ...\". But this error persisted no matter what was done afterwards (even just \"1+1\"!). I had to get out of Sage to start again. Thats the most pressing issue I could find but otherwise looks good! Theres also a couple of ideas I can run by you if you want, now that Ive exercised all the use cases I could think of.",
    "created_at": "2010-11-06T06:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1825",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

I exercised this reasonably well and the functionality is great. After it passed all the tests I could think of, I renamed the folder that had the attached file (to see what would happen). The error was not unexpected: "OSError: [Errno 2] No such file or directory: ...". But this error persisted no matter what was done afterwards (even just "1+1"!). I had to get out of Sage to start again. Thats the most pressing issue I could find but otherwise looks good! Theres also a couple of ideas I can run by you if you want, now that Ive exercised all the use cases I could think of.



---

archive/issue_comments_001826.json:
```json
{
    "body": "Replying to [comment:27 rossk]:\n>I renamed the folder that had the attached file (to see what would happen). The error was not unexpected: \"OSError: [Errno 2] No such file or directory: ...\". But this error persisted no matter what was done afterwards (even just \"1+1\"!). I had to get out of Sage to start again.\n\n\nI've checked and this happens even without this patch applied, so it's a separate issue I think.  Not much error checking is done for attached files!  I've started ticket #10229 for this.",
    "created_at": "2010-11-06T13:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1826",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Replying to [comment:27 rossk]:
>I renamed the folder that had the attached file (to see what would happen). The error was not unexpected: "OSError: [Errno 2] No such file or directory: ...". But this error persisted no matter what was done afterwards (even just "1+1"!). I had to get out of Sage to start again.


I've checked and this happens even without this patch applied, so it's a separate issue I think.  Not much error checking is done for attached files!  I've started ticket #10229 for this.



---

archive/issue_comments_001827.json:
```json
{
    "body": "Because the functionality is important, it works as designed, and passed all tests (the path can be set, displayed and modified as intended), this ticket can get a positive review now. If nobody objects, Ill do that after a short wait for any feedback on the next comment.",
    "created_at": "2010-11-06T20:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1827",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Because the functionality is important, it works as designed, and passed all tests (the path can be set, displayed and modified as intended), this ticket can get a positive review now. If nobody objects, Ill do that after a short wait for any feedback on the next comment.



---

archive/issue_comments_001828.json:
```json
{
    "body": "It may be too late for the following suggestions but Ill put them forward in case you think they have enough merit to refactor the code now (otherwise ignore them or they can go in another ticket). They are based on the idea that the main things we want to do with a path is: (1) start Sage with a sensible default (2) display what the current path is (3) set the path (4) add a folder to the end/beginning of the path (5) reset the path (6) totally clear the path. (I acknowledge some ideas have come from other packages e.g. matlab). So here's is how the path may be made to work in the future. Please let me know what you think. These are just ideas and doesnt change the good work youve already done - thanks for that!  \n\n```\n# display the default attach-path (unless a SAGE_ATTACH_PATH environment variable is set, then the attach-path when Sage starts is the path in SAGE_ATTACH_PATH)\nsage: attach_path()\n['.']\n\n# set the attach path to a list of folders: ['./folder1','./folder2']\n# (Note: if you want the current directory '.' included, you must specify it)\nsage: attach_path(['folder1','folder2'])\n\n# append to the (end of) attach path\nsage: attach_path_join(attach_path(), ['folder3'])\n\n# display the attach path \nsage: attach_path()\n['folder1','folder2','folder3']\n\n# add to the start of the attach path\nsage: attach_path_join(['folder0'], attach_path())\n\n# display the attach path again\nsage: attach_path()\n['folder0','folder1','folder2','folder3']\n\n# append to the (end of) attach path *recursively*\nsage: attach_path_join_subfolders(attach_path(), ['folder4'])\n\n# display the attach path \nsage: attach_path()\n['folder0','folder1','folder2','folder3','folder4','folder4/dir1','folder4/dir2']\n\n# reset the attach path - sets the attach path to the default \nsage: reset_attach_path()\n\n# clear the attach path - sets it to '' i.e. neither '.' nor SAGE_ATTACH_PATH  are included (when you want to ensure no implicit attaching is done or to rebuild the path from scratch)\nsage: clear_attach_path()\n\n# display the attach path \nsage: attach_path()\n[]\n```",
    "created_at": "2010-11-06T20:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1828",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

It may be too late for the following suggestions but Ill put them forward in case you think they have enough merit to refactor the code now (otherwise ignore them or they can go in another ticket). They are based on the idea that the main things we want to do with a path is: (1) start Sage with a sensible default (2) display what the current path is (3) set the path (4) add a folder to the end/beginning of the path (5) reset the path (6) totally clear the path. (I acknowledge some ideas have come from other packages e.g. matlab). So here's is how the path may be made to work in the future. Please let me know what you think. These are just ideas and doesnt change the good work youve already done - thanks for that!  

```
# display the default attach-path (unless a SAGE_ATTACH_PATH environment variable is set, then the attach-path when Sage starts is the path in SAGE_ATTACH_PATH)
sage: attach_path()
['.']

# set the attach path to a list of folders: ['./folder1','./folder2']
# (Note: if you want the current directory '.' included, you must specify it)
sage: attach_path(['folder1','folder2'])

# append to the (end of) attach path
sage: attach_path_join(attach_path(), ['folder3'])

# display the attach path 
sage: attach_path()
['folder1','folder2','folder3']

# add to the start of the attach path
sage: attach_path_join(['folder0'], attach_path())

# display the attach path again
sage: attach_path()
['folder0','folder1','folder2','folder3']

# append to the (end of) attach path *recursively*
sage: attach_path_join_subfolders(attach_path(), ['folder4'])

# display the attach path 
sage: attach_path()
['folder0','folder1','folder2','folder3','folder4','folder4/dir1','folder4/dir2']

# reset the attach path - sets the attach path to the default 
sage: reset_attach_path()

# clear the attach path - sets it to '' i.e. neither '.' nor SAGE_ATTACH_PATH  are included (when you want to ensure no implicit attaching is done or to rebuild the path from scratch)
sage: clear_attach_path()

# display the attach path 
sage: attach_path()
[]
```



---

archive/issue_comments_001829.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-07T10:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1829",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_001830.json:
```json
{
    "body": "Time to give this the positive review it deserves. Looking forward to using attach paths!",
    "created_at": "2010-11-07T10:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1830",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Time to give this the positive review it deserves. Looking forward to using attach paths!



---

archive/issue_events_000874.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-10T22:19:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/378#event-874"
}
```



---

archive/issue_comments_001831.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-10T22:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/378#issuecomment-1831",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
