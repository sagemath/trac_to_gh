# Issue 8712: Use `optparse` in sage -merge for increased usability.

archive/issues_008712.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nUsing `optparse` will, at the very least, show a proper usage message, which displays all the options.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8712\n\n",
    "created_at": "2010-04-18T08:52:59Z",
    "labels": [
        "component: build"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Use `optparse` in sage -merge for increased usability.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8712",
    "user": "https://github.com/TimDumol"
}
```
Assignee: GeorgSWeber

Using `optparse` will, at the very least, show a proper usage message, which displays all the options.

Issue created by migration from https://trac.sagemath.org/ticket/8712





---

archive/issue_comments_079361.json:
```json
{
    "body": "Makes sage-apply-ticket use `optparse` instead of `getopt`.",
    "created_at": "2010-04-18T12:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8712#issuecomment-79361",
    "user": "https://github.com/TimDumol"
}
```

Makes sage-apply-ticket use `optparse` instead of `getopt`.



---

archive/issue_comments_079362.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-18T12:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8712#issuecomment-79362",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079363.json:
```json
{
    "body": "Attachment [trac_8712-sage-merge-optparse.patch](tarball://root/attachments/some-uuid/ticket8712/trac_8712-sage-merge-optparse.patch) by @TimDumol created at 2010-04-18 12:16:53\n\nThis patch makes `sage-apply-ticket` use `optparse` instead of `getopt`, making things more robust, and adding a help/usage message, which displays all options and normal usage cases.",
    "created_at": "2010-04-18T12:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8712#issuecomment-79363",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_8712-sage-merge-optparse.patch](tarball://root/attachments/some-uuid/ticket8712/trac_8712-sage-merge-optparse.patch) by @TimDumol created at 2010-04-18 12:16:53

This patch makes `sage-apply-ticket` use `optparse` instead of `getopt`, making things more robust, and adding a help/usage message, which displays all options and normal usage cases.



---

archive/issue_comments_079364.json:
```json
{
    "body": "Attachment [trac_8712-sage-merge-optparse.2.patch](tarball://root/attachments/some-uuid/ticket8712/trac_8712-sage-merge-optparse.2.patch) by @TimDumol created at 2010-04-18 12:48:43\n\nFixes at typo. Apply this patch only.",
    "created_at": "2010-04-18T12:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8712#issuecomment-79364",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_8712-sage-merge-optparse.2.patch](tarball://root/attachments/some-uuid/ticket8712/trac_8712-sage-merge-optparse.2.patch) by @TimDumol created at 2010-04-18 12:48:43

Fixes at typo. Apply this patch only.



---

archive/issue_comments_079365.json:
```json
{
    "body": "The help message reads:\n\n\n```\nUsage: sage -merge [options] [ticket-number]\n\nTries to automate the process of merging tickets in release management.\nSee http://wiki.sagemath.org/devel/ReleaseManagement for more info.\n\nExample usage:\n\nsage -merge -c or sage -merge --candidates\n\n    * List all candidates for merging, i.e. all trac tickets with positive review. \n\nsage -merge <ticket_number> <options>\n\n    * Download patches from trac for the given ticket number, merge them, run tests, and report the results. \n\nsage -merge -a <options> or sage -merge --all <options>\n\n    * For each ticket on trac with a positive review, download the patches, apply them, and run doctests. At the end, report which tickets passed, which failed, and which didn't have any files to doctest (as is commonly the case with tickets for new spkg's). \n\n\nOptions:\n  -h, --help            show this help message and exit\n  -a, --all             For each ticket on trac with a positive review,\n                        download, apply, and test each. At the end, report\n                        which pass, fail, and have no files to doctest\n  -c, --candidates      List all candidates for merging, i.e., all trac\n                        tickets with positive review\n  -v, --verbose         Display the results of each test\n  -n NUM_THREADS, --num-threads=NUM_THREADS\n                        Number of threads to work with\n  -r REPOSITORY, --repository=REPOSITORY\n                        Which repository to apply to. Choices: ['bin',\n                        'extcode', 'sage', 'examples', 'scripts', 'main']\n  -t TEST, --test=TEST  What things to doctest. Choices: ['none', 'files',\n                        'directory', 'long'] or any prefix of a choice.\n  -o, --overwrite       Whether to overwrite files when downloading.\n  -d DIRECTORY, --directory=DIRECTORY\n                        Directory to store patches in.\n\n  Behavior:\n    Behavior after merging. Default is to pop after merging\n\n    -l, --leave-in-queue\n                        Leaves the patches in mercurial queue. Conflicts with\n                        --finish.\n    -f, --finish        Performs qfinish, commiting the patches. Conflicts\n                        with --leave-in-queue.\n```\n",
    "created_at": "2010-04-18T13:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8712#issuecomment-79365",
    "user": "https://github.com/TimDumol"
}
```

The help message reads:


```
Usage: sage -merge [options] [ticket-number]

Tries to automate the process of merging tickets in release management.
See http://wiki.sagemath.org/devel/ReleaseManagement for more info.

Example usage:

sage -merge -c or sage -merge --candidates

    * List all candidates for merging, i.e. all trac tickets with positive review. 

sage -merge <ticket_number> <options>

    * Download patches from trac for the given ticket number, merge them, run tests, and report the results. 

sage -merge -a <options> or sage -merge --all <options>

    * For each ticket on trac with a positive review, download the patches, apply them, and run doctests. At the end, report which tickets passed, which failed, and which didn't have any files to doctest (as is commonly the case with tickets for new spkg's). 


