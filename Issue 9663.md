# Issue 9663: Fast computation of Stirling numbers of 2nd kind

archive/issues_009663.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  was\n\nCurrently, Stirling numbers are computed by calling GAP. The patch provides fast Cython code for Stirling numbers of the second kind, and allows using GAP or Maxima as an optional algorithm.\n\nBy having less overhead, the Cython code is about 10000 times faster than GAP or Maxima for tiny inputs, and it remains much faster than GAP for larger inputs as well. Apparently Maxima uses a fast algorithm unlike GAP, but my code is still about twice as fast as Maxima for huge n due to an algorithmic optimization.\n\n\n```\nsage: %timeit stirling_number2(10,5)\n625 loops, best of 3: 2.33 \u00b5s per loop\nsage: %timeit stirling_number2(10,5,algorithm='gap')\n25 loops, best of 3: 20 ms per loop\nsage: %timeit stirling_number2(10,5,algorithm='maxima')\n5 loops, best of 3: 40 ms per loop\n\n625 loops, best of 3: 16.2 \u00b5s per loop\nsage: %timeit stirling_number2(100,50,algorithm='gap')\n25 loops, best of 3: 20 ms per loop\nsage: %timeit stirling_number2(100,50,algorithm='maxima')\n5 loops, best of 3: 40 ms per loop\n\nsage: %timeit stirling_number2(2000,1500)\n25 loops, best of 3: 35.9 ms per loop\nsage: %timeit stirling_number2(2000,1500,algorithm='gap')\n5 loops, best of 3: 348 ms per loop\nsage: %timeit stirling_number2(2000,1500,algorithm='maxima')\n5 loops, best of 3: 210 ms per loop\n\nsage: %timeit stirling_number2(4000,3000)\n5 loops, best of 3: 249 ms per loop\nsage: %timeit stirling_number2(4000,3000,algorithm='gap')\n5 loops, best of 3: 2.96 s per loop\nsage: %timeit stirling_number2(4000,3000,algorithm='maxima')\n5 loops, best of 3: 948 ms per loop\n\nsage: %time stirling_number2(20000,15000);\nCPU times: user 20.30 s, sys: 0.23 s, total: 20.53 s\nWall time: 21.82 s\nsage: %time stirling_number2(20000,15000,algorithm='maxima');\nCPU times: user 0.00 s, sys: 0.01 s, total: 0.01 s\nWall time: 51.90 s\n```\n\n\nMathematica seems to be about as slow as GAP (warning: timed on a different system):\n\n```\nIn[1]:= Timing[StirlingS2[4000,3000];]\nOut[1]= {27.1809, Null}\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9663\n\n",
    "created_at": "2010-08-01T18:44:18Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Fast computation of Stirling numbers of 2nd kind",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9663",
    "user": "fredrik.johansson"
}
```
Assignee: sage-combinat

CC:  was

Currently, Stirling numbers are computed by calling GAP. The patch provides fast Cython code for Stirling numbers of the second kind, and allows using GAP or Maxima as an optional algorithm.

By having less overhead, the Cython code is about 10000 times faster than GAP or Maxima for tiny inputs, and it remains much faster than GAP for larger inputs as well. Apparently Maxima uses a fast algorithm unlike GAP, but my code is still about twice as fast as Maxima for huge n due to an algorithmic optimization.


```
sage: %timeit stirling_number2(10,5)
625 loops, best of 3: 2.33 µs per loop
sage: %timeit stirling_number2(10,5,algorithm='gap')
25 loops, best of 3: 20 ms per loop
sage: %timeit stirling_number2(10,5,algorithm='maxima')
5 loops, best of 3: 40 ms per loop

625 loops, best of 3: 16.2 µs per loop
sage: %timeit stirling_number2(100,50,algorithm='gap')
25 loops, best of 3: 20 ms per loop
sage: %timeit stirling_number2(100,50,algorithm='maxima')
5 loops, best of 3: 40 ms per loop

sage: %timeit stirling_number2(2000,1500)
25 loops, best of 3: 35.9 ms per loop
sage: %timeit stirling_number2(2000,1500,algorithm='gap')
5 loops, best of 3: 348 ms per loop
sage: %timeit stirling_number2(2000,1500,algorithm='maxima')
5 loops, best of 3: 210 ms per loop

sage: %timeit stirling_number2(4000,3000)
5 loops, best of 3: 249 ms per loop
sage: %timeit stirling_number2(4000,3000,algorithm='gap')
5 loops, best of 3: 2.96 s per loop
sage: %timeit stirling_number2(4000,3000,algorithm='maxima')
5 loops, best of 3: 948 ms per loop

sage: %time stirling_number2(20000,15000);
CPU times: user 20.30 s, sys: 0.23 s, total: 20.53 s
Wall time: 21.82 s
sage: %time stirling_number2(20000,15000,algorithm='maxima');
CPU times: user 0.00 s, sys: 0.01 s, total: 0.01 s
Wall time: 51.90 s
```


