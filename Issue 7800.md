# Issue 7800: dsage -- re-enable use of openssl to certificate keys, if openssl is installed  (why the notebook in secure mode is so slow to generate initial kesy!)

archive/issues_007800.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: notebook secure dsage\n\nFor some mysterious reason somebody disabled use of openssl with dsage to create certificates. This new spkg fixes this problem. The actual patch is a simple 1-liner: \n\n```\nwstein@boxen:~/build/referee/sage-4.3/spkg/standard/dsage-1.0.1.p0/src/dsage/scripts$ hg diff\ndiff --git a/dsage/scripts/dsage_setup.py b/dsage/scripts/dsage_setup.py\n--- a/dsage/scripts/dsage_setup.py\n+++ b/dsage/scripts/dsage_setup.py\n@@ -174,7 +174,7 @@\n     print DELIMITER\n     print \"Generating SSL certificate for server...\"\n     \n-    if False and os.uname()[0] != 'Darwin' and cmd_exists('openssl'):\n+    if os.uname()[0] != 'Darwin' and cmd_exists('openssl'):\n         # We use openssl by default if it exists, since it is *vastly*\n         # faster on Linux.\n         cmd = ['openssl genrsa > %s' % privkey_file]\n```\n\n\nWithout this, on many platforms -- e.g., sage.math -- it takes hours to generate keys, since GNUtls's key generation program is crap.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7800\n\n",
    "created_at": "2009-12-31T17:19:50Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "dsage -- re-enable use of openssl to certificate keys, if openssl is installed  (why the notebook in secure mode is so slow to generate initial kesy!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7800",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

Keywords: notebook secure dsage

For some mysterious reason somebody disabled use of openssl with dsage to create certificates. This new spkg fixes this problem. The actual patch is a simple 1-liner: 

```
wstein@boxen:~/build/referee/sage-4.3/spkg/standard/dsage-1.0.1.p0/src/dsage/scripts$ hg diff
diff --git a/dsage/scripts/dsage_setup.py b/dsage/scripts/dsage_setup.py
--- a/dsage/scripts/dsage_setup.py
+++ b/dsage/scripts/dsage_setup.py
@@ -174,7 +174,7 @@
     print DELIMITER
     print "Generating SSL certificate for server..."
     
-    if False and os.uname()[0] != 'Darwin' and cmd_exists('openssl'):
+    if os.uname()[0] != 'Darwin' and cmd_exists('openssl'):
         # We use openssl by default if it exists, since it is *vastly*
         # faster on Linux.
         cmd = ['openssl genrsa > %s' % privkey_file]
```


Without this, on many platforms -- e.g., sage.math -- it takes hours to generate keys, since GNUtls's key generation program is crap.

Issue created by migration from https://trac.sagemath.org/ticket/7800





---

archive/issue_comments_067371.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-31T17:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7800#issuecomment-67371",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067372.json:
```json
{
    "body": "The new spkg is here:\n\n  http://wstein.org/home/wstein/patches/dsage-1.0.1.p1.spkg",
    "created_at": "2009-12-31T17:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7800#issuecomment-67372",
    "user": "https://github.com/williamstein"
}
```

The new spkg is here:

  http://wstein.org/home/wstein/patches/dsage-1.0.1.p1.spkg



---

archive/issue_comments_067373.json:
```json
{
    "body": "Post on mailing list:\n\n\n```\n\nHi,\n\nI kept suggesting the above, because long ago I wrote this code in dsage:\n\n-------------\n    if os.uname()[0] != 'Darwin' and cmd_exists('openssl'):\n        # We use openssl by default if it exists, since it is *vastly*\n        # faster on Linux.\n        cmd = ['openssl genrsa > %s' % privkey_file]\n        print \"Using openssl to generate key\"\n        print cmd[0]\n        subprocess.call(cmd, shell=True)\n-------------\n\nSo I thought people were having issues with slow keys since they didn't have openssl installed.  However, I just checked and the above code mysteriously morphed into:\n\n-------------\n    if False and os.uname()[0] != 'Darwin' and cmd_exists('openssl'):\n        # We use openssl by default if it exists, since it is *vastly*\n        # faster on Linux.\n        cmd = ['openssl genrsa > %s' % privkey_file]\n        print \"Using openssl to generate key\"\n        print cmd[0]\n        subprocess.call(cmd, shell=True)\n    else:...\n-------------\n\nI'm guessing somebody tested certtool on one platform where they got luck and certtool seemed to actually work in a reasonable amount of time, and concluded the issue was fixed.  Nope. \n\nPlease referee\n\n   http://trac.sagemath.org/sage_trac/ticket/7800\n\nwhich reverts this behavior, switching back to using openssl if available. \n```\n",
    "created_at": "2009-12-31T17:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7800#issuecomment-67373",
    "user": "https://github.com/williamstein"
}
```

Post on mailing list:


```

