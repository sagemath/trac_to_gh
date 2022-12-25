# Issue 9310: sage-4.4.4.alpha1 blocker -- random doctest failure on menas (skynet)

archive/issues_009310.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @vbraun\n\n\n```\n\nwstein@menas:~/screen/menas/sage-4.4.4.alpha1> ./sage -t  -long \"devel/sage/sage/groups/matrix_gps/matrix_group.py\"\nsage -t -long \"devel/sage/sage/groups/matrix_gps/matrix_group.py\"\n**********************************************************************\nFile \"/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py\", line 647:\n    sage: G.random_element()\nExpected:\n    [2 1 1 1]\n    [1 0 2 1]\n    [0 1 1 0]\n    [1 0 0 1]\nGot:\n    [0 1 1 0]\n    [1 2 2 2]\n    [1 1 1 0]\n    [2 0 1 2]\n**********************************************************************\nFile \"/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py\", line 658:\n    sage: G.random_element()\nExpected:\n    [1 3]\n    [0 3]\nGot:\n    [4 2]\n    [1 0]\n**********************************************************************\nFile \"/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py\", line 661:\n    sage: G.random_element()\nExpected:\n    [2 2]\n    [1 0]\nGot:\n    [4 1]\n    [0 2]\n**********************************************************************\nFile \"/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py\", line 664:\n    sage: G.random_element()\nExpected:\n    [4 0]\n    [1 4]\n\nGot:\n    [2 4]\n    [2 3]\n**********************************************************************\n1 items had failures:\n   4 of  10 in __main__.example_22\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_matrix_group.py\n         [88.9 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9310\n\n",
    "created_at": "2010-06-22T15:00:46Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "sage-4.4.4.alpha1 blocker -- random doctest failure on menas (skynet)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9310",
    "user": "https://github.com/williamstein"
}
```
Assignee: mvngu

CC:  @vbraun


```

wstein@menas:~/screen/menas/sage-4.4.4.alpha1> ./sage -t  -long "devel/sage/sage/groups/matrix_gps/matrix_group.py"
sage -t -long "devel/sage/sage/groups/matrix_gps/matrix_group.py"
**********************************************************************
File "/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 647:
    sage: G.random_element()
Expected:
    [2 1 1 1]
    [1 0 2 1]
    [0 1 1 0]
    [1 0 0 1]
Got:
    [0 1 1 0]
    [1 2 2 2]
    [1 1 1 0]
    [2 0 1 2]
**********************************************************************
File "/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 658:
    sage: G.random_element()
Expected:
    [1 3]
    [0 3]
Got:
    [4 2]
    [1 0]
**********************************************************************
File "/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 661:
    sage: G.random_element()
Expected:
    [2 2]
    [1 0]
Got:
    [4 1]
    [0 2]
**********************************************************************
File "/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 664:
    sage: G.random_element()
Expected:
    [4 0]
    [1 4]

Got:
    [2 4]
    [2 3]
**********************************************************************
1 items had failures:
   4 of  10 in __main__.example_22
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_matrix_group.py
         [88.9 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/9310





---

archive/issue_comments_087536.json:
```json
{
    "body": "\n```\n\nwstein@menas:~/screen/menas/sage-4.4.4.alpha1> uname -a\nLinux menas 2.6.27.39-0.2-default #1 SMP 2009-11-23 12:57:38 +0100 x86_64 x86_64 x86_64 GNU/Linux\nwstein@menas:~/screen/menas/sage-4.4.4.alpha1> cat /etc/issue\nWelcome to openSUSE 11.1 - Kernel \\r (\\l).\n```\n",
    "created_at": "2010-06-22T15:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87536",
    "user": "https://github.com/williamstein"
}
```


```

