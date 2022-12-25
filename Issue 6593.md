# Issue 6593: [with patch, positive review] WordMorphism: doctest failure in Fedora

archive/issues_006593.json:
```json
{
    "body": "Assignee: @seblabbe\n\nCC:  sage-combinat @jaapspies\n\nKeywords: word morphism\n\nWhen sage-4.1.1.alpha0 was released (see http://groups.google.com/group/sage-devel/browse_thread/thread/267a2cb90085536b?hl=en), the following problem was reported :\n\n```\nSame here on Fedora 10 and Fedora 11, 32 bit.\n\nIn addition both in a fresh install and in an upgrade:\n\nsage -t  \"devel/sage/sage/combinat/words/morphism.py\"\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.1/devel/sage/sage/combinat/words/morphism.py\", line 616:\n     sage: m.extend_by(n)\nExpected:\n     Morphism from Words over Ordered Alphabet ['a', 'b', 0, 1] to Words over Ordered Alphabet ['a', 'b', 0, 1]\nGot:\n     Morphism from Words over Ordered Alphabet [0, 1, 'a', 'b'] to Words over Ordered Alphabet [0, 1, 'a', 'b']\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.1/devel/sage/sage/combinat/words/morphism.py\", line 618:\n     sage: n.extend_by(m)\nExpected:\n     Morphism from Words over Ordered Alphabet ['a', 'b', 0, 1] to Words over Ordered Alphabet ['a', 'b', 0, 1, 5]\nGot:\n     Morphism from Words over Ordered Alphabet [0, 1, 'a', 'b'] to Words over Ordered Alphabet [0, 1, 5, 'a', 'b']\n**********************************************************************\n1 items had failures:\n    2 of  10 in __main__.example_11\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/jaap/Download/sage-4.1/tmp/.doctest_morphism.py\n         [3.2 s]\nexit code: 1024\n\nJaap \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6593\n\n",
    "closed_at": "2009-07-23T06:04:57Z",
    "created_at": "2009-07-22T16:31:05Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, positive review] WordMorphism: doctest failure in Fedora",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6593",
    "user": "https://github.com/seblabbe"
}
```
Assignee: @seblabbe

CC:  sage-combinat @jaapspies

Keywords: word morphism

When sage-4.1.1.alpha0 was released (see http://groups.google.com/group/sage-devel/browse_thread/thread/267a2cb90085536b?hl=en), the following problem was reported :

```
Same here on Fedora 10 and Fedora 11, 32 bit.

In addition both in a fresh install and in an upgrade:

sage -t  "devel/sage/sage/combinat/words/morphism.py"
**********************************************************************
File "/home/jaap/Download/sage-4.1/devel/sage/sage/combinat/words/morphism.py", line 616:
     sage: m.extend_by(n)
Expected:
     Morphism from Words over Ordered Alphabet ['a', 'b', 0, 1] to Words over Ordered Alphabet ['a', 'b', 0, 1]
Got:
     Morphism from Words over Ordered Alphabet [0, 1, 'a', 'b'] to Words over Ordered Alphabet [0, 1, 'a', 'b']
**********************************************************************
File "/home/jaap/Download/sage-4.1/devel/sage/sage/combinat/words/morphism.py", line 618:
     sage: n.extend_by(m)
Expected:
     Morphism from Words over Ordered Alphabet ['a', 'b', 0, 1] to Words over Ordered Alphabet ['a', 'b', 0, 1, 5]
Got:
     Morphism from Words over Ordered Alphabet [0, 1, 'a', 'b'] to Words over Ordered Alphabet [0, 1, 5, 'a', 'b']
**********************************************************************
1 items had failures:
    2 of  10 in __main__.example_11
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/jaap/Download/sage-4.1/tmp/.doctest_morphism.py
         [3.2 s]
exit code: 1024

Jaap 
```

Issue created by migration from https://trac.sagemath.org/ticket/6593





---

archive/issue_comments_053855.json:
```json
{
    "body": "Attachment [trac_6593-word-morphism-doctest-sl.patch](tarball://root/attachments/some-uuid/ticket6593/trac_6593-word-morphism-doctest-sl.patch) by @seblabbe created at 2009-07-22 17:08:55",
    "created_at": "2009-07-22T17:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6593#issuecomment-53855",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_6593-word-morphism-doctest-sl.patch](tarball://root/attachments/some-uuid/ticket6593/trac_6593-word-morphism-doctest-sl.patch) by @seblabbe created at 2009-07-22 17:08:55



---

archive/issue_comments_053856.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-22T17:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6593#issuecomment-53856",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to assigned.



---

archive/issue_comments_053857.json:
```json
{
    "body": "The patch simply use the print statement which call the `__str__` instead of `__repr__`. The `__str__` sorts the string enumeration before printing it so that it should print the same way on Fedora or on other system.",
    "created_at": "2009-07-22T17:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6593#issuecomment-53857",
    "user": "https://github.com/seblabbe"
}
```

The patch simply use the print statement which call the `__str__` instead of `__repr__`. The `__str__` sorts the string enumeration before printing it so that it should print the same way on Fedora or on other system.



---

archive/issue_comments_053858.json:
```json
{
    "body": "After applying the patch in Fedora 11, 32 bit:\n\n```\n[jaap@paix sage-4.1.1.alpha0]$ ./sage -t \"devel/sage/sage/combinat/words/morphism.py\"\nsage -t  \"devel/sage/sage/combinat/words/morphism.py\"       \n\t [4.9 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.9 seconds\n\n```\n\n\nJaap",
    "created_at": "2009-07-22T21:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6593#issuecomment-53858",
    "user": "https://github.com/jaapspies"
}
```

After applying the patch in Fedora 11, 32 bit:

```
[jaap@paix sage-4.1.1.alpha0]$ ./sage -t "devel/sage/sage/combinat/words/morphism.py"
sage -t  "devel/sage/sage/combinat/words/morphism.py"       
	 [4.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.9 seconds

```


Jaap



---

archive/issue_events_015545.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-23T06:04:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6593",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6593#event-15545"
}
```



---

archive/issue_comments_053859.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T06:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6593#issuecomment-53859",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
