# Issue 9739: Handle duplicate file basenames when testing multiple files in parallel

archive/issues_009739.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  drkirkby jhpalmieri leif robertwb jdemeyer\n\nWhen we test\n\n`/path/to/foo.py`\n\n`sage-doctest` writes\n\n`SAGE_TESTDIR/.doctest_foo.py`\n\nruns the new file through `python`, and deletes it.  This can cause\ncollisions when we test in parallel multiple files with the same\nbasename, e.g., `__init__`, `all`, `misc`, `conf`, `constructor`, `morphism`, `index`, `tests`, `homset`, `element`, `twist`, `tutorial`, `sagetex`, `crystals`, `cartesian_product`, `template`, `ring`, etc.\n\nThere's a similar problem with testing non-library files, which `sage-doctest` first effectively copies to `SAGE_TESTDIR`.\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/367bfc0d83c0e9b8#367bfc0d83c0e9b8) for background.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9739\n\n",
    "created_at": "2010-08-13T01:27:24Z",
    "labels": [
        "doctest",
        "critical",
        "bug"
    ],
    "title": "Handle duplicate file basenames when testing multiple files in parallel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9739",
    "user": "mpatel"
}
```
Assignee: mvngu

CC:  drkirkby jhpalmieri leif robertwb jdemeyer

When we test

`/path/to/foo.py`

`sage-doctest` writes

`SAGE_TESTDIR/.doctest_foo.py`

runs the new file through `python`, and deletes it.  This can cause
collisions when we test in parallel multiple files with the same
basename, e.g., `__init__`, `all`, `misc`, `conf`, `constructor`, `morphism`, `index`, `tests`, `homset`, `element`, `twist`, `tutorial`, `sagetex`, `crystals`, `cartesian_product`, `template`, `ring`, etc.

There's a similar problem with testing non-library files, which `sage-doctest` first effectively copies to `SAGE_TESTDIR`.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/367bfc0d83c0e9b8#367bfc0d83c0e9b8) for background.

Issue created by migration from https://trac.sagemath.org/ticket/9739





---

archive/issue_comments_095221.json:
```json
{
    "body": "William Stein [suggests](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/488672084383d442#488672084383d442):\n\n```\nCould we use the tempfile module instead of using SAGE_TESTDIR.  The\ntempfile module makes files and directories by default that are unique\nand are *designed* to live on a fast filesystem, which gets cleaned\nregularly.\n\nsage: import tempfile \n```\n",
    "created_at": "2010-08-13T01:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95221",
    "user": "mpatel"
}
```

William Stein [suggests](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/488672084383d442#488672084383d442):

```
Could we use the tempfile module instead of using SAGE_TESTDIR.  The
tempfile module makes files and directories by default that are unique
and are *designed* to live on a fast filesystem, which gets cleaned
regularly.