wstein@menas:~/screen/menas/sage-4.4.4.alpha1> uname -a
Linux menas 2.6.27.39-0.2-default #1 SMP 2009-11-23 12:57:38 +0100 x86_64 x86_64 x86_64 GNU/Linux
wstein@menas:~/screen/menas/sage-4.4.4.alpha1> cat /etc/issue
Welcome to openSUSE 11.1 - Kernel \r (\l).
```




---

archive/issue_comments_087537.json:
```json
{
    "body": "Note -- In sage-4.4.1 on the same computer, the file doctests fine.  The only diff between the files is:\n\n```\nwstein@menas:~/screen/menas/sage-4.4.1> diff devel/sage/sage/groups/matrix_gps/matrix_group.py ../sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py|more\n330a331,351\n>     def is_abelian(self):\n>         r\"\"\"\n>         Return True if this group is an abelian group.\n>         \n>         Note: The result is cached, since it tends to get called\n>         rather often (e.g. by word_problem) and it's very slow to\n>         use the Gap interface every time. \n> \n>         EXAMPLES::\n>         \n>             sage: SL(1, 17).is_abelian()\n>             True\n>             sage: SL(2, 17).is_abelian()\n>             False\n>         \"\"\"\n>         try:\n>             return self.__is_abelian\n>         except AttributeError:\n>             self.__is_abelian = self._gap_().IsAbelian().bool()\n>             return self.__is_abelian\n> \n624c645,646\n<   \n```\n\n\nThus a change somewhere *else* in Sage is causing this problem.",
    "created_at": "2010-06-22T15:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87537",
    "user": "https://github.com/williamstein"
}
```

Note -- In sage-4.4.1 on the same computer, the file doctests fine.  The only diff between the files is:

```
wstein@menas:~/screen/menas/sage-4.4.1> diff devel/sage/sage/groups/matrix_gps/matrix_group.py ../sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py|more
330a331,351
>     def is_abelian(self):
>         r"""
>         Return True if this group is an abelian group.
>         
>         Note: The result is cached, since it tends to get called
>         rather often (e.g. by word_problem) and it's very slow to
>         use the Gap interface every time. 
> 
>         EXAMPLES::
>         
>             sage: SL(1, 17).is_abelian()
>             True
>             sage: SL(2, 17).is_abelian()
>             False
>         """
>         try:
>             return self.__is_abelian
>         except AttributeError:
>             self.__is_abelian = self._gap_().IsAbelian().bool()
>             return self.__is_abelian
> 
624c645,646
<   
```


Thus a change somewhere *else* in Sage is causing this problem.



---

archive/issue_comments_087538.json:
```json
{
    "body": "I had noticed this on sage.math when merging http://trac.sagemath.org/sage_trac/ticket/8984",
    "created_at": "2010-06-22T17:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87538",
    "user": "https://github.com/mwhansen"
}
```

I had noticed this on sage.math when merging http://trac.sagemath.org/sage_trac/ticket/8984



---

archive/issue_comments_087539.json:
```json
{
    "body": "FWIW, I run this 6 times on my Solaris 10 box (SPARC) with no problems using sage-4.4.4.alpha1.tar \n\nDave",
    "created_at": "2010-06-22T23:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87539",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

FWIW, I run this 6 times on my Solaris 10 box (SPARC) with no problems using sage-4.4.4.alpha1.tar 

Dave



---

archive/issue_comments_087540.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> I had noticed this on sage.math when merging http://trac.sagemath.org/sage_trac/ticket/8984\n\nAh, interesting. So hopefully #8984 is not the cause, and could be merged in!",
    "created_at": "2010-06-23T05:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87540",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:3 mhansen]:
> I had noticed this on sage.math when merging http://trac.sagemath.org/sage_trac/ticket/8984

Ah, interesting. So hopefully #8984 is not the cause, and could be merged in!



---

archive/issue_comments_087541.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2010-06-27T01:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87541",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_087542.json:
```json
{
    "body": "There seems to be a **lot** of doctests which are failing in a non-reproducible way. \n\n* elliptic_curves/BSD.py #9273 (Whilst #9316 is supposed to fix the spurious \"# File not found\" error at end of doctests, BSD.py has still failed for me in non-reproducible way. See #9449 which shows the output of `make ptestlong` First BSD.py fails without printing the  \"# File not found\" message, then it passes. \n* devel/sage/sage/misc/trace.py - see #9446\n* devel/sage/doc/fr/tutorial/programming.rst - see #9449, where this failed first time, but subsequently passed on the same computer, with the same build of Sage. (Though a couple of patches were applied the second time). \n* devel/sage/sage/schemes/plane_curves/constructor.py - again see #9449 which failed once, then passed on a second run. \n* devel/sage/sage/parallel/decorate.py\nThis failed both times, but on the first time it failed, the test was reported to have a 0 failures! \n\n```\n    sage -t     -long devel/sage/sage/parallel/decorate.py # 0 doctests failed\n```\n\nAfter adding patches #8641, #9243, #9316 which are related to the doctesting framework, this was at least reported as one doctest failing in `devel/sage/sage/parallel/decorate.py` \n\n```\n       sage -t  -long devel/sage/sage/parallel/decorate.py # 1 doctests failed\n```\n\nI'm not however convinced that the addition of  #8641, #9243 and #9316 were the result of the improved behavior, as other tests still failed with 0 reported failures. \n\n**IT SEEMS TO ME, THE DOCTESTING FRAMEWORK IS BROKEN IN SAGE NOW**",
    "created_at": "2010-07-08T11:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87542",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

