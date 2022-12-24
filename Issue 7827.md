# Issue 7827: Fix atlas-3.8.3.p9 compilation on FreeBSD

archive/issues_007827.json:
```json
{
    "body": "Assignee: pjeremy\n\nCC:  drkirby was\n\n* FreeBSD uses an '_fbsd' suffix on the ELF format supported by ld - prevents ld: unrecognised emulation mode: elf_x86_64 error during atlas build. Reported upstream as https://sourceforge.net/tracker/index.php?func=detail&aid=2728930&group_id=23725&atid=379482\n\n* Treat shared libraries the same as Linux - otherwise they aren't correctly detected by (eg) numpy. (sage-specific) \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7827\n\n",
    "created_at": "2010-01-03T04:15:58Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "title": "Fix atlas-3.8.3.p9 compilation on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7827",
    "user": "pjeremy"
}
```
Assignee: pjeremy

CC:  drkirby was

* FreeBSD uses an '_fbsd' suffix on the ELF format supported by ld - prevents ld: unrecognised emulation mode: elf_x86_64 error during atlas build. Reported upstream as https://sourceforge.net/tracker/index.php?func=detail&aid=2728930&group_id=23725&atid=379482

* Treat shared libraries the same as Linux - otherwise they aren't correctly detected by (eg) numpy. (sage-specific) 


Issue created by migration from https://trac.sagemath.org/ticket/7827





---

archive/issue_comments_067755.json:
```json
{
    "body": "Attachment [7827.atlas.patch](tarball://root/attachments/some-uuid/ticket7827/7827.atlas.patch) by pjeremy created at 2010-01-03 04:18:09",
    "created_at": "2010-01-03T04:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67755",
    "user": "pjeremy"
}
```

Attachment [7827.atlas.patch](tarball://root/attachments/some-uuid/ticket7827/7827.atlas.patch) by pjeremy created at 2010-01-03 04:18:09



---

archive/issue_comments_067756.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T04:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67756",
    "user": "pjeremy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067757.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-12T17:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67757",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067758.json:
```json
{
    "body": "I'm personally unable to verify this works on FreeBSD, but I can certainly see the changes will have no effect on any platform other than FreeBSD. So its a positive from me.",
    "created_at": "2010-01-12T17:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67758",
    "user": "drkirkby"
}
```

I'm personally unable to verify this works on FreeBSD, but I can certainly see the changes will have no effect on any platform other than FreeBSD. So its a positive from me.



---

archive/issue_comments_067759.json:
```json
{
    "body": "pjeremy -- There are repositories in the directories themselves, and the best way to post a modification to an spkg is to check in the changes to the mercurial repo, and `sage -pkg` it up, posting a link to a whole spkg on the ticket. This ticket in particular won't work as is, because #7838 updated from `p9` to `p10`.",
    "created_at": "2010-01-14T06:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67759",
    "user": "rlm"
}
```

pjeremy -- There are repositories in the directories themselves, and the best way to post a modification to an spkg is to check in the changes to the mercurial repo, and `sage -pkg` it up, posting a link to a whole spkg on the ticket. This ticket in particular won't work as is, because #7838 updated from `p9` to `p10`.



---

archive/issue_comments_067760.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-24T16:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67760",
    "user": "mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_067761.json:
```json
{
    "body": "An updated spkg is available at\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/atlas/atlas-3.8.3.p11.spkg\n\nI committed the patch [7827.atlas.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7827/7827.atlas.patch) in pjeremy's name. The patched version of `SpewMakeInc.c` is available under `patches/`. I also patched the installation script `spkg-install-script` to copy pjeremy's patched `patches/SpewMakeInc.c` over to `src/CONFIG/src/SpewMakeInc.c`. The relevant modification is:\n\n```\ndiff -r cffdd7ee34e2 spkg-install-script\n--- a/spkg-install-script\n+++ b/spkg-install-script\n@@ -120,6 +120,10 @@\n \n CUR=`pwd`\n echo $CUR\n+if [ `uname` = \"FreeBSD\" ]; then\n+    echo Patching SpewMakeInc.c for FreeBSD-specific build\n+    cp patches/SpewMakeInc.c src/CONFIG/src/SpewMakeInc.c\n+fi\n # add PPC4 7447 CPU and better Itanium2 detection:\n echo Deal with PPC4 7447 model and Itanium 2\n cp patches/archinfo_linux.c src/CONFIG/src/backend/archinfo_linux.c\n```\n\nThe updated spkg needs another pair of eyes (anyone's, other than mine) to comb through it. If my change to `spkg-install-script` gets the green light, then the updated spkg can be merged.",
    "created_at": "2010-01-24T16:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67761",
    "user": "mvngu"
}
```

An updated spkg is available at

http://sage.math.washington.edu/home/mvngu/spkg/standard/atlas/atlas-3.8.3.p11.spkg

I committed the patch [7827.atlas.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7827/7827.atlas.patch) in pjeremy's name. The patched version of `SpewMakeInc.c` is available under `patches/`. I also patched the installation script `spkg-install-script` to copy pjeremy's patched `patches/SpewMakeInc.c` over to `src/CONFIG/src/SpewMakeInc.c`. The relevant modification is:

```
diff -r cffdd7ee34e2 spkg-install-script
--- a/spkg-install-script
+++ b/spkg-install-script
@@ -120,6 +120,10 @@
 
 CUR=`pwd`
 echo $CUR
+if [ `uname` = "FreeBSD" ]; then
+    echo Patching SpewMakeInc.c for FreeBSD-specific build
+    cp patches/SpewMakeInc.c src/CONFIG/src/SpewMakeInc.c
+fi
 # add PPC4 7447 CPU and better Itanium2 detection:
 echo Deal with PPC4 7447 model and Itanium 2
 cp patches/archinfo_linux.c src/CONFIG/src/backend/archinfo_linux.c
```

The updated spkg needs another pair of eyes (anyone's, other than mine) to comb through it. If my change to `spkg-install-script` gets the green light, then the updated spkg can be merged.



---

archive/issue_comments_067762.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-24T16:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67762",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067763.json:
```json
{
    "body": "This looks good. Note there are also some patches to #8039 which needs work, but I suspect will make it into 4.3.2. \n\nDave",
    "created_at": "2010-01-27T02:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67763",
    "user": "drkirkby"
}
```

This looks good. Note there are also some patches to #8039 which needs work, but I suspect will make it into 4.3.2. 

Dave



---

archive/issue_comments_067764.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-27T02:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67764",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067765.json:
```json
{
    "body": "Merged [atlas-3.8.3.p11.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/atlas/atlas-3.8.3.p11.spkg) in the standard spkg repository.",
    "created_at": "2010-02-01T00:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67765",
    "user": "mvngu"
}
```

Merged [atlas-3.8.3.p11.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/atlas/atlas-3.8.3.p11.spkg) in the standard spkg repository.



---

archive/issue_comments_067766.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-01T00:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7827#issuecomment-67766",
    "user": "mvngu"
}
```

Resolution: fixed
