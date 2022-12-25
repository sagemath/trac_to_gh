# Issue 5628: a little sage-flags.txt issue

archive/issues_005628.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nOn Sat, Mar 28, 2009 at 9:05 PM, Gonzalo Tornaria:\n>\n> I did an upgrade from 3.4 as follows:\n>\n> 1. sage -br main  ---> switch to main, which is CLEAN\n> 2. sage -upgrade\n> http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/sage-3.4.1.alpha0\n> 3. once that was finished, I pulled  the new changes into my sage-brandt branch\n> 4. applied the rebased 5520 + my tiny patch\n> 5. sage -br brandt\n>\n> But now, \"sage -br main\" (which is now clean 3.4.1.alpha0) causes the\n> same issue.\n>\n> Gonzalo\n\nJust delete \n   local/lib/sage-flags.txt\n\nAlso, I've opened a blocker ticket about this, since everybody who upgrades will run into exactly the same problem.  \n\nThe problem is that the new version of the script that checks the flags doesn't see sse4_1 anymore (nothing in Sage specifically uses that), but it's still in your old sage-flags.txt file.  Two possible solutions:\n   (1) delete sage-flags.txt as part of \"sage -upgrade\"\n   (2) make it so sse4_1 is specifically ignored.\n\nI like (1). \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5628\n\n",
    "created_at": "2009-03-29T03:29:59Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "a little sage-flags.txt issue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5628",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
On Sat, Mar 28, 2009 at 9:05 PM, Gonzalo Tornaria:
>
> I did an upgrade from 3.4 as follows:
>
> 1. sage -br main  ---> switch to main, which is CLEAN
> 2. sage -upgrade
> http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/sage-3.4.1.alpha0
> 3. once that was finished, I pulled  the new changes into my sage-brandt branch
> 4. applied the rebased 5520 + my tiny patch
> 5. sage -br brandt
>
> But now, "sage -br main" (which is now clean 3.4.1.alpha0) causes the
> same issue.
>
> Gonzalo

Just delete 
   local/lib/sage-flags.txt

Also, I've opened a blocker ticket about this, since everybody who upgrades will run into exactly the same problem.  

The problem is that the new version of the script that checks the flags doesn't see sse4_1 anymore (nothing in Sage specifically uses that), but it's still in your old sage-flags.txt file.  Two possible solutions:
   (1) delete sage-flags.txt as part of "sage -upgrade"
   (2) make it so sse4_1 is specifically ignored.

I like (1). 
```


Issue created by migration from https://trac.sagemath.org/ticket/5628





---

archive/issue_comments_043863.json:
```json
{
    "body": "Attachment [trac_5628-scripts.patch](tarball://root/attachments/some-uuid/ticket5628/trac_5628-scripts.patch) by @williamstein created at 2009-03-29 03:32:24",
    "created_at": "2009-03-29T03:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5628#issuecomment-43863",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5628-scripts.patch](tarball://root/attachments/some-uuid/ticket5628/trac_5628-scripts.patch) by @williamstein created at 2009-03-29 03:32:24



---

archive/issue_comments_043864.json:
```json
{
    "body": "The issue with this patch is that the `sage-flags.txt` file will not be regenerated unless sage install directory changes (because `write_flags_file()` is only called from within `install_moved()`.\n\nMaybe the flags file should also be created from the `check_processor_flags()` function. But then, this only works if sage is run at least once after an upgrade.\n\nOtherwise, doing `sage -upgrade` followed by `sage -bdist` ends up with a sage binary with no `sage-flags.txt`, defeating the purpose of the flags file.",
    "created_at": "2009-03-29T04:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5628#issuecomment-43864",
    "user": "https://github.com/tornaria"
}
```

The issue with this patch is that the `sage-flags.txt` file will not be regenerated unless sage install directory changes (because `write_flags_file()` is only called from within `install_moved()`.

Maybe the flags file should also be created from the `check_processor_flags()` function. But then, this only works if sage is run at least once after an upgrade.

Otherwise, doing `sage -upgrade` followed by `sage -bdist` ends up with a sage binary with no `sage-flags.txt`, defeating the purpose of the flags file.



---

archive/issue_comments_043865.json:
```json
{
    "body": "I have an alternative fix:\n\n```\ndiff -r 804879ae0134 sage-location\n--- a/sage-location     Thu Mar 26 16:43:48 2009 -0700\n+++ b/sage-location     Sat Mar 28 22:32:50 2009 -0700\n@@ -77,7 +77,7 @@\n     if not os.path.exists(flags_file): return\n     # We check that the processor flags of the original build are a\n     # subset of the new machine.  If not, we print a massive warning.\n-    X = set(open(flags_file).read().split())\n+    X = set(open(flags_file).read().split()).intersection(FLAGS)\n     Y = set(get_flags_info().split())\n     if not X.issubset(Y):\n         print \"\"\n```\n\n\nThis makes it so that only the flags listed in FLAGS are relevant for `check_processor_flags()`. Thus, after an upgrade, the flag `sse4_1` will still be in the flags file, but it won't be required at runtime.",
    "created_at": "2009-03-29T04:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5628#issuecomment-43865",
    "user": "https://github.com/tornaria"
}
```

I have an alternative fix:

```
diff -r 804879ae0134 sage-location
--- a/sage-location     Thu Mar 26 16:43:48 2009 -0700
+++ b/sage-location     Sat Mar 28 22:32:50 2009 -0700
@@ -77,7 +77,7 @@
     if not os.path.exists(flags_file): return
     # We check that the processor flags of the original build are a
     # subset of the new machine.  If not, we print a massive warning.
-    X = set(open(flags_file).read().split())
+    X = set(open(flags_file).read().split()).intersection(FLAGS)
     Y = set(get_flags_info().split())
     if not X.issubset(Y):
         print ""
```


This makes it so that only the flags listed in FLAGS are relevant for `check_processor_flags()`. Thus, after an upgrade, the flag `sse4_1` will still be in the flags file, but it won't be required at runtime.



---

archive/issue_comments_043866.json:
```json
{
    "body": "I actually like Gonzalo's fix better than William's - not sure what to do about this yet.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T00:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5628#issuecomment-43866",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I actually like Gonzalo's fix better than William's - not sure what to do about this yet.

Cheers,

Michael



---

archive/issue_comments_043867.json:
```json
{
    "body": "I'm fine with either version.",
    "created_at": "2009-04-06T17:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5628#issuecomment-43867",
    "user": "https://github.com/williamstein"
}
```

I'm fine with either version.



---

archive/issue_comments_043868.json:
```json
{
    "body": "This is a 3.4.1 blocker.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T18:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5628#issuecomment-43868",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a 3.4.1 blocker.

Cheers,

Michael



---

archive/issue_comments_043869.json:
```json
{
    "body": "Attachment [trac_5628.patch](tarball://root/attachments/some-uuid/ticket5628/trac_5628.patch) by mabshoff created at 2009-04-11 01:48:51\n\nPositive review for trac_5628.patch. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T01:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5628#issuecomment-43869",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5628.patch](tarball://root/attachments/some-uuid/ticket5628/trac_5628.patch) by mabshoff created at 2009-04-11 01:48:51

Positive review for trac_5628.patch. 

Cheers,

Michael



---

archive/issue_events_005869.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-11T01:49:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5628",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5628#event-5869"
}
```



---

archive/issue_comments_043870.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-11T01:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5628#issuecomment-43870",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043871.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T01:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5628#issuecomment-43871",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