There seems to be a **lot** of doctests which are failing in a non-reproducible way. 

* elliptic_curves/BSD.py #9273 (Whilst #9316 is supposed to fix the spurious "# File not found" error at end of doctests, BSD.py has still failed for me in non-reproducible way. See #9449 which shows the output of `make ptestlong` First BSD.py fails without printing the  "# File not found" message, then it passes. 
* devel/sage/sage/misc/trace.py - see #9446
* devel/sage/doc/fr/tutorial/programming.rst - see #9449, where this failed first time, but subsequently passed on the same computer, with the same build of Sage. (Though a couple of patches were applied the second time). 
* devel/sage/sage/schemes/plane_curves/constructor.py - again see #9449 which failed once, then passed on a second run. 
* devel/sage/sage/parallel/decorate.py
This failed both times, but on the first time it failed, the test was reported to have a 0 failures! 

```
    sage -t     -long devel/sage/sage/parallel/decorate.py # 0 doctests failed
```

After adding patches #8641, #9243, #9316 which are related to the doctesting framework, this was at least reported as one doctest failing in `devel/sage/sage/parallel/decorate.py` 

```
       sage -t  -long devel/sage/sage/parallel/decorate.py # 1 doctests failed
```

I'm not however convinced that the addition of  #8641, #9243 and #9316 were the result of the improved behavior, as other tests still failed with 0 reported failures. 

**IT SEEMS TO ME, THE DOCTESTING FRAMEWORK IS BROKEN IN SAGE NOW**



---

archive/issue_comments_087543.json:
```json
{
    "body": "As noted in #10739, I have two independent builds of sage-4.6.2.alpha3 on my machine, one in which this test passes and the other in which it fails.\n\nReplying to [vbraun](http://trac.sagemath.org/sage_trac/ticket/10739#comment:10) (from #10739)\n> But if one build repeatedly passes \"make ptest\" and the other consistently fails, this would be an excellent opportunity to debug #9310. Presumably the only difference is that the first compilation was interrupted at one point, so the order in which spkgs were built is different.\n\nPrecisely, the first build was interrupted (see #10739 for details) and the second was not.\n\n> This might have changed linked libraries in some components due to (undiscovered) soft dependencies, for example. Can you diff the two trees (excluding log files etc) and find out the difference? \n\nI ran `diff -rq` on the two directories and there are about 25000 files that differ (pyc files, pyo files, ...). I figured that this might have something to do with hardcoded paths, so I moved one out of the way, moved the other into its place, launched sage to reset the hardcoded paths, and then ran `diff -rq` on the two trees. It still shows about 25000 differing files.\n\nAny suggestions on what to try next?",
    "created_at": "2011-02-05T04:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87543",
    "user": "https://github.com/saliola"
}
```

As noted in #10739, I have two independent builds of sage-4.6.2.alpha3 on my machine, one in which this test passes and the other in which it fails.

