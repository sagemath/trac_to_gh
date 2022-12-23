# Issue 954: Make sure compiler is C99 capable

archive/issues_000954.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: gcc, flint, C99\n\nFlint requires C99 capable compilers. gcc 3.4.x and later are, but gcc 3.3 and earlier are not. There are still a number of those older compilers around, so error out early right away with an understandable error message to avoid bug reports with flint compiling to fail.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/954\n\n",
    "created_at": "2007-10-21T03:43:10Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Make sure compiler is C99 capable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/954",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Keywords: gcc, flint, C99

Flint requires C99 capable compilers. gcc 3.4.x and later are, but gcc 3.3 and earlier are not. There are still a number of those older compilers around, so error out early right away with an understandable error message to avoid bug reports with flint compiling to fail.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/954





---

archive/issue_comments_005808.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-21T03:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5808",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005809.json:
```json
{
    "body": "At least for gcc we can probably use\n\n```\ngcc -dumpversion\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-10-28T11:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5809",
    "user": "mabshoff"
}
```

At least for gcc we can probably use

```
gcc -dumpversion
```


Cheers,

Michael



---

archive/issue_comments_005810.json:
```json
{
    "body": "This can't be written using python, so...\nmaybe in perl?",
    "created_at": "2007-11-03T22:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5810",
    "user": "was"
}
```

This can't be written using python, so...
maybe in perl?



---

archive/issue_comments_005811.json:
```json
{
    "body": "perl script to test gcc version",
    "created_at": "2007-11-04T01:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5811",
    "user": "jkantor"
}
```

perl script to test gcc version



---

archive/issue_comments_005812.json:
```json
{
    "body": "Attachment\n\nI wrote a perl script to test if gcc version is greater than or equal to 3.4.0. \nIt exits 0 if this is the case and 1 otherwise. \n\nThe flint spkg-install should be easily modified to run this script and test the exit code and\ntake appropriate action. I didn't know what the desired behavior was so I didn't do this yet.",
    "created_at": "2007-11-04T01:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5812",
    "user": "jkantor"
}
```

Attachment

I wrote a perl script to test if gcc version is greater than or equal to 3.4.0. 
It exits 0 if this is the case and 1 otherwise. 

The flint spkg-install should be easily modified to run this script and test the exit code and
take appropriate action. I didn't know what the desired behavior was so I didn't do this yet.



---

archive/issue_comments_005813.json:
```json
{
    "body": "More specifically adding this to the top of the flint spkg-install should be enough\n\n\n```\n./test_gcc_version.pl\nif [ $? -ne 0 ]; then\n   echo \"GCC version less than 3.4.0\"\n   echo \"Flint will not be able to compile successfully\"\n   exit 1\nfi\n```\n",
    "created_at": "2007-11-04T01:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5813",
    "user": "jkantor"
}
```

More specifically adding this to the top of the flint spkg-install should be enough


```
./test_gcc_version.pl
if [ $? -ne 0 ]; then
   echo "GCC version less than 3.4.0"
   echo "Flint will not be able to compile successfully"
   exit 1
fi
```




---

archive/issue_comments_005814.json:
```json
{
    "body": "Merged in 1.9.1 alpha2",
    "created_at": "2007-12-20T21:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5814",
    "user": "rlm"
}
```

Merged in 1.9.1 alpha2



---

archive/issue_comments_005815.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-20T21:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5815",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_005816.json:
```json
{
    "body": "rather 2.9.1 alpha2...",
    "created_at": "2007-12-20T21:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/954#issuecomment-5816",
    "user": "rlm"
}
```

rather 2.9.1 alpha2...
