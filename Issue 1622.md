# Issue 1622: update gnutls to 2.2.0

archive/issues_001622.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1622\n\n",
    "created_at": "2007-12-29T04:36:21Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "update gnutls to 2.2.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1622",
    "user": "mabshoff"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/1622





---

archive/issue_comments_010324.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-29T04:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1622#issuecomment-10324",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010325.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2007-12-29T04:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1622#issuecomment-10325",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_010326.json:
```json
{
    "body": "They just released 2.3.0 so we might as well update to the latest.\n\nhttp://www.gnu.org/software/gnutls/releases/gnutls-2.3.0.tar.bz2",
    "created_at": "2008-01-11T00:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1622#issuecomment-10326",
    "user": "yi"
}
```

They just released 2.3.0 so we might as well update to the latest.

http://www.gnu.org/software/gnutls/releases/gnutls-2.3.0.tar.bz2



---

archive/issue_comments_010327.json:
```json
{
    "body": "I just tried to create spkg's for it and everything is dandy except python-gnutls.  There are major changes to the openpgp parts of gnutls which causes the pytho-gnutls not to work. I've contacted the author of python-gnutls to see if he'll update the wrapper.",
    "created_at": "2008-01-11T07:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1622#issuecomment-10327",
    "user": "yi"
}
```

I just tried to create spkg's for it and everything is dandy except python-gnutls.  There are major changes to the openpgp parts of gnutls which causes the pytho-gnutls not to work. I've contacted the author of python-gnutls to see if he'll update the wrapper.



---

archive/issue_comments_010328.json:
```json
{
    "body": "Also, here is a list of related packages that need to be updated as well:\n\nopencdk\nlibgcrypt\nlibgpg-error\npython-gnutls",
    "created_at": "2008-01-11T07:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1622#issuecomment-10328",
    "user": "yi"
}
```

Also, here is a list of related packages that need to be updated as well:

opencdk
libgcrypt
libgpg-error
python-gnutls



---

archive/issue_comments_010329.json:
```json
{
    "body": "Replying to [comment:4 yi]:\n> Also, here is a list of related packages that need to be updated as well:\n> \n> opencdk\n> libgcrypt\n> libgpg-error\n> python-gnutls\n\nYou are correct that once we update GNUTLS we at least need to update OpenCDK, but I will also update the others in one swoop. I will do this after I switch python to ucs4 though, which is the big goal for alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-11T10:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1622#issuecomment-10329",
    "user": "mabshoff"
}
```

Replying to [comment:4 yi]:
> Also, here is a list of related packages that need to be updated as well:
> 
> opencdk
> libgcrypt
> libgpg-error
> python-gnutls

You are correct that once we update GNUTLS we at least need to update OpenCDK, but I will also update the others in one swoop. I will do this after I switch python to ucs4 though, which is the big goal for alpha2.

Cheers,

Michael



---

archive/issue_comments_010330.json:
```json
{
    "body": "An updated spkg with 64 bit OSX Mac support is at:\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha0/gnutls-2.2.1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-19T23:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1622#issuecomment-10330",
    "user": "mabshoff"
}
```

An updated spkg with 64 bit OSX Mac support is at:

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha0/gnutls-2.2.1.spkg

Cheers,

Michael



---

archive/issue_comments_010331.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-19T23:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1622#issuecomment-10331",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha0



---

archive/issue_comments_010332.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-19T23:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1622#issuecomment-10332",
    "user": "mabshoff"
}
```

Resolution: fixed