Mathematica seems to be about as slow as GAP (warning: timed on a different system):

```
In[1]:= Timing[StirlingS2[4000,3000];]
Out[1]= {27.1809, Null}
```


Issue created by migration from https://trac.sagemath.org/ticket/9663





---

archive/issue_comments_093785.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-01T19:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93785",
    "user": "fredrik.johansson"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093786.json:
```json
{
    "body": "Please explain the *massive* number of changes to module_list.py of the form:\n\n```\n153\t \t                [[blank looking line]]\n \t153\t                [[another blank looking line]]\n```\n",
    "created_at": "2010-08-05T02:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93786",
    "user": "was"
}
```

Please explain the *massive* number of changes to module_list.py of the form:

```
153	 	                [[blank looking line]]
 	153	                [[another blank looking line]]
```




---

archive/issue_comments_093787.json:
```json
{
    "body": "Oops, my editor was set to \"strip trailing whitespace when saving files\".",
    "created_at": "2010-08-05T10:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93787",
    "user": "fredrik.johansson"
}
```

Oops, my editor was set to "strip trailing whitespace when saving files".



---

archive/issue_comments_093788.json:
```json
{
    "body": "fast implementation of stirling_number2 -- updated patch",
    "created_at": "2010-08-05T22:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93788",
    "user": "fredrik.johansson"
}
```

fast implementation of stirling_number2 -- updated patch



---

archive/issue_comments_093789.json:
```json
{
    "body": "Attachment [stirling2.patch](tarball://root/attachments/some-uuid/ticket9663/stirling2.patch) by fredrik.johansson created at 2010-08-05 22:40:40\n\nPlease see the new version of the patch.",
    "created_at": "2010-08-05T22:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93789",
    "user": "fredrik.johansson"
}
```

Attachment [stirling2.patch](tarball://root/attachments/some-uuid/ticket9663/stirling2.patch) by fredrik.johansson created at 2010-08-05 22:40:40

Please see the new version of the patch.



---

archive/issue_comments_093790.json:
```json
{
    "body": "Nice one !!\n\nI learned many things while reviewing this patch `:-)`\n\nWould you mind adding this small doctest in the patch I attach ? If not, you can set this ticket to \"positive_review\" !\n\nThanksssssssssssss !!!\n\nNathann",
    "created_at": "2010-09-05T15:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93790",
    "user": "ncohen"
}
```

Nice one !!

I learned many things while reviewing this patch `:-)`

Would you mind adding this small doctest in the patch I attach ? If not, you can set this ticket to "positive_review" !

Thanksssssssssssss !!!

Nathann



---

archive/issue_comments_093791.json:
```json
{
    "body": "Attachment [trac_9663 - additional test.patch](tarball://root/attachments/some-uuid/ticket9663/trac_9663 - additional test.patch) by ncohen created at 2010-09-05 15:20:23",
    "created_at": "2010-09-05T15:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93791",
    "user": "ncohen"
}
```

Attachment [trac_9663 - additional test.patch](tarball://root/attachments/some-uuid/ticket9663/trac_9663 - additional test.patch) by ncohen created at 2010-09-05 15:20:23



---

archive/issue_comments_093792.json:
```json
{
    "body": "Are you around ? There's basically nothing to do on this patch `:-)`\n\nNathann",
    "created_at": "2010-10-04T06:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93792",
    "user": "ncohen"
}
```

Are you around ? There's basically nothing to do on this patch `:-)`

Nathann



---

archive/issue_comments_093793.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-24T10:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93793",
    "user": "nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093794.json:
