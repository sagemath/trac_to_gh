# Issue 8641: "sage -t" should exit with nonzero exit code if doctests fail

Issue created by migration from https://trac.sagemath.org/ticket/8641

Original creator: ddrake

Original creation time: 2010-04-02 02:41:39

Assignee: tbd

CC:  wjp

Right now, if I run doctests with "sage -t" and some doctests fail, the exit code is zero -- but it would be very handy to have a nonzero exit code; for example, it would make using Mercurial's bisect command very useful.

In #7995, it seems like sage-doctest is passing back some useful exit codes, so we just need to pass those on in a reasonable way.


---

Comment by jhpalmieri created at 2010-04-13 20:19:00

I'm following up on the discussion at the end of #7995.

First, the code `err = err // 256` seems okay: putting a print statement at the end of that python function shows that `err` seems to have an appropriate value.

Other parts of the python code in sage-test confuse me, though. It seems to me that the function `test_file` always returns 0 (if the file exists), regardless of the success or failure of the test.  The function `test` has a return value which depends on whether tests passed, but `test_file` never uses the return value from `test`, does it?

In practice, if I run `sage -sh` and then do `sage-doctest` on a file with errors, I get a nonzero return value, but if I run `sage-test` on the same file, I get a return value of 0.


---

Comment by jhpalmieri created at 2010-04-13 20:32:58

Here's a patch; I'll mark this ready for review, but it should perhaps be considered a first draft.


---

Comment by jhpalmieri created at 2010-04-13 20:32:58

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-04-13 22:28:51

This needs to deal with the non-platform-independent behavior of return codes -- see the discussion at the bottom of #7995.


---

Comment by jhpalmieri created at 2010-04-13 22:28:51

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-04-13 22:34:08

Perhaps replacing `os.system(s)` with `check_call(s, shell=True)` (after importing `check_call` from subprocess) will work?  Here's draft number two.


---

Comment by jhpalmieri created at 2010-04-13 22:34:08

Changing status from needs_work to needs_review.


---

Attachment

scripts repo


---

Comment by jhpalmieri created at 2010-04-13 22:34:59

This seems to work for me on both my mac and on sage.math.  It needs to be tested much more extensively, though.


---

Comment by ddrake created at 2010-04-13 23:46:48

Changing status from needs_review to needs_work.


---

Comment by ddrake created at 2010-04-13 23:46:48

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

Comment by ddrake created at 2010-04-14 01:49:14

Also, there's a couple loops where we need to use the "err = err | return code" bit, otherwise we will lose the information that a doctest failed. I've updated your patch to do this; I'll upload a new patch shortly.


---

Comment by ddrake created at 2010-04-14 01:55:43

apply to scripts repo. Replaces previous.


---

Attachment

This isn't quite working for me: I get errors if I do "sage -t -long FILE".  I'm attaching a patch on top of yours which fixes it for me on my iMac, on sage.math, and on t2 (Solaris).


---

Comment by jhpalmieri created at 2010-04-14 03:01:47

Changing status from needs_work to needs_review.


---

Attachment

apply on top of trac_8641.patch


---

Comment by ddrake created at 2010-04-14 03:52:10

Replying to [comment:9 jhpalmieri]:
> This isn't quite working for me: I get errors if I do "sage -t -long FILE".  I'm attaching a patch on top of yours which fixes it for me on my iMac, on sage.math, and on t2 (Solaris).

Ah, nice catch. I didn't test with -long. I took your patch and it works properly on my Ubuntu machines and on bsd.math.

wjp, could you take a look at these patches? I think everything is fine, but another opinion would be nice.

Also, we still should work on sage-ptest; as pointed out at #7995, there's duplicated code there. But at least with this ticket, we can easily use Mercurial's bisect command to track down failing doctests.


---

Comment by wjp created at 2010-04-14 12:10:32

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

Comment by wjp created at 2010-04-14 12:16:08

P.S. It does sound like using subprocess.call might be more portable; its docs have fewer warnings about undefined return values.

It does throw a KeyboardInterrupt itself when the called program gets a SIGINT, though, so we may have to catch that to execute the line


```
failed.append(sage_test_command(F)+" # KeyboardInterrupt")
```


I'll take a closer look at the patch later today.


---

Comment by mpatel created at 2010-06-12 09:37:20

Replying to [comment:12 wjp]:

> I'll take a closer look at the patch later today.

Do you recommend any changes to [attachment:trac_8641.patch] or [attachment:trac_8641-part2.patch]?

By the way, we may need to rebase these for #8891.


---

Comment by mpatel created at 2010-06-14 09:29:53

Combined patch rebased vs 4.4.4.alpha0 + #8891.  Replaces all previous.


---

Attachment

Replying to [comment:13 mpatel]:

> By the way, we may need to rebase these for #8891.

I've attached a [attachment:trac_8641-doctest_exit_codes.patch combined, rebased patch].


