# Issue 5352: the valgrind log files in sage-doctest are written to $HOME/.sage instead of $DOT_SAGE

archive/issues_005352.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @orlitzky\n\nFix it so that the logs end up in DOT_SAGE since that does not have to be $HOME/.sage as hard coded for the log files.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5352\n\n",
    "created_at": "2009-02-23T22:37:41Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "the valgrind log files in sage-doctest are written to $HOME/.sage instead of $DOT_SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5352",
    "user": "mabshoff"
}
```
Assignee: cwitty

CC:  @orlitzky

Fix it so that the logs end up in DOT_SAGE since that does not have to be $HOME/.sage as hard coded for the log files.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5352





---

archive/issue_comments_041227.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-23T22:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41227",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041228.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2009-02-23T22:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41228",
    "user": "mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_041229.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41229",
    "user": "mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_041230.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-05T17:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41230",
    "user": "@a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_041231.json:
```json
{
    "body": "Patch tested successfully on 4.6.1, however (beginner question) what is the correct procedure\nfor reviewing such an out of sage-library/ issue ?",
    "created_at": "2011-02-08T10:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41231",
    "user": "rochelol2"
}
```

Patch tested successfully on 4.6.1, however (beginner question) what is the correct procedure
for reviewing such an out of sage-library/ issue ?



---

archive/issue_comments_041232.json:
```json
{
    "body": "Replying to [comment:4 rochelol2]:\n> Patch tested successfully on 4.6.1, however (beginner question) what is the correct procedure\n> for reviewing such an out of sage-library/ issue ?\n\nThere is a repository, referred to as the script repository, in `$SAGE_LOCAL/bin`. The patch should apply cleanly to this repo, have proper mercurial headers, etc.\n\nAttached patch does not fix all the problem places. The script `sage-valgrind` still refers to `$HOME/.sage`. Could you fix that and use \"hg export\" to create the patch?",
    "created_at": "2011-05-31T13:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41232",
    "user": "@burcin"
}
```

Replying to [comment:4 rochelol2]:
> Patch tested successfully on 4.6.1, however (beginner question) what is the correct procedure
> for reviewing such an out of sage-library/ issue ?

There is a repository, referred to as the script repository, in `$SAGE_LOCAL/bin`. The patch should apply cleanly to this repo, have proper mercurial headers, etc.

Attached patch does not fix all the problem places. The script `sage-valgrind` still refers to `$HOME/.sage`. Could you fix that and use "hg export" to create the patch?



---

archive/issue_comments_041233.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-05-31T13:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41233",
    "user": "@burcin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_041234.json:
```json
{
    "body": "Attachment [trac_5352_valgrind_log.patch](tarball://root/attachments/some-uuid/ticket5352/trac_5352_valgrind_log.patch) by @a-andre created at 2011-06-02 15:34:50",
    "created_at": "2011-06-02T15:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41234",
    "user": "@a-andre"
}
```

Attachment [trac_5352_valgrind_log.patch](tarball://root/attachments/some-uuid/ticket5352/trac_5352_valgrind_log.patch) by @a-andre created at 2011-06-02 15:34:50



---

archive/issue_comments_041235.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-02T15:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41235",
    "user": "@a-andre"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041236.json:
```json
{
    "body": "I think all of the affected scripts need to source sage-env for the default value of `$DOT_SAGE`. As is,\n\n\n```\n$ ./local/bin/sage-valgrind \n/local/bin/sage-ipython\nmkdir: cannot create directory `/valgrind': Permission denied\n```\n",
    "created_at": "2011-12-04T03:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41236",
    "user": "@orlitzky"
}
```

I think all of the affected scripts need to source sage-env for the default value of `$DOT_SAGE`. As is,


```
$ ./local/bin/sage-valgrind 
/local/bin/sage-ipython
mkdir: cannot create directory `/valgrind': Permission denied
```




---

archive/issue_comments_041237.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-12-04T03:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41237",
    "user": "@orlitzky"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_041238.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-04T17:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41238",
    "user": "@orlitzky"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041239.json:
```json
{
    "body": "Replying to [comment:7 mjo]:\n> I think all of the affected scripts need to source sage-env for the default value of `$DOT_SAGE`.\n\nAfter RTFMing, I see that I shouldn't be running the script from bash anyway, so this criticism is invalid.",
    "created_at": "2011-12-04T17:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41239",
    "user": "@orlitzky"
}
```

Replying to [comment:7 mjo]:
> I think all of the affected scripts need to source sage-env for the default value of `$DOT_SAGE`.

After RTFMing, I see that I shouldn't be running the script from bash anyway, so this criticism is invalid.



---

archive/issue_comments_041240.json:
```json
{
    "body": "I think this looks good. Here's how I tested:\n\n1. Install valgrind.\n2. Rebuild sage with SAGE_VALGRIND=\"yes\".\n3. Create an empty suppressions file (Trac #11918)\n4. Remove my ~/.sage/valgrind\n5. Create and export DOT_SAGE=~/grind\n6. Execute,\n   * sage -valgrind\n   * sage -cachegrind\n   * sage -callgrind\n   * sage -massif\n   * sage -tp 4 -long -valgrind devel/sage/sage (Killed this one prematurely since it was going to take a month)\n7. Tried to run sage -omega, but the exp-omega tool has been removed from recent versions of valgrind.\n8. Checked my ~/.sage and ~/grind directories to make sure all of the log files wound up in the right places.\n9. make ptestlong, no failures\n10. Grep for leftover '$HOME/.sage' instances in local/bin",
    "created_at": "2011-12-05T04:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41240",
    "user": "@orlitzky"
}
```

I think this looks good. Here's how I tested:

1. Install valgrind.
2. Rebuild sage with SAGE_VALGRIND="yes".
3. Create an empty suppressions file (Trac #11918)
4. Remove my ~/.sage/valgrind
5. Create and export DOT_SAGE=~/grind
6. Execute,
   * sage -valgrind
   * sage -cachegrind
   * sage -callgrind
   * sage -massif
   * sage -tp 4 -long -valgrind devel/sage/sage (Killed this one prematurely since it was going to take a month)
7. Tried to run sage -omega, but the exp-omega tool has been removed from recent versions of valgrind.
8. Checked my ~/.sage and ~/grind directories to make sure all of the log files wound up in the right places.
9. make ptestlong, no failures
10. Grep for leftover '$HOME/.sage' instances in local/bin



---

archive/issue_comments_041241.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-05T04:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41241",
    "user": "@orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_041242.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-09T10:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5352#issuecomment-41242",
    "user": "@jdemeyer"
}
```

Resolution: fixed
