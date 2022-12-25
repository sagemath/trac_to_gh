# Issue 9609: Remove unnecessary files from spkg/standard

archive/issues_009609.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @dandrake\n\n[Dan Drake wrote on sage-release](https://groups.google.com/group/sage-release/browse_thread/thread/b6fd67d4d4543129/9e68e7105e23ab29#9e68e7105e23ab29):\n\n```\nIn SAGE_ROOT/spkg/standard, with 4.5.alpha0, I see:\n\n$ ls | grep -v spkg\ntotal 303320\n-rw-r--r-- 1 drake drake       43 Jun 28 09:36 README.txt\n-rw-r--r-- 1 drake drake    18614 Jul 25 20:52 deps\n-rw-r--r-- 1 drake drake      163 Jun 28 09:36 libdist_filelist\n-rwxr-xr-x 1 drake drake     1571 Jun 28 09:36 newest_version*\n-rw-r--r-- 1 drake drake      977 Jun 28 09:36 notes.txt\n-rw-r--r-- 1 drake drake      383 Jun 28 09:36 numeric-24.2.txt\n\nThe files libdist_filelist, notes.txt, and numeric-24.2.txt seem like leftover notes that. Can I delete them? \n```\n\n\nThe files `libdist_filelist`, `notes.txt`, and `numeric-24.2.txt` [have been removed from Sage 4.5.2.alpha1](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692):\n\n```\nThe second unreviewed change is the deletion of several extra files in spkg/standard, as I mentioned in https://groups.google.com/group/sage-release/t/b6fd67d4d4543129. In the unlikely case that those files were important or necessary, we can just copy them from the alpha0 tarball. \n```\n\n\nThis ticket is for reviewing the change.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9609\n\n",
    "created_at": "2010-07-27T07:28:42Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Remove unnecessary files from spkg/standard",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9609",
    "user": "https://github.com/qed777"
}
```
Assignee: GeorgSWeber

CC:  @dandrake

[Dan Drake wrote on sage-release](https://groups.google.com/group/sage-release/browse_thread/thread/b6fd67d4d4543129/9e68e7105e23ab29#9e68e7105e23ab29):

```
In SAGE_ROOT/spkg/standard, with 4.5.alpha0, I see:

$ ls | grep -v spkg
total 303320
-rw-r--r-- 1 drake drake       43 Jun 28 09:36 README.txt
-rw-r--r-- 1 drake drake    18614 Jul 25 20:52 deps
-rw-r--r-- 1 drake drake      163 Jun 28 09:36 libdist_filelist
-rwxr-xr-x 1 drake drake     1571 Jun 28 09:36 newest_version*
-rw-r--r-- 1 drake drake      977 Jun 28 09:36 notes.txt
-rw-r--r-- 1 drake drake      383 Jun 28 09:36 numeric-24.2.txt

