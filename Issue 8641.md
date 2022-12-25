# Issue 8641: "sage -t" should exit with nonzero exit code if doctests fail

archive/issues_008641.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @wjp\n\nRight now, if I run doctests with \"sage -t\" and some doctests fail, the exit code is zero -- but it would be very handy to have a nonzero exit code; for example, it would make using Mercurial's bisect command very useful.\n\nIn #7995, it seems like sage-doctest is passing back some useful exit codes, so we just need to pass those on in a reasonable way.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8641\n\n",
    "created_at": "2010-04-02T02:41:39Z",
    "labels": [
        "component: doctest coverage",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "\"sage -t\" should exit with nonzero exit code if doctests fail",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8641",
    "user": "https://github.com/dandrake"
}
```
Assignee: tbd

CC:  @wjp

Right now, if I run doctests with "sage -t" and some doctests fail, the exit code is zero -- but it would be very handy to have a nonzero exit code; for example, it would make using Mercurial's bisect command very useful.

In #7995, it seems like sage-doctest is passing back some useful exit codes, so we just need to pass those on in a reasonable way.

Issue created by migration from https://trac.sagemath.org/ticket/8641





---

archive/issue_comments_078220.json:
```json
{
    "body": "I'm following up on the discussion at the end of #7995.\n\nFirst, the code `err = err // 256` seems okay: putting a print statement at the end of that python function shows that `err` seems to have an appropriate value.\n\nOther parts of the python code in sage-test confuse me, though. It seems to me that the function `test_file` always returns 0 (if the file exists), regardless of the success or failure of the test.  The function `test` has a return value which depends on whether tests passed, but `test_file` never uses the return value from `test`, does it?\n\nIn practice, if I run `sage -sh` and then do `sage-doctest` on a file with errors, I get a nonzero return value, but if I run `sage-test` on the same file, I get a return value of 0.",
    "created_at": "2010-04-13T20:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78220",
    "user": "https://github.com/jhpalmieri"
}
```

I'm following up on the discussion at the end of #7995.

First, the code `err = err // 256` seems okay: putting a print statement at the end of that python function shows that `err` seems to have an appropriate value.

Other parts of the python code in sage-test confuse me, though. It seems to me that the function `test_file` always returns 0 (if the file exists), regardless of the success or failure of the test.  The function `test` has a return value which depends on whether tests passed, but `test_file` never uses the return value from `test`, does it?

In practice, if I run `sage -sh` and then do `sage-doctest` on a file with errors, I get a nonzero return value, but if I run `sage-test` on the same file, I get a return value of 0.



---

archive/issue_comments_078221.json:
```json
{
    "body": "Here's a patch; I'll mark this ready for review, but it should perhaps be considered a first draft.",
    "created_at": "2010-04-13T20:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78221",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch; I'll mark this ready for review, but it should perhaps be considered a first draft.



---

archive/issue_comments_078222.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-13T20:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78222",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078223.json:
```json
{
    "body": "This needs to deal with the non-platform-independent behavior of return codes -- see the discussion at the bottom of #7995.",
    "created_at": "2010-04-13T22:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78223",
    "user": "https://github.com/jhpalmieri"
}
```

This needs to deal with the non-platform-independent behavior of return codes -- see the discussion at the bottom of #7995.



---

archive/issue_comments_078224.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-13T22:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78224",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078225.json:
```json
{
    "body": "Perhaps replacing `os.system(s)` with `check_call(s, shell=True)` (after importing `check_call` from subprocess) will work?  Here's draft number two.",
    "created_at": "2010-04-13T22:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78225",
    "user": "https://github.com/jhpalmieri"
}
```

Perhaps replacing `os.system(s)` with `check_call(s, shell=True)` (after importing `check_call` from subprocess) will work?  Here's draft number two.



---

archive/issue_comments_078226.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-13T22:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78226",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078227.json:
```json
{
    "body": "Attachment [trac_8641-sage-test.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641-sage-test.patch) by @jhpalmieri created at 2010-04-13 22:34:25\n\nscripts repo",
    "created_at": "2010-04-13T22:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78227",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8641-sage-test.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641-sage-test.patch) by @jhpalmieri created at 2010-04-13 22:34:25

