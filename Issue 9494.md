# Issue 9494: Add a doctest to benchmark.py

archive/issues_009494.json:
```json
{
    "body": "Assignee: mvngu\n\nDemo at SD23.5, also increases coverage!\n\nIssue created by migration from https://trac.sagemath.org/ticket/9494\n\n",
    "created_at": "2010-07-14T09:28:21Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "Add a doctest to benchmark.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9494",
    "user": "demosd235"
}
```
Assignee: mvngu

Demo at SD23.5, also increases coverage!

Issue created by migration from https://trac.sagemath.org/ticket/9494





---

archive/issue_comments_091150.json:
```json
{
    "body": "Add a comment to a ticket here.",
    "created_at": "2010-07-14T09:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91150",
    "user": "demosd235"
}
```

Add a comment to a ticket here.



---

archive/issue_comments_091151.json:
```json
{
    "body": "Is this ready yet?",
    "created_at": "2010-07-14T09:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91151",
    "user": "demosd235"
}
```

Is this ready yet?



---

archive/issue_comments_091152.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-14T09:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91152",
    "user": "demosd235"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091153.json:
```json
{
    "body": "According to http://www.sagemath.org/doc/developer/conventions.html#docstring-markup-with-rest-and-sphinx it should be `EXAMPLES:` instead of `EXAMPLE::`.\n\nIt's enough to put only 3 dots between `<BLANKLINE>` and `System` but this is okay as well.",
    "created_at": "2010-12-01T12:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91153",
    "user": "aapitzsch"
}
```

According to http://www.sagemath.org/doc/developer/conventions.html#docstring-markup-with-rest-and-sphinx it should be `EXAMPLES:` instead of `EXAMPLE::`.

It's enough to put only 3 dots between `<BLANKLINE>` and `System` but this is okay as well.



---

archive/issue_comments_091154.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-05-26T15:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91154",
    "user": "mariah"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_091155.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-08-22T07:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91155",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_091156.json:
```json
{
    "body": "If an \"EXAMPLES\" block just has one example, then it is OK to drop the S.  And if there is no prose before the test, then a double-colon can be used to indicate verbatim text next.\n\nThere are excess ... but they cause no harm.  This ticket looks good to me.  Am I missing something?  It looks ready for a positive review to me.\n\nI am working on this as a high-priority ticket for Bug Days 32.\n\nRob",
    "created_at": "2011-08-22T07:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91156",
    "user": "rbeezer"
}
```

If an "EXAMPLES" block just has one example, then it is OK to drop the S.  And if there is no prose before the test, then a double-colon can be used to indicate verbatim text next.

There are excess ... but they cause no harm.  This ticket looks good to me.  Am I missing something?  It looks ready for a positive review to me.

I am working on this as a high-priority ticket for Bug Days 32.

Rob



---

archive/issue_comments_091157.json:
```json
{
    "body": "The patch looks good to me and passes doctests:\n\n\n```\n\nbjones@sage:~/sage/sage-4.7.1/devel/sage$ ../../sage -t sage/tests/benchmark.py \nsage -t  \"devel/sage-9494/sage/tests/benchmark.py\"          \n\t [8.6 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 8.6 seconds\n```\n\n\nI'm giving it a positive review.",
    "created_at": "2011-08-23T00:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91157",
    "user": "benjaminfjones"
}
```

The patch looks good to me and passes doctests:


```

