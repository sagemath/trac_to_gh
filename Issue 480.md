# Issue 480: Make Sage work with SELinux on Linux

archive/issues_000480.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  was vbraun\n\nFedora Core 7 has SELinux turned on per default. Sage should support running when SELinux is activated. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/480\n\n",
    "created_at": "2007-08-22T21:37:55Z",
    "labels": [
        "distribution",
        "major",
        "enhancement"
    ],
    "title": "Make Sage work with SELinux on Linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/480",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  was vbraun

Fedora Core 7 has SELinux turned on per default. Sage should support running when SELinux is activated. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/480





---

archive/issue_comments_002393.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-22T21:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/480#issuecomment-2393",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002394.json:
```json
{
    "body": "From http://www.ittvis.com/services/techtip.asp?ttid=3092:\n\n```\nTo rectify this issue, you can either:\n\n    * Change the default security context for IDL by issuing the command:\n\n      chcon -t texrel_shlib_t /usr/local/rsi/idl_6.1/bin/bin.linux.x86/*.so\n```\n\n\nCheers,\n\nM ichael",
    "created_at": "2007-12-06T20:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/480#issuecomment-2394",
    "user": "mabshoff"
}
```

From http://www.ittvis.com/services/techtip.asp?ttid=3092:

```
To rectify this issue, you can either:

    * Change the default security context for IDL by issuing the command:

      chcon -t texrel_shlib_t /usr/local/rsi/idl_6.1/bin/bin.linux.x86/*.so
```


Cheers,

M ichael



---

archive/issue_comments_002395.json:
```json
{
    "body": "\n```\nOn my CENTOS 5 system, I found the SELinux errors can be avoided by setting SELinux to \"permissive\" rather than \"enforced.\"  \"Disabled\" was not necessary.  Lots of software seems to be affected by the new tighted SELinux settings, including Mathematica.\nThanks for your great work on SAGE!\n```\n",
    "created_at": "2007-12-24T06:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/480#issuecomment-2395",
    "user": "mhansen"
}
```


```
On my CENTOS 5 system, I found the SELinux errors can be avoided by setting SELinux to "permissive" rather than "enforced."  "Disabled" was not necessary.  Lots of software seems to be affected by the new tighted SELinux settings, including Mathematica.
Thanks for your great work on SAGE!
```




---

archive/issue_comments_002396.json:
```json
{
    "body": "Is this still valid?",
    "created_at": "2012-05-28T07:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/480#issuecomment-2396",
    "user": "mhansen"
}
```

Is this still valid?



---

archive/issue_comments_002397.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-28T07:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/480#issuecomment-2397",
    "user": "mhansen"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_002398.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2012-05-28T07:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/480#issuecomment-2398",
    "user": "mhansen"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_002399.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-08-01T06:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/480#issuecomment-2399",
    "user": "mhansen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_002400.json:
```json
{
    "body": "I think we can closed this as invalid since SELinux has been incorporated to the 2.6 kernel for quite awhile now.",
    "created_at": "2012-08-01T06:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/480#issuecomment-2400",
    "user": "mhansen"
}
```

I think we can closed this as invalid since SELinux has been incorporated to the 2.6 kernel for quite awhile now.



---

archive/issue_comments_002401.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-01T06:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/480#issuecomment-2401",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_002402.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-08-01T12:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/480#issuecomment-2402",
    "user": "jdemeyer"
}
```

Resolution: worksforme