scripts repo



---

archive/issue_comments_078228.json:
```json
{
    "body": "This seems to work for me on both my mac and on sage.math.  It needs to be tested much more extensively, though.",
    "created_at": "2010-04-13T22:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78228",
    "user": "https://github.com/jhpalmieri"
}
```

This seems to work for me on both my mac and on sage.math.  It needs to be tested much more extensively, though.



---

archive/issue_comments_078229.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-13T23:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78229",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078230.json:
```json
{
    "body": "Your patch seems to work as far as hitting Ctrl-C goes, but if doctesting more than one file, if doctests fail, the entire run fails:\n\n```\nTraceback (most recent call last):\n  File \"/scratch/sage-4.3.5/local/bin/sage-test\", line 177, in <module>\n    err = test_file(F)\n  File \"/scratch/sage-4.3.5/local/bin/sage-test\", line 125, in test_file\n    err = test(F, 'doctest ' + opts + extra_opts)\n  File \"/scratch/sage-4.3.5/local/bin/sage-test\", line 84, in test\n    err = check_call(s, shell=True)\n  File \"/scratch/sage-4.3.5/local/lib/python/subprocess.py\", line 488, in check_call\n    raise CalledProcessError(retcode, cmd)\nsubprocess.CalledProcessError: Command '/scratch/sage-4.3.5/local/bin/sage-doctest  \"devel/sage/sage/combinat/tableau.py\"' returned non-zero exit status 100\n```\n\nI think we want subprocess.call, not check_call; that will allow us to pass the exit code back up if we want to; \"call\" returns the exit code, but check_call either returns or raises CalledProcessError. Of course, if you like, we can catch the exception and just use that information.\n\nAlso, I think we can avoid the shell=True bit, since our command line is so simple: just do\n\n```\nerr = call([os.path.join(SAGE_ROOT, 'local', 'bin', 'sage-%s' % cmd), F])\n```\n\nand, on line 127, change 'doctest ' (note the space) to 'doctest'.\n\nFinally, if using the subprocess module, I think we get the genuine return code and there's no need for any \"err = err // 256\" business.",
    "created_at": "2010-04-13T23:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78230",
    "user": "https://github.com/dandrake"
}
```

Your patch seems to work as far as hitting Ctrl-C goes, but if doctesting more than one file, if doctests fail, the entire run fails:

```
Traceback (most recent call last):
  File "/scratch/sage-4.3.5/local/bin/sage-test", line 177, in <module>
    err = test_file(F)
  File "/scratch/sage-4.3.5/local/bin/sage-test", line 125, in test_file
    err = test(F, 'doctest ' + opts + extra_opts)
  File "/scratch/sage-4.3.5/local/bin/sage-test", line 84, in test
    err = check_call(s, shell=True)
  File "/scratch/sage-4.3.5/local/lib/python/subprocess.py", line 488, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '/scratch/sage-4.3.5/local/bin/sage-doctest  "devel/sage/sage/combinat/tableau.py"' returned non-zero exit status 100
