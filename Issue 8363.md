# Issue 8363: cddlib-094f.p4 has a useless check for mpir which breaks on Solaris

archive/issues_008363.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies\n\nspkg/install/deps shows that cddlib depends on mpir\n\n\n```\n$(INST)/$(CDDLIB): $(BASE) $(INST)/$(MPIR)\n        $(SAGE_SPKG) $(CDDLIB) 2>&1\n```\n\n\nbut for some reason someone has added a check in cddlib's spkg-install. This seems a bit pointless, but is causing a breakage on Solaris\n\n\n```\n# We depend on mpir, make sure it is installed (GMP fork)\nMPIR_VERSION=`cd $SAGE_ROOT/spkg/standard/; ./newest_version mpir`\nif [ $? -ne 0 ]; then\n    echo \"Failed to find mpir.  Please install the mpir spkg\"\n    exit 1\nfi\n```\n\n\nThey do not even export MPIR_VERSION, so it is a useless bit of code that is breaking on Solaris. \n\nAlso, currently cddlib will not build on 64-bit Solaris, due to the normal check that the platform is OS X: \n\n\n```\nif [ `uname` = \"Darwin\" ] && [ \"$SAGE64\" = \"yes\" ]; then\n   echo \"64 bit MacIntel\"\n   CFLAGS=\"$CFLAGS -m64 \"; export CFLAGS\nfi\n```\n\n\nBoth these issues are easily resolved. A patch and updated .spkg will follow shortly. \n\nDave \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8363\n\n",
    "created_at": "2010-02-25T15:31:56Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "cddlib-094f.p4 has a useless check for mpir which breaks on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8363",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies

spkg/install/deps shows that cddlib depends on mpir


```
$(INST)/$(CDDLIB): $(BASE) $(INST)/$(MPIR)
        $(SAGE_SPKG) $(CDDLIB) 2>&1
```


but for some reason someone has added a check in cddlib's spkg-install. This seems a bit pointless, but is causing a breakage on Solaris


```
# We depend on mpir, make sure it is installed (GMP fork)
MPIR_VERSION=`cd $SAGE_ROOT/spkg/standard/; ./newest_version mpir`
if [ $? -ne 0 ]; then
    echo "Failed to find mpir.  Please install the mpir spkg"
    exit 1
fi
```


They do not even export MPIR_VERSION, so it is a useless bit of code that is breaking on Solaris. 

Also, currently cddlib will not build on 64-bit Solaris, due to the normal check that the platform is OS X: 


```
if [ `uname` = "Darwin" ] && [ "$SAGE64" = "yes" ]; then
   echo "64 bit MacIntel"
   CFLAGS="$CFLAGS -m64 "; export CFLAGS
fi
```


Both these issues are easily resolved. A patch and updated .spkg will follow shortly. 

Dave 



Issue created by migration from https://trac.sagemath.org/ticket/8363





---

