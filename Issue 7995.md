# Issue 7995: sage-test doesn't handle all of sage-doctest's return values

archive/issues_007995.json:
```json
{
    "body": "Assignee: tbd\n\nThe `sage-doctest` script returns some status info in its exit code, like if it was aborted with a `KeyboardInterrupt`. The `sage-ptest` script interprets this information, but `sage-test` mostly ignores it.\n\nOne symptom is that Ctrl-C-ing a `sage -t` run of multiple files doesn't work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7995\n\n",
    "created_at": "2010-01-19T07:38:35Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "sage-test doesn't handle all of sage-doctest's return values",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7995",
    "user": "@wjp"
}
```
Assignee: tbd

The `sage-doctest` script returns some status info in its exit code, like if it was aborted with a `KeyboardInterrupt`. The `sage-ptest` script interprets this information, but `sage-test` mostly ignores it.

One symptom is that Ctrl-C-ing a `sage -t` run of multiple files doesn't work.

Issue created by migration from https://trac.sagemath.org/ticket/7995





---

archive/issue_comments_069828.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T02:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69828",
    "user": "@wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069829.json:
```json
{
    "body": "Patch attached.\n\nIn the future we may want to merge the sage-ptest and sage-test scripts entirely. They have a lot of duplicate code and minor unnecessary differences.",
    "created_at": "2010-01-20T02:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69829",
    "user": "@wjp"
}
```

Patch attached.

In the future we may want to merge the sage-ptest and sage-test scripts entirely. They have a lot of duplicate code and minor unnecessary differences.



---

archive/issue_comments_069830.json:
```json
{
    "body": "Attachment [scripts_7995_sage-test_error_handling.patch](tarball://root/attachments/some-uuid/ticket7995/scripts_7995_sage-test_error_handling.patch) by @wjp created at 2010-01-20 05:16:15",
    "created_at": "2010-01-20T05:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69830",
    "user": "@wjp"
}
```

Attachment [scripts_7995_sage-test_error_handling.patch](tarball://root/attachments/some-uuid/ticket7995/scripts_7995_sage-test_error_handling.patch) by @wjp created at 2010-01-20 05:16:15



---

archive/issue_comments_069831.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T08:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69831",
    "user": "@nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069832.json:
```json
{
    "body": "I don't know much the doctest framework. But the code looks good, and this removes two seriously annoying misfeatures of doctests. Thanks so much for scratching this itch for me!\n\nQuick remarks:\n\n- When there is an exception in the doctesting framework; will we get\n  a traceback? That would be most handy!\n\n- in \"... Check the process exit codes ...\": codes -> code?\n\n- The following two comments seem contradictory. Or am I\n  misunderstanding something?\n\n> # Return value in process exit code: \n> # 0: all tests passed \n> # 1: file not found \n> # 2: KeyboardInterrupt \n> # 3: doctest process was terminated by a signal \n> # 4: the doctesting framework raised an exception \n> # 100: failed doctests \n> #################################################################### \n>\n> def test_code(filename): \n>     # Return value in the doctest process exit code: \n>     # 0: everything passed \n>     # 1-253: number of failed doctests \n>     # 254: >= 254 doctests failed \n>     # 255: exception raised by doctesting framework",
    "created_at": "2010-01-20T08:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69832",
    "user": "@nthiery"
}
```

I don't know much the doctest framework. But the code looks good, and this removes two seriously annoying misfeatures of doctests. Thanks so much for scratching this itch for me!

Quick remarks:

- When there is an exception in the doctesting framework; will we get
  a traceback? That would be most handy!

- in "... Check the process exit codes ...": codes -> code?

- The following two comments seem contradictory. Or am I
  misunderstanding something?

> # Return value in process exit code: 
> # 0: all tests passed 
> # 1: file not found 
> # 2: KeyboardInterrupt 
> # 3: doctest process was terminated by a signal 
> # 4: the doctesting framework raised an exception 
> # 100: failed doctests 
> #################################################################### 
>
> def test_code(filename): 
>     # Return value in the doctest process exit code: 
>     # 0: everything passed 
>     # 1-253: number of failed doctests 
>     # 254: >= 254 doctests failed 
>     # 255: exception raised by doctesting framework



---

archive/issue_comments_069833.json:
```json
{
    "body": "Sorry, I screwed up my citation. Here it is again.\n\n- The following two comments seem contradictory. Or am I\n  misunderstanding something?\n\n\n```\n # Return value in process exit code: \n # 0: all tests passed \n # 1: file not found \n # 2: KeyboardInterrupt \n # 3: doctest process was terminated by a signal \n # 4: the doctesting framework raised an exception \n # 100: failed doctests \n #################################################################### \n\n def test_code(filename): \n     # Return value in the doctest process exit code: \n     # 0: everything passed \n     # 1-253: number of failed doctests \n     # 254: >= 254 doctests failed \n     # 255: exception raised by doctesting framework \n```\n",
    "created_at": "2010-01-20T09:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69833",
    "user": "@nthiery"
}
```

Sorry, I screwed up my citation. Here it is again.

- The following two comments seem contradictory. Or am I
  misunderstanding something?


```
 # Return value in process exit code: 
 # 0: all tests passed 
 # 1: file not found 
 # 2: KeyboardInterrupt 
 # 3: doctest process was terminated by a signal 
 # 4: the doctesting framework raised an exception 
 # 100: failed doctests 
 #################################################################### 

 def test_code(filename): 
     # Return value in the doctest process exit code: 
     # 0: everything passed 
     # 1-253: number of failed doctests 
     # 254: >= 254 doctests failed 
     # 255: exception raised by doctesting framework 
