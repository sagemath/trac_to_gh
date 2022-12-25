# Issue 3902: %cython -- add an option #clibinclude that is like cinclude; otherwise linking in your own libraries is impossible

archive/issues_003902.json:
```json
{
    "body": "Assignee: cwitty\n\nRight now we have\n\n```\n      \\item[clang] may be either c or c++ indicating whether a C or\n                   C++ compiler should be used\n\n      \\item[clib] additional libraries to be linked in, the space\n                  separated list is split and passed to distutils.\n\n      \\item[cinclude] additional directories to search for header\n                      files. The space separated list is split and\n                      passed to distutils.\n```\n\nand we need\n\n```\n      \\item[clibinclude] additional directories to search for library\n                      files. The space separated list is split and\n                      passed to distutils.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3902\n\n",
    "created_at": "2008-08-19T21:27:53Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "%cython -- add an option #clibinclude that is like cinclude; otherwise linking in your own libraries is impossible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3902",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

Right now we have

```
      \item[clang] may be either c or c++ indicating whether a C or
                   C++ compiler should be used

      \item[clib] additional libraries to be linked in, the space
                  separated list is split and passed to distutils.

      \item[cinclude] additional directories to search for header
                      files. The space separated list is split and
                      passed to distutils.
```

and we need

```
      \item[clibinclude] additional directories to search for library
                      files. The space separated list is split and
                      passed to distutils.
```


Issue created by migration from https://trac.sagemath.org/ticket/3902





---

archive/issue_comments_027862.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3902#issuecomment-27862",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_027863.json:
```json
{
    "body": "Obsoleted by Cython features.",
    "created_at": "2019-01-11T13:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3902#issuecomment-27863",
    "user": "https://github.com/jdemeyer"
}
```

Obsoleted by Cython features.



---

archive/issue_comments_027864.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2019-01-11T13:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3902#issuecomment-27864",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: wontfix
