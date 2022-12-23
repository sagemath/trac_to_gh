# Issue 153: automated testing of the whole SAGE install

archive/issues_000153.json:
```json
{
    "body": "Assignee: was\n\nAdd the following:\n\n\n```\n  sage -i -t packagename.spkg\n```\n\n\nwill build and install the package and run whatever the standard tests are\nfor that package.  The tests will be run by running \n\n```\n  spkg-test\n```\n\nif that script is in the package.  Otherwise, it always reports failure.\nThen I go through and figure out what the test suite is for each package,\nand get it to work. \n\nHave a \"make safe\" which does build of all of SAGE but at each point\nrunning the tests.\n\nWilliam\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/153\n\n",
    "created_at": "2006-10-25T21:53:14Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "automated testing of the whole SAGE install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/153",
    "user": "was"
}
```
Assignee: was

Add the following:


```
  sage -i -t packagename.spkg
```


will build and install the package and run whatever the standard tests are
for that package.  The tests will be run by running 

```
  spkg-test
```

if that script is in the package.  Otherwise, it always reports failure.
Then I go through and figure out what the test suite is for each package,
and get it to work. 

Have a "make safe" which does build of all of SAGE but at each point
running the tests.

William


Issue created by migration from https://trac.sagemath.org/ticket/153





---

archive/issue_comments_000698.json:
```json
{
    "body": "This is a duplicate of #299.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-23T11:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/153#issuecomment-698",
    "user": "mabshoff"
}
```

This is a duplicate of #299.

Cheers,

Michael



---

archive/issue_comments_000699.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-08-23T11:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/153#issuecomment-699",
    "user": "mabshoff"
}
```

Resolution: duplicate
