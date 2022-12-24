# Issue 5814: %prun doesn't work in the notebook

archive/issues_005814.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5814\n\n",
    "created_at": "2009-04-17T21:50:36Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.9",
    "title": "%prun doesn't work in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5814",
    "user": "rlm"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/5814





---

archive/issue_comments_045654.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-04-18T07:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45654",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_045655.json:
```json
{
    "body": "I'm changing this to an enhancement.  It's not a bug that \"random\" ipython features don't work in the notebook.  There's no reason they should until they get implemented.\n\nThe prun functionality -- which is really the python profiler -- could be used in the notebook by people who know enough about how the profiler works under the hood.  %prun is just IPython's wrapper around Python's standard profiler to make it easier to use.",
    "created_at": "2009-04-18T07:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45655",
    "user": "was"
}
```

I'm changing this to an enhancement.  It's not a bug that "random" ipython features don't work in the notebook.  There's no reason they should until they get implemented.

The prun functionality -- which is really the python profiler -- could be used in the notebook by people who know enough about how the profiler works under the hood.  %prun is just IPython's wrapper around Python's standard profiler to make it easier to use.



---

archive/issue_comments_045656.json:
```json
{
    "body": "Here's a branch that implements this feature. Feedback appreciated!\n\nhttps://github.com/tkluck/sagenb/commits/support_prun",
    "created_at": "2012-08-07T14:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45656",
    "user": "tkluck"
}
```

Here's a branch that implements this feature. Feedback appreciated!

https://github.com/tkluck/sagenb/commits/support_prun



---

archive/issue_comments_045657.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-08-07T14:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45657",
    "user": "tkluck"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_045658.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-10T09:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45658",
    "user": "kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_045659.json:
```json
{
    "body": "Thanks, tkluck. I see you made a pull request at https://github.com/sagemath/sagenb/pull/91 . Please continue any review process there :)\n\nI'm marking this ticket as invalid.",
    "created_at": "2012-08-10T09:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45659",
    "user": "kini"
}
```

Thanks, tkluck. I see you made a pull request at https://github.com/sagemath/sagenb/pull/91 . Please continue any review process there :)

I'm marking this ticket as invalid.



---