```

I think we want subprocess.call, not check_call; that will allow us to pass the exit code back up if we want to; "call" returns the exit code, but check_call either returns or raises CalledProcessError. Of course, if you like, we can catch the exception and just use that information.

Also, I think we can avoid the shell=True bit, since our command line is so simple: just do

```
err = call([os.path.join(SAGE_ROOT, 'local', 'bin', 'sage-%s' % cmd), F])
```

and, on line 127, change 'doctest ' (note the space) to 'doctest'.

Finally, if using the subprocess module, I think we get the genuine return code and there's no need for any "err = err // 256" business.



---

archive/issue_comments_078231.json:
```json
{
    "body": "Also, there's a couple loops where we need to use the \"err = err | return code\" bit, otherwise we will lose the information that a doctest failed. I've updated your patch to do this; I'll upload a new patch shortly.",
    "created_at": "2010-04-14T01:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78231",
    "user": "https://github.com/dandrake"
}
```

Also, there's a couple loops where we need to use the "err = err | return code" bit, otherwise we will lose the information that a doctest failed. I've updated your patch to do this; I'll upload a new patch shortly.



---

archive/issue_comments_078232.json:
```json
{
    "body": "apply to scripts repo. Replaces previous.",
    "created_at": "2010-04-14T01:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78232",
    "user": "https://github.com/dandrake"
}
```

apply to scripts repo. Replaces previous.



---

archive/issue_comments_078233.json:
```json
{
    "body": "Attachment [trac_8641.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641.patch) by @jhpalmieri created at 2010-04-14 03:01:47\n\nThis isn't quite working for me: I get errors if I do \"sage -t -long FILE\".  I'm attaching a patch on top of yours which fixes it for me on my iMac, on sage.math, and on t2 (Solaris).",
    "created_at": "2010-04-14T03:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78233",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8641.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641.patch) by @jhpalmieri created at 2010-04-14 03:01:47

This isn't quite working for me: I get errors if I do "sage -t -long FILE".  I'm attaching a patch on top of yours which fixes it for me on my iMac, on sage.math, and on t2 (Solaris).



---

archive/issue_comments_078234.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-14T03:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78234",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078235.json:
```json
{
    "body": "Attachment [trac_8641-part2.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641-part2.patch) by @jhpalmieri created at 2010-04-14 03:02:14\n\napply on top of trac_8641.patch",
    "created_at": "2010-04-14T03:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78235",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8641-part2.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641-part2.patch) by @jhpalmieri created at 2010-04-14 03:02:14

apply on top of trac_8641.patch



---

archive/issue_comments_078236.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n> This isn't quite working for me: I get errors if I do \"sage -t -long FILE\".  I'm attaching a patch on top of yours which fixes it for me on my iMac, on sage.math, and on t2 (Solaris).\n\nAh, nice catch. I didn't test with -long. I took your patch and it works properly on my Ubuntu machines and on bsd.math.\n\nwjp, could you take a look at these patches? I think everything is fine, but another opinion would be nice.\n\nAlso, we still should work on sage-ptest; as pointed out at #7995, there's duplicated code there. But at least with this ticket, we can easily use Mercurial's bisect command to track down failing doctests.",
    "created_at": "2010-04-14T03:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78236",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:9 jhpalmieri]:
> This isn't quite working for me: I get errors if I do "sage -t -long FILE".  I'm attaching a patch on top of yours which fixes it for me on my iMac, on sage.math, and on t2 (Solaris).

Ah, nice catch. I didn't test with -long. I took your patch and it works properly on my Ubuntu machines and on bsd.math.

wjp, could you take a look at these patches? I think everything is fine, but another opinion would be nice.

Also, we still should work on sage-ptest; as pointed out at #7995, there's duplicated code there. But at least with this ticket, we can easily use Mercurial's bisect command to track down failing doctests.



---

archive/issue_comments_078237.json:
```json
{
    "body": "I wonder if something else could be happening. Possibly by coincidence, 2 is also SIGINT. Could it be that on sage.math the sage-doctest script itself is being killed by the Ctrl-C instead of the doctest it is running?\n\nAfter all, if you trigger one of the other error cases (like regular error failures), they are caught on sage.math properly.\n\nAlso, a transcript from sage.math:\n\n\n```\nsage: os.system(\"true\")\n0\nsage: os.system(\"false\")\n256\nsage: os.system(\"sleep 100\")\n[press Ctrl-C]\n2\n```\n\n\nSo the return values of `os.system` seem to match the specs.",
    "created_at": "2010-04-14T12:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78237",
    "user": "https://github.com/wjp"
}
```

I wonder if something else could be happening. Possibly by coincidence, 2 is also SIGINT. Could it be that on sage.math the sage-doctest script itself is being killed by the Ctrl-C instead of the doctest it is running?

After all, if you trigger one of the other error cases (like regular error failures), they are caught on sage.math properly.

Also, a transcript from sage.math:


```
sage: os.system("true")
0
sage: os.system("false")
256
sage: os.system("sleep 100")
[press Ctrl-C]
2
```


So the return values of `os.system` seem to match the specs.



---

archive/issue_comments_078238.json:
```json
{
    "body": "P.S. It does sound like using subprocess.call might be more portable; its docs have fewer warnings about undefined return values.\n\nIt does throw a KeyboardInterrupt itself when the called program gets a SIGINT, though, so we may have to catch that to execute the line\n\n\n```\nfailed.append(sage_test_command(F)+\" # KeyboardInterrupt\")\n```\n\n\nI'll take a closer look at the patch later today.",
    "created_at": "2010-04-14T12:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78238",
    "user": "https://github.com/wjp"
}
```

P.S. It does sound like using subprocess.call might be more portable; its docs have fewer warnings about undefined return values.

It does throw a KeyboardInterrupt itself when the called program gets a SIGINT, though, so we may have to catch that to execute the line


```
failed.append(sage_test_command(F)+" # KeyboardInterrupt")
```


I'll take a closer look at the patch later today.



---

archive/issue_comments_078239.json:
```json
{
    "body": "Replying to [comment:12 wjp]:\n\n> I'll take a closer look at the patch later today.\n\nDo you recommend any changes to [attachment:trac_8641.patch] or [attachment:trac_8641-part2.patch]?\n\nBy the way, we may need to rebase these for #8891.",
    "created_at": "2010-06-12T09:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78239",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:12 wjp]:

