# Issue 5515: "make" attempts to build documentation even if the build fails

archive/issues_005515.json:
```json
{
    "body": "Assignee: mabshoff\n\nIn $SAGE_ROOT/spkg/install:\n\n```\ntime make -f standard/deps $1\n\"$SAGE_ROOT\"/sage -docbuild --jsmath all html\n```\n\n\nThis hides the true cause of a build error if something goes wrong -- you see a totally irrelevant error about failing to build the documentation, instead of a useful error about whatever went wrong with the build.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5515\n\n",
    "created_at": "2009-03-14T15:09:49Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"make\" attempts to build documentation even if the build fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5515",
    "user": "cwitty"
}
```
Assignee: mabshoff

In $SAGE_ROOT/spkg/install:

```
time make -f standard/deps $1
"$SAGE_ROOT"/sage -docbuild --jsmath all html
```


This hides the true cause of a build error if something goes wrong -- you see a totally irrelevant error about failing to build the documentation, instead of a useful error about whatever went wrong with the build.

Issue created by migration from https://trac.sagemath.org/ticket/5515





---

archive/issue_comments_042870.json:
```json
{
    "body": "I was hit by this issue in three different ways, with different errors reported:\n1. error building `gmp-mpir-0.9` (#5516), when I didn't have system wide python installed, the error reported in the last line in the compilation was:\n\n```\n/opt/sage/sage-3.4/local/bin/sage-sage: line 852: python: command not found\n```\n\n2. same error in `gmp-mpir-0.9` (#5516), after installing system wide python, the error reported was:\n\n```\npython: can't open file '/opt/sage/sage-3.4/devel/sage/doc/common/builder.py': [Errno 2] No such file or directory\n```\n\n3. error building `cvxopt-0.9.p7` (#5517), the error reported was:\n\n```\nImportError: No module named jinja\n```\n\nI think all of these misreporting are due to the issue reported in this ticket. The actual issues in `gmp-mpir-0.9` and `cvxopt-0.9.p7` are reported in #5516 and #5517 resp.",
    "created_at": "2009-03-14T16:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5515#issuecomment-42870",
    "user": "tornaria"
}
```

I was hit by this issue in three different ways, with different errors reported:
1. error building `gmp-mpir-0.9` (#5516), when I didn't have system wide python installed, the error reported in the last line in the compilation was:

```
/opt/sage/sage-3.4/local/bin/sage-sage: line 852: python: command not found
```

2. same error in `gmp-mpir-0.9` (#5516), after installing system wide python, the error reported was:

```
python: can't open file '/opt/sage/sage-3.4/devel/sage/doc/common/builder.py': [Errno 2] No such file or directory
```

3. error building `cvxopt-0.9.p7` (#5517), the error reported was:

```
ImportError: No module named jinja
```

I think all of these misreporting are due to the issue reported in this ticket. The actual issues in `gmp-mpir-0.9` and `cvxopt-0.9.p7` are reported in #5516 and #5517 resp.



---

archive/issue_comments_042871.json:
```json
{
    "body": "Duplicate of #6295.",
    "created_at": "2009-08-30T18:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5515#issuecomment-42871",
    "user": "timdumol"
}
```

Duplicate of #6295.



---

archive/issue_comments_042872.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-09-26T07:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5515#issuecomment-42872",
    "user": "mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_042873.json:
```json
{
    "body": "Close this ticket as a duplicate of #6295.",
    "created_at": "2009-09-26T07:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5515#issuecomment-42873",
    "user": "mvngu"
}
```

Close this ticket as a duplicate of #6295.