archive/issue_comments_045660.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-08-15T07:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45660",
    "user": "jdemeyer"
}
```

Resolution: invalid



---

archive/issue_comments_045661.json:
```json
{
    "body": "Attachment [trac_5814_enable_prun_in_notebook.patch](tarball://root/attachments/some-uuid/ticket5814/trac_5814_enable_prun_in_notebook.patch) by tkluck created at 2012-09-05 12:58:16\n\nIt turns out that this does need to be tackled in the sage library itself. It is possible to add a `prun` object there, which will be automatically used without having to do any special handling in the notebook. I've closed my pull request for the notebook and am reopening this ticket.",
    "created_at": "2012-09-05T12:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45661",
    "user": "tkluck"
}
```

Attachment [trac_5814_enable_prun_in_notebook.patch](tarball://root/attachments/some-uuid/ticket5814/trac_5814_enable_prun_in_notebook.patch) by tkluck created at 2012-09-05 12:58:16

It turns out that this does need to be tackled in the sage library itself. It is possible to add a `prun` object there, which will be automatically used without having to do any special handling in the notebook. I've closed my pull request for the notebook and am reopening this ticket.



---

archive/issue_comments_045662.json:
```json
{
    "body": "Changing assignee from boothby to tkluck.",
    "created_at": "2012-09-05T12:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45662",
    "user": "tkluck"
}
```

Changing assignee from boothby to tkluck.



---

archive/issue_comments_045663.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2012-09-11T11:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45663",
    "user": "jdemeyer"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_045664.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2012-09-11T11:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45664",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_045665.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-09-11T14:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45665",
    "user": "tkluck"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_045666.json:
```json
{
    "body": "Just wanting to make sure that this patch ready for review, there are a few people here at Sage Days 45 that would like this feature. (Also do you know someone who would have the expertise to do a full review?)\n\nMy quick comment is that you'll need to give doctests to your functions.\n\nThanks,\n\nTravis",
    "created_at": "2013-02-12T00:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45666",
    "user": "tscrim"
}
```

Just wanting to make sure that this patch ready for review, there are a few people here at Sage Days 45 that would like this feature. (Also do you know someone who would have the expertise to do a full review?)

My quick comment is that you'll need to give doctests to your functions.

Thanks,

Travis



---

archive/issue_comments_045667.json:
```json
{
    "body": "Attachment [trac_5814_add_doctests_to_prun_object.patch](tarball://root/attachments/some-uuid/ticket5814/trac_5814_add_doctests_to_prun_object.patch) by tkluck created at 2013-03-11 15:49:41",
    "created_at": "2013-03-11T15:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45667",
    "user": "tkluck"
}
```

Attachment [trac_5814_add_doctests_to_prun_object.patch](tarball://root/attachments/some-uuid/ticket5814/trac_5814_add_doctests_to_prun_object.patch) by tkluck created at 2013-03-11 15:49:41



---

archive/issue_comments_045668.json:
```json
{
    "body": "Thanks for your comment, Travis. I just added the doctests. I'm not sure whether any special expertise is necessary, so please go ahead and give this a try.",
    "created_at": "2013-03-11T15:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45668",
    "user": "tkluck"
}
```

Thanks for your comment, Travis. I just added the doctests. I'm not sure whether any special expertise is necessary, so please go ahead and give this a try.



---

archive/issue_comments_045669.json:
```json
{
    "body": "Attachment [trac_5814-prun_notebook-review-ts.patch](tarball://root/attachments/some-uuid/ticket5814/trac_5814-prun_notebook-review-ts.patch) by tscrim created at 2013-04-01 18:03:29",
    "created_at": "2013-04-01T18:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45669",
    "user": "tscrim"
}
```

Attachment [trac_5814-prun_notebook-review-ts.patch](tarball://root/attachments/some-uuid/ticket5814/trac_5814-prun_notebook-review-ts.patch) by tscrim created at 2013-04-01 18:03:29



---

archive/issue_comments_045670.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-01T18:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45670",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_045671.json:
```json
{
    "body": "Hey Timo,\n\nI've uploaded a small review patch which fixes the doctests and gives full coverage. Thank you for the patch.\n\nBest,\n\nTravis\n\n\n```\nsage -t ../misc/prun.py\n    [6 tests, 0.0 s]\n----------------------------------------------------------------------\nAll tests passed!\n----------------------------------------------------------------------\nTotal time for all tests: 0.2 seconds\n    cpu time: 0.0 seconds\n    cumulative wall time: 0.0 seconds\n```\n",
    "created_at": "2013-04-01T18:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45671",
    "user": "tscrim"
}
```

Hey Timo,

I've uploaded a small review patch which fixes the doctests and gives full coverage. Thank you for the patch.

Best,

Travis


```
sage -t ../misc/prun.py
    [6 tests, 0.0 s]
----------------------------------------------------------------------
All tests passed!
----------------------------------------------------------------------
Total time for all tests: 0.2 seconds
    cpu time: 0.0 seconds
    cumulative wall time: 0.0 seconds
