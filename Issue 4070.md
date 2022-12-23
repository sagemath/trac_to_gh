# Issue 4070: [with spkg, patch: needs review] fix polybori-0.5.rc1 build issues

archive/issues_004070.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc1/polybori-0.5rc.p3.spkg\n\nfixes a couple issues:\n\n* delete dynamic libs so that the extension is linked statically\n* touch the pbori.pyx extension so that it forces a rebuild\n\nThe attached patch also disables m4ri_destroy_all_codes() in pbori.pyx since it causes double frees on OSX. This is maybe related to #1611.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4070\n\n",
    "created_at": "2008-09-07T17:22:52Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "[with spkg, patch: needs review] fix polybori-0.5.rc1 build issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4070",
    "user": "mabshoff"
}
```
Assignee: mabshoff

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc1/polybori-0.5rc.p3.spkg

fixes a couple issues:

* delete dynamic libs so that the extension is linked statically
* touch the pbori.pyx extension so that it forces a rebuild

The attached patch also disables m4ri_destroy_all_codes() in pbori.pyx since it causes double frees on OSX. This is maybe related to #1611.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4070





---

archive/issue_comments_029372.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-07T17:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4070#issuecomment-29372",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029373.json:
```json
{
    "body": "Attachment\n\nBuilds fine on:\n* x86_64, Core2Duo, Debian GNU/Linux testing (my notebook)\n* x86_64, Opteron, Ubuntu (my desktop)\n* x86_64, Opteron, Debian GNU/Linux testing (my server at RHUL)\n* x86_64, Opteron, Debian GNU/Linux stable (**sage.math**)\n* x86_64, 2xCore2Duo, Fedora 8 (**eno**)\n\nStrictly speaking, `libs/polybori/decl.pxi` should be touched instead of `rings/polynomial/pbori.pyx` but this isn't a show stopper for now, since only one module links against PolyBoRi anyway (i.e. `rings.polynomialpbori`)",
    "created_at": "2008-09-07T18:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4070#issuecomment-29373",
    "user": "malb"
}
```

Attachment

Builds fine on:
* x86_64, Core2Duo, Debian GNU/Linux testing (my notebook)
* x86_64, Opteron, Ubuntu (my desktop)
* x86_64, Opteron, Debian GNU/Linux testing (my server at RHUL)
* x86_64, Opteron, Debian GNU/Linux stable (**sage.math**)
* x86_64, 2xCore2Duo, Fedora 8 (**eno**)

Strictly speaking, `libs/polybori/decl.pxi` should be touched instead of `rings/polynomial/pbori.pyx` but this isn't a show stopper for now, since only one module links against PolyBoRi anyway (i.e. `rings.polynomialpbori`)



---

archive/issue_comments_029374.json:
```json
{
    "body": "\n```\n[18:20] <mabshoff> #4070, patch will be in a second.\n[18:20] <mabshoff> There are odd issues in matrix2.pyx on OSX only where there are issues with Matrix inversion.\n[18:22] <mabshoff> patch is also up now.\n[18:22] <mabshoff> You need that one to fix an issue once the spkg is updated.\n[18:39] <mhansen> #4070 fixes the issues for me.\n```\n",
    "created_at": "2008-09-07T18:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4070#issuecomment-29374",
    "user": "malb"
}
```


```
[18:20] <mabshoff> #4070, patch will be in a second.
[18:20] <mabshoff> There are odd issues in matrix2.pyx on OSX only where there are issues with Matrix inversion.
[18:22] <mabshoff> patch is also up now.
[18:22] <mabshoff> You need that one to fix an issue once the spkg is updated.
[18:39] <mhansen> #4070 fixes the issues for me.
```




---

archive/issue_comments_029375.json:
```json
{
    "body": "The SPKG also passed manual inspection (everything checked in properly, stuff is documented, etc.) Running doctests on the mentioned machines now.",
    "created_at": "2008-09-07T18:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4070#issuecomment-29375",
    "user": "malb"
}
```

The SPKG also passed manual inspection (everything checked in properly, stuff is documented, etc.) Running doctests on the mentioned machines now.



---

archive/issue_comments_029376.json:
```json
{
    "body": "## Doctests\n### x86_64, Core2Duo, Debian GNU/Linux testing (my notebook)\n\n```\nThe following tests failed:\n\n        sage -t  devel/sage/sage/interfaces/sage0.py # 8 doctests failed\n```\n\n### x86_64, Opteron, Ubuntu (my desktop)\n\na lot of segmentation faults, `sage -ba`ing now, might be local problem.\n\n### x86_64, Opteron, Debian GNU/Linux testing (my server at RHUL)\n\npass\n\n### x86_64, Opteron, Debian GNU/Linux stable (sage.math)\n\npass\n\n### x86_64, 2xCore2Duo, Fedora 8 (eno)\n\npass",
    "created_at": "2008-09-07T18:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4070#issuecomment-29376",
    "user": "malb"
}
```

## Doctests
### x86_64, Core2Duo, Debian GNU/Linux testing (my notebook)

```
The following tests failed:

        sage -t  devel/sage/sage/interfaces/sage0.py # 8 doctests failed
```

### x86_64, Opteron, Ubuntu (my desktop)

a lot of segmentation faults, `sage -ba`ing now, might be local problem.

### x86_64, Opteron, Debian GNU/Linux testing (my server at RHUL)

pass

### x86_64, Opteron, Debian GNU/Linux stable (sage.math)

pass

### x86_64, 2xCore2Duo, Fedora 8 (eno)

pass



---

archive/issue_comments_029377.json:
```json
{
    "body": "After a `sage -ba` everything is fine on my Desktop.",
    "created_at": "2008-09-07T20:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4070#issuecomment-29377",
    "user": "malb"
}
```

After a `sage -ba` everything is fine on my Desktop.



---

archive/issue_comments_029378.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-07T23:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4070#issuecomment-29378",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029379.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-07T23:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4070#issuecomment-29379",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1
