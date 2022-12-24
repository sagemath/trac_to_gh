# Issue 4936: massive bloat: make something delete everything in ~/.sage/gap > 1 week old and untouched

archive/issues_004936.json:
```json
{
    "body": "Assignee: mabshoff\n\nIt is *always* safe to delete anything in ~/.sage/gap, since it will get autorecreated when Sage is started.   I just looked at my ~/.sage/gap on sage.math and it is HUGE:\n\n\n```\nwstein@sage:~/.sage/gap$ ls -1 |wc -l\n90\nwstein@sage:~/.sage/gap$ du -sch .\n1.3G\t.\n1.3G\ttotal\n```\n\n\nI have stuff in there going back to March 2008.\n\nThe code in gap.py that creates the workspace in .sage/gap should also delete all old workspaces.   I think 1 week is arbitrary, but is safe since as mentioned above any time length is safe.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4936\n\n",
    "created_at": "2009-01-04T17:02:31Z",
    "labels": [
        "performance",
        "major",
        "bug"
    ],
    "title": "massive bloat: make something delete everything in ~/.sage/gap > 1 week old and untouched",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4936",
    "user": "was"
}
```
Assignee: mabshoff

It is *always* safe to delete anything in ~/.sage/gap, since it will get autorecreated when Sage is started.   I just looked at my ~/.sage/gap on sage.math and it is HUGE:


```
wstein@sage:~/.sage/gap$ ls -1 |wc -l
90
wstein@sage:~/.sage/gap$ du -sch .
1.3G	.
1.3G	total
```


I have stuff in there going back to March 2008.

The code in gap.py that creates the workspace in .sage/gap should also delete all old workspaces.   I think 1 week is arbitrary, but is safe since as mentioned above any time length is safe.

Issue created by migration from https://trac.sagemath.org/ticket/4936





---

archive/issue_comments_037471.json:
```json
{
    "body": "I know there are GAP users who always load GAP via a workspace. I'm worried that if the only way to use GAP in Sage was to use a \"recent\" workspace then these users would not be well-werved.\n\nA possible workaround would be if there was a way to optionally use a specific workspace. In other words, .\\sage -gap and gap_console() could take an optional argument with a specific workspace. Does this seem reasonable? It might be rarely used, but it could be a potentially very useful feature to allow users to use another workspace.",
    "created_at": "2009-01-04T17:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4936#issuecomment-37471",
    "user": "wdj"
}
```

I know there are GAP users who always load GAP via a workspace. I'm worried that if the only way to use GAP in Sage was to use a "recent" workspace then these users would not be well-werved.

A possible workaround would be if there was a way to optionally use a specific workspace. In other words, .\sage -gap and gap_console() could take an optional argument with a specific workspace. Does this seem reasonable? It might be rarely used, but it could be a potentially very useful feature to allow users to use another workspace.



---

archive/issue_comments_037472.json:
```json
{
    "body": "> I know there are GAP users who always load GAP via a workspace. \n> I'm worried that if the only way to use GAP in Sage was to use \n> a \"recent\" workspace then these users would not be well-werved.\n\nThis criticism of my suggestion doesn't make sense, because I'm *only* suggesting deleting the old workspaces in ~/.sage/gap/.  Not all workspaces on the users computer or something.      Anyway, I think your worry about makes no sense (to me). Please correct me if I'm wrong (quite possible).  Thanks.",
    "created_at": "2009-01-05T17:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4936#issuecomment-37472",
    "user": "was"
}
```

> I know there are GAP users who always load GAP via a workspace. 
> I'm worried that if the only way to use GAP in Sage was to use 
> a "recent" workspace then these users would not be well-werved.

This criticism of my suggestion doesn't make sense, because I'm *only* suggesting deleting the old workspaces in ~/.sage/gap/.  Not all workspaces on the users computer or something.      Anyway, I think your worry about makes no sense (to me). Please correct me if I'm wrong (quite possible).  Thanks.



---

archive/issue_comments_037473.json:
```json
{
    "body": "To test the attached patch, look $HOME/.sage/gap, and notice if you have a lot of old files there.  Maybe even fake some old workspace files like this:\n\n```\ntouch -t 01010000 workspace-00\n```\n\n\nThen touch local/bin/gap_stamp to force a recheck\n\n```\ncd SAGE_ROOT\ntouch local/bin/gap_stamp\n```\n\n\nand note that when you start sage the files you created in $DOT_SAGE/gap are deleted.",
    "created_at": "2009-01-24T06:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4936#issuecomment-37473",
    "user": "was"
}
```

To test the attached patch, look $HOME/.sage/gap, and notice if you have a lot of old files there.  Maybe even fake some old workspace files like this:

```
touch -t 01010000 workspace-00
```


Then touch local/bin/gap_stamp to force a recheck

```
cd SAGE_ROOT
touch local/bin/gap_stamp
```


and note that when you start sage the files you created in $DOT_SAGE/gap are deleted.



---

archive/issue_comments_037474.json:
```json
{
    "body": "Attachment [trac_4936.patch](tarball://root/attachments/some-uuid/ticket4936/trac_4936.patch) by mhansen created at 2009-01-24 06:31:20\n\nThis works perfectly for me.",
    "created_at": "2009-01-24T06:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4936#issuecomment-37474",
    "user": "mhansen"
}
```

Attachment [trac_4936.patch](tarball://root/attachments/some-uuid/ticket4936/trac_4936.patch) by mhansen created at 2009-01-24 06:31:20

This works perfectly for me.



---

archive/issue_comments_037475.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T14:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4936#issuecomment-37475",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037476.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T14:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4936#issuecomment-37476",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2