```




---

archive/issue_comments_045672.json:
```json
{
    "body": "It's probably outside the scope of this ticket, but the *really* useful thing would be if `%prun ...` in the notebook would return an interactive browser for the `Stat` object that is returned by `cProfile().runctx(...)`. While a basic printout of profiling data gives some indication, one usually needs to dig around a little in the data to find what the real bottleneck is (see where most calls come from, switch between cumulative and proper time, etc.)\n\nWriting such a browser might be a nice exercise for a student who is interested in interface programming. I bet there are good profiler browsers around to get inspiration from.\n\nA tool I haven't used yet but looks like a decent effort is [runsnakerun](https://pypi.python.org/pypi/RunSnakeRun). Duplicating that effort for the sage notebook might not seem like such a smart idea. Perhaps we can make the tool more easily accessible from sage? Given that it uses wxPython that might not be so very easily done ... I ended up installing it using OS tools, meaning that I *have* to write the profile data to a file and analyse it separately.",
    "created_at": "2013-04-01T18:44:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45672",
    "user": "nbruin"
}
```

It's probably outside the scope of this ticket, but the *really* useful thing would be if `%prun ...` in the notebook would return an interactive browser for the `Stat` object that is returned by `cProfile().runctx(...)`. While a basic printout of profiling data gives some indication, one usually needs to dig around a little in the data to find what the real bottleneck is (see where most calls come from, switch between cumulative and proper time, etc.)

Writing such a browser might be a nice exercise for a student who is interested in interface programming. I bet there are good profiler browsers around to get inspiration from.

A tool I haven't used yet but looks like a decent effort is [runsnakerun](https://pypi.python.org/pypi/RunSnakeRun). Duplicating that effort for the sage notebook might not seem like such a smart idea. Perhaps we can make the tool more easily accessible from sage? Given that it uses wxPython that might not be so very easily done ... I ended up installing it using OS tools, meaning that I *have* to write the profile data to a file and analyse it separately.



---

archive/issue_comments_045673.json:
```json
{
    "body": "Replying to [comment:12 nbruin]:\n> It's probably outside the scope of this ticket, but the *really* useful thing would be if `%prun ...` in the notebook would return an interactive browser for the `Stat` object that is returned by `cProfile().runctx(...)`. While a basic printout of profiling data gives some indication, one usually needs to dig around a little in the data to find what the real bottleneck is (see where most calls come from, switch between cumulative and proper time, etc.)\n\n+1/2 since being able to read/interpret the raw data is a good skill to have IMO. However a graphical (or at least a tree structure) of the data is also very useful.\n> \n> Writing such a browser might be a nice exercise for a student who is interested in interface programming. I bet there are good profiler browsers around to get inspiration from.\n\n+1 here. I feel like we need a wiki page to keep a list of \"good student projects\"...\n\n> A tool I haven't used yet but looks like a decent effort is [runsnakerun](https://pypi.python.org/pypi/RunSnakeRun). Duplicating that effort for the sage notebook might not seem like such a smart idea. Perhaps we can make the tool more easily accessible from sage? Given that it uses wxPython that might not be so very easily done ... I ended up installing it using OS tools, meaning that I *have* to write the profile data to a file and analyse it separately.\n\nI've seen runsnakerun used in a few places (although I haven't used it myself), and instead of duplicating it in the notebook, perhaps we could link it into sage (notebook) as some type of package? Actually...perhaps what we should do is have a variable/function which calls your favorite profiler on the executed command(s), something like:\n\n```\n%profile\n2 + 2\n```\n",
    "created_at": "2013-04-03T12:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45673",
    "user": "tscrim"
}
```

Replying to [comment:12 nbruin]:
> It's probably outside the scope of this ticket, but the *really* useful thing would be if `%prun ...` in the notebook would return an interactive browser for the `Stat` object that is returned by `cProfile().runctx(...)`. While a basic printout of profiling data gives some indication, one usually needs to dig around a little in the data to find what the real bottleneck is (see where most calls come from, switch between cumulative and proper time, etc.)

+1/2 since being able to read/interpret the raw data is a good skill to have IMO. However a graphical (or at least a tree structure) of the data is also very useful.
> 
> Writing such a browser might be a nice exercise for a student who is interested in interface programming. I bet there are good profiler browsers around to get inspiration from.

+1 here. I feel like we need a wiki page to keep a list of "good student projects"...

> A tool I haven't used yet but looks like a decent effort is [runsnakerun](https://pypi.python.org/pypi/RunSnakeRun). Duplicating that effort for the sage notebook might not seem like such a smart idea. Perhaps we can make the tool more easily accessible from sage? Given that it uses wxPython that might not be so very easily done ... I ended up installing it using OS tools, meaning that I *have* to write the profile data to a file and analyse it separately.

I've seen runsnakerun used in a few places (although I haven't used it myself), and instead of duplicating it in the notebook, perhaps we could link it into sage (notebook) as some type of package? Actually...perhaps what we should do is have a variable/function which calls your favorite profiler on the executed command(s), something like:

```
%profile
2 + 2
```




---

archive/issue_comments_045674.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-04-04T11:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45674",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_045675.json:
```json
{
    "body": "The first patch isn't a proper HG changeset (patches should be generated using `hg export`, the second patch is fine).",
    "created_at": "2013-04-04T11:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45675",
    "user": "jdemeyer"
}
```

The first patch isn't a proper HG changeset (patches should be generated using `hg export`, the second patch is fine).



---

archive/issue_comments_045676.json:
```json
{
    "body": "Attachment [trac_5814-prun_notebook-combined.patch](tarball://root/attachments/some-uuid/ticket5814/trac_5814-prun_notebook-combined.patch) by tscrim created at 2013-04-04 16:25:46",
    "created_at": "2013-04-04T16:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45676",
    "user": "tscrim"
}
```

Attachment [trac_5814-prun_notebook-combined.patch](tarball://root/attachments/some-uuid/ticket5814/trac_5814-prun_notebook-combined.patch) by tscrim created at 2013-04-04 16:25:46



---

archive/issue_comments_045677.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-04-04T16:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45677",
    "user": "tscrim"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_045678.json:
```json
{
    "body": "Fixed by combining all the patches into one. I hope that's okay.",
    "created_at": "2013-04-04T16:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45678",
    "user": "tscrim"
}
```

Fixed by combining all the patches into one. I hope that's okay.



---

archive/issue_comments_045679.json:
```json
{
    "body": "Thanks for your work on this, Travis! Your changes look excellent.\n\nI'm kind of surprised that you found 20 function calls where I had 3. I'll try that again later, but I trust you on it.",
    "created_at": "2013-04-05T05:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45679",
    "user": "tkluck"
}
```

Thanks for your work on this, Travis! Your changes look excellent.

I'm kind of surprised that you found 20 function calls where I had 3. I'll try that again later, but I trust you on it.



---

archive/issue_comments_045680.json:
```json
{
    "body": "That also seemed to be what the patchbot was getting, but if you're still getting fewer function calls, then we will have to change the test slightly. I'm also running these from the command line where I know the preparser is replacing `1` with `Integer(1)` which is an extra function call. I'm guessing you were doing the testing from the notebook? I'm 99% certain the notebook is doing the same, but it might evaluating these *before* it actually executes the `%prun` test...I'll do some tests later today too.\n\nFor patchbot:\n\nApply: trac_5814-prun_notebook-combined.patch",
    "created_at": "2013-04-05T12:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45680",
    "user": "tscrim"
}
```

That also seemed to be what the patchbot was getting, but if you're still getting fewer function calls, then we will have to change the test slightly. I'm also running these from the command line where I know the preparser is replacing `1` with `Integer(1)` which is an extra function call. I'm guessing you were doing the testing from the notebook? I'm 99% certain the notebook is doing the same, but it might evaluating these *before* it actually executes the `%prun` test...I'll do some tests later today too.

For patchbot:

Apply: trac_5814-prun_notebook-combined.patch



---

archive/issue_comments_045681.json:
```json
{
    "body": "In the notebook I get 3 function calls\n\n```\n         3 function calls in 0.007 seconds\n\n   Ordered by: standard name\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.007    0.007    0.007    0.007 <string>:1(<module>)\n        1    0.000    0.000    0.000    0.000 {len}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n```\n\nwith the command line:\n\n```\n         3 function calls in 0.000 seconds\n\n   Ordered by: standard name\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.000    0.000    0.000    0.000 <string>:1(<module>)\n        1    0.000    0.000    0.000    0.000 {len}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n```\n\nSo it's something specific to the doctesting framework that's not reflected in sage while it's directly running (I've noticed this in a few other places before too).",
    "created_at": "2013-04-05T15:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45681",
    "user": "tscrim"
}
```

In the notebook I get 3 function calls

```
         3 function calls in 0.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.007    0.007    0.007    0.007 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

