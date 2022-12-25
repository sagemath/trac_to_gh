# Issue 1474: gap -- port to Itanium Linux

archive/issues_001474.json:
```json
{
    "body": "Assignee: @williamstein\n\nProblem: GAP totally fails to build with -O2 (the default).  With\n-O0 it builds and works, but is very very very slow, for the reasons\ndiscussed below.  I'm trying to find somebody who can\nhelp with this.  The bottom email below from Steve Linton explains\nwhat needs to be done.  If anybody wants to work on this, let me know\n(wstein`@`gmail.com). \n\n\n```\n> > >   (1) What's the latest status of this question?\n> >\n> > No change.\n> >\n> > >   (2) Is there any hope?\n> >\n> > Yes. It needs a C programmer who can manage a few lines of in-line assembler\n> > with GCC, an Itanium to test it on and about 30 lines of code.\n> > If it acquired a high enough priority I would do it, but I can't hope to do it\n> > this month or next. I can explain what is needed about GAP in an email if you\n> > have a C programmer.\n\n(see below for what is needed)\n\n>\n> > >   (3) Who should I talk to?\n> > >\n> > Me.\n>\n> Excellent.\n>\n> > > Would giving a certain GAP developer a temporary account on an Itanium\n> > > machine help?  It's possible that this could be arranged.\n> > >\n> >\n> > There aren't many of that are happy doing fiddly C work of this kind. I can\n> > see if anyone wants to try.\n>\n> Thanks.  There are actually a lot of Itaniums at supercomputing centers\n> in the US, for some reason.\n>\n\n```\n\n\n\n\n```\nSteve Linton to me\n\t\n\t\nOK. The issue is with garbage collection. The GAP garbage collector looks for\nany C local variable which appears to contain a reference to a GAP object. If\nit finds one it assumes that it is a reference and keeps the object in\nquestion alive. This is done in GenStackFuncBags in gasman.c. There is\nrelevant documentation about line 1474 and the code is at line 1667. A\ncollection of horrible, but surprisingly portable hacks are used to find and\nscan all the C local variables on the stack and in the registers.\n\nThe problems on Itanium are that an Itanium has two stacks. One is used\nfor local variables, return addresses, etc. in the usual way. The other is used\nwhen the register file overflows.\n\nSo what is needed is a few lines of assembler to\n\n1) force the whole register file to be flushed onto this stack\n(SparcStackFuncBags does this on Sparc)\n\n2) find the top and botom of this stack so that it can be scanned.\n\nIt all works with -O0 because nothing is then kept in registers that is not\nalso on the main stack, but this is cripplingly slow.\n\nIf someone can come up with the assembler and the necessary wrapper to include\nit in gasman.c I can trivially adjust the C code to call it and then scan both\nstacks.\n\n       Steve\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1474\n\n",
    "created_at": "2007-12-12T13:13:43Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "gap -- port to Itanium Linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1474",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Problem: GAP totally fails to build with -O2 (the default).  With
-O0 it builds and works, but is very very very slow, for the reasons
discussed below.  I'm trying to find somebody who can
help with this.  The bottom email below from Steve Linton explains
what needs to be done.  If anybody wants to work on this, let me know
(wstein`@`gmail.com). 


```
> > >   (1) What's the latest status of this question?
> >
> > No change.
> >
> > >   (2) Is there any hope?
> >
> > Yes. It needs a C programmer who can manage a few lines of in-line assembler
> > with GCC, an Itanium to test it on and about 30 lines of code.
> > If it acquired a high enough priority I would do it, but I can't hope to do it
> > this month or next. I can explain what is needed about GAP in an email if you
> > have a C programmer.

(see below for what is needed)

>
> > >   (3) Who should I talk to?
> > >
> > Me.
>
> Excellent.
>
> > > Would giving a certain GAP developer a temporary account on an Itanium
> > > machine help?  It's possible that this could be arranged.
> > >
> >
> > There aren't many of that are happy doing fiddly C work of this kind. I can
> > see if anyone wants to try.
>
> Thanks.  There are actually a lot of Itaniums at supercomputing centers
> in the US, for some reason.
>

```




```
Steve Linton to me
	
	
OK. The issue is with garbage collection. The GAP garbage collector looks for
any C local variable which appears to contain a reference to a GAP object. If
it finds one it assumes that it is a reference and keeps the object in
question alive. This is done in GenStackFuncBags in gasman.c. There is
relevant documentation about line 1474 and the code is at line 1667. A
collection of horrible, but surprisingly portable hacks are used to find and
scan all the C local variables on the stack and in the registers.

The problems on Itanium are that an Itanium has two stacks. One is used
for local variables, return addresses, etc. in the usual way. The other is used
when the register file overflows.

So what is needed is a few lines of assembler to

1) force the whole register file to be flushed onto this stack
(SparcStackFuncBags does this on Sparc)

2) find the top and botom of this stack so that it can be scanned.

It all works with -O0 because nothing is then kept in registers that is not
also on the main stack, but this is cripplingly slow.

If someone can come up with the assembler and the necessary wrapper to include
it in gasman.c I can trivially adjust the C code to call it and then scan both
stacks.

       Steve
```


Issue created by migration from https://trac.sagemath.org/ticket/1474





---

archive/issue_comments_009461.json:
```json
{
    "body": "See fwd message on sage-devel:\n\n\n\n```\nDear GAP Forum,\n\nAs some of you will recall, there is a very long standing\nproblem running GAP on processors from Intel's Itanium processor family, found\nmainly in large multi-processor servers and supercomputers.\n\nWe believe that we have now fixed this problem, and the fix will be included\nin the next release of GAP, but, if you wish to try it out in the meantime,\nyou can download it as a patch to apply to GAP 4r4p10. See\nhttp://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html\nfor a link to the patch.\n\nPlease let us know how you get on.\n\n\tSteve Linton\n```\n",
    "created_at": "2008-02-14T17:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1474#issuecomment-9461",
    "user": "https://github.com/jaapspies"
}
```

See fwd message on sage-devel:



```
Dear GAP Forum,

As some of you will recall, there is a very long standing
problem running GAP on processors from Intel's Itanium processor family, found
mainly in large multi-processor servers and supercomputers.

We believe that we have now fixed this problem, and the fix will be included
in the next release of GAP, but, if you wish to try it out in the meantime,
you can download it as a patch to apply to GAP 4r4p10. See
http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html
for a link to the patch.

Please let us know how you get on.

	Steve Linton
```




---

archive/issue_comments_009462.json:
```json
{
    "body": "William did try the updated sources yesterday and they segfaulted on his Itanium test box :(\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T17:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1474#issuecomment-9462",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

William did try the updated sources yesterday and they segfaulted on his Itanium test box :(

Cheers,

Michael



---

archive/issue_events_001625.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2008-02-19T15:29:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1474",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1474#event-1625"
}
```



---

archive/issue_comments_009463.json:
```json
{
    "body": "Steve Linton did this :-)\n\nhttp://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html\n\nNow putting it into sage: #2209",
    "created_at": "2008-02-19T15:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1474#issuecomment-9463",
    "user": "https://github.com/williamstein"
}
```

Steve Linton did this :-)

http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html

Now putting it into sage: #2209



---

archive/issue_comments_009464.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-19T15:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1474#issuecomment-9464",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
