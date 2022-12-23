# Issue 9643: Force ECL to disable assembly code on Solaris 10 as it does on OpenSolaris

archive/issues_009643.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jhpalmieri jsp mariah mpatel\n\n#9474 disabled assembly code in ECL if the following three conditions were all met\n\n* OpenSolaris  (also known as Solaris 11 or SunOS 5.11)\n* x64 platform\n* 64-bit build\n\nThese conditions were checked, by testing the output of `uname -rsm`, which was: \n\n\n```\ndrkirkby@hawk:~$ uname -rsm\nSunOS 5.11 i86pc\n```\n\n\nA note was added in `spkg-install` that it might be necessary to disable the assembly code on other variants of Solaris, but I was unsure at the time. \n\nJohn Palmieri has discovered ECL fails to build on Solaris 10 with the x64 processor in 64-bit mode. So the conditions for disabling the assembly code needs to be made less strict, as the release number (5.10 for Solaris 10, 5.11 for OpenSolaris), must be ignored. Instead the test will use `uname -sm`, dropping the `-r` option which checked the release. \n\n\n```\ndrkirkby@hawk:~$ uname -sm\nSunOS i86pc\n```\n\n\nThis should be a very easy fix. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9643\n\n",
    "created_at": "2010-07-29T23:30:46Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "Force ECL to disable assembly code on Solaris 10 as it does on OpenSolaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9643",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  jhpalmieri jsp mariah mpatel

#9474 disabled assembly code in ECL if the following three conditions were all met

* OpenSolaris  (also known as Solaris 11 or SunOS 5.11)
* x64 platform
* 64-bit build

These conditions were checked, by testing the output of `uname -rsm`, which was: 


```
drkirkby@hawk:~$ uname -rsm
SunOS 5.11 i86pc
```


A note was added in `spkg-install` that it might be necessary to disable the assembly code on other variants of Solaris, but I was unsure at the time. 

John Palmieri has discovered ECL fails to build on Solaris 10 with the x64 processor in 64-bit mode. So the conditions for disabling the assembly code needs to be made less strict, as the release number (5.10 for Solaris 10, 5.11 for OpenSolaris), must be ignored. Instead the test will use `uname -sm`, dropping the `-r` option which checked the release. 


```
drkirkby@hawk:~$ uname -sm
SunOS i86pc
```


This should be a very easy fix. 

Issue created by migration from https://trac.sagemath.org/ticket/9643





---

archive/issue_comments_093467.json:
```json
{
    "body": "A new .spkg file can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p2.spkg\n\nThis is currently untested, so I am not marking this for review just now. But I'm 95% sure this will resolve the issue. \n\nDave",
    "created_at": "2010-07-29T23:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9643#issuecomment-93467",
    "user": "drkirkby"
}
```

A new .spkg file can be found at 

http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p2.spkg

This is currently untested, so I am not marking this for review just now. But I'm 95% sure this will resolve the issue. 

Dave



---

archive/issue_comments_093468.json:
```json
{
    "body": "Mercurial patch which should disable assembly code on Solaris 10 or OpenSolaris in 64-bit mode on x64 hardware",
    "created_at": "2010-07-29T23:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9643#issuecomment-93468",
    "user": "drkirkby"
}
```

Mercurial patch which should disable assembly code on Solaris 10 or OpenSolaris in 64-bit mode on x64 hardware



---

