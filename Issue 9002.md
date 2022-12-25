# Issue 9002: Noise on PPC Mac in parametric_surface.pyx

archive/issues_009002.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  georgsweber\n\nWith 4.4.2 on 10.4 on PPC G4:\n\n```\nsage -t  \"devel/sage/sage/plot/plot3d/parametric_surface.pyx\"\n**********************************************************************\n    sage: M.bounding_box()\nExpected:\n    ((-10.0, -7.5390734925047846, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))\nGot:\n    ((-10.0, -7.5390734925047855, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9002\n\n",
    "created_at": "2010-05-21T00:01:14Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Noise on PPC Mac in parametric_surface.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9002",
    "user": "https://github.com/kcrisman"
}
```
Assignee: tbd

CC:  georgsweber

With 4.4.2 on 10.4 on PPC G4:

```
sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
**********************************************************************
    sage: M.bounding_box()
Expected:
    ((-10.0, -7.5390734925047846, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
Got:
    ((-10.0, -7.5390734925047855, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/9002





---

archive/issue_comments_083100.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-26T02:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83100",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083101.json:
```json
{
    "body": "This should be tested both on a PPC Mac and some Intel or AMD architecture.  Works for me :)",
    "created_at": "2010-05-26T02:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83101",
    "user": "https://github.com/kcrisman"
}
```

This should be tested both on a PPC Mac and some Intel or AMD architecture.  Works for me :)



---

archive/issue_comments_083102.json:
```json
{
    "body": "How is the \"expected\" value arrived at? It is just what someone happened to get on their computer, or was it evaluated to high precision in a different way?",
    "created_at": "2010-06-23T00:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83102",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

How is the "expected" value arrived at? It is just what someone happened to get on their computer, or was it evaluated to high precision in a different way?



---

archive/issue_comments_083103.json:
```json
{
    "body": "The expected value doesn't matter in that sense.  It is just creating a box which contains a certain graphic, and the last few digits are completely irrelevant (try the pictures).  E.g., \n\n```\nsage: from sage.plot.plot3d.parametric_surface import MobiusStrip\nsage: M = MobiusStrip(.0000000000007,.00000000000003,2)\nsage: M.bounding_box()\n((-7.3000000000000002e-13, -7.0049870840325469e-13, -2.9940801852848143e-14), (7.3000000000000002e-13, 7.0049870840325469e-13, 2.9940801852848143e-14))\n```\n\nand you can also check by looking at the graphic that the box is correct (though the formatting of the numbers could be better, which is a separate issue).\n\nNow, that doesn't mean that somewhere there isn't some evil bug lurking.  But tracking down where the discrepancy comes from in this code would mean following a *lot* of branches, for no real purpose.  Most likely it is the fact that `MobiusStrip` has an `eval()` method that uses `math.sin` and `math.cos` a lot, which presumably will be very slightly different on different architectures.\n\nDavid, I realize this is a decision regarding how far back to look for numerical consistency, and I agree than for things like `gamma(2.3)` it would be very good to ensure maximum consistency.  But here the whole point is a heuristic to get a box that encloses the figure, and differences at that level of accuracy are irrelevant and take resources away from other badly needed improvements to Sage.  So it is unfortunate that we won't track it down, but it is reasonable, I think.\n\nGeorg, when you review this, you might as well try the example in this comment, to make sure that it looks right, but if it does then just do a normal review.  Unless you want to compare what you get from `eval()` with this one, which is surely where the actual difference lies.  I essentially only have access to one box at a time, so it's very difficult for me to compare them.",
    "created_at": "2010-06-23T13:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83103",
    "user": "https://github.com/kcrisman"
}
```

The expected value doesn't matter in that sense.  It is just creating a box which contains a certain graphic, and the last few digits are completely irrelevant (try the pictures).  E.g., 

```
sage: from sage.plot.plot3d.parametric_surface import MobiusStrip
sage: M = MobiusStrip(.0000000000007,.00000000000003,2)
sage: M.bounding_box()
((-7.3000000000000002e-13, -7.0049870840325469e-13, -2.9940801852848143e-14), (7.3000000000000002e-13, 7.0049870840325469e-13, 2.9940801852848143e-14))
```

and you can also check by looking at the graphic that the box is correct (though the formatting of the numbers could be better, which is a separate issue).

Now, that doesn't mean that somewhere there isn't some evil bug lurking.  But tracking down where the discrepancy comes from in this code would mean following a *lot* of branches, for no real purpose.  Most likely it is the fact that `MobiusStrip` has an `eval()` method that uses `math.sin` and `math.cos` a lot, which presumably will be very slightly different on different architectures.

David, I realize this is a decision regarding how far back to look for numerical consistency, and I agree than for things like `gamma(2.3)` it would be very good to ensure maximum consistency.  But here the whole point is a heuristic to get a box that encloses the figure, and differences at that level of accuracy are irrelevant and take resources away from other badly needed improvements to Sage.  So it is unfortunate that we won't track it down, but it is reasonable, I think.

Georg, when you review this, you might as well try the example in this comment, to make sure that it looks right, but if it does then just do a normal review.  Unless you want to compare what you get from `eval()` with this one, which is surely where the actual difference lies.  I essentially only have access to one box at a time, so it's very difficult for me to compare them.



---

archive/issue_comments_083104.json:
```json
{
    "body": "Replying to [comment:3 kcrisman]:\n> David, I realize this is a decision regarding how far back to look for numerical consistency, and I agree than for things like `gamma(2.3)` it would be very good to ensure maximum consistency.  But here the whole point is a heuristic to get a box that encloses the figure, and differences at that level of accuracy are irrelevant and take resources away from other badly needed improvements to Sage.  So it is unfortunate that we won't track it down, but it is reasonable, I think.\n\nFair enough. Your point is taken. I just tend to \"see red\" when I see numerical noise fixes, where it appears the original \"expected\" value just seems to be based on what someone happened to get on their computer on that particular day, with no further reasoning. Then when it fails, someone adds a few dots and it magically passes. IMHO, too many people seem happy to do this. \n\nBut in this case, I can see where you are coming from. Tracing the exact value would be a pointless waste of time. \n\n<moan> Personally, where is is possible, I'd like to see high precision numerical values put as a comment in a doc test. So your gamma(2.3) would record a value like 1.16671190519816034504188144120291793853399434971946889397020666387 and say what method was used to get it. Then if code is updated and tests fail, we could question the changes more objecitively than just fixing them by adding a few dots. Ideally such a number should shows results from a independent methods. </moan>\n\nDave",
    "created_at": "2010-06-23T13:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83104",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:3 kcrisman]:
> David, I realize this is a decision regarding how far back to look for numerical consistency, and I agree than for things like `gamma(2.3)` it would be very good to ensure maximum consistency.  But here the whole point is a heuristic to get a box that encloses the figure, and differences at that level of accuracy are irrelevant and take resources away from other badly needed improvements to Sage.  So it is unfortunate that we won't track it down, but it is reasonable, I think.

Fair enough. Your point is taken. I just tend to "see red" when I see numerical noise fixes, where it appears the original "expected" value just seems to be based on what someone happened to get on their computer on that particular day, with no further reasoning. Then when it fails, someone adds a few dots and it magically passes. IMHO, too many people seem happy to do this. 

But in this case, I can see where you are coming from. Tracing the exact value would be a pointless waste of time. 

<moan> Personally, where is is possible, I'd like to see high precision numerical values put as a comment in a doc test. So your gamma(2.3) would record a value like 1.16671190519816034504188144120291793853399434971946889397020666387 and say what method was used to get it. Then if code is updated and tests fail, we could question the changes more objecitively than just fixing them by adding a few dots. Ideally such a number should shows results from a independent methods. </moan>

Dave



---

archive/issue_comments_083105.json:
```json
{
    "body": "England vs Slovenia kicks off in 10 minutes. After the game I'll review this. It looks simple enough, and you have convinced me there is no point worrying unduly about the exact number. \n\nDave",
    "created_at": "2010-06-23T13:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83105",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

England vs Slovenia kicks off in 10 minutes. After the game I'll review this. It looks simple enough, and you have convinced me there is no point worrying unduly about the exact number. 

Dave



---

archive/issue_comments_083106.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n> England vs Slovenia kicks off in 10 minutes. After the game I'll review this. It looks simple enough, and you have convinced me there is no point worrying unduly about the exact number. \n\nAh, see, I get to wait for a few more hours until Germany-Ghana.  I suppose I should watch US-Algeria too, but work calls.\n\nDo you have a PPC Mac box to test this on?  I think we still need Georg or someone else for that.",
    "created_at": "2010-06-23T14:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83106",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:5 drkirkby]:
> England vs Slovenia kicks off in 10 minutes. After the game I'll review this. It looks simple enough, and you have convinced me there is no point worrying unduly about the exact number. 

Ah, see, I get to wait for a few more hours until Germany-Ghana.  I suppose I should watch US-Algeria too, but work calls.

Do you have a PPC Mac box to test this on?  I think we still need Georg or someone else for that.



---

archive/issue_comments_083107.json:
```json
{
    "body": "I'm happy to give this a positive. We know what result it was producing, and your fix should allow that to pass. I can't possibly see how this can make the situation any worst, even in the **very** unlikely even it does not cure the problem. \n\nI've tested on SPARC (Solaris 10) and x86 (Linux) processors. \n\n## Linux (sage.math) with Intel Xeon processor\n\n```\nsage -t  \"devel/sage/sage/plot/plot3d/parametric_surface.pyx\"\n\t [11.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 11.3 seconds\nkirkby@sage:~/sage-4.4.3$ uname -a\nLinux sage.math.washington.edu 2.6.24-26-server #1 SMP Tue Dec 1 18:26:43 UTC 2009 x86_64 GNU/Linux\n```\n\n\n## 'redstart' Solaris 10 with Sun UltraSPARC III+ processors\n\n```\ndrkirkby@redstart:~/sage-4.4.4.alpha1$ ./sage -t  \"devel/sage/sage/plot/plot3d/parametric_surface.pyx\"\nsage -t  \"devel/sage/sage/plot/plot3d/parametric_surface.pyx\"\n\t [33.6 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 33.6 seconds\n```\n",
    "created_at": "2010-06-23T17:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83107",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm happy to give this a positive. We know what result it was producing, and your fix should allow that to pass. I can't possibly see how this can make the situation any worst, even in the **very** unlikely even it does not cure the problem. 

I've tested on SPARC (Solaris 10) and x86 (Linux) processors. 

## Linux (sage.math) with Intel Xeon processor

```
sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
	 [11.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 11.3 seconds
kirkby@sage:~/sage-4.4.3$ uname -a
Linux sage.math.washington.edu 2.6.24-26-server #1 SMP Tue Dec 1 18:26:43 UTC 2009 x86_64 GNU/Linux
```


## 'redstart' Solaris 10 with Sun UltraSPARC III+ processors

```
drkirkby@redstart:~/sage-4.4.4.alpha1$ ./sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
	 [33.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 33.6 seconds
```




---

archive/issue_comments_083108.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T17:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83108",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083109.json:
```json
{
    "body": "On my Mac PPC (PowerPC_G4) with vanilla Sage-4.4.3, before applying the patch:\n\n```\nsage -t  \"devel/sage/sage/plot/plot3d/parametric_surface.pyx\"\n**********************************************************************\nFile \"/Volumes/SageVolume/sage/sage-4.4.3/devel/sage/sage/plot/plot3d/parametric_surface.pyx\", line 311:\n    sage: M.bounding_box()\nExpected:\n    ((-10.0, -7.5390734925047846, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))\nGot:\n    ((-10.0, -7.5390734925047855, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_11\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_parametric_surface.py\n         [106.1 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/plot/plot3d/parametric_surface.pyx\"\nTotal time for all tests: 106.1 seconds\n```\n\nand after applying the patch:\n\n```\nsage -t  \"devel/sage/sage/plot/plot3d/parametric_surface.pyx\"\n         [86.9 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 87.0 seconds\n```\n\nGood work, positive review well deserved!",
    "created_at": "2010-06-28T21:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83109",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

On my Mac PPC (PowerPC_G4) with vanilla Sage-4.4.3, before applying the patch:

```
sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
**********************************************************************
File "/Volumes/SageVolume/sage/sage-4.4.3/devel/sage/sage/plot/plot3d/parametric_surface.pyx", line 311:
    sage: M.bounding_box()
Expected:
    ((-10.0, -7.5390734925047846, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
Got:
    ((-10.0, -7.5390734925047855, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_11
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_parametric_surface.py
         [106.1 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
Total time for all tests: 106.1 seconds
```

and after applying the patch:

```
sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
         [86.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 87.0 seconds
```

Good work, positive review well deserved!



---

archive/issue_comments_083110.json:
```json
{
    "body": "This ticket seems the same as #9516...",
    "created_at": "2010-07-22T02:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83110",
    "user": "https://github.com/dandrake"
}
```

This ticket seems the same as #9516...



---

archive/issue_comments_083111.json:
```json
{
    "body": "Karl-Dieter (or release manager): can you fix the User field in your patch? It looks like you didn't set a username in your hgrc.",
    "created_at": "2010-07-22T02:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83111",
    "user": "https://github.com/dandrake"
}
```

Karl-Dieter (or release manager): can you fix the User field in your patch? It looks like you didn't set a username in your hgrc.



---

archive/issue_comments_083112.json:
```json
{
    "body": "Replying to [comment:11 ddrake]:\n> Karl-Dieter (or release manager): can you fix the User field in your patch? It looks like you didn't set a username in your hgrc.\n\nHave you made that comment on the wrong ticket? I see\n\n`# User crisman`@`Crismans-Computer.local`\n\nin the patch. \n\nDave",
    "created_at": "2010-07-22T06:53:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83112",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:11 ddrake]:
