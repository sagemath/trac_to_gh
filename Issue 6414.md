# Issue 6414: OS X binaries should issue a better warning on incompatible CPUs

archive/issues_006414.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  dimpase\n\nCurrently, every now and then a user reports on sage-support, that he got an error message like\n\n```\n/Applications/sage-4.0.1-OSX10.5-PowerPC-PowerMacintosh-Darwin/sage/\nlocal/bin/sage-sage: line 198:   407 Illegal instruction     sage-\nipython \"$@\" -i\n```\n\nThis is e.g. the case if a Sage binary built on a MacPPC with a G5 processor (typically the one the OS X 10.5 bdist is created on) is used on a MacPPC with only a G4 processor.\n\nFor the *nix world on Intel/AMD processors, the sage-flags.txt file was created for just the purpose to check whether the CPU is sufficient, to let a certain Sage binary run.\n\nWe seem to need something in that direction for OS X, too (though momentarily only for the PPC processors, not the Intel ones).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6414\n\n",
    "created_at": "2009-06-25T20:41:50Z",
    "labels": [
        "distribution",
        "minor",
        "enhancement"
    ],
    "title": "OS X binaries should issue a better warning on incompatible CPUs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6414",
    "user": "GeorgSWeber"
}
```
Assignee: tbd

CC:  dimpase

Currently, every now and then a user reports on sage-support, that he got an error message like

```
/Applications/sage-4.0.1-OSX10.5-PowerPC-PowerMacintosh-Darwin/sage/
local/bin/sage-sage: line 198:   407 Illegal instruction     sage-
ipython "$@" -i
```

This is e.g. the case if a Sage binary built on a MacPPC with a G5 processor (typically the one the OS X 10.5 bdist is created on) is used on a MacPPC with only a G4 processor.

For the *nix world on Intel/AMD processors, the sage-flags.txt file was created for just the purpose to check whether the CPU is sufficient, to let a certain Sage binary run.

We seem to need something in that direction for OS X, too (though momentarily only for the PPC processors, not the Intel ones).


Issue created by migration from https://trac.sagemath.org/ticket/6414





---

archive/issue_comments_051496.json:
```json
{
    "body": "Is this still an issue with the new checks for moving OSX etc?",
    "created_at": "2010-05-26T20:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51496",
    "user": "kcrisman"
}
```

Is this still an issue with the new checks for moving OSX etc?



---

archive/issue_comments_051497.json:
```json
{
    "body": "This is essentially the same as #5950, except newer and with a little more info, so I'm keeping it.  Both of these should be addressed, I guess.  From #5950:\n\n> -bdist should add something analog to the SSE flags on Linux so that if someone tried to run a ppc build on an x86 it aborts with a sane error message instead of just blowing up.",
    "created_at": "2015-01-05T16:08:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51497",
    "user": "kcrisman"
}
```

This is essentially the same as #5950, except newer and with a little more info, so I'm keeping it.  Both of these should be addressed, I guess.  From #5950:

> -bdist should add something analog to the SSE flags on Linux so that if someone tried to run a ppc build on an x86 it aborts with a sane error message instead of just blowing up.



---

archive/issue_comments_051498.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-04-11T09:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51498",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051499.json:
```json
{
    "body": "There should be no warning needed, the binaries should be produced to run on any CPU.",
    "created_at": "2016-04-11T09:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51499",
    "user": "jdemeyer"
}
```

There should be no warning needed, the binaries should be produced to run on any CPU.



---

archive/issue_comments_051500.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-04-11T09:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51500",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051501.json:
```json
{
    "body": "> There should be no warning needed, the binaries should be produced to run on any CPU.\n? That doesn't really work on OS X all the time, we have seen many error messages on ask.sagemath for this for different instruction sets.",
    "created_at": "2016-04-11T14:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51501",
    "user": "kcrisman"
}
```

> There should be no warning needed, the binaries should be produced to run on any CPU.
? That doesn't really work on OS X all the time, we have seen many error messages on ask.sagemath for this for different instruction sets.



---

archive/issue_comments_051502.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2016-04-11T14:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51502",
    "user": "kcrisman"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_051503.json:
```json
{
    "body": "(By which I mean to say this isn't just a PPC/Intel issue.)",
    "created_at": "2016-04-11T14:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51503",
    "user": "kcrisman"
}
```

(By which I mean to say this isn't just a PPC/Intel issue.)



---

archive/issue_comments_051504.json:
```json
{
    "body": "it does not work all the time because of problems in the building process (forgetting to set proper flags), or perhaps toolchain bugs, or both, I don't really know. \n\nSAGE_FAT_BINARY cooked with wrong FAT... :-)",
    "created_at": "2016-04-11T15:10:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51504",
    "user": "dimpase"
}
```

it does not work all the time because of problems in the building process (forgetting to set proper flags), or perhaps toolchain bugs, or both, I don't really know. 

SAGE_FAT_BINARY cooked with wrong FAT... :-)



---

archive/issue_comments_051505.json:
```json
{
    "body": "Replying to [comment:8 dimpase]:\n> it does not work all the time because of problems in the building process (forgetting to set proper flags), or perhaps toolchain bugs, or both, I don't really know.\n\nI haven't heard of any such bug recently. In any case, such things should be fixed on a case-by-case basis, I don't think that there is a general fix possible. So I still think that this ticket should be closed.",
    "created_at": "2016-04-11T17:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51505",
    "user": "jdemeyer"
}
```

Replying to [comment:8 dimpase]:
> it does not work all the time because of problems in the building process (forgetting to set proper flags), or perhaps toolchain bugs, or both, I don't really know.

I haven't heard of any such bug recently. In any case, such things should be fixed on a case-by-case basis, I don't think that there is a general fix possible. So I still think that this ticket should be closed.



---

archive/issue_comments_051506.json:
```json
{
    "body": "Replying to [comment:9 jdemeyer]:\n> Replying to [comment:8 dimpase]:\n> > it does not work all the time because of problems in the building process (forgetting to set proper flags), or perhaps toolchain bugs, or both, I don't really know.\n> \n> I haven't heard of any such bug recently.\ncertainly with 6.9 binaries it is the case (e.g. reported  [today on sage-support](https://groups.google.com/d/msg/sage-support/C1eENI3yrtw/b5ChRoJkAQAJ)). There were also very entertaining bugs like this reported by someone with a Mac box having a non-standard (upgraded?) CPU... \nDon't recall about 7.1/2 right now. \n\nBy the way: [faq-usage](http://doc.sagemath.org/html/en/faq/faq-usage.html#i-downloaded-a-sage-binary-and-it-crashes-on-startup-with-illegal-instruction-what-can-i-do) says: **Nobody has yet figured out how to build Sage in such a way that MPIR and ATLAS work on all hardware.**\n\n\n> In any case, such things should be fixed on a case-by-case basis, I don't think that there is a general fix possible. So I still think that this ticket should be closed.",
    "created_at": "2016-04-11T23:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51506",
    "user": "dimpase"
}
```

Replying to [comment:9 jdemeyer]:
> Replying to [comment:8 dimpase]:
> > it does not work all the time because of problems in the building process (forgetting to set proper flags), or perhaps toolchain bugs, or both, I don't really know.
> 
> I haven't heard of any such bug recently.
certainly with 6.9 binaries it is the case (e.g. reported  [today on sage-support](https://groups.google.com/d/msg/sage-support/C1eENI3yrtw/b5ChRoJkAQAJ)). There were also very entertaining bugs like this reported by someone with a Mac box having a non-standard (upgraded?) CPU... 
Don't recall about 7.1/2 right now. 

By the way: [faq-usage](http://doc.sagemath.org/html/en/faq/faq-usage.html#i-downloaded-a-sage-binary-and-it-crashes-on-startup-with-illegal-instruction-what-can-i-do) says: **Nobody has yet figured out how to build Sage in such a way that MPIR and ATLAS work on all hardware.**


> In any case, such things should be fixed on a case-by-case basis, I don't think that there is a general fix possible. So I still think that this ticket should be closed.



---

archive/issue_comments_051507.json:
```json
{
    "body": "OK, then let's close this ticket not as \"worksforme\" but as \"invalid\" because it's too general.",
    "created_at": "2016-04-12T07:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51507",
    "user": "jdemeyer"
}
```

OK, then let's close this ticket not as "worksforme" but as "invalid" because it's too general.



---

archive/issue_comments_051508.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2016-04-12T07:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51508",
    "user": "jdemeyer"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_051509.json:
```json
{
    "body": "That seems like a good compromise.",
    "created_at": "2016-04-12T12:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51509",
    "user": "kcrisman"
}
```

That seems like a good compromise.



---

archive/issue_comments_051510.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6414#issuecomment-51510",
    "user": "vbraun"
}
```

Resolution: fixed
