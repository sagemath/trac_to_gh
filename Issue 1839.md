# Issue 1839: [with script; needs review and integration] sage-crap: incorporate this script into sage and start using it before each release.

archive/issues_001839.json:
```json
{
    "body": "Assignee: malb\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1839\n\n",
    "created_at": "2008-01-18T22:04:27Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "title": "[with script; needs review and integration] sage-crap: incorporate this script into sage and start using it before each release.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1839",
    "user": "was"
}
```
Assignee: malb



Issue created by migration from https://trac.sagemath.org/ticket/1839





---

archive/issue_comments_011640.json:
```json
{
    "body": "Changing assignee from malb to mabshoff.",
    "created_at": "2008-01-18T22:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11640",
    "user": "mabshoff"
}
```

Changing assignee from malb to mabshoff.



---

archive/issue_comments_011641.json:
```json
{
    "body": "Changing component from commutative algebra to packages.",
    "created_at": "2008-01-18T22:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11641",
    "user": "mabshoff"
}
```

Changing component from commutative algebra to packages.



---

archive/issue_comments_011642.json:
```json
{
    "body": "I BSD license this file\n\n```\n* Copyright (c) 2008, William Stein (with permission)\n* All rights reserved.\n*\n* Redistribution and use in source and binary forms, with or without\n* modification, are permitted provided that the following conditions are met:\n*     * Redistributions of source code must retain the above copyright\n*       notice, this list of conditions and the following disclaimer.\n*     * Redistributions in binary form must reproduce the above copyright\n*       notice, this list of conditions and the following disclaimer in the\n*       documentation and/or other materials provided with the distribution.\n*     * Neither the name of the Sage Project nor the\n*       names of its contributors may be used to endorse or promote products\n*       derived from this software without specific prior written permission.\n*\n* THIS SOFTWARE IS PROVIDED BY WILLIAM STEIN ``AS IS'' AND ANY\n* EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED\n* WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\n* DISCLAIMED. IN NO EVENT SHALL William Stein BE LIABLE FOR ANY\n* DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n* (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\n* LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND\n* ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n* (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS\n* SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n```\n",
    "created_at": "2008-04-05T22:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11642",
    "user": "was"
}
```

I BSD license this file

```
* Copyright (c) 2008, William Stein (with permission)
* All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions are met:
*     * Redistributions of source code must retain the above copyright
*       notice, this list of conditions and the following disclaimer.
*     * Redistributions in binary form must reproduce the above copyright
*       notice, this list of conditions and the following disclaimer in the
*       documentation and/or other materials provided with the distribution.
*     * Neither the name of the Sage Project nor the
*       names of its contributors may be used to endorse or promote products
*       derived from this software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY WILLIAM STEIN ``AS IS'' AND ANY
* EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
* WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
* DISCLAIMED. IN NO EVENT SHALL William Stein BE LIABLE FOR ANY
* DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
* (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
* LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
* ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
* (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
* SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```




---

archive/issue_comments_011643.json:
```json
{
    "body": "See http://8tb.us/home/boothby/crap.patch",
    "created_at": "2008-04-06T07:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11643",
    "user": "was"
}
```

See http://8tb.us/home/boothby/crap.patch



---

archive/issue_comments_011644.json:
```json
{
    "body": "Attachment [crap.patch](tarball://root/attachments/some-uuid/ticket1839/crap.patch) by boothby created at 2008-04-06 19:32:12\n\nThe attached patch integrates sage-crap, and works on my machines. (debian xeon / ubuntu 32bit)",
    "created_at": "2008-04-06T19:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11644",
    "user": "boothby"
}
```

Attachment [crap.patch](tarball://root/attachments/some-uuid/ticket1839/crap.patch) by boothby created at 2008-04-06 19:32:12

The attached patch integrates sage-crap, and works on my machines. (debian xeon / ubuntu 32bit)



---

archive/issue_comments_011645.json:
```json
{
    "body": "A couple remarks:\n\n* is this script still destructive? In that care it should be mentioned in the help\n* the script does deal with spkgs and not tars per se - maybe the help in sage-sage should be changed?\n\nOther than we might want to add a -crapall option since that is likely the default way one would deploy such a script, i.e. before a release. Maybe even adding a crap score might be a good thing :)\n\nCheers,\n\nMichael",
    "created_at": "2008-05-06T11:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11645",
    "user": "mabshoff"
}
```

A couple remarks:

* is this script still destructive? In that care it should be mentioned in the help
* the script does deal with spkgs and not tars per se - maybe the help in sage-sage should be changed?

Other than we might want to add a -crapall option since that is likely the default way one would deploy such a script, i.e. before a release. Maybe even adding a crap score might be a good thing :)

Cheers,

Michael



---

archive/issue_comments_011646.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-15T21:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11646",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_011647.json:
```json
{
    "body": "The referee report is above by malb.  William Stein will do the work to fix this patch.",
    "created_at": "2008-06-15T22:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11647",
    "user": "was"
}
```

The referee report is above by malb.  William Stein will do the work to fix this patch.



---

archive/issue_comments_011648.json:
```json
{
    "body": "Example of using this with runlevel=1 on sage-3.0.3.alpha2 -- where we see there is some crap!:\n\n```\nwas@sage:~/build/sage-3.0.3.alpha2$ ./sage -crap sage-3.0.3.alpha2.tar \n/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2.tar\nrunlevel=  1\n/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/src-gmp/.DS_Store: JVT NAL sequence\n/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/src/.DS_Store: JVT NAL sequence\n/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src/.DS_Store.1: JVT NAL sequence\n/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src/.DS_Store: empty\n/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src-gmp/.DS_Store.1: JVT NAL sequence\n/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src-gmp/.DS_Store: empty\n/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/.DS_Store.1: JVT NAL sequence\n/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/cddlibman.aux: LaTeX auxiliary file\n/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/cddlibman.dvi: TeX DVI\n/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/cddlibman.toc: UNKNOWN\ncddlibman.toc: LaTeX  table of contents\n```\n",
    "created_at": "2008-06-15T23:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11648",
    "user": "was"
}
```

Example of using this with runlevel=1 on sage-3.0.3.alpha2 -- where we see there is some crap!:

```
was@sage:~/build/sage-3.0.3.alpha2$ ./sage -crap sage-3.0.3.alpha2.tar 
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2.tar
runlevel=  1
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/src-gmp/.DS_Store: JVT NAL sequence
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/src/.DS_Store: JVT NAL sequence
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src/.DS_Store.1: JVT NAL sequence
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src/.DS_Store: empty
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src-gmp/.DS_Store.1: JVT NAL sequence
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/lib-src-gmp/.DS_Store: empty
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/.DS_Store.1: JVT NAL sequence
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/cddlibman.aux: LaTeX auxiliary file
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/cddlibman.dvi: TeX DVI
/home/was/.sage/temp/sage/32206/dir_0/sage-3.0.3.alpha2/spkg/standard/cddlib-094b.p2/src/doc/cddlibman.toc: UNKNOWN
cddlibman.toc: LaTeX  table of contents
```




---

archive/issue_comments_011649.json:
```json
{
    "body": "Attachment [scripts-1839.patch](tarball://root/attachments/some-uuid/ticket1839/scripts-1839.patch) by was created at 2008-06-16 00:15:29\n\npart 2 of the patch",
    "created_at": "2008-06-16T00:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11649",
    "user": "was"
}
```

Attachment [scripts-1839.patch](tarball://root/attachments/some-uuid/ticket1839/scripts-1839.patch) by was created at 2008-06-16 00:15:29

part 2 of the patch



---

archive/issue_comments_011650.json:
```json
{
    "body": "I requested boothby to review this.",
    "created_at": "2008-06-19T23:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11650",
    "user": "was"
}
```

I requested boothby to review this.



---

archive/issue_comments_011651.json:
```json
{
    "body": "I consider my having read over it as a review and my little integration patch as part of that.",
    "created_at": "2008-07-08T00:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11651",
    "user": "was"
}
```

I consider my having read over it as a review and my little integration patch as part of that.



---

archive/issue_comments_011652.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0. I also give this ticket a positive review and all issues that crop up will be dealt with on follow up tickets.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-08T00:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11652",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc0. I also give this ticket a positive review and all issues that crop up will be dealt with on follow up tickets.

Cheers,

Michael



---

archive/issue_comments_011653.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0",
    "created_at": "2008-07-08T00:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11653",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc0



---

archive/issue_comments_011654.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-08T00:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1839#issuecomment-11654",
    "user": "mabshoff"
}
```

Resolution: fixed