```json
{
    "body": "The two patch applied on 4.5.3 All tests pass, no warning in docbuild... Nice documentation, powerful implantation... Good job!\n\nI give the two patch a positive review.\n\nFor the release manager, please apply :\n* stirling2.patch\n* trac_9663 - additional test.patch",
    "created_at": "2010-10-24T10:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93794",
    "user": "nborie"
}
```

The two patch applied on 4.5.3 All tests pass, no warning in docbuild... Nice documentation, powerful implantation... Good job!

I give the two patch a positive review.

For the release manager, please apply :
* stirling2.patch
* trac_9663 - additional test.patch



---

archive/issue_comments_093795.json:
```json
{
    "body": "I think you should add a patch with a test for \"unknown algorithm\".",
    "created_at": "2010-10-26T08:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93795",
    "user": "jdemeyer"
}
```

I think you should add a patch with a test for "unknown algorithm".



---

archive/issue_comments_093796.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-10-26T08:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93796",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093797.json:
```json
{
    "body": "Also, **please** do not put spaces in patch filenames.",
    "created_at": "2010-10-26T08:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93797",
    "user": "jdemeyer"
}
```

Also, **please** do not put spaces in patch filenames.



---

archive/issue_comments_093798.json:
```json
{
    "body": "Replying to [comment:8 jdemeyer]:\n> I think you should add a patch with a test for \"unknown algorithm\".\n\nWhat do you mean ?\n\nNathann",
    "created_at": "2010-10-26T09:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93798",
    "user": "ncohen"
}
```

Replying to [comment:8 jdemeyer]:
> I think you should add a patch with a test for "unknown algorithm".

What do you mean ?

Nathann



---

archive/issue_comments_093799.json:
```json
{
    "body": "Replying to [comment:11 ncohen]:\n> Replying to [comment:8 jdemeyer]:\n> > I think you should add a patch with a test for \"unknown algorithm\".\n> \n> What do you mean ?\n\nA test which does something like\n\n```\nsage: n = stirling_number2(20,11,algorithm='foobar')\n```\n\nto check the \"unknown algorithm\" code.",
    "created_at": "2010-10-26T09:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93799",
    "user": "jdemeyer"
}
```

Replying to [comment:11 ncohen]:
> Replying to [comment:8 jdemeyer]:
> > I think you should add a patch with a test for "unknown algorithm".
> 
> What do you mean ?

A test which does something like

```
sage: n = stirling_number2(20,11,algorithm='foobar')
```

to check the "unknown algorithm" code.



---

archive/issue_comments_093800.json:
```json
{
    "body": "Here is a new version of my patch with the requested doctest.\n\nNathann",
    "created_at": "2010-10-26T10:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93800",
    "user": "ncohen"
}
```

Here is a new version of my patch with the requested doctest.

Nathann



---

archive/issue_comments_093801.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-26T10:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93801",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093802.json:
```json
{
    "body": "Replying to [comment:13 ncohen]:\n> Here is a new version of my patch with the requested doctest.\n> \n> Nathann\n\nOn line 670, `TESTS::` should be `TESTS:` (the :: should precede a block of code, which is not the case here).",
    "created_at": "2010-10-26T11:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93802",
    "user": "jdemeyer"
}
```

Replying to [comment:13 ncohen]:
> Here is a new version of my patch with the requested doctest.
> 
> Nathann

On line 670, `TESTS::` should be `TESTS:` (the :: should precede a block of code, which is not the case here).



---

archive/issue_comments_093803.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-26T11:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93803",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093804.json:
```json
{
    "body": "Done.\n\nNathann",
    "created_at": "2010-10-26T11:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93804",
    "user": "ncohen"
}
```

Done.

Nathann



---

archive/issue_comments_093805.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-26T11:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93805",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093806.json:
```json
{
    "body": "Attachment [trac_9663-additional_tests.patch](tarball://root/attachments/some-uuid/ticket9663/trac_9663-additional_tests.patch) by ncohen created at 2010-10-26 11:58:37",
    "created_at": "2010-10-26T11:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93806",
    "user": "ncohen"
}
```

Attachment [trac_9663-additional_tests.patch](tarball://root/attachments/some-uuid/ticket9663/trac_9663-additional_tests.patch) by ncohen created at 2010-10-26 11:58:37



---

archive/issue_comments_093807.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-27T12:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93807",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093808.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9663#issuecomment-93808",
    "user": "jdemeyer"
}
```

Resolution: fixed
