# Issue 4986: import audit

archive/issues_004986.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @craigcitro @nexttime @kcrisman\n\nIt is currently way to easy to introduce circular imports in Sage, and a mess to try and hunt time down. An order in which things are imported is found in sage.all, but due to the cascade of imports in sage.misc (and elsewhere) this is not an accurate representation of what actually happens. This could stand to be cleaned up a lot. Ideally, little/none of sage.foo.* should be used before sage.foo.all is imported. \n\nThis patch prints out imports as they happen, and where they're initiated. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4986\n\n",
    "created_at": "2009-01-16T04:04:46Z",
    "labels": [
        "performance",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "import audit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4986",
    "user": "@robertwb"
}
```
Assignee: mabshoff

CC:  @craigcitro @nexttime @kcrisman

It is currently way to easy to introduce circular imports in Sage, and a mess to try and hunt time down. An order in which things are imported is found in sage.all, but due to the cascade of imports in sage.misc (and elsewhere) this is not an accurate representation of what actually happens. This could stand to be cleaned up a lot. Ideally, little/none of sage.foo.* should be used before sage.foo.all is imported. 

This patch prints out imports as they happen, and where they're initiated. 

Issue created by migration from https://trac.sagemath.org/ticket/4986





---

archive/issue_comments_038027.json:
```json
{
    "body": "I guess the patch isn't posted yet, but this seems like \"sage -startuptime\" which prints out imports as they occur.",
    "created_at": "2009-01-16T04:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4986#issuecomment-38027",
    "user": "@mwhansen"
}
```

I guess the patch isn't posted yet, but this seems like "sage -startuptime" which prints out imports as they occur.



---

archive/issue_comments_038028.json:
```json
{
    "body": "Attachment [import-audit.patch](tarball://root/attachments/some-uuid/ticket4986/import-audit.patch) by @robertwb created at 2009-01-16 04:16:30",
    "created_at": "2009-01-16T04:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4986#issuecomment-38028",
    "user": "@robertwb"
}
```

Attachment [import-audit.patch](tarball://root/attachments/some-uuid/ticket4986/import-audit.patch) by @robertwb created at 2009-01-16 04:16:30



---

archive/issue_comments_038029.json:
```json
{
    "body": "Yes, it is a lot like sage -startuptime. One difference is that it prints out where each import is coming from, and also filters based on whether or not the corresponding *.all module has been loaded.",
    "created_at": "2009-01-16T04:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4986#issuecomment-38029",
    "user": "@robertwb"
}
```

Yes, it is a lot like sage -startuptime. One difference is that it prints out where each import is coming from, and also filters based on whether or not the corresponding *.all module has been loaded.



---

archive/issue_comments_038030.json:
```json
{
    "body": "To clarify, this patch should not be applied (unless we want the info to come up with every startup, or only enable it with a flag). Also, the work has not been done, What is attached is just a diagnostic tool.",
    "created_at": "2009-01-16T07:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4986#issuecomment-38030",
    "user": "@robertwb"
}
```

To clarify, this patch should not be applied (unless we want the info to come up with every startup, or only enable it with a flag). Also, the work has not been done, What is attached is just a diagnostic tool.



---

archive/issue_comments_038031.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4986#issuecomment-38031",
    "user": "@aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_038032.json:
```json
{
    "body": "In case anything should happen here...",
    "created_at": "2011-08-21T01:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4986#issuecomment-38032",
    "user": "@nexttime"
}
```

In case anything should happen here...



---

archive/issue_comments_038033.json:
```json
{
    "body": "Ditto.",
    "created_at": "2011-08-21T04:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4986#issuecomment-38033",
    "user": "@kcrisman"
}
```

Ditto.



---

archive/issue_comments_038034.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> Ditto.\n\nRe: sage-devel thread: I was wondering what you were waiting for.\n\n(Haven't tested the patch here; I think you won't be able to print PARI's variables with this method anyway, at least not easily.)\n\nNote that you can inject code into the C files generated by Cython, e.g. with your favourite friend `sed`, especially into the functions called upon module initialization:\n\n```sh\n$ cd devel/sage/sage/rings\n$ sed -i -e '/^PyMODINIT_FUNC PyInit_.*(void)$/,+3s/^{$/{\\n  printf(\"Hello!\\\\n\");\\n/' real_mpfr.c\n$ ../../../../sage -br\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n...\nbuilding 'sage.rings.real_mpfr' extension\nExecute 1 commands (using 1 threads)\n...\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nHello!\nsage: \n```\n\n(This example is of course quite specific to the current layout of the C code generated by Cython. Also, for simplicity I've used the less portable `-i` option.)\n| Sage Version 4.7.2.alpha1, Release Date: 2011-08-17                |\n| Type notebook() for the GUI, and license() for information.        |\nJust a \"proof of concept\"; I can write an appropriate shell script for your debugging purpose once I've found the relevant ticket... ;-)",
    "created_at": "2011-08-21T06:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4986#issuecomment-38034",
    "user": "@nexttime"
}
```

Replying to [comment:7 kcrisman]:
> Ditto.

Re: sage-devel thread: I was wondering what you were waiting for.

(Haven't tested the patch here; I think you won't be able to print PARI's variables with this method anyway, at least not easily.)

Note that you can inject code into the C files generated by Cython, e.g. with your favourite friend `sed`, especially into the functions called upon module initialization:

```sh
$ cd devel/sage/sage/rings
$ sed -i -e '/^PyMODINIT_FUNC PyInit_.*(void)$/,+3s/^{$/{\n  printf("Hello!\\n");\n/' real_mpfr.c
$ ../../../../sage -br
----------------------------------------------------------
sage: Building and installing modified Sage library files.
...
building 'sage.rings.real_mpfr' extension
Execute 1 commands (using 1 threads)
...
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Hello!
sage: 
```

(This example is of course quite specific to the current layout of the C code generated by Cython. Also, for simplicity I've used the less portable `-i` option.)
| Sage Version 4.7.2.alpha1, Release Date: 2011-08-17                |
| Type notebook() for the GUI, and license() for information.        |
Just a "proof of concept"; I can write an appropriate shell script for your debugging purpose once I've found the relevant ticket... ;-)