> I'll take a closer look at the patch later today.

Do you recommend any changes to [attachment:trac_8641.patch] or [attachment:trac_8641-part2.patch]?

By the way, we may need to rebase these for #8891.



---

archive/issue_comments_078240.json:
```json
{
    "body": "Combined patch rebased vs 4.4.4.alpha0 + #8891.  Replaces all previous.",
    "created_at": "2010-06-14T09:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78240",
    "user": "https://github.com/qed777"
}
```

Combined patch rebased vs 4.4.4.alpha0 + #8891.  Replaces all previous.



---

archive/issue_comments_078241.json:
```json
{
    "body": "Attachment [trac_8641-doctest_exit_codes.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641-doctest_exit_codes.patch) by @qed777 created at 2010-06-14 09:32:06\n\nReplying to [comment:13 mpatel]:\n\n> By the way, we may need to rebase these for #8891.\n\nI've attached a [attachment:trac_8641-doctest_exit_codes.patch combined, rebased patch].",
    "created_at": "2010-06-14T09:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78241",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8641-doctest_exit_codes.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641-doctest_exit_codes.patch) by @qed777 created at 2010-06-14 09:32:06

Replying to [comment:13 mpatel]:

> By the way, we may need to rebase these for #8891.

I've attached a [attachment:trac_8641-doctest_exit_codes.patch combined, rebased patch].



---

archive/issue_comments_078242.json:
```json
{
    "body": "Replying to [comment:15 mpatel]:\n> Replying to [comment:13 mpatel]:\n> \n> > By the way, we may need to rebase these for #8891.\n> \n> I've attached a [attachment:trac_8641-doctest_exit_codes.patch combined, rebased patch].\n\nHmm, on 4.4.4.alpha0, I get a hunk reject: on line 123 or so, my copy of sage-test says\n\n```\n   elif os.path.isdir(F) and not (F[:1] == '.') \\\n            and not '#' in F and not os.sep + 'notes' in F:\n```\n\nand your patch says\n\n```\n     elif (os.path.isdir(F) and  not '#' in F and\n           not os.sep + 'notes' in F):\n```\n\n...so somebody changed the backslash line continuation to parentheses. I'll manually fix the hunk and test your patch.",
    "created_at": "2010-06-15T02:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78242",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:15 mpatel]:
> Replying to [comment:13 mpatel]:
> 
> > By the way, we may need to rebase these for #8891.
> 
> I've attached a [attachment:trac_8641-doctest_exit_codes.patch combined, rebased patch].

Hmm, on 4.4.4.alpha0, I get a hunk reject: on line 123 or so, my copy of sage-test says