> Karl-Dieter (or release manager): can you fix the User field in your patch? It looks like you didn't set a username in your hgrc.

Have you made that comment on the wrong ticket? I see

`# User crisman`@`Crismans-Computer.local`

in the patch. 

Dave



---

archive/issue_comments_083113.json:
```json
{
    "body": "Replying to [comment:12 drkirkby]:\n> Replying to [comment:11 ddrake]:\n> > Karl-Dieter (or release manager): can you fix the User field in your patch? It looks like you didn't set a username in your hgrc.\n> \n> Have you made that comment on the wrong ticket? I see\n> \n> `# User crisman`@`Crismans-Computer.local`\n> \n> in the patch. \n> \n> Dave \n\nThinking about that more, that more, your point is valid, as that is not a full name. I can understand someone not wanting their full email address. Just in case the person does not know the format, a .hgrc which adds a name and email address would be:\n\n```\ndrkirkby@hawk:~$ cat .hgrc\n[ui]\nusername = Forename Surname <your.address@yoursite.com>\n\n[extensions]\n# Enable the Mercurial queue extension.\nhgext.mq =\n```\n",
    "created_at": "2010-07-22T07:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83113",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:12 drkirkby]:
> Replying to [comment:11 ddrake]:
> > Karl-Dieter (or release manager): can you fix the User field in your patch? It looks like you didn't set a username in your hgrc.
> 
> Have you made that comment on the wrong ticket? I see
> 
> `# User crisman`@`Crismans-Computer.local`
> 
> in the patch. 
> 
> Dave 

