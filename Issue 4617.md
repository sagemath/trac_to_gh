# Issue 4617: Create a `test-dummy.spkg`

archive/issues_004617.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: dummy test package\n\nThis is related with ticket #4587\n\nFor doc-testing the installation of packages, there should be some `test-dummy.spkg`\n\nThe purpose of the package is to do *nothing*. William suggested to mark it `optional -- admin`, I am not sure what that means.\n\nAlso, there should be an easy way to get rid of `test-dummy.spkg` after installation.\n\nIdea:\n* `sage -i test-dummy.spkg` should simply result in an entry in the list of installed packages.\n* uninstalling it is done by removing the list entry and deleting the file `test-dummy.spkg`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4617\n\n",
    "created_at": "2008-11-25T12:55:40Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "title": "Create a `test-dummy.spkg`",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4617",
    "user": "SimonKing"
}
```
Assignee: mabshoff

Keywords: dummy test package

This is related with ticket #4587

For doc-testing the installation of packages, there should be some `test-dummy.spkg`

The purpose of the package is to do *nothing*. William suggested to mark it `optional -- admin`, I am not sure what that means.

Also, there should be an easy way to get rid of `test-dummy.spkg` after installation.

Idea:
* `sage -i test-dummy.spkg` should simply result in an entry in the list of installed packages.
* uninstalling it is done by removing the list entry and deleting the file `test-dummy.spkg`.

Issue created by migration from https://trac.sagemath.org/ticket/4617





---

archive/issue_comments_034655.json:
```json
{
    "body": "Replying to [ticket:4617 SimonKing]:\n> William suggested to mark it `optional -- admin`, I am not sure what that means. [it means that it would only be tested when we do sage -t -only_optional=admin, where admin means \"tested by the admin who has write privileges to the sage install]\n\nThanks! \n\n>  * uninstalling it is done by removing the list entry and deleting the file `test-dummy.spkg`.\n\n... which probably also requires admin privileges. So, the to-be-created doctests for #4587 will also be optional -- admin, right?",
    "created_at": "2008-11-25T20:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4617#issuecomment-34655",
    "user": "SimonKing"
}
```

Replying to [ticket:4617 SimonKing]:
> William suggested to mark it `optional -- admin`, I am not sure what that means. [it means that it would only be tested when we do sage -t -only_optional=admin, where admin means "tested by the admin who has write privileges to the sage install]

Thanks! 

>  * uninstalling it is done by removing the list entry and deleting the file `test-dummy.spkg`.

... which probably also requires admin privileges. So, the to-be-created doctests for #4587 will also be optional -- admin, right?



---

archive/issue_comments_034656.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-11-06T15:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4617#issuecomment-34656",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_034657.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-11-06T15:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4617#issuecomment-34657",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034658.json:
```json
{
    "body": "Obsolete",
    "created_at": "2014-11-06T15:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4617#issuecomment-34658",
    "user": "jdemeyer"
}
```

Obsolete



---

archive/issue_comments_034659.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-11-07T16:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4617#issuecomment-34659",
    "user": "vbraun"
}
```

Resolution: wontfix