```
   elif os.path.isdir(F) and not (F[:1] == '.') \
            and not '#' in F and not os.sep + 'notes' in F:
```

and your patch says

```
     elif (os.path.isdir(F) and  not '#' in F and
           not os.sep + 'notes' in F):
```

...so somebody changed the backslash line continuation to parentheses. I'll manually fix the hunk and test your patch.



---

archive/issue_comments_078243.json:
```json
{
    "body": "Replying to [comment:15 mpatel]:\n> I've attached a [attachment:trac_8641-doctest_exit_codes.patch combined, rebased patch].\n\nI fixed the hunk reject and your patch seems to work fine. The exit codes match up with what `sage-doctest` says (although I didn't check exit code 4, since I don't know how to make the doctesting framework raise an exception). I tried with individual files, directories, with and without \"-long\", so it seems to work pretty well on my Ubuntu machine.",
    "created_at": "2010-06-15T03:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78243",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:15 mpatel]:
> I've attached a [attachment:trac_8641-doctest_exit_codes.patch combined, rebased patch].

I fixed the hunk reject and your patch seems to work fine. The exit codes match up with what `sage-doctest` says (although I didn't check exit code 4, since I don't know how to make the doctesting framework raise an exception). I tried with individual files, directories, with and without "-long", so it seems to work pretty well on my Ubuntu machine.



---

archive/issue_comments_078244.json:
```json
{
    "body": "Replying to [comment:17 ddrake]:\n> I fixed the hunk reject and your patch seems to work fine. The exit codes match up with what `sage-doctest` says (although I didn't check exit code 4, since I don't know how to make the doctesting framework raise an exception). I tried with individual files, directories, with and without \"-long\", so it seems to work pretty well on my Ubuntu machine.\n\nI tested on bsd.math and the patch works there, too.",
    "created_at": "2010-06-15T05:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78244",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:17 ddrake]:
> I fixed the hunk reject and your patch seems to work fine. The exit codes match up with what `sage-doctest` says (although I didn't check exit code 4, since I don't know how to make the doctesting framework raise an exception). I tried with individual files, directories, with and without "-long", so it seems to work pretty well on my Ubuntu machine.

I tested on bsd.math and the patch works there, too.



---

archive/issue_comments_078245.json:
```json
{
    "body": "Replying to [comment:17 ddrake]:\n> (although I didn't check exit code 4, since I don't know how to make the doctesting framework raise an exception).\n\nShould you still want to try, the example in ticket #7993 will trigger one of those.",
    "created_at": "2010-06-15T08:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78245",
    "user": "https://github.com/wjp"
}
```

Replying to [comment:17 ddrake]:
> (although I didn't check exit code 4, since I don't know how to make the doctesting framework raise an exception).

Should you still want to try, the example in ticket #7993 will trigger one of those.



---