bjones@sage:~/sage/sage-4.7.1/devel/sage$ ../../sage -t sage/tests/benchmark.py 
sage -t  "devel/sage-9494/sage/tests/benchmark.py"          
	 [8.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 8.6 seconds
```


I'm giving it a positive review.



---

archive/issue_comments_091158.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-08-23T00:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91158",
    "user": "benjaminfjones"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_091159.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-23T00:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91159",
    "user": "benjaminfjones"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091160.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91160",
    "user": "was"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_091161.json:
```json
{
    "body": "Actually, `mpoly_all()` needs work, since it is apparently unable to interrupt (e.g.) Mathematica a second time.\n\nOn redhawk, where `/home` still isn't mounted, Mathematica is installed but fails to startup (prompting the user), such that I get:\n\n```sh\nleif@redhawk:/$ time sage -c \"from sage.tests.benchmark import mpoly_all; mpoly_all()\" \n\n\n\nCompute (x_0 + ... + x_99) * (x_100 + ... + x_200) over Rational Field (use singular for Sage mult.)\n  System      min         avg         max         trials          cpu or wall\n* sage        0.049767    0.049767    0.049767    1                  0.049767w\nUnable to start magma\ncomputation timed out because alarm was set for 60 seconds\nUnable to start macaulay2 because the command 'M2 --no-debug --no-readline --silent -e 'ZZ#{Standard,Core#\"private dictionary\"#\"InputPrompt\"} = lineno -> \"_EGAS_ : \";ZZ#{Standard,Core#\"private dictionary\"#\"InputContinuationPrompt\"} = lineno -> \"_EGAS_ : \";printWidth = 0;lineNumber = 10^9;'' failed.\n\n\n\n\nCompute (x_0 + ... + x_199) * (x_200 + ... + x_400) over Rational Field (use singular for Sage mult.)\n  System      min         avg         max         trials          cpu or wall\n* sage        0.089736    0.089736    0.089736    1                  0.089736w\nUnable to start magma\nInterrupting Mathematica...\n```\n\nwhich does not terminate.\n\nWhat is this doctest supposed to \"test\" at all?\n\nThe output is random, so it doesn't really test anything, except perhaps which external programs are installed, but that's nothing subject to a doctest, so IMHO this ticket should either be closed as invalid, or the \"doctest\" (i.e., the example) should be marked `# not tested`, at least until `mpoly_all()` got fixed.",
    "created_at": "2011-09-16T06:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91161",
    "user": "leif"
}
```

Actually, `mpoly_all()` needs work, since it is apparently unable to interrupt (e.g.) Mathematica a second time.

On redhawk, where `/home` still isn't mounted, Mathematica is installed but fails to startup (prompting the user), such that I get:

```sh
leif@redhawk:/$ time sage -c "from sage.tests.benchmark import mpoly_all; mpoly_all()" 



Compute (x_0 + ... + x_99) * (x_100 + ... + x_200) over Rational Field (use singular for Sage mult.)
  System      min         avg         max         trials          cpu or wall
* sage        0.049767    0.049767    0.049767    1                  0.049767w
Unable to start magma
computation timed out because alarm was set for 60 seconds
Unable to start macaulay2 because the command 'M2 --no-debug --no-readline --silent -e 'ZZ#{Standard,Core#"private dictionary"#"InputPrompt"} = lineno -> "_EGAS_ : ";ZZ#{Standard,Core#"private dictionary"#"InputContinuationPrompt"} = lineno -> "_EGAS_ : ";printWidth = 0;lineNumber = 10^9;'' failed.




Compute (x_0 + ... + x_199) * (x_200 + ... + x_400) over Rational Field (use singular for Sage mult.)
  System      min         avg         max         trials          cpu or wall
* sage        0.089736    0.089736    0.089736    1                  0.089736w
Unable to start magma
Interrupting Mathematica...
```

which does not terminate.

What is this doctest supposed to "test" at all?

The output is random, so it doesn't really test anything, except perhaps which external programs are installed, but that's nothing subject to a doctest, so IMHO this ticket should either be closed as invalid, or the "doctest" (i.e., the example) should be marked `# not tested`, at least until `mpoly_all()` got fixed.



---

archive/issue_comments_091162.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-09-16T06:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91162",
    "user": "leif"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_091163.json:
```json
{
    "body": "Attachment\n\nmarked mpoly_all() as not tested",
    "created_at": "2012-04-07T23:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91163",
    "user": "benjaminfjones"
}
```

Attachment

marked mpoly_all() as not tested



---

archive/issue_comments_091164.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-04-07T23:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91164",
    "user": "benjaminfjones"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091165.json:
```json
{
    "body": "I marked `mpoly_all()` as `# not tested`. The new patch applied cleanly to 5.0.beta12 and passes tests on `sage.math.washington.edu` where Mma is installed. I'm running tests on redhawk now to double check.",
    "created_at": "2012-04-07T23:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91165",
    "user": "benjaminfjones"
}
```

I marked `mpoly_all()` as `# not tested`. The new patch applied cleanly to 5.0.beta12 and passes tests on `sage.math.washington.edu` where Mma is installed. I'm running tests on redhawk now to double check.



---

