# Issue 2662: simplify_full function

archive/issues_002662.json:
```json
{
    "body": "Assignee: was\n\nCreate a simplify_full function that (somewhat intelligently?) applies a battery simplifications to try to get a function to be simpler.  \n\nIt would be nice to support some of the options that FullSimplify in Mma has (see http://reference.wolfram.com/mathematica/ref/FullSimplify.html?q=fullsimplify&lang=en ):\n\n* user can pass in a \"complexity function\" which determines how simple an expression is\n* user can pass in a time limit for the simplification\n* user can pass in a list of things that won't be simplified\n* etc.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2662\n\n",
    "created_at": "2008-03-24T21:18:35Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "simplify_full function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2662",
    "user": "jason"
}
```
Assignee: was

Create a simplify_full function that (somewhat intelligently?) applies a battery simplifications to try to get a function to be simpler.  

It would be nice to support some of the options that FullSimplify in Mma has (see http://reference.wolfram.com/mathematica/ref/FullSimplify.html?q=fullsimplify&lang=en ):

* user can pass in a "complexity function" which determines how simple an expression is
* user can pass in a time limit for the simplification
* user can pass in a list of things that won't be simplified
* etc.


Issue created by migration from https://trac.sagemath.org/ticket/2662





---

archive/issue_comments_018323.json:
```json
{
    "body": "mhansen created a simplify_full function in #2661.  So how about this ticket is the enhancement ticket for putting the Mma options that we can into full_simplify.",
    "created_at": "2008-03-24T21:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2662#issuecomment-18323",
    "user": "jason"
}
```

mhansen created a simplify_full function in #2661.  So how about this ticket is the enhancement ticket for putting the Mma options that we can into full_simplify.



---

archive/issue_comments_018324.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-25T00:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2662#issuecomment-18324",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018325.json:
```json
{
    "body": "Changing assignee from was to gfurnish.",
    "created_at": "2008-03-25T00:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2662#issuecomment-18325",
    "user": "gfurnish"
}
```

Changing assignee from was to gfurnish.



---

archive/issue_comments_018326.json:
```json
{
    "body": "This definately *has* to be handled better in new symbolics then it is currently.",
    "created_at": "2008-03-25T00:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2662#issuecomment-18326",
    "user": "gfurnish"
}
```

This definately *has* to be handled better in new symbolics then it is currently.



---

archive/issue_comments_018327.json:
```json
{
    "body": "Note also there are several other open tickets about the various simplify functions, with no resolution yet on what our \"real\" options should be.",
    "created_at": "2009-12-30T04:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2662#issuecomment-18327",
    "user": "kcrisman"
}
```

Note also there are several other open tickets about the various simplify functions, with no resolution yet on what our "real" options should be.



---

archive/issue_comments_018328.json:
```json
{
    "body": "#13099 is related.",
    "created_at": "2012-12-04T16:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2662#issuecomment-18328",
    "user": "jason"
}
```

#13099 is related.