archive/issue_comments_078246.json:
```json
{
    "body": "Attachment [trac_8641-doctest_exit_codes.2.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641-doctest_exit_codes.2.patch) by @qed777 created at 2010-06-15 09:25:57\n\nModify `sage-ptest`, too.  Apply to 4.4.4.alpha0 + #8891.  Apply only this patch.",
    "created_at": "2010-06-15T09:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78246",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8641-doctest_exit_codes.2.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641-doctest_exit_codes.2.patch) by @qed777 created at 2010-06-15 09:25:57

Modify `sage-ptest`, too.  Apply to 4.4.4.alpha0 + #8891.  Apply only this patch.



---

archive/issue_comments_078247.json:
```json
{
    "body": "I've attached an attempt to get the same behavior for `sage -tp`.  The patch should apply to 4.4.4.alpha0 + #8891, unless I've `qfold`ed improperly.\n\nIt seems there's much room for improvement in `sage-ptest`.  For example, are the mutex locks really necessary?   I think both `skip` and `populatefilelist` run only in the main process.  But I suppose we could leave this and other potential oddities for #9224.",
    "created_at": "2010-06-15T09:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78247",
    "user": "https://github.com/qed777"
}
```

I've attached an attempt to get the same behavior for `sage -tp`.  The patch should apply to 4.4.4.alpha0 + #8891, unless I've `qfold`ed improperly.

It seems there's much room for improvement in `sage-ptest`.  For example, are the mutex locks really necessary?   I think both `skip` and `populatefilelist` run only in the main process.  But I suppose we could leave this and other potential oddities for #9224.



---

archive/issue_comments_078248.json:
```json
{
    "body": "Changing assignee from tbd to @dandrake.",
    "created_at": "2010-06-16T04:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78248",
    "user": "https://github.com/dandrake"
}
```

Changing assignee from tbd to @dandrake.



---

archive/issue_comments_078249.json:
```json
{
    "body": "mpatel: on line 337 of sage-ptest and line 176 of sage-test, your patch (attachment:trac_8641-doctest_exit_codes.2.patch) always sets err = 2. Can you change that to\n\n```\n   err = 2 | err\n```\n\n? Then, if doctesting a bunch of files and hit ctrl-c, you can tell the difference between \"all the tests that ran passed\" and \"there was at least one doctest failure\". (And other errors that might have happened before you hit ctrl-c.)",
    "created_at": "2010-06-16T04:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78249",
    "user": "https://github.com/dandrake"
}
```

mpatel: on line 337 of sage-ptest and line 176 of sage-test, your patch (attachment:trac_8641-doctest_exit_codes.2.patch) always sets err = 2. Can you change that to

```
   err = 2 | err