The files libdist_filelist, notes.txt, and numeric-24.2.txt seem like leftover notes that. Can I delete them? 
```


The files `libdist_filelist`, `notes.txt`, and `numeric-24.2.txt` [have been removed from Sage 4.5.2.alpha1](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692):

```
The second unreviewed change is the deletion of several extra files in spkg/standard, as I mentioned in https://groups.google.com/group/sage-release/t/b6fd67d4d4543129. In the unlikely case that those files were important or necessary, we can just copy them from the alpha0 tarball. 
```


This ticket is for reviewing the change.

Issue created by migration from https://trac.sagemath.org/ticket/9609





---

archive/issue_comments_092926.json:
```json
{
    "body": "Possibly related:\n\n```sh\n$ cd SAGE_LOCAL/bin\n$ grep libdist *\nsage-libdist:libdist_filelist = open('%s/spkg/standard/libdist_filelist'%r\nsage-libdist:    if len(ext) > 1 and not name_without_version in libdist_filelist:\nsage-libdist:This is the readme for sage-libdist, which is the\nsage-libdist:libdist = 'sage-libdist%s'%r[i:]\nsage-libdist:if os.path.exists(libdist):\nsage-libdist:    os.system('rm -rf %s'%libdist)\nsage-libdist:os.system('mv %s %s'%(r,libdist))\nsage-libdist:os.system('tar -cvf %s.tar %s'%(libdist,libdist))\nsage-libdist:os.system('rm -rf %s'%libdist)\nsage-sage:   \"$SAGE_ROOT\"/local/bin/sage-libdist sage-$2.tar\nsage-sdist:cp -p $PKGDIR/$STD/libdist_filelist $TMP/$PKGDIR/$STD/\n```\n\nBut I can't investigate further right now.",
    "created_at": "2010-07-27T08:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9609#issuecomment-92926",
    "user": "https://github.com/qed777"
}
```

Possibly related:

```sh
$ cd SAGE_LOCAL/bin
$ grep libdist *
sage-libdist:libdist_filelist = open('%s/spkg/standard/libdist_filelist'%r
sage-libdist:    if len(ext) > 1 and not name_without_version in libdist_filelist:
sage-libdist:This is the readme for sage-libdist, which is the
sage-libdist:libdist = 'sage-libdist%s'%r[i:]
sage-libdist:if os.path.exists(libdist):
sage-libdist:    os.system('rm -rf %s'%libdist)
sage-libdist:os.system('mv %s %s'%(r,libdist))
sage-libdist:os.system('tar -cvf %s.tar %s'%(libdist,libdist))
sage-libdist:os.system('rm -rf %s'%libdist)
sage-sage:   "$SAGE_ROOT"/local/bin/sage-libdist sage-$2.tar
sage-sdist:cp -p $PKGDIR/$STD/libdist_filelist $TMP/$PKGDIR/$STD/
```

But I can't investigate further right now.



---

archive/issue_comments_092927.json:
```json
{
    "body": "As part of the file \"sage-sage\":\n\n```\n   echo \"sage -ldist currently disabled\"\n   echo \"To work on it, remove the exit after this message in SAGE_ROOT/local/bin/sage-sage\"\n```\n\nSo sage-libdist is not currently active.  I think that we should keep the file libdist_filelist just in case.  In my opinion, the other two files can be removed, but I don't know their history.  You might ping William about this.",
    "created_at": "2010-07-27T15:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9609#issuecomment-92927",
    "user": "https://github.com/jhpalmieri"
}
```

As part of the file "sage-sage":

```
   echo "sage -ldist currently disabled"
   echo "To work on it, remove the exit after this message in SAGE_ROOT/local/bin/sage-sage"
```

So sage-libdist is not currently active.  I think that we should keep the file libdist_filelist just in case.  In my opinion, the other two files can be removed, but I don't know their history.  You might ping William about this.



---

archive/issue_comments_092928.json:
```json
{
    "body": "Also, as mpatel points out: the script sage-sdist tries to copy libdist_filelist, so that may break with this file missing.",
    "created_at": "2010-07-27T15:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9609#issuecomment-92928",
    "user": "https://github.com/jhpalmieri"
}
```

Also, as mpatel points out: the script sage-sdist tries to copy libdist_filelist, so that may break with this file missing.



---

archive/issue_comments_092929.json:
```json
{
    "body": "Okay, it looks like we should put libdist_filelist back in (and then, in my opinion, find out why it's there and if possible, open a ticket for removing it and the parts of the scripts that reference it).\n\nThe numeric-24.2.txt is a short description of a Python module that we don't ship. Even if we did include it, I can see no reason why such a file should be kept in spkg/standard.\n\nnotes.txt refers to the sage_c_lib package, which no longer exists, and to a very outdated version of linbox. The libtool information in that file should be kept in the linbox spkg and/or put on the wiki.\n\nI think we can resolve this ticket by just putting libdist_filelist back.",
    "created_at": "2010-07-28T01:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9609#issuecomment-92929",
    "user": "https://github.com/dandrake"
}
```

Okay, it looks like we should put libdist_filelist back in (and then, in my opinion, find out why it's there and if possible, open a ticket for removing it and the parts of the scripts that reference it).

The numeric-24.2.txt is a short description of a Python module that we don't ship. Even if we did include it, I can see no reason why such a file should be kept in spkg/standard.

notes.txt refers to the sage_c_lib package, which no longer exists, and to a very outdated version of linbox. The libtool information in that file should be kept in the linbox spkg and/or put on the wiki.

I think we can resolve this ticket by just putting libdist_filelist back.



---

archive/issue_comments_092930.json:
```json
{
    "body": "Sounds good to me.  We can always recover the other files from an old tarball if we ever need them.",
    "created_at": "2010-07-28T02:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9609#issuecomment-92930",
    "user": "https://github.com/jhpalmieri"
}
```

Sounds good to me.  We can always recover the other files from an old tarball if we ever need them.



---

archive/issue_comments_092931.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T02:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9609#issuecomment-92931",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092932.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-28T02:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9609#issuecomment-92932",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092933.json:
```json
{
    "body": "I'm including 4.5.2.alpha0's `spkg/standard/libdist_filelist` in 4.5.2.rc0.",
    "created_at": "2010-07-29T04:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9609#issuecomment-92933",
    "user": "https://github.com/qed777"
}
```

I'm including 4.5.2.alpha0's `spkg/standard/libdist_filelist` in 4.5.2.rc0.



---

archive/issue_events_009752.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-07-29T04:53:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9609",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9609#event-9752"
}
```



---

archive/issue_comments_092934.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-29T04:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9609#issuecomment-92934",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