Replying to [vbraun](http://trac.sagemath.org/sage_trac/ticket/10739#comment:10) (from #10739)
> But if one build repeatedly passes "make ptest" and the other consistently fails, this would be an excellent opportunity to debug #9310. Presumably the only difference is that the first compilation was interrupted at one point, so the order in which spkgs were built is different.

Precisely, the first build was interrupted (see #10739 for details) and the second was not.

> This might have changed linked libraries in some components due to (undiscovered) soft dependencies, for example. Can you diff the two trees (excluding log files etc) and find out the difference? 

I ran `diff -rq` on the two directories and there are about 25000 files that differ (pyc files, pyo files, ...). I figured that this might have something to do with hardcoded paths, so I moved one out of the way, moved the other into its place, launched sage to reset the hardcoded paths, and then ran `diff -rq` on the two trees. It still shows about 25000 differing files.

Any suggestions on what to try next?



---

archive/issue_comments_087544.json:
```json
{
    "body": "I just noticed that after I tar up the offending build directory, untar it elsewhere, launch sage to reset the hardcoded paths, and doctest the `matrix_group.py` file, then all tests pass. So relocating the tree has some sort of an effect here.",
    "created_at": "2011-02-05T04:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87544",
    "user": "https://github.com/saliola"
}
```

I just noticed that after I tar up the offending build directory, untar it elsewhere, launch sage to reset the hardcoded paths, and doctest the `matrix_group.py` file, then all tests pass. So relocating the tree has some sort of an effect here.



---

archive/issue_comments_087545.json:
```json
{
    "body": "I was able to reproduce the failure on Sage-4.6.2.rc0 with Fedora 14 x86_64 by running \n\n```\nsage -t -randorder sage/groups/matrix_gps/matrix_group.py\n```\n\nrepeatedly. The doctest usually passes but once in a while fails as in the ticket description.",
    "created_at": "2011-02-20T12:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87545",
    "user": "https://github.com/vbraun"
}
```

I was able to reproduce the failure on Sage-4.6.2.rc0 with Fedora 14 x86_64 by running 

```
sage -t -randorder sage/groups/matrix_gps/matrix_group.py
```

repeatedly. The doctest usually passes but once in a while fails as in the ticket description.



---

archive/issue_comments_087546.json:
```json
{
    "body": "I did run the test 1000x with -randorder, and found a couple of doctests that depend on the execution order. Since we always initialize GAP's random number generator it is very likely that the output of these operations depends on the order of memory locations. Presumably this causes the doctest failure on some architectures even without -randorder.\n\nThe problems are in \n* `module_composition_factors`\n* `as_permutation_group`\n* `random_element`\n\nThe first two use `MeatAxe`. I think that `random_element` enumerates all group elements and then picks a random one. We do control the random numbers, but enumerating uses the coset enumerator and presumably depends on memory locations.",
    "created_at": "2011-02-21T11:51:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87546",
    "user": "https://github.com/vbraun"
}
```

I did run the test 1000x with -randorder, and found a couple of doctests that depend on the execution order. Since we always initialize GAP's random number generator it is very likely that the output of these operations depends on the order of memory locations. Presumably this causes the doctest failure on some architectures even without -randorder.

The problems are in 
* `module_composition_factors`
* `as_permutation_group`
* `random_element`

The first two use `MeatAxe`. I think that `random_element` enumerates all group elements and then picks a random one. We do control the random numbers, but enumerating uses the coset enumerator and presumably depends on memory locations.



---

archive/issue_comments_087547.json:
```json
{
    "body": "Attachment [trac_9310_matrix_group_random_doctest_failure.patch](tarball://root/attachments/some-uuid/ticket9310/trac_9310_matrix_group_random_doctest_failure.patch) by @vbraun created at 2011-02-21 19:05:34\n\nInitial patch",
    "created_at": "2011-02-21T19:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87547",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9310_matrix_group_random_doctest_failure.patch](tarball://root/attachments/some-uuid/ticket9310/trac_9310_matrix_group_random_doctest_failure.patch) by @vbraun created at 2011-02-21 19:05:34

Initial patch



---

archive/issue_comments_087548.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-02-21T19:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87548",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087549.json:
```json
{
    "body": "This patch \n* sorts the output of `module_composition_factors`, and\n* changes the doctests for `as_permutation_group`, `random_element` to be insensitive to the random choices.",
    "created_at": "2011-02-21T19:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87549",
    "user": "https://github.com/vbraun"
}
```

This patch 
* sorts the output of `module_composition_factors`, and
* changes the doctests for `as_permutation_group`, `random_element` to be insensitive to the random choices.



---

archive/issue_comments_087550.json:
```json
{
    "body": "Applied patch to sage-4.7.1.alpha2, did 'make testlong'.  All tests passed.  Positive review!",
    "created_at": "2011-06-15T14:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87550",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Applied patch to sage-4.7.1.alpha2, did 'make testlong'.  All tests passed.  Positive review!



---

archive/issue_comments_087551.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-15T14:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87551",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087552.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-06-18T08:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87552",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009468.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-06-18T08:35:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9310#event-9468"
}
```



---

archive/issue_comments_087553.json:
```json
{
    "body": "We should perhaps now change the ticket's title.",
    "created_at": "2011-06-25T21:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87553",
    "user": "https://github.com/nexttime"
}
```

We should perhaps now change the ticket's title.



---

archive/issue_comments_087554.json:
```json
{
    "body": "Changing keywords from \"\" to \"matrix_group random_element doctest failure\".",
    "created_at": "2011-06-25T21:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9310#issuecomment-87554",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "" to "matrix_group random_element doctest failure".