```

? Then, if doctesting a bunch of files and hit ctrl-c, you can tell the difference between "all the tests that ran passed" and "there was at least one doctest failure". (And other errors that might have happened before you hit ctrl-c.)



---

archive/issue_comments_078250.json:
```json
{
    "body": "Use `err = err | 2` for `KeyboardInterrupt`.  Apply only this patch, to 4.4.4.alpha0 + #8891.",
    "created_at": "2010-06-16T07:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78250",
    "user": "https://github.com/qed777"
}
```

Use `err = err | 2` for `KeyboardInterrupt`.  Apply only this patch, to 4.4.4.alpha0 + #8891.



---

archive/issue_comments_078251.json:
```json
{
    "body": "Attachment [trac_8641-doctest_exit_codes.3.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641-doctest_exit_codes.3.patch) by @qed777 created at 2010-06-16 07:20:05\n\nDone.  [attachment:trac_8641-doctest_exit_codes.3.patch V3] uses `err = 2 | err` for `KeyboardInterrupt`s to both scripts.",
    "created_at": "2010-06-16T07:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78251",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8641-doctest_exit_codes.3.patch](tarball://root/attachments/some-uuid/ticket8641/trac_8641-doctest_exit_codes.3.patch) by @qed777 created at 2010-06-16 07:20:05

Done.  [attachment:trac_8641-doctest_exit_codes.3.patch V3] uses `err = 2 | err` for `KeyboardInterrupt`s to both scripts.



---

archive/issue_comments_078252.json:
```json
{
    "body": "This looks good, and I've used it a bunch and it works properly. But I'm listed as one of the authors, so perhaps I shouldn't flip it to positive review...wjp, can you look this over? I did check exit code 4 and that works properly.",
    "created_at": "2010-06-16T15:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78252",
    "user": "https://github.com/dandrake"
}
```

This looks good, and I've used it a bunch and it works properly. But I'm listed as one of the authors, so perhaps I shouldn't flip it to positive review...wjp, can you look this over? I did check exit code 4 and that works properly.



---

archive/issue_comments_078253.json:
```json
{
    "body": "I'll try to find time to take a proper look friday or this weekend, but at first glance it seems like my comment 12 about `SIGINT`/`KeyboardInterrupt` is still valid.",
    "created_at": "2010-06-17T21:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78253",
    "user": "https://github.com/wjp"
}
```

I'll try to find time to take a proper look friday or this weekend, but at first glance it seems like my comment 12 about `SIGINT`/`KeyboardInterrupt` is still valid.



---

archive/issue_comments_078254.json:
```json
{
    "body": "Replying to [comment:12 wjp]:\n> [subprocess.call] does throw a KeyboardInterrupt itself when the called program gets a SIGINT, though, so we may have to catch that to execute the line\n> \n> {{{\n> failed.append(sage_test_command(F)+\" # KeyboardInterrupt\")\n> }}}\n\nHrm, I'm not sure this is true -- at least on my Ubuntu machine. With the most recent version of patch, I changed the bit starting at line 84 of sage-test to this:\n\n```\n  try:\n      err = call(s, shell=True)\n      print '%s returned code %s' % (s, err)\n  except KeyboardInterrupt:\n      print '*****sage-text line 87 caught keyboard interrupt'\n      raise\n```\n\nI then ran a doctest (combinat/words/finite_word.py) and in another terminal, sent the called process a SIGINT with\n\n```\nkill -2 `ps ax | grep finite_word | grep sage-doctest | grep python | awk '{print $1}'\n```\n\nThe result is:\n\n```\nsage -t  \"devel/sage/sage/combinat/words/finite_word.py\"\nKeyboardInterrupt -- interrupted after 3.37038588524 seconds!\n/home/drake/s/sage-4.4.4.alpha0-test/local/bin/sage-doctest  \"devel/sage/sage/combinat/words/finite_word.py\" returned code 2\nAborting further tests.\n```\n\nThe \"interrupted after 3.370...\" is from sage-doctest, line 668, which then exits with return code 2. It seems like subprocess.call in this instance notes that the process finished, and dutifully passes on the return code -- without raising a KeyboardInterrupt. Then, on line 95 the `failed.append(sage_test_command(F)+\" # KeyboardInterrupt\")` bit is executed and a KeyboardInterrupt is raised; that causes the \"Aborting further tests\" to be printed.\n\nIf I hit ctrl-c while running the doctest, it gets caught as you would expect:\n\n```\nsage -t  \"devel/sage/sage/combinat/words/finite_word.py\"\n^CKeyboardInterrupt -- interrupted after 2.75523304939 seconds!\n*****sage-text line 87 caught keyboard interrupt\nAborting further tests.\n```\n\n\nWhat is interesting is, if instead of sending SIGINT to the Python sage-doctest process, I send a SIGINT to the *shell* process created by subprocess.call, it seems to do nothing -- the doctest runs normally, finishes, but the return code is -2; this agrees with [the Popen returncode documentation](http://docs.python.org/library/subprocess.html#subprocess.Popen.returncode). Then, the entire process exits with return code 254, which is a bit strange, but at least it's indicating that something strange happened.",
    "created_at": "2010-06-18T03:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78254",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:12 wjp]:
> [subprocess.call] does throw a KeyboardInterrupt itself when the called program gets a SIGINT, though, so we may have to catch that to execute the line
> 
> {{{
> failed.append(sage_test_command(F)+" # KeyboardInterrupt")
> }}}

Hrm, I'm not sure this is true -- at least on my Ubuntu machine. With the most recent version of patch, I changed the bit starting at line 84 of sage-test to this:

```
  try:
      err = call(s, shell=True)
      print '%s returned code %s' % (s, err)
  except KeyboardInterrupt:
      print '*****sage-text line 87 caught keyboard interrupt'
      raise
```

I then ran a doctest (combinat/words/finite_word.py) and in another terminal, sent the called process a SIGINT with

