# Issue 3029: [with patch; positive review] Move DEB_AUTO_UPDATE_DEBIAN_CONTROL out of Debian packages

archive/issues_003029.json:
```json
{
    "body": "Assignee: @timabbott\n\nDebian doesn't allow you to upload packages that use DEB_AUTO_UPDATE_DEBIAN_CONTROL because it causes confusion with Non-Maintainer Uploads.  Since I'd like to get the packages so that they can be uploaded to Debian, we should remove it from our rules files.  Since it's fine for our purposes, I've modified sage-debsource to set DEB_AUTO_UPDATE_DEBIAN_CONTROL so that it always gets used when we are building packages.  I think it's probably easier for Michael to just make the changes than to merge N patches, so the following code will do the relevant update when the relevant spkgs are unpacked.\n\n```\nperl -i -0pe 's/^DEB_AUTO_UPDATE_DEBIAN_CONTROL = 1\\n//m' \n*/dist/debian/*/rules */dist/debian/rules\n```\n(if the patches are easier to deal with, let me know and I'll generate them)\nThe complete list of spkgs that require this treatment is as follows:\n\n* cddlib\n* eclib\n* extcode\n* flint\n* flintqs\n* gap\n* genus2reduction\n* gfan\n* givaro\n* iml\n* jmol\n* lcalc\n* libfplll\n* libm4ri\n* linbox\n* ntl\n* palp\n* polybori\n* rubiks\n* scipy_sandbox\n* singular\n* symmetrica\n* sympow\n* tachyon\n* zn_poly\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3029\n\n",
    "closed_at": "2008-04-27T07:19:49Z",
    "created_at": "2008-04-26T04:13:21Z",
    "labels": [
        "component: debian-package",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with patch; positive review] Move DEB_AUTO_UPDATE_DEBIAN_CONTROL out of Debian packages",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3029",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

Debian doesn't allow you to upload packages that use DEB_AUTO_UPDATE_DEBIAN_CONTROL because it causes confusion with Non-Maintainer Uploads.  Since I'd like to get the packages so that they can be uploaded to Debian, we should remove it from our rules files.  Since it's fine for our purposes, I've modified sage-debsource to set DEB_AUTO_UPDATE_DEBIAN_CONTROL so that it always gets used when we are building packages.  I think it's probably easier for Michael to just make the changes than to merge N patches, so the following code will do the relevant update when the relevant spkgs are unpacked.

```
perl -i -0pe 's/^DEB_AUTO_UPDATE_DEBIAN_CONTROL = 1\n//m' 
*/dist/debian/*/rules */dist/debian/rules
```
(if the patches are easier to deal with, let me know and I'll generate them)
The complete list of spkgs that require this treatment is as follows:

* cddlib
* eclib
* extcode
* flint
* flintqs
* gap
* genus2reduction
* gfan
* givaro
* iml
* jmol
* lcalc
* libfplll
* libm4ri
* linbox
* ntl
* palp
* polybori
* rubiks
* scipy_sandbox
* singular
* symmetrica
* sympow
* tachyon
* zn_poly


Issue created by migration from https://trac.sagemath.org/ticket/3029





---

archive/issue_comments_020786.json:
```json
{
    "body": "Attachment [auto-update-debian-control.patch](tarball://root/attachments/some-uuid/ticket3029/auto-update-debian-control.patch) by @timabbott created at 2008-04-26 04:13:28",
    "created_at": "2008-04-26T04:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20786",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-update-debian-control.patch](tarball://root/attachments/some-uuid/ticket3029/auto-update-debian-control.patch) by @timabbott created at 2008-04-26 04:13:28



---

archive/issue_comments_020787.json:
```json
{
    "body": "Hi Tim,\n\ndo I still need to run the perl script if I apply the patches? I would prefer to import 25 patches since then I do have a record. Since I will likely touch a lot of the spkgs in the next two days for cleanups I think it will be fine if you post those 25 patches and I just merge them as I go.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T04:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20787",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Tim,

do I still need to run the perl script if I apply the patches? I would prefer to import 25 patches since then I do have a record. Since I will likely touch a lot of the spkgs in the next two days for cleanups I think it will be fine if you post those 25 patches and I just merge them as I go.

Cheers,

Michael



---

archive/issue_comments_020788.json:
```json
{
    "body": "No, the perl script is what generates the patches that need to be done (there's also a single patch not done by the perl script that I've already uploaded).  I'll go ahead and post the 25 patches, then.",
    "created_at": "2008-04-26T04:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20788",
    "user": "https://github.com/timabbott"
}
```

No, the perl script is what generates the patches that need to be done (there's also a single patch not done by the perl script that I've already uploaded).  I'll go ahead and post the 25 patches, then.



---

archive/issue_comments_020789.json:
```json
{
    "body": "Attachment [auto-cddlib.patch](tarball://root/attachments/some-uuid/ticket3029/auto-cddlib.patch) by @timabbott created at 2008-04-26 05:01:41",
    "created_at": "2008-04-26T05:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20789",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-cddlib.patch](tarball://root/attachments/some-uuid/ticket3029/auto-cddlib.patch) by @timabbott created at 2008-04-26 05:01:41



---

archive/issue_comments_020790.json:
```json
{
    "body": "Attachment [auto-extcode.patch](tarball://root/attachments/some-uuid/ticket3029/auto-extcode.patch) by @timabbott created at 2008-04-26 05:01:50",
    "created_at": "2008-04-26T05:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20790",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-extcode.patch](tarball://root/attachments/some-uuid/ticket3029/auto-extcode.patch) by @timabbott created at 2008-04-26 05:01:50



---

archive/issue_comments_020791.json:
```json
{
    "body": "Attachment [auto-flint.patch](tarball://root/attachments/some-uuid/ticket3029/auto-flint.patch) by @timabbott created at 2008-04-26 05:01:57",
    "created_at": "2008-04-26T05:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20791",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-flint.patch](tarball://root/attachments/some-uuid/ticket3029/auto-flint.patch) by @timabbott created at 2008-04-26 05:01:57



---

archive/issue_comments_020792.json:
```json
{
    "body": "Attachment [auto-flintqs.patch](tarball://root/attachments/some-uuid/ticket3029/auto-flintqs.patch) by @timabbott created at 2008-04-26 05:02:04",
    "created_at": "2008-04-26T05:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20792",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-flintqs.patch](tarball://root/attachments/some-uuid/ticket3029/auto-flintqs.patch) by @timabbott created at 2008-04-26 05:02:04



---

archive/issue_comments_020793.json:
```json
{
    "body": "Attachment [auto-gfan.patch](tarball://root/attachments/some-uuid/ticket3029/auto-gfan.patch) by @timabbott created at 2008-04-26 05:02:11",
    "created_at": "2008-04-26T05:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20793",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-gfan.patch](tarball://root/attachments/some-uuid/ticket3029/auto-gfan.patch) by @timabbott created at 2008-04-26 05:02:11



---

archive/issue_comments_020794.json:
```json
{
    "body": "Attachment [auto-iml.patch](tarball://root/attachments/some-uuid/ticket3029/auto-iml.patch) by @timabbott created at 2008-04-26 05:02:31",
    "created_at": "2008-04-26T05:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20794",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-iml.patch](tarball://root/attachments/some-uuid/ticket3029/auto-iml.patch) by @timabbott created at 2008-04-26 05:02:31



---

archive/issue_comments_020795.json:
```json
{
    "body": "Attachment [auto-jmol.patch](tarball://root/attachments/some-uuid/ticket3029/auto-jmol.patch) by @timabbott created at 2008-04-26 05:02:40",
    "created_at": "2008-04-26T05:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20795",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-jmol.patch](tarball://root/attachments/some-uuid/ticket3029/auto-jmol.patch) by @timabbott created at 2008-04-26 05:02:40



---

archive/issue_comments_020796.json:
```json
{
    "body": "Attachment [auto-libfplll.patch](tarball://root/attachments/some-uuid/ticket3029/auto-libfplll.patch) by @timabbott created at 2008-04-26 05:02:49",
    "created_at": "2008-04-26T05:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20796",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-libfplll.patch](tarball://root/attachments/some-uuid/ticket3029/auto-libfplll.patch) by @timabbott created at 2008-04-26 05:02:49



---

archive/issue_comments_020797.json:
```json
{
    "body": "Attachment [auto-libm4ri.patch](tarball://root/attachments/some-uuid/ticket3029/auto-libm4ri.patch) by @timabbott created at 2008-04-26 05:02:59",
    "created_at": "2008-04-26T05:02:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20797",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-libm4ri.patch](tarball://root/attachments/some-uuid/ticket3029/auto-libm4ri.patch) by @timabbott created at 2008-04-26 05:02:59



---

archive/issue_comments_020798.json:
```json
{
    "body": "Attachment [auto-palp.patch](tarball://root/attachments/some-uuid/ticket3029/auto-palp.patch) by @timabbott created at 2008-04-26 05:03:20",
    "created_at": "2008-04-26T05:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20798",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-palp.patch](tarball://root/attachments/some-uuid/ticket3029/auto-palp.patch) by @timabbott created at 2008-04-26 05:03:20



---

archive/issue_comments_020799.json:
```json
{
    "body": "Attachment [auto-rubiks.patch](tarball://root/attachments/some-uuid/ticket3029/auto-rubiks.patch) by @timabbott created at 2008-04-26 05:03:28",
    "created_at": "2008-04-26T05:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20799",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-rubiks.patch](tarball://root/attachments/some-uuid/ticket3029/auto-rubiks.patch) by @timabbott created at 2008-04-26 05:03:28



---

archive/issue_comments_020800.json:
```json
{
    "body": "Attachment [auto-singular.patch](tarball://root/attachments/some-uuid/ticket3029/auto-singular.patch) by @timabbott created at 2008-04-26 05:03:42",
    "created_at": "2008-04-26T05:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20800",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-singular.patch](tarball://root/attachments/some-uuid/ticket3029/auto-singular.patch) by @timabbott created at 2008-04-26 05:03:42



---

archive/issue_comments_020801.json:
```json
{
    "body": "Attachment [auto-symmetr.patch](tarball://root/attachments/some-uuid/ticket3029/auto-symmetr.patch) by @timabbott created at 2008-04-26 05:04:06",
    "created_at": "2008-04-26T05:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20801",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-symmetr.patch](tarball://root/attachments/some-uuid/ticket3029/auto-symmetr.patch) by @timabbott created at 2008-04-26 05:04:06



---

archive/issue_comments_020802.json:
```json
{
    "body": "Attachment [auto-tachyon.patch](tarball://root/attachments/some-uuid/ticket3029/auto-tachyon.patch) by @timabbott created at 2008-04-26 05:04:14",
    "created_at": "2008-04-26T05:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20802",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-tachyon.patch](tarball://root/attachments/some-uuid/ticket3029/auto-tachyon.patch) by @timabbott created at 2008-04-26 05:04:14



---

archive/issue_comments_020803.json:
```json
{
    "body": "Attachment [auto-scipy_sandbox.patch](tarball://root/attachments/some-uuid/ticket3029/auto-scipy_sandbox.patch) by @timabbott created at 2008-04-26 05:05:38",
    "created_at": "2008-04-26T05:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20803",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-scipy_sandbox.patch](tarball://root/attachments/some-uuid/ticket3029/auto-scipy_sandbox.patch) by @timabbott created at 2008-04-26 05:05:38



---

archive/issue_comments_020804.json:
```json
{
    "body": "Attachment [auto-ntl.patch](tarball://root/attachments/some-uuid/ticket3029/auto-ntl.patch) by @timabbott created at 2008-04-26 05:11:11",
    "created_at": "2008-04-26T05:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20804",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-ntl.patch](tarball://root/attachments/some-uuid/ticket3029/auto-ntl.patch) by @timabbott created at 2008-04-26 05:11:11



---

archive/issue_comments_020805.json:
```json
{
    "body": "Attachment [auto-polybori.patch](tarball://root/attachments/some-uuid/ticket3029/auto-polybori.patch) by @timabbott created at 2008-04-26 05:12:08",
    "created_at": "2008-04-26T05:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20805",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-polybori.patch](tarball://root/attachments/some-uuid/ticket3029/auto-polybori.patch) by @timabbott created at 2008-04-26 05:12:08



---

archive/issue_comments_020806.json:
```json
{
    "body": "Attachment [auto-gap.patch](tarball://root/attachments/some-uuid/ticket3029/auto-gap.patch) by @timabbott created at 2008-04-26 05:12:39",
    "created_at": "2008-04-26T05:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20806",
    "user": "https://github.com/timabbott"
}
```

Attachment [auto-gap.patch](tarball://root/attachments/some-uuid/ticket3029/auto-gap.patch) by @timabbott created at 2008-04-26 05:12:39



---

archive/issue_comments_020807.json:
```json
{
    "body": "The patches look good to me. Most of them are really trivial, the two, three others are fine, too. I put them into the spkgs without bumping the patch level to avoid massive recompile on update.\n\nPlease, no more massive 25 spkg patch orgies ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-27T07:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20807",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patches look good to me. Most of them are really trivial, the two, three others are fine, too. I put them into the spkgs without bumping the patch level to avoid massive recompile on update.

Please, no more massive 25 spkg patch orgies ;)

Cheers,

Michael



---

archive/issue_comments_020808.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-04-27T07:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20808",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha1



---

archive/issue_comments_020809.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-27T07:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3029#issuecomment-20809",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006874.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-27T07:19:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3029",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3029#event-6874"
}
```
