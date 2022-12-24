# Issue 877: "sage -coverage" should not care about functions which are local to other functions/methods

archive/issues_000877.json:
```json
{
    "body": "Assignee: tba\n\nCurrently, if you have something like:\n\n```\ndef foo():\n    def bar():\n        pass\n    pass\n```\n\nthen \"sage -coverage\" will complain that bar() has no docstring or doctests.  However, such functions cannot be (directly) doctested, so that warning is invalid.  In my opinion, bar() should not be required to have a docstring either.\n\nIssue created by migration from https://trac.sagemath.org/ticket/877\n\n",
    "created_at": "2007-10-13T13:47:23Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "\"sage -coverage\" should not care about functions which are local to other functions/methods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/877",
    "user": "cwitty"
}
```
Assignee: tba

Currently, if you have something like:

```
def foo():
    def bar():
        pass
    pass
```

then "sage -coverage" will complain that bar() has no docstring or doctests.  However, such functions cannot be (directly) doctested, so that warning is invalid.  In my opinion, bar() should not be required to have a docstring either.

Issue created by migration from https://trac.sagemath.org/ticket/877





---

archive/issue_comments_005425.json:
```json
{
    "body": "To get around this, I took my local function/method and made it a regular one.  I then used functools.partial to use it.   This allowed my function to be tested like every other one.  In the few cases where I had to do this, I ended up liking the functools version better.",
    "created_at": "2008-04-04T20:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5425",
    "user": "mhansen"
}
```

To get around this, I took my local function/method and made it a regular one.  I then used functools.partial to use it.   This allowed my function to be tested like every other one.  In the few cases where I had to do this, I ended up liking the functools version better.



---

archive/issue_comments_005426.json:
```json
{
    "body": "#4323 is a duplicate of that ticket.",
    "created_at": "2009-02-10T07:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5426",
    "user": "zimmerma"
}
```

#4323 is a duplicate of that ticket.



---

archive/issue_comments_005427.json:
```json
{
    "body": "Changing assignee from tba to jhpalmieri.",
    "created_at": "2009-07-24T23:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5427",
    "user": "jhpalmieri"
}
```

Changing assignee from tba to jhpalmieri.



---

archive/issue_comments_005428.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-24T23:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5428",
    "user": "jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005429.json:
```json
{
    "body": "Here is a patch for this.  With sage-4.1.1.alpha0, it increases overall coverage from 77.9% to 78.5%.\n\nTo test: I know that the files steenrod_algebra_element.py and structure/factorization.py have such nested functions, so try 'sage -coverage' on these files, before and after patching.",
    "created_at": "2009-07-24T23:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5429",
    "user": "jhpalmieri"
}
```

Here is a patch for this.  With sage-4.1.1.alpha0, it increases overall coverage from 77.9% to 78.5%.

To test: I know that the files steenrod_algebra_element.py and structure/factorization.py have such nested functions, so try 'sage -coverage' on these files, before and after patching.



---

archive/issue_comments_005430.json:
```json
{
    "body": "Attachment [trac_877-scripts-coverage.patch](tarball://root/attachments/some-uuid/ticket877/trac_877-scripts-coverage.patch) by jhpalmieri created at 2009-07-24 23:55:48\n\napply to scripts repository",
    "created_at": "2009-07-24T23:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5430",
    "user": "jhpalmieri"
}
```

