# Issue 7652: Adds Linear Programming to the Constructions document

archive/issues_007652.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  mvngu\n\nFollowing Minh's idea from #6765, here is the first version of this document.\n\nThis patch documents the small improvement from #7637 (which is hence needed by the docstrings)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7652\n\n",
    "created_at": "2009-12-10T14:54:54Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "Adds Linear Programming to the Constructions document",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7652",
    "user": "ncohen"
}
```
Assignee: mvngu

CC:  mvngu

Following Minh's idea from #6765, here is the first version of this document.

This patch documents the small improvement from #7637 (which is hence needed by the docstrings)

Issue created by migration from https://trac.sagemath.org/ticket/7652





---

archive/issue_comments_065447.json:
```json
{
    "body": "I have not applied this but only read the patch file.\n\nComments on the English grammar:\n\n\n```\n10\tA linear program is the sum of two information : \n```\n\nshould read\n\n```\n10\tA linear program consists of the following two pieces of information : \n```\n\nI'm not an expert on complexity theory, but I think\n\n```\n29\tis usually `NP`-Complete (= it can take exponential time, according to a  \n30\twidely-spread belief that `P\\neq NP`) \n```\n\nis not precisely correct as stated it it? Perhaps better would be\n\n\n```\n29\tis usually `NP`-Complete (if `P\\neq NP` then there is not polynomial time 30      algorithm solving a general MILP problem) \n```\n\n\nSorry, I don't understand this beginning of a sentence:\n\n```\n82\tCan be written (quite naturally, I hope !) this way :: \n```\n",
    "created_at": "2009-12-10T20:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7652#issuecomment-65447",
    "user": "wdj"
}
```

I have not applied this but only read the patch file.

Comments on the English grammar:


```
10	A linear program is the sum of two information : 
```

should read

```
10	A linear program consists of the following two pieces of information : 
```

I'm not an expert on complexity theory, but I think

```
29	is usually `NP`-Complete (= it can take exponential time, according to a  
30	widely-spread belief that `P\neq NP`) 
```

is not precisely correct as stated it it? Perhaps better would be


```
29	is usually `NP`-Complete (if `P\neq NP` then there is not polynomial time 30      algorithm solving a general MILP problem) 
```


Sorry, I don't understand this beginning of a sentence:

```
82	Can be written (quite naturally, I hope !) this way :: 
```




---

archive/issue_comments_065448.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-11T13:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7652#issuecomment-65448",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065449.json:
```json
{
    "body": "Attachment\n\nI have attached a reviewer patch `trac_7652-reviewer.patch` that includes the following changes:\n\n* some typo fixes\n* proper ReST formatting\n\nOnce my patch is given some thumbs up, then patches should be applied in this order:\n\n1. `trac_7652.patch`\n2. `trac_7652-reviewer.patch`",
    "created_at": "2009-12-11T13:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7652#issuecomment-65449",
    "user": "mvngu"
}
```

Attachment

I have attached a reviewer patch `trac_7652-reviewer.patch` that includes the following changes:

* some typo fixes
* proper ReST formatting

Once my patch is given some thumbs up, then patches should be applied in this order:

1. `trac_7652.patch`
2. `trac_7652-reviewer.patch`



---

archive/issue_comments_065450.json:
```json
{
    "body": "reviewer patch",
    "created_at": "2009-12-12T01:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7652#issuecomment-65450",
    "user": "mvngu"
}
```

reviewer patch



---

archive/issue_comments_065451.json:
```json
{
    "body": "Attachment\n\nNew reviewer patch attached, which needs some reviewing. Note that the patch `trac_7652.patch` results in the following doctest failures:\n\n```\n[mvngu@sage sage-4.3.alpha1-7652-linear]$ ./sage -t -long devel/sage-main/doc/en/constructions/linear_programming.rst \nsage -t -long \"devel/sage-main/doc/en/constructions/linear_programming.rst\"\n**********************************************************************\nFile \"/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/devel/sage-main/doc/en/constructions/linear_programming.rst\", line 112:\n    sage: p.set_objective( p[\"first unique variable\"] + B[2] + p[-3] )\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[4]>\", line 1, in <module>\n        p.set_objective( p[\"first unique variable\"] + B[Integer(2)] + p[-Integer(3)] )###line 112:\n    sage: p.set_objective( p[\"first unique variable\"] + B[2] + p[-3] )\n    AttributeError: MixedIntegerLinearProgram instance has no attribute '__getitem__'\n**********************************************************************\nFile \"/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/devel/sage-main/doc/en/constructions/linear_programming.rst\", line 134:\n    sage: print x_sol\nExpected:\n    {1: 0.83333333333333337, 2: 0.0}\nGot:\n    {1: None, 2: None}\n**********************************************************************\n2 items had failures:\n   1 of   5 in __main__.example_2\n   1 of   9 in __main__.example_3\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_linear_programming.py\n\t [2.1 s]\nexit code: 1024\n```\n\nMy reviewer patch resolves the second failure, but I'm unable to resolve the first one. Help wanted.",
    "created_at": "2009-12-12T01:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7652#issuecomment-65451",
    "user": "mvngu"
}
```

Attachment

New reviewer patch attached, which needs some reviewing. Note that the patch `trac_7652.patch` results in the following doctest failures:

```
[mvngu@sage sage-4.3.alpha1-7652-linear]$ ./sage -t -long devel/sage-main/doc/en/constructions/linear_programming.rst 
sage -t -long "devel/sage-main/doc/en/constructions/linear_programming.rst"
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/devel/sage-main/doc/en/constructions/linear_programming.rst", line 112:
    sage: p.set_objective( p["first unique variable"] + B[2] + p[-3] )
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[4]>", line 1, in <module>
        p.set_objective( p["first unique variable"] + B[Integer(2)] + p[-Integer(3)] )###line 112:
    sage: p.set_objective( p["first unique variable"] + B[2] + p[-3] )
    AttributeError: MixedIntegerLinearProgram instance has no attribute '__getitem__'
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha1-7652-linear/devel/sage-main/doc/en/constructions/linear_programming.rst", line 134:
    sage: print x_sol
Expected:
    {1: 0.83333333333333337, 2: 0.0}
Got:
    {1: None, 2: None}
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_2
   1 of   9 in __main__.example_3
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_linear_programming.py
	 [2.1 s]
exit code: 1024
```

My reviewer patch resolves the second failure, but I'm unable to resolve the first one. Help wanted.



---

archive/issue_comments_065452.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-12T09:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7652#issuecomment-65452",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065453.json:
```json
{
    "body": "Even when you think there is an error somewhere, your patches are perfect Minh !!! This example failed because of the patch #7637 mentioned in the description of the TRAC ticket, which is a small and recent improvement made for Martin Albrecht who needed something of the kind :-)\n\nOnce this patch is applied, yours is too, and there is no error in the docstrings, with or without the -optional flag... Positive review ! Thank you for your help again ! :-)\n\nNathann",
    "created_at": "2009-12-12T09:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7652#issuecomment-65453",
    "user": "ncohen"
}
```

Even when you think there is an error somewhere, your patches are perfect Minh !!! This example failed because of the patch #7637 mentioned in the description of the TRAC ticket, which is a small and recent improvement made for Martin Albrecht who needed something of the kind :-)

Once this patch is applied, yours is too, and there is no error in the docstrings, with or without the -optional flag... Positive review ! Thank you for your help again ! :-)

Nathann



---

archive/issue_comments_065454.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-14T16:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7652#issuecomment-65454",
    "user": "mhansen"
}
```

Resolution: fixed
