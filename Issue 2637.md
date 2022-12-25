# Issue 2637: Patch so that a user can choose encodings in sage scripts.

archive/issues_002637.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: encoding utf-8\n\nThis ticket is related to my question on sage-support:\nhttp://groups.google.com/group/sage-support/browse_thread/thread/dab6a0880fa8b942\nand Martin Albrecht's patch.\n\nWith Martin's patch, sage scripts default to utf-8 encoding, which is a good default as ascii is a subset of utf-8, it is compatible with existing sage-scripts.\n\nBut I think that a user should be able to select a coding, if utf-8 is not suitable for him. For example a user with an editor not supporting unicode or a user needing utf-16. So sage should support python encoding hints.  \n \nPlease see the attached patch to sage/misc/interpreter.py, which tries to find out if the first line contains an encoding hint. If true, use the line from the file, else print the utf-8 encoding hint.\n\nWith best regards,\nLars Fischer\n\nIssue created by migration from https://trac.sagemath.org/ticket/2637\n\n",
    "created_at": "2008-03-21T21:43:30Z",
    "labels": [
        "component: user interface",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Patch so that a user can choose encodings in sage scripts.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2637",
    "user": "https://trac.sagemath.org/admin/accounts/users/lars.fischer"
}
```
Assignee: @williamstein

Keywords: encoding utf-8

This ticket is related to my question on sage-support:
http://groups.google.com/group/sage-support/browse_thread/thread/dab6a0880fa8b942
and Martin Albrecht's patch.

With Martin's patch, sage scripts default to utf-8 encoding, which is a good default as ascii is a subset of utf-8, it is compatible with existing sage-scripts.

But I think that a user should be able to select a coding, if utf-8 is not suitable for him. For example a user with an editor not supporting unicode or a user needing utf-16. So sage should support python encoding hints.  
 
Please see the attached patch to sage/misc/interpreter.py, which tries to find out if the first line contains an encoding hint. If true, use the line from the file, else print the utf-8 encoding hint.

With best regards,
Lars Fischer

Issue created by migration from https://trac.sagemath.org/ticket/2637





---

archive/issue_comments_018076.json:
```json
{
    "body": "Find an use encoding hints in the first line of a sage script.",
    "created_at": "2008-03-21T21:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18076",
    "user": "https://trac.sagemath.org/admin/accounts/users/lars.fischer"
}
```

Find an use encoding hints in the first line of a sage script.



---

archive/issue_comments_018077.json:
```json
{
    "body": "Attachment [encoding.hg](tarball://root/attachments/some-uuid/ticket2637/encoding.hg) by mabshoff created at 2008-03-21 21:46:32\n\nI do not see a patch attached. Where is it?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T21:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [encoding.hg](tarball://root/attachments/some-uuid/ticket2637/encoding.hg) by mabshoff created at 2008-03-21 21:46:32

I do not see a patch attached. Where is it?

Cheers,

Michael



---

archive/issue_events_006186.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-21T21:51:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2637#event-6186"
}
```



---

archive/issue_comments_018078.json:
```json
{
    "body": "Ok, the bundle showed up, i.e. it was a race condition. We do prefer patches over bundles, especially for single commit changesets.\n\nI am not sure this is a good feature since UTF-8 is ubiquitous out there these days. We build Python with ucs4 anyway, so I see no point to this patch. This  will only cause trouble if people start exchanging Sage files with different encodings. The code isn't doctested either, so if it were accepted that needs to be added, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T21:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18078",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, the bundle showed up, i.e. it was a race condition. We do prefer patches over bundles, especially for single commit changesets.

I am not sure this is a good feature since UTF-8 is ubiquitous out there these days. We build Python with ucs4 anyway, so I see no point to this patch. This  will only cause trouble if people start exchanging Sage files with different encodings. The code isn't doctested either, so if it were accepted that needs to be added, too.

Cheers,

Michael



---

archive/issue_comments_018079.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> Ok, the bundle showed up, i.e. it was a race condition. We do prefer patches over bundles, especially for single commit changesets.\n\n\nI followed the advise in \nhttp://www.sagemath.org/doc/html/prog/node72.html\n* \"For the occasional contributor:\"\n \n> I am not sure this is a good feature since UTF-8 is ubiquitous out there these days. We build Python with ucs4 anyway, so I see no point to this patch. This  will only cause trouble if people start exchanging Sage files with different encodings. The code isn't doctested either, so if it were accepted that needs to be added, too.\n\n\nI was thinking exactly the same after I saw the Martin's patch: \n*\"That will only cause trouble if someone wants to use something different than UTF-8. With sage being compatible with Python, sage should also support encoding selection.\"* \nSo I think it is the other way around: you get in trouble if people start using sage e.g. in Asia, using their their local encoding and there is no way to tell sage that the file is something different than UTF-8.\n\nPerhaps I am a bit too sensitive, because I have a long and frustrating history with computersystems making assumptions about encodings. \n\nIf there is interest, I can add doctests. What hg_sage. .... function would I use to get a file, I can attach? export() with the last but one entry from the log, and then replacing the attachment above?\n\nWith best regards,\nLars Fischer",
    "created_at": "2008-03-22T12:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18079",
    "user": "https://trac.sagemath.org/admin/accounts/users/lars.fischer"
}
```

Replying to [comment:2 mabshoff]:
> Ok, the bundle showed up, i.e. it was a race condition. We do prefer patches over bundles, especially for single commit changesets.


I followed the advise in 
http://www.sagemath.org/doc/html/prog/node72.html
* "For the occasional contributor:"
 
> I am not sure this is a good feature since UTF-8 is ubiquitous out there these days. We build Python with ucs4 anyway, so I see no point to this patch. This  will only cause trouble if people start exchanging Sage files with different encodings. The code isn't doctested either, so if it were accepted that needs to be added, too.


I was thinking exactly the same after I saw the Martin's patch: 
*"That will only cause trouble if someone wants to use something different than UTF-8. With sage being compatible with Python, sage should also support encoding selection."* 
So I think it is the other way around: you get in trouble if people start using sage e.g. in Asia, using their their local encoding and there is no way to tell sage that the file is something different than UTF-8.

Perhaps I am a bit too sensitive, because I have a long and frustrating history with computersystems making assumptions about encodings. 

If there is interest, I can add doctests. What hg_sage. .... function would I use to get a file, I can attach? export() with the last but one entry from the log, and then replacing the attachment above?

With best regards,
Lars Fischer



---

archive/issue_comments_018080.json:
```json
{
    "body": "I created a new patch file with hg_sage.export() . I hope this is a patch file. At least the first line in the file says so. \n\nNow the function contains some doctest. But I cannot sage -t interpreter.py, there is a nodoctest in the first line and if I temporarily  delete it, there are errors. \n\nI attached interpreter.py and after that I was able to record the tests.\n\nWith best regards,\nLars Fischer",
    "created_at": "2008-03-31T14:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18080",
    "user": "https://trac.sagemath.org/admin/accounts/users/lars.fischer"
}
```

I created a new patch file with hg_sage.export() . I hope this is a patch file. At least the first line in the file says so. 

Now the function contains some doctest. But I cannot sage -t interpreter.py, there is a nodoctest in the first line and if I temporarily  delete it, there are errors. 

I attached interpreter.py and after that I was able to record the tests.

With best regards,
Lars Fischer



---

archive/issue_comments_018081.json:
```json
{
    "body": "Find and use encoding hints in the first line of a sage script. Replace the previous attachment.",
    "created_at": "2008-03-31T14:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18081",
    "user": "https://trac.sagemath.org/admin/accounts/users/lars.fischer"
}
```

Find and use encoding hints in the first line of a sage script. Replace the previous attachment.



---

archive/issue_comments_018082.json:
```json
{
    "body": "Attachment [encoding.hg.patch](tarball://root/attachments/some-uuid/ticket2637/encoding.hg.patch) by mabshoff created at 2008-04-13 17:57:49\n\nHi Lars,\n\nafter thinking about the issue some more I changed my mind and now believe that this is a good idea. Patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T17:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18082",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [encoding.hg.patch](tarball://root/attachments/some-uuid/ticket2637/encoding.hg.patch) by mabshoff created at 2008-04-13 17:57:49

Hi Lars,

after thinking about the issue some more I changed my mind and now believe that this is a good idea. Patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_018083.json:
```json
{
    "body": "But there are a bunch of issues with the doctests:\n\n* devel/sage/sage/misc/interpreter.py has doctests disabled in general\n* you need to add \"from sage.misc.interpreter import handle_encoding_declaration\" to make the doctests work\n* Even then I get the following failure:\n\n```\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/interpreter.py\", line 355:\n    sage: c4='import os, sys\\n...'\nExpected:\n    handle_encoding_declaration(c1, sys.stdout)\n    # -*- coding: latin-1 -*-\n    'import os, sys\\n..'\nGot nothing\n```\nThere are other, unrelated doctest failure issues in that file, I fixed most of them and will hopefully post a patch shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T18:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18083",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

But there are a bunch of issues with the doctests:

* devel/sage/sage/misc/interpreter.py has doctests disabled in general
* you need to add "from sage.misc.interpreter import handle_encoding_declaration" to make the doctests work
* Even then I get the following failure:

```
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/interpreter.py", line 355:
    sage: c4='import os, sys\n...'
Expected:
    handle_encoding_declaration(c1, sys.stdout)
    # -*- coding: latin-1 -*-
    'import os, sys\n..'
Got nothing
```
There are other, unrelated doctest failure issues in that file, I fixed most of them and will hopefully post a patch shortly.

Cheers,

Michael



---

archive/issue_comments_018084.json:
```json
{
    "body": "Changing keywords from \"encoding utf-8\" to \"encoding utf-8, editor_malb\".",
    "created_at": "2008-06-20T04:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18084",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "encoding utf-8" to "encoding utf-8, editor_malb".



---

archive/issue_comments_018085.json:
```json
{
    "body": "Lars are you planing to address Michael's concern? I took over making sure that the patch gets in (I'm the editor for it now) and thus I wonder.",
    "created_at": "2008-06-23T23:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18085",
    "user": "https://github.com/malb"
}
```

Lars are you planing to address Michael's concern? I took over making sure that the patch gets in (I'm the editor for it now) and thus I wonder.



---

archive/issue_comments_018086.json:
```json
{
    "body": "Apply `encoding.hg.patch` first then `trac2637_fixes.patch` which still needs a review. With my fixes I'd give Lars' patch a positive review. Mabshoff can you review my patch?",
    "created_at": "2008-06-24T08:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18086",
    "user": "https://github.com/malb"
}
```

Apply `encoding.hg.patch` first then `trac2637_fixes.patch` which still needs a review. With my fixes I'd give Lars' patch a positive review. Mabshoff can you review my patch?



---

archive/issue_comments_018087.json:
```json
{
    "body": "Replying to [comment:8 malb]:\n\nHello,\n\nI am very busy at the moment. Because of that I was so quiet. Additionally the last upgrade  to sage 3.0 (sage -b main; sage -upgrade;) left my testing branch with the modified version of handle_encoding_declaration unusable:\n\n```\nsage -br test\n\n----------------------------------------------------------\nsage: Building and installing modified SAGE library files.\n.....\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nSetting permissions of DOT_SAGE directory so only you can read and write it.\nLoading SAGE library. Current Mercurial branch is: test\n---------------------------------------------------------------------------\n<type 'exceptions.ImportError'>           Traceback (most recent call last)\n....\n/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/all.py in <module>()\n     35\n     36 # Boolean Polynomial Rings\n---> 37 from sage.rings.polynomial.pbori import BooleanPolynomialRing\n     38\n     39 from sage.rings.polynomial.multi_polynomial_ideal import is_MPolynomialIdeal\n| SAGE Version 3.0, Release Date: 2008-04-23                         |\n| Type notebook() for the GUI, and license() for information.        |\n<type 'exceptions.ImportError'>: libpolybori.so: cannot open shared object file: No such file or directory\nsage:                    \n```\n\nI did not know how to deal with it, today I just rm-rf my sage-test branch, cloned a new one from the 3.0 version, sage -br test, hg_sage.applied encoding.hg.patch and trac2637_fixes.patch.\n\nAfter that sage -b  and then sage -t interpreter.py was successful.\n\n> Lars are you planing to address Michael's concern? I took over making sure that the patch gets in (I'm the editor for it now) and thus I wonder.\n\n\nWhat concern do you mean, after testing works?\n\n\nWith best regards,\n\nLars Fischer",
    "created_at": "2008-06-24T12:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18087",
    "user": "https://trac.sagemath.org/admin/accounts/users/lars.fischer"
}
```

Replying to [comment:8 malb]:

Hello,

I am very busy at the moment. Because of that I was so quiet. Additionally the last upgrade  to sage 3.0 (sage -b main; sage -upgrade;) left my testing branch with the modified version of handle_encoding_declaration unusable:

```
sage -br test

----------------------------------------------------------
sage: Building and installing modified SAGE library files.
.....
----------------------------------------------------------------------
----------------------------------------------------------------------
Setting permissions of DOT_SAGE directory so only you can read and write it.
Loading SAGE library. Current Mercurial branch is: test
---------------------------------------------------------------------------
<type 'exceptions.ImportError'>           Traceback (most recent call last)
....
/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/all.py in <module>()
     35
     36 # Boolean Polynomial Rings
---> 37 from sage.rings.polynomial.pbori import BooleanPolynomialRing
     38
     39 from sage.rings.polynomial.multi_polynomial_ideal import is_MPolynomialIdeal
| SAGE Version 3.0, Release Date: 2008-04-23                         |
| Type notebook() for the GUI, and license() for information.        |
<type 'exceptions.ImportError'>: libpolybori.so: cannot open shared object file: No such file or directory
sage:                    
```

I did not know how to deal with it, today I just rm-rf my sage-test branch, cloned a new one from the 3.0 version, sage -br test, hg_sage.applied encoding.hg.patch and trac2637_fixes.patch.

After that sage -b  and then sage -t interpreter.py was successful.

> Lars are you planing to address Michael's concern? I took over making sure that the patch gets in (I'm the editor for it now) and thus I wonder.


What concern do you mean, after testing works?


With best regards,

Lars Fischer



---

archive/issue_comments_018088.json:
```json
{
    "body": "Replying to [comment:10 lars.fischer]:\n> After that sage -b  and then sage -t interpreter.py was successful.\n> \n> > Lars are you planing to address Michael's concern? I took over making sure that the patch gets in (I'm the editor for it now) and thus I wonder.\n\n> \n> What concern do you mean, after testing works?\n\n\nI addressed the Michael's review in my patch so all that is needed from my perspective is a review of my patch. This can be either done by you or by Michael or by somebody else. Cheers, Martin",
    "created_at": "2008-06-24T12:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18088",
    "user": "https://github.com/malb"
}
```

Replying to [comment:10 lars.fischer]:
> After that sage -b  and then sage -t interpreter.py was successful.
> 
> > Lars are you planing to address Michael's concern? I took over making sure that the patch gets in (I'm the editor for it now) and thus I wonder.

> 
> What concern do you mean, after testing works?


I addressed the Michael's review in my patch so all that is needed from my perspective is a review of my patch. This can be either done by you or by Michael or by somebody else. Cheers, Martin



---

archive/issue_comments_018089.json:
```json
{
    "body": "Two suggestions for Martin's patch: I would remove the doctest:\n\n```\n78\t \t    sage: V = VectorSp \n \t78\t \n \t79\t    sage: V = VectorSp # not tested \n79\t80\t    VectorSpace                      VectorSpace_subspace \n80\t81\t    VectorSpace_ambient              VectorSpace_subspace_with_basis \n81\t82\t    VectorSpace_generic\n```\nsince it does not work any more as is and open a ticket for\n\n```\n513\t \t        sage: preparser(False) \n514\t \t        sage: 2/3 \n \t519\t \n \t520\t        sage: preparser(False)  \n \t521\t        sage: 2/3 # not tested since the doctest framework preparses anyway \n515\t522\t        0 \n \t523\t \n```\nunless the preparser is unfixable. When I attempted to fix all the doctests in the file I ran into the same problem and gave up after I ran into the same problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-24T13:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18089",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Two suggestions for Martin's patch: I would remove the doctest:

```
78	 	    sage: V = VectorSp 
 	78	 
 	79	    sage: V = VectorSp # not tested 
79	80	    VectorSpace                      VectorSpace_subspace 
80	81	    VectorSpace_ambient              VectorSpace_subspace_with_basis 
81	82	    VectorSpace_generic
```
since it does not work any more as is and open a ticket for

```
513	 	        sage: preparser(False) 
514	 	        sage: 2/3 
 	519	 
 	520	        sage: preparser(False)  
 	521	        sage: 2/3 # not tested since the doctest framework preparses anyway 
515	522	        0 
 	523	 
```
unless the preparser is unfixable. When I attempted to fix all the doctests in the file I ran into the same problem and gave up after I ran into the same problem.

Cheers,

Michael



---

archive/issue_comments_018090.json:
```json
{
    "body": "Attachment [trac2637_fixes.patch](tarball://root/attachments/some-uuid/ticket2637/trac2637_fixes.patch) by @malb created at 2008-06-24 13:41:06\n\naddresses mabshoff's review, sort of",
    "created_at": "2008-06-24T13:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18090",
    "user": "https://github.com/malb"
}
```

Attachment [trac2637_fixes.patch](tarball://root/attachments/some-uuid/ticket2637/trac2637_fixes.patch) by @malb created at 2008-06-24 13:41:06

addresses mabshoff's review, sort of



---

archive/issue_comments_018091.json:
```json
{
    "body": "* Yes, the file is old and a mess.\n  * The doctests double as documentation so I vote against removing them.\n  * I updated the VectorSpa<tab> docs to the current behaviour.\n  * Cleaning up interpreter.py should be a different ticket and no hold-back for this one IMHO.",
    "created_at": "2008-06-24T13:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18091",
    "user": "https://github.com/malb"
}
```

* Yes, the file is old and a mess.
  * The doctests double as documentation so I vote against removing them.
  * I updated the VectorSpa<tab> docs to the current behaviour.
  * Cleaning up interpreter.py should be a different ticket and no hold-back for this one IMHO.



---

archive/issue_comments_018092.json:
```json
{
    "body": "I agree with malb and I will review malb's new patch today.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-24T14:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18092",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I agree with malb and I will review malb's new patch today.

Cheers,

Michael



---

archive/issue_comments_018093.json:
```json
{
    "body": "Positive review. Sorry for the *loooonnnng* delay - my bad.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T05:47:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. Sorry for the *loooonnnng* delay - my bad.

Cheers,

Michael



---

archive/issue_comments_018094.json:
```json
{
    "body": "I am too paranoid to put this into 3.2.1 at this late stage, but it will be one of the first patches in 3.2.2.alpha0 early next week.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T06:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18094",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am too paranoid to put this into 3.2.1 at this late stage, but it will be one of the first patches in 3.2.2.alpha0 early next week.

Cheers,

Michael



---

archive/issue_events_006187.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-10T12:36:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2637#event-6187"
}
```



---

archive/issue_comments_018095.json:
```json
{
    "body": "Merged encoding.hg.patch and two hunks from trac2637_fixes.patch in Sage 3.2.2.alpha1. \n\nThe other four hunks from trac2637_fixes.patch were already in the tree.\n\nFinally :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T12:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18095",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged encoding.hg.patch and two hunks from trac2637_fixes.patch in Sage 3.2.2.alpha1. 

The other four hunks from trac2637_fixes.patch were already in the tree.

Finally :)

Cheers,

Michael



---

archive/issue_comments_018096.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-10T12:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2637#issuecomment-18096",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
