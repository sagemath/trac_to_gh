# Issue 1209: make it so maple.gcd?? shows source code

archive/issues_001209.json:
```json
{
    "body": "Assignee: was\n\n\n```\nOn Nov 19, 2007 8:29 AM, Jason Grout <jason-sage@creativetrax.com> wrote:\n> \n> William Stein wrote:\n> \n> >  3. Dumb question -- Where is the actual source code of anything in Maple?\n> >      I'm skimming through my Maple install to see some actual source code and\n> >      I can't find anything.  The lib/ directory has lots of .mla\n> > files, but these are all\n> >      pre-compiled binary files -- no source code.  Is there some tool\n> > included with\n> >      Maple to decompile them?     (I'm not being rhetorical, I simply don't know\n> >      how to actually view source code of Maple functions, even if I wanted to.)\n> \n> Some links dealing with this:\n> \n> http://www.mapleprimes.com/blog/jacquesc/old-timer-techniques\n> \n> http://www.mapleprimes.com/forum/algorithms-used-in-maple\n> \n> http://thproxy.jinr.ru/Documents/MapleV/qa/section3_4.html\n> \n> I've used the printlevel and I think the showstat techniques before.\n> Unfortunately, I can't test them because I no longer have access to\n> Maple (at least on my home machine).  I guess that's they whole point\n> again---even if there is some way for someone to get the output of the\n> procedure, it doesn't do me any good because I don't have Maple and\n> can't check it anyway.\n\nThis *does* work in Maple 11:\n\nsage: maple_console()\n    |\\^/|     Maple 11 (APPLE UNIVERSAL OSX)\n._|\\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple Inc. 2007\n \\  MAPLE  /  All rights reserved. Maple is a trademark of\n <____ ____>  Waterloo Maple Inc.\n      |       Type ? for help.\n> print(gcd);\n                                  proc(aa, bb, cofa::name, cofb::name)  ...  end proc\n\n> interface(verboseproc=2);\n                                                           1\n\n> print(gcd);              \nproc(aa, bb, cofa::name, cofb::name)\nlocal Z, GCD, a, b;\noption `Copyright (c) 1992 by the University of Waterloo. All rights reserved.`;\n    if 2 < nargs and member(cofa, indets(aa) union indets(bb)) then error \"The optional 3rd argument given to `\\\n...\n\nI wonder what proportion of the 1300 or so top-level functions in Maple (according\nto a sage's maple.[tab]) actually have source code.    \n\nInterestingly, I bet I can make it so \n\n  sage: maple.gcd??\n\nwill show the source code using one you suggest above.  Trac ticket:\n   \n\n> Whether or not using printlevel or showstat is legal (in light of Josh's\n> response from Maple) is an interesting question.  They are built-in\n> capabilities meant for introspection.  They were also encouraged by the\n> Maple people in the above posts.\n\n<tinfoil hat> Maybe it is a trap.  :-)  </tinfoil hat>\n\n - William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1209\n\n",
    "created_at": "2007-11-19T16:58:02Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "make it so maple.gcd?? shows source code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1209",
    "user": "was"
}
```
Assignee: was


```
On Nov 19, 2007 8:29 AM, Jason Grout <jason-sage@creativetrax.com> wrote:
> 
> William Stein wrote:
> 
> >  3. Dumb question -- Where is the actual source code of anything in Maple?
> >      I'm skimming through my Maple install to see some actual source code and
> >      I can't find anything.  The lib/ directory has lots of .mla
> > files, but these are all
> >      pre-compiled binary files -- no source code.  Is there some tool
> > included with
> >      Maple to decompile them?     (I'm not being rhetorical, I simply don't know
> >      how to actually view source code of Maple functions, even if I wanted to.)
> 
> Some links dealing with this:
> 
> http://www.mapleprimes.com/blog/jacquesc/old-timer-techniques
> 
> http://www.mapleprimes.com/forum/algorithms-used-in-maple
> 
> http://thproxy.jinr.ru/Documents/MapleV/qa/section3_4.html
> 
> I've used the printlevel and I think the showstat techniques before.
> Unfortunately, I can't test them because I no longer have access to
> Maple (at least on my home machine).  I guess that's they whole point
> again---even if there is some way for someone to get the output of the
> procedure, it doesn't do me any good because I don't have Maple and
> can't check it anyway.

This *does* work in Maple 11:

sage: maple_console()
    |\^/|     Maple 11 (APPLE UNIVERSAL OSX)
._|\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple Inc. 2007
 \  MAPLE  /  All rights reserved. Maple is a trademark of
 <____ ____>  Waterloo Maple Inc.
      |       Type ? for help.
> print(gcd);
                                  proc(aa, bb, cofa::name, cofb::name)  ...  end proc

> interface(verboseproc=2);
                                                           1

> print(gcd);              
proc(aa, bb, cofa::name, cofb::name)
local Z, GCD, a, b;
option `Copyright (c) 1992 by the University of Waterloo. All rights reserved.`;
    if 2 < nargs and member(cofa, indets(aa) union indets(bb)) then error "The optional 3rd argument given to `\
...

I wonder what proportion of the 1300 or so top-level functions in Maple (according
to a sage's maple.[tab]) actually have source code.    

Interestingly, I bet I can make it so 

  sage: maple.gcd??

will show the source code using one you suggest above.  Trac ticket:
   

> Whether or not using printlevel or showstat is legal (in light of Josh's
> response from Maple) is an interesting question.  They are built-in
> capabilities meant for introspection.  They were also encouraged by the
> Maple people in the above posts.

<tinfoil hat> Maybe it is a trap.  :-)  </tinfoil hat>

 - William
