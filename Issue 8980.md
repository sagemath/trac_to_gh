# Issue 8980: gac script hardcodes build path

archive/issues_008980.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nwjlaffin@dellbees$ pwd\n/sage/local/lib/gap-4.4.12/bin/x86_64-unknown-linux-gnu-gcc\nwjlaffin@dellbees$ grep build -n gac\n54:gap_bin=/sage/spkg/build/gap-4.4.12.p3/src/bin/x86_64-unknown-linux-gnu-gcc\n```\n\n\nChanging the bin path to the path given by pwd fixes the problem. Needs a robust fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8980\n\n",
    "created_at": "2010-05-17T00:50:06Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "title": "gac script hardcodes build path",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8980",
    "user": "wjlaffin"
}
```
Assignee: tbd


```
wjlaffin@dellbees$ pwd
/sage/local/lib/gap-4.4.12/bin/x86_64-unknown-linux-gnu-gcc
wjlaffin@dellbees$ grep build -n gac
54:gap_bin=/sage/spkg/build/gap-4.4.12.p3/src/bin/x86_64-unknown-linux-gnu-gcc
```


Changing the bin path to the path given by pwd fixes the problem. Needs a robust fix.

Issue created by migration from https://trac.sagemath.org/ticket/8980





---

archive/issue_comments_082853.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2017-09-22T13:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8980#issuecomment-82853",
    "user": "jdemeyer"
}
```

Resolution: invalid



---

archive/issue_comments_082854.json:
```json
{
    "body": "Obsolete",
    "created_at": "2017-09-22T13:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8980#issuecomment-82854",
    "user": "jdemeyer"
}
```

Obsolete
