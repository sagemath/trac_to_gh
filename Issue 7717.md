# Issue 7717: sage -coverage enhancement

archive/issues_007717.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: coverage\n\nAdds features to the sage-coverage script.\n\n- rewrite for modularity and easier addition of features\n- changes the score of the file to reflect the presence or absence of a TestSuite.run or equivalent test.\n- adds option to check cdef'd functions\n- adds option to check docstrings on classes\n- adds option to check for the existence of INPUT block\n- adds option to check that parameters are all listed in the INPUT block.\n- adds option to check for the existence of OUTPUT block\n\nSo that we don't bring our coverage level way down, these aren't turned on automatically.  Instead, they can be invoked from the command line by using options ( -cdefs, -classes, -input, -output and -params)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7717\n\n",
    "created_at": "2009-12-17T01:44:07Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage -coverage enhancement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7717",
    "user": "roed"
}
```
Assignee: mvngu

Keywords: coverage

Adds features to the sage-coverage script.

- rewrite for modularity and easier addition of features
- changes the score of the file to reflect the presence or absence of a TestSuite.run or equivalent test.
- adds option to check cdef'd functions
- adds option to check docstrings on classes
- adds option to check for the existence of INPUT block
- adds option to check that parameters are all listed in the INPUT block.
- adds option to check for the existence of OUTPUT block

So that we don't bring our coverage level way down, these aren't turned on automatically.  Instead, they can be invoked from the command line by using options ( -cdefs, -classes, -input, -output and -params)

Issue created by migration from https://trac.sagemath.org/ticket/7717





---

archive/issue_comments_066283.json:
```json
{
    "body": "Duplicate of 7716: please delete.",
    "created_at": "2009-12-17T01:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7717#issuecomment-66283",
    "user": "roed"
}
```

Duplicate of 7716: please delete.



---

archive/issue_comments_066284.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-12-17T01:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7717#issuecomment-66284",
    "user": "mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_066285.json:
```json
{
    "body": "Closing this as a duplicate of #7716.",
    "created_at": "2009-12-17T01:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7717#issuecomment-66285",
    "user": "mvngu"
}
```

Closing this as a duplicate of #7716.