Attachment [trac_877-scripts-coverage.patch](tarball://root/attachments/some-uuid/ticket877/trac_877-scripts-coverage.patch) by jhpalmieri created at 2009-07-24 23:55:48

apply to scripts repository



---

archive/issue_comments_005431.json:
```json
{
    "body": "(Maybe it only goes from 78.0% to 78.5%.)",
    "created_at": "2009-07-24T23:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5431",
    "user": "jhpalmieri"
}
```

(Maybe it only goes from 78.0% to 78.5%.)



---

archive/issue_comments_005432.json:
```json
{
    "body": "Looks good to me:\n\nBEFORE:\n\n```\n< Overall weighted coverage score:  77.8%\n< Total number of functions:  22395\n```\n\nAFTER\n\n```\n> Overall weighted coverage score:  78.3%\n> Total number of functions:  22207\n```\n\n\nThe code looks fine and it works fine, so far as I can tell.",
    "created_at": "2009-07-25T00:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5432",
    "user": "was"
}
```

Looks good to me:

BEFORE:

```
< Overall weighted coverage score:  77.8%
< Total number of functions:  22395
```

AFTER

```
> Overall weighted coverage score:  78.3%
> Total number of functions:  22207
```


The code looks fine and it works fine, so far as I can tell.



---

archive/issue_comments_005433.json:
```json
{
    "body": "quick note just from looking at the patch: i makes more sense to move the re.compile statement *before* the `while True:` loop. It's purpose is to speed up the regex searches and shouldn't be compiled in every loop! just exchange line 20 and 21 in the merged file.",
    "created_at": "2009-07-25T12:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5433",
    "user": "schilly"
}
```

quick note just from looking at the patch: i makes more sense to move the re.compile statement *before* the `while True:` loop. It's purpose is to speed up the regex searches and shouldn't be compiled in every loop! just exchange line 20 and 21 in the merged file.



---

archive/issue_comments_005434.json:
```json
{
    "body": "use this version instead",
    "created_at": "2009-07-25T14:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5434",
    "user": "jhpalmieri"
}
```

use this version instead



---

archive/issue_comments_005435.json:
```json
{
    "body": "Attachment [trac_877-scripts-coverage2.patch](tarball://root/attachments/some-uuid/ticket877/trac_877-scripts-coverage2.patch) by jhpalmieri created at 2009-07-25 15:00:33\n\ntrac_877-scripts-coverage2.patch interchanges the lines that schilly mentions.  It also moves another re.compile statement earlier.  It also stores the list of nested functions in the list \"closures\", for possible future use.",
    "created_at": "2009-07-25T15:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5435",
    "user": "jhpalmieri"
}
```

Attachment [trac_877-scripts-coverage2.patch](tarball://root/attachments/some-uuid/ticket877/trac_877-scripts-coverage2.patch) by jhpalmieri created at 2009-07-25 15:00:33

trac_877-scripts-coverage2.patch interchanges the lines that schilly mentions.  It also moves another re.compile statement earlier.  It also stores the list of nested functions in the list "closures", for possible future use.



---

archive/issue_comments_005436.json:
```json
{
    "body": "This is what I observe regarding John's patch. In Sage 4.1 without the patch `trac_877-scripts-coverage2.patch`, we have \n\n```\nOverall weighted coverage score:  77.8%\nTotal number of functions:  22398\n```\n\nApplying that patch to Sage 4.1:\n\n```\nOverall weighted coverage score:  78.3%\nTotal number of functions:  22210\n```\n\nIf I understand John's patch correctly, it doesn't count functions which are local to other functions/methods. This accounts for the reduced number of total functions after applying the patch. Moving on to Sage 4.1.1.alpha0 without the patch:\n\n```\nOverall weighted coverage score:  78.0%\nTotal number of functions:  22497\n```\n\nAnd with the patch:\n\n```\nOverall weighted coverage score:  78.5%\nTotal number of functions:  22308\n```\n\nHere is the coverage after applying the patch to my merge tree:\n\n```\nOverall weighted coverage score:  78.6%\nTotal number of functions:  22317\n```\n\n\n\nMerged `trac_877-scripts-coverage2.patch` in the scripts repository.",
    "created_at": "2009-07-25T19:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5436",
    "user": "mvngu"
}
```

This is what I observe regarding John's patch. In Sage 4.1 without the patch `trac_877-scripts-coverage2.patch`, we have 

```
Overall weighted coverage score:  77.8%
Total number of functions:  22398
```

Applying that patch to Sage 4.1:

```
Overall weighted coverage score:  78.3%
Total number of functions:  22210
```

If I understand John's patch correctly, it doesn't count functions which are local to other functions/methods. This accounts for the reduced number of total functions after applying the patch. Moving on to Sage 4.1.1.alpha0 without the patch:

```
Overall weighted coverage score:  78.0%
Total number of functions:  22497
```

And with the patch:

```
Overall weighted coverage score:  78.5%
Total number of functions:  22308
```

Here is the coverage after applying the patch to my merge tree:

```
Overall weighted coverage score:  78.6%
Total number of functions:  22317
```



Merged `trac_877-scripts-coverage2.patch` in the scripts repository.



---

archive/issue_comments_005437.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-25T19:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/877#issuecomment-5437",
    "user": "mvngu"
}
```

Resolution: fixed