```




---

archive/issue_comments_069834.json:
```json
{
    "body": "Replying to [comment:4 nthiery]:\n> Sorry, I screwed up my citation. Here it is again.\n\nOops again. This remark is actually about #7993. I was looking at both, and got confused.",
    "created_at": "2010-01-20T09:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69834",
    "user": "@nthiery"
}
```

Replying to [comment:4 nthiery]:
> Sorry, I screwed up my citation. Here it is again.

Oops again. This remark is actually about #7993. I was looking at both, and got confused.



---

archive/issue_comments_069835.json:
```json
{
    "body": "Thanks for the feedback.\n\nThe `sage-doctest` script generates a new python file that runs the actual doctests, and runs this script in a seperate thread. The second block of process exit codes are for this 'inner' doctest process. I'll clarify the confusing comment (and fix the typo you mentioned).\n\nAs for the exception: you can get a traceback if you re-run with the -verbose. Do you think we should show them by default?",
    "created_at": "2010-01-20T17:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69835",
    "user": "@wjp"
}
```

Thanks for the feedback.

The `sage-doctest` script generates a new python file that runs the actual doctests, and runs this script in a seperate thread. The second block of process exit codes are for this 'inner' doctest process. I'll clarify the confusing comment (and fix the typo you mentioned).

As for the exception: you can get a traceback if you re-run with the -verbose. Do you think we should show them by default?



---

archive/issue_comments_069836.json:
```json
{
    "body": "I attached a new patch to #7993 that changes the exit code comments.",
    "created_at": "2010-01-20T18:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69836",
    "user": "@wjp"
}
```

I attached a new patch to #7993 that changes the exit code comments.



---

archive/issue_comments_069837.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-23T01:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69837",
    "user": "@aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069838.json:
```json
{
    "body": "I played with this a bit and it works well.",
    "created_at": "2010-01-23T01:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69838",
    "user": "@aghitza"
}
```

I played with this a bit and it works well.



---

archive/issue_comments_069839.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-23T01:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69839",
    "user": "@aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069840.json:
```json
{
    "body": "Merged in the script repository.",
    "created_at": "2010-01-23T09:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69840",
    "user": "mvngu"
}
```

Merged in the script repository.



---

archive/issue_comments_069841.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T09:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69841",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_069842.json:
```json
{
    "body": "The patch here doesn't work; it exits sage-doctest with sys.exit(2), and then munges the error code with \"err = err // 256\" -- that is, it does floor division by 256, so the 2 becomes 0 and KeyboardInterrupts are never detected!\n\nI hope to fix this while working on #8641.",
    "created_at": "2010-04-13T13:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69842",
    "user": "@dandrake"
}
```

The patch here doesn't work; it exits sage-doctest with sys.exit(2), and then munges the error code with "err = err // 256" -- that is, it does floor division by 256, so the 2 becomes 0 and KeyboardInterrupts are never detected!

I hope to fix this while working on #8641.



---

archive/issue_comments_069843.json:
```json
{
    "body": "I tested this, and it worked for me, as well as matching what the python docs say it does on unix systems. Does it not work on your system?\n\nThe python docs for `os.system`:\n\n\n```\nOn Unix, the return value is the exit status of the process encoded in\nthe format specified for wait().\n```\n\n\nAnd for `os.wait`:\n\n\n```\nWait for completion of a child process, and return a tuple containing\nits pid and exit status indication: a 16-bit number, whose low byte is\nthe signal number that killed the process, and whose high byte is the\nexit status (if the signal number is zero); the high bit of the low byte\nis set if a core file was produced. Availability: Unix.\n```\n",
    "created_at": "2010-04-13T13:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69843",
    "user": "@wjp"
}
```

I tested this, and it worked for me, as well as matching what the python docs say it does on unix systems. Does it not work on your system?

The python docs for `os.system`:


```
On Unix, the return value is the exit status of the process encoded in
the format specified for wait().
```


And for `os.wait`:


```
Wait for completion of a child process, and return a tuple containing
its pid and exit status indication: a 16-bit number, whose low byte is
the signal number that killed the process, and whose high byte is the
exit status (if the signal number is zero); the high bit of the low byte
is set if a core file was produced. Availability: Unix.
```




---

archive/issue_comments_069844.json:
```json
{
    "body": "See #8641 for a followup.",
    "created_at": "2010-04-13T20:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69844",
    "user": "@jhpalmieri"
}
```

See #8641 for a followup.



---

archive/issue_comments_069845.json:
```json
{
    "body": "Replying to [comment:12 wjp]:\n> I tested this, and it worked for me, as well as matching what the python docs say it does on unix systems. Does it not work on your system?\n\nNo, it doesn't. I'll work on this more, but I know that, on my Ubuntu 9.10 system, if I ctrl-c while running tests on a bunch of files, it doesn't interrupt the whole process. In sage-test, I have this:\n\n```\nprint 'finished with %s, err: %s' % (F, err)\nerr = err // 256\nprint 'finished with %s, err: %s' % (F, err)\n```\n\nand here's what I get:\n\n```\ndrake@sagenb:~/s/sage-4.3.5$ ./sage -t devel/sage/sage/combinat/t*.py\nsage -t  \"devel/sage/sage/combinat/tableau.py\"              \n^CKeyboardInterrupt -- interrupted after 2.3 seconds!\nfinished with devel/sage/sage/combinat/tableau.py, err: 2\nfinished with devel/sage/sage/combinat/tableau.py, err: 0\n         [2.4 s]\nsage -t  \"devel/sage/sage/combinat/tools.py\"                \nfinished with devel/sage/sage/combinat/tools.py, err: 0\nfinished with devel/sage/sage/combinat/tools.py, err: 0\n         [1.6 s]\nsage -t  \"devel/sage/sage/combinat/tuple.py\"                \nfinished with devel/sage/sage/combinat/tuple.py, err: 0\nfinished with devel/sage/sage/combinat/tuple.py, err: 0\n         [2.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 6.2 seconds\n```\n\n\nI'm not sure why this isn't working.",
    "created_at": "2010-04-13T22:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69845",
    "user": "@dandrake"
}
```

Replying to [comment:12 wjp]:
> I tested this, and it worked for me, as well as matching what the python docs say it does on unix systems. Does it not work on your system?

No, it doesn't. I'll work on this more, but I know that, on my Ubuntu 9.10 system, if I ctrl-c while running tests on a bunch of files, it doesn't interrupt the whole process. In sage-test, I have this:

```
print 'finished with %s, err: %s' % (F, err)
err = err // 256
print 'finished with %s, err: %s' % (F, err)
```

and here's what I get:

```
drake@sagenb:~/s/sage-4.3.5$ ./sage -t devel/sage/sage/combinat/t*.py
sage -t  "devel/sage/sage/combinat/tableau.py"              
^CKeyboardInterrupt -- interrupted after 2.3 seconds!
finished with devel/sage/sage/combinat/tableau.py, err: 2
finished with devel/sage/sage/combinat/tableau.py, err: 0
         [2.4 s]
