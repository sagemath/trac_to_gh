# Issue 8583: Add guidelines for updating standard packages.

archive/issues_008583.json:
```json
{
    "body": "Assignee: mvngu\n\nThe developers guide has some guidance on how to update .spkg files\n\nhttp://www.sagemath.org/doc/developer/patching_spkgs.html\n\nwhich is well written and clear, but need expanding. The following is a list of suggestions, which are based on my original proposal, and feedback from others on sage-devel. \n\n == Additional Information Needed for Updating Packages. ==\n\n1) Are there any new warnings about depreciated options to the configure script(s) if they are used? If there are new warnings, you need to understand why the option was given, why it depreciated, and what you should do about it.\n\n2) Are there any warnings about unrecognized options to configure scripts? If so, it is **essential** these are resolved.\n\n3) If there are any patches to the original package, do they need re-writing? If a source file is overwritten, are you sure that overwriting it is still appropriate?\n\n4) Does the new package build on Linux, OSX and Solaris? The author should provide the output of 'uname -a' on all system where they have checked the updated package and place that on the trac ticket.\n\n5) Are any special build instructions listed in SPKG.txt followed?\n\n6) Read ALL the comments in SPKG.txt, to see what people have changed and why. Do any of them have implications for the update?\n\n7) Are all the patches applied still necessary? Sometimes bugs may be fixed upstream, so a patch is not required.\n\n8) Are there any new dependencies? Sometimes new versions of packages require libraries that versions ones did not, or require later versions of libraries. If so, does Sage include those dependencies? Just because your system has the dependency, do not assume that everyone else will have it. \n\n9) Have you read the release notes for the update? If not, do so, and ensure there is nothing that will obviously cause a problem in Sage. If possible provide a web link to the release notes to aid the reviewer. \n\n10) Have you documented the trac ticket for the update in SPKG.txt? If not, do so. If a ticket is not open for the update, then create the ticket, and reference that in SPKG.txt\n\n == Additional Information Needed for Reviewing Packages. ==\n\nThe reviewer(s) should test the updated package on at least one Linux, one OS X and one Solaris 10 system. Ideally, these systems should be different to those used by the author. In the case of the Linux system, testing the package on a different distribution of Linux to that used by the author would be preferable. However, in some cases the reviewer may have no option but to test on the same systems as the author, though they should try to test on different systems if possible. \n\nThe reviewer should place on the trac ticket the output of 'uname -a' on the systems which they have tested the package. \n\nThe reviewer should read the release notes for the new package, to determine if he/she believes there are changes which may be needed to the package.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8583\n\n",
    "created_at": "2010-03-23T06:28:44Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add guidelines for updating standard packages.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8583",
    "user": "drkirkby"
}
```
Assignee: mvngu

The developers guide has some guidance on how to update .spkg files

http://www.sagemath.org/doc/developer/patching_spkgs.html

which is well written and clear, but need expanding. The following is a list of suggestions, which are based on my original proposal, and feedback from others on sage-devel. 

 == Additional Information Needed for Updating Packages. ==

1) Are there any new warnings about depreciated options to the configure script(s) if they are used? If there are new warnings, you need to understand why the option was given, why it depreciated, and what you should do about it.

2) Are there any warnings about unrecognized options to configure scripts? If so, it is **essential** these are resolved.

3) If there are any patches to the original package, do they need re-writing? If a source file is overwritten, are you sure that overwriting it is still appropriate?

4) Does the new package build on Linux, OSX and Solaris? The author should provide the output of 'uname -a' on all system where they have checked the updated package and place that on the trac ticket.

5) Are any special build instructions listed in SPKG.txt followed?

6) Read ALL the comments in SPKG.txt, to see what people have changed and why. Do any of them have implications for the update?

7) Are all the patches applied still necessary? Sometimes bugs may be fixed upstream, so a patch is not required.

8) Are there any new dependencies? Sometimes new versions of packages require libraries that versions ones did not, or require later versions of libraries. If so, does Sage include those dependencies? Just because your system has the dependency, do not assume that everyone else will have it. 

9) Have you read the release notes for the update? If not, do so, and ensure there is nothing that will obviously cause a problem in Sage. If possible provide a web link to the release notes to aid the reviewer. 

10) Have you documented the trac ticket for the update in SPKG.txt? If not, do so. If a ticket is not open for the update, then create the ticket, and reference that in SPKG.txt

 == Additional Information Needed for Reviewing Packages. ==

The reviewer(s) should test the updated package on at least one Linux, one OS X and one Solaris 10 system. Ideally, these systems should be different to those used by the author. In the case of the Linux system, testing the package on a different distribution of Linux to that used by the author would be preferable. However, in some cases the reviewer may have no option but to test on the same systems as the author, though they should try to test on different systems if possible. 

The reviewer should place on the trac ticket the output of 'uname -a' on the systems which they have tested the package. 

The reviewer should read the release notes for the new package, to determine if he/she believes there are changes which may be needed to the package.

Issue created by migration from https://trac.sagemath.org/ticket/8583





---

archive/issue_comments_077733.json:
```json
{
    "body": "Any progress on this one Minh? If Sage 5 is going to support Solaris, there needs to be something in place to tell people that they must test and changes to standard packages on Solaris. \n\nWhat worries me a bit is sometimes people think their package will only affect one platform, since it uses 'uname' in some way, but a typo could make it affect others too. \n\n\n```\nif [ `uname` != sunos ] ; then\n...\n```\n\n\nmight look as though it will do something on every platform except Solaris, but in fact the string is SunOS and not sunos. Hence I believe people need to test the code - not just think it is ok. \n\ndave",
    "created_at": "2010-04-13T07:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8583#issuecomment-77733",
    "user": "drkirkby"
}
```

Any progress on this one Minh? If Sage 5 is going to support Solaris, there needs to be something in place to tell people that they must test and changes to standard packages on Solaris. 

What worries me a bit is sometimes people think their package will only affect one platform, since it uses 'uname' in some way, but a typo could make it affect others too. 


```
if [ `uname` != sunos ] ; then
...
```


might look as though it will do something on every platform except Solaris, but in fact the string is SunOS and not sunos. Hence I believe people need to test the code - not just think it is ok. 

dave



---

archive/issue_comments_077734.json:
```json
{
    "body": "outdated, should close",
    "created_at": "2021-12-02T00:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8583#issuecomment-77734",
    "user": "@mkoeppe"
}
```

outdated, should close



---

archive/issue_comments_077735.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-12-02T00:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8583#issuecomment-77735",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077736.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-12-03T10:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8583#issuecomment-77736",
    "user": "@dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077737.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-12-03T18:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8583#issuecomment-77737",
    "user": "@mkoeppe"
}
```

Resolution: invalid