Thinking about that more, that more, your point is valid, as that is not a full name. I can understand someone not wanting their full email address. Just in case the person does not know the format, a .hgrc which adds a name and email address would be:

```
drkirkby@hawk:~$ cat .hgrc
[ui]
username = Forename Surname <your.address@yoursite.com>

[extensions]
# Enable the Mercurial queue extension.
hgext.mq =
```




---

archive/issue_comments_083114.json:
```json
{
    "body": "Sorry, I didn't think of that.  I created this patch on a PPC Mac, and it's one I don't ordinarily use for Sage developing and hence didn't have an hgrc file.  I'll try to fix that momentarily.  Otherwise all my patches have my usual email address on them.",
    "created_at": "2010-07-22T12:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83114",
    "user": "https://github.com/kcrisman"
}
```

Sorry, I didn't think of that.  I created this patch on a PPC Mac, and it's one I don't ordinarily use for Sage developing and hence didn't have an hgrc file.  I'll try to fix that momentarily.  Otherwise all my patches have my usual email address on them.



---

archive/issue_comments_083115.json:
```json
{
    "body": "Attachment [trac_9002-ppc-noise.patch](tarball://root/attachments/some-uuid/ticket9002/trac_9002-ppc-noise.patch) by @kcrisman created at 2010-07-22 12:36:18\n\nBased on 4.5.1",
    "created_at": "2010-07-22T12:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83115",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9002-ppc-noise.patch](tarball://root/attachments/some-uuid/ticket9002/trac_9002-ppc-noise.patch) by @kcrisman created at 2010-07-22 12:36:18

Based on 4.5.1



---

archive/issue_comments_083116.json:
```json
{
    "body": "Hopefully this will address the issue!",
    "created_at": "2010-07-22T12:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83116",
    "user": "https://github.com/kcrisman"
}
```

Hopefully this will address the issue!



---

archive/issue_comments_083117.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T23:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83117",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_083118.json:
```json
{
    "body": "Replying to [comment:15 kcrisman]:\n> Hopefully this will address the issue!\n\nExcellent. Thanks! Merged in 4.5.2.alpha1.",
    "created_at": "2010-07-22T23:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9002#issuecomment-83118",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:15 kcrisman]:
> Hopefully this will address the issue!

Excellent. Thanks! Merged in 4.5.2.alpha1.



---

archive/issue_events_009156.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-22T23:34:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9002",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9002#event-9156"
}
```