```
kill -2 `ps ax | grep finite_word | grep sage-doctest | grep python | awk '{print $1}'
```

The result is:

```
sage -t  "devel/sage/sage/combinat/words/finite_word.py"
KeyboardInterrupt -- interrupted after 3.37038588524 seconds!
/home/drake/s/sage-4.4.4.alpha0-test/local/bin/sage-doctest  "devel/sage/sage/combinat/words/finite_word.py" returned code 2
Aborting further tests.
```

The "interrupted after 3.370..." is from sage-doctest, line 668, which then exits with return code 2. It seems like subprocess.call in this instance notes that the process finished, and dutifully passes on the return code -- without raising a KeyboardInterrupt. Then, on line 95 the `failed.append(sage_test_command(F)+" # KeyboardInterrupt")` bit is executed and a KeyboardInterrupt is raised; that causes the "Aborting further tests" to be printed.

If I hit ctrl-c while running the doctest, it gets caught as you would expect:

```
sage -t  "devel/sage/sage/combinat/words/finite_word.py"
^CKeyboardInterrupt -- interrupted after 2.75523304939 seconds!
*****sage-text line 87 caught keyboard interrupt
Aborting further tests.
```


What is interesting is, if instead of sending SIGINT to the Python sage-doctest process, I send a SIGINT to the *shell* process created by subprocess.call, it seems to do nothing -- the doctest runs normally, finishes, but the return code is -2; this agrees with [the Popen returncode documentation](http://docs.python.org/library/subprocess.html#subprocess.Popen.returncode). Then, the entire process exits with return code 254, which is a bit strange, but at least it's indicating that something strange happened.



---

archive/issue_comments_078255.json:
```json
{
    "body": "Hm, you're right. I may have mixed up process IDs the previous time I tried.\n\nIn any case, it might make sense to explicitly catch this `KeyboardInterrupt`?. But it's not strictly necessary since it'll be caught on a higher level anyway. (It may be something to save for further doctesting cleanup patches.)\n\nI don't like the lines `err = err | test_file(F)`, `err = err | ret` and `err = err | 2`, though. They suggest that `err` is a bitmask or boolean, while it isn't. We could make it a bitmask, of course, so that 0 = all ok, 1 = failed tests, 2 = interrupted, 3 = failed tests and interrupted. Are there any other special cases we would want to consider in that case? Maybe a separate bit for timeouts? (See also #9316)",
    "created_at": "2010-06-27T10:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78255",
    "user": "https://github.com/wjp"
}
```

Hm, you're right. I may have mixed up process IDs the previous time I tried.

In any case, it might make sense to explicitly catch this `KeyboardInterrupt`?. But it's not strictly necessary since it'll be caught on a higher level anyway. (It may be something to save for further doctesting cleanup patches.)

I don't like the lines `err = err | test_file(F)`, `err = err | ret` and `err = err | 2`, though. They suggest that `err` is a bitmask or boolean, while it isn't. We could make it a bitmask, of course, so that 0 = all ok, 1 = failed tests, 2 = interrupted, 3 = failed tests and interrupted. Are there any other special cases we would want to consider in that case? Maybe a separate bit for timeouts? (See also #9316)



---

archive/issue_comments_078256.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-06T20:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78256",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078257.json:
```json
{
    "body": "Mpatel pointed out that #9243 already tackles the powers-of-two thing.\n\nI'm giving this a positive review, provided that #9243 is merged too. (I'll review that ticket too.)",
    "created_at": "2010-07-06T20:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78257",
    "user": "https://github.com/wjp"
}
```

Mpatel pointed out that #9243 already tackles the powers-of-two thing.

I'm giving this a positive review, provided that #9243 is merged too. (I'll review that ticket too.)



---

archive/issue_comments_078258.json:
```json
{
    "body": "To release manager:  Apply just [attachment:trac_8641-doctest_exit_codes.3.patch] to 4.5.alpha4.",
    "created_at": "2010-07-07T03:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78258",
    "user": "https://github.com/qed777"
}
```

To release manager:  Apply just [attachment:trac_8641-doctest_exit_codes.3.patch] to 4.5.alpha4.



---

archive/issue_comments_078259.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T07:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78259",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_078260.json:
```json
{
    "body": "Merged attachment:trac_8641-doctest_exit_codes.3.patch in 4.5.2.alpha1.",
    "created_at": "2010-07-22T07:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8641#issuecomment-78260",
    "user": "https://github.com/dandrake"
}
```

Merged attachment:trac_8641-doctest_exit_codes.3.patch in 4.5.2.alpha1.



---

archive/issue_events_008810.json:
```json
{
    "actor": "@dandrake",
    "created_at": "2010-07-22T07:39:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8641",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8641#event-8810"
}
```
