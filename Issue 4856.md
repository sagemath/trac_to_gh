# Issue 4856: [with patch; needs review] make qasm an optional spkg

archive/issues_004856.json:
```json
{
    "body": "Assignee: mabshoff\n\nSee attached spkg.  This came up at \n\n  http://groups.google.com/group/sage-devel/browse_thread/thread/175e8f515e58d497\n\nIt might be a good example of something, so maybe should become an optional spkg...   It's pretty specialized and very small. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4856\n\n",
    "created_at": "2008-12-23T07:45:22Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch; needs review] make qasm an optional spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4856",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

See attached spkg.  This came up at 

  http://groups.google.com/group/sage-devel/browse_thread/thread/175e8f515e58d497

It might be a good example of something, so maybe should become an optional spkg...   It's pretty specialized and very small. 

Issue created by migration from https://trac.sagemath.org/ticket/4856





---

archive/issue_comments_036734.json:
```json
{
    "body": "Attachment [qasm-1.4.spkg](tarball://root/attachments/some-uuid/ticket4856/qasm-1.4.spkg) by @williamstein created at 2008-12-23 07:45:37",
    "created_at": "2008-12-23T07:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4856#issuecomment-36734",
    "user": "https://github.com/williamstein"
}
```

Attachment [qasm-1.4.spkg](tarball://root/attachments/some-uuid/ticket4856/qasm-1.4.spkg) by @williamstein created at 2008-12-23 07:45:37



---

archive/issue_comments_036735.json:
```json
{
    "body": "This ticket needs work in several areas:\n\n* SPKG.txt is not up to current standards, see http://wiki.sagemath.org/spkgTemplate\n\n* spkg-install is not up to current standards, see http://wiki.sagemath.org/SPKG_Audit resp. trac ticket #633 --- adding a check for SAGE_LOCAL to be non-empty is a blocker IMHO\n\n* The spkg-install says:\n\n```\n    echo \"You must make sure the dvipng program is available on your system.\"\n    echo \"You might be able to install the dvipng program listed in the\"\n    echo \"output of 'sage -optional'.  If that doesn't work, just use whatever\"\n    echo \"is offered by your operating system.\"\n    exit 1\n```\n\nbut in the discussion on sage-devel (link above) it is said:\n\n```\nDo not install that dvipng spkg.  You *MUST* install dvipng instead\nusing whatever method your operating system provides (e.g., rpm, deb,\netc.).  It's a completely standard linux program.  The Sage dvipng\nspkg will be deleted soon, since it doesn't make sense for us to be\nhosting it.\n\n -- William \n```\n\n\n* (optional) the qasm.py would benefit from a doctest, the addition of some kind of example could easily be turned into a working spkg-check script",
    "created_at": "2009-01-02T09:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4856#issuecomment-36735",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

This ticket needs work in several areas:

* SPKG.txt is not up to current standards, see http://wiki.sagemath.org/spkgTemplate

* spkg-install is not up to current standards, see http://wiki.sagemath.org/SPKG_Audit resp. trac ticket #633 --- adding a check for SAGE_LOCAL to be non-empty is a blocker IMHO

* The spkg-install says:

```
    echo "You must make sure the dvipng program is available on your system."
    echo "You might be able to install the dvipng program listed in the"
    echo "output of 'sage -optional'.  If that doesn't work, just use whatever"
    echo "is offered by your operating system."
    exit 1
```

but in the discussion on sage-devel (link above) it is said:

```
Do not install that dvipng spkg.  You *MUST* install dvipng instead
using whatever method your operating system provides (e.g., rpm, deb,
etc.).  It's a completely standard linux program.  The Sage dvipng
spkg will be deleted soon, since it doesn't make sense for us to be
hosting it.

 -- William 
```


* (optional) the qasm.py would benefit from a doctest, the addition of some kind of example could easily be turned into a working spkg-check script



---

archive/issue_comments_036736.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-01-02T15:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4856#issuecomment-36736",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix



---

archive/issue_comments_036737.json:
```json
{
    "body": ">  adding a check for SAGE_LOCAL to be non-empty is a blocker IMHO\n\nI've always considered that SAGE_LOCAL thing pointless.\n\nAnyway, upon further reflection, and given the lack of response by anybody in the community related to qasm, I think this is way too specialized to be an official optional spkg.  I'm thus closing this ticket.",
    "created_at": "2009-01-02T15:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4856#issuecomment-36737",
    "user": "https://github.com/williamstein"
}
```

>  adding a check for SAGE_LOCAL to be non-empty is a blocker IMHO

I've always considered that SAGE_LOCAL thing pointless.

Anyway, upon further reflection, and given the lack of response by anybody in the community related to qasm, I think this is way too specialized to be an official optional spkg.  I'm thus closing this ticket.



---

archive/issue_comments_036738.json:
```json
{
    "body": "Replying to [comment:3 was]:\n> >  adding a check for SAGE_LOCAL to be non-empty is a blocker IMHO\n> \n> I've always considered that SAGE_LOCAL thing pointless.\n> \n\nNot if you run spkg-install from the command line to debug things.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-02T15:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4856#issuecomment-36738",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 was]:
> >  adding a check for SAGE_LOCAL to be non-empty is a blocker IMHO
> 
> I've always considered that SAGE_LOCAL thing pointless.
> 

Not if you run spkg-install from the command line to debug things.

Cheers,

Michael
