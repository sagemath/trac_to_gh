# Issue 9316: Spurious (?) "# File not found" error at end of doctests

archive/issues_009316.json:
```json
{
    "body": "Assignee: @wjp\n\nCC:  @nexttime\n\nMany people have reported a \"File not found\" error that is reported at the end of \"make test\" when *in fact* a timeout occurred. \n\nThis is caused by some weird code introduced in #7993 (see sage-test):\n\n```\n...\n    s = os.path.join(SAGE_ROOT, 'local', 'bin', 'sage-%s' % cmd) + ' \"%s\"' % F\n    err = os.system(s)\n    # On unix systems, the return value of os.system has the process return\n    # value in the second byte.\n    err = err // 256\n\n    # Check the process exit code that sage-doctest returns\n\n    if err == 1: # process exit code 1: File not found\n        failed.append(sage_test_command(F)+\" # File not found\")\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9316\n\n",
    "created_at": "2010-06-23T04:19:18Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Spurious (?) \"# File not found\" error at end of doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9316",
    "user": "https://github.com/williamstein"
}
```
Assignee: @wjp

CC:  @nexttime

Many people have reported a "File not found" error that is reported at the end of "make test" when *in fact* a timeout occurred. 

This is caused by some weird code introduced in #7993 (see sage-test):

```
...
    s = os.path.join(SAGE_ROOT, 'local', 'bin', 'sage-%s' % cmd) + ' "%s"' % F
    err = os.system(s)
    # On unix systems, the return value of os.system has the process return
    # value in the second byte.
    err = err // 256

    # Check the process exit code that sage-doctest returns

    if err == 1: # process exit code 1: File not found
        failed.append(sage_test_command(F)+" # File not found")
```


Issue created by migration from https://trac.sagemath.org/ticket/9316





---

archive/issue_comments_087644.json:
```json
{
    "body": "Example:\n\n```\n\nsage -t  \"devel/sage/sage/rings/number_field/number_field_rel.py\"\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\nTraceback (most recent call last):\n  File \"/home/john/sage-4.4.4.alpha1/local/bin/sage-doctest\", line 798, in <module>\n    test_file(argv[1], library_code = library_code)\n  File \"/home/john/sage-4.4.4.alpha1/local/bin/sage-doctest\", line 695, in test_file\n    print \"The doctested process was killed by signal %s\" % (-e)\nTypeError: bad operand type for unary -: 'NoneType'\n         [8319.2 s]\n```\n\nThe reason for the timeout was simply that I suspended my laptop for a couple of hours and then woke it up.  But at the end of the test (I was doing \"make test\" on 4.4.4.alpha1) the error message said\n\n```\n\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/rings/number_field/number_field_rel.py\" # File not found\n```\n",
    "created_at": "2010-06-23T04:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87644",
    "user": "https://github.com/JohnCremona"
}
```

Example:

```

sage -t  "devel/sage/sage/rings/number_field/number_field_rel.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
Traceback (most recent call last):
  File "/home/john/sage-4.4.4.alpha1/local/bin/sage-doctest", line 798, in <module>
    test_file(argv[1], library_code = library_code)
  File "/home/john/sage-4.4.4.alpha1/local/bin/sage-doctest", line 695, in test_file
    print "The doctested process was killed by signal %s" % (-e)
TypeError: bad operand type for unary -: 'NoneType'
         [8319.2 s]
```

The reason for the timeout was simply that I suspended my laptop for a couple of hours and then woke it up.  But at the end of the test (I was doing "make test" on 4.4.4.alpha1) the error message said

```

The following tests failed:


        sage -t  "devel/sage/sage/rings/number_field/number_field_rel.py" # File not found
