# Issue 2041: [with doc patch, needs review] tutorial: long lines in verbatim environments get cut off in pdf file

archive/issues_002041.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nSee the discussion at\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/99ef95ceff366175/8e44f7219c7394d9\n\nLines longer than about 74 characters in verbatim environments are longer than the text width in the pdf files.  Worse, if they're longer than about 80 characters they just fall off the page and the rest gets cut off.\n\nThe attached doc patch does the following:\n1. Ignore the \"slightly long, but still completely visible\" lines (i.e left them the way they were).  They're not that pretty, but wrapping them only makes things nicer by a marginal amount.\n2. Manually wrapped the really long lines where stuff was lost: when these lines corresponded to sage: input commands, I broke them up in a place that looked ok to me with a backslash and continued on the next line.  I added warnings to the reader not to type in the ....: that appear on subsequent lines then.  If the lines correspond to long sage output, I just broke them after 72 characters, the exact same way that sage would behave if the terminal were 72 characters wide.  \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2041\n\n",
    "created_at": "2008-02-03T23:38:23Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "[with doc patch, needs review] tutorial: long lines in verbatim environments get cut off in pdf file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2041",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

See the discussion at
http://groups.google.com/group/sage-devel/browse_thread/thread/99ef95ceff366175/8e44f7219c7394d9

Lines longer than about 74 characters in verbatim environments are longer than the text width in the pdf files.  Worse, if they're longer than about 80 characters they just fall off the page and the rest gets cut off.

The attached doc patch does the following:
1. Ignore the "slightly long, but still completely visible" lines (i.e left them the way they were).  They're not that pretty, but wrapping them only makes things nicer by a marginal amount.
2. Manually wrapped the really long lines where stuff was lost: when these lines corresponded to sage: input commands, I broke them up in a place that looked ok to me with a backslash and continued on the next line.  I added warnings to the reader not to type in the ....: that appear on subsequent lines then.  If the lines correspond to long sage output, I just broke them after 72 characters, the exact same way that sage would behave if the terminal were 72 characters wide.  



Issue created by migration from https://trac.sagemath.org/ticket/2041





---

archive/issue_comments_013217.json:
```json
{
    "body": "Hi Alex, \n\nyou seem to have used some kind of hard wrapping to correct the issue. And the result some times cases line breaks inside words like\n\n```\n2480 Eisenstein subspace of dimension 1 of Modular Forms space of dimension 2 f \n2481 or Congruence Subgroup Gamma0(11) of weight 2 over Rational Field \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-04T05:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13217",
    "user": "mabshoff"
}
```

Hi Alex, 

you seem to have used some kind of hard wrapping to correct the issue. And the result some times cases line breaks inside words like

```
2480 Eisenstein subspace of dimension 1 of Modular Forms space of dimension 2 f 
2481 or Congruence Subgroup Gamma0(11) of weight 2 over Rational Field 
```


Cheers,

Michael



---

archive/issue_comments_013218.json:
```json
{
    "body": "Yes, that was on purpose (as I said above).  That's precisely how Sage's output is printed, I don't see why it should be beautified for documentation purposes.  The point of the tutorial is to get people used to the system, not to some idealized notion of the system.\n\nAnyway, that was just my train of thought when working on this, and I'm willing to change my mind if there are arguments against it.",
    "created_at": "2008-02-04T15:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13218",
    "user": "AlexGhitza"
}
```

Yes, that was on purpose (as I said above).  That's precisely how Sage's output is printed, I don't see why it should be beautified for documentation purposes.  The point of the tutorial is to get people used to the system, not to some idealized notion of the system.

Anyway, that was just my train of thought when working on this, and I'm willing to change my mind if there are arguments against it.



---

archive/issue_comments_013219.json:
```json
{
    "body": "I have fixed the problem Michael pointed out, and did some more beautification work on the tutorial: some typos, some changes in formulation.  I've replaced the old patch with the new and improved one.",
    "created_at": "2008-02-12T04:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13219",
    "user": "AlexGhitza"
}
```

I have fixed the problem Michael pointed out, and did some more beautification work on the tutorial: some typos, some changes in formulation.  I've replaced the old patch with the new and improved one.



---

archive/issue_comments_013220.json:
```json
{
    "body": "Except for the hunk\n\n```\n995\t998\t\\SAGE makes some use of Singular \\cite{Si}, e.g.,  \n996\t \tfor computation of gcd's and Gr\\\"obner basis \n \t999\tfor computation of gcd's and Gr\\\"obner bases \n997\t1000\tof ideals. \n```\n\nthe patch looks good. We use `Gr\\\"obner basis` all over the place in the document and it seems to be the standard name even in English. I am giving the patch a positive review and will remove the hunk above before applying.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T00:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13220",
    "user": "mabshoff"
}
```

Except for the hunk

```
995	998	\SAGE makes some use of Singular \cite{Si}, e.g.,  
996	 	for computation of gcd's and Gr\"obner basis 
 	999	for computation of gcd's and Gr\"obner bases 
997	1000	of ideals. 
```

the patch looks good. We use `Gr\"obner basis` all over the place in the document and it seems to be the standard name even in English. I am giving the patch a positive review and will remove the hunk above before applying.

