# Issue 122: some minor issues with some build procedures in packages (noted by Mike Rubinstein)

archive/issues_000122.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nHi william. Here are the two funny things I noticed\non Friday:\n \nIn sage-1.4/spkg/build/mpfr-20060930/spkg-install\n \nthere are a couple of options given to ./configure that are specific to\nNTL and don't seem to have anything to do with mpfr, namely:\n \nNTL_GMP_LIP=on NTL_STD_CXX=on\n \n-------------------------------------------\nIn sage-1.4/spkg/build/gmp-4.2.1/spkg-install\n \nI'm not sure what the --build=none-apple-darwin option is good for.\nI got gmp to compile fine on my PowerBook G4 without it.\nYou have:\n \n           # I learned this from\n           # http://www.mail-archive.com/clamav-users@lists.clamav.net/msg22183.html\n           #  -- William Stein, 2006-04-06\n           # It's perhaps weird that this is needed on the powerpc, but it is...\n           SAGE_CONF_OPTS=\"--build=none-apple-darwin --enable-shared --disable-static\"\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/122\n\n",
    "created_at": "2006-10-09T08:13:29Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "title": "some minor issues with some build procedures in packages (noted by Mike Rubinstein)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/122",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
Hi william. Here are the two funny things I noticed
on Friday:
 
In sage-1.4/spkg/build/mpfr-20060930/spkg-install
 
there are a couple of options given to ./configure that are specific to
NTL and don't seem to have anything to do with mpfr, namely:
 
NTL_GMP_LIP=on NTL_STD_CXX=on
 
-------------------------------------------
In sage-1.4/spkg/build/gmp-4.2.1/spkg-install
 
I'm not sure what the --build=none-apple-darwin option is good for.
I got gmp to compile fine on my PowerBook G4 without it.
You have:
 
           # I learned this from
           # http://www.mail-archive.com/clamav-users@lists.clamav.net/msg22183.html
           #  -- William Stein, 2006-04-06
           # It's perhaps weird that this is needed on the powerpc, but it is...
           SAGE_CONF_OPTS="--build=none-apple-darwin --enable-shared --disable-static"
```


Issue created by migration from https://trac.sagemath.org/ticket/122





---

archive/issue_comments_000561.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-15T18:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/122#issuecomment-561",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000239.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2006-10-15T18:48:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/122",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/122#event-239"
}
```
