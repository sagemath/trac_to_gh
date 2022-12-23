# Issue 3029: [with patch; needs review] Move DEB_AUTO_UPDATE_DEBIAN_CONTROL out of Debian packages

archive/issues_003029.json:
```json
{
    "body": "Assignee: tabbott\n\nDebian doesn't allow you to upload packages that use DEB_AUTO_UPDATE_DEBIAN_CONTROL because it causes confusion with Non-Maintainer Uploads.  Since I'd like to get the packages so that they can be uploaded to Debian, we should remove it from our rules files.  Since it's fine for our purposes, I've modified sage-debsource to set DEB_AUTO_UPDATE_DEBIAN_CONTROL so that it always gets used when we are building packages.  I think it's probably easier for Michael to just make the changes than to merge N patches, so the following code will do the relevant update when the relevant spkgs are unpacked.\n\nperl -i -0pe 's/^DEB_AUTO_UPDATE_DEBIAN_CONTROL = 1\\n//m' */dist/debian/*/rules */dist/debian/rules\n\n(if the patches are easier to deal with, let me know and I'll generate them)\nThe complete list of spkgs that require this treatment is as follows:\n\ncddlib\neclib\nextcode\nflint\nflintqs\ngap\ngenus2reduction\ngfan\ngivaro\niml\njmol\nlcalc\nlibfplll\nlibm4ri\nlinbox\nntl\npalp\npolybori\nrubiks\nscipy_sandbox\nsingular\nsymmetrica\nsympow\ntachyon\nzn_poly\n\nIssue created by migration from https://trac.sagemath.org/ticket/3029\n\n",
    "created_at": "2008-04-26T04:13:21Z",
    "labels": [
        "debian-package",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] Move DEB_AUTO_UPDATE_DEBIAN_CONTROL out of Debian packages",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3029",
    "user": "tabbott"
}
```
Assignee: tabbott

Debian doesn't allow you to upload packages that use DEB_AUTO_UPDATE_DEBIAN_CONTROL because it causes confusion with Non-Maintainer Uploads.  Since I'd like to get the packages so that they can be uploaded to Debian, we should remove it from our rules files.  Since it's fine for our purposes, I've modified sage-debsource to set DEB_AUTO_UPDATE_DEBIAN_CONTROL so that it always gets used when we are building packages.  I think it's probably easier for Michael to just make the changes than to merge N patches, so the following code will do the relevant update when the relevant spkgs are unpacked.

perl -i -0pe 's/^DEB_AUTO_UPDATE_DEBIAN_CONTROL = 1\n//m' */dist/debian/*/rules */dist/debian/rules

(if the patches are easier to deal with, let me know and I'll generate them)
The complete list of spkgs that require this treatment is as follows:

cddlib
eclib
extcode
flint
flintqs
gap
genus2reduction
gfan
givaro
iml
jmol
lcalc
libfplll
libm4ri
linbox
ntl
palp
polybori
rubiks
scipy_sandbox
singular
symmetrica
sympow
tachyon
zn_poly

Issue created by migration from https://trac.sagemath.org/ticket/3029





---

archive/issue_comments_020829.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T04:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20829",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020830.json:
```json
{
    "body": "Hi Tim,\n\ndo I still need to run the perl script if I apply the patches? I would prefer to import 25 patches since then I do have a record. Since I will likely touch a lot of the spkgs in the next two days for cleanups I think it will be fine if you post those 25 patches and I just merge them as I go.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T04:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20830",
    "user": "mabshoff"
}
```

Hi Tim,

do I still need to run the perl script if I apply the patches? I would prefer to import 25 patches since then I do have a record. Since I will likely touch a lot of the spkgs in the next two days for cleanups I think it will be fine if you post those 25 patches and I just merge them as I go.

Cheers,

Michael



---

archive/issue_comments_020831.json:
```json
{
    "body": "No, the perl script is what generates the patches that need to be done (there's also a single patch not done by the perl script that I've already uploaded).  I'll go ahead and post the 25 patches, then.",
    "created_at": "2008-04-26T04:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20831",
    "user": "tabbott"
}
```

No, the perl script is what generates the patches that need to be done (there's also a single patch not done by the perl script that I've already uploaded).  I'll go ahead and post the 25 patches, then.



---

archive/issue_comments_020832.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20832",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020833.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20833",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020834.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20834",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020835.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20835",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020836.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20836",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020837.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20837",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020838.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20838",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020839.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20839",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020840.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:02:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20840",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020841.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20841",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020842.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20842",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020843.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20843",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020844.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20844",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020845.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20845",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020846.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20846",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020847.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20847",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020848.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20848",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020849.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T05:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20849",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020850.json:
```json
{
    "body": "The patches look good to me. Most of them are really trivial, the two, three others are fine, too. I put them into the spkgs without bumping the patch level to avoid massive recompile on update.\n\nPlease, no more massive 25 spkg patch orgies ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-27T07:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20850",
    "user": "mabshoff"
}
```

The patches look good to me. Most of them are really trivial, the two, three others are fine, too. I put them into the spkgs without bumping the patch level to avoid massive recompile on update.

Please, no more massive 25 spkg patch orgies ;)

Cheers,

Michael



---

archive/issue_comments_020851.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-04-27T07:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20851",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha1



---

archive/issue_comments_020852.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-27T07:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20852",
    "user": "mabshoff"
}
```

Resolution: fixed