with the command line:

```
         3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

So it's something specific to the doctesting framework that's not reflected in sage while it's directly running (I've noticed this in a few other places before too).



---

archive/issue_comments_045682.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-04-06T14:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45682",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_045683.json:
```json
{
    "body": "Does this actually work in the notebook?  (Sometimes Ipython upgrades cause trouble with such magic.)  I just get\n\n```\nNameError: name 'prun' is not defined\n```\n\nin 6.3 and 6.4.beta6.",
    "created_at": "2014-10-22T16:24:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45683",
    "user": "kcrisman"
}
```

Does this actually work in the notebook?  (Sometimes Ipython upgrades cause trouble with such magic.)  I just get

```
NameError: name 'prun' is not defined
```

in 6.3 and 6.4.beta6.



---

archive/issue_comments_045684.json:
```json
{
    "body": "I'm almost sure it did...but it's been so long that I can be certain. Considering we were using iPython 0.13 or something like that at the time, I wouldn't be surprised if something broke along the way.",
    "created_at": "2014-10-22T18:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45684",
    "user": "tscrim"
}
```

I'm almost sure it did...but it's been so long that I can be certain. Considering we were using iPython 0.13 or something like that at the time, I wouldn't be surprised if something broke along the way.



---

archive/issue_comments_045685.json:
```json
{
    "body": "Does it work for you now?",
    "created_at": "2014-10-22T19:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45685",
    "user": "kcrisman"
}
```

Does it work for you now?



---

archive/issue_comments_045686.json:
```json
{
    "body": "Nope.",
    "created_at": "2014-10-22T19:09:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5814#issuecomment-45686",
    "user": "tscrim"
}
```

Nope.
