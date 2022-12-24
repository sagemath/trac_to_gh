# Issue 1589: jmol -- using via https is a pain in the butt

archive/issues_001589.json:
```json
{
    "body": "Assignee: was\n\nIf you try to use jmol over https, every single time\nyou display an image it displays the following dialog box:\n\n\"Client Authentication: The client is trying to ... Please select\nthe certificate:\"\n\nThen there is a list with no certificates, and a button \"Details\"\nthat when clicked does nothing.    \n\nThis is really annoying.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1589\n\n",
    "created_at": "2007-12-23T06:55:33Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "jmol -- using via https is a pain in the butt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1589",
    "user": "was"
}
```
Assignee: was

If you try to use jmol over https, every single time
you display an image it displays the following dialog box:

"Client Authentication: The client is trying to ... Please select
the certificate:"

Then there is a list with no certificates, and a button "Details"
that when clicked does nothing.    

This is really annoying.


Issue created by migration from https://trac.sagemath.org/ticket/1589





---

archive/issue_comments_010115.json:
```json
{
    "body": "This is a known issue with java and https. See http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6186280\n\nHowever, to use http we might need to sign the applet, which would be a (different) dialog. \n\nThere may be something we can change on the twisted side of things so that it knows not to ask for a client certificate. This I think is our best bet, but I am very unfamiliar with the notebook authentication code (but would be willing to learn).",
    "created_at": "2007-12-23T08:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1589#issuecomment-10115",
    "user": "robertwb"
}
```

This is a known issue with java and https. See http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6186280

However, to use http we might need to sign the applet, which would be a (different) dialog. 

There may be something we can change on the twisted side of things so that it knows not to ask for a client certificate. This I think is our best bet, but I am very unfamiliar with the notebook authentication code (but would be willing to learn).



---

archive/issue_comments_010116.json:
```json
{
    "body": "I have confirmed that this is a twisted authentication issue, one can serve applets over https (and have said applets request resources) without this annoying dialog. \n\nI'm looking into our authentication code now.",
    "created_at": "2008-01-02T20:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1589#issuecomment-10116",
    "user": "robertwb"
}
```

I have confirmed that this is a twisted authentication issue, one can serve applets over https (and have said applets request resources) without this annoying dialog. 

I'm looking into our authentication code now.



---

archive/issue_comments_010117.json:
```json
{
    "body": "Attachment [1589-gnutls-cert.diff](tarball://root/attachments/some-uuid/ticket1589/1589-gnutls-cert.diff) by robertwb created at 2008-01-03 08:43:00\n\nGNUTLS provides two options for client-side certificates, CERT_REQUEST and CERT_REQUIRE, both of which request a certificate. I found the place in the source that uses these constants, and if one sets the value to 0 (unexposed via in the api) a certificate won't be requested. \n\nThe least intrusive change was to spoof CERT_REQUEST=0 in the notebook run script. This finally gets rid of that dialog that's been haunting me for almost a year now (was there with the other java 3d viewers as well).",
    "created_at": "2008-01-03T08:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1589#issuecomment-10117",
    "user": "robertwb"
}
```

Attachment [1589-gnutls-cert.diff](tarball://root/attachments/some-uuid/ticket1589/1589-gnutls-cert.diff) by robertwb created at 2008-01-03 08:43:00

GNUTLS provides two options for client-side certificates, CERT_REQUEST and CERT_REQUIRE, both of which request a certificate. I found the place in the source that uses these constants, and if one sets the value to 0 (unexposed via in the api) a certificate won't be requested. 

The least intrusive change was to spoof CERT_REQUEST=0 in the notebook run script. This finally gets rid of that dialog that's been haunting me for almost a year now (was there with the other java 3d viewers as well).



---

archive/issue_comments_010118.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2008-01-04T06:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1589#issuecomment-10118",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_010119.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-04T06:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1589#issuecomment-10119",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010120.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-05T12:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1589#issuecomment-10120",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010121.json:
```json
{
    "body": "Merged in 2.9.2.",
    "created_at": "2008-01-05T12:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1589#issuecomment-10121",
    "user": "mabshoff"
}
```

Merged in 2.9.2.