```




---

archive/issue_comments_087645.json:
```json
{
    "body": "I agree a timeout can cause this. I tried the patch which is supposed to fix the Mathematica interface, but that timed out after 10,000 seconds with a \"File not found\" message. \n\nHowever, BSD.py is completing well within the time I've set as SAGE_TIMEOUT and SAGE_TIMEOUT_LONG, so I doubt the BSD.py issue was a simple timeout \n\n\n```\ndrkirkby@redstart:~$ echo $SAGE_TIMEOUT_LONG\n10000\ndrkirkby@redstart:~$ echo $SAGE_TIMEOUT     \n1000\n```\n\n\nBut BSD.py is taking 205 seconds\n\n\n```\ndrkirkby@redstart:~/sage-4.4.4.alpha1$ ./sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/BSD.py\"\n         [205.5 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 205.5 seconds\n```\n\n\nSure BSD.py will take longer if the machine is more heavily loaded, but it would need a **huge** load to make the test take over 10000 seconds. The load would have to go up by a factor of 48! Given it's my own machine, and nobody else uses it, I have a pretty good idea the load would not have risen that much. \n\nMy Blade 1000 does not have a lot of RAM (only 2 GB), so potentially it could swap if it run out of RAM, but I don't believe that was the problem. It certainly does not have any power saving features - that's why I keep it in the garage and use it as a heater in the Winter! That machine does not hybernate! \n\nDave",
    "created_at": "2010-06-23T05:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87645",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I agree a timeout can cause this. I tried the patch which is supposed to fix the Mathematica interface, but that timed out after 10,000 seconds with a "File not found" message. 

However, BSD.py is completing well within the time I've set as SAGE_TIMEOUT and SAGE_TIMEOUT_LONG, so I doubt the BSD.py issue was a simple timeout 


```
drkirkby@redstart:~$ echo $SAGE_TIMEOUT_LONG
10000
drkirkby@redstart:~$ echo $SAGE_TIMEOUT     
1000
```


But BSD.py is taking 205 seconds


```
drkirkby@redstart:~/sage-4.4.4.alpha1$ ./sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py
sage -t -long "devel/sage/sage/schemes/elliptic_curves/BSD.py"
         [205.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 205.5 seconds
```


Sure BSD.py will take longer if the machine is more heavily loaded, but it would need a **huge** load to make the test take over 10000 seconds. The load would have to go up by a factor of 48! Given it's my own machine, and nobody else uses it, I have a pretty good idea the load would not have risen that much. 

My Blade 1000 does not have a lot of RAM (only 2 GB), so potentially it could swap if it run out of RAM, but I don't believe that was the problem. It certainly does not have any power saving features - that's why I keep it in the garage and use it as a heater in the Winter! That machine does not hybernate! 

Dave



---

archive/issue_comments_087646.json:
```json
{
    "body": "This appears to be caused by timeouts not being properly handled by `sage-doctest`. It prints the error message, but then doesn't actually do anything with it. It looks like I completely missed that case when doing #7993. This also explains the strange exception John is seeing. It's reaching code that shouldn't be reached in this case.\n\nIn the patch I'm attaching, I'm making `sage-doctest` return exit code 5 for a time out, and `sage-test` and `sage-ptest` will also interpret that that way.\n\n(Note that this will conflict with #8641, but the conflict is easy to resolve.)",
    "created_at": "2010-06-23T08:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87646",
    "user": "https://github.com/wjp"
}
```

This appears to be caused by timeouts not being properly handled by `sage-doctest`. It prints the error message, but then doesn't actually do anything with it. It looks like I completely missed that case when doing #7993. This also explains the strange exception John is seeing. It's reaching code that shouldn't be reached in this case.

In the patch I'm attaching, I'm making `sage-doctest` return exit code 5 for a time out, and `sage-test` and `sage-ptest` will also interpret that that way.

(Note that this will conflict with #8641, but the conflict is easy to resolve.)



---

archive/issue_comments_087647.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-23T08:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87647",
    "user": "https://github.com/wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087648.json:
```json
{
    "body": "I won't say positive review 100% because someone who knows all the ins and outs should have a quick look at it.    But it works as advertised.  I do wonder if there need to be two separate tests for \n\n```\n\nsage -t  \"devel/sage/sage/calculus/calculus.py\"             \n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n\t [556.2 s]\n```\n\nor if one could immediately sys.exit(5) instead of having two separate timeout messages?  Or this may be a feature - one for the process, one for the file.",
    "created_at": "2010-06-23T14:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87648",
    "user": "https://github.com/kcrisman"
}
```

I won't say positive review 100% because someone who knows all the ins and outs should have a quick look at it.    But it works as advertised.  I do wonder if there need to be two separate tests for 

```

sage -t  "devel/sage/sage/calculus/calculus.py"             
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
	 [556.2 s]
```

or if one could immediately sys.exit(5) instead of having two separate timeout messages?  Or this may be a feature - one for the process, one for the file.



---

archive/issue_comments_087649.json:
```json
{
    "body": "I'm still suspicious that the \"File not found\" error I got with BSD.py (#9273)is anything to do with a timeout problem. Why should a test take 205 seconds on one occasion and over 10000 seconds on another?",
    "created_at": "2010-06-25T06:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87649",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm still suspicious that the "File not found" error I got with BSD.py (#9273)is anything to do with a timeout problem. Why should a test take 205 seconds on one occasion and over 10000 seconds on another?



---

archive/issue_comments_087650.json:
```json
{
    "body": "I'd be ok with directly doing a `sys.exit(5)`, I think. Or maybe removing the `print` statements from after the `kill` calls, and only leave the `print` with the `sys.exit(5)` at the end in place.\n\nAnother thing in there that doesn't seem to make much sense is the '`err`' string, which never seems to be set, but still is used in one of the `KeyboardInterrupt` checks.",
    "created_at": "2010-06-25T08:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87650",
    "user": "https://github.com/wjp"
}
```

I'd be ok with directly doing a `sys.exit(5)`, I think. Or maybe removing the `print` statements from after the `kill` calls, and only leave the `print` with the `sys.exit(5)` at the end in place.

Another thing in there that doesn't seem to make much sense is the '`err`' string, which never seems to be set, but still is used in one of the `KeyboardInterrupt` checks.



---

archive/issue_comments_087651.json:
```json
{
    "body": "I submitted a new patch that uses exit code 6 instead of 5, since it turns out 5 is used internally by `sage-ptest`.",
    "created_at": "2010-06-27T11:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87651",
    "user": "https://github.com/wjp"
}
```

I submitted a new patch that uses exit code 6 instead of 5, since it turns out 5 is used internally by `sage-ptest`.



---

archive/issue_comments_087652.json:
```json
{
    "body": "Attachment [scripts9316_timeout_rebased.patch](tarball://root/attachments/some-uuid/ticket9316/scripts9316_timeout_rebased.patch) by @wjp created at 2010-07-06 20:59:47\n\nrebased after #8641 and #9243",
    "created_at": "2010-07-06T20:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87652",
    "user": "https://github.com/wjp"
}
```

Attachment [scripts9316_timeout_rebased.patch](tarball://root/attachments/some-uuid/ticket9316/scripts9316_timeout_rebased.patch) by @wjp created at 2010-07-06 20:59:47

rebased after #8641 and #9243



---

archive/issue_comments_087653.json:
```json
{
    "body": "Attachment [scripts9316_timeout.patch](tarball://root/attachments/some-uuid/ticket9316/scripts9316_timeout.patch) by @wjp created at 2010-07-06 21:03:09",
    "created_at": "2010-07-06T21:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87653",
    "user": "https://github.com/wjp"
}
```

Attachment [scripts9316_timeout.patch](tarball://root/attachments/some-uuid/ticket9316/scripts9316_timeout.patch) by @wjp created at 2010-07-06 21:03:09



---

archive/issue_comments_087654.json:
```json
{
    "body": "I removed the second print statement so there is no longer a double TIMED OUT message, and rebased the patch to apply after #8641 and #9243.",
    "created_at": "2010-07-06T21:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87654",
    "user": "https://github.com/wjp"
}
```

I removed the second print statement so there is no longer a double TIMED OUT message, and rebased the patch to apply after #8641 and #9243.



---

archive/issue_comments_087655.json:
```json
{
    "body": "I get\n\n```sh\n$ env SAGE_TIMEOUT=10 ./sage -t devel/sage/sage/rings/number_field/number_field_rel.py \nsage -t  \"devel/sage/sage/rings/number_field/number_field_rel.py\"\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n\n         [10.2 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/rings/number_field/number_field_rel.py\" # Time out\nTotal time for all tests: 10.2 seconds\n$ echo $?\n64\n```\n  \n\nMaybe we should print a brief message about increasing `SAGE_TIMEOUT` and `SAGE_TIMEOUT_LONG`, if at least one test times out?\n\nTo release manager: Apply only [attachment:scripts9316_timeout_rebased.patch] to 4.5.alpha4 + #8641 + #9243.",
    "created_at": "2010-07-07T03:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87655",
    "user": "https://github.com/qed777"
}
```

I get

```sh
$ env SAGE_TIMEOUT=10 ./sage -t devel/sage/sage/rings/number_field/number_field_rel.py 
sage -t  "devel/sage/sage/rings/number_field/number_field_rel.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

         [10.2 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/rings/number_field/number_field_rel.py" # Time out
Total time for all tests: 10.2 seconds
$ echo $?
64
```
  

Maybe we should print a brief message about increasing `SAGE_TIMEOUT` and `SAGE_TIMEOUT_LONG`, if at least one test times out?

To release manager: Apply only [attachment:scripts9316_timeout_rebased.patch] to 4.5.alpha4 + #8641 + #9243.



---

archive/issue_comments_087656.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-07T03:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87656",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087657.json:
```json
{
    "body": "Related tickets: #9224, #9225.  Suggestions are welcome!",
    "created_at": "2010-07-07T03:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87657",
    "user": "https://github.com/qed777"
}
```

Related tickets: #9224, #9225.  Suggestions are welcome!



---

archive/issue_comments_087658.json:
```json
{
    "body": "Replying to [comment:9 mpatel]:\n \n> Maybe we should print a brief message about increasing `SAGE_TIMEOUT` and `SAGE_TIMEOUT_LONG`, if at least one test times out?\n\nThat does seem very sensible, since these options are not well known. They are now documented in #8263, which adds them to the Installation Guide, but I would agree it would be useful to print this. \n\nAlso see #9449 for yet more issues with doctesting, where the results are confusing. I don't know if tests have passed or failed in some cases.",
    "created_at": "2010-07-08T11:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87658",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:9 mpatel]:
 
> Maybe we should print a brief message about increasing `SAGE_TIMEOUT` and `SAGE_TIMEOUT_LONG`, if at least one test times out?

That does seem very sensible, since these options are not well known. They are now documented in #8263, which adds them to the Installation Guide, but I would agree it would be useful to print this. 

Also see #9449 for yet more issues with doctesting, where the results are confusing. I don't know if tests have passed or failed in some cases.



---

archive/issue_comments_087659.json:
```json
{
    "body": "Merged attachment:scripts9316_timeout_rebased.patch in 4.5.2.alpha1.",
    "created_at": "2010-07-22T07:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87659",
    "user": "https://github.com/dandrake"
}
```

Merged attachment:scripts9316_timeout_rebased.patch in 4.5.2.alpha1.



---

archive/issue_comments_087660.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T07:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9316#issuecomment-87660",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_events_022960.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-22T07:59:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9316",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9316#event-22960"
}
```
