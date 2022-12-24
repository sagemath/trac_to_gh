# Issue 9738: Stealth core dump from testing sage/interfaces/genus2reduction.py

archive/issues_009738.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @robertwb @williamstein @jdemeyer\n\nWith Sage 4.5.3.alpha0 on sage.math:\n\n```sh\n$ cd SAGE_ROOT\n$ find -name core -type f\n$ ulimit -c unlimited\n$ ./sage -t -long devel/sage/sage/interfaces/genus2reduction.py \nsage -t -long \"devel/sage/sage/interfaces/genus2reduction.py\"\n         [3.1 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 3.1 seconds\n$ find -name core -type f\n./data/extcode/genus2reduction/core\n$\n```\n\nFor background see [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/239f712a39fce4a).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9738\n\n",
    "created_at": "2010-08-12T22:58:35Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Stealth core dump from testing sage/interfaces/genus2reduction.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9738",
    "user": "@qed777"
}
```
Assignee: mvngu

CC:  @robertwb @williamstein @jdemeyer

With Sage 4.5.3.alpha0 on sage.math:

```sh
$ cd SAGE_ROOT
$ find -name core -type f
$ ulimit -c unlimited
$ ./sage -t -long devel/sage/sage/interfaces/genus2reduction.py 
sage -t -long "devel/sage/sage/interfaces/genus2reduction.py"
         [3.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.1 seconds
$ find -name core -type f
./data/extcode/genus2reduction/core
$
```

For background see [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/239f712a39fce4a).

Issue created by migration from https://trac.sagemath.org/ticket/9738





---

archive/issue_comments_095207.json:
```json
{
    "body": "I interleaved `find -name core -type f` with executing the examples in `genus2reduction.py` in an interactive Sage session.  I see the core file only *after* I exit Sage, which ends with\n\n```\nExiting Sage (CPU time 0m0.17s, Wall time 2m6.89s).\nExiting spawned Genus2reduction process.\n```\n\nAlso, [here is the log](http://sage.math.washington.edu/home/mpatel/trac/9738/genus2reduction-21918-22537264-2.log) I  find in `DOT_SAGE/pexpect_logs/` after\n\n```sh\nenv SAGE_PEXPECT_LOG=\"yes\" ./sage -t devel/sage/sage/interfaces/genus2reduction.py\n```\n",
    "created_at": "2010-08-12T23:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95207",
    "user": "@qed777"
}
```

I interleaved `find -name core -type f` with executing the examples in `genus2reduction.py` in an interactive Sage session.  I see the core file only *after* I exit Sage, which ends with

```
Exiting Sage (CPU time 0m0.17s, Wall time 2m6.89s).
Exiting spawned Genus2reduction process.
```

Also, [here is the log](http://sage.math.washington.edu/home/mpatel/trac/9738/genus2reduction-21918-22537264-2.log) I  find in `DOT_SAGE/pexpect_logs/` after

```sh
env SAGE_PEXPECT_LOG="yes" ./sage -t devel/sage/sage/interfaces/genus2reduction.py
```




---

archive/issue_comments_095208.json:
```json
{
    "body": "Attachment [genus2reduction.c.diff](tarball://root/attachments/some-uuid/ticket9738/genus2reduction.c.diff) by @qed777 created at 2010-08-13 00:40:49\n\nQuit on `quit`.  Diff of `genus2reduction.c` from g2r 0.3.p6.",
    "created_at": "2010-08-13T00:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95208",
    "user": "@qed777"
}
```

Attachment [genus2reduction.c.diff](tarball://root/attachments/some-uuid/ticket9738/genus2reduction.c.diff) by @qed777 created at 2010-08-13 00:40:49

Quit on `quit`.  Diff of `genus2reduction.c` from g2r 0.3.p6.



---

archive/issue_comments_095209.json:
```json
{
    "body": "I've attached a possible solution.  If it looks good, I can make a new spkg.  We may need to coordinate with #9591.",
    "created_at": "2010-08-13T00:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95209",
    "user": "@qed777"
}
```

I've attached a possible solution.  If it looks good, I can make a new spkg.  We may need to coordinate with #9591.



---

archive/issue_comments_095210.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> We may need to coordinate with #9591.\n\nI don't think there is a problem, this issue is independent of #9343 and #9591 (we just have to rename the spkg at #9591 if this gets merged first).",
    "created_at": "2010-08-13T22:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95210",
    "user": "@jdemeyer"
}
```

Replying to [comment:2 mpatel]:
> We may need to coordinate with #9591.

I don't think there is a problem, this issue is independent of #9343 and #9591 (we just have to rename the spkg at #9591 if this gets merged first).



---

archive/issue_comments_095211.json:
```json
{
    "body": "Attachment [9738_genus2reduction_init_opts.patch](tarball://root/attachments/some-uuid/ticket9738/9738_genus2reduction_init_opts.patch) by @jdemeyer created at 2010-08-13 22:49:53\n\nAlternative patch to fix the issue",
    "created_at": "2010-08-13T22:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95211",
    "user": "@jdemeyer"
}
```

Attachment [9738_genus2reduction_init_opts.patch](tarball://root/attachments/some-uuid/ticket9738/9738_genus2reduction_init_opts.patch) by @jdemeyer created at 2010-08-13 22:49:53

Alternative patch to fix the issue



---

archive/issue_comments_095212.json:
```json
{
    "body": "I think mpatel's patch fixes the problem but does not address the real issue here, namely that PARI by default catches various signals and \"handles\" them.  But this is not what we want here.  Not making PARI install signal handlers solves the issue.\n\nMy patch also makes genus2reduction exit when EOF is encountered in the standard input.",
    "created_at": "2010-08-13T22:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95212",
    "user": "@jdemeyer"
}
```

I think mpatel's patch fixes the problem but does not address the real issue here, namely that PARI by default catches various signals and "handles" them.  But this is not what we want here.  Not making PARI install signal handlers solves the issue.

My patch also makes genus2reduction exit when EOF is encountered in the standard input.



---

archive/issue_comments_095213.json:
```json
{
    "body": "Jeroen's patch is definitely better than mine.  Thanks!\n\nWhether I run the doctest above or run `genus2reduction` directly from the shell and press ctrl-c/d, the program quits with no core dump.  Evaluating `genus2reduction.console()` in the Sage console and pressing ctrl-c/d returns me to the `sage:` prompt.  Also, running the long doctest suite passes without reproducible failures and leaves no relevant cores.\n\n`Genus2reduction_expect` in `genus2reduction.py` still uses its base class' `Expect._quit_string`, which returns \"quit\", but I think we can leave that alone(?).\n\nAre there any objections to making a new spkg here with Jeroen's patch?  If we do, we should put `genus2reduction.c` under version control.  Although I'm averse to putting too many logically different spkg changes in one ticket, I'll understand if we roll the changes here into #9591 and make this ticket a virtual blocker for an otherwise PARI-focused Sage 4.6.",
    "created_at": "2010-08-13T23:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95213",
    "user": "@qed777"
}
```

Jeroen's patch is definitely better than mine.  Thanks!

Whether I run the doctest above or run `genus2reduction` directly from the shell and press ctrl-c/d, the program quits with no core dump.  Evaluating `genus2reduction.console()` in the Sage console and pressing ctrl-c/d returns me to the `sage:` prompt.  Also, running the long doctest suite passes without reproducible failures and leaves no relevant cores.

`Genus2reduction_expect` in `genus2reduction.py` still uses its base class' `Expect._quit_string`, which returns "quit", but I think we can leave that alone(?).

Are there any objections to making a new spkg here with Jeroen's patch?  If we do, we should put `genus2reduction.c` under version control.  Although I'm averse to putting too many logically different spkg changes in one ticket, I'll understand if we roll the changes here into #9591 and make this ticket a virtual blocker for an otherwise PARI-focused Sage 4.6.



---

archive/issue_comments_095214.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2010-08-14T05:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95214",
    "user": "@qed777"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_095215.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n> Are there any objections to making a new spkg here with Jeroen's patch?\nNo objections.  If you think this patch can make it into sage-4.5.3, go ahead and do it.  If we merge it in sage-4.6, it would be better suited in #9591.",
    "created_at": "2010-08-14T09:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95215",
    "user": "@jdemeyer"
}
```

Replying to [comment:6 mpatel]:
> Are there any objections to making a new spkg here with Jeroen's patch?
No objections.  If you think this patch can make it into sage-4.5.3, go ahead and do it.  If we merge it in sage-4.6, it would be better suited in #9591.



---

archive/issue_comments_095216.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-14T19:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95216",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095217.json:
```json
{
    "body": "Since there seems to be a push towards merging #9343 (and hence #9591) soon, I will merge my patch into #9591.",
    "created_at": "2010-08-14T19:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95217",
    "user": "@jdemeyer"
}
```

Since there seems to be a push towards merging #9343 (and hence #9591) soon, I will merge my patch into #9591.



---

archive/issue_comments_095218.json:
```json
{
    "body": "# Release manager\n\nPlease close this ticket when #9591 is merged.",
    "created_at": "2010-08-31T00:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95218",
    "user": "@qed777"
}
```

# Release manager

Please close this ticket when #9591 is merged.



---

archive/issue_comments_095219.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-04T07:07:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95219",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095220.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-09-10T10:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9738#issuecomment-95220",
    "user": "@qed777"
}
```

Resolution: duplicate