sage: import tempfile 
```




---

archive/issue_comments_095222.json:
```json
{
    "body": "Attachment [basenames_frequencies.txt](tarball://root/attachments/some-uuid/ticket9739/basenames_frequencies.txt) by mpatel created at 2010-08-13 01:39:09\n\nFrequency-sorted list of doctest file basenames (includes .py, .pyx, .pxi, .rst, .tex files).  Not a patch.",
    "created_at": "2010-08-13T01:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95222",
    "user": "mpatel"
}
```

Attachment [basenames_frequencies.txt](tarball://root/attachments/some-uuid/ticket9739/basenames_frequencies.txt) by mpatel created at 2010-08-13 01:39:09

Frequency-sorted list of doctest file basenames (includes .py, .pyx, .pxi, .rst, .tex files).  Not a patch.



---

archive/issue_comments_095223.json:
```json
{
    "body": "I've attached a list of ~1500 unique basenames for the ~2500 files we doctest (give or take a handful).",
    "created_at": "2010-08-13T01:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95223",
    "user": "mpatel"
}
```

I've attached a list of ~1500 unique basenames for the ~2500 files we doctest (give or take a handful).



---

archive/issue_comments_095224.json:
```json
{
    "body": "Doctest with unique temporary files.  Apply to scripts repo.",
    "created_at": "2010-09-04T06:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95224",
    "user": "mpatel"
}
```

Doctest with unique temporary files.  Apply to scripts repo.



---

archive/issue_comments_095225.json:
```json
{
    "body": "Attachment [trac_9739-unique_doctest_names.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739-unique_doctest_names.patch) by mpatel created at 2010-09-04 07:01:05\n\nI've attached a patch.  I haven't modified `sage-test`, since we're likely to phase it out at #9224.",
    "created_at": "2010-09-04T07:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95225",
    "user": "mpatel"
}
```

Attachment [trac_9739-unique_doctest_names.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739-unique_doctest_names.patch) by mpatel created at 2010-09-04 07:01:05

I've attached a patch.  I haven't modified `sage-test`, since we're likely to phase it out at #9224.



---

archive/issue_comments_095226.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-04T07:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95226",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095227.json:
```json
{
    "body": "Hmmm, I'm not sure if people will like substituting the filename with the whole test command everywhere. (I have a wide screen, but...)\n\nCan we please stop creating \"hidden\" doctest files? To me that doesn't make sense at all; especially but not limited to files in `~/.sage/*/`.\n\nDoes the *\"For whitespace errors, see ...\"* still work (i.e., print the correct filename)?\n\nThe notion of *\"absolute filenames relative to ...\"* is a bit weird... (But thanks for renaming `abs()`. :) )\n\nThe rest seems ok; I've yet only looked at the patch though.",
    "created_at": "2010-09-04T07:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95227",
    "user": "leif"
}
```

Hmmm, I'm not sure if people will like substituting the filename with the whole test command everywhere. (I have a wide screen, but...)

Can we please stop creating "hidden" doctest files? To me that doesn't make sense at all; especially but not limited to files in `~/.sage/*/`.

Does the *"For whitespace errors, see ..."* still work (i.e., print the correct filename)?

The notion of *"absolute filenames relative to ..."* is a bit weird... (But thanks for renaming `abs()`. :) )

The rest seems ok; I've yet only looked at the patch though.



---

archive/issue_comments_095228.json:
```json
{
    "body": "While printing the number of global and file iterations even if both are 1 isn't that useful, I'd like to see the current / appropriate timeout setting[s] printed in `sage-ptest` (i.e. `SAGE_TIMEOUT` for normal tests, and *only* `SAGE_TIMEOUT_LONG` when `-long` was given).\n\n(In principle, files containing no examples marked `# long time` should IMHO *not* be tested with `SAGE_TIMEOUT_LONG`, but the normal timeout. In that case we should print both timeout settings, and perhaps also indicate with which a file is being tested.)",
    "created_at": "2010-09-04T08:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95228",
    "user": "leif"
}
```

While printing the number of global and file iterations even if both are 1 isn't that useful, I'd like to see the current / appropriate timeout setting[s] printed in `sage-ptest` (i.e. `SAGE_TIMEOUT` for normal tests, and *only* `SAGE_TIMEOUT_LONG` when `-long` was given).

(In principle, files containing no examples marked `# long time` should IMHO *not* be tested with `SAGE_TIMEOUT_LONG`, but the normal timeout. In that case we should print both timeout settings, and perhaps also indicate with which a file is being tested.)



---

archive/issue_comments_095229.json:
```json
{
    "body": "Replying to [comment:5 leif]:\n> Hmmm, I'm not sure if people will like substituting the filename with the whole test command everywhere. (I have a wide screen, but...)\n\nOk, sorry, hard to read. The behavoir seems to be the same as before...",
    "created_at": "2010-09-04T08:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95229",
    "user": "leif"
}
```

Replying to [comment:5 leif]:
> Hmmm, I'm not sure if people will like substituting the filename with the whole test command everywhere. (I have a wide screen, but...)

Ok, sorry, hard to read. The behavoir seems to be the same as before...



---

archive/issue_comments_095230.json:
```json
{
    "body": "How should I best apply this:\n\n\n```\ndrkirkby@hawk:~/2/sage-4.5.3.alpha2$ cd local/bin\ndrkirkby@hawk:~/2/sage-4.5.3.alpha2/local/bin$ hg qimport  http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9739/trac_9739-unique_doctest_names.patch\nadding trac_9739-unique_doctest_names.patch to series file\ndrkirkby@hawk:~/2/sage-4.5.3.alpha2/local/bin$ hg push\nabort: repository /space/rlm/sage-4.1.rc1/local/bin not found!\n```\n\n\nSomething, somewhere seems to be looking for some directory of what I assume is Robert Millers. \n\nDave",
    "created_at": "2010-09-04T09:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95230",
    "user": "drkirkby"
}
```

How should I best apply this:


```
drkirkby@hawk:~/2/sage-4.5.3.alpha2$ cd local/bin
drkirkby@hawk:~/2/sage-4.5.3.alpha2/local/bin$ hg qimport  http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9739/trac_9739-unique_doctest_names.patch
adding trac_9739-unique_doctest_names.patch to series file
drkirkby@hawk:~/2/sage-4.5.3.alpha2/local/bin$ hg push
abort: repository /space/rlm/sage-4.1.rc1/local/bin not found!
```


Something, somewhere seems to be looking for some directory of what I assume is Robert Millers. 

Dave



---

archive/issue_comments_095231.json:
```json
{
    "body": "Replying to [comment:8 drkirkby]:\n> Something, somewhere seems to be looking for some directory of what I assume is Robert Millers. \n\nWhat happens if you (re)move `SAGE_LOCAL/bin/.hg/hgrc`?  The problem might be that when you're in `SAGE_LOCAL/bin`, you're invoking `./hg`, instead of `/usr/local/bin/hg`.",
    "created_at": "2010-09-04T09:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95231",
    "user": "mpatel"
}
```

Replying to [comment:8 drkirkby]:
> Something, somewhere seems to be looking for some directory of what I assume is Robert Millers. 

What happens if you (re)move `SAGE_LOCAL/bin/.hg/hgrc`?  The problem might be that when you're in `SAGE_LOCAL/bin`, you're invoking `./hg`, instead of `/usr/local/bin/hg`.



---

archive/issue_comments_095232.json:
```json
{
    "body": "Note that you don't want to create a race condition with two tests\ntrying to create the same directory at the same time. Perhaps mangling\n\"/\" -> \".\" would be sufficient.",
    "created_at": "2010-09-16T00:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95232",
    "user": "robertwb"
}
```

Note that you don't want to create a race condition with two tests
trying to create the same directory at the same time. Perhaps mangling
"/" -> "." would be sufficient.



---

archive/issue_comments_095233.json:
```json
{
    "body": "Replying to [comment:11 robertwb]:\n> Note that you don't want to create a race condition with two tests\n> trying to create the same directory at the same time. Perhaps mangling\n> \"/\" -> \".\" would be sufficient.\n\nThanks, Robert.  How about adding the process ID, too, or instead?  I'd also like to reduce the chance of races when we run multiple `sage -t(p)` commands simultaneously with the same `DOT_SAGE`.  Or are there other potential races under this directory, e.g., in `DOT_SAGE/gap`?",
    "created_at": "2010-10-02T21:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95233",
    "user": "mpatel"
}
```

Replying to [comment:11 robertwb]:
> Note that you don't want to create a race condition with two tests
> trying to create the same directory at the same time. Perhaps mangling
> "/" -> "." would be sufficient.

Thanks, Robert.  How about adding the process ID, too, or instead?  I'd also like to reduce the chance of races when we run multiple `sage -t(p)` commands simultaneously with the same `DOT_SAGE`.  Or are there other potential races under this directory, e.g., in `DOT_SAGE/gap`?



---

archive/issue_comments_095234.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-02T21:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95234",
    "user": "mpatel"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095235.json:
```json
{
    "body": "Has there been any more thoughts on this? \n\nI had a doctest failure today on my OpenSolaris machine *hawk*, which is almost certainly a result of this bug. This is using sage-4.6.rc0.\n\n\n```\nThe following tests failed:\n\n\tsage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/notebook/misc.py # 0 doctests failed\n\tsage -t  -long devel/sage/sage/plot/plot.py # 5 doctests failed\n```\n\n\nThe likely reason for the first of these failures can be seen if we look further up the log. \n\n\n```\nsage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/misc.py\n         [2.9 s]\nsage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/notebook/misc.py\npython: can't open file '/export/home/drkirkby/.sage//tmp/misc.py': [Errno 2] No such file or directory\n\n         [0.2 s]\n```\n\n\nThe log clearly shows a file `misc.py` being tested, followed by a second test with a different file also called `misc.py`. That file is then not found. It seems almost inevitable one test deleted the file needed by another test as they were both called `misc.py` and both tested around the same time. \n\nNote this is the same machine on which the buildbot passed all doctests. \n\nhttp://build.sagemath.org/sage/builders/hawk%20full/builds/8/steps/shell_6/logs/stdio\n\nso it seems to be an intermittent problem. (I've also had all tests pass on this). \n\nThese doctests issues are really annoying, as one never knows if its a real Sage bug, or a doctest bug. \n\nDave",
    "created_at": "2010-10-23T17:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95235",
    "user": "drkirkby"
}
```

Has there been any more thoughts on this? 

I had a doctest failure today on my OpenSolaris machine *hawk*, which is almost certainly a result of this bug. This is using sage-4.6.rc0.


```
The following tests failed:

	sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/notebook/misc.py # 0 doctests failed
	sage -t  -long devel/sage/sage/plot/plot.py # 5 doctests failed
```


The likely reason for the first of these failures can be seen if we look further up the log. 


```
sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/misc.py
         [2.9 s]
sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/notebook/misc.py
python: can't open file '/export/home/drkirkby/.sage//tmp/misc.py': [Errno 2] No such file or directory

         [0.2 s]
```


The log clearly shows a file `misc.py` being tested, followed by a second test with a different file also called `misc.py`. That file is then not found. It seems almost inevitable one test deleted the file needed by another test as they were both called `misc.py` and both tested around the same time. 

Note this is the same machine on which the buildbot passed all doctests. 

http://build.sagemath.org/sage/builders/hawk%20full/builds/8/steps/shell_6/logs/stdio

so it seems to be an intermittent problem. (I've also had all tests pass on this). 

These doctests issues are really annoying, as one never knows if its a real Sage bug, or a doctest bug. 

Dave



---

archive/issue_comments_095236.json:
```json
{
    "body": "I'm planning to return to this soon, probably after 4.6 is out.",
    "created_at": "2010-10-23T21:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95236",
    "user": "mpatel"
}
```

I'm planning to return to this soon, probably after 4.6 is out.



---

archive/issue_comments_095237.json:
```json
{
    "body": "Replying to [comment:16 mpatel]:\n> I'm planning to return to this soon, probably after 4.6 is out.\nThat would be great, because I have also hit this error quite a few times.",
    "created_at": "2010-10-24T08:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95237",
    "user": "jdemeyer"
}
```

Replying to [comment:16 mpatel]:
> I'm planning to return to this soon, probably after 4.6 is out.
That would be great, because I have also hit this error quite a few times.



---

archive/issue_comments_095238.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-10-25T08:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95238",
    "user": "jdemeyer"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_095239.json:
```json
{
    "body": "Changing keywords from \"\" to \"doctest scripts\".",
    "created_at": "2010-10-25T08:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95239",
    "user": "jdemeyer"
}
```

Changing keywords from "" to "doctest scripts".



---

archive/issue_comments_095240.json:
```json
{
    "body": "There is another problem, which could exist even if every file had a different name. \n\nIf one tests multiple instances of Sage serially, then since they both write to $HOME/.sage, failures can occur even if the file names of the doctests are unique to any one copy of Sage. They need to be unique for any number of instances of Sage. I think testing under $HOME/.sage is a bit silly myself - it would be better to test under the directory where Sage is installed. \n\nI found that testing `devel/sage/sage/libs/fplll/fplll.pyx` (see #10195), would generate problems when I was testing two copies of Sage at the same time (slightly different versions). I don't know if this patch can handle that situation, but it would be good if it could. \n\nDave",
    "created_at": "2010-10-31T13:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95240",
    "user": "drkirkby"
}
```

There is another problem, which could exist even if every file had a different name. 

If one tests multiple instances of Sage serially, then since they both write to $HOME/.sage, failures can occur even if the file names of the doctests are unique to any one copy of Sage. They need to be unique for any number of instances of Sage. I think testing under $HOME/.sage is a bit silly myself - it would be better to test under the directory where Sage is installed. 

I found that testing `devel/sage/sage/libs/fplll/fplll.pyx` (see #10195), would generate problems when I was testing two copies of Sage at the same time (slightly different versions). I don't know if this patch can handle that situation, but it would be good if it could. 

Dave



---

archive/issue_comments_095241.json:
```json
{
    "body": "Replying to [comment:19 drkirkby]:\n> There is another problem, which could exist even if every file had a different name. \n> \n> If one tests multiple instances of Sage serially, then since they both write to $HOME/.sage, failures can occur even if the file names of the doctests are unique to any one copy of Sage.\n\nWell this would definitely be a **user error**. You can always set `DOT_SAGE` or `SAGE_TESTDIR` (or whatever it is called) if you want to run multiple tests simultaneously in different shells, even in / with the *same* Sage installation.\n\n> They need to be unique for any number of instances of Sage. I think testing under $HOME/.sage is a bit silly myself - it would be better to test under the directory where Sage is installed.\n\nDefinitely not, since this wouldn't work for site installations, where users usually have no write permissions under `SAGE_ROOT`.\n\n\n> I don't know if this patch can handle that situation, but it would be good if it could.\n\nOne could use Sage's PID, user and machine parameters etc. to try to create unique directories, or generally create \"random\" directories with `mktemp (1)` or `mkdtemp()`, but I think this would be an overkill, since the user can itself do such by setting one of the above variables.",
    "created_at": "2010-10-31T13:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95241",
    "user": "leif"
}
```

Replying to [comment:19 drkirkby]:
> There is another problem, which could exist even if every file had a different name. 
> 
> If one tests multiple instances of Sage serially, then since they both write to $HOME/.sage, failures can occur even if the file names of the doctests are unique to any one copy of Sage.

Well this would definitely be a **user error**. You can always set `DOT_SAGE` or `SAGE_TESTDIR` (or whatever it is called) if you want to run multiple tests simultaneously in different shells, even in / with the *same* Sage installation.

> They need to be unique for any number of instances of Sage. I think testing under $HOME/.sage is a bit silly myself - it would be better to test under the directory where Sage is installed.

Definitely not, since this wouldn't work for site installations, where users usually have no write permissions under `SAGE_ROOT`.


> I don't know if this patch can handle that situation, but it would be good if it could.

One could use Sage's PID, user and machine parameters etc. to try to create unique directories, or generally create "random" directories with `mktemp (1)` or `mkdtemp()`, but I think this would be an overkill, since the user can itself do such by setting one of the above variables.



---

archive/issue_comments_095242.json:
```json
{
    "body": "Replying to [comment:20 leif]:\n> Replying to [comment:19 drkirkby]:\n> > There is another problem, which could exist even if every file had a different name. \n> > \n> > If one tests multiple instances of Sage serially, then since they both write to $HOME/.sage, failures can occur even if the file names of the doctests are unique to any one copy of Sage.\n> \n> Well this would definitely be a **user error**. You can always set `DOT_SAGE` or `SAGE_TESTDIR` (or whatever it is called) if you want to run multiple tests simultaneously in different shells, even in / with the *same* Sage installation.\n> \n> > They need to be unique for any number of instances of Sage. I think testing under $HOME/.sage is a bit silly myself - it would be better to test under the directory where Sage is installed.\n> \n> Definitely not, since this wouldn't work for site installations, where users usually have no write permissions under `SAGE_ROOT`.\n> \n> \n> > I don't know if this patch can handle that situation, but it would be good if it could.\n> \n> One could use Sage's PID, user and machine parameters etc. to try to create unique directories, or generally create \"random\" directories with `mktemp (1)` or `mkdtemp()`, but I think this would be an overkill, since the user can itself do such by setting one of the above variables.\n\nI disagree. I don't think creating unique temporary files is overkill. It would be far less error prone. With a test you want to run many times, having a dozen copies of Sage around for test purposes is quite a sensible thing to do with multi-core machines. Havving to set DOT_SAGE for each is annoying, when a unique temporary file could be made. \n\nDave",
    "created_at": "2010-10-31T19:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95242",
    "user": "drkirkby"
}
```

Replying to [comment:20 leif]:
> Replying to [comment:19 drkirkby]:
> > There is another problem, which could exist even if every file had a different name. 
> > 
> > If one tests multiple instances of Sage serially, then since they both write to $HOME/.sage, failures can occur even if the file names of the doctests are unique to any one copy of Sage.
> 
> Well this would definitely be a **user error**. You can always set `DOT_SAGE` or `SAGE_TESTDIR` (or whatever it is called) if you want to run multiple tests simultaneously in different shells, even in / with the *same* Sage installation.
> 
> > They need to be unique for any number of instances of Sage. I think testing under $HOME/.sage is a bit silly myself - it would be better to test under the directory where Sage is installed.
> 
> Definitely not, since this wouldn't work for site installations, where users usually have no write permissions under `SAGE_ROOT`.
> 
> 
> > I don't know if this patch can handle that situation, but it would be good if it could.
> 
> One could use Sage's PID, user and machine parameters etc. to try to create unique directories, or generally create "random" directories with `mktemp (1)` or `mkdtemp()`, but I think this would be an overkill, since the user can itself do such by setting one of the above variables.

I disagree. I don't think creating unique temporary files is overkill. It would be far less error prone. With a test you want to run many times, having a dozen copies of Sage around for test purposes is quite a sensible thing to do with multi-core machines. Havving to set DOT_SAGE for each is annoying, when a unique temporary file could be made. 

Dave



---

archive/issue_comments_095243.json:
```json
{
    "body": "Replying to [comment:21 drkirkby]:\n> I disagree. I don't think creating unique temporary files is overkill. \n\nI didn't say that, but it IMHO suffices to have unique names in the namespace of a ptest run.\n\n\n> It would be far less error prone. With a test you want to run many times, having a dozen copies of Sage around for test purposes is quite a sensible thing to do with multi-core machines. Havving to set DOT_SAGE for each is annoying, when a unique temporary file could be made.\n\nAs I said, you can automatically set up unique test directories by setting one of the above variables e.g. based on the \"login\" shell's PID, one per terminal / shell.\n\nIf multiple machines share the same filesystem, simply add e.g. the hostname, too.",
    "created_at": "2010-10-31T20:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95243",
    "user": "leif"
}
```

Replying to [comment:21 drkirkby]:
> I disagree. I don't think creating unique temporary files is overkill. 

I didn't say that, but it IMHO suffices to have unique names in the namespace of a ptest run.


> It would be far less error prone. With a test you want to run many times, having a dozen copies of Sage around for test purposes is quite a sensible thing to do with multi-core machines. Havving to set DOT_SAGE for each is annoying, when a unique temporary file could be made.

As I said, you can automatically set up unique test directories by setting one of the above variables e.g. based on the "login" shell's PID, one per terminal / shell.

If multiple machines share the same filesystem, simply add e.g. the hostname, too.



---

archive/issue_comments_095244.json:
```json
{
    "body": "+1 to temp (per instance) directories. They would get cleaned up properly, and /tmp is almost always fast and local which is another plus. \n\n(Really, we shouldn't have to be writing these files out at all...)",
    "created_at": "2010-11-02T02:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95244",
    "user": "robertwb"
}
```

+1 to temp (per instance) directories. They would get cleaned up properly, and /tmp is almost always fast and local which is another plus. 

(Really, we shouldn't have to be writing these files out at all...)



---

archive/issue_comments_095245.json:
```json
{
    "body": "Replying to [comment:23 robertwb]:\n> +1 to temp (per instance) directories. They would get cleaned up properly, and /tmp is almost always fast and local which is another plus. \n> \n> (Really, we shouldn't have to be writing these files out at all...)\n\nI'm not sure if you are agreeing with me or Leif there Robert - perhaps you can clarify. \n\nI was going to suggest that we should be using /tmp, but I did not since I can see a disadvantage of it. NFS file systems have caused problems with doc tests failing, especially if they are mis-configured. As such, it would be better if a user tested Sage on the file system where it will be used. By using /tmp they might get a false sense of security. That said, using /tmp for temporary files has been the norm for years. \n\nI personally think where reasonably practical, we should stop multiple instances of running Sage tests interfering with each other. Although Leif considers this a user error, it is one that a user might easily make. \n\nBut if it possible to avoid creating temporary files, then that should be done. But I would imagine that requires more changes than just adding a pid or hostname. \n\nDave",
    "created_at": "2010-11-02T08:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95245",
    "user": "drkirkby"
}
```

Replying to [comment:23 robertwb]:
> +1 to temp (per instance) directories. They would get cleaned up properly, and /tmp is almost always fast and local which is another plus. 
> 
> (Really, we shouldn't have to be writing these files out at all...)

I'm not sure if you are agreeing with me or Leif there Robert - perhaps you can clarify. 

I was going to suggest that we should be using /tmp, but I did not since I can see a disadvantage of it. NFS file systems have caused problems with doc tests failing, especially if they are mis-configured. As such, it would be better if a user tested Sage on the file system where it will be used. By using /tmp they might get a false sense of security. That said, using /tmp for temporary files has been the norm for years. 

I personally think where reasonably practical, we should stop multiple instances of running Sage tests interfering with each other. Although Leif considers this a user error, it is one that a user might easily make. 

But if it possible to avoid creating temporary files, then that should be done. But I would imagine that requires more changes than just adding a pid or hostname. 

Dave



---

archive/issue_comments_095246.json:
```json
{
    "body": "OT: My `make ptestlong` of Sage 4.6 on Ubuntu 9.04 x86 somehow went into an infinite loop...\n\nThis never happened before (in dozens of builds), any idea?\n\n(I started the complete build with `make ptestlong`, build succeeded and building the documentation went normal, but now I'm meanwhile at the tenth doctest run! Checked this with `grep Doctesting ptestlong.log`.)",
    "created_at": "2010-11-03T02:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95246",
    "user": "leif"
}
```

OT: My `make ptestlong` of Sage 4.6 on Ubuntu 9.04 x86 somehow went into an infinite loop...

This never happened before (in dozens of builds), any idea?

(I started the complete build with `make ptestlong`, build succeeded and building the documentation went normal, but now I'm meanwhile at the tenth doctest run! Checked this with `grep Doctesting ptestlong.log`.)



---

archive/issue_comments_095247.json:
```json
{
    "body": "Replying to [comment:24 drkirkby]:\n> Replying to [comment:23 robertwb]:\n> > +1 to temp (per instance) directories. They would get cleaned up properly, and /tmp is almost always fast and local which is another plus. \n> > \n> > (Really, we shouldn't have to be writing these files out at all...)\n> \n> I'm not sure if you are agreeing with me or Leif there Robert - perhaps you can clarify. \n\nAgreeing with drkirkby, we should use temp directories. \n\n> I was going to suggest that we should be using /tmp, but I did not since I can see a disadvantage of it. NFS file systems have caused problems with doc tests failing, especially if they are mis-configured. As such, it would be better if a user tested Sage on the file system where it will be used. By using /tmp they might get a false sense of security. That said, using /tmp for temporary files has been the norm for years. \n\nDon't know if mktemp is POSIX, but it's widely available. Of course from Python you always have http://docs.python.org/library/tempfile.html Both are much better than manually specifying /tmp. \n\n> I personally think where reasonably practical, we should stop multiple instances of running Sage tests interfering with each other. Although Leif considers this a user error, it is one that a user might easily make. \n\nI don't consider it a user error, and I also don't like filling .sage with lots of junk. \n\n> But if it possible to avoid creating temporary files, then that should be done. But I would imagine that requires more changes than just adding a pid or hostname. \n\nTrue, and this ticket has been opened for far too long. \n\n- Robert",
    "created_at": "2010-11-03T08:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95247",
    "user": "robertwb"
}
```

Replying to [comment:24 drkirkby]:
> Replying to [comment:23 robertwb]:
> > +1 to temp (per instance) directories. They would get cleaned up properly, and /tmp is almost always fast and local which is another plus. 
> > 
> > (Really, we shouldn't have to be writing these files out at all...)
> 
> I'm not sure if you are agreeing with me or Leif there Robert - perhaps you can clarify. 

Agreeing with drkirkby, we should use temp directories. 

> I was going to suggest that we should be using /tmp, but I did not since I can see a disadvantage of it. NFS file systems have caused problems with doc tests failing, especially if they are mis-configured. As such, it would be better if a user tested Sage on the file system where it will be used. By using /tmp they might get a false sense of security. That said, using /tmp for temporary files has been the norm for years. 

Don't know if mktemp is POSIX, but it's widely available. Of course from Python you always have http://docs.python.org/library/tempfile.html Both are much better than manually specifying /tmp. 

> I personally think where reasonably practical, we should stop multiple instances of running Sage tests interfering with each other. Although Leif considers this a user error, it is one that a user might easily make. 

I don't consider it a user error, and I also don't like filling .sage with lots of junk. 

> But if it possible to avoid creating temporary files, then that should be done. But I would imagine that requires more changes than just adding a pid or hostname. 

True, and this ticket has been opened for far too long. 

- Robert



---

archive/issue_comments_095248.json:
```json
{
    "body": "Replying to [comment:25 leif]:\n> OT: My `make ptestlong` of Sage 4.6 on Ubuntu 9.04 x86 somehow went into an infinite loop...\n> \n> This never happened before (in dozens of builds), any idea?\n> \n> (I started the complete build with `make ptestlong`, build succeeded and building the documentation went normal, but now I'm meanwhile at the tenth doctest run! Checked this with `grep Doctesting ptestlong.log`.)\n> \n\nOuch. I just noticed I had set `SAGE_TEST_GLOBAL_ITER=1000` earlier in that shell...\n\n(But all tests passed; I then aborted it during the 14th run.)",
    "created_at": "2010-11-03T18:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95248",
    "user": "leif"
}
```

Replying to [comment:25 leif]:
> OT: My `make ptestlong` of Sage 4.6 on Ubuntu 9.04 x86 somehow went into an infinite loop...
> 
> This never happened before (in dozens of builds), any idea?
> 
> (I started the complete build with `make ptestlong`, build succeeded and building the documentation went normal, but now I'm meanwhile at the tenth doctest run! Checked this with `grep Doctesting ptestlong.log`.)
> 

Ouch. I just noticed I had set `SAGE_TEST_GLOBAL_ITER=1000` earlier in that shell...

(But all tests passed; I then aborted it during the 14th run.)



---

archive/issue_comments_095249.json:
```json
{
    "body": "What is the current status of this patch, do you consider it ready for review?  If not, I'm willing to join in and help where needed.",
    "created_at": "2010-11-07T10:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95249",
    "user": "jdemeyer"
}
```

What is the current status of this patch, do you consider it ready for review?  If not, I'm willing to join in and help where needed.



---

archive/issue_comments_095250.json:
```json
{
    "body": "Replying to [comment:28 jdemeyer]:\n> What is the current status of this patch, do you consider it ready for review?  If not, I'm willing to join in and help where needed.\n\nIt's not ready for review.  I don't think I have the time to work on this in the next several days, so if you'd like to help, please do!\n\nI think we can make a temporary directory for each run in `sage-(p)test` and pass it to `sage-doctest`, which should ensure the temporary files under the directory are unique.  The existing doesn't quite yet do the latter, but it should be easy to modify it so it does (e.g., with full paths and/or pids, etc.).",
    "created_at": "2010-11-07T23:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95250",
    "user": "mpatel"
}
```

Replying to [comment:28 jdemeyer]:
> What is the current status of this patch, do you consider it ready for review?  If not, I'm willing to join in and help where needed.

It's not ready for review.  I don't think I have the time to work on this in the next several days, so if you'd like to help, please do!

I think we can make a temporary directory for each run in `sage-(p)test` and pass it to `sage-doctest`, which should ensure the temporary files under the directory are unique.  The existing doesn't quite yet do the latter, but it should be easy to modify it so it does (e.g., with full paths and/or pids, etc.).



---

archive/issue_comments_095251.json:
```json
{
    "body": "Using both a hostname and a PID should mean the filename is practically unique if people test on more than one computer using a shared drive. I don't think 'mktemp' will be unique on NFS shared drives, though the probability of a collision would then be very small indeed. But adding a hostname would reduce it even further. \n\nBut we need to be careful if using mktemp. Whilst many systems have it, the implementation is not the same on every system. I know Solaris works a bit different to Linux or OS X (I forget which). I know using something on Solaris with mktemp which would not work with Linux or OS X. (I forget which OS it was though). It seems HP-UX and Solaris differ too. \n\nI would be very keen to use something that will work on AIX. There is a chance of IBM donating a quad core 4.5 GHz machine to the Sage project with AIX on it. \n\nAnyway, whatever solution is used, I think it will be 1000x better than the current solution, but personally I'd like to see something that's unique to a machine and portable. \n\nDave",
    "created_at": "2010-11-08T00:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95251",
    "user": "drkirkby"
}
```

Using both a hostname and a PID should mean the filename is practically unique if people test on more than one computer using a shared drive. I don't think 'mktemp' will be unique on NFS shared drives, though the probability of a collision would then be very small indeed. But adding a hostname would reduce it even further. 

But we need to be careful if using mktemp. Whilst many systems have it, the implementation is not the same on every system. I know Solaris works a bit different to Linux or OS X (I forget which). I know using something on Solaris with mktemp which would not work with Linux or OS X. (I forget which OS it was though). It seems HP-UX and Solaris differ too. 

I would be very keen to use something that will work on AIX. There is a chance of IBM donating a quad core 4.5 GHz machine to the Sage project with AIX on it. 

Anyway, whatever solution is used, I think it will be 1000x better than the current solution, but personally I'd like to see something that's unique to a machine and portable. 

Dave



---

archive/issue_comments_095252.json:
```json
{
    "body": "I'm still interested in working on this patch, but I don't expect it to be ready on time for 4.6.1.",
    "created_at": "2010-12-02T15:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95252",
    "user": "jdemeyer"
}
```

I'm still interested in working on this patch, but I don't expect it to be ready on time for 4.6.1.



---

archive/issue_comments_095253.json:
```json
{
    "body": "While we are at it, I have some more comments on `sage-ptest` I'll also post here with an inline patch:\n\n\n```diff\ndiff --git a/sage-ptest b/sage-ptest\n--- a/sage-ptest\n+++ b/sage-ptest\n@@ -81,12 +81,18 @@\n     Returns true if the file should not be tested\n     \"\"\"\n     if not os.path.exists(F):\n+        # XXX IMHO this should never happen; in case it does, it's certainly\n+        #     an error to be reported (either filesystem, or bad name specified\n+        #     on the command line). -leif\n         return True\n     G = abspath(F)\n     i = G.rfind(os.path.sep)\n+    # XXX The following should IMHO be performed in populatefilelist():\n+    #     (Currently, populatefilelist() only looks for \"__nodoctest__\".)\n     if os.path.exists(os.path.join(G[:i], 'nodoctest.py')):\n         printmutex.acquire()\n         print \"%s (skipping) -- nodoctest.py file in directory\"%abs(F)\n+        sys.stdout.flush()\n         printmutex.release()\n         return True\n     filenm = os.path.split(F)[1]\n@@ -95,6 +101,7 @@\n         return True\n     if G.find(os.path.join('doc', 'output')) != -1:\n         return True\n+    # XXX The following is (also/already) handled in populatefilelist():\n     if not (os.path.splitext(F)[1] in ['.py', '.pyx', '.tex', '.pxi', '.sage', '.rst']):\n         return True\n     return False\n@@ -115,6 +122,7 @@\n     for i in range(0,numiteration):\n         os.chdir(os.path.dirname(F))\n         command = os.path.join(SAGE_ROOT, 'local', 'bin', 'sage-%s' % cmd)\n+        # FIXME: Why call bash here? (Also, we use 'shell=True' below anyway.)\n         s = 'bash -c \"%s %s > %s\" ' % (command, filestr, outfile.name)\n         try:\n             t = time.time()\n@@ -161,10 +169,12 @@\n         print sage_test_cmd(F[len(CUR)+1:])\n     else:\n         print abs(F)\n+    sys.stdout.flush()\n     if ol!=\"\" and (not ol.isspace()):\n         if (ol[len(ol)-1]==\"\\n\"):\n             ol=ol[0:len(ol)-1]\n         print ol\n+        sys.stdout.flush()\n     time_dict[abs_sage_path(F)] = finished_time\n     if XML_RESULTS:\n         t = finished_time\n@@ -192,6 +202,7 @@\n         \"\"\".strip() % locals())\n         f.close()\n     print \"\\t [%.1f s]\"%(finished_time)\n+    sys.stdout.flush()\n \n def infiles_cmp(a,b):\n     \"\"\"\n@@ -231,7 +242,14 @@\n                 base, ext = os.path.splitext(F)\n                 if not (ext in ['.sage', '.py', '.pyx', '.tex', '.pxi', '.rst']):\n                     continue\n-                elif '__nodoctest__' in files:\n+                elif '__nodoctest__' in files: # XXX Shouldn't this be 'lfiles'?\n+                    # Also, this test should IMHO be in the outer loop (1 level).\n+                    # Furthermore, the current practice is to put \"nodoctest.py\"\n+                    # files in the directories that should be skipped, not\n+                    # \"__nodoctest__\". (I haven't found a single instance of the\n+                    # latter in Sage 4.6.1.alpha3.)\n+                    # \"nodoctest.py\" is handled in skip() (!), to also be fixed.\n+                    # -leif\n                     continue\n                 appendstr = os.path.join(root,F)\n                 if skip(appendstr):\n@@ -252,6 +270,9 @@\n     argv = [X for X in argv if X[0] != '-']\n \n     try: \n+        # FIXME: Nice, but <NUMTHREADS> should immediately follow '-tp' etc.,\n+        #        i.e., be the next argument. We might have file or directory\n+        #        names that properly convert to an int...\n         numthreads = int(argv[1])\n         infiles = argv[2:]\n     except ValueError: # can't convert first arg to an integer: arg was probably omitted\n```\n\n(This is against Sage 4.6.1.alpha3.)\n\nThe comments all refer to inconsistencies; the only actual change is flushing the output since it currently comes in bursts, which is IMHO odd for watching it. I don't think this measurably slows down doctesting...",
    "created_at": "2010-12-16T02:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95253",
    "user": "leif"
}
```

While we are at it, I have some more comments on `sage-ptest` I'll also post here with an inline patch:


```diff
diff --git a/sage-ptest b/sage-ptest
--- a/sage-ptest
+++ b/sage-ptest
@@ -81,12 +81,18 @@
     Returns true if the file should not be tested
     """
     if not os.path.exists(F):
+        # XXX IMHO this should never happen; in case it does, it's certainly
+        #     an error to be reported (either filesystem, or bad name specified
+        #     on the command line). -leif
         return True
     G = abspath(F)
     i = G.rfind(os.path.sep)
+    # XXX The following should IMHO be performed in populatefilelist():
+    #     (Currently, populatefilelist() only looks for "__nodoctest__".)
     if os.path.exists(os.path.join(G[:i], 'nodoctest.py')):
         printmutex.acquire()
         print "%s (skipping) -- nodoctest.py file in directory"%abs(F)
+        sys.stdout.flush()
         printmutex.release()
         return True
     filenm = os.path.split(F)[1]
@@ -95,6 +101,7 @@
         return True
     if G.find(os.path.join('doc', 'output')) != -1:
         return True
+    # XXX The following is (also/already) handled in populatefilelist():
     if not (os.path.splitext(F)[1] in ['.py', '.pyx', '.tex', '.pxi', '.sage', '.rst']):
         return True
     return False
@@ -115,6 +122,7 @@
     for i in range(0,numiteration):
         os.chdir(os.path.dirname(F))
         command = os.path.join(SAGE_ROOT, 'local', 'bin', 'sage-%s' % cmd)
+        # FIXME: Why call bash here? (Also, we use 'shell=True' below anyway.)
         s = 'bash -c "%s %s > %s" ' % (command, filestr, outfile.name)
         try:
             t = time.time()
@@ -161,10 +169,12 @@
         print sage_test_cmd(F[len(CUR)+1:])
     else:
         print abs(F)
+    sys.stdout.flush()
     if ol!="" and (not ol.isspace()):
         if (ol[len(ol)-1]=="\n"):
             ol=ol[0:len(ol)-1]
         print ol
+        sys.stdout.flush()
     time_dict[abs_sage_path(F)] = finished_time
     if XML_RESULTS:
         t = finished_time
@@ -192,6 +202,7 @@
         """.strip() % locals())
         f.close()
     print "\t [%.1f s]"%(finished_time)
+    sys.stdout.flush()
 
 def infiles_cmp(a,b):
     """
@@ -231,7 +242,14 @@
                 base, ext = os.path.splitext(F)
                 if not (ext in ['.sage', '.py', '.pyx', '.tex', '.pxi', '.rst']):
                     continue
-                elif '__nodoctest__' in files:
+                elif '__nodoctest__' in files: # XXX Shouldn't this be 'lfiles'?
+                    # Also, this test should IMHO be in the outer loop (1 level).
+                    # Furthermore, the current practice is to put "nodoctest.py"
+                    # files in the directories that should be skipped, not
+                    # "__nodoctest__". (I haven't found a single instance of the
+                    # latter in Sage 4.6.1.alpha3.)
+                    # "nodoctest.py" is handled in skip() (!), to also be fixed.
+                    # -leif
                     continue
                 appendstr = os.path.join(root,F)
                 if skip(appendstr):
@@ -252,6 +270,9 @@
     argv = [X for X in argv if X[0] != '-']
 
     try: 
+        # FIXME: Nice, but <NUMTHREADS> should immediately follow '-tp' etc.,
+        #        i.e., be the next argument. We might have file or directory
+        #        names that properly convert to an int...
         numthreads = int(argv[1])
         infiles = argv[2:]
     except ValueError: # can't convert first arg to an integer: arg was probably omitted
```

(This is against Sage 4.6.1.alpha3.)

The comments all refer to inconsistencies; the only actual change is flushing the output since it currently comes in bursts, which is IMHO odd for watching it. I don't think this measurably slows down doctesting...



---

archive/issue_comments_095254.json:
```json
{
    "body": "Just for the record:\n\n#10458 also patches `sage-ptest` to support IPython/Sage-style line continuations in doctests (\"`....: `\" rather than only \"`...`\").",
    "created_at": "2010-12-16T03:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95254",
    "user": "leif"
}
```

Just for the record:

#10458 also patches `sage-ptest` to support IPython/Sage-style line continuations in doctests ("`....: `" rather than only "`...`").



---

archive/issue_comments_095255.json:
```json
{
    "body": "Replying to [comment:33 leif]:\n> Just for the record:\n> \n> #10458 also patches `sage-ptest` to support IPython/Sage-style line continuations in doctests (\"`....: `\" rather than only \"`...`\").\n\nOoops, sorry, #10458 patches `sage-doctest`, **not** `sage-ptest`.",
    "created_at": "2010-12-16T03:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95255",
    "user": "leif"
}
```

Replying to [comment:33 leif]:
> Just for the record:
> 
> #10458 also patches `sage-ptest` to support IPython/Sage-style line continuations in doctests ("`....: `" rather than only "`...`").

Ooops, sorry, #10458 patches `sage-doctest`, **not** `sage-ptest`.



---

archive/issue_comments_095256.json:
```json
{
    "body": "Changing type from defect to task.",
    "created_at": "2011-01-27T21:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95256",
    "user": "forextrading11"
}
```

Changing type from defect to task.



---

archive/issue_comments_095257.json:
```json
{
    "body": "Replying to [ticket:9739 mpatel]:\n> When we test\n> \n> `/path/to/foo.py`\n> \n> `sage-doctest` writes\n> \n> `SAGE_TESTDIR/.doctest_foo.py`\n> \n> runs the new file through `python`, and deletes it.  This can cause\n> collisions when we test in parallel multiple files with the same\n> basename, e.g., `__init__`, `all`, `misc`, `conf`, `constructor`, `morphism`, `index`, `tests`, `homset`, `element`, `twist`, `tutorial`, `sagetex`, `crystals`, `cartesian_product`, `template`, `ring`, etc.\n> \n> There's a similar problem with testing non-library files, which `sage-doctest` first effectively copies to `SAGE_TESTDIR`.\n> \n> See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/367bfc0d83c0e9b8#367bfc0d83c0e9b8) for background.\n> \n> This ticket may help with some of the doctesting problems discussed on the Sage mailing lists.  Related tickets: #9224, #9225, #9449.",
    "created_at": "2011-01-27T21:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95257",
    "user": "forextrading11"
}
```

Replying to [ticket:9739 mpatel]:
> When we test
> 
> `/path/to/foo.py`
> 
> `sage-doctest` writes
> 
> `SAGE_TESTDIR/.doctest_foo.py`
> 
> runs the new file through `python`, and deletes it.  This can cause
> collisions when we test in parallel multiple files with the same
> basename, e.g., `__init__`, `all`, `misc`, `conf`, `constructor`, `morphism`, `index`, `tests`, `homset`, `element`, `twist`, `tutorial`, `sagetex`, `crystals`, `cartesian_product`, `template`, `ring`, etc.
> 
> There's a similar problem with testing non-library files, which `sage-doctest` first effectively copies to `SAGE_TESTDIR`.
> 
> See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/367bfc0d83c0e9b8#367bfc0d83c0e9b8) for background.
> 
> This ticket may help with some of the doctesting problems discussed on the Sage mailing lists.  Related tickets: #9224, #9225, #9449.



---

archive/issue_comments_095258.json:
```json
{
    "body": "Changing keywords from \"doctest scripts\" to \"currency trading, forex analysis, forex trading, online forex trading\".",
    "created_at": "2011-01-27T21:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95258",
    "user": "forextrading11"
}
```

Changing keywords from "doctest scripts" to "currency trading, forex analysis, forex trading, online forex trading".



---

archive/issue_comments_095259.json:
```json
{
    "body": "Changing priority from blocker to trivial.",
    "created_at": "2011-01-27T21:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95259",
    "user": "forextrading11"
}
```

Changing priority from blocker to trivial.



---

archive/issue_comments_095260.json:
```json
{
    "body": "Changing component from doctest to build.",
    "created_at": "2011-01-27T21:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95260",
    "user": "forextrading11"
}
```

Changing component from doctest to build.



---

archive/issue_comments_095261.json:
```json
{
    "body": "Changing type from task to defect.",
    "created_at": "2011-01-28T06:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95261",
    "user": "jason"
}
```

Changing type from task to defect.



---

archive/issue_comments_095262.json:
```json
{
    "body": "Changing keywords from \"currency trading, forex analysis, forex trading, online forex trading\" to \"doctest scripts\".",
    "created_at": "2011-01-28T06:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95262",
    "user": "jason"
}
```

Changing keywords from "currency trading, forex analysis, forex trading, online forex trading" to "doctest scripts".



---

archive/issue_comments_095263.json:
```json
{
    "body": "Changing priority from trivial to blocker.",
    "created_at": "2011-01-28T06:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95263",
    "user": "jason"
}
```

Changing priority from trivial to blocker.



---

archive/issue_comments_095264.json:
```json
{
    "body": "Changing component from build to doctest.",
    "created_at": "2011-01-28T06:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95264",
    "user": "jason"
}
```

Changing component from build to doctest.



---

archive/issue_comments_095265.json:
```json
{
    "body": "Please ban forextrading11 for spam.",
    "created_at": "2011-01-28T06:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95265",
    "user": "jason"
}
```

Please ban forextrading11 for spam.



---

archive/issue_comments_095266.json:
```json
{
    "body": "Replying to [comment:37 jason]:\n> Please ban forextrading11 for spam.\n\nDone.",
    "created_at": "2011-01-28T07:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95266",
    "user": "mvngu"
}
```

Replying to [comment:37 jason]:
> Please ban forextrading11 for spam.

Done.



---

archive/issue_comments_095267.json:
```json
{
    "body": "Replying to [comment:39 jdemeyer]:\n\nThis is marked as a blocker for 4.7. but there's been no work on it for 8 weeks. \n\nDave",
    "created_at": "2011-04-07T21:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95267",
    "user": "drkirkby"
}
```

Replying to [comment:39 jdemeyer]:

This is marked as a blocker for 4.7. but there's been no work on it for 8 weeks. 

Dave



---

archive/issue_comments_095268.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2011-04-18T08:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95268",
    "user": "jdemeyer"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_095269.json:
```json
{
    "body": "To me it would -- at least for the moment, or this ticket -- be totally sufficient to have unique filenames by mangling the relative path into the temporary filename.\n\nIf someone wants to test multiple Sage installations at the same time, he can simply set `SAGE_TESTDIR` to different locations in each shell.\n\nDoctesting in (or below) `$DOT_SAGE` (which is usually `$HOME/.sage/`) is IMHO a bad idea anyway, not only because `/tmp/` is much more likely to be [on] a local filesystem than `/home/`. (It is usually also faster and auto-cleaned.) Creating a unique temporary directory there shouldn't be a problem.\n\nFor the sake of *\"For whitespace errors see ...\"*, failing files could still be copied elsewhere (to a perhaps more persistent location) at the end of the doctest process.",
    "created_at": "2011-07-27T12:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95269",
    "user": "leif"
}
```

To me it would -- at least for the moment, or this ticket -- be totally sufficient to have unique filenames by mangling the relative path into the temporary filename.

If someone wants to test multiple Sage installations at the same time, he can simply set `SAGE_TESTDIR` to different locations in each shell.

Doctesting in (or below) `$DOT_SAGE` (which is usually `$HOME/.sage/`) is IMHO a bad idea anyway, not only because `/tmp/` is much more likely to be [on] a local filesystem than `/home/`. (It is usually also faster and auto-cleaned.) Creating a unique temporary directory there shouldn't be a problem.

For the sake of *"For whitespace errors see ..."*, failing files could still be copied elsewhere (to a perhaps more persistent location) at the end of the doctest process.



---

archive/issue_comments_095270.json:
```json
{
    "body": "I've restored the original description the spammer deleted.",
    "created_at": "2011-07-27T13:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95270",
    "user": "leif"
}
```

I've restored the original description the spammer deleted.



---

archive/issue_comments_095271.json:
```json
{
    "body": "For the record, we already have the following in `sage/misc/misc.py`:\n\n\n```python\n...\nHOSTNAME = socket.gethostname().replace('-','_').replace('/','_').replace('\\\\','_')\n\nLOCAL_IDENTIFIER = '%s.%s'%(HOSTNAME , os.getpid())\n...\ntry:\n    DOT_SAGE = os.environ['DOT_SAGE']\nexcept KeyError:\n    try:\n        DOT_SAGE = '%s/.sage/'%os.environ['HOME']\n    except KeyError:\n        DOT_SAGE = '%s/.sage/'%SAGE_ROOT\n...\nif not os.path.exists(DOT_SAGE):\n    os.makedirs(DOT_SAGE)\n\n_mode = os.stat(DOT_SAGE)[stat.ST_MODE]\n_desired_mode = 040700     # drwx------\nif _mode != _desired_mode:\n    print \"Setting permissions of DOT_SAGE directory so only you can read and write it.\"\n    # Change mode of DOT_SAGE.\n    os.chmod(DOT_SAGE, _desired_mode)\n...\nSAGE_TMP='%s/temp/%s/%s/'%(DOT_SAGE, HOSTNAME, os.getpid())\nif not os.path.exists(SAGE_TMP):\n    try:\n        os.makedirs(SAGE_TMP)\n    except OSError, msg:\n        print msg\n        raise OSError, \" ** Error trying to create the Sage tmp directory...\"\n...\n```\n",
    "created_at": "2011-07-27T14:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95271",
    "user": "leif"
}
```

For the record, we already have the following in `sage/misc/misc.py`:


```python
...
HOSTNAME = socket.gethostname().replace('-','_').replace('/','_').replace('\\','_')

LOCAL_IDENTIFIER = '%s.%s'%(HOSTNAME , os.getpid())
...
try:
    DOT_SAGE = os.environ['DOT_SAGE']
except KeyError:
    try:
        DOT_SAGE = '%s/.sage/'%os.environ['HOME']
    except KeyError:
        DOT_SAGE = '%s/.sage/'%SAGE_ROOT
...
if not os.path.exists(DOT_SAGE):
    os.makedirs(DOT_SAGE)

_mode = os.stat(DOT_SAGE)[stat.ST_MODE]
_desired_mode = 040700     # drwx------
if _mode != _desired_mode:
    print "Setting permissions of DOT_SAGE directory so only you can read and write it."
    # Change mode of DOT_SAGE.
    os.chmod(DOT_SAGE, _desired_mode)
...
SAGE_TMP='%s/temp/%s/%s/'%(DOT_SAGE, HOSTNAME, os.getpid())
if not os.path.exists(SAGE_TMP):
    try:
        os.makedirs(SAGE_TMP)
    except OSError, msg:
        print msg
        raise OSError, " ** Error trying to create the Sage tmp directory..."
...
```




---

archive/issue_comments_095272.json:
```json
{
    "body": "... so we could do almost the same for / below `SAGE_TESTDIR`, perhaps creating a single directory name from `HOSTNAME` and the PID (avoiding further race conditions, provided `$SAGE_TESTDIR` already exists), putting all temporary files (names mangled as proposed, unique to each *test instance*) into that, i.e.\n\n`${SAGE_TESTDIR}/${hostname}-${pid}/doctest-relative__path__to__foo__foo.py`\n\nfor a file `./relative/path/to/foo/foo.py`.",
    "created_at": "2011-07-27T14:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95272",
    "user": "leif"
}
```

... so we could do almost the same for / below `SAGE_TESTDIR`, perhaps creating a single directory name from `HOSTNAME` and the PID (avoiding further race conditions, provided `$SAGE_TESTDIR` already exists), putting all temporary files (names mangled as proposed, unique to each *test instance*) into that, i.e.

`${SAGE_TESTDIR}/${hostname}-${pid}/doctest-relative__path__to__foo__foo.py`

for a file `./relative/path/to/foo/foo.py`.



---

archive/issue_comments_095273.json:
```json
{
    "body": "Can we just use Python's tempfile module, for example [mkstemp](http://docs.python.org/library/tempfile.html#tempfile.mkstemp)?  This should produce a temporary file safely, avoiding race conditions.  We can have the name end with the file being tested, including its path.\n\n(I think we should do the same thing for `SAGE_TMP` in `misc.py`, but that's for another ticket.)",
    "created_at": "2011-07-27T14:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95273",
    "user": "jhpalmieri"
}
```

Can we just use Python's tempfile module, for example [mkstemp](http://docs.python.org/library/tempfile.html#tempfile.mkstemp)?  This should produce a temporary file safely, avoiding race conditions.  We can have the name end with the file being tested, including its path.

(I think we should do the same thing for `SAGE_TMP` in `misc.py`, but that's for another ticket.)



---

archive/issue_comments_095274.json:
```json
{
    "body": "Replying to [comment:47 jhpalmieri]:\n> Can we just use Python's tempfile module, for example [mkstemp](http://docs.python.org/library/tempfile.html#tempfile.mkstemp)?  This should produce a temporary file safely, avoiding race conditions.  We can have the name end with the file being tested, including its path.\n\nI see no reason for doing so. We don't need even more cryptic filenames, and I don't think it will work across NFS filesystems.\n\nThe only \"race condition\" that can occur in what I suggested above is in the creation of `SAGE_TESTDIR` itself (if it doesn't already exist), and that can easily be catched.\n\n> (I think we should do the same thing for `SAGE_TMP` in `misc.py`, but that's for another ticket.)\n\nI wouldn't do that either. If we create temporary files from shell scripts, we can use the same mechanism.",
    "created_at": "2011-07-27T15:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95274",
    "user": "leif"
}
```

Replying to [comment:47 jhpalmieri]:
> Can we just use Python's tempfile module, for example [mkstemp](http://docs.python.org/library/tempfile.html#tempfile.mkstemp)?  This should produce a temporary file safely, avoiding race conditions.  We can have the name end with the file being tested, including its path.

I see no reason for doing so. We don't need even more cryptic filenames, and I don't think it will work across NFS filesystems.

The only "race condition" that can occur in what I suggested above is in the creation of `SAGE_TESTDIR` itself (if it doesn't already exist), and that can easily be catched.

> (I think we should do the same thing for `SAGE_TMP` in `misc.py`, but that's for another ticket.)

I wouldn't do that either. If we create temporary files from shell scripts, we can use the same mechanism.



---

archive/issue_comments_095275.json:
```json
{
    "body": "Furthermore:\n\n *\"The file descriptor is not inherited by child processes.\"*\n\n *\"There is thus no guarantee that the generated filename will have any nice properties, such as not requiring quoting when passed to external commands via `os.popen()`.\"*",
    "created_at": "2011-07-27T15:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95275",
    "user": "leif"
}
```

Furthermore:

 *"The file descriptor is not inherited by child processes."*

 *"There is thus no guarantee that the generated filename will have any nice properties, such as not requiring quoting when passed to external commands via `os.popen()`."*



---

archive/issue_comments_095276.json:
```json
{
    "body": "> I see no reason for doing so.\n\nThere are several reasons for doing so: one is to not reinvent the wheel, and anything we come up with is likely to be less robust than what's built into Python.  Also, if we want to doctest outside of `$HOME/.sage`, is `/tmp` always the best place?  The mkstemp function doesn't always create files there, so I'm not convinced we should.\n\nBy the way, using the PID in the directory name means creating many directories: as far as I can tell, running `sage -t DIR` uses a different process for each file in DIR.  Perhaps the PID should be in the mangled filename instead of part of a new directory.",
    "created_at": "2011-07-27T15:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95276",
    "user": "jhpalmieri"
}
```

> I see no reason for doing so.

There are several reasons for doing so: one is to not reinvent the wheel, and anything we come up with is likely to be less robust than what's built into Python.  Also, if we want to doctest outside of `$HOME/.sage`, is `/tmp` always the best place?  The mkstemp function doesn't always create files there, so I'm not convinced we should.

By the way, using the PID in the directory name means creating many directories: as far as I can tell, running `sage -t DIR` uses a different process for each file in DIR.  Perhaps the PID should be in the mangled filename instead of part of a new directory.



---

archive/issue_comments_095277.json:
```json
{
    "body": "Still, the best thing is to not create temporary files at all.\n\n(And only dump what would have been written in case of doctest errors, once at the end, with the \"same problems\", though identical filenames would there be even more unlikely, and could easily be numbered.)\n\nBut that's probably for another ticket; we should IMHO here only *quickly* fix the most prominent errors, namely identical filenames within the *same* `ptest`[`long`] instance. If we also allow simultaneous testing of the same or different Sage installations, that's ok, but a pretty minor issue, because -- in contrast to the former -- you can trivially avoid race conditions between such concurrent `ptest` runs. (And a normal user wouldn't do the latter either.)",
    "created_at": "2011-07-27T15:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95277",
    "user": "leif"
}
```

Still, the best thing is to not create temporary files at all.

(And only dump what would have been written in case of doctest errors, once at the end, with the "same problems", though identical filenames would there be even more unlikely, and could easily be numbered.)

But that's probably for another ticket; we should IMHO here only *quickly* fix the most prominent errors, namely identical filenames within the *same* `ptest`[`long`] instance. If we also allow simultaneous testing of the same or different Sage installations, that's ok, but a pretty minor issue, because -- in contrast to the former -- you can trivially avoid race conditions between such concurrent `ptest` runs. (And a normal user wouldn't do the latter either.)



---

archive/issue_comments_095278.json:
```json
{
    "body": "Replying to [comment:50 jhpalmieri]:\n> > I see no reason for doing so.\n> \n> There are several reasons for doing so: one is to not reinvent the wheel, and anything we come up with is likely to be less robust than what's built into Python.\n\nAmen? Also, unless it uses a local filesystem, I don't think it will work with NFS.\n\n>  Also, if we want to doctest outside of `$HOME/.sage`, is `/tmp` always the best place?  The mkstemp function doesn't always create files there, so I'm not convinced we should.\n\nIt simply (in contrast to Sage) respects the commonly used `TMP` (`TEMP` on M$ Windows) and `TMPDIR` environment variables.\n\nBtw, on typical machines `/tmp` does not even really exist on a drive, it's just in memory (and if that's exhausted, swap space will be used transparently). If it is a real partition on a drive, you either use an SSD or at least use that area of a conventional hard drive that is fastest (same for swap).\n\n> By the way, using the PID in the directory name means creating many directories: as far as I can tell, running `sage -t DIR` uses a different process for each file in DIR.  Perhaps the PID should be in the mangled filename instead of part of a new directory.\n\nAt least at the moment, we're dealing with `ptest*` only here, so that's another matter (if you want to run multiple `testlong`s for example using the same temporary directory). So `sage -t ...` wouldn't create any directories at all.",
    "created_at": "2011-07-27T16:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95278",
    "user": "leif"
}
```

Replying to [comment:50 jhpalmieri]:
> > I see no reason for doing so.
> 
> There are several reasons for doing so: one is to not reinvent the wheel, and anything we come up with is likely to be less robust than what's built into Python.

Amen? Also, unless it uses a local filesystem, I don't think it will work with NFS.

>  Also, if we want to doctest outside of `$HOME/.sage`, is `/tmp` always the best place?  The mkstemp function doesn't always create files there, so I'm not convinced we should.

It simply (in contrast to Sage) respects the commonly used `TMP` (`TEMP` on M$ Windows) and `TMPDIR` environment variables.

Btw, on typical machines `/tmp` does not even really exist on a drive, it's just in memory (and if that's exhausted, swap space will be used transparently). If it is a real partition on a drive, you either use an SSD or at least use that area of a conventional hard drive that is fastest (same for swap).

> By the way, using the PID in the directory name means creating many directories: as far as I can tell, running `sage -t DIR` uses a different process for each file in DIR.  Perhaps the PID should be in the mangled filename instead of part of a new directory.

At least at the moment, we're dealing with `ptest*` only here, so that's another matter (if you want to run multiple `testlong`s for example using the same temporary directory). So `sage -t ...` wouldn't create any directories at all.



---

archive/issue_comments_095279.json:
```json
{
    "body": "Replying to [comment:52 leif]:\n\n> > By the way, using the PID in the directory name means creating many directories: as far as I can tell, running `sage -t DIR` uses a different process for each file in DIR.  Perhaps the PID should be in the mangled filename instead of part of a new directory.\n> \n> At least at the moment, we're dealing with `ptest*` only here, so that's another matter (if you want to run multiple `testlong`s for example using the same temporary directory). So `sage -t ...` wouldn't create any directories at all.\n\nI was envisioning patching sage-doctest, since that's what copies the file being tested to SAGE_TESTDIR (and later deletes it), and it gets run by \"sage -t ...\", \"sage -tp ...\", etc.   Running \"sage -tp DIR\" also uses a different PID for each execution of sage-doctest.",
    "created_at": "2011-07-27T16:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95279",
    "user": "jhpalmieri"
}
```

Replying to [comment:52 leif]:

> > By the way, using the PID in the directory name means creating many directories: as far as I can tell, running `sage -t DIR` uses a different process for each file in DIR.  Perhaps the PID should be in the mangled filename instead of part of a new directory.
> 
> At least at the moment, we're dealing with `ptest*` only here, so that's another matter (if you want to run multiple `testlong`s for example using the same temporary directory). So `sage -t ...` wouldn't create any directories at all.

I was envisioning patching sage-doctest, since that's what copies the file being tested to SAGE_TESTDIR (and later deletes it), and it gets run by "sage -t ...", "sage -tp ...", etc.   Running "sage -tp DIR" also uses a different PID for each execution of sage-doctest.



---

archive/issue_comments_095280.json:
```json
{
    "body": "Replying to [comment:53 jhpalmieri]:\n> I was envisioning patching sage-doctest, since that's what copies the file being tested to SAGE_TESTDIR (and later deletes it), and it gets run by \"sage -t ...\", \"sage -tp ...\", etc.   Running \"sage -tp DIR\" also uses a different PID for each execution of sage-doctest.\n\nI would simply pass `sage-doctest` the already created directory (either as a parameter, or simply in the environment variable which it already uses anyway).\n\nCreating the directory inside `sage-doctest` doesn't make any sense, since **all** instances would attempt to create it. (You can or could use `os.getppid()` though.)\n\n\nThe whole collection of doctest scripts needs an overhaul (or redesign) in the long run...\n\nP.S.: We can use `tempfile.gettempdir()` in case `SAGE_TESTDIR` isn't set if that makes you happy.",
    "created_at": "2011-07-27T17:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95280",
    "user": "leif"
}
```

Replying to [comment:53 jhpalmieri]:
> I was envisioning patching sage-doctest, since that's what copies the file being tested to SAGE_TESTDIR (and later deletes it), and it gets run by "sage -t ...", "sage -tp ...", etc.   Running "sage -tp DIR" also uses a different PID for each execution of sage-doctest.

I would simply pass `sage-doctest` the already created directory (either as a parameter, or simply in the environment variable which it already uses anyway).

Creating the directory inside `sage-doctest` doesn't make any sense, since **all** instances would attempt to create it. (You can or could use `os.getppid()` though.)


The whole collection of doctest scripts needs an overhaul (or redesign) in the long run...

P.S.: We can use `tempfile.gettempdir()` in case `SAGE_TESTDIR` isn't set if that makes you happy.



---

archive/issue_comments_095281.json:
```json
{
    "body": "Right now, if there are doctest failures or if doctesting is interrupted, the temporary files remain in SAGE_TEMPDIR.  If we create a new directory each time, then these directories will remain (we should certainly check if they're empty and then delete them, but if they're not empty, we should not automatically delete them, I think).  Is it any better or worse to have a bunch of directories in SAGE_TEMPDIR, as opposed to a bunch of files?\n\nMeanwhile, here's an attempt at a patch.",
    "created_at": "2011-07-27T18:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95281",
    "user": "jhpalmieri"
}
```

Right now, if there are doctest failures or if doctesting is interrupted, the temporary files remain in SAGE_TEMPDIR.  If we create a new directory each time, then these directories will remain (we should certainly check if they're empty and then delete them, but if they're not empty, we should not automatically delete them, I think).  Is it any better or worse to have a bunch of directories in SAGE_TEMPDIR, as opposed to a bunch of files?

Meanwhile, here's an attempt at a patch.



---

archive/issue_comments_095282.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-07-27T18:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95282",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095283.json:
```json
{
    "body": "At this point just a comment on the naming / mangling:\n\n* To me, it doesn't make any sense to create \"hidden\" files, so I would omit the leading period.\n* We should perhaps apply some character substitutions to `socket.gethostname()` as well, like `sage.misc.misc` does (see quote above).\n* Thinking more about it, I would replace slashs (`os.path.sep`) by periods (and not double-underscores or, as currently, dashs), since that way the temporary filenames resemble (at least partially) fully qualified Python module names.\n\n(As discussed, I'd also change the *default* for `SAGE_TESTDIR`, e.g. to `tempfile.gettempdir()`.)\n\nWe could make sure once that the temporary directory (`${SAGE_TESTDIR}/${hostname}-${pid}/`) is writable by the user. I think we should also clean it up in case it already exists, as anything left there is potentially very old and unrelated to the current test run. We *might* also adjust the permissions of the directory.\n\n\nLooking only at your (John's) patch, is `temp_py_file` defined anywhere? (I only see it gets added to `tmpfiles`.)\n\n\nP.S.: Why not base the patch on Mitesh's? (Which AFAIR only needed two changes.)",
    "created_at": "2011-07-28T14:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95283",
    "user": "leif"
}
```

At this point just a comment on the naming / mangling:

* To me, it doesn't make any sense to create "hidden" files, so I would omit the leading period.
* We should perhaps apply some character substitutions to `socket.gethostname()` as well, like `sage.misc.misc` does (see quote above).
* Thinking more about it, I would replace slashs (`os.path.sep`) by periods (and not double-underscores or, as currently, dashs), since that way the temporary filenames resemble (at least partially) fully qualified Python module names.

(As discussed, I'd also change the *default* for `SAGE_TESTDIR`, e.g. to `tempfile.gettempdir()`.)

We could make sure once that the temporary directory (`${SAGE_TESTDIR}/${hostname}-${pid}/`) is writable by the user. I think we should also clean it up in case it already exists, as anything left there is potentially very old and unrelated to the current test run. We *might* also adjust the permissions of the directory.


Looking only at your (John's) patch, is `temp_py_file` defined anywhere? (I only see it gets added to `tmpfiles`.)


P.S.: Why not base the patch on Mitesh's? (Which AFAIR only needed two changes.)



---

archive/issue_comments_095284.json:
```json
{
    "body": "Replying to [comment:56 leif]:\n> At this point just a comment on the naming / mangling:\n> \n>  * To me, it doesn't make any sense to create \"hidden\" files, so I would omit the leading period.\n\nOkay, not a high priority and outside the scope of this ticket, but harmless enough.  Done.  (We could do the same thing with the files recording timing data, but that's for another ticket.)\n\n>  * We should perhaps apply some character substitutions to `socket.gethostname()` as well, like `sage.misc.misc` does (see quote above).\n\nDone.\n\n>  * Thinking more about it, I would replace slashs (`os.path.sep`) by periods (and not double-underscores or, as currently, dashs), since that way the temporary filenames resemble (at least partially) fully qualified Python module names.\n\nDone.\n\n> \n> (As discussed, I'd also change the *default* for `SAGE_TESTDIR`, e.g. to `tempfile.gettempdir()`.)\n\nI know that I was suggesting this earlier, but on further reflection, we shouldn't do this here: for example, there may be users who expect the doctesting files to be in `.sage/tmp/`, and changing this may therefore make people unhappy.  I think it's a good idea, but it should be on another ticket. (I'm agreeing with Dave's point that we should try to fix just the bug here, and then we can work on other improvement separately.)\n\n> We could make sure once that the temporary directory (`${SAGE_TESTDIR}/${hostname}-${pid}/`) is writable by the user. I think we should also clean it up in case it already exists, as anything left there is potentially very old and unrelated to the current test run. We *might* also adjust the permissions of the directory.\n\nDone.\n\n> Looking only at your (John's) patch, is `temp_py_file` defined anywhere? (I only see it gets added to `tmpfiles`.)\n\nThat was a mistake, which I think I've fixed.\n \n> P.S.: Why not base the patch on Mitesh's? (Which AFAIR only needed two changes.)\n\nNo good reason.",
    "created_at": "2011-07-28T16:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95284",
    "user": "jhpalmieri"
}
```

Replying to [comment:56 leif]:
> At this point just a comment on the naming / mangling:
> 
>  * To me, it doesn't make any sense to create "hidden" files, so I would omit the leading period.

Okay, not a high priority and outside the scope of this ticket, but harmless enough.  Done.  (We could do the same thing with the files recording timing data, but that's for another ticket.)

>  * We should perhaps apply some character substitutions to `socket.gethostname()` as well, like `sage.misc.misc` does (see quote above).

Done.

>  * Thinking more about it, I would replace slashs (`os.path.sep`) by periods (and not double-underscores or, as currently, dashs), since that way the temporary filenames resemble (at least partially) fully qualified Python module names.

Done.

> 
> (As discussed, I'd also change the *default* for `SAGE_TESTDIR`, e.g. to `tempfile.gettempdir()`.)

I know that I was suggesting this earlier, but on further reflection, we shouldn't do this here: for example, there may be users who expect the doctesting files to be in `.sage/tmp/`, and changing this may therefore make people unhappy.  I think it's a good idea, but it should be on another ticket. (I'm agreeing with Dave's point that we should try to fix just the bug here, and then we can work on other improvement separately.)

> We could make sure once that the temporary directory (`${SAGE_TESTDIR}/${hostname}-${pid}/`) is writable by the user. I think we should also clean it up in case it already exists, as anything left there is potentially very old and unrelated to the current test run. We *might* also adjust the permissions of the directory.

Done.

> Looking only at your (John's) patch, is `temp_py_file` defined anywhere? (I only see it gets added to `tmpfiles`.)

That was a mistake, which I think I've fixed.
 
> P.S.: Why not base the patch on Mitesh's? (Which AFAIR only needed two changes.)

No good reason.



---

archive/issue_comments_095285.json:
```json
{
    "body": "Oops, just found a mistake.  In non-Sage library code, when doctesting \"file0.py\", we write a line\n\n```\nfrom file0 import *\n```\n\nWith the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.  We can either just revert the part of the code involving non-Sage library code, or we can try to fix the mangled names.  Right now I'm doing the first of these, since the first priority should be to fix things for doctesting the Sage library.",
    "created_at": "2011-07-28T17:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95285",
    "user": "jhpalmieri"
}
```

Oops, just found a mistake.  In non-Sage library code, when doctesting "file0.py", we write a line

```
from file0 import *
```

With the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.  We can either just revert the part of the code involving non-Sage library code, or we can try to fix the mangled names.  Right now I'm doing the first of these, since the first priority should be to fix things for doctesting the Sage library.



---

archive/issue_comments_095286.json:
```json
{
    "body": "Replying to [comment:57 jhpalmieri]:\n> Replying to [comment:56 leif]:\n> > (As discussed, I'd also change the *default* for `SAGE_TESTDIR`, e.g. to `tempfile.gettempdir()`.)\n> \n> I know that I was suggesting this earlier, but on further reflection, we shouldn't do this here: for example, there may be users who expect the doctesting files to be in `.sage/tmp/`, and changing this may therefore make people unhappy.  I think it's a good idea, but it should be on another ticket. (I'm agreeing with Dave's point that we should try to fix just the bug here, and then we can work on other improvement separately.)\n\nThat was my opinion; Dave earlier requested extensions to allow *simultaneous* testing (including `make test`[`long`] etc.) of *multiple* (possibly the same) Sage installations in the \"same\" directory (`SAGE_TESTDIR`), i.e. without having to manually set `SAGE_TESTDIR` in different shells.\n\nAs further enhancements, we should perhaps print the location at the beginning, and also at the end if any doctest errors occurred. (I'm right now not sure if `GLOBAL_ITER` etc. get printed, I only recall we should also print **either** `SAGE_TIMEOUT` **or** `SAGE_TIMEOUT_LONG`, whichever is appropriate, as many people seem to misunderstand the meaning and perhaps also don't know the defaults, which are btw. *wall* time and not CPU time -- perhaps subject to change later as well... :) .)\n\n(A few `print` statements wouldn't complicate the patch *here* though. And if we print `SAGE_TESTDIR` anyway, we could at the same time change its default to a sensible value as well.)\n\n\n\n\n> > P.S.: Why not base the patch on Mitesh's? (Which AFAIR only needed two changes.)\n> \n> No good reason.\n\nHmmm. Mitesh fixed some other things as well, so we should somehow make sure the changes don't get lost once this ticket is merged / closed. (I remember having reviewed them last year, before he updated the patch again though IIRC. I think Robert was also ok with his changes, except for the creation of directories / the temporary files' names and locations.)\n\nUnfortunately, there are meanwhile *many* \"concurrent\" tickets dealing with the doctest scripts.\n\nI'd of course also like to see my comments from the [comment:32 inline patch to `sage-ptest` above] in it... ;-) (Just the comments, which are FIXMEs / TODOs, not [necessarily] the `flush()`s.)\n\n\n\n\nI'll apply and take a look at your second patch later.",
    "created_at": "2011-07-28T17:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95286",
    "user": "leif"
}
```

Replying to [comment:57 jhpalmieri]:
> Replying to [comment:56 leif]:
> > (As discussed, I'd also change the *default* for `SAGE_TESTDIR`, e.g. to `tempfile.gettempdir()`.)
> 
> I know that I was suggesting this earlier, but on further reflection, we shouldn't do this here: for example, there may be users who expect the doctesting files to be in `.sage/tmp/`, and changing this may therefore make people unhappy.  I think it's a good idea, but it should be on another ticket. (I'm agreeing with Dave's point that we should try to fix just the bug here, and then we can work on other improvement separately.)

That was my opinion; Dave earlier requested extensions to allow *simultaneous* testing (including `make test`[`long`] etc.) of *multiple* (possibly the same) Sage installations in the "same" directory (`SAGE_TESTDIR`), i.e. without having to manually set `SAGE_TESTDIR` in different shells.

As further enhancements, we should perhaps print the location at the beginning, and also at the end if any doctest errors occurred. (I'm right now not sure if `GLOBAL_ITER` etc. get printed, I only recall we should also print **either** `SAGE_TIMEOUT` **or** `SAGE_TIMEOUT_LONG`, whichever is appropriate, as many people seem to misunderstand the meaning and perhaps also don't know the defaults, which are btw. *wall* time and not CPU time -- perhaps subject to change later as well... :) .)

(A few `print` statements wouldn't complicate the patch *here* though. And if we print `SAGE_TESTDIR` anyway, we could at the same time change its default to a sensible value as well.)




> > P.S.: Why not base the patch on Mitesh's? (Which AFAIR only needed two changes.)
> 
> No good reason.

Hmmm. Mitesh fixed some other things as well, so we should somehow make sure the changes don't get lost once this ticket is merged / closed. (I remember having reviewed them last year, before he updated the patch again though IIRC. I think Robert was also ok with his changes, except for the creation of directories / the temporary files' names and locations.)

Unfortunately, there are meanwhile *many* "concurrent" tickets dealing with the doctest scripts.

I'd of course also like to see my comments from the [comment:32 inline patch to `sage-ptest` above] in it... ;-) (Just the comments, which are FIXMEs / TODOs, not [necessarily] the `flush()`s.)




I'll apply and take a look at your second patch later.



---

archive/issue_comments_095287.json:
```json
{
    "body": "Replying to [comment:58 jhpalmieri]:\n> Oops, just found a mistake.  In non-Sage library code, when doctesting \"file0.py\", we write a line\n\n```\nfrom file0 import *\n```\n\n> With the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.\n\nHence underscores, which I originally thought of?\n\nIt doesn't make sense to copy [only] each single non-library file to doctest to the temporary directory anyway, as it might import other files located in the original directory.\n\nWe could either just `cd` to the original directory, or -- IMHO much better -- add the original directory to `PYTHONPATH` or `sys.path`, both methods solving the mangling issue in `from ... import *`, as well as saving useless copying. (We of course still have to create temporary preparsed files in `SAGE_TESTDIR/.../` for `.sage` and `.spyx` files though.)",
    "created_at": "2011-07-28T18:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95287",
    "user": "leif"
}
```

Replying to [comment:58 jhpalmieri]:
> Oops, just found a mistake.  In non-Sage library code, when doctesting "file0.py", we write a line

```
from file0 import *
```

> With the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.

Hence underscores, which I originally thought of?

It doesn't make sense to copy [only] each single non-library file to doctest to the temporary directory anyway, as it might import other files located in the original directory.

We could either just `cd` to the original directory, or -- IMHO much better -- add the original directory to `PYTHONPATH` or `sys.path`, both methods solving the mangling issue in `from ... import *`, as well as saving useless copying. (We of course still have to create temporary preparsed files in `SAGE_TESTDIR/.../` for `.sage` and `.spyx` files though.)



---

archive/issue_comments_095288.json:
```json
{
    "body": "Replying to [comment:60 leif]:\n> Replying to [comment:58 jhpalmieri]:\n> > Oops, just found a mistake.  In non-Sage library code, when doctesting \"file0.py\", we write a line\n> {{{\n> from file0 import *\n> }}}\n> > With the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.\n> \n> Hence underscores, which I originally thought of?\n\nWell, the host name could contain all sorts of characters in it, couldn't it?  Same for the directories in the path to the file, especially since we're talking about files not in the Sage library.  Doing some sort of regexp search and replace is a lot of work for perhaps minimal gain.  It certainly doesn't have to do with the issue on this ticket.\n\n> It doesn't make sense to copy [only] each single non-library file to doctest to the temporary directory anyway, as it might import other files located in the original directory.\n\nOutside the scope of this ticket.  If we leave that part alone, we're not creating a new bug, just leaving a less-than-perfect implementation in place.\n\nMeanwhile, if you want to add in some print statements, comments, some of the relevant parts of Mitesh's patch, or anything else, go ahead.  I have to work on some other things for at least a few days.",
    "created_at": "2011-07-28T21:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95288",
    "user": "jhpalmieri"
}
```

Replying to [comment:60 leif]:
> Replying to [comment:58 jhpalmieri]:
> > Oops, just found a mistake.  In non-Sage library code, when doctesting "file0.py", we write a line
> {{{
> from file0 import *
> }}}
> > With the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.
> 
> Hence underscores, which I originally thought of?

Well, the host name could contain all sorts of characters in it, couldn't it?  Same for the directories in the path to the file, especially since we're talking about files not in the Sage library.  Doing some sort of regexp search and replace is a lot of work for perhaps minimal gain.  It certainly doesn't have to do with the issue on this ticket.

> It doesn't make sense to copy [only] each single non-library file to doctest to the temporary directory anyway, as it might import other files located in the original directory.

Outside the scope of this ticket.  If we leave that part alone, we're not creating a new bug, just leaving a less-than-perfect implementation in place.

Meanwhile, if you want to add in some print statements, comments, some of the relevant parts of Mitesh's patch, or anything else, go ahead.  I have to work on some other things for at least a few days.



---

archive/issue_comments_095289.json:
```json
{
    "body": "Replying to [comment:61 jhpalmieri]:\n> Replying to [comment:60 leif]:\n> > Replying to [comment:58 jhpalmieri]:\n> > > Oops, just found a mistake.  In non-Sage library code, when doctesting \"file0.py\", we write a line\n\n```\nfrom file0 import *\n```\n\n> > > With the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.\n> > Hence underscores, which I originally thought of?\n> \n> Well, the host name could contain all sorts of characters in it, couldn't it?  Same for the directories in the path to the file, especially since we're talking about files not in the Sage library.\n> Doing some sort of regexp search and replace is a lot of work for perhaps minimal gain.\n\nWell, you don't have to mangle the name in the `import` statement at all (and the hostname is part of the *directory* name, not a filename, anyway).\n\n> It certainly doesn't have to do with the issue on this ticket.\n\nOf course it does. You tried to also mangle the `import` name to avoid name clashs, but that's simply not necessary. Just prepend the original (source) directory of the file to test to `PYTHONPATH`, and keep the [base]name of the file in `from ... import *` unmodified (and of course without a path). \n\nFor files of the Sage library, we strip that path (at least Mitesh did), since all necessary (root) directories are already in `PYTHONPATH`.\n\nThe only \"problem\" are files that have to be preparsed (`*.sage`), at least if we don't want to create the intermediate, preparsed `.py` files at the original location, preferably just once.\n\nFor these files, we simply can do almost what Mitesh did, namely create a temporary file with an \"arbitrary\" (Python module name-conforming) but unique basename and the extension `.py` in `SAGE_TESTDIR` (from the perspective of `sage-doctest`, i.e. already containing the hostname and the pid of the parent process), using either `tempfile.mkstemp()` [which is safe here] or preferably just `sage-doctest`'s PID, import *that* in the `doctest_*` file, and also append it to `tmpfiles`:\n\n```python\n    # We are in \"sage-doctest\",\n    # SAGE_TESTDIR is already \".../${hostname}-${ppid}/\"\n    ...\n    if not library_code: \n\n        if ext in ['.pyx','.spyx']: \n            s += \"cython(open('%s').read())\\n\\n\" % file_name\n\n        elif ext in ['.py', '.sage']: \n\n            source = file_name # full name with path\n            target_name = \"%s_%d\" % (name, os.getpid()) # like 'name', but unique\n            target_base = os.path.join(SAGE_TESTDIR, target_name) # like 'base', also unique\n\n            if ext == '.sage':\n                # Unfortunately, \"sage -preparse <file>.sage\" doesn't have any\n                # output options and always creates <file>.py in the same\n                # directory, so we first copy the *source* into SAGE_TESTDIR:\n                os.system(\"cp '%s' %s.sage\" % (source, target_base))\n                # Now create SAGE_TESTDIR/<target_name>.py:\n                os.system(\"sage -preparse %s.sage\" % target_base)\n                # Remove the copy of the original (.sage):\n                # (We could also just add it to 'tmpfiles'.)\n                os.system(\"rm -f %s.sage\" % target_base)\n\n            else:\n                # Plain Python file (\".py\"), just copy it:\n                # (If we added source's directory to PYTHONPATH,\n                # we wouldn't have to copy the file, but then also\n                # would have to import from 'name' instead of 'target_name'.)\n                os.system(\"cp '%s' %s.py\" % (source, target_base))\n\n            s += \"from %s import *\\n\\n\" % target_name\n\n            tmpfiles.append(target_base + \".py\") # preparsed or copied original\n            tmpfiles.append(target_base + \".pyc\") # compiled version of it\n\n    ...\n```\n\n\n\n\n\nA better solution, as Mitesh noted in the `TODO` comment, is to preparse the file into a string, and directly write that string into the `doctest_*` file where we currently have the `from ... import *`.\n\n*That enhancement* is most probably a thing to do on a follow-up ticket, but not supporting (i.e. avoiding name clashes for) non-library files would be a regression w.r.t. Mitesh's patch.\n\n\n\n\n> > It doesn't make sense to copy [only] each single non-library file to doctest to the temporary directory anyway, as it might import other files located in the original directory.\n> \n> Outside the scope of this ticket.  If we leave that part alone, we're not creating a new bug, just leaving a less-than-perfect implementation in place.\n\nSee above. I there just copy the \"main\" file, which we still can change later.\n\n\n\n\n> Meanwhile, if you want to add in some print statements, comments, some of the relevant parts of Mitesh's patch, or anything else, go ahead.  I have to work on some other things for at least a few days.\n\nAs I said, I would have preferred having your patch based on Mitesh's, since there are a couple of changes that could have been kept, just changing the \"mangling\".\n\nI can add a reviewer patch for *my comments* (and perhaps a few `print` statements) later; rebasing Mitesh's would be a lot of work and so I don't know if I'll do that.",
    "created_at": "2011-07-29T01:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95289",
    "user": "leif"
}
```

Replying to [comment:61 jhpalmieri]:
> Replying to [comment:60 leif]:
> > Replying to [comment:58 jhpalmieri]:
> > > Oops, just found a mistake.  In non-Sage library code, when doctesting "file0.py", we write a line

```
from file0 import *
```

> > > With the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.
> > Hence underscores, which I originally thought of?
> 
> Well, the host name could contain all sorts of characters in it, couldn't it?  Same for the directories in the path to the file, especially since we're talking about files not in the Sage library.
> Doing some sort of regexp search and replace is a lot of work for perhaps minimal gain.

Well, you don't have to mangle the name in the `import` statement at all (and the hostname is part of the *directory* name, not a filename, anyway).

> It certainly doesn't have to do with the issue on this ticket.

Of course it does. You tried to also mangle the `import` name to avoid name clashs, but that's simply not necessary. Just prepend the original (source) directory of the file to test to `PYTHONPATH`, and keep the [base]name of the file in `from ... import *` unmodified (and of course without a path). 

For files of the Sage library, we strip that path (at least Mitesh did), since all necessary (root) directories are already in `PYTHONPATH`.

The only "problem" are files that have to be preparsed (`*.sage`), at least if we don't want to create the intermediate, preparsed `.py` files at the original location, preferably just once.

For these files, we simply can do almost what Mitesh did, namely create a temporary file with an "arbitrary" (Python module name-conforming) but unique basename and the extension `.py` in `SAGE_TESTDIR` (from the perspective of `sage-doctest`, i.e. already containing the hostname and the pid of the parent process), using either `tempfile.mkstemp()` [which is safe here] or preferably just `sage-doctest`'s PID, import *that* in the `doctest_*` file, and also append it to `tmpfiles`:

```python
    # We are in "sage-doctest",
    # SAGE_TESTDIR is already ".../${hostname}-${ppid}/"
    ...
    if not library_code: 

        if ext in ['.pyx','.spyx']: 
            s += "cython(open('%s').read())\n\n" % file_name

        elif ext in ['.py', '.sage']: 

            source = file_name # full name with path
            target_name = "%s_%d" % (name, os.getpid()) # like 'name', but unique
            target_base = os.path.join(SAGE_TESTDIR, target_name) # like 'base', also unique

            if ext == '.sage':
                # Unfortunately, "sage -preparse <file>.sage" doesn't have any
                # output options and always creates <file>.py in the same
                # directory, so we first copy the *source* into SAGE_TESTDIR:
                os.system("cp '%s' %s.sage" % (source, target_base))
                # Now create SAGE_TESTDIR/<target_name>.py:
                os.system("sage -preparse %s.sage" % target_base)
                # Remove the copy of the original (.sage):
                # (We could also just add it to 'tmpfiles'.)
                os.system("rm -f %s.sage" % target_base)

            else:
                # Plain Python file (".py"), just copy it:
                # (If we added source's directory to PYTHONPATH,
                # we wouldn't have to copy the file, but then also
                # would have to import from 'name' instead of 'target_name'.)
                os.system("cp '%s' %s.py" % (source, target_base))

            s += "from %s import *\n\n" % target_name

            tmpfiles.append(target_base + ".py") # preparsed or copied original
            tmpfiles.append(target_base + ".pyc") # compiled version of it

    ...
```





A better solution, as Mitesh noted in the `TODO` comment, is to preparse the file into a string, and directly write that string into the `doctest_*` file where we currently have the `from ... import *`.

*That enhancement* is most probably a thing to do on a follow-up ticket, but not supporting (i.e. avoiding name clashes for) non-library files would be a regression w.r.t. Mitesh's patch.




> > It doesn't make sense to copy [only] each single non-library file to doctest to the temporary directory anyway, as it might import other files located in the original directory.
> 
> Outside the scope of this ticket.  If we leave that part alone, we're not creating a new bug, just leaving a less-than-perfect implementation in place.

See above. I there just copy the "main" file, which we still can change later.




> Meanwhile, if you want to add in some print statements, comments, some of the relevant parts of Mitesh's patch, or anything else, go ahead.  I have to work on some other things for at least a few days.

As I said, I would have preferred having your patch based on Mitesh's, since there are a couple of changes that could have been kept, just changing the "mangling".

I can add a reviewer patch for *my comments* (and perhaps a few `print` statements) later; rebasing Mitesh's would be a lot of work and so I don't know if I'll do that.



---

archive/issue_comments_095290.json:
```json
{
    "body": "Here is a patch based on Mitesh's; the \"delta\" patch shows the changes; these changes include your in-line patch.  This does not change SAGE_TESTDIR to `tempfile.gettempdir()`: we store timing information in this directory, so it should not be temporary.  It might be a good idea to change `TMP` (as used in `sage-ptest`) to a temporary directory, but I didn't make this change either, just added a comnent about it.\n\nThe changes: \n- the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.\n- there was one situation in which the temporary files stored in `tmpfiles` needed to be deleted but weren't; this was the case before any of the patches.\n- there are now messages printed about the doctesting directory, and then deleting it at the end.",
    "created_at": "2011-08-13T01:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95290",
    "user": "jhpalmieri"
}
```

Here is a patch based on Mitesh's; the "delta" patch shows the changes; these changes include your in-line patch.  This does not change SAGE_TESTDIR to `tempfile.gettempdir()`: we store timing information in this directory, so it should not be temporary.  It might be a good idea to change `TMP` (as used in `sage-ptest`) to a temporary directory, but I didn't make this change either, just added a comnent about it.

The changes: 
- the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.
- there was one situation in which the temporary files stored in `tmpfiles` needed to be deleted but weren't; this was the case before any of the patches.
- there are now messages printed about the doctesting directory, and then deleting it at the end.



---

archive/issue_comments_095291.json:
```json
{
    "body": "Oh, I forgot: I tested this with some non-library code, and it mostly worked.  I say \"mostly\" because when I set `SAGE_CHECK=yes` and installed the package at #9894, a bunch of files produced errors.  I got the following odd behavior:\n\n- before applying the patch, after spkg-check ran, it said that maybe a dozen files gave errors, but only 4 of them remained in `SAGE_TESTDIR` (4 of them, plus their `.pyc` files, plus their `.doctest...` files).\n\n- after applying the patch: for the dozen files which gave errors, all of them remained in `SAGE_TESTDIR`, plus their `.pyc` files, plus only 4 of the `doctest...` files \u2014 the ones corresponding to the same 4 files as in the first case.\n\nI don't know what's going on here.  The spkg-check script is not a completely straightforward program; it doesn't just run \"sage -tp\" on some directory.  So that may cause some of the issues.  Anyway, there are better results after applying the patch than before, but it's still not perfect.\n\nFor all of my other tests with non-library code, it worked just the way it should.",
    "created_at": "2011-08-13T01:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95291",
    "user": "jhpalmieri"
}
```

Oh, I forgot: I tested this with some non-library code, and it mostly worked.  I say "mostly" because when I set `SAGE_CHECK=yes` and installed the package at #9894, a bunch of files produced errors.  I got the following odd behavior:

- before applying the patch, after spkg-check ran, it said that maybe a dozen files gave errors, but only 4 of them remained in `SAGE_TESTDIR` (4 of them, plus their `.pyc` files, plus their `.doctest...` files).

- after applying the patch: for the dozen files which gave errors, all of them remained in `SAGE_TESTDIR`, plus their `.pyc` files, plus only 4 of the `doctest...` files — the ones corresponding to the same 4 files as in the first case.

I don't know what's going on here.  The spkg-check script is not a completely straightforward program; it doesn't just run "sage -tp" on some directory.  So that may cause some of the issues.  Anyway, there are better results after applying the patch than before, but it's still not perfect.

For all of my other tests with non-library code, it worked just the way it should.



---

archive/issue_comments_095292.json:
```json
{
    "body": "*Sorry, atm too tired to look at the whole, only a few remarks before I again forget them...*\n\nReplying to [comment:63 jhpalmieri]:\n> Here is a patch based on Mitesh's; the \"delta\" patch shows the changes; these changes include your in-line patch.\n\nNice, thanks. Even flushing the output.\n\n\n\n\n> This does not change SAGE_TESTDIR to `tempfile.gettempdir()`: we store timing information in this directory, so it should not be temporary.\n\nWho cares? ;-)\n\nThe odd thing with that is that we then again produce potential race conditions for the timing files. I think we'd have to use locking then (which can also cause headaches), perhaps on a follow-up.\n\nIMHO these files also shouldn't be \"hidden\", and could live in or below `DOT_SAGE` (if we have to use locking anyway). Moreover, they perhaps shouldn't get lost if one \"manually\" sets `SAGE_TESTDIR` to e.g. `/tmp`, which seems reasonable at least as long as we don't automatically use some presumably fast filesystem for the really temporary files. \n\n\n\n\n> It might be a good idea to change `TMP` (as used in `sage-ptest`) to a temporary directory, but I didn't make this change either, just added a comnent about it.\n\nOk, see above; at least documented.\n\n\n\n\n> The changes: \n\n>  - the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.\n\nThis doesn't help when simultaneously testing the same file from one `sage-ptest` instance (`SAGE_TEST_ITER`, `SAGE_TEST_GLOBAL_ITER`) if I'm not wrong; we could mangle **`sage-doctest`'s** PID into the *filename*, too, as I suggested above.\n\n\n\n\n>  - there are now messages printed about the doctesting directory, and then deleting it at the end.\n\nFor readability, I'd move the `print` statements (*\"Removing the directory ...\"*, which hopefully don't raise exceptions) out of the `try` block.\n\nAlso, `sage-ptest` should know whether tests failed (or doctesting was interrupted), in which case we don't have to issue a warning since keeping the failed doctest files is intentional (and the left files should have been mentioned in previous messages).\n\nSo I wouldn't try to remove the directory if any doctests failed, unless they were [all] interrupted by Ctrl-C (in which case `sage-doctest` should immediately remove all temporary files belonging to the aborted doctest, which it currently doesn't).\n\n----\n\nBtw., unrelated to *this* ticket: `sage-doctest` shouldn't sleep for 0.1 seconds (and not continually poll the state of the child process) if the timeout is in seconds anyway; instead, it should use `signal.alarm()` and `wait()`.",
    "created_at": "2011-08-13T04:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95292",
    "user": "leif"
}
```

*Sorry, atm too tired to look at the whole, only a few remarks before I again forget them...*

Replying to [comment:63 jhpalmieri]:
> Here is a patch based on Mitesh's; the "delta" patch shows the changes; these changes include your in-line patch.

Nice, thanks. Even flushing the output.




> This does not change SAGE_TESTDIR to `tempfile.gettempdir()`: we store timing information in this directory, so it should not be temporary.

Who cares? ;-)

The odd thing with that is that we then again produce potential race conditions for the timing files. I think we'd have to use locking then (which can also cause headaches), perhaps on a follow-up.

IMHO these files also shouldn't be "hidden", and could live in or below `DOT_SAGE` (if we have to use locking anyway). Moreover, they perhaps shouldn't get lost if one "manually" sets `SAGE_TESTDIR` to e.g. `/tmp`, which seems reasonable at least as long as we don't automatically use some presumably fast filesystem for the really temporary files. 




> It might be a good idea to change `TMP` (as used in `sage-ptest`) to a temporary directory, but I didn't make this change either, just added a comnent about it.

Ok, see above; at least documented.




> The changes: 

>  - the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.

This doesn't help when simultaneously testing the same file from one `sage-ptest` instance (`SAGE_TEST_ITER`, `SAGE_TEST_GLOBAL_ITER`) if I'm not wrong; we could mangle **`sage-doctest`'s** PID into the *filename*, too, as I suggested above.




>  - there are now messages printed about the doctesting directory, and then deleting it at the end.

For readability, I'd move the `print` statements (*"Removing the directory ..."*, which hopefully don't raise exceptions) out of the `try` block.

Also, `sage-ptest` should know whether tests failed (or doctesting was interrupted), in which case we don't have to issue a warning since keeping the failed doctest files is intentional (and the left files should have been mentioned in previous messages).

So I wouldn't try to remove the directory if any doctests failed, unless they were [all] interrupted by Ctrl-C (in which case `sage-doctest` should immediately remove all temporary files belonging to the aborted doctest, which it currently doesn't).

----

Btw., unrelated to *this* ticket: `sage-doctest` shouldn't sleep for 0.1 seconds (and not continually poll the state of the child process) if the timeout is in seconds anyway; instead, it should use `signal.alarm()` and `wait()`.



---

archive/issue_comments_095293.json:
```json
{
    "body": "Replying to [comment:65 leif]:\n\n> > This does not change SAGE_TESTDIR to `tempfile.gettempdir()`: we store timing information in this directory, so it should not be temporary.\n> \n> Who cares? ;-)\n\nWell, someone might...\n \n> The odd thing with that is that we then again produce potential race conditions for the timing files. I think we'd have to use locking then (which can also cause headaches), perhaps on a follow-up.\n\nTrue, theoretically, but I've never heard of this coming up.  I don't think these files are open for very long, so race conditions should be very rare.  I agree it should be dealt with on a follow-up, if at all.  (Instead of locking, we could perhaps use a \"try ... except\" block, since if two processes are trying to write to the same timing file, it's not a disaster if we just completely discard one of those.)\n\n> IMHO these files also shouldn't be \"hidden\", and could live in or below `DOT_SAGE`\n\nI thought about this when working on the most recent patch, but it was too much work for too little gain to make it backwards compatible (if `.ptest_timing...` exists, then read it, otherwise, look for `ptest_timing...`, etc.).  It could be done on another ticket.\n\n>  (if we have to use locking anyway). Moreover, they perhaps shouldn't get lost if one \"manually\" sets `SAGE_TESTDIR` to e.g. `/tmp`, which seems reasonable at least as long as we don't automatically use some presumably fast filesystem for the really temporary files. \n\nThat's a good point.\n\n> > The changes: \n\n> >  - the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.\n> \n> This doesn't help when simultaneously testing the same file from one `sage-ptest` instance (`SAGE_TEST_ITER`, `SAGE_TEST_GLOBAL_ITER`) if I'm not wrong; we could mangle **`sage-doctest`'s** PID into the *filename*, too, as I suggested above.\n\nI can do that, or we can use `mkstemp` instead of or in addition to the path.  Opinions either way?\n\n> >  - there are now messages printed about the doctesting directory, and then deleting it at the end.\n> \n> For readability, I'd move the `print` statements (*\"Removing the directory ...\"*, which hopefully don't raise exceptions) out of the `try` block.\n\nOkay.\n\n> Also, `sage-ptest` should know whether tests failed (or doctesting was interrupted), in which case we don't have to issue a warning since keeping the failed doctest files is intentional (and the left files should have been mentioned in previous messages).\n> \n> So I wouldn't try to remove the directory if any doctests failed, unless they were [all] interrupted by Ctrl-C (in which case `sage-doctest` should immediately remove all temporary files belonging to the aborted doctest, which it currently doesn't).\n\nPerhaps it should, but that should be on another ticket.  As Dave said earlier, \"a sub-optimal solution is a better temporary measure than a complete industrial strength bullet-proof solution\".  I don't want to have to deal with the inner workings of doctesting here any more than is necessary, and I don't think this particular issue is necessary to deal with for this ticket.  I can add a comment to the code about this.",
    "created_at": "2011-08-13T17:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95293",
    "user": "jhpalmieri"
}
```

Replying to [comment:65 leif]:

> > This does not change SAGE_TESTDIR to `tempfile.gettempdir()`: we store timing information in this directory, so it should not be temporary.
> 
> Who cares? ;-)

Well, someone might...
 
> The odd thing with that is that we then again produce potential race conditions for the timing files. I think we'd have to use locking then (which can also cause headaches), perhaps on a follow-up.

True, theoretically, but I've never heard of this coming up.  I don't think these files are open for very long, so race conditions should be very rare.  I agree it should be dealt with on a follow-up, if at all.  (Instead of locking, we could perhaps use a "try ... except" block, since if two processes are trying to write to the same timing file, it's not a disaster if we just completely discard one of those.)

> IMHO these files also shouldn't be "hidden", and could live in or below `DOT_SAGE`

I thought about this when working on the most recent patch, but it was too much work for too little gain to make it backwards compatible (if `.ptest_timing...` exists, then read it, otherwise, look for `ptest_timing...`, etc.).  It could be done on another ticket.

>  (if we have to use locking anyway). Moreover, they perhaps shouldn't get lost if one "manually" sets `SAGE_TESTDIR` to e.g. `/tmp`, which seems reasonable at least as long as we don't automatically use some presumably fast filesystem for the really temporary files. 

That's a good point.

> > The changes: 

> >  - the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.
> 
> This doesn't help when simultaneously testing the same file from one `sage-ptest` instance (`SAGE_TEST_ITER`, `SAGE_TEST_GLOBAL_ITER`) if I'm not wrong; we could mangle **`sage-doctest`'s** PID into the *filename*, too, as I suggested above.

I can do that, or we can use `mkstemp` instead of or in addition to the path.  Opinions either way?

> >  - there are now messages printed about the doctesting directory, and then deleting it at the end.
> 
> For readability, I'd move the `print` statements (*"Removing the directory ..."*, which hopefully don't raise exceptions) out of the `try` block.

Okay.

> Also, `sage-ptest` should know whether tests failed (or doctesting was interrupted), in which case we don't have to issue a warning since keeping the failed doctest files is intentional (and the left files should have been mentioned in previous messages).
> 
> So I wouldn't try to remove the directory if any doctests failed, unless they were [all] interrupted by Ctrl-C (in which case `sage-doctest` should immediately remove all temporary files belonging to the aborted doctest, which it currently doesn't).

Perhaps it should, but that should be on another ticket.  As Dave said earlier, "a sub-optimal solution is a better temporary measure than a complete industrial strength bullet-proof solution".  I don't want to have to deal with the inner workings of doctesting here any more than is necessary, and I don't think this particular issue is necessary to deal with for this ticket.  I can add a comment to the code about this.



---

archive/issue_comments_095294.json:
```json
{
    "body": "Replying to [comment:66 jhpalmieri]:\n> True, theoretically, but I've never heard of this coming up.  I don't think these files are open for very long, so race conditions should be very rare.  I agree it should be dealt with on a follow-up, if at all.  (Instead of locking, we could perhaps use a \"try ... except\" block, since if two processes are trying to write to the same timing file, it's not a disaster if we just completely discard one of those.)\n\nOk, I thought timings were accumulated; never looked at this.\n\n> I thought about this when working on the most recent patch, but it was too much work for too little gain to make it backwards compatible (if `.ptest_timing...` exists, then read it, otherwise, look for `ptest_timing...`, etc.).  It could be done on another ticket.\n\nI wouldn't care much about backward compatibility in this case.\n\n\n\n\n> > >  - the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.\n> > \n> > This doesn't help when simultaneously testing the same file from one `sage-ptest` instance (`SAGE_TEST_ITER`, `SAGE_TEST_GLOBAL_ITER`) if I'm not wrong; we could mangle **`sage-doctest`'s** PID into the *filename*, too, as I suggested above.\n> \n> I can do that, or we can use `mkstemp` instead of or in addition to the path.  Opinions either way?\n\nI'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].\n\n\n\n\n> > Also, `sage-ptest` should know whether tests failed (or doctesting was interrupted), in which case we don't have to issue a warning since keeping the failed doctest files is intentional (and the left files should have been mentioned in previous messages).\n> > \n\n> > So I wouldn't try to remove the directory if any doctests failed, unless they were [all] interrupted by Ctrl-C (in which case `sage-doctest` should immediately remove all temporary files belonging to the aborted doctest, which it currently doesn't).\n> \n> Perhaps it should, but that should be on another ticket.\n\nThe deletion upon Ctrl-C in `sage-doctest`; I just wouldn't try to remove the directory in `sage-ptest` if any error occurred (along with a perhaps confusing warning message).\n\n> \"complete industrial strength bullet-proof solution\"\n\nI don't think we'll ever reach this, also because the addition of new features will never stop. So Sage's version number won't converge.\n\n> I can add a comment to the code about this.\n\nI'd appreciate that, such that others can catch up. IMHO too much things end up in ticket comments hardly anybody will see or read later.",
    "created_at": "2011-08-13T18:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95294",
    "user": "leif"
}
```

Replying to [comment:66 jhpalmieri]:
> True, theoretically, but I've never heard of this coming up.  I don't think these files are open for very long, so race conditions should be very rare.  I agree it should be dealt with on a follow-up, if at all.  (Instead of locking, we could perhaps use a "try ... except" block, since if two processes are trying to write to the same timing file, it's not a disaster if we just completely discard one of those.)

Ok, I thought timings were accumulated; never looked at this.

> I thought about this when working on the most recent patch, but it was too much work for too little gain to make it backwards compatible (if `.ptest_timing...` exists, then read it, otherwise, look for `ptest_timing...`, etc.).  It could be done on another ticket.

I wouldn't care much about backward compatibility in this case.




> > >  - the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.
> > 
> > This doesn't help when simultaneously testing the same file from one `sage-ptest` instance (`SAGE_TEST_ITER`, `SAGE_TEST_GLOBAL_ITER`) if I'm not wrong; we could mangle **`sage-doctest`'s** PID into the *filename*, too, as I suggested above.
> 
> I can do that, or we can use `mkstemp` instead of or in addition to the path.  Opinions either way?

I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].




> > Also, `sage-ptest` should know whether tests failed (or doctesting was interrupted), in which case we don't have to issue a warning since keeping the failed doctest files is intentional (and the left files should have been mentioned in previous messages).
> > 

> > So I wouldn't try to remove the directory if any doctests failed, unless they were [all] interrupted by Ctrl-C (in which case `sage-doctest` should immediately remove all temporary files belonging to the aborted doctest, which it currently doesn't).
> 
> Perhaps it should, but that should be on another ticket.

The deletion upon Ctrl-C in `sage-doctest`; I just wouldn't try to remove the directory in `sage-ptest` if any error occurred (along with a perhaps confusing warning message).

> "complete industrial strength bullet-proof solution"

I don't think we'll ever reach this, also because the addition of new features will never stop. So Sage's version number won't converge.

> I can add a comment to the code about this.

I'd appreciate that, such that others can catch up. IMHO too much things end up in ticket comments hardly anybody will see or read later.



---

archive/issue_comments_095295.json:
```json
{
    "body": "Replying to [comment:67 leif]:\n> I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].\n\nDo we also need to add this PID to the output from `filename_mangler`, in case someone is doctesting the same file in the Sage library several times simultaneously?\n\nRegarding the timing files: I'm not touching that code, although I've added some comments.\n\nRegarding deleting files on interruption: it's not clear how to easily determine whether there was an error before the interruption \u2014 do you need to use `post_process`? \u2014 so I'm just adding some comments and not touching the code.",
    "created_at": "2011-08-13T20:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95295",
    "user": "jhpalmieri"
}
```

Replying to [comment:67 leif]:
> I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].

Do we also need to add this PID to the output from `filename_mangler`, in case someone is doctesting the same file in the Sage library several times simultaneously?

Regarding the timing files: I'm not touching that code, although I've added some comments.

Regarding deleting files on interruption: it's not clear how to easily determine whether there was an error before the interruption — do you need to use `post_process`? — so I'm just adding some comments and not touching the code.



---

archive/issue_comments_095296.json:
```json
{
    "body": "Attachment [trac_9739.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739.patch) by jhpalmieri created at 2011-08-13 20:55:27\n\nscripts repo",
    "created_at": "2011-08-13T20:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95296",
    "user": "jhpalmieri"
}
```

Attachment [trac_9739.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739.patch) by jhpalmieri created at 2011-08-13 20:55:27

scripts repo



---

archive/issue_comments_095297.json:
```json
{
    "body": "Replying to [comment:68 jhpalmieri]:\n> Replying to [comment:67 leif]:\n> > I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].\n> \n> Do we also need to add this PID to the output from `filename_mangler`, in case someone is doctesting the same file in the Sage library several times simultaneously?\n\nYes; you apparently already did so in the new patch.\n\nBut we actually don't have to mangle any path into the filename if we do that, since every file is tested by its own `sage-doctest` instance, in a directory unique to the host and the `sage-ptest` instance. [We'd have to do the same for `sage-test`, i.e., also create a unique directory there, perhaps on a follow-up, to also support simultaneous *sequential* testing on *different* hosts which share the same `$SAGE_TESTDIR` (from the perspective of `sage-[p]test`).]\n\n\n\n\n> Regarding the timing files: I'm not touching that code, although I've added some comments.\n\nOk.\n\n\n\n\n> Regarding deleting files on interruption: it's not clear how to easily determine whether there was an error before the interruption \u2014 do you need to use `post_process`? \u2014 so I'm just adding some comments and not touching the code.\n\nOk. I actually didn't think about doctest errors *in the same file* that may have occurred prior to interruption; it would IMHO be ok to just \"discard\" them, but we can decide on that on the corresponding follow-up.",
    "created_at": "2011-08-14T01:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95297",
    "user": "leif"
}
```

Replying to [comment:68 jhpalmieri]:
> Replying to [comment:67 leif]:
> > I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].
> 
> Do we also need to add this PID to the output from `filename_mangler`, in case someone is doctesting the same file in the Sage library several times simultaneously?

Yes; you apparently already did so in the new patch.

But we actually don't have to mangle any path into the filename if we do that, since every file is tested by its own `sage-doctest` instance, in a directory unique to the host and the `sage-ptest` instance. [We'd have to do the same for `sage-test`, i.e., also create a unique directory there, perhaps on a follow-up, to also support simultaneous *sequential* testing on *different* hosts which share the same `$SAGE_TESTDIR` (from the perspective of `sage-[p]test`).]




> Regarding the timing files: I'm not touching that code, although I've added some comments.

Ok.




> Regarding deleting files on interruption: it's not clear how to easily determine whether there was an error before the interruption — do you need to use `post_process`? — so I'm just adding some comments and not touching the code.

Ok. I actually didn't think about doctest errors *in the same file* that may have occurred prior to interruption; it would IMHO be ok to just "discard" them, but we can decide on that on the corresponding follow-up.



---

archive/issue_comments_095298.json:
```json
{
    "body": "P.S.: For future changes, could we do some versioning with the patch(es)?\n\nI meanwhile have a handful of tabs with different versions of the attached one and different deltas, losing track... ;-)",
    "created_at": "2011-08-14T01:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95298",
    "user": "leif"
}
```

P.S.: For future changes, could we do some versioning with the patch(es)?

I meanwhile have a handful of tabs with different versions of the attached one and different deltas, losing track... ;-)



---

archive/issue_comments_095299.json:
```json
{
    "body": "What still needs to be done here?\n\nReplying to [comment:70 leif]:\n> Replying to [comment:68 jhpalmieri]:\n> > Replying to [comment:67 leif]:\n> > > I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].\n> > \n> > Do we also need to add this PID to the output from `filename_mangler`, in case someone is doctesting the same file in the Sage library several times simultaneously?\n> \n> Yes; you apparently already did so in the new patch.\n> \n> But we actually don't have to mangle any path into the filename if we do that, since every file is tested by its own `sage-doctest` instance, in a directory unique to the host and the `sage-ptest` instance.\n\nI can remove the pathname from the mangling. If we're just adding the pid, I may discard the function `filename_mangler` and deal with it like this:\n\n```diff\n-        f = os.path.splitext(filename_mangler(file))[0] + '.py'\n+        f = os.path.join(SAGE_TESTDIR, \"doctest_%s_%s.py\" % (os.getpid(), name))\n```\n\n`filename_mangler` only gets used in this one place anyway.\n\n> > Regarding deleting files on interruption: it's not clear how to easily determine whether there was an error before the interruption \u2014 do you need to use `post_process`? \u2014 so I'm just adding some comments and not touching the code.\n> \n> Ok. I actually didn't think about doctest errors *in the same file* that may have occurred prior to interruption; it would IMHO be ok to just \"discard\" them, but we can decide on that on the corresponding follow-up.\n\nWell, some library files can take a long time to doctest, so I can imagine someone doctesting a file, seeing that it fails and then interrupting it, but wanting to keep the temporary file for some reason.  (As I said, I'm not planning on modifying this code anyway.)",
    "created_at": "2011-08-15T16:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95299",
    "user": "jhpalmieri"
}
```

What still needs to be done here?

Replying to [comment:70 leif]:
> Replying to [comment:68 jhpalmieri]:
> > Replying to [comment:67 leif]:
> > > I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].
> > 
> > Do we also need to add this PID to the output from `filename_mangler`, in case someone is doctesting the same file in the Sage library several times simultaneously?
> 
> Yes; you apparently already did so in the new patch.
> 
> But we actually don't have to mangle any path into the filename if we do that, since every file is tested by its own `sage-doctest` instance, in a directory unique to the host and the `sage-ptest` instance.

I can remove the pathname from the mangling. If we're just adding the pid, I may discard the function `filename_mangler` and deal with it like this:

```diff
-        f = os.path.splitext(filename_mangler(file))[0] + '.py'
+        f = os.path.join(SAGE_TESTDIR, "doctest_%s_%s.py" % (os.getpid(), name))
```

`filename_mangler` only gets used in this one place anyway.

> > Regarding deleting files on interruption: it's not clear how to easily determine whether there was an error before the interruption — do you need to use `post_process`? — so I'm just adding some comments and not touching the code.
> 
> Ok. I actually didn't think about doctest errors *in the same file* that may have occurred prior to interruption; it would IMHO be ok to just "discard" them, but we can decide on that on the corresponding follow-up.

Well, some library files can take a long time to doctest, so I can imagine someone doctesting a file, seeing that it fails and then interrupting it, but wanting to keep the temporary file for some reason.  (As I said, I'm not planning on modifying this code anyway.)



---

archive/issue_comments_095300.json:
```json
{
    "body": "Because, as mentioned, it currently can happen that doctests for a file `.../bar/foo` are reported to have passed successfully though actually `.../baz/foo` was tested.\n\nAfterwards rerunning (just) the tests for `.../baz/foo` (which in contrast were reported to have failed) won't show any errors, hiding possible doctest errors in `.../bar/foo`.",
    "created_at": "2011-09-10T18:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95300",
    "user": "leif"
}
```

Because, as mentioned, it currently can happen that doctests for a file `.../bar/foo` are reported to have passed successfully though actually `.../baz/foo` was tested.

Afterwards rerunning (just) the tests for `.../baz/foo` (which in contrast were reported to have failed) won't show any errors, hiding possible doctest errors in `.../bar/foo`.



---

archive/issue_comments_095301.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2011-09-10T18:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95301",
    "user": "leif"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_095302.json:
```json
{
    "body": "Replying to [comment:72 jhpalmieri]:\n> What still needs to be done here? \n\n> \n\n> Replying to [comment:70 leif]:\n> > Replying to [comment:68 jhpalmieri]:\n> > > Replying to [comment:67 leif]:\n> > > > I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].\n> I can remove the pathname from the mangling. If we're just adding the pid, I may discard the function `filename_mangler` and deal with it like this:\n\n```diff\n-        f = os.path.splitext(filename_mangler(file))[0] + '.py'\n+        f = os.path.join(SAGE_TESTDIR, \"doctest_%s_%s.py\" % (os.getpid(), name))\n```\n\n\nI'd prefer having the name first, then the PID; then we can also drop the `doctest_` prefix (because e.g. `1_module` is not a valid Python module name).\n\nI think this way it's easier to locate a file (with `ls` or some file manager), since the files will be in alphabetical order, sorted by their original name (as opposed to some random PIDs).",
    "created_at": "2011-09-10T18:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95302",
    "user": "leif"
}
```

Replying to [comment:72 jhpalmieri]:
> What still needs to be done here? 

> 

> Replying to [comment:70 leif]:
> > Replying to [comment:68 jhpalmieri]:
> > > Replying to [comment:67 leif]:
> > > > I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].
> I can remove the pathname from the mangling. If we're just adding the pid, I may discard the function `filename_mangler` and deal with it like this:

```diff
-        f = os.path.splitext(filename_mangler(file))[0] + '.py'
+        f = os.path.join(SAGE_TESTDIR, "doctest_%s_%s.py" % (os.getpid(), name))
```


I'd prefer having the name first, then the PID; then we can also drop the `doctest_` prefix (because e.g. `1_module` is not a valid Python module name).

I think this way it's easier to locate a file (with `ls` or some file manager), since the files will be in alphabetical order, sorted by their original name (as opposed to some random PIDs).



---

archive/issue_comments_095303.json:
```json
{
    "body": "Here are some new patches.  First, [attachment:trac_9739.v2.patch] and a \"delta\" patch [attachment:trac_9739-delta1to2.patch]: the differences from the previous version are\n\n- It changes how filenames are mangled: it uses \"NAME_PID.py\" instead of \"doctest_PID_NAME.py\" or whatever what there before.\n\n- I've decided that I agree with you: we shouldn't print the messages about removing the doctesting directory every time.  I've changed it so it only prints them if \"-verbose\" is one of the command-line options.  (This is overusing the \"-verbose\" option, I suppose, so we could instead could completely disable printing just by setting the variable \"verbose\" in sage-ptest to be False always.)  If the directory is not deleted at the end, then a message is printed regardless of verbosity settings.\n\nAlong these lines, we have [attachment:trac_9739-graphviz.patch], a patch for the main Sage library, which writes a temporary file to SAGE_TMP rather than to SAGE_TESTDIR, so that the doctesting directory is indeed empty after doctesting the Sage library.",
    "created_at": "2011-09-10T20:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95303",
    "user": "jhpalmieri"
}
```

Here are some new patches.  First, [attachment:trac_9739.v2.patch] and a "delta" patch [attachment:trac_9739-delta1to2.patch]: the differences from the previous version are

- It changes how filenames are mangled: it uses "NAME_PID.py" instead of "doctest_PID_NAME.py" or whatever what there before.

- I've decided that I agree with you: we shouldn't print the messages about removing the doctesting directory every time.  I've changed it so it only prints them if "-verbose" is one of the command-line options.  (This is overusing the "-verbose" option, I suppose, so we could instead could completely disable printing just by setting the variable "verbose" in sage-ptest to be False always.)  If the directory is not deleted at the end, then a message is printed regardless of verbosity settings.

Along these lines, we have [attachment:trac_9739-graphviz.patch], a patch for the main Sage library, which writes a temporary file to SAGE_TMP rather than to SAGE_TESTDIR, so that the doctesting directory is indeed empty after doctesting the Sage library.



---

archive/issue_comments_095304.json:
```json
{
    "body": "Attachment [trac_9739-delta1to2.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739-delta1to2.patch) by jhpalmieri created at 2011-09-10 20:59:59\n\nfor review only",
    "created_at": "2011-09-10T20:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95304",
    "user": "jhpalmieri"
}
```

Attachment [trac_9739-delta1to2.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739-delta1to2.patch) by jhpalmieri created at 2011-09-10 20:59:59

for review only



---

archive/issue_comments_095305.json:
```json
{
    "body": "main Sage library repo",
    "created_at": "2011-09-10T21:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95305",
    "user": "jhpalmieri"
}
```

main Sage library repo



---

archive/issue_comments_095306.json:
```json
{
    "body": "Attachment [trac_9739-graphviz.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739-graphviz.patch) by leif created at 2011-09-10 22:56:19\n\nReplying to [comment:75 jhpalmieri]:\n> Along these lines, we have [attachment:trac_9739-graphviz.patch], a patch for the main Sage library, which writes a temporary file to SAGE_TMP rather than to SAGE_TESTDIR, so that the doctesting directory is indeed empty after doctesting the Sage library.\n\nShouldn't doctests delete the files they create afterwards anyway?",
    "created_at": "2011-09-10T22:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95306",
    "user": "leif"
}
```

Attachment [trac_9739-graphviz.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739-graphviz.patch) by leif created at 2011-09-10 22:56:19

Replying to [comment:75 jhpalmieri]:
> Along these lines, we have [attachment:trac_9739-graphviz.patch], a patch for the main Sage library, which writes a temporary file to SAGE_TMP rather than to SAGE_TESTDIR, so that the doctesting directory is indeed empty after doctesting the Sage library.

Shouldn't doctests delete the files they create afterwards anyway?



---

archive/issue_comments_095307.json:
```json
{
    "body": "Some minor things:\n\n* `\"%s\" % os.getpid()` works, but in principle it should use `\"%d\"`.\n* I think we should also (already) support the proper long option format, `--verbose`, there.\n* I would omit the \"*Warning:*\" in case (we know that) doctest errors occurred, since it is the desired behaviour to keep at least the failing files in that case. \n\n  We *could* also list the contents of the directory there (\"*The following files have been kept [because of doctest errors]: ...*\"). (In principle we also would have to relate them back to their original files, to remove the ambiguity this ticket is all about.)",
    "created_at": "2011-09-10T23:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95307",
    "user": "leif"
}
```

Some minor things:

* `"%s" % os.getpid()` works, but in principle it should use `"%d"`.
* I think we should also (already) support the proper long option format, `--verbose`, there.
* I would omit the "*Warning:*" in case (we know that) doctest errors occurred, since it is the desired behaviour to keep at least the failing files in that case. 

  We *could* also list the contents of the directory there ("*The following files have been kept [because of doctest errors]: ...*"). (In principle we also would have to relate them back to their original files, to remove the ambiguity this ticket is all about.)



---

archive/issue_comments_095308.json:
```json
{
    "body": "> Shouldn't doctests delete the files they create afterwards anyway?\n\nExamples in Sage code can create files anywhere in the filesystem, but they *should* only create temporary files or delete files after they're finished with them.  The directory SAGE_TMP gets cleaned up automatically, so it's a good choice, as opposed to SAGE_TESTDIR.\n\nReplying to [comment:77 leif]:\n> Some minor things:\n> \n>  * `\"%s\" % os.getpid()` works, but in principle it should use `\"%d\"`.\n\nOkay. We seem to have used \"%d\" elsewhere in the file, not sure why I didn't this time.\n\n>  * I think we should also (already) support the proper long option format, `--verbose`, there.\n\nOh, right, I misunderstood `opts`: I thought it was just the string of options instead of a list.\n\n>  * I would omit the \"*Warning:*\" in case (we know that) doctest errors occurred, since it is the desired behaviour to keep at least the failing files in that case. \n\n\nOkay.\n\n>    We *could* also list the contents of the directory there (\"*The following files have been kept [because of doctest errors]: ...*\"). (In principle we also would have to relate them back to their original files, to remove the ambiguity this ticket is all about.)\n\nLooks like an enhancement for another ticket.\n\nI don't think it's worth making a \"v3\" patch out of this.  Here's the difference between the previous v2 patch and this one:\n\n```diff\ndiff --git a/sage-doctest b/sage-doctest\n--- a/sage-doctest\n+++ b/sage-doctest\n@@ -644,7 +644,7 @@ def test_file(file, library_code):\n \n         name = os.path.basename(file)\n         name = name[:name.find(\".\")]\n-        f = os.path.join(SAGE_TESTDIR, \"%s_%s.py\" % (name, os.getpid()))\n+        f = os.path.join(SAGE_TESTDIR, \"%s_%d.py\" % (name, os.getpid()))\n \n         open(f,\"w\").write(s)\n         tmpfiles.append(f)\ndiff --git a/sage-ptest b/sage-ptest\n--- a/sage-ptest\n+++ b/sage-ptest\n@@ -295,7 +295,7 @@ for gr in range(0,numglobaliteration):\n \n         infiles.append(os.path.join(sagenb_loc, 'sagenb'))\n \n-    verbose = '-verbose' in opts\n+    verbose = ('-verbose' in opts or '--verbose' in opts)\n \n     if numthreads == 0:\n         # Set numthreads to be the number of processors, with a default\n@@ -430,7 +430,7 @@ for gr in range(0,numglobaliteration):\n         # TODO (probably in sage-doctest): if tests were interrupted\n         # but there were no failures in the interrupted files, delete\n         # the temporary files, so that this directory is empty.\n-        print \"Warning: the temporary doctesting directory\"\n+        print \"The temporary doctesting directory\"\n         print \"   %s\" % TMP\n         print \"was not removed: it is not empty, probably because doctesting\"\n         print \"failed or was interrupted.\"\n```\n",
    "created_at": "2011-09-10T23:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95308",
    "user": "jhpalmieri"
}
```

> Shouldn't doctests delete the files they create afterwards anyway?

Examples in Sage code can create files anywhere in the filesystem, but they *should* only create temporary files or delete files after they're finished with them.  The directory SAGE_TMP gets cleaned up automatically, so it's a good choice, as opposed to SAGE_TESTDIR.

Replying to [comment:77 leif]:
> Some minor things:
> 
>  * `"%s" % os.getpid()` works, but in principle it should use `"%d"`.

Okay. We seem to have used "%d" elsewhere in the file, not sure why I didn't this time.

>  * I think we should also (already) support the proper long option format, `--verbose`, there.

Oh, right, I misunderstood `opts`: I thought it was just the string of options instead of a list.

>  * I would omit the "*Warning:*" in case (we know that) doctest errors occurred, since it is the desired behaviour to keep at least the failing files in that case. 


Okay.

>    We *could* also list the contents of the directory there ("*The following files have been kept [because of doctest errors]: ...*"). (In principle we also would have to relate them back to their original files, to remove the ambiguity this ticket is all about.)

Looks like an enhancement for another ticket.

I don't think it's worth making a "v3" patch out of this.  Here's the difference between the previous v2 patch and this one:

```diff
diff --git a/sage-doctest b/sage-doctest
--- a/sage-doctest
+++ b/sage-doctest
@@ -644,7 +644,7 @@ def test_file(file, library_code):
 
         name = os.path.basename(file)
         name = name[:name.find(".")]
-        f = os.path.join(SAGE_TESTDIR, "%s_%s.py" % (name, os.getpid()))
+        f = os.path.join(SAGE_TESTDIR, "%s_%d.py" % (name, os.getpid()))
 
         open(f,"w").write(s)
         tmpfiles.append(f)
diff --git a/sage-ptest b/sage-ptest
--- a/sage-ptest
+++ b/sage-ptest
@@ -295,7 +295,7 @@ for gr in range(0,numglobaliteration):
 
         infiles.append(os.path.join(sagenb_loc, 'sagenb'))
 
-    verbose = '-verbose' in opts
+    verbose = ('-verbose' in opts or '--verbose' in opts)
 
     if numthreads == 0:
         # Set numthreads to be the number of processors, with a default
@@ -430,7 +430,7 @@ for gr in range(0,numglobaliteration):
         # TODO (probably in sage-doctest): if tests were interrupted
         # but there were no failures in the interrupted files, delete
         # the temporary files, so that this directory is empty.
-        print "Warning: the temporary doctesting directory"
+        print "The temporary doctesting directory"
         print "   %s" % TMP
         print "was not removed: it is not empty, probably because doctesting"
         print "failed or was interrupted."
```




---

archive/issue_comments_095309.json:
```json
{
    "body": "Attachment [trac_9739.v2.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739.v2.patch) by jhpalmieri created at 2011-09-10 23:31:29\n\nscripts repo",
    "created_at": "2011-09-10T23:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95309",
    "user": "jhpalmieri"
}
```

Attachment [trac_9739.v2.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739.v2.patch) by jhpalmieri created at 2011-09-10 23:31:29

scripts repo



---

archive/issue_comments_095310.json:
```json
{
    "body": "Replying to [comment:78 jhpalmieri]:\n> >    We *could* also list the contents of the directory there (\"*The following files have been kept [because of doctest errors]: ...*\"). (In principle we also would have to relate them back to their original files, to remove the ambiguity this ticket is all about.)\n> \n> Looks like an enhancement for another ticket.\n\nOk. Just in case you were bored... Btw, it wouldn't be bad to put the full path of the original file into a comment of the generated doctest file either.\n\n> I don't think it's worth making a \"v3\" patch out of this.  Here's the difference between the previous v2 patch and this one ...\n\nOk.",
    "created_at": "2011-09-10T23:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95310",
    "user": "leif"
}
```

Replying to [comment:78 jhpalmieri]:
> >    We *could* also list the contents of the directory there ("*The following files have been kept [because of doctest errors]: ...*"). (In principle we also would have to relate them back to their original files, to remove the ambiguity this ticket is all about.)
> 
> Looks like an enhancement for another ticket.

Ok. Just in case you were bored... Btw, it wouldn't be bad to put the full path of the original file into a comment of the generated doctest file either.

> I don't think it's worth making a "v3" patch out of this.  Here's the difference between the previous v2 patch and this one ...

Ok.



---

archive/issue_comments_095311.json:
```json
{
    "body": "... although I'd say\n   *\"... **presumably** because doctest**s** failed or **doctesting** was interrupted\"*.",
    "created_at": "2011-09-10T23:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95311",
    "user": "leif"
}
```

... although I'd say
   *"... **presumably** because doctest**s** failed or **doctesting** was interrupted"*.



---

archive/issue_comments_095312.json:
```json
{
    "body": "Okay, here is a v3 patch with cumulative changes from the original v2 patch in the corresponding delta patch; thus you can get from the original patch to the v3 patch by applying the two delta patches.\n\nI added the path of the original file to the doctest file, but did nothing about listing files in the directory.  (It should be clear from other messages what the files are -- they should correspond to doctest failures -- and people can also just `ls` the directory.  The current message is there just to alert people to the fact that their `.sage` directory (by default) is possibly being polluted with some things which could be cleaned up if desired, so just printing the directory name is good enough.)",
    "created_at": "2011-09-11T01:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95312",
    "user": "jhpalmieri"
}
```

Okay, here is a v3 patch with cumulative changes from the original v2 patch in the corresponding delta patch; thus you can get from the original patch to the v3 patch by applying the two delta patches.

I added the path of the original file to the doctest file, but did nothing about listing files in the directory.  (It should be clear from other messages what the files are -- they should correspond to doctest failures -- and people can also just `ls` the directory.  The current message is there just to alert people to the fact that their `.sage` directory (by default) is possibly being polluted with some things which could be cleaned up if desired, so just printing the directory name is good enough.)



---

archive/issue_comments_095313.json:
```json
{
    "body": "Attachment [trac_9739-delta2to3.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739-delta2to3.patch) by jhpalmieri created at 2011-09-11 01:15:14\n\nfor review only",
    "created_at": "2011-09-11T01:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95313",
    "user": "jhpalmieri"
}
```

Attachment [trac_9739-delta2to3.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739-delta2to3.patch) by jhpalmieri created at 2011-09-11 01:15:14

for review only



---

archive/issue_comments_095314.json:
```json
{
    "body": "scripts repo",
    "created_at": "2011-09-11T01:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95314",
    "user": "jhpalmieri"
}
```

scripts repo



---

archive/issue_comments_095315.json:
```json
{
    "body": "Attachment [trac_9739.v3.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739.v3.patch) by jhpalmieri created at 2011-09-11 01:15:34",
    "created_at": "2011-09-11T01:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95315",
    "user": "jhpalmieri"
}
```

Attachment [trac_9739.v3.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739.v3.patch) by jhpalmieri created at 2011-09-11 01:15:34



---

archive/issue_comments_095316.json:
```json
{
    "body": "I think we should create the same temporary directory (`$SAGE_TESTDIR/$hostname-$pid`) in `sage-test` as well (on this ticket), and export this in `SAGE_TESTDIR` for `sage-doctest`.\n\nAlso wouldn't be bad to put such common code into a separate module, before we \"unify\" (or unite) `sage-test` and `sage-ptest`.",
    "created_at": "2011-09-11T01:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95316",
    "user": "leif"
}
```

I think we should create the same temporary directory (`$SAGE_TESTDIR/$hostname-$pid`) in `sage-test` as well (on this ticket), and export this in `SAGE_TESTDIR` for `sage-doctest`.

Also wouldn't be bad to put such common code into a separate module, before we "unify" (or unite) `sage-test` and `sage-ptest`.



---

archive/issue_comments_095317.json:
```json
{
    "body": "Sorry, missed your updates. Now I can't provide a reviewer patch... :)\n\nWonderful:\n\n```\n/tmp/leif/home/.sage/tmp/redhawk-16925:\ntotal 300\n-rw-r--r-- 1 leif leif  2398 2011-09-10 18:45 algebra_18699.py\n-rw-r--r-- 1 leif leif  2422 2011-09-10 18:45 algebras_18570.py\n-rw-r--r-- 1 leif leif  2441 2011-09-10 18:45 arithgroup_18497.py\n-rw-r--r-- 1 leif leif 14054 2011-09-10 18:45 branching_rules_17653.py\n-rw-r--r-- 1 leif leif  2052 2011-09-10 18:45 cmd_18353.py\n-rw-r--r-- 1 leif leif 14762 2011-09-10 18:45 coercion_18657.py\n-rw-r--r-- 1 leif leif  2454 2011-09-10 18:45 crystals_18792.py\n-rw-r--r-- 1 leif leif  2231 2011-09-10 18:45 databases_18494.py\n-rw-r--r-- 1 leif leif  2200 2011-09-10 18:45 designs_18697.py\n-rw-r--r-- 1 leif leif  2352 2011-09-10 18:45 developer_18793.py\n-rw-r--r-- 1 leif leif  2301 2011-09-10 18:45 functions_18457.py\n-rw-r--r-- 1 leif leif 25616 2011-09-10 18:45 group_theory_17619.py\n-rw-r--r-- 1 leif leif  2320 2011-09-10 18:45 hecke_18619.py\n-rw-r--r-- 1 leif leif  2422 2011-09-10 18:45 homology_18513.py\n-rw-r--r-- 1 leif leif  2252 2011-09-10 18:45 iet_18686.py\n\n-rw-r--r-- 1 leif leif  6279 2011-09-10 18:45 index_17344.py\n-rw-r--r-- 1 leif leif  3478 2011-09-10 18:45 index_18779.py\n\n-rw-r--r-- 1 leif leif  3556 2011-09-10 18:45 kazhdan_lusztig_polynomials_17696.py\n-rw-r--r-- 1 leif leif  2425 2011-09-10 18:45 modabvar_18649.py\n-rw-r--r-- 1 leif leif  2498 2011-09-10 18:45 modsym_18633.py\n-rw-r--r-- 1 leif leif  2075 2011-09-10 18:45 networking_18398.py\n-rw-r--r-- 1 leif leif  2130 2011-09-10 18:45 numerical_18660.py\n-rw-r--r-- 1 leif leif  3142 2011-09-10 18:45 padics_18685.py\n-rw-r--r-- 1 leif leif  2182 2011-09-10 18:45 parallel_18621.py\n-rw-r--r-- 1 leif leif  2444 2011-09-10 18:45 plot3d_18453.py\n-rw-r--r-- 1 leif leif  2391 2011-09-10 18:45 polynomial_rings_18651.py\n-rw-r--r-- 1 leif leif  2301 2011-09-10 18:45 polynomial_rings_infinite_18371.py\n-rw-r--r-- 1 leif leif  2784 2011-09-10 18:45 polynomial_rings_univar_18551.py\n-rw-r--r-- 1 leif leif  2259 2011-09-10 18:45 posets_18828.py\n-rw-r--r-- 1 leif leif  2324 2011-09-10 18:45 power_series_18638.py\n-rw-r--r-- 1 leif leif  2127 2011-09-10 18:45 probability_18369.py\n-rw-r--r-- 1 leif leif  2303 2011-09-10 18:45 quadratic_forms_18675.py\n-rw-r--r-- 1 leif leif  2159 2011-09-10 18:45 quat_algebras_18571.py\n-rw-r--r-- 1 leif leif  2413 2011-09-10 18:45 root_systems_18706.py\n-rw-r--r-- 1 leif leif  2100 2011-09-10 18:45 semirings_18493.py\n-rw-r--r-- 1 leif leif  2146 2011-09-10 18:45 species_18786.py\n-rw-r--r-- 1 leif leif  2179 2011-09-10 18:45 stats_18647.py\n-rw-r--r-- 1 leif leif  2668 2011-09-10 18:45 symmetric_functions_18691.py\n-rw-r--r-- 1 leif leif  2201 2011-09-10 18:45 tableaux_18773.py\n-rw-r--r-- 1 leif leif  2025 2011-09-10 18:45 todolist_18572.py\n-rw-r--r-- 1 leif leif 20114 2011-09-10 18:45 tour_advanced_17551.py\n-rw-r--r-- 1 leif leif  6039 2011-09-10 18:45 tour_groups_17418.py\n\n-rw-r--r-- 1 leif leif 11469 2011-09-10 18:44 tour_plotting_17181.py\n-rw-r--r-- 1 leif leif 11468 2011-09-10 18:45 tour_plotting_17372.py\n\n-rw-r--r-- 1 leif leif 17816 2011-09-10 18:45 weyl_character_ring_17672.py\n-rw-r--r-- 1 leif leif 10807 2011-09-10 18:45 weyl_groups_17663.py\n-rw-r--r-- 1 leif leif  2522 2011-09-10 18:45 words_18739.py\n```\n\n(Blank lines inserted.)",
    "created_at": "2011-09-11T01:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95317",
    "user": "leif"
}
```

Sorry, missed your updates. Now I can't provide a reviewer patch... :)

Wonderful:

```
/tmp/leif/home/.sage/tmp/redhawk-16925:
total 300
-rw-r--r-- 1 leif leif  2398 2011-09-10 18:45 algebra_18699.py
-rw-r--r-- 1 leif leif  2422 2011-09-10 18:45 algebras_18570.py
-rw-r--r-- 1 leif leif  2441 2011-09-10 18:45 arithgroup_18497.py
-rw-r--r-- 1 leif leif 14054 2011-09-10 18:45 branching_rules_17653.py
-rw-r--r-- 1 leif leif  2052 2011-09-10 18:45 cmd_18353.py
-rw-r--r-- 1 leif leif 14762 2011-09-10 18:45 coercion_18657.py
-rw-r--r-- 1 leif leif  2454 2011-09-10 18:45 crystals_18792.py
-rw-r--r-- 1 leif leif  2231 2011-09-10 18:45 databases_18494.py
-rw-r--r-- 1 leif leif  2200 2011-09-10 18:45 designs_18697.py
-rw-r--r-- 1 leif leif  2352 2011-09-10 18:45 developer_18793.py
-rw-r--r-- 1 leif leif  2301 2011-09-10 18:45 functions_18457.py
-rw-r--r-- 1 leif leif 25616 2011-09-10 18:45 group_theory_17619.py
-rw-r--r-- 1 leif leif  2320 2011-09-10 18:45 hecke_18619.py
-rw-r--r-- 1 leif leif  2422 2011-09-10 18:45 homology_18513.py
-rw-r--r-- 1 leif leif  2252 2011-09-10 18:45 iet_18686.py

-rw-r--r-- 1 leif leif  6279 2011-09-10 18:45 index_17344.py
-rw-r--r-- 1 leif leif  3478 2011-09-10 18:45 index_18779.py

-rw-r--r-- 1 leif leif  3556 2011-09-10 18:45 kazhdan_lusztig_polynomials_17696.py
-rw-r--r-- 1 leif leif  2425 2011-09-10 18:45 modabvar_18649.py
-rw-r--r-- 1 leif leif  2498 2011-09-10 18:45 modsym_18633.py
-rw-r--r-- 1 leif leif  2075 2011-09-10 18:45 networking_18398.py
-rw-r--r-- 1 leif leif  2130 2011-09-10 18:45 numerical_18660.py
-rw-r--r-- 1 leif leif  3142 2011-09-10 18:45 padics_18685.py
-rw-r--r-- 1 leif leif  2182 2011-09-10 18:45 parallel_18621.py
-rw-r--r-- 1 leif leif  2444 2011-09-10 18:45 plot3d_18453.py
-rw-r--r-- 1 leif leif  2391 2011-09-10 18:45 polynomial_rings_18651.py
-rw-r--r-- 1 leif leif  2301 2011-09-10 18:45 polynomial_rings_infinite_18371.py
-rw-r--r-- 1 leif leif  2784 2011-09-10 18:45 polynomial_rings_univar_18551.py
-rw-r--r-- 1 leif leif  2259 2011-09-10 18:45 posets_18828.py
-rw-r--r-- 1 leif leif  2324 2011-09-10 18:45 power_series_18638.py
-rw-r--r-- 1 leif leif  2127 2011-09-10 18:45 probability_18369.py
-rw-r--r-- 1 leif leif  2303 2011-09-10 18:45 quadratic_forms_18675.py
-rw-r--r-- 1 leif leif  2159 2011-09-10 18:45 quat_algebras_18571.py
-rw-r--r-- 1 leif leif  2413 2011-09-10 18:45 root_systems_18706.py
-rw-r--r-- 1 leif leif  2100 2011-09-10 18:45 semirings_18493.py
-rw-r--r-- 1 leif leif  2146 2011-09-10 18:45 species_18786.py
-rw-r--r-- 1 leif leif  2179 2011-09-10 18:45 stats_18647.py
-rw-r--r-- 1 leif leif  2668 2011-09-10 18:45 symmetric_functions_18691.py
-rw-r--r-- 1 leif leif  2201 2011-09-10 18:45 tableaux_18773.py
-rw-r--r-- 1 leif leif  2025 2011-09-10 18:45 todolist_18572.py
-rw-r--r-- 1 leif leif 20114 2011-09-10 18:45 tour_advanced_17551.py
-rw-r--r-- 1 leif leif  6039 2011-09-10 18:45 tour_groups_17418.py

-rw-r--r-- 1 leif leif 11469 2011-09-10 18:44 tour_plotting_17181.py
-rw-r--r-- 1 leif leif 11468 2011-09-10 18:45 tour_plotting_17372.py

-rw-r--r-- 1 leif leif 17816 2011-09-10 18:45 weyl_character_ring_17672.py
-rw-r--r-- 1 leif leif 10807 2011-09-10 18:45 weyl_groups_17663.py
-rw-r--r-- 1 leif leif  2522 2011-09-10 18:45 words_18739.py
```

(Blank lines inserted.)



---

archive/issue_comments_095318.json:
```json
{
    "body": "Replying to [comment:83 leif]:\n> I think we should create the same temporary directory (`$SAGE_TESTDIR/$hostname-$pid`) in `sage-test` as well (on this ticket), and export this in `SAGE_TESTDIR` for `sage-doctest`.\n> \n> Also wouldn't be bad to put such common code into a separate module, before we \"unify\" (or unite) `sage-test` and `sage-ptest`.\n\nThese both sound like issues for #9224, not here.  I really don't want to add any more to this ticket unless there is an extremely good reason to do so.",
    "created_at": "2011-09-11T17:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95318",
    "user": "jhpalmieri"
}
```

Replying to [comment:83 leif]:
> I think we should create the same temporary directory (`$SAGE_TESTDIR/$hostname-$pid`) in `sage-test` as well (on this ticket), and export this in `SAGE_TESTDIR` for `sage-doctest`.
> 
> Also wouldn't be bad to put such common code into a separate module, before we "unify" (or unite) `sage-test` and `sage-ptest`.

These both sound like issues for #9224, not here.  I really don't want to add any more to this ticket unless there is an extremely good reason to do so.



---

archive/issue_comments_095319.json:
```json
{
    "body": "Sorry for the delay.\n\nI started testing the v2 yesterday, also with `make testlong`, which took ages, the latter unfortunately right before you made the v3, and later made a mistake when wanting to test v3, retesting v2 again... 8/\n\nI've now also tested v3, with both sequential doctests (since we've modified `sage-doctest`, but not yet `sage-test`, except for a comment), and parallel tests with up to 128 threads.\n\nI've reviewed the code already, so I can -- hopefully finally -- give this a **positive review**. (At least until something unexpected happens; I must admit I haven't tested the latest versions with non-library code yet.)\n\nThanks for spending so much time on this.\n\n\n\n\nReplying to [comment:85 jhpalmieri]:\n> Replying to [comment:83 leif]:\n> > I think we should create the same temporary directory (`$SAGE_TESTDIR/$hostname-$pid`) in `sage-test` as well (on this ticket), and export this in `SAGE_TESTDIR` for `sage-doctest`.\n> > \n> > Also wouldn't be bad to put such common code into a separate module, before we \"unify\" (or unite) `sage-test` and `sage-ptest`.\n> \n> These both sound like issues for #9224, not here.\n\nWell, Dave wanted this (the former), at least when we started here last year... ;-)\n\nI've added a comment there w.r.t. also using unique directories when testing sequentially, since there might be multiple instances running at the same time.\n\n\n\n\n> I really don't want to add any more to this ticket unless there is an extremely good reason to do so.\n\nOk, agreed. This ticket has really been dragging enough.\n\n\n\n\nBy the way, you were right; `opts` is a *string* (of the concatenated options) there, as opposed to a list of strings, so `\"-verbose\" in opts` would have been enough. But it works this way, too, and is IMHO nothing worth fixing again *here*.\n\nAlso, or on the other hand, I don't think anybody will ever use `--verbose` when doctesting in parallel, since the output would be totally messed up, unless one uses `sage -tp 1 ...` (or `make NUM_THREADS=1 ...`, which is also useful in some cases.",
    "created_at": "2011-09-11T19:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95319",
    "user": "leif"
}
```

Sorry for the delay.

I started testing the v2 yesterday, also with `make testlong`, which took ages, the latter unfortunately right before you made the v3, and later made a mistake when wanting to test v3, retesting v2 again... 8/

I've now also tested v3, with both sequential doctests (since we've modified `sage-doctest`, but not yet `sage-test`, except for a comment), and parallel tests with up to 128 threads.

I've reviewed the code already, so I can -- hopefully finally -- give this a **positive review**. (At least until something unexpected happens; I must admit I haven't tested the latest versions with non-library code yet.)

Thanks for spending so much time on this.




Replying to [comment:85 jhpalmieri]:
> Replying to [comment:83 leif]:
> > I think we should create the same temporary directory (`$SAGE_TESTDIR/$hostname-$pid`) in `sage-test` as well (on this ticket), and export this in `SAGE_TESTDIR` for `sage-doctest`.
> > 
> > Also wouldn't be bad to put such common code into a separate module, before we "unify" (or unite) `sage-test` and `sage-ptest`.
> 
> These both sound like issues for #9224, not here.

Well, Dave wanted this (the former), at least when we started here last year... ;-)

I've added a comment there w.r.t. also using unique directories when testing sequentially, since there might be multiple instances running at the same time.




> I really don't want to add any more to this ticket unless there is an extremely good reason to do so.

Ok, agreed. This ticket has really been dragging enough.




By the way, you were right; `opts` is a *string* (of the concatenated options) there, as opposed to a list of strings, so `"-verbose" in opts` would have been enough. But it works this way, too, and is IMHO nothing worth fixing again *here*.

Also, or on the other hand, I don't think anybody will ever use `--verbose` when doctesting in parallel, since the output would be totally messed up, unless one uses `sage -tp 1 ...` (or `make NUM_THREADS=1 ...`, which is also useful in some cases.



---

archive/issue_comments_095320.json:
```json
{
    "body": "Changing keywords from \"doctest scripts\" to \"doctest scripts race condition unique filenames ptestlong -tp\".",
    "created_at": "2011-09-11T19:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95320",
    "user": "leif"
}
```

Changing keywords from "doctest scripts" to "doctest scripts race condition unique filenames ptestlong -tp".



---

archive/issue_comments_095321.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-11T19:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95321",
    "user": "leif"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095322.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-12T18:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95322",
    "user": "leif"
}
```

Resolution: fixed



---

archive/issue_comments_095323.json:
```json
{
    "body": "Here's an add-on patch to fix the issues mentioned at #8708: testing non-library .py files is broken in two ways.",
    "created_at": "2011-09-28T00:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95323",
    "user": "jhpalmieri"
}
```

Here's an add-on patch to fix the issues mentioned at #8708: testing non-library .py files is broken in two ways.



---

archive/issue_comments_095324.json:
```json
{
    "body": "Could you reupload it with a matching commit message? ;-)",
    "created_at": "2011-09-28T00:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95324",
    "user": "leif"
}
```

Could you reupload it with a matching commit message? ;-)



---

archive/issue_comments_095325.json:
```json
{
    "body": "I knew we weren't really done with this ticket...",
    "created_at": "2011-09-28T01:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95325",
    "user": "jhpalmieri"
}
```

I knew we weren't really done with this ticket...



---

archive/issue_comments_095326.json:
```json
{
    "body": "I've attached your patch with a corrected commit message 6 seconds before you did. :D\n\nDeleting it again; thanks.\n\n\n\n\nI thought we were done, but it will break again as soon as others start to mess with how files are preparsed or their names...",
    "created_at": "2011-09-28T01:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95326",
    "user": "leif"
}
```

I've attached your patch with a corrected commit message 6 seconds before you did. :D

Deleting it again; thanks.




I thought we were done, but it will break again as soon as others start to mess with how files are preparsed or their names...



---

archive/issue_comments_095327.json:
```json
{
    "body": "Should the extra patch be put on a new ticket to make sure it gets reviewed and/or merged in the next alpha?  I'm a little concerned that it will get lost since it was attached to an already closed-and-merged ticket.",
    "created_at": "2011-10-03T19:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95327",
    "user": "jhpalmieri"
}
```

Should the extra patch be put on a new ticket to make sure it gets reviewed and/or merged in the next alpha?  I'm a little concerned that it will get lost since it was attached to an already closed-and-merged ticket.



---

archive/issue_comments_095328.json:
```json
{
    "body": "Replying to [comment:93 jhpalmieri]:\n> Should the extra patch be put on a new ticket\nAbsolutely, see #11893.  I deleted the patch here to remove confusion.",
    "created_at": "2011-10-03T19:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95328",
    "user": "jdemeyer"
}
```

Replying to [comment:93 jhpalmieri]:
> Should the extra patch be put on a new ticket
Absolutely, see #11893.  I deleted the patch here to remove confusion.



---

archive/issue_comments_095329.json:
```json
{
    "body": "Can somebody please review John's patch at #11893?",
    "created_at": "2011-10-03T19:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95329",
    "user": "jdemeyer"
}
```

Can somebody please review John's patch at #11893?



---

archive/issue_comments_095330.json:
```json
{
    "body": "Replying to [comment:94 jdemeyer]:\n> Replying to [comment:93 jhpalmieri]:\n> > Should the extra patch be put on a new ticket\n> Absolutely, see #11893.  I deleted the patch here to remove confusion.\n\nPlease reattach it; it is already merged!",
    "created_at": "2011-10-03T20:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95330",
    "user": "leif"
}
```

Replying to [comment:94 jdemeyer]:
> Replying to [comment:93 jhpalmieri]:
> > Should the extra patch be put on a new ticket
> Absolutely, see #11893.  I deleted the patch here to remove confusion.

Please reattach it; it is already merged!



---

archive/issue_comments_095331.json:
```json
{
    "body": "Replying to [comment:97 leif]:\n> Replying to [comment:94 jdemeyer]:\n> > Replying to [comment:93 jhpalmieri]:\n> > > Should the extra patch be put on a new ticket\n> > Absolutely, see #11893.  I deleted the patch here to remove confusion.\n> \n> Please reattach it; it is already merged!\n\nSee http://trac.sagemath.org/sage_trac/ticket/8708#comment:14 ff. for part of the discussion.",
    "created_at": "2011-10-03T20:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95331",
    "user": "leif"
}
```

Replying to [comment:97 leif]:
> Replying to [comment:94 jdemeyer]:
> > Replying to [comment:93 jhpalmieri]:
> > > Should the extra patch be put on a new ticket
> > Absolutely, see #11893.  I deleted the patch here to remove confusion.
> 
> Please reattach it; it is already merged!

See http://trac.sagemath.org/sage_trac/ticket/8708#comment:14 ff. for part of the discussion.



---

archive/issue_comments_095332.json:
```json
{
    "body": "It wasn't clear from this ticket that the patch had been merged: it was marked as merged and closed before the patch was attached, and I didn't check the actual log to see if it had been merged.  Sorry.",
    "created_at": "2011-10-03T20:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95332",
    "user": "jhpalmieri"
}
```

It wasn't clear from this ticket that the patch had been merged: it was marked as merged and closed before the patch was attached, and I didn't check the actual log to see if it had been merged.  Sorry.



---

archive/issue_comments_095333.json:
```json
{
    "body": "scripts repo; apply on top of other patch",
    "created_at": "2011-10-03T20:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95333",
    "user": "jhpalmieri"
}
```

scripts repo; apply on top of other patch



---

archive/issue_comments_095334.json:
```json
{
    "body": "Attachment [trac_9739-extra.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739-extra.patch) by leif created at 2011-10-03 20:34:49\n\nReplying to [comment:99 jhpalmieri]:\n> It wasn't clear from this ticket that the patch had been merged: it was marked as merged and closed before the patch was attached, and I didn't check the actual log to see if it had been merged.  Sorry.\n\nWell, I could have added a clarifying comment, although I thought it was clear from the context that it is indeed merged; otherwise I would have reopened the ticket or moved the patch to another one.",
    "created_at": "2011-10-03T20:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95334",
    "user": "leif"
}
```

Attachment [trac_9739-extra.patch](tarball://root/attachments/some-uuid/ticket9739/trac_9739-extra.patch) by leif created at 2011-10-03 20:34:49

Replying to [comment:99 jhpalmieri]:
> It wasn't clear from this ticket that the patch had been merged: it was marked as merged and closed before the patch was attached, and I didn't check the actual log to see if it had been merged.  Sorry.

Well, I could have added a clarifying comment, although I thought it was clear from the context that it is indeed merged; otherwise I would have reopened the ticket or moved the patch to another one.



---

archive/issue_comments_095335.json:
```json
{
    "body": "Sorry for the mess here, I jumped too quickly.  Unfortunately, my attempt to avoid confusion only created confusion.",
    "created_at": "2011-10-04T07:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9739#issuecomment-95335",
    "user": "jdemeyer"
}
```

Sorry for the mess here, I jumped too quickly.  Unfortunately, my attempt to avoid confusion only created confusion.