---

Comment by ddrake created at 2010-06-15 02:36:00

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

Comment by ddrake created at 2010-06-15 03:58:51

Replying to [comment:15 mpatel]:
> I've attached a [attachment:trac_8641-doctest_exit_codes.patch combined, rebased patch].

I fixed the hunk reject and your patch seems to work fine. The exit codes match up with what `sage-doctest` says (although I didn't check exit code 4, since I don't know how to make the doctesting framework raise an exception). I tried with individual files, directories, with and without "-long", so it seems to work pretty well on my Ubuntu machine.


---

Comment by ddrake created at 2010-06-15 05:03:03

Replying to [comment:17 ddrake]:
> I fixed the hunk reject and your patch seems to work fine. The exit codes match up with what `sage-doctest` says (although I didn't check exit code 4, since I don't know how to make the doctesting framework raise an exception). I tried with individual files, directories, with and without "-long", so it seems to work pretty well on my Ubuntu machine.

I tested on bsd.math and the patch works there, too.


---

Comment by wjp created at 2010-06-15 08:13:21

Replying to [comment:17 ddrake]:
> (although I didn't check exit code 4, since I don't know how to make the doctesting framework raise an exception).

Should you still want to try, the example in ticket #7993 will trigger one of those.


---

Attachment

Modify `sage-ptest`, too.  Apply to 4.4.4.alpha0 + #8891.  Apply only this patch.


---

Comment by mpatel created at 2010-06-15 09:35:04

I've attached an attempt to get the same behavior for `sage -tp`.  The patch should apply to 4.4.4.alpha0 + #8891, unless I've `qfold`ed improperly.

It seems there's much room for improvement in `sage-ptest`.  For example, are the mutex locks really necessary?   I think both `skip` and `populatefilelist` run only in the main process.  But I suppose we could leave this and other potential oddities for #9224.


---

Comment by ddrake created at 2010-06-16 04:20:39

Changing assignee from tbd to ddrake.


---

Comment by ddrake created at 2010-06-16 04:20:39

mpatel: on line 337 of sage-ptest and line 176 of sage-test, your patch (attachment:trac_8641-doctest_exit_codes.2.patch) always sets err = 2. Can you change that to

```
   err = 2 | err
```

? Then, if doctesting a bunch of files and hit ctrl-c, you can tell the difference between "all the tests that ran passed" and "there was at least one doctest failure". (And other errors that might have happened before you hit ctrl-c.)


---

Comment by mpatel created at 2010-06-16 07:13:52

Use `err = err | 2` for `KeyboardInterrupt`.  Apply only this patch, to 4.4.4.alpha0 + #8891.


---

Attachment

Done.  [attachment:trac_8641-doctest_exit_codes.3.patch V3] uses `err = 2 | err` for `KeyboardInterrupt`s to both scripts.


---

Comment by ddrake created at 2010-06-16 15:00:25

This looks good, and I've used it a bunch and it works properly. But I'm listed as one of the authors, so perhaps I shouldn't flip it to positive review...wjp, can you look this over? I did check exit code 4 and that works properly.


---

Comment by wjp created at 2010-06-17 21:56:39

I'll try to find time to take a proper look friday or this weekend, but at first glance it seems like my comment 12 about `SIGINT`/`KeyboardInterrupt` is still valid.


---

Comment by ddrake created at 2010-06-18 03:17:14

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

Comment by wjp created at 2010-06-27 10:47:45

Hm, you're right. I may have mixed up process IDs the previous time I tried.

In any case, it might make sense to explicitly catch this `KeyboardInterrupt`?. But it's not strictly necessary since it'll be caught on a higher level anyway. (It may be something to save for further doctesting cleanup patches.)

I don't like the lines `err = err | test_file(F)`, `err = err | ret` and `err = err | 2`, though. They suggest that `err` is a bitmask or boolean, while it isn't. We could make it a bitmask, of course, so that 0 = all ok, 1 = failed tests, 2 = interrupted, 3 = failed tests and interrupted. Are there any other special cases we would want to consider in that case? Maybe a separate bit for timeouts? (See also #9316)


---

Comment by wjp created at 2010-07-06 20:45:49

Changing status from needs_review to positive_review.


---

Comment by wjp created at 2010-07-06 20:45:49

Mpatel pointed out that #9243 already tackles the powers-of-two thing.

I'm giving this a positive review, provided that #9243 is merged too. (I'll review that ticket too.)


---

Comment by mpatel created at 2010-07-07 03:13:38

To release manager:  Apply just [attachment:trac_8641-doctest_exit_codes.3.patch] to 4.5.alpha4.


---

Comment by ddrake created at 2010-07-22 07:39:35

Resolution: fixed


---

Comment by ddrake created at 2010-07-22 07:39:35

Merged attachment:trac_8641-doctest_exit_codes.3.patch in 4.5.2.alpha1.
