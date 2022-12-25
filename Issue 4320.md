# Issue 4320: linear codes improvements

archive/issues_004320.json:
```json
{
    "body": "Assignee: @rlmill\n\nThis is a patch which incorporates several changes in linear_codes.py which should speed up (and in some cases do:-) some coding theory computations considerably. It adds interfaces to Cython and C functions of Robert Miller, CJ Tjhal, and Jeffery Leon. \nSpeed up of minimum_distance (for codes over GF(2) and GF(3)), the spectrum (=weight_distribution), and permutation_automorphism_group are expected and in most cases achieved. (Also a new function is_permutation_equivalent was added, which interfaces with Robert Miller's double coset partition refinement code.) \n\nA few points that the referee might want to look at in particular. \n(1) At least one of the functions (code2leon) opens, reads and writes, and closes files. I think I did it correctly, but I read keeping files open is a bad thing, so I hope it was done correctly.\n(2) There is a ridiculously slow line which lists the codewords of a given weight. For some reason, GAP (and Guava) is much much faster. It occurs in the permutation_automorphism_group and is commented so you can find it easily. Maybe I am creating the list wrong?\n\nIn any case, it passes sage -testall and optional methods were added to the problematical methods, so one always has the option of using the fastest method.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4320\n\n",
    "created_at": "2008-10-18T20:31:09Z",
    "labels": [
        "component: coding theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "linear codes improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4320",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @rlmill

This is a patch which incorporates several changes in linear_codes.py which should speed up (and in some cases do:-) some coding theory computations considerably. It adds interfaces to Cython and C functions of Robert Miller, CJ Tjhal, and Jeffery Leon. 
Speed up of minimum_distance (for codes over GF(2) and GF(3)), the spectrum (=weight_distribution), and permutation_automorphism_group are expected and in most cases achieved. (Also a new function is_permutation_equivalent was added, which interfaces with Robert Miller's double coset partition refinement code.) 

A few points that the referee might want to look at in particular. 
(1) At least one of the functions (code2leon) opens, reads and writes, and closes files. I think I did it correctly, but I read keeping files open is a bad thing, so I hope it was done correctly.
(2) There is a ridiculously slow line which lists the codewords of a given weight. For some reason, GAP (and Guava) is much much faster. It occurs in the permutation_automorphism_group and is commented so you can find it easily. Maybe I am creating the list wrong?

In any case, it passes sage -testall and optional methods were added to the problematical methods, so one always has the option of using the fastest method.


Issue created by migration from https://trac.sagemath.org/ticket/4320





---

archive/issue_comments_031556.json:
```json
{
    "body": "based on 3.1.4",
    "created_at": "2008-10-18T20:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31556",
    "user": "https://github.com/wdjoyner"
}
```

based on 3.1.4



---

archive/issue_comments_031557.json:
```json
{
    "body": "Attachment [trac_4320-linear-codes.patch](tarball://root/attachments/some-uuid/ticket4320/trac_4320-linear-codes.patch) by @wdjoyner created at 2008-10-18 22:56:04",
    "created_at": "2008-10-18T22:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31557",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4320-linear-codes.patch](tarball://root/attachments/some-uuid/ticket4320/trac_4320-linear-codes.patch) by @wdjoyner created at 2008-10-18 22:56:04



---

archive/issue_comments_031558.json:
```json
{
    "body": "David,\n\nThe code here looks pretty good. I think it's ready to merge except for one thing: When you create a file to be read by Leon's programs (or for any other reason, really), you should be creating it in a temp directory which gets automatically cleaned up. You can get one by doing `from sage.misc.misc import SAGE_TMP`.",
    "created_at": "2008-10-20T17:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31558",
    "user": "https://github.com/rlmill"
}
```

David,

The code here looks pretty good. I think it's ready to merge except for one thing: When you create a file to be read by Leon's programs (or for any other reason, really), you should be creating it in a temp directory which gets automatically cleaned up. You can get one by doing `from sage.misc.misc import SAGE_TMP`.



---

archive/issue_comments_031559.json:
```json
{
    "body": "Another thing: SAGE_ROOT can also easily be accessed and things like\n\n```\nrt = commands.getoutput(\"echo $SAGE_ROOT\")\n```\n\nare bad. Another thing is the hard coding of the executable name since one has to append \".exe\" on Cygwin for example.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-20T17:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31559",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Another thing: SAGE_ROOT can also easily be accessed and things like

```
rt = commands.getoutput("echo $SAGE_ROOT")
```

are bad. Another thing is the hard coding of the executable name since one has to append ".exe" on Cygwin for example.

Cheers,

Michael



---

archive/issue_comments_031560.json:
```json
{
    "body": "Here's a session that illustrates several of the things you need to change\nin this patch, evidently:\n\n```\nsage: sage.misc.misc.SAGE_ROOT        # sage root dir\n'/home/was/build/sage-3.1.3.alpha3'\nsage: sage.misc.misc.SAGE_TMP         # location of sage tmp dir; deleted on sage exit\n'/home/was/.sage//temp/sage/21351/'\nsage: sage.misc.misc.tmp_filename()   # a temp filename, which you can use\n'/home/was/.sage//temp/sage/21351//tmp_0'\nsage: sage.misc.misc.tmp_dir()\n'/home/was/.sage/temp/sage/21351/dir_0'  # creates a temp directory for you\n```\n",
    "created_at": "2008-10-20T19:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31560",
    "user": "https://github.com/williamstein"
}
```

Here's a session that illustrates several of the things you need to change
in this patch, evidently:

```
sage: sage.misc.misc.SAGE_ROOT        # sage root dir
'/home/was/build/sage-3.1.3.alpha3'
sage: sage.misc.misc.SAGE_TMP         # location of sage tmp dir; deleted on sage exit
'/home/was/.sage//temp/sage/21351/'
sage: sage.misc.misc.tmp_filename()   # a temp filename, which you can use
'/home/was/.sage//temp/sage/21351//tmp_0'
sage: sage.misc.misc.tmp_dir()
'/home/was/.sage/temp/sage/21351/dir_0'  # creates a temp directory for you
```




---

archive/issue_comments_031561.json:
```json
{
    "body": "Thanks for all these great comments. \nI have had the patch ready for a day or so now but am having trouble with the process. Problem: I run sage -t on linear_codes.py and code_constructions.py. They pass. sage -testall fails every time with this:\n\n\n```\n sage -t  devel/sage/sage/coding/linear_code.py              **********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.2.alpha0/tmp/linear_code.py\", line 1950:\n    sage: C.spectrum(method=\"leon\")\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.2.alpha0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_44[10]>\", line 1, in <module>\n        C.spectrum(method=\"leon\")###line 1950:\n    sage: C.spectrum(method=\"leon\")\n      File \"/home/wdj/sagefiles/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 2009, in spectrum\n        Wts[x[0]]=x[1]\n    IndexError: list assignment index out of range\n**********************************************************************\n```\n\nI cannot figure this one out.\n\nAny ideas?\n\nThe new patch is rebased on 3.2.alpha0 and does not (I'm pretty sure) depend on the other patch.",
    "created_at": "2008-10-23T00:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31561",
    "user": "https://github.com/wdjoyner"
}
```

Thanks for all these great comments. 
I have had the patch ready for a day or so now but am having trouble with the process. Problem: I run sage -t on linear_codes.py and code_constructions.py. They pass. sage -testall fails every time with this:


```
 sage -t  devel/sage/sage/coding/linear_code.py              **********************************************************************
File "/home/wdj/sagefiles/sage-3.2.alpha0/tmp/linear_code.py", line 1950:
    sage: C.spectrum(method="leon")
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.2.alpha0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[10]>", line 1, in <module>
        C.spectrum(method="leon")###line 1950:
    sage: C.spectrum(method="leon")
      File "/home/wdj/sagefiles/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 2009, in spectrum
        Wts[x[0]]=x[1]
    IndexError: list assignment index out of range
**********************************************************************
```

I cannot figure this one out.

Any ideas?

The new patch is rebased on 3.2.alpha0 and does not (I'm pretty sure) depend on the other patch.



---

archive/issue_comments_031562.json:
```json
{
    "body": "based on 3.2.alpha0 and is a stand-alone patch.",
    "created_at": "2008-10-23T00:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31562",
    "user": "https://github.com/wdjoyner"
}
```

based on 3.2.alpha0 and is a stand-alone patch.



---

archive/issue_comments_031563.json:
```json
{
    "body": "Attachment [trac_4320-linear-codes2.patch](tarball://root/attachments/some-uuid/ticket4320/trac_4320-linear-codes2.patch) by @wdjoyner created at 2008-10-23 11:02:36\n\nI wonder if this is somehow because of the fact that if you run the Leon code command wtdist on the command line directly you get \"smash stack\" and (memory errors resulting in?) traceback messages? This is a known issue (discovered by Robert Miller and Tom Boothby) and I have added a warning line to the docstring.\nI don't understand when this does not arise for sage -t and does for sage -testall though, so easily could be completely wrong.",
    "created_at": "2008-10-23T11:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31563",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4320-linear-codes2.patch](tarball://root/attachments/some-uuid/ticket4320/trac_4320-linear-codes2.patch) by @wdjoyner created at 2008-10-23 11:02:36

I wonder if this is somehow because of the fact that if you run the Leon code command wtdist on the command line directly you get "smash stack" and (memory errors resulting in?) traceback messages? This is a known issue (discovered by Robert Miller and Tom Boothby) and I have added a warning line to the docstring.
I don't understand when this does not arise for sage -t and does for sage -testall though, so easily could be completely wrong.



---

archive/issue_comments_031564.json:
```json
{
    "body": "This patch also has this property for 3.1.4 (ie, patch applies cleanly, sage -testall fails for linear_code but sage -t passes for linear_code):\n\n\n```\nwdj@hera:~/sagefiles/sage-3.1.4$ ./sage -testall       \n\n<snip>\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage/sage/coding/linear_code.py\nTotal time for all tests: 5448.1 seconds\nPlease see /home/wdj/sagefiles/sage-3.1.4/tmp/test.log for the complete log from this test.\nwdj@hera:~/sagefiles/sage-3.1.4$ ./sage -t  devel/sage/sage/coding/linear_code.py\nsage -t  devel/sage/sage/coding/linear_code.py\n         [17.8 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 17.8 seconds\n\n```\n\nHas anyone seen this kind of behaviour before?",
    "created_at": "2008-10-24T09:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31564",
    "user": "https://github.com/wdjoyner"
}
```

This patch also has this property for 3.1.4 (ie, patch applies cleanly, sage -testall fails for linear_code but sage -t passes for linear_code):


```
wdj@hera:~/sagefiles/sage-3.1.4$ ./sage -testall       

<snip>

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/coding/linear_code.py
Total time for all tests: 5448.1 seconds
Please see /home/wdj/sagefiles/sage-3.1.4/tmp/test.log for the complete log from this test.
wdj@hera:~/sagefiles/sage-3.1.4$ ./sage -t  devel/sage/sage/coding/linear_code.py
sage -t  devel/sage/sage/coding/linear_code.py
         [17.8 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 17.8 seconds

```

Has anyone seen this kind of behaviour before?



---

archive/issue_comments_031565.json:
```json
{
    "body": "I installed sage-3.2.alpha0 on an intel macbook, OS10.4, and pretty much the same thing happened. (linear_code failed sage -testall but passed sage -t.) \nHowever, this time group_algebra also failed, though it seems completely unrelated. (I don't use that module in this version - but it's on the TODO list!)",
    "created_at": "2008-10-25T01:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31565",
    "user": "https://github.com/wdjoyner"
}
```

I installed sage-3.2.alpha0 on an intel macbook, OS10.4, and pretty much the same thing happened. (linear_code failed sage -testall but passed sage -t.) 
However, this time group_algebra also failed, though it seems completely unrelated. (I don't use that module in this version - but it's on the TODO list!)



---

archive/issue_comments_031566.json:
```json
{
    "body": "I think I might have a vague clue why this latest patch passes sage -t but not sage -testall (this happens for different versions of sage and on both ubuntu and mac OS10.4, as well). The main different in this case between sage -t and sage -testall is that sage -testall records the results in a logfile and sage -t does not. The command line version of the spectrum(method=\"leon\") method has a traceback. Somehow I think this messes with the buffer and then logging is screwed up.\n\nIn any case, the attached patch (which is to be applied *after* the patch number 2) fixes the docstrings so that (1) the tests pass (sage -testall as well as sage -t) and (2) I didn't just delete test computations (which I thought would be \"cheating\":-), but just rephrased them.",
    "created_at": "2008-10-26T14:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31566",
    "user": "https://github.com/wdjoyner"
}
```

I think I might have a vague clue why this latest patch passes sage -t but not sage -testall (this happens for different versions of sage and on both ubuntu and mac OS10.4, as well). The main different in this case between sage -t and sage -testall is that sage -testall records the results in a logfile and sage -t does not. The command line version of the spectrum(method="leon") method has a traceback. Somehow I think this messes with the buffer and then logging is screwed up.

In any case, the attached patch (which is to be applied *after* the patch number 2) fixes the docstrings so that (1) the tests pass (sage -testall as well as sage -t) and (2) I didn't just delete test computations (which I thought would be "cheating":-), but just rephrased them.



---

archive/issue_comments_031567.json:
```json
{
    "body": "Attachment [trac_4320-linear-codes3.patch](tarball://root/attachments/some-uuid/ticket4320/trac_4320-linear-codes3.patch) by @wdjoyner created at 2008-10-26 14:30:40\n\nalso based on 3.2.alpha0. To be applied after trac_4320-linear-codes2.patch",
    "created_at": "2008-10-26T14:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31567",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4320-linear-codes3.patch](tarball://root/attachments/some-uuid/ticket4320/trac_4320-linear-codes3.patch) by @wdjoyner created at 2008-10-26 14:30:40

also based on 3.2.alpha0. To be applied after trac_4320-linear-codes2.patch



---

archive/issue_comments_031568.json:
```json
{
    "body": "Replying to [comment:6 wdj]:\n> I wonder if this is somehow because of the fact that if you run the Leon code command wtdist on the command line directly you get \"smash stack\" and (memory errors resulting in?) traceback messages?\n\nI am not really sure we want to support this code as long as it seemingly does not work correctly, i.e. smashing the stack and heaps of memory errors do not really bode well for that code. IIRC the code has been GPLed and sooner or later the code by rlm will cover most of the functionality, so I would highly recommend that we dump wtdist as soon as possible unless someone fixes it.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T14:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31568",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:6 wdj]:
> I wonder if this is somehow because of the fact that if you run the Leon code command wtdist on the command line directly you get "smash stack" and (memory errors resulting in?) traceback messages?

I am not really sure we want to support this code as long as it seemingly does not work correctly, i.e. smashing the stack and heaps of memory errors do not really bode well for that code. IIRC the code has been GPLed and sooner or later the code by rlm will cover most of the functionality, so I would highly recommend that we dump wtdist as soon as possible unless someone fixes it.

Cheers,

Michael



---

archive/issue_comments_031569.json:
```json
{
    "body": "(1) I basically agree. But please note method=\"leon\" is not the default - only one option. Since Leon's code is hard to use directly, the sage interface for it is useful I hope.\n\n(2) I was not aware Robert Miller was working on weight distribution code. The Cython code he wrote for automorphism groups uses totally different ideas, so that would be a completely separate project. I would be very happy to be corrected on that though!\n\n(3) I hope everything is okay for now though.",
    "created_at": "2008-10-26T14:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31569",
    "user": "https://github.com/wdjoyner"
}
```

(1) I basically agree. But please note method="leon" is not the default - only one option. Since Leon's code is hard to use directly, the sage interface for it is useful I hope.

(2) I was not aware Robert Miller was working on weight distribution code. The Cython code he wrote for automorphism groups uses totally different ideas, so that would be a completely separate project. I would be very happy to be corrected on that though!

(3) I hope everything is okay for now though.



---

archive/issue_comments_031570.json:
```json
{
    "body": "Replying to [comment:12 wdj]:\n> (1) I basically agree. But please note method=\"leon\" is not the default - only one option. Since Leon's code is hard to use directly, the sage interface for it is useful I hope.\n\nYes, I know :)\n\n> (2) I was not aware Robert Miller was working on weight distribution code. The Cython code he wrote for automorphism groups uses totally different ideas, so that would be a completely separate project. I would be very happy to be corrected on that though!\n\nOk, I am might be totally wrong here. In the end the hope is that the code can either be ported to Sage or fixed. Either way, I just want to avoid adding dependencies to crappy code where I will end up holding the short stick on the platforms I am porting to.\n\n> (3) I hope everything is okay for now though.\n\nYeah, let's hope someone does review this patch quickly then.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T15:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31570",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:12 wdj]:
> (1) I basically agree. But please note method="leon" is not the default - only one option. Since Leon's code is hard to use directly, the sage interface for it is useful I hope.

Yes, I know :)

> (2) I was not aware Robert Miller was working on weight distribution code. The Cython code he wrote for automorphism groups uses totally different ideas, so that would be a completely separate project. I would be very happy to be corrected on that though!

Ok, I am might be totally wrong here. In the end the hope is that the code can either be ported to Sage or fixed. Either way, I just want to avoid adding dependencies to crappy code where I will end up holding the short stick on the platforms I am porting to.

> (3) I hope everything is okay for now though.

Yeah, let's hope someone does review this patch quickly then.

Cheers,

Michael



---

archive/issue_comments_031571.json:
```json
{
    "body": "See also #4495",
    "created_at": "2008-11-11T21:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31571",
    "user": "https://github.com/rlmill"
}
```

See also #4495



---

archive/issue_comments_031572.json:
```json
{
    "body": "I'd be happy to add a patch to link to #4495 once it is implemented!",
    "created_at": "2008-11-11T23:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31572",
    "user": "https://github.com/wdjoyner"
}
```

I'd be happy to add a patch to link to #4495 once it is implemented!



---

archive/issue_comments_031573.json:
```json
{
    "body": "rlm gave this a positive review off-list providing doctests pass and I am happy with it.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T06:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31573",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

rlm gave this a positive review off-list providing doctests pass and I am happy with it.

Cheers,

Michael



---

archive/issue_comments_031574.json:
```json
{
    "body": "Attachment [trac_4320-linear-codes4.patch](tarball://root/attachments/some-uuid/ticket4320/trac_4320-linear-codes4.patch) by @wdjoyner created at 2008-11-22 13:12:41\n\nbased on 3.1.4 but applies to 3.2 as well. Goes on top of patches 2 and 3",
    "created_at": "2008-11-22T13:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31574",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4320-linear-codes4.patch](tarball://root/attachments/some-uuid/ticket4320/trac_4320-linear-codes4.patch) by @wdjoyner created at 2008-11-22 13:12:41

based on 3.1.4 but applies to 3.2 as well. Goes on top of patches 2 and 3



---

archive/issue_comments_031575.json:
```json
{
    "body": "I got an off-trac review of Dan Gordan last night, who had a couple of complaints (one about the optional method \"gap+verbose\" for a non-binary code and another was that is_permutation_equivalent did not first check that the lengths of the 2 codes were equal). These were easy fixes, so I hope it s okay to add them as well. Applies okay and passes tests on my macbook.\nMichael: hope this is not an inconvenience.",
    "created_at": "2008-11-22T13:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31575",
    "user": "https://github.com/wdjoyner"
}
```

I got an off-trac review of Dan Gordan last night, who had a couple of complaints (one about the optional method "gap+verbose" for a non-binary code and another was that is_permutation_equivalent did not first check that the lengths of the 2 codes were equal). These were easy fixes, so I hope it s okay to add them as well. Applies okay and passes tests on my macbook.
Michael: hope this is not an inconvenience.



---

archive/issue_comments_031576.json:
```json
{
    "body": "Hi David,\n\nOne more thing to fix after all: code2leon creates the file \"output\" into the cwd:\n\n```\nsage: open(\"output\").close()\n```\n\nI will take another look to make sure there is no other case like that and then this can go in. Doctests pass for me.\n\nSorry for the tardy review :(\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T13:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31576",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi David,

One more thing to fix after all: code2leon creates the file "output" into the cwd:

```
sage: open("output").close()
```

I will take another look to make sure there is no other case like that and then this can go in. Doctests pass for me.

Sorry for the tardy review :(

Cheers,

Michael



---

archive/issue_comments_031577.json:
```json
{
    "body": "And I saw two more cases of 'open(\"output\")' in the first file, so please make sure to fix all three cases. Pending those fixes this patch finally gets a positive review from my end. You might also want to consider posting a cumulative patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T13:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31577",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And I saw two more cases of 'open("output")' in the first file, so please make sure to fix all three cases. Pending those fixes this patch finally gets a positive review from my end. You might also want to consider posting a cumulative patch.

Cheers,

Michael



---

archive/issue_comments_031578.json:
```json
{
    "body": "Better late than never:-) However, I don't know what this means:\n\"One more thing to fix after all: code2leon creates the file \"output\" into the cwd: ...\"\ncwd? Once I know this, possibly I can figure out how to fix it...",
    "created_at": "2008-11-25T13:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31578",
    "user": "https://github.com/wdjoyner"
}
```

Better late than never:-) However, I don't know what this means:
"One more thing to fix after all: code2leon creates the file "output" into the cwd: ..."
cwd? Once I know this, possibly I can figure out how to fix it...



---

archive/issue_comments_031579.json:
```json
{
    "body": "Hi David,\n\ncwd == current working directory. The problem is that the user who doctests might not have write permission in the Sage tree. So if you create any files they should always reside in $SAGE_TMP.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T13:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31579",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi David,

cwd == current working directory. The problem is that the user who doctests might not have write permission in the Sage tree. So if you create any files they should always reside in $SAGE_TMP.

Cheers,

Michael



---

archive/issue_comments_031580.json:
```json
{
    "body": "Okay, no problem - that I can fix.\n\nIt is it easy to create a cumulative patch (short of retyping all the changes into a new clone)?",
    "created_at": "2008-11-25T13:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31580",
    "user": "https://github.com/wdjoyner"
}
```

Okay, no problem - that I can fix.

It is it easy to create a cumulative patch (short of retyping all the changes into a new clone)?



---

archive/issue_comments_031581.json:
```json
{
    "body": "If you have a fresh tree just just use GNU patch to apply all three patches, then fix the issue, commit and export. If that is trouble just post a patch on top and I will merge all four patches. To review the changes a new patch would be better, so do it the way you prefer.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T13:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31581",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

If you have a fresh tree just just use GNU patch to apply all three patches, then fix the issue, commit and export. If that is trouble just post a patch on top and I will merge all four patches. To review the changes a new patch would be better, so do it the way you prefer.

Cheers,

Michael



---

archive/issue_comments_031582.json:
```json
{
    "body": "Attachment [trac_4320-linear-codes5.patch](tarball://root/attachments/some-uuid/ticket4320/trac_4320-linear-codes5.patch) by @wdjoyner created at 2008-11-26 01:51:30\n\nto be applied on top of patches 2, 3, and 4",
    "created_at": "2008-11-26T01:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31582",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4320-linear-codes5.patch](tarball://root/attachments/some-uuid/ticket4320/trac_4320-linear-codes5.patch) by @wdjoyner created at 2008-11-26 01:51:30

to be applied on top of patches 2, 3, and 4



---

archive/issue_comments_031583.json:
```json
{
    "body": "I just made a small patch with the changes you suggested. This makes it easier for you to read, me to create and test, and i have more confidence that it is the desired patch.\n\nApplies okay and passes tests on my intel macbook.",
    "created_at": "2008-11-26T01:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31583",
    "user": "https://github.com/wdjoyner"
}
```

I just made a small patch with the changes you suggested. This makes it easier for you to read, me to create and test, and i have more confidence that it is the desired patch.

Applies okay and passes tests on my intel macbook.



---

archive/issue_comments_031584.json:
```json
{
    "body": "The last patch is still not 100% fool proof since doctesting the same file in parallel introduces race conditions, but that does not stop me from giving the cumulative four patches a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T01:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31584",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The last patch is still not 100% fool proof since doctesting the same file in parallel introduces race conditions, but that does not stop me from giving the cumulative four patches a positive review.

Cheers,

Michael



---

archive/issue_comments_031585.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-26T09:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31585",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004565.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-26T09:35:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4320#event-4565"
}
```



---

archive/issue_comments_031586.json:
```json
{
    "body": "Merged trac_4320-linear-codes2.patch through trac_4320-linear-codes5.patch in Sage 3.2.1.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T09:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4320#issuecomment-31586",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_4320-linear-codes2.patch through trac_4320-linear-codes5.patch in Sage 3.2.1.alpha1

Cheers,

Michael