```


Issue created by migration from https://trac.sagemath.org/ticket/1209





---

archive/issue_comments_007485.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-11-19T16:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7485",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_007486.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-01-27T07:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7486",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_007487.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-27T07:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7487",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007488.json:
```json
{
    "body": "New patch added.",
    "created_at": "2008-01-27T07:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7488",
    "user": "mhansen"
}
```

New patch added.



---

archive/issue_comments_007489.json:
```json
{
    "body": "I say apply, even though this patch spawns a new maple for each query.  mhansen couldn't get 'maple.gcd?' to work without doing that, so it can be a new ticket.",
    "created_at": "2008-01-27T07:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7489",
    "user": "ncalexan"
}
```

I say apply, even though this patch spawns a new maple for each query.  mhansen couldn't get 'maple.gcd?' to work without doing that, so it can be a new ticket.



---

archive/issue_comments_007490.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T07:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7490",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007491.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc1",
    "created_at": "2008-01-27T07:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7491",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc1



---

archive/issue_comments_007492.json:
```json
{
    "body": "Referee report:\n\n* All doctests pass.  Excellent. \n\n* Line 455: \"trys\" --> \"tries\"\n\n* It would be good if you also added something to the programming guide that explains the new `_sage_src_` \"protocol\" that you just invented in the course of making this patch.",
    "created_at": "2008-01-27T13:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7492",
    "user": "was"
}
```

Referee report:

* All doctests pass.  Excellent. 

* Line 455: "trys" --> "tries"

* It would be good if you also added something to the programming guide that explains the new `_sage_src_` "protocol" that you just invented in the course of making this patch.



---

archive/issue_comments_007493.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-01-27T13:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7493",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_007494.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-01-27T13:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7494",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_007495.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-27T19:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7495",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_007496.json:
```json
{
    "body": "New patch that fixes the typo is posted.  I made the programming guide suggestion #2335 .",
    "created_at": "2008-02-27T19:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7496",
    "user": "mhansen"
}
```

New patch that fixes the typo is posted.  I made the programming guide suggestion #2335 .



---

archive/issue_comments_007497.json:
```json
{
    "body": "I get some reject against my 2.10.3.rc0:\n\n```\nsage$ patch -p1 --dry-run < trac_1209.patch\npatching file sage/interfaces/maple.py\nHunk #1 succeeded at 485 with fuzz 2 (offset 35 lines).\nHunk #2 FAILED at 584.\n1 out of 2 hunks FAILED -- saving rejects to file sage/interfaces/maple.py.rej\npatching file sage/misc/sagedoc.py\nReversed (or previously applied) patch detected!  Assume -R? [n] n\nApply anyway? [n] n\nSkipping patch.\n1 out of 1 hunk ignored -- saving rejects to file sage/misc/sagedoc.py.rej\n```\n\nAm I missing a dependency or do I just need a rebase here?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-28T00:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7497",
    "user": "mabshoff"
}
```

I get some reject against my 2.10.3.rc0:

```
sage$ patch -p1 --dry-run < trac_1209.patch
patching file sage/interfaces/maple.py
Hunk #1 succeeded at 485 with fuzz 2 (offset 35 lines).
Hunk #2 FAILED at 584.
1 out of 2 hunks FAILED -- saving rejects to file sage/interfaces/maple.py.rej
patching file sage/misc/sagedoc.py
Reversed (or previously applied) patch detected!  Assume -R? [n] n
Apply anyway? [n] n
Skipping patch.
1 out of 1 hunk ignored -- saving rejects to file sage/misc/sagedoc.py.rej
```

Am I missing a dependency or do I just need a rebase here?

Cheers,

Michael



---

archive/issue_comments_007498.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-28T00:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7498",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_007499.json:
```json
{
    "body": "New patch posted which should apply cleanly.",
    "created_at": "2008-02-28T00:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7499",
    "user": "mhansen"
}
```

New patch posted which should apply cleanly.



---

archive/issue_comments_007500.json:
```json
{
    "body": "Closer, but still not across the finish line:\n\n```\nsage$ patch -p1 --dry-run < trac_1209.2.patch\npatching file sage/interfaces/maple.py\nHunk #1 succeeded at 485 with fuzz 2 (offset 35 lines).\nHunk #2 FAILED at 584.\n1 out of 2 hunks FAILED -- saving rejects to file sage/interfaces/maple.py.rej\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-28T00:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7500",
    "user": "mabshoff"
}
```

Closer, but still not across the finish line:

```
sage$ patch -p1 --dry-run < trac_1209.2.patch
patching file sage/interfaces/maple.py
Hunk #1 succeeded at 485 with fuzz 2 (offset 35 lines).
Hunk #2 FAILED at 584.
1 out of 2 hunks FAILED -- saving rejects to file sage/interfaces/maple.py.rej
```


Cheers,

Michael



---

archive/issue_comments_007501.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-28T01:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7501",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_007502.json:
```json
{
    "body": "This last one should do it.",
    "created_at": "2008-02-28T01:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7502",
    "user": "mhansen"
}
```

This last one should do it.



---

archive/issue_comments_007503.json:
```json
{
    "body": "Merged 1209.3.patch in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T01:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7503",
    "user": "mabshoff"
}
```

Merged 1209.3.patch in Sage 2.10.3.rc0



---

archive/issue_comments_007504.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T01:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1209#issuecomment-7504",
    "user": "mabshoff"
}
```

Resolution: fixed