Cheers,

Michael



---

archive/issue_comments_013221.json:
```json
{
    "body": "I had to resolve some rejects since some of the fixes already made it in. The final version of the patch that I applied can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/trac_2041-tut_long_lines.patch\n\nTo get the full picture look at the commit prior to this patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T00:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13221",
    "user": "mabshoff"
}
```

I had to resolve some rejects since some of the fixes already made it in. The final version of the patch that I applied can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/trac_2041-tut_long_lines.patch

To get the full picture look at the commit prior to this patch.

Cheers,

Michael



---

archive/issue_comments_013222.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-16T00:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13222",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013223.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-16T00:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13223",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1



---

archive/issue_comments_013224.json:
```json
{
    "body": "The patch actually causes various doctest failures in `tut.tex`. I am not sure how to balance this issue with readability.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T04:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13224",
    "user": "mabshoff"
}
```

The patch actually causes various doctest failures in `tut.tex`. I am not sure how to balance this issue with readability.

Cheers,

Michael



---

archive/issue_comments_013225.json:
```json
{
    "body": "Attachment [2041-tut_long_lines.patch](tarball://root/attachments/some-uuid/ticket2041/2041-tut_long_lines.patch) by AlexGhitza created at 2008-02-17 20:09:49",
    "created_at": "2008-02-17T20:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13225",
    "user": "AlexGhitza"
}
```

Attachment [2041-tut_long_lines.patch](tarball://root/attachments/some-uuid/ticket2041/2041-tut_long_lines.patch) by AlexGhitza created at 2008-02-17 20:09:49



---

archive/issue_comments_013226.json:
```json
{
    "body": "OK, I've redone this patch to fix the doctest failures.  Right now there are no doctest failures, at the price of three lines being too long.  I say we put this patch in as it is, and deal with these three lines when we get a chance.",
    "created_at": "2008-02-17T20:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13226",
    "user": "AlexGhitza"
}
```

OK, I've redone this patch to fix the doctest failures.  Right now there are no doctest failures, at the price of three lines being too long.  I say we put this patch in as it is, and deal with these three lines when we get a chance.



---

archive/issue_comments_013227.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-02-17T20:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13227",
    "user": "AlexGhitza"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_013228.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-02-17T20:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13228",
    "user": "AlexGhitza"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_013229.json:
```json
{
    "body": "Since the patch has already been replied I need a patch that reverts the three problematic issues. I will look into this or once 2.10.1.alpha1 is out you could give me a relative patch ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T20:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13229",
    "user": "mabshoff"
}
```

Since the patch has already been replied I need a patch that reverts the three problematic issues. I will look into this or once 2.10.1.alpha1 is out you could give me a relative patch ;)

Cheers,

Michael



---

archive/issue_comments_013230.json:
```json
{
    "body": "I'm getting rather confused with what I have now versus what's merged versus what's on trac, so I'll just wait until 2.10.2.alpha1 and submit a relative patch (unless of course mabshoff will already have worked his magic :)",
    "created_at": "2008-02-17T20:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13230",
    "user": "AlexGhitza"
}
```

I'm getting rather confused with what I have now versus what's merged versus what's on trac, so I'll just wait until 2.10.2.alpha1 and submit a relative patch (unless of course mabshoff will already have worked his magic :)



---

archive/issue_comments_013231.json:
```json
{
    "body": "I have uploaded a patch that is based on 2.10.2.alpha1 and passes all the tests in sage -t tut.tex.",
    "created_at": "2008-02-20T13:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13231",
    "user": "AlexGhitza"
}
```

I have uploaded a patch that is based on 2.10.2.alpha1 and passes all the tests in sage -t tut.tex.



---

archive/issue_comments_013232.json:
```json
{
    "body": "Attachment [tut_verbatim.patch](tarball://root/attachments/some-uuid/ticket2041/tut_verbatim.patch) by mabshoff created at 2008-02-20 13:55:29\n\nThe new patch `tut_verbatim.patch` looks good to me except\n\n```\n999\t \tfor computation of gcd's and Gr\\\"obner basis \n \t999\tfor computation of gcd's and Gr\\\"obner bases \n```\n\n\nApplying with that hunk removed. Great work Alex.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-20T13:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13232",
    "user": "mabshoff"
}
```

Attachment [tut_verbatim.patch](tarball://root/attachments/some-uuid/ticket2041/tut_verbatim.patch) by mabshoff created at 2008-02-20 13:55:29

The new patch `tut_verbatim.patch` looks good to me except

```
999	 	for computation of gcd's and Gr\"obner basis 
 	999	for computation of gcd's and Gr\"obner bases 
```


Applying with that hunk removed. Great work Alex.

Cheers,

Michael



---

archive/issue_comments_013233.json:
```json
{
    "body": "Merged `tut_verbatim.patch` in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T14:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13233",
    "user": "mabshoff"
}
```

Merged `tut_verbatim.patch` in Sage 2.10.2.alpha2



---

archive/issue_comments_013234.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T14:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2041#issuecomment-13234",
    "user": "mabshoff"
}
```

Resolution: fixed
