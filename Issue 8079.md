# Issue 8079: Better documentation for patching spgk's

archive/issues_008079.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  mvngu\n\nIt would be great if the best-practices for patching sage packages were better (at all) documented. The following blog post should be definitely included into the developer manual:\n\nhttp://mvngu.wordpress.com/2010/01/20/how-to-patch-a-sage-package/\n\nIn addition, I'd like to know how to deal with updated configure scripts. Some issues are:\n* The automake sources (configure.ac, Makefile.am, more?) are small and their changes need to be recorded in case upstream makes a new release.\n* The automake sources might be automake-version dependent.\n* Not everyone has all versions of automake installed, so spkg-install can't call automake.\n* Running autoconf/automake generates big shell scripts (configure, makefile). Differences in these need not be recorded.   \n* But different versions of automake will produce different scripts, which would clutter up naive patches.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8079\n\n",
    "created_at": "2010-01-26T14:41:10Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "Better documentation for patching spgk's",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8079",
    "user": "vbraun"
}
```
Assignee: mvngu

CC:  mvngu

It would be great if the best-practices for patching sage packages were better (at all) documented. The following blog post should be definitely included into the developer manual:

http://mvngu.wordpress.com/2010/01/20/how-to-patch-a-sage-package/

In addition, I'd like to know how to deal with updated configure scripts. Some issues are:
* The automake sources (configure.ac, Makefile.am, more?) are small and their changes need to be recorded in case upstream makes a new release.
* The automake sources might be automake-version dependent.
* Not everyone has all versions of automake installed, so spkg-install can't call automake.
* Running autoconf/automake generates big shell scripts (configure, makefile). Differences in these need not be recorded.   
* But different versions of automake will produce different scripts, which would clutter up naive patches.

Issue created by migration from https://trac.sagemath.org/ticket/8079





---

archive/issue_comments_070804.json:
```json
{
    "body": "The attachment [trac_8079-patching-spkgs.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8079/trac_8079-patching-spkgs.patch) adds a chapter to the Developer's Guide, explaining how to patch an existing spkg. This attachment also solves the issues reported at #8104 and #3882. Once this ticket is closed, tickets #8104 and #3882 can also be closed as fixed.",
    "created_at": "2010-02-09T12:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8079#issuecomment-70804",
    "user": "mvngu"
}
```

The attachment [trac_8079-patching-spkgs.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8079/trac_8079-patching-spkgs.patch) adds a chapter to the Developer's Guide, explaining how to patch an existing spkg. This attachment also solves the issues reported at #8104 and #3882. Once this ticket is closed, tickets #8104 and #3882 can also be closed as fixed.



---

archive/issue_comments_070805.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-09T12:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8079#issuecomment-70805",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070806.json:
```json
{
    "body": "Attachment [trac_8079-patching-spkgs.patch](tarball://root/attachments/some-uuid/ticket8079/trac_8079-patching-spkgs.patch) by mvngu created at 2010-02-10 05:23:28\n\nbased on Sage 4.3.2; depends on #8199",
    "created_at": "2010-02-10T05:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8079#issuecomment-70806",
    "user": "mvngu"
}
```

Attachment [trac_8079-patching-spkgs.patch](tarball://root/attachments/some-uuid/ticket8079/trac_8079-patching-spkgs.patch) by mvngu created at 2010-02-10 05:23:28

based on Sage 4.3.2; depends on #8199



---

archive/issue_comments_070807.json:
```json
{
    "body": "Applied patches from tickets #8079, #8199, #7944. Both html and pdf developer manuals built without error. Have little experience with the material but FWIW, it reads very clearly and will be valued by new developers (+1 for positive review)",
    "created_at": "2010-02-11T06:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8079#issuecomment-70807",
    "user": "rossk"
}
```

Applied patches from tickets #8079, #8199, #7944. Both html and pdf developer manuals built without error. Have little experience with the material but FWIW, it reads very clearly and will be valued by new developers (+1 for positive review)



---

archive/issue_comments_070808.json:
```json
{
    "body": "Overall this looks nice and would have been very helpful to me when first trying spkgs (and still is helpful!).  I don't on a first reading see an explicit reference to the first patched version being .p0 (computer science/Python/Sage numbering) as opposed to .p1 (math numbering), though there is one implicit reference to this.",
    "created_at": "2010-02-12T02:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8079#issuecomment-70808",
    "user": "kcrisman"
}
```

Overall this looks nice and would have been very helpful to me when first trying spkgs (and still is helpful!).  I don't on a first reading see an explicit reference to the first patched version being .p0 (computer science/Python/Sage numbering) as opposed to .p1 (math numbering), though there is one implicit reference to this.



---

archive/issue_comments_070809.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-12T09:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8079#issuecomment-70809",
    "user": "rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070810.json:
```json
{
    "body": "Changing keywords from \"\" to \"Developer's Guide patching spkg\".",
    "created_at": "2010-02-12T09:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8079#issuecomment-70810",
    "user": "rossk"
}
```

Changing keywords from "" to "Developer's Guide patching spkg".



---

archive/issue_comments_070811.json:
```json
{
    "body": "Feel free to open another ticket for the remaining issues in the ticket description.",
    "created_at": "2010-02-14T14:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8079#issuecomment-70811",
    "user": "mvngu"
}
```

Feel free to open another ticket for the remaining issues in the ticket description.



---

archive/issue_comments_070812.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-14T14:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8079#issuecomment-70812",
    "user": "mvngu"
}
```

Resolution: fixed