Hi,

I kept suggesting the above, because long ago I wrote this code in dsage:

-------------
    if os.uname()[0] != 'Darwin' and cmd_exists('openssl'):
        # We use openssl by default if it exists, since it is *vastly*
        # faster on Linux.
        cmd = ['openssl genrsa > %s' % privkey_file]
        print "Using openssl to generate key"
        print cmd[0]
        subprocess.call(cmd, shell=True)
-------------

So I thought people were having issues with slow keys since they didn't have openssl installed.  However, I just checked and the above code mysteriously morphed into:

-------------
    if False and os.uname()[0] != 'Darwin' and cmd_exists('openssl'):
        # We use openssl by default if it exists, since it is *vastly*
        # faster on Linux.
        cmd = ['openssl genrsa > %s' % privkey_file]
        print "Using openssl to generate key"
        print cmd[0]
        subprocess.call(cmd, shell=True)
    else:...
-------------

I'm guessing somebody tested certtool on one platform where they got luck and certtool seemed to actually work in a reasonable amount of time, and concluded the issue was fixed.  Nope. 

Please referee

   http://trac.sagemath.org/sage_trac/ticket/7800

which reverts this behavior, switching back to using openssl if available. 
```




---

archive/issue_comments_067374.json:
```json
{
    "body": "Can you check in all existing changes?\n\n```\n[mvngu@boxen dsage-1.0.1.p1]$ hg st\nM SPKG.txt\n```\n",
    "created_at": "2010-01-05T22:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7800#issuecomment-67374",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Can you check in all existing changes?

```
[mvngu@boxen dsage-1.0.1.p1]$ hg st
M SPKG.txt
```




---

archive/issue_comments_067375.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-06T01:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7800#issuecomment-67375",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067376.json:
```json
{
    "body": "I took the source tarball of Sage 4.3.1.alpha1, replaced `dsage-1.0.1.p0.spkg` with `dsage-1.0.1.p1.spkg`, and built Sage 4.3.1.alpha1 on mod.math with this updated dsage spkg. The build went OK, the only doctest failure is\n\n```\nsage -t -long devel/sage/sage/misc/sagedoc.py # 1 doctests failed\n```\n\nwhich is already reported at [sage-devel](http://groups.google.com/group/sage-devel/msg/4c7635baffe9b1f3). I then set the variable DOT_SAGE to a directory other than my home directory, loaded the newly compiled Sage, and started the notebook. As advertised, the RSA key generation process now uses openssl (which is available on mod.math). Using openssl, the key generation process is now much faster than previously (almost instantaneous). Before merging the updated dsage spkg, all outstanding changes need to be checked in. This is a positive review, provided that the check in issue is taken care of.",
    "created_at": "2010-01-06T01:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7800#issuecomment-67376",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I took the source tarball of Sage 4.3.1.alpha1, replaced `dsage-1.0.1.p0.spkg` with `dsage-1.0.1.p1.spkg`, and built Sage 4.3.1.alpha1 on mod.math with this updated dsage spkg. The build went OK, the only doctest failure is

```
sage -t -long devel/sage/sage/misc/sagedoc.py # 1 doctests failed
```

which is already reported at [sage-devel](http://groups.google.com/group/sage-devel/msg/4c7635baffe9b1f3). I then set the variable DOT_SAGE to a directory other than my home directory, loaded the newly compiled Sage, and started the notebook. As advertised, the RSA key generation process now uses openssl (which is available on mod.math). Using openssl, the key generation process is now much faster than previously (almost instantaneous). Before merging the updated dsage spkg, all outstanding changes need to be checked in. This is a positive review, provided that the check in issue is taken care of.



---

archive/issue_comments_067377.json:
```json
{
    "body": "> Before merging the updated dsage spkg, all outstanding changes need to \n> be checked in. This is a positive review, provided that the check in \n> issue is taken care of. \n\nDone.",
    "created_at": "2010-01-06T03:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7800#issuecomment-67377",
    "user": "https://github.com/williamstein"
}
```

> Before merging the updated dsage spkg, all outstanding changes need to 
> be checked in. This is a positive review, provided that the check in 
> issue is taken care of. 

Done.



---

archive/issue_comments_067378.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T07:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7800#issuecomment-67378",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_018679.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-14T07:17:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7800",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7800#event-18679"
}
```