archive/issue_comments_093469.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-05T00:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9643#issuecomment-93469",
    "user": "drkirkby"
}
```

Attachment



---

archive/issue_comments_093470.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-07T19:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9643#issuecomment-93470",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093471.json:
```json
{
    "body": "Just to make it clear, on any Solaris 10 or OpenSolaris machine, with an Intel/AMD processor, the output of `uname -m` is the same:\n\n* On my Sun Ultra 27 running OpenSolaris\n\n```\ndrkirkby@hawk:~$ uname -m\ni86pc\ndrkirkby@hawk:~$ uname -sm\nSunOS i86pc\ndrkirkby@hawk:~$ uname -rsm\nSunOS 5.11 i86pc\ndrkirkby@hawk:~$ \n```\n\n* On fulvia on skynet:\n\n```\n64 drkirkby@fulvia:[~] $ uname -m\ni86pc\n64 drkirkby@fulvia:[~] $ uname -sm\nSunOS i86pc\n64 drkirkby@fulvia:[~] $ uname -rsm\nSunOS 5.10 i86pc\n```\n\n\nOne can differentiate Solaris 10 and Solaris 11 machines by using the release version of the operating system (Solaris 10 shows 5.10, and OpenSolaris shows 5.11). \n\nSince I now wish to disable the assembly code on both Solaris 10 and Solaris 11, the option which shows the release (`-r`) needs removing. \n\nI'm choosing not to use the `-p` option to `uname`, as it's not portable. \n\nhttp://www.opengroup.org/onlinepubs/009695399/utilities/uname.html\n\nThe only portable options to uname are `-a, -m, -n, -r` and `-v`.",
    "created_at": "2010-08-09T08:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9643#issuecomment-93471",
    "user": "drkirkby"
}
```

Just to make it clear, on any Solaris 10 or OpenSolaris machine, with an Intel/AMD processor, the output of `uname -m` is the same:

* On my Sun Ultra 27 running OpenSolaris

```
drkirkby@hawk:~$ uname -m
i86pc
drkirkby@hawk:~$ uname -sm
SunOS i86pc
drkirkby@hawk:~$ uname -rsm
SunOS 5.11 i86pc
drkirkby@hawk:~$ 
```

* On fulvia on skynet:

```
64 drkirkby@fulvia:[~] $ uname -m
i86pc
64 drkirkby@fulvia:[~] $ uname -sm
SunOS i86pc
64 drkirkby@fulvia:[~] $ uname -rsm
SunOS 5.10 i86pc
```


One can differentiate Solaris 10 and Solaris 11 machines by using the release version of the operating system (Solaris 10 shows 5.10, and OpenSolaris shows 5.11). 

Since I now wish to disable the assembly code on both Solaris 10 and Solaris 11, the option which shows the release (`-r`) needs removing. 

I'm choosing not to use the `-p` option to `uname`, as it's not portable. 

http://www.opengroup.org/onlinepubs/009695399/utilities/uname.html

The only portable options to uname are `-a, -m, -n, -r` and `-v`.



---

archive/issue_comments_093472.json:
```json
{
    "body": "Replying to [comment:4 drkirkby]:\n \n> I'm choosing not to use the `-p` option to `uname`, as it's not portable. \n> \n> http://www.opengroup.org/onlinepubs/009695399/utilities/uname.html\n> \n> The only portable options to uname are `-a, -m, -n, -r` and `-v`.\n\nOops, `-s`, which writes the name of the implementation of the operating system, is portable too.",
    "created_at": "2010-08-09T08:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9643#issuecomment-93472",
    "user": "drkirkby"
}
```

Replying to [comment:4 drkirkby]:
 
> I'm choosing not to use the `-p` option to `uname`, as it's not portable. 
> 
> http://www.opengroup.org/onlinepubs/009695399/utilities/uname.html
> 
> The only portable options to uname are `-a, -m, -n, -r` and `-v`.

Oops, `-s`, which writes the name of the implementation of the operating system, is portable too.



---

archive/issue_comments_093473.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-09T09:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9643#issuecomment-93473",
    "user": "fbissey"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093474.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-08-09T09:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9643#issuecomment-93474",
    "user": "fbissey"
}
```

Looks good to me.



---

archive/issue_comments_093475.json:
```json
{
    "body": "## Note to the release manager\n\nThere are no library patches. The patch is already integrated into this .spkg, so it only needs to be merged - nothing else. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p2.spkg",
    "created_at": "2010-08-09T09:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9643#issuecomment-93475",
    "user": "drkirkby"
}
```

## Note to the release manager

There are no library patches. The patch is already integrated into this .spkg, so it only needs to be merged - nothing else. 

http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p2.spkg



---

archive/issue_comments_093476.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-15T08:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9643#issuecomment-93476",
    "user": "mpatel"
}
```

Resolution: fixed
