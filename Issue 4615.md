# Issue 4615: [with spkg, needs review] Make boehm_gc a standard spkg

archive/issues_004615.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is part of the project to replace clisp by ecl. The vote was at\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/450bb51e12fab1aa\n\nSince it is already an optional spkg all that needs to be done is to patch deps and so on. Maxima should depend on boehm_gc.\n\nThe spkg is at\n\nhttp://sagemath.org/packages/optional/boehm_gc-7.1.p0.spkg\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4615\n\n",
    "created_at": "2008-11-25T11:49:34Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with spkg, needs review] Make boehm_gc a standard spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4615",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This is part of the project to replace clisp by ecl. The vote was at

http://groups.google.com/group/sage-devel/browse_thread/thread/450bb51e12fab1aa

Since it is already an optional spkg all that needs to be done is to patch deps and so on. Maxima should depend on boehm_gc.

The spkg is at

http://sagemath.org/packages/optional/boehm_gc-7.1.p0.spkg

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4615





---

archive/issue_comments_034643.json:
```json
{
    "body": "REFEREE:\n\nI confirmed that src exactly equals upstream from http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/\n\nI checked that the package installs on OS X, and that the spkg-install, etc., looks good.  It took 44 seconds to build on my OS X box, which isn't too bad.\n\nThis gets positive review, though of course deps and install must be modified.  Add this to install:\n\n\n```\nBOEHM_GC=`$newest boehm_gc`\nexport BOEHM_GC\n```\n\n\nModify deps by adding/changing:\n\n```\n$(INST)/$(BOEHM_GC): $(BASE)\n\t$(SAGE_SPKG) $(BOEHM_GC) 2>&1\n```\n\n\nBoehm is *not* a dependency for Maxima as the ticket description says.  Instead Boehm should be made a dependency for ECL when that is added, and then Maxima depends on ECL.",
    "created_at": "2008-11-27T17:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4615#issuecomment-34643",
    "user": "@williamstein"
}
```

REFEREE:

I confirmed that src exactly equals upstream from http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/

I checked that the package installs on OS X, and that the spkg-install, etc., looks good.  It took 44 seconds to build on my OS X box, which isn't too bad.

This gets positive review, though of course deps and install must be modified.  Add this to install:


```
BOEHM_GC=`$newest boehm_gc`
export BOEHM_GC
```


Modify deps by adding/changing:

```
$(INST)/$(BOEHM_GC): $(BASE)
	$(SAGE_SPKG) $(BOEHM_GC) 2>&1
```


Boehm is *not* a dependency for Maxima as the ticket description says.  Instead Boehm should be made a dependency for ECL when that is added, and then Maxima depends on ECL.



---

archive/issue_comments_034644.json:
```json
{
    "body": "Yes, it is technically correct that ecl will depend on boehm, but making Maxima depend on it wouldn't hurt anybody.\n\nOne thing missing from William's remarks about deps is that additionally `$(INST)/$(BOEHM_GC)` needs to be added to the `all` target in deps.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T07:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4615#issuecomment-34644",
    "user": "mabshoff"
}
```

Yes, it is technically correct that ecl will depend on boehm, but making Maxima depend on it wouldn't hurt anybody.

One thing missing from William's remarks about deps is that additionally `$(INST)/$(BOEHM_GC)` needs to be added to the `all` target in deps.

Cheers,

Michael



---

archive/issue_comments_034645.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-29T07:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4615#issuecomment-34645",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034646.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0",
    "created_at": "2008-11-29T07:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4615#issuecomment-34646",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc0