Options:
  -h, --help            show this help message and exit
  -a, --all             For each ticket on trac with a positive review,
                        download, apply, and test each. At the end, report
                        which pass, fail, and have no files to doctest
  -c, --candidates      List all candidates for merging, i.e., all trac
                        tickets with positive review
  -v, --verbose         Display the results of each test
  -n NUM_THREADS, --num-threads=NUM_THREADS
                        Number of threads to work with
  -r REPOSITORY, --repository=REPOSITORY
                        Which repository to apply to. Choices: ['bin',
                        'extcode', 'sage', 'examples', 'scripts', 'main']
  -t TEST, --test=TEST  What things to doctest. Choices: ['none', 'files',
                        'directory', 'long'] or any prefix of a choice.
  -o, --overwrite       Whether to overwrite files when downloading.
  -d DIRECTORY, --directory=DIRECTORY
                        Directory to store patches in.

  Behavior:
    Behavior after merging. Default is to pop after merging

    -l, --leave-in-queue
                        Leaves the patches in mercurial queue. Conflicts with
                        --finish.
    -f, --finish        Performs qfinish, commiting the patches. Conflicts
                        with --leave-in-queue.
```




---

archive/issue_comments_079366.json:
```json
{
    "body": "Looks pretty good. I found two small bugs (num_threads wasn't being passed correctly at one point, and the download directory wasn't dealt with right), and I think that the default values (e.g., the number of threads) should be in the help message.  I also think we can add a little statement saying that doctests were skipped if that is the case.  I'm attaching a reviewer patch implementing all of this.  If you're happy with it, I'm happy with the rest, so it can get a positive review.",
    "created_at": "2010-06-22T05:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8712#issuecomment-79366",
    "user": "https://github.com/jhpalmieri"
}
```

Looks pretty good. I found two small bugs (num_threads wasn't being passed correctly at one point, and the download directory wasn't dealt with right), and I think that the default values (e.g., the number of threads) should be in the help message.  I also think we can add a little statement saying that doctests were skipped if that is the case.  I'm attaching a reviewer patch implementing all of this.  If you're happy with it, I'm happy with the rest, so it can get a positive review.



---

archive/issue_comments_079367.json:
```json
{
    "body": "Attachment [trac_8712-reviewer.patch](tarball://root/attachments/some-uuid/ticket8712/trac_8712-reviewer.patch) by @jhpalmieri created at 2010-06-22 05:07:46\n\napply on top of trac_8712-sage-merge-optparse.2.patch",
    "created_at": "2010-06-22T05:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8712#issuecomment-79367",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8712-reviewer.patch](tarball://root/attachments/some-uuid/ticket8712/trac_8712-reviewer.patch) by @jhpalmieri created at 2010-06-22 05:07:46

apply on top of trac_8712-sage-merge-optparse.2.patch



---

archive/issue_comments_079368.json:
```json
{
    "body": "Nice catches! I'm fine with your changes.",
    "created_at": "2010-06-23T08:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8712#issuecomment-79368",
    "user": "https://github.com/TimDumol"
}
```

Nice catches! I'm fine with your changes.



---

archive/issue_comments_079369.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T15:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8712#issuecomment-79369",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079370.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8712#issuecomment-79370",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_079371.json:
```json
{
    "body": "Merged:\n\n    trac_8712-sage-merge-optparse.2.patch\n    trac_8712-reviewer.patch",
    "created_at": "2010-06-25T15:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8712#issuecomment-79371",
    "user": "https://github.com/rlmill"
}
```

Merged:

    trac_8712-sage-merge-optparse.2.patch
    trac_8712-reviewer.patch