archive/issue_comments_074601.json:
```json
{
    "body": "Attachment [cddlib-094f.p5.patch](tarball://root/attachments/some-uuid/ticket8363/cddlib-094f.p5.patch) by drkirkby created at 2010-02-25 16:33:13\n\nMercurial patch",
    "created_at": "2010-02-25T16:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74601",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [cddlib-094f.p5.patch](tarball://root/attachments/some-uuid/ticket8363/cddlib-094f.p5.patch) by drkirkby created at 2010-02-25 16:33:13

Mercurial patch



---

archive/issue_comments_074602.json:
```json
{
    "body": "Updated package with changes to allow to work fully on Solaris.",
    "created_at": "2010-02-25T16:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74602",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Updated package with changes to allow to work fully on Solaris.



---

archive/issue_comments_074603.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-25T16:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74603",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074604.json:
```json
{
    "body": "Attachment [cddlib-094f.p5.spkg](tarball://root/attachments/some-uuid/ticket8363/cddlib-094f.p5.spkg) by drkirkby created at 2010-02-25 16:35:11",
    "created_at": "2010-02-25T16:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74604",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [cddlib-094f.p5.spkg](tarball://root/attachments/some-uuid/ticket8363/cddlib-094f.p5.spkg) by drkirkby created at 2010-02-25 16:35:11



---

archive/issue_comments_074605.json:
```json
{
    "body": "Please put a link to the spkg in the ticket. An attachment does not work.\n\nJaap",
    "created_at": "2010-02-25T17:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74605",
    "user": "https://github.com/jaapspies"
}
```

Please put a link to the spkg in the ticket. An attachment does not work.

Jaap



---

archive/issue_comments_074606.json:
```json
{
    "body": "On hawk:\n\n\n```\nld: fatal: file /usr/local/lib/libgmp.so: wrong ELF class: ELFCLASS32\nld: fatal: file processing errors. No output written to .libs/scdd_gmp\ncollect2: ld returned 1 exit status\nmake[1]: *** [scdd_gmp] Error 1\nmake[1]: Leaving directory `/export/home/jaap/sage_port/sage-4.3.2.alpha1/spkg/build/cddlib-094f.p5/src/src-gmp'\nmake: *** [all-recursive] Error 1\nError building cddlib\n\n\n```\n\nIn my VirtualBox:\n\n```\nlibtool: link: gcc -m64 -o .libs/scdd_gmp simplecdd.o  -L/usr/local/lib -L/export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib ../lib-src-gmp/.libs/libcddgmp.so /export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib/libgmp.so /usr/local/lib/libgmp.so -R/export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib -R/usr/local/lib\nld: fatal: recording name conflict: file `/export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib/libgmp.so' and file `/usr/local/lib/libgmp.so' provide identical dependency names: libgmp.so.3  (possible multiple inclusion of the same file)\nld: fatal: file processing errors. No output written to .libs/scdd_gmp\ncollect2: ld returned 1 exit status\nmake[1]: *** [scdd_gmp] Error 1\nmake[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.3.alpha1/spkg/build/cddlib-094f.p5/src/src-gmp'\nmake: *** [all-recursive] Error 1\nError building cddlib\n\n\n```\n\n\nSo I think this ticket needs work.\n\nJaap",
    "created_at": "2010-02-25T17:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74606",
    "user": "https://github.com/jaapspies"
}
```

On hawk:


```
ld: fatal: file /usr/local/lib/libgmp.so: wrong ELF class: ELFCLASS32
ld: fatal: file processing errors. No output written to .libs/scdd_gmp
collect2: ld returned 1 exit status
make[1]: *** [scdd_gmp] Error 1
make[1]: Leaving directory `/export/home/jaap/sage_port/sage-4.3.2.alpha1/spkg/build/cddlib-094f.p5/src/src-gmp'
make: *** [all-recursive] Error 1
Error building cddlib


```

In my VirtualBox:

```
libtool: link: gcc -m64 -o .libs/scdd_gmp simplecdd.o  -L/usr/local/lib -L/export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib ../lib-src-gmp/.libs/libcddgmp.so /export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib/libgmp.so /usr/local/lib/libgmp.so -R/export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib -R/usr/local/lib
ld: fatal: recording name conflict: file `/export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib/libgmp.so' and file `/usr/local/lib/libgmp.so' provide identical dependency names: libgmp.so.3  (possible multiple inclusion of the same file)
ld: fatal: file processing errors. No output written to .libs/scdd_gmp
collect2: ld returned 1 exit status
make[1]: *** [scdd_gmp] Error 1
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.3.alpha1/spkg/build/cddlib-094f.p5/src/src-gmp'
make: *** [all-recursive] Error 1
Error building cddlib


```


So I think this ticket needs work.

Jaap



---

archive/issue_comments_074607.json:
```json
{
    "body": "Em, looks like multiple inclusion of the same libraries. I'm not sure how to solve this. I'll take a look - perhaps there is a configure option to select what library gets linked. \n\ndave",
    "created_at": "2010-02-25T22:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74607",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Em, looks like multiple inclusion of the same libraries. I'm not sure how to solve this. I'll take a look - perhaps there is a configure option to select what library gets linked. 

dave



---

archive/issue_comments_074608.json:
```json
{
    "body": "Thinking about this ticket, it does fix what the title says it does. In other words, it removes the useless but broken check for mpir. \n\nI don't believe the removal of the OS X restriction for a 64-bit build can do any harm and its failure to work probably has more to do with the multiple inclusion of libraries. \n\nAs such, I believe this should get a positive review. \n\nThe fact it does not build on OpenSolaris is another issue. \n\nDave",
    "created_at": "2010-02-26T01:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74608",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thinking about this ticket, it does fix what the title says it does. In other words, it removes the useless but broken check for mpir. 

I don't believe the removal of the OS X restriction for a 64-bit build can do any harm and its failure to work probably has more to do with the multiple inclusion of libraries. 

As such, I believe this should get a positive review. 

The fact it does not build on OpenSolaris is another issue. 

Dave



---

archive/issue_comments_074609.json:
```json
{
    "body": "Packages should not be attached to tickets. Instead, provide a URL to the spkg. David's updated spkg is available at\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/cddlib/cddlib-094f.p5.spkg",
    "created_at": "2010-03-01T02:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74609",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Packages should not be attached to tickets. Instead, provide a URL to the spkg. David's updated spkg is available at

http://sage.math.washington.edu/home/mvngu/spkg/standard/cddlib/cddlib-094f.p5.spkg



---

archive/issue_comments_074610.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-03-01T16:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74610",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_074611.json:
```json
{
    "body": "Updating to blocker, as this is essential for a successful Solaris build, which with care should build and pass all doc tests.",
    "created_at": "2010-03-01T16:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74611",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Updating to blocker, as this is essential for a successful Solaris build, which with care should build and pass all doc tests.



---

archive/issue_comments_074612.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-02T13:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74612",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074613.json:
```json
{
    "body": "I'm happy with the changes in `cddlib-094f.p5.spkg`.",
    "created_at": "2010-03-02T13:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74613",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I'm happy with the changes in `cddlib-094f.p5.spkg`.



---

archive/issue_comments_074614.json:
```json
{
    "body": "Thank you Minh. I don't know what I was thinking when I attached the package to the trac ticket. Perhaps I thought it was so small - not sure. Anyway, I will not do it again. \n\nThank you for the positive review. \n\nI've opened another ticket, #8419, to resolve the issue which Jaap found - i.e. cddlib is not building as 64-bit on OpenSolaris.",
    "created_at": "2010-03-02T14:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74614",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thank you Minh. I don't know what I was thinking when I attached the package to the trac ticket. Perhaps I thought it was so small - not sure. Anyway, I will not do it again. 

Thank you for the positive review. 

I've opened another ticket, #8419, to resolve the issue which Jaap found - i.e. cddlib is not building as 64-bit on OpenSolaris.



---

archive/issue_events_020042.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T23:35:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8363#event-20042"
}
```



---

archive/issue_comments_074615.json:
```json
{
    "body": "Merged [cddlib-094f.p5.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/cddlib/cddlib-094f.p5.spkg) in the standard spkg repository.",
    "created_at": "2010-03-02T23:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74615",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [cddlib-094f.p5.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/cddlib/cddlib-094f.p5.spkg) in the standard spkg repository.



---

archive/issue_comments_074616.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T23:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8363#issuecomment-74616",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
