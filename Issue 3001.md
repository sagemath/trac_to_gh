# Issue 3001: sage ignores custom environment variables

archive/issues_003001.json:
```json
{
    "body": "Assignee: mabshoff\n\nIn sage-spkg \"gcc -v\" is used, instead of \"${CC-gcc} -v\". Easy fix:\n\n```\n\n---------------------------------------------------------------\n--- a/sage-spkg Mon Apr 21 01:43:53 2008 -0700\n+++ b/sage-spkg Tue Apr 22 12:37:48 2008 -0300\n@@ -241,8 +241,8 @@\n\n echo \"****************************************************\"\n echo \"GCC Version\"\n-echo \"gcc -v\"\n-gcc -v\n+echo \"${CC-gcc} -v\"\n+${CC-gcc} -v\n if [ $? -ne 0 ]; then\n   echo \"Unable to determine gcc version.\"\n fi\n---------------------------------------------------------------\n```\n\n\n\nIn sage-env, tests if CC is gcc, which means \"CC=gcc-4.3\" might not\nwork exactly the same as if gcc is a symlink to gcc-4.3, for instance:\n\n```\nif [ \"$SAGE64\" = \"yes\" -a CC = \"gcc\" ]; then\n  CFLAGS=\"$CFLAGS -m64\"\nfi\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3001\n\n",
    "created_at": "2008-04-22T16:48:10Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "sage ignores custom environment variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3001",
    "user": "@dfdeshom"
}
```
Assignee: mabshoff

In sage-spkg "gcc -v" is used, instead of "${CC-gcc} -v". Easy fix:

```

---------------------------------------------------------------
--- a/sage-spkg Mon Apr 21 01:43:53 2008 -0700
+++ b/sage-spkg Tue Apr 22 12:37:48 2008 -0300
@@ -241,8 +241,8 @@

 echo "****************************************************"
 echo "GCC Version"
-echo "gcc -v"
-gcc -v
+echo "${CC-gcc} -v"
+${CC-gcc} -v
 if [ $? -ne 0 ]; then
   echo "Unable to determine gcc version."
 fi
---------------------------------------------------------------
```



In sage-env, tests if CC is gcc, which means "CC=gcc-4.3" might not
work exactly the same as if gcc is a symlink to gcc-4.3, for instance:

```
if [ "$SAGE64" = "yes" -a CC = "gcc" ]; then
  CFLAGS="$CFLAGS -m64"
fi
```


Issue created by migration from https://trac.sagemath.org/ticket/3001





---

archive/issue_comments_020650.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-26T10:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3001#issuecomment-20650",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020651.json:
```json
{
    "body": "After thinking about this a little more: ${CC-gcc} is gcc specific and we can no longer assume that we are compiling with gcc in the first place. Hence I would like to suggest that we use `CC` and `CXX` in those places and make sure in `sage-env` that they are set.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T10:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3001#issuecomment-20651",
    "user": "mabshoff"
}
```

After thinking about this a little more: ${CC-gcc} is gcc specific and we can no longer assume that we are compiling with gcc in the first place. Hence I would like to suggest that we use `CC` and `CXX` in those places and make sure in `sage-env` that they are set.

Cheers,

Michael



---

archive/issue_comments_020652.json:
```json
{
    "body": "Attachment [trac_3001.patch](tarball://root/attachments/some-uuid/ticket3001/trac_3001.patch) by @dandrake created at 2009-07-02 02:30:25",
    "created_at": "2009-07-02T02:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3001#issuecomment-20652",
    "user": "@dandrake"
}
```

Attachment [trac_3001.patch](tarball://root/attachments/some-uuid/ticket3001/trac_3001.patch) by @dandrake created at 2009-07-02 02:30:25



---

archive/issue_comments_020653.json:
```json
{
    "body": "I also noticed that the sage_scripts spkg has an uncommitted change (from #6248), and a couple files that aren't checked in that perhaps should be. Whoever merges this patch should also take care of those little issues.",
    "created_at": "2009-07-02T02:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3001#issuecomment-20653",
    "user": "@dandrake"
}
```

I also noticed that the sage_scripts spkg has an uncommitted change (from #6248), and a couple files that aren't checked in that perhaps should be. Whoever merges this patch should also take care of those little issues.



---

archive/issue_comments_020654.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-26T02:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3001#issuecomment-20654",
    "user": "mvngu"
}
```

Resolution: fixed
