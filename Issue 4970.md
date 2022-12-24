# Issue 4970: modify tkinter detection in our python spkg so that it works on macs

archive/issues_004970.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  dunfield\n\nThis is from a sage-support thread:\n\n```\nHi Michael\n\nthanks a lot! Tkinter is now working fine for me and I can use\nmatplotlib with the TkAgg backend\nFor the record, here are the steps I followed to get it working on Mac\nOS (10.4 and 10.5)\n1) Download the Tcl/Tk sources\n2) Compile the unix version (of Tcl and Tk) as follows\n./configure --enable-framework --disable-xft, make, make install\n3) Modify the setup.py file in the src directory of python-2.5.2.p8 by\nputting\n/System/Library  underneath /Library/Frameworks at the top the\nfunction detect_tkinter_darwin\n4) run ./spkg-install in python-2.5.2.p8\n5) reinstall matplotlib: sage -f matplotlib-0.98.3.p4\n\nAs this is the way Apple recommends to do it in the developer\ndocumentation. I suggest that\nthe fix in the function detect_tkinter_darwin of the python-2.5.2.p8\nsetup.py gets included in the official Sage release. People needing\nTkinter on mac would then just need to have Tcl/Tk without\nxft installed before compiling Sage.\n\nBest wishes and thanks for the great job you are doing with the Sage\ndevelopers and maintainers,\nEric\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4970\n\n",
    "created_at": "2009-01-13T14:12:13Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "modify tkinter detection in our python spkg so that it works on macs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4970",
    "user": "was"
}
```
Assignee: mabshoff

CC:  dunfield

This is from a sage-support thread:

```
Hi Michael

thanks a lot! Tkinter is now working fine for me and I can use
matplotlib with the TkAgg backend
For the record, here are the steps I followed to get it working on Mac
OS (10.4 and 10.5)
1) Download the Tcl/Tk sources
2) Compile the unix version (of Tcl and Tk) as follows
./configure --enable-framework --disable-xft, make, make install
3) Modify the setup.py file in the src directory of python-2.5.2.p8 by
putting
/System/Library  underneath /Library/Frameworks at the top the
function detect_tkinter_darwin
4) run ./spkg-install in python-2.5.2.p8
5) reinstall matplotlib: sage -f matplotlib-0.98.3.p4

As this is the way Apple recommends to do it in the developer
documentation. I suggest that
the fix in the function detect_tkinter_darwin of the python-2.5.2.p8
setup.py gets included in the official Sage release. People needing
Tkinter on mac would then just need to have Tcl/Tk without
xft installed before compiling Sage.

Best wishes and thanks for the great job you are doing with the Sage
developers and maintainers,
Eric
```


Issue created by migration from https://trac.sagemath.org/ticket/4970





---

archive/issue_comments_037850.json:
```json
{
    "body": "I will do this during the upgrade to Python 2.5.4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-13T17:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4970#issuecomment-37850",
    "user": "mabshoff"
}
```

I will do this during the upgrade to Python 2.5.4.

Cheers,

Michael



---

archive/issue_comments_037851.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> I will do this during the upgrade to Python 2.5.4.\n\nI did not do this in the python-2.5.4.spkg update since we have for now disabled support of TkAgg in MPL since it caused exceptions in the plotting code on systems where no X was installed and/or not running. We can resolve this problem in two ways:\n\n* conditionally reenable TkAgg support in MPL\n* fix the issue in MPL or at least catch the exception and just ignore it\n \n> Cheers,\n> \n> Michael\n\nAnyway, I am attaching a patch on top of the python-2.5.4.spkg that can be used as the basis to make this happen on OSX once we sorted out the TkAgg issue.\n\nBumping to 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T06:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4970#issuecomment-37851",
    "user": "mabshoff"
}
```

Replying to [comment:1 mabshoff]:
> I will do this during the upgrade to Python 2.5.4.

I did not do this in the python-2.5.4.spkg update since we have for now disabled support of TkAgg in MPL since it caused exceptions in the plotting code on systems where no X was installed and/or not running. We can resolve this problem in two ways:

* conditionally reenable TkAgg support in MPL
* fix the issue in MPL or at least catch the exception and just ignore it
 
> Cheers,
> 
> Michael

Anyway, I am attaching a patch on top of the python-2.5.4.spkg that can be used as the basis to make this happen on OSX once we sorted out the TkAgg issue.

Bumping to 3.4.1.

Cheers,

Michael



---

archive/issue_comments_037852.json:
```json
{
    "body": "Attachment [trac_4970-potential-fix.patch](tarball://root/attachments/some-uuid/ticket4970/trac_4970-potential-fix.patch) by mabshoff created at 2009-02-16 06:26:01",
    "created_at": "2009-02-16T06:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4970#issuecomment-37852",
    "user": "mabshoff"
}
```

Attachment [trac_4970-potential-fix.patch](tarball://root/attachments/some-uuid/ticket4970/trac_4970-potential-fix.patch) by mabshoff created at 2009-02-16 06:26:01



---

archive/issue_comments_037853.json:
```json
{
    "body": "trac_4970-potential-fix.patch is an untested prototype patch. Given that we fixed the libpng problem which triggered all this in the first place we might not even need any of the above modifications. \n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T06:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4970#issuecomment-37853",
    "user": "mabshoff"
}
```

trac_4970-potential-fix.patch is an untested prototype patch. Given that we fixed the libpng problem which triggered all this in the first place we might not even need any of the above modifications. 

Cheers,

Michael



---

archive/issue_comments_037854.json:
```json
{
    "body": "As of January 2015, Tkinter works out-of-the box on OS X with any recent source or binary release of Sage, so the patch here isn't needed anymore.",
    "created_at": "2015-01-06T13:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4970#issuecomment-37854",
    "user": "dunfield"
}
```

As of January 2015, Tkinter works out-of-the box on OS X with any recent source or binary release of Sage, so the patch here isn't needed anymore.



---

archive/issue_comments_037855.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2015-01-07T15:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4970#issuecomment-37855",
    "user": "dunfield"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_037856.json:
```json
{
    "body": "Changing assignee from mabshoff to dunfield.",
    "created_at": "2015-01-07T15:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4970#issuecomment-37856",
    "user": "dunfield"
}
```

Changing assignee from mabshoff to dunfield.



---

archive/issue_comments_037857.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-01-13T01:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4970#issuecomment-37857",
    "user": "vbraun"
}
```

Resolution: fixed