sage -t  "devel/sage/sage/combinat/tools.py"                
finished with devel/sage/sage/combinat/tools.py, err: 0
finished with devel/sage/sage/combinat/tools.py, err: 0
         [1.6 s]
sage -t  "devel/sage/sage/combinat/tuple.py"                
finished with devel/sage/sage/combinat/tuple.py, err: 0
finished with devel/sage/sage/combinat/tuple.py, err: 0
         [2.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 6.2 seconds
```


I'm not sure why this isn't working.



---

archive/issue_comments_069846.json:
```json
{
    "body": "I put in a few print statements, like Dan did:\n\n```\n    print err,\n    err = err // 256\n    print err\n```\n\nOn my iMac running OS X 10.6, when I hit ctrl-C, I see\n\n```\n515 2\n```\n\nwhich looks okay.\n\nOn sage.math, I see\n\n```\n2 0\n```\n\nwhich doesn't.",
    "created_at": "2010-04-13T22:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7995#issuecomment-69846",
    "user": "@jhpalmieri"
}
```

I put in a few print statements, like Dan did:

```
    print err,
    err = err // 256
    print err
```

On my iMac running OS X 10.6, when I hit ctrl-C, I see

```
515 2
```

which looks okay.

On sage.math, I see

```
2 0
```

which doesn't.