archive/issue_comments_091166.json:
```json
{
    "body": "There seems to still be an issue with the Mma installation on redhawk and the `mpoly_all()` test is still unable to interrupt the crashed process all the time:\n\n\n```\nCompute (x_1 + 2*x_2 + 3*x_3 + ... + 128*x_128) * (129 * x_129 + ... + 257*x_257) over Rational Field (use singular for Sage mult.)\n  System      min         avg         max         trials          cpu or wall\n* sage        0.049826    0.049826    0.049826    1                  0.049826w\nUnable to start magma\nMathematica crashed -- automatically restarting.\ncomputation timed out because alarm was set for 60 seconds\nUnable to start macaulay2 because the command 'M2 --no-debug --no-readline --silent -e 'ZZ#{Standard,Core#\"private dictionary\"#\"InputPrompt\"} = lineno -> \"_EGAS_ : \";ZZ#{Standard,Core#\"private dictionary\"#\"InputContinuationPrompt\"} = lineno -> \"_EGAS_ : \";printWidth = 0;lineNumber = 10^9;'' failed.\n\n\n\n\nCompute (x_1 + 2*x_2 + 3*x_3 + ... + 256*x_256) * (257 * x_257 + ... + 513*x_513) over Rational Field (use singular for Sage mult.)\n  System      min         avg         max         trials          cpu or wall\n* sage        0.149662    0.149662    0.149662    1                  0.149662w\nUnable to start magma\nInterrupting Mathematica...\n^C\nUnable to start macaulay2 because the command 'M2 --no-debug --no-readline --silent -e 'ZZ#{Standard,Core#\"private dictionary\"#\"InputPrompt\"} = lineno -> \"_EGAS_ : \";ZZ#{Standard,Core#\"private dictionary\"#\"InputContinuationPrompt\"} = lineno -> \"_EGAS_ : \";printWidth = 0;lineNumber = 10^9;'' failed.\n```\n\n\nBut I'd say that's an issue for another ticket.",
    "created_at": "2012-04-08T04:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91166",
    "user": "benjaminfjones"
}
```

There seems to still be an issue with the Mma installation on redhawk and the `mpoly_all()` test is still unable to interrupt the crashed process all the time:


```
Compute (x_1 + 2*x_2 + 3*x_3 + ... + 128*x_128) * (129 * x_129 + ... + 257*x_257) over Rational Field (use singular for Sage mult.)
  System      min         avg         max         trials          cpu or wall
* sage        0.049826    0.049826    0.049826    1                  0.049826w
Unable to start magma
Mathematica crashed -- automatically restarting.
computation timed out because alarm was set for 60 seconds
Unable to start macaulay2 because the command 'M2 --no-debug --no-readline --silent -e 'ZZ#{Standard,Core#"private dictionary"#"InputPrompt"} = lineno -> "_EGAS_ : ";ZZ#{Standard,Core#"private dictionary"#"InputContinuationPrompt"} = lineno -> "_EGAS_ : ";printWidth = 0;lineNumber = 10^9;'' failed.




Compute (x_1 + 2*x_2 + 3*x_3 + ... + 256*x_256) * (257 * x_257 + ... + 513*x_513) over Rational Field (use singular for Sage mult.)
  System      min         avg         max         trials          cpu or wall
* sage        0.149662    0.149662    0.149662    1                  0.149662w
Unable to start magma
Interrupting Mathematica...
^C
Unable to start macaulay2 because the command 'M2 --no-debug --no-readline --silent -e 'ZZ#{Standard,Core#"private dictionary"#"InputPrompt"} = lineno -> "_EGAS_ : ";ZZ#{Standard,Core#"private dictionary"#"InputContinuationPrompt"} = lineno -> "_EGAS_ : ";printWidth = 0;lineNumber = 10^9;'' failed.
```


But I'd say that's an issue for another ticket.



---

archive/issue_comments_091167.json:
```json
{
    "body": "Moved patch to git.\n----\nNew commits:",
    "created_at": "2014-02-14T16:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91167",
    "user": "rws"
}
```

Moved patch to git.
----
New commits:



---

archive/issue_comments_091168.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-14T16:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91168",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091169.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2014-02-20T17:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91169",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_091170.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2014-02-20T17:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91170",
    "user": "git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_091171.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-20T17:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91171",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091172.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-23T07:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9494#issuecomment-91172",
    "user": "vbraun"
}
```

Resolution: fixed
