# Issue 7325: Sage cannot solve inequalities

archive/issues_007325.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @mwhansen\n\nKeywords: relation, symbolics, inequality, solve\n\nThere is no interface to solvers of inequalities available in Maxima.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7325\n\n",
    "created_at": "2009-10-27T21:47:53Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Sage cannot solve inequalities",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7325",
    "user": "https://github.com/robert-marik"
}
```
Assignee: tbd

CC:  @mwhansen

Keywords: relation, symbolics, inequality, solve

There is no interface to solvers of inequalities available in Maxima.

Issue created by migration from https://trac.sagemath.org/ticket/7325





---

archive/issue_comments_061094.json:
```json
{
    "body": "Attachment [inequalities.patch](tarball://root/attachments/some-uuid/ticket7325/inequalities.patch) by @robert-marik created at 2009-10-27 21:48:20",
    "created_at": "2009-10-27T21:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61094",
    "user": "https://github.com/robert-marik"
}
```

Attachment [inequalities.patch](tarball://root/attachments/some-uuid/ticket7325/inequalities.patch) by @robert-marik created at 2009-10-27 21:48:20



---

archive/issue_comments_061095.json:
```json
{
    "body": "The patch is a simple interface to two Maxima solvers. \n\nFor one inequality we use solve_rat_ineq from Maxima and for one or more inequalities written as list we use fourier_elim from Maxima.",
    "created_at": "2009-10-27T21:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61095",
    "user": "https://github.com/robert-marik"
}
```

The patch is a simple interface to two Maxima solvers. 

For one inequality we use solve_rat_ineq from Maxima and for one or more inequalities written as list we use fourier_elim from Maxima.



---

archive/issue_comments_061096.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-27T21:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61096",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061097.json:
```json
{
    "body": "Please note that #7155 also was about this - always check if a ticket already exists.  I have closed this.\n\nDoes this depend (for instance, for parsing 1#0) on any other tickets?  It is usually best if one builds on other Sage capacity, current or forthcoming.\n\nREVIEW:\nThe basic idea behind this ticket is good.  There is a new global solve_ineq (which could eventually be called from solve if it detects inequalities?), and two different inequality solvers for the univariate and multivariate cases.  So in general, this is on the right track.\n\nHowever, the implementation of the univariate solve is nearly all in one gigantic Maxima/Lisp command, as far as I can tell, and that makes it incredibly hard to read for the typical Sage/Python programmer.  It is not clear why the various options are there, nor what they do, because of this.  At the very least, the one gigantic command should be separated into smaller pieces, with comments, so that any future person can figure them out.\n\nThe output style makes sense, but many more examples would be welcome.  Is it possible that some of the stuff in the first example could be made easier using a little bit of Maxima parsing (e.g., sage.calculus.calculus.from_string_to_symbolic or whatever)?\n\nAlso, there are some nonstandard things.  *opts should probably be made more explicit - what are the options or keywords, exactly, that are expected?  All the line breaks make the code harder, not easier to read; Pythonic indentation should be used.  There are also some typos or slightly ungrammatical English (which is fine for a first patch, but a reviewer should eventually check), and the documentation is not in the normal markup format (see other examples, including in the same file, for prototypes, including blank lines and the :: stuff, or see the Sage developer's [guide](http://www.sagemath.org/doc/developer/)).  \n\nAll that said, assuming it works (which I trust it does, but am not currently checking since I can't understand the code), this will be a valuable addition to Sage, particularly since it has a framework that will allow addition of other inequality solving options - such as the upcoming improved to_poly_solve of Maxima, or one or more of the various linear programming solvers now included in Sage per default.",
    "created_at": "2009-10-28T00:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61097",
    "user": "https://github.com/kcrisman"
}
```

Please note that #7155 also was about this - always check if a ticket already exists.  I have closed this.

Does this depend (for instance, for parsing 1#0) on any other tickets?  It is usually best if one builds on other Sage capacity, current or forthcoming.

REVIEW:
The basic idea behind this ticket is good.  There is a new global solve_ineq (which could eventually be called from solve if it detects inequalities?), and two different inequality solvers for the univariate and multivariate cases.  So in general, this is on the right track.

However, the implementation of the univariate solve is nearly all in one gigantic Maxima/Lisp command, as far as I can tell, and that makes it incredibly hard to read for the typical Sage/Python programmer.  It is not clear why the various options are there, nor what they do, because of this.  At the very least, the one gigantic command should be separated into smaller pieces, with comments, so that any future person can figure them out.

The output style makes sense, but many more examples would be welcome.  Is it possible that some of the stuff in the first example could be made easier using a little bit of Maxima parsing (e.g., sage.calculus.calculus.from_string_to_symbolic or whatever)?

Also, there are some nonstandard things.  *opts should probably be made more explicit - what are the options or keywords, exactly, that are expected?  All the line breaks make the code harder, not easier to read; Pythonic indentation should be used.  There are also some typos or slightly ungrammatical English (which is fine for a first patch, but a reviewer should eventually check), and the documentation is not in the normal markup format (see other examples, including in the same file, for prototypes, including blank lines and the :: stuff, or see the Sage developer's [guide](http://www.sagemath.org/doc/developer/)).  

All that said, assuming it works (which I trust it does, but am not currently checking since I can't understand the code), this will be a valuable addition to Sage, particularly since it has a framework that will allow addition of other inequality solving options - such as the upcoming improved to_poly_solve of Maxima, or one or more of the various linear programming solvers now included in Sage per default.



---

archive/issue_comments_061098.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-28T00:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61098",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061099.json:
```json
{
    "body": "Many thanks for valuable comments. I am still newbie in this and I'll try to improve patch according to your suggestions. \n\nIt was intended as nothing more than interface to commands available in Maxima. \n\nBtw: This one huge lisp command comes also from Maxima -- it is nothing more than a fix for the bug [SF 2882408](http://sourceforge.net/tracker/?func=detail&aid=2882408&group_id=4933&atid=104933) and should be removed after fixing this Maxima bug. Hence only few lines remain, like in other interfaces to Maxima commands.",
    "created_at": "2009-10-30T12:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61099",
    "user": "https://github.com/robert-marik"
}
```

Many thanks for valuable comments. I am still newbie in this and I'll try to improve patch according to your suggestions. 

It was intended as nothing more than interface to commands available in Maxima. 

Btw: This one huge lisp command comes also from Maxima -- it is nothing more than a fix for the bug [SF 2882408](http://sourceforge.net/tracker/?func=detail&aid=2882408&group_id=4933&atid=104933) and should be removed after fixing this Maxima bug. Hence only few lines remain, like in other interfaces to Maxima commands.



---

archive/issue_comments_061100.json:
```json
{
    "body": "New patch. Before applying this patch, you are strongly recomended to update the file \nlocal/share/maxima/5.19.1/share/contrib/solve_rat_ineq.mac to [fixed version](http://maxima.cvs.sourceforge.net/viewvc/*checkout*/maxima/maxima/share/contrib/solve_rat_ineq.mac?revision=1.8).\n\nThe package does not parse maxima's output involwing 'not equal', like x#0. Perhaps trac #1163 or another trac resolve this problem later.",
    "created_at": "2009-11-09T23:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61100",
    "user": "https://github.com/robert-marik"
}
```

New patch. Before applying this patch, you are strongly recomended to update the file 
local/share/maxima/5.19.1/share/contrib/solve_rat_ineq.mac to [fixed version](http://maxima.cvs.sourceforge.net/viewvc/*checkout*/maxima/maxima/share/contrib/solve_rat_ineq.mac?revision=1.8).

The package does not parse maxima's output involwing 'not equal', like x#0. Perhaps trac #1163 or another trac resolve this problem later.



---

archive/issue_comments_061101.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-09T23:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61101",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061102.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2009-11-09T23:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61102",
    "user": "https://github.com/robert-marik"
}
```

apply only this patch



---

archive/issue_comments_061103.json:
```json
{
    "body": "Attachment [trac-7325-inequalities-revisited.patch](tarball://root/attachments/some-uuid/ticket7325/trac-7325-inequalities-revisited.patch) by @robert-marik created at 2009-11-09 23:34:03\n\napply only this patch",
    "created_at": "2009-11-09T23:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61103",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-7325-inequalities-revisited.patch](tarball://root/attachments/some-uuid/ticket7325/trac-7325-inequalities-revisited.patch) by @robert-marik created at 2009-11-09 23:34:03

apply only this patch



---

archive/issue_comments_061104.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-10T03:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61104",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061105.json:
```json
{
    "body": "Attachment [trac-7325-inequalities-revisited.2.patch](tarball://root/attachments/some-uuid/ticket7325/trac-7325-inequalities-revisited.2.patch) by @kcrisman created at 2009-11-10 03:04:48\n\n#1163 has now been updated to parse not equal, at least hopefully; ideally, this patch would be able to use that - or one could open a new ticket.  \n\nAs for the current patch, it is a vast improvement on the previous one for readability.  There are still a few formatting things - for INPUT and OUTPUT I think only : is needed, not ::, for instance.  For solve_ineq_univar and solve_ineq_fourier, the output should probably be formatted as a list, like the input is.  The input in solve_ineq (one could say, \"an inequality or list of inequalities\" or something like that) should not make it look like one can put in ineq twice.\n\nPerhaps this should come with a new Maxima spkg?  It does not pass tests upon being applied to 4.2.1.alpha0, and this is a prerequisite for inclusion of a patch.  However, probably this only requires a change to the spkg by applying the patch mentioned above - in fact, the current Maxima has a (now unnecessary, as it happens) patch on it too, and so probably one can follow that example for how to get them to apply that way (rather than packaging up a whole new one).  See the [Sage developers' guide](http://www.sagemath.org/doc/developer/), especially the part about [new spkgs](http://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg-file).",
    "created_at": "2009-11-10T03:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61105",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac-7325-inequalities-revisited.2.patch](tarball://root/attachments/some-uuid/ticket7325/trac-7325-inequalities-revisited.2.patch) by @kcrisman created at 2009-11-10 03:04:48

#1163 has now been updated to parse not equal, at least hopefully; ideally, this patch would be able to use that - or one could open a new ticket.  

As for the current patch, it is a vast improvement on the previous one for readability.  There are still a few formatting things - for INPUT and OUTPUT I think only : is needed, not ::, for instance.  For solve_ineq_univar and solve_ineq_fourier, the output should probably be formatted as a list, like the input is.  The input in solve_ineq (one could say, "an inequality or list of inequalities" or something like that) should not make it look like one can put in ineq twice.

Perhaps this should come with a new Maxima spkg?  It does not pass tests upon being applied to 4.2.1.alpha0, and this is a prerequisite for inclusion of a patch.  However, probably this only requires a change to the spkg by applying the patch mentioned above - in fact, the current Maxima has a (now unnecessary, as it happens) patch on it too, and so probably one can follow that example for how to get them to apply that way (rather than packaging up a whole new one).  See the [Sage developers' guide](http://www.sagemath.org/doc/developer/), especially the part about [new spkgs](http://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg-file).



---

archive/issue_comments_061106.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-11T13:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61106",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061107.json:
```json
{
    "body": "The updated spkg package for Maxima is at [http://user.mendelu.cz/marik/sage/maxima-5.19.1.p1.spkg](http://user.mendelu.cz/marik/sage/maxima-5.19.1.p1.spkg).\nInstall this new spkg to make examples introduced in patch work (they are choosen to ensure that the file solve_rat_ineq.mac has been fixed).\n\nThe updated patch is trac-7325-inequalities-3.patch\n\nApply only this patch",
    "created_at": "2009-11-11T13:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61107",
    "user": "https://github.com/robert-marik"
}
```

The updated spkg package for Maxima is at [http://user.mendelu.cz/marik/sage/maxima-5.19.1.p1.spkg](http://user.mendelu.cz/marik/sage/maxima-5.19.1.p1.spkg).
Install this new spkg to make examples introduced in patch work (they are choosen to ensure that the file solve_rat_ineq.mac has been fixed).

The updated patch is trac-7325-inequalities-3.patch

Apply only this patch



---

archive/issue_comments_061108.json:
```json
{
    "body": "Attachment [trac-7325-inequalities-3.patch](tarball://root/attachments/some-uuid/ticket7325/trac-7325-inequalities-3.patch) by @robert-marik created at 2009-11-11 13:50:29\n\nApply only thisd patch and update maxima spkg (the link is in discussion, message from November 11 2009)",
    "created_at": "2009-11-11T13:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61108",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-7325-inequalities-3.patch](tarball://root/attachments/some-uuid/ticket7325/trac-7325-inequalities-3.patch) by @robert-marik created at 2009-11-11 13:50:29

Apply only thisd patch and update maxima spkg (the link is in discussion, message from November 11 2009)



---

archive/issue_comments_061109.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T19:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61109",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061110.json:
```json
{
    "body": "Positive review!  Apparently a couple things changed in terms of the Maxima (for the better) on this spkg, so I rearranged the doctests to indicate this, and I added a few doctests at the top of the file, copied from below, so it is easy to see on the reference guide.  Otherwise, nice!   \n\nTo release manager: apply only 'final' patch.",
    "created_at": "2009-11-17T19:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61110",
    "user": "https://github.com/kcrisman"
}
```

Positive review!  Apparently a couple things changed in terms of the Maxima (for the better) on this spkg, so I rearranged the doctests to indicate this, and I added a few doctests at the top of the file, copied from below, so it is easy to see on the reference guide.  Otherwise, nice!   

To release manager: apply only 'final' patch.



---

archive/issue_comments_061111.json:
```json
{
    "body": "Attachment [trac_7325-final.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325-final.patch) by @kcrisman created at 2009-11-17 19:57:03\n\nBased on 4.2.1, apply only this patch and the spkg.",
    "created_at": "2009-11-17T19:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61111",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_7325-final.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325-final.patch) by @kcrisman created at 2009-11-17 19:57:03

Based on 4.2.1, apply only this patch and the spkg.



---

archive/issue_comments_061112.json:
```json
{
    "body": "An updated Maxima spkg is available at\n\nhttp://sage.math.washington.edu/home/mhansen/maxima-5.19.1.p2.spkg\n\nA related ticket is #7287.",
    "created_at": "2009-12-03T01:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61112",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

An updated Maxima spkg is available at

http://sage.math.washington.edu/home/mhansen/maxima-5.19.1.p2.spkg

A related ticket is #7287.



---

archive/issue_comments_061113.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-03T01:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61113",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_061114.json:
```json
{
    "body": "With the new Maxima spkg and the patch `trac_7325-final.patch`, I got these failures:\n\n```\n[mvngu@sage sage-4.3.alpha0-maxima]$ ./sage -t -long devel/sage-main/sage/symbolic/relation.py \nsage -t -long \"devel/sage-main/sage/symbolic/relation.py\"   \n**********************************************************************\nFile \"/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py\", line 152:\n    sage: solve_ineq([log(x)>log(y)])\nExpected:\n    [y < x, 0 < y]\nGot:\n    [0 < y, y < x, 0 < x]\n**********************************************************************\nFile \"/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py\", line 909:\n    sage: solve_ineq_fourier([x+y<9,x-y>4])\nExpected:\n    [y + 4 < x, x < -y + 9, y < (5/2)]\nGot:\n    [y < min(x - 4, -x + 9)]\n**********************************************************************\nFile \"/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py\", line 918:\n    sage: solve_ineq_fourier([log(x)>log(y)])\nExpected:\n    [y < x, 0 < y]\nGot:\n    [0 < y, y < x, 0 < x]\n**********************************************************************\nFile \"/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py\", line 999:\n    sage: solve_ineq([x+y<9,x-y>3])\nExpected:\n    [y + 3 < x, x < -y + 9, y < 3]\nGot:\n    [y < min(x - 3, -x + 9)]\n**********************************************************************\n3 items had failures:\n   1 of 117 in __main__.example_0\n   2 of   8 in __main__.example_7\n   1 of   8 in __main__.example_8\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_relation.py\n         [6.9 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage-main/sage/symbolic/relation.py\"\n```\n",
    "created_at": "2009-12-03T01:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61114",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

With the new Maxima spkg and the patch `trac_7325-final.patch`, I got these failures:

```
[mvngu@sage sage-4.3.alpha0-maxima]$ ./sage -t -long devel/sage-main/sage/symbolic/relation.py 
sage -t -long "devel/sage-main/sage/symbolic/relation.py"   
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py", line 152:
    sage: solve_ineq([log(x)>log(y)])
Expected:
    [y < x, 0 < y]
Got:
    [0 < y, y < x, 0 < x]
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py", line 909:
    sage: solve_ineq_fourier([x+y<9,x-y>4])
Expected:
    [y + 4 < x, x < -y + 9, y < (5/2)]
Got:
    [y < min(x - 4, -x + 9)]
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py", line 918:
    sage: solve_ineq_fourier([log(x)>log(y)])
Expected:
    [y < x, 0 < y]
Got:
    [0 < y, y < x, 0 < x]
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py", line 999:
    sage: solve_ineq([x+y<9,x-y>3])
Expected:
    [y + 3 < x, x < -y + 9, y < 3]
Got:
    [y < min(x - 3, -x + 9)]
**********************************************************************
3 items had failures:
   1 of 117 in __main__.example_0
   2 of   8 in __main__.example_7
   1 of   8 in __main__.example_8
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_relation.py
         [6.9 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-main/sage/symbolic/relation.py"
```




---

archive/issue_comments_061115.json:
```json
{
    "body": "This is weird.  Can you check this on a couple different platforms?  The -final patch was changed precisely because the Maxima results had changed for me, so maybe there is something different going on here.\n\nAlso, what ticket does the Maxima upgrade belong to, if any?",
    "created_at": "2009-12-03T02:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61115",
    "user": "https://github.com/kcrisman"
}
```

This is weird.  Can you check this on a couple different platforms?  The -final patch was changed precisely because the Maxima results had changed for me, so maybe there is something different going on here.

Also, what ticket does the Maxima upgrade belong to, if any?



---

archive/issue_comments_061116.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> This is weird.  Can you check this on a couple different platforms?  The -final patch was changed precisely because the Maxima results had changed for me, so maybe there is something different going on here.\n> \n> Also, what ticket does the Maxima upgrade belong to, if any?\n\nSorry, this question was answered on another ticket - I see, it has the ECL and this change in it.  Great!  Incidentally, Maxima should have another point release soon, which means we would get a fair number of new fixes that way as well.",
    "created_at": "2009-12-03T03:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61116",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:10 kcrisman]:
> This is weird.  Can you check this on a couple different platforms?  The -final patch was changed precisely because the Maxima results had changed for me, so maybe there is something different going on here.
> 
> Also, what ticket does the Maxima upgrade belong to, if any?

Sorry, this question was answered on another ticket - I see, it has the ECL and this change in it.  Great!  Incidentally, Maxima should have another point release soon, which means we would get a fair number of new fixes that way as well.



---

archive/issue_comments_061117.json:
```json
{
    "body": "Replying to [comment:9 mvngu]:\n> With the new Maxima spkg and the patch `trac_7325-final.patch`, I got these failures:\n\nThis follows probably from updated version of fourier elimination in Maxima. The answers are correct and equivalent to previous answers. I think that it is sufficient to fix the tests and to fix the following message from solve command\n\n```\nNotImplementedError: solving only implemented for equalities\n```\n\n\nI'll update the patches after testing on 4.3.rc1\n\nwhat about to replace output of \n\n```\nsolve_ineq(x^2>-1)\n```\n\nfrom \n\n```\n'all'\n```\n\nto \n\n```\nx>-Infinity\n```\n\n?",
    "created_at": "2009-12-04T21:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61117",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:9 mvngu]:
> With the new Maxima spkg and the patch `trac_7325-final.patch`, I got these failures:

This follows probably from updated version of fourier elimination in Maxima. The answers are correct and equivalent to previous answers. I think that it is sufficient to fix the tests and to fix the following message from solve command

```
NotImplementedError: solving only implemented for equalities
```


I'll update the patches after testing on 4.3.rc1

what about to replace output of 

```
solve_ineq(x^2>-1)
```

from 

```
'all'
```

to 

```
x>-Infinity
```

?



---

archive/issue_comments_061118.json:
```json
{
    "body": "Attachment [trac_7325-final-2.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325-final-2.patch) by @robert-marik created at 2009-12-05 21:48:09\n\napply after trac_7325-final.patch",
    "created_at": "2009-12-05T21:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61118",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac_7325-final-2.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325-final-2.patch) by @robert-marik created at 2009-12-05 21:48:09

apply after trac_7325-final.patch



---

archive/issue_comments_061119.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-05T21:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61119",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061120.json:
```json
{
    "body": "btw: with sage 4.3. you need not to install new Maxima spkg, install only final and final-2 patches. Tested on rc1.",
    "created_at": "2009-12-09T21:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61120",
    "user": "https://github.com/robert-marik"
}
```

btw: with sage 4.3. you need not to install new Maxima spkg, install only final and final-2 patches. Tested on rc1.



---

archive/issue_comments_061121.json:
```json
{
    "body": "Does this all work well with the new Maxima (see [http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7](http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7) as well?  Sorry for not having time to review this carefully yet.",
    "created_at": "2009-12-21T02:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61121",
    "user": "https://github.com/kcrisman"
}
```

Does this all work well with the new Maxima (see [http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7](http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7) as well?  Sorry for not having time to review this carefully yet.



---

archive/issue_comments_061122.json:
```json
{
    "body": "Replying to [comment:15 kcrisman]:\n> Does this all work well with the new Maxima (see [http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7](http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7) as well?  \n\nNot tested on Maxima 5.20.1 - this version is not available in Sage and ticket #7745 is not closed yet.",
    "created_at": "2009-12-21T06:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61122",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:15 kcrisman]:
> Does this all work well with the new Maxima (see [http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7](http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7) as well?  

Not tested on Maxima 5.20.1 - this version is not available in Sage and ticket #7745 is not closed yet.



---

archive/issue_comments_061123.json:
```json
{
    "body": "Attachment [trac_7325_rebased_4.3.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325_rebased_4.3.patch) by @robert-marik created at 2009-12-27 18:07:01\n\nMerged two final patches and rebased for Sage 4.3. Apply only this patch.",
    "created_at": "2009-12-27T18:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61123",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac_7325_rebased_4.3.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325_rebased_4.3.patch) by @robert-marik created at 2009-12-27 18:07:01

Merged two final patches and rebased for Sage 4.3. Apply only this patch.



---

archive/issue_comments_061124.json:
```json
{
    "body": "Attachment [trac_7325_rebased_4.3.2.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325_rebased_4.3.2.patch) by @robert-marik created at 2009-12-27 18:09:52\n\nMerged both final patches and rebased for Sage 4.3.",
    "created_at": "2009-12-27T18:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61124",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac_7325_rebased_4.3.2.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325_rebased_4.3.2.patch) by @robert-marik created at 2009-12-27 18:09:52

Merged both final patches and rebased for Sage 4.3.



---

archive/issue_comments_061125.json:
```json
{
    "body": "I had some problems with trac server and by accident inserted the patch two times. Both are identical, apply only trac_7325_rebased_4.3.patch . Thanks.",
    "created_at": "2009-12-27T18:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61125",
    "user": "https://github.com/robert-marik"
}
```

I had some problems with trac server and by accident inserted the patch two times. Both are identical, apply only trac_7325_rebased_4.3.patch . Thanks.



---

archive/issue_comments_061126.json:
```json
{
    "body": "Works well also with Maxima 5.20.1. (However, the patch #7745 does not install cleanly with tha patch for this ticket and some parts have to be fixed manualy.)",
    "created_at": "2009-12-27T18:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61126",
    "user": "https://github.com/robert-marik"
}
```

Works well also with Maxima 5.20.1. (However, the patch #7745 does not install cleanly with tha patch for this ticket and some parts have to be fixed manualy.)



---

archive/issue_comments_061127.json:
```json
{
    "body": "I will hopefully soon have time to actually test this - thanks for your patience!  Here are a few things to keep in mind for when you rebase to 4.3.1.alpha1 (as #7745 is now merged).\n\n0. Rebase, of course :)\n\n1. I think I agree that x>-Infinity is much more \"Sage-like\", or maybe `[x>-Infinity]` would be more in keeping with the other solutions.   Good thought.  Or maybe `[x>-Infinity, x<Infinity]` ?  I'm not sure about that.\n\n2. Probably ```special cases``` shouldn't be in the quoting environment.  In fact, [] and the above are both lists, so you would just need to clarify what they mean.\n\n3. Something similar should happen with multivariate.  Here, there is also a small inconsistency involved - `[0 < y, y < x, 0 < x]` for multivariate, but `[This is the Trac macro *0 < y, y < x, 0 < x* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0 < y, y < x, 0 < x-macro)` seems to be the univariate result type.  \n\n4. In calculus/calculus.py, there is the following code:\n\n```\nmaxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(to_poly_solver)', 'load(simplify_sum)'],\n                script_subdirectory=None)\n```\n\nMaybe the initialization of solve_rat_ineq and fourier_elim should be there?   Otherwise we are trying to load this with every attempt at a solve_ineq, which seems inefficient.\n\n5. Looking at things, I wonder if it would be possible (without too many bugs) to actually implement ineq.solve(), not just solve(ineq) - that is, in relation.py and expression.py, rather than having solve() gag on inequalities, have it at least try the solve_ineq and just catch any exceptions that are raised and instead raise a NotImplementedError for that particular inequality.  I wonder?\n\nBut as before, a great addition to Sage - just trying to get the maximum benefit from this ticket!  Thanks again.",
    "created_at": "2010-01-08T16:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61127",
    "user": "https://github.com/kcrisman"
}
```

I will hopefully soon have time to actually test this - thanks for your patience!  Here are a few things to keep in mind for when you rebase to 4.3.1.alpha1 (as #7745 is now merged).

0. Rebase, of course :)

1. I think I agree that x>-Infinity is much more "Sage-like", or maybe `[x>-Infinity]` would be more in keeping with the other solutions.   Good thought.  Or maybe `[x>-Infinity, x<Infinity]` ?  I'm not sure about that.

2. Probably ```special cases``` shouldn't be in the quoting environment.  In fact, [] and the above are both lists, so you would just need to clarify what they mean.

3. Something similar should happen with multivariate.  Here, there is also a small inconsistency involved - `[0 < y, y < x, 0 < x]` for multivariate, but `[This is the Trac macro *0 < y, y < x, 0 < x* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0 < y, y < x, 0 < x-macro)` seems to be the univariate result type.  

4. In calculus/calculus.py, there is the following code:

```
maxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(to_poly_solver)', 'load(simplify_sum)'],
                script_subdirectory=None)
```

Maybe the initialization of solve_rat_ineq and fourier_elim should be there?   Otherwise we are trying to load this with every attempt at a solve_ineq, which seems inefficient.

5. Looking at things, I wonder if it would be possible (without too many bugs) to actually implement ineq.solve(), not just solve(ineq) - that is, in relation.py and expression.py, rather than having solve() gag on inequalities, have it at least try the solve_ineq and just catch any exceptions that are raised and instead raise a NotImplementedError for that particular inequality.  I wonder?

But as before, a great addition to Sage - just trying to get the maximum benefit from this ticket!  Thanks again.



---

archive/issue_comments_061128.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-08T16:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61128",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061129.json:
```json
{
    "body": "Replying to [comment:19 kcrisman]:\n> \n> 4. In calculus/calculus.py, there is the following code:\n> {{{\n> maxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(to_poly_solver)', 'load(simplify_sum)'],\n>                 script_subdirectory=None)\n> }}}\n> Maybe the initialization of solve_rat_ineq and fourier_elim should be there?   Otherwise we are trying to load this with every attempt at a solve_ineq, which seems inefficient.\n\nI think that it is inefficient to load a bundle of packages whenever Maxima starts. This makes computations provided by Maxima slower. Perhaps we could use some variable swhich stores information, whether solvers of inequality have been used or no. \n\n\nAnd thanks for the other comments.",
    "created_at": "2010-01-08T21:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61129",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:19 kcrisman]:
> 
> 4. In calculus/calculus.py, there is the following code:
> {{{
> maxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(to_poly_solver)', 'load(simplify_sum)'],
>                 script_subdirectory=None)
> }}}
> Maybe the initialization of solve_rat_ineq and fourier_elim should be there?   Otherwise we are trying to load this with every attempt at a solve_ineq, which seems inefficient.

I think that it is inefficient to load a bundle of packages whenever Maxima starts. This makes computations provided by Maxima slower. Perhaps we could use some variable swhich stores information, whether solvers of inequality have been used or no. 


And thanks for the other comments.



---

archive/issue_comments_061130.json:
```json
{
    "body": "Replying to [comment:20 robert.marik]:\n> I think that it is inefficient to load a bundle of packages whenever Maxima starts. This makes computations provided by Maxima slower. Perhaps we could use some variable swhich stores information, whether solvers of inequality have been used or no. \n\nCould you explain how loading these packages makes Maxima's computations slower?  I'm not sure I follow.",
    "created_at": "2010-01-08T21:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61130",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:20 robert.marik]:
> I think that it is inefficient to load a bundle of packages whenever Maxima starts. This makes computations provided by Maxima slower. Perhaps we could use some variable swhich stores information, whether solvers of inequality have been used or no. 

Could you explain how loading these packages makes Maxima's computations slower?  I'm not sure I follow.



---

archive/issue_comments_061131.json:
```json
{
    "body": "> > 4. In calculus/calculus.py, there is the following code:\n> > {{{\n> > maxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(to_poly_solver)', 'load(simplify_sum)'],\n> >                 script_subdirectory=None)\n> > }}}\n> > Maybe the initialization of solve_rat_ineq and fourier_elim should be there?   Otherwise we are trying to load this with every attempt at a solve_ineq, which seems inefficient.\n> \n> I think that it is inefficient to load a bundle of packages whenever Maxima starts. This makes computations provided by Maxima slower. Perhaps we could use some variable swhich stores information, whether solvers of inequality have been used or no. \n> \n\nIf you think that is a good way of doing it, then we should also do this for the loading of simplify_sum and to_poly_solve, because certainly they would be in the same boat.  Does checking a boolean sound appropriate?  If you do that here, then I would be happy to do it in the other places.\n\nTo mhansen: I think robert.marik is referring to the making it a slightly slower startup, not the actual computations.  It's true that loading tons of packages would eventually slow that down if someone just wanted to get an integral.",
    "created_at": "2010-01-08T21:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61131",
    "user": "https://github.com/kcrisman"
}
```

> > 4. In calculus/calculus.py, there is the following code:
> > {{{
> > maxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(to_poly_solver)', 'load(simplify_sum)'],
> >                 script_subdirectory=None)
> > }}}
> > Maybe the initialization of solve_rat_ineq and fourier_elim should be there?   Otherwise we are trying to load this with every attempt at a solve_ineq, which seems inefficient.
> 
> I think that it is inefficient to load a bundle of packages whenever Maxima starts. This makes computations provided by Maxima slower. Perhaps we could use some variable swhich stores information, whether solvers of inequality have been used or no. 
> 

If you think that is a good way of doing it, then we should also do this for the loading of simplify_sum and to_poly_solve, because certainly they would be in the same boat.  Does checking a boolean sound appropriate?  If you do that here, then I would be happy to do it in the other places.

To mhansen: I think robert.marik is referring to the making it a slightly slower startup, not the actual computations.  It's true that loading tons of packages would eventually slow that down if someone just wanted to get an integral.



---

archive/issue_comments_061132.json:
```json
{
    "body": "Rebased and improved, apply only this patch, added support for (x^2-1>0).solve(x)",
    "created_at": "2010-01-22T15:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61132",
    "user": "https://github.com/robert-marik"
}
```

Rebased and improved, apply only this patch, added support for (x^2-1>0).solve(x)



---

archive/issue_comments_061133.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-22T15:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61133",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061134.json:
```json
{
    "body": "Attachment [trac_7325_rebased_4.3.1.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325_rebased_4.3.1.patch) by @robert-marik created at 2010-01-22 15:29:57\n\nThe last patch solves (I hope) the problems from above.\n\nI found a Maxima bug when solving x^4+2>0 - the problem is from Maxima (and not related to this ticket) and should be easy to fix. Reported at Maxima forum, will be reported on SF with a solution how to fix (in few days or weeks).",
    "created_at": "2010-01-22T15:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61134",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac_7325_rebased_4.3.1.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325_rebased_4.3.1.patch) by @robert-marik created at 2010-01-22 15:29:57

The last patch solves (I hope) the problems from above.

I found a Maxima bug when solving x^4+2>0 - the problem is from Maxima (and not related to this ticket) and should be easy to fix. Reported at Maxima forum, will be reported on SF with a solution how to fix (in few days or weeks).



---

archive/issue_comments_061135.json:
```json
{
    "body": "Just for the record: the problem related to inequality\n\n```\nsage:(x^4+2>0).solve(x)\n[[x > -(-1)^(1/4)*2^(1/4), x < (-1)^(1/4)*2^(1/4)]]\n```\n\nis caused by a known [bug](http://sourceforge.net/tracker/?func=detail&aid=2786017&group_id=4933&atid=104933) in algsys and should be fixed [soon](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29593).",
    "created_at": "2010-01-22T20:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61135",
    "user": "https://github.com/robert-marik"
}
```

Just for the record: the problem related to inequality

```
sage:(x^4+2>0).solve(x)
[[x > -(-1)^(1/4)*2^(1/4), x < (-1)^(1/4)*2^(1/4)]]
```

is caused by a known [bug](http://sourceforge.net/tracker/?func=detail&aid=2786017&group_id=4933&atid=104933) in algsys and should be fixed [soon](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29593).



---

archive/issue_comments_061136.json:
```json
{
    "body": "Robert,\n\nOverall this is really good now.  One possible thing is what the best way to implement the checking for whether things are already loaded - I have no idea whether this is more efficient than before or not, truthfully, I probably should have brought it up.  The other is that usually one imports maxima from sage.calculus.calculus and then one doesn't have to always check the parents.  But since this is new code and not slowing down old code, that can wait - it's really time we have this.\n\nI am still waiting for 4.3.1 to make check on my dev machine, but once it does I will try this out once again and add a tiny reviewer patch - there is a one-character typo, for instance.  Thanks for all your hard work on this!\n\nReplying to [comment:24 robert.marik]:\n> Just for the record: the problem related to inequality\n> {{{\n> sage:(x^4+2>0).solve(x)\n> [This is the Trac macro *x > -* that was inherited from the migration called with arguments (-1)<sup>)](https://trac.sagemath.org/wiki/WikiMacros#x > --macro)\n> }}}\n> is caused by a known [bug](http://sourceforge.net/tracker/?func=detail&aid=2786017&group_id=4933&atid=104933) in algsys and should be fixed [soon](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29593).\nCan you open a ticket for this and put it as \"Reported upstream, \" etc.?  Even though it's not a Sage bug, we might as well track it - I don't see the need to upgrade Maxima every time they fix a minor bug that affects Sage, but if there is a ticket for it then when there are enough such tickets that are resolved upstream we will see the need to upgrade.",
    "created_at": "2010-01-23T01:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61136",
    "user": "https://github.com/kcrisman"
}
```

Robert,

Overall this is really good now.  One possible thing is what the best way to implement the checking for whether things are already loaded - I have no idea whether this is more efficient than before or not, truthfully, I probably should have brought it up.  The other is that usually one imports maxima from sage.calculus.calculus and then one doesn't have to always check the parents.  But since this is new code and not slowing down old code, that can wait - it's really time we have this.

I am still waiting for 4.3.1 to make check on my dev machine, but once it does I will try this out once again and add a tiny reviewer patch - there is a one-character typo, for instance.  Thanks for all your hard work on this!

Replying to [comment:24 robert.marik]:
> Just for the record: the problem related to inequality
> {{{
> sage:(x^4+2>0).solve(x)
> [This is the Trac macro *x > -* that was inherited from the migration called with arguments (-1)<sup>)](https://trac.sagemath.org/wiki/WikiMacros#x > --macro)
> }}}
> is caused by a known [bug](http://sourceforge.net/tracker/?func=detail&aid=2786017&group_id=4933&atid=104933) in algsys and should be fixed [soon](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29593).
Can you open a ticket for this and put it as "Reported upstream, " etc.?  Even though it's not a Sage bug, we might as well track it - I don't see the need to upgrade Maxima every time they fix a minor bug that affects Sage, but if there is a ticket for it then when there are enough such tickets that are resolved upstream we will see the need to upgrade.



---

archive/issue_comments_061137.json:
```json
{
    "body": "Hmm, weird in line 5932 (the log(x) log(y) solving inequality) I get a doctest error, where instead of three conditions, I get the (simpler) equivalent two conditions 0<y, y<x or whatever.  If I instead add the condition [y,x], I get the result in the doctest, while [x,y] gives the result that is documented for [x,y].  The same happens on the one with the min in the same doctests.  Could the reason be the same as you mentioned above (changes in the fourier_elim, yet again), or perhaps truly a platform issue (I am on Macintel)?\n\nAargh, it was so close!  But I am sure this can be easily resolved.  I do like the way you dealt with the \"or\" things, by the way.  It would be nice to wrap that for understanding general Maxima results (like from to_poly_solve), obviously not in this ticket.",
    "created_at": "2010-01-23T03:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61137",
    "user": "https://github.com/kcrisman"
}
```

Hmm, weird in line 5932 (the log(x) log(y) solving inequality) I get a doctest error, where instead of three conditions, I get the (simpler) equivalent two conditions 0<y, y<x or whatever.  If I instead add the condition [y,x], I get the result in the doctest, while [x,y] gives the result that is documented for [x,y].  The same happens on the one with the min in the same doctests.  Could the reason be the same as you mentioned above (changes in the fourier_elim, yet again), or perhaps truly a platform issue (I am on Macintel)?

Aargh, it was so close!  But I am sure this can be easily resolved.  I do like the way you dealt with the "or" things, by the way.  It would be nice to wrap that for understanding general Maxima results (like from to_poly_solve), obviously not in this ticket.



---

archive/issue_comments_061138.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-23T03:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61138",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061139.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-26T12:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61139",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061140.json:
```json
{
    "body": "I do not know why doctests failed. Perhaps some nonstandard settings in my .maxima file. Anyway, I replaced the doctests with simpler ones.\n\nThere is one related bug which has been fixed in Maxima CVS: #8078",
    "created_at": "2010-01-26T12:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61140",
    "user": "https://github.com/robert-marik"
}
```

I do not know why doctests failed. Perhaps some nonstandard settings in my .maxima file. Anyway, I replaced the doctests with simpler ones.

There is one related bug which has been fixed in Maxima CVS: #8078



---

archive/issue_comments_061141.json:
```json
{
    "body": "Replying to [comment:27 robert.marik]:\n> I do not know why doctests failed. Perhaps some nonstandard settings in my .maxima file. Anyway, I replaced the doctests with simpler ones.\nNo, we should document behavior like this so that people aren't confused; until it's 100% clear why it's happening, we shouldn't cover it up.  If I get some time, I will try to track it down using sage.math and my own box; you have clearly done enough work on this patch to deserve a break :)\n\n> There is one related bug which has been fixed in Maxima CVS: #8078\nYes, thanks for reporting that one.",
    "created_at": "2010-01-26T13:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61141",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:27 robert.marik]:
> I do not know why doctests failed. Perhaps some nonstandard settings in my .maxima file. Anyway, I replaced the doctests with simpler ones.
No, we should document behavior like this so that people aren't confused; until it's 100% clear why it's happening, we shouldn't cover it up.  If I get some time, I will try to track it down using sage.math and my own box; you have clearly done enough work on this patch to deserve a break :)

> There is one related bug which has been fixed in Maxima CVS: #8078
Yes, thanks for reporting that one.



---

archive/issue_comments_061142.json:
```json
{
    "body": "There seems to be something wrong with attachment:trac_7325_2_rebased_for_4.3.1.patch. It contains two similar patches, with distinct headers etc. I didn't check if they are identical copies of the same patch.",
    "created_at": "2010-01-26T15:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61142",
    "user": "https://github.com/burcin"
}
```

There seems to be something wrong with attachment:trac_7325_2_rebased_for_4.3.1.patch. It contains two similar patches, with distinct headers etc. I didn't check if they are identical copies of the same patch.



---

archive/issue_comments_061143.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-26T18:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61143",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061144.json:
```json
{
    "body": "oops, i was not aware of the fact that if I use hg_sage.export() and the file exists, the output is attached to the end of the file. I will check everything and prepare new patch.",
    "created_at": "2010-01-26T18:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61144",
    "user": "https://github.com/robert-marik"
}
```

oops, i was not aware of the fact that if I use hg_sage.export() and the file exists, the output is attached to the end of the file. I will check everything and prepare new patch.



---

archive/issue_comments_061145.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2010-01-26T18:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61145",
    "user": "https://github.com/robert-marik"
}
```

apply only this patch



---

archive/issue_comments_061146.json:
```json
{
    "body": "Attachment [trac_7325_2_rebased_for_4.3.1.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325_2_rebased_for_4.3.1.patch) by @robert-marik created at 2010-01-26 18:55:29\n\nReplying to [comment:29 burcin]:\n> There seems to be something wrong with attachment:trac_7325_2_rebased_for_4.3.1.patch. It contains two similar patches, with distinct headers etc. I didn't check if they are identical copies of the same patch.\n\nFixed, thanks. Robert",
    "created_at": "2010-01-26T18:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61146",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac_7325_2_rebased_for_4.3.1.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325_2_rebased_for_4.3.1.patch) by @robert-marik created at 2010-01-26 18:55:29

Replying to [comment:29 burcin]:
> There seems to be something wrong with attachment:trac_7325_2_rebased_for_4.3.1.patch. It contains two similar patches, with distinct headers etc. I didn't check if they are identical copies of the same patch.

Fixed, thanks. Robert



---

archive/issue_comments_061147.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-26T18:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61147",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061148.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-29T20:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61148",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061149.json:
```json
{
    "body": "There were some additional examples which still were platform-dependent.  This is really weird, I have to say!    In particular, the following\n\n```\n                try:\n                    return(solve_ineq(self)) # trying solve_ineq_univar\n                except:\n                    pass\n                try:\n                    return(solve_ineq([self])) # trying solve_ineq_fourier\n```\n\nmeans that exp.solve(x) ignores the x.  However, I don't know that that is really worth changing since it still gives correct answers.\n\nThis patch should do it, hopefully it applies to alpha0.  The only changes were in doctests to ensure it passes, and to explain what is going on.  Perhaps it is in Maxima itself that this platform-dependence happens, but I don't have time to check this.\n\nAlso corrected two minor typos.",
    "created_at": "2010-01-29T20:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61149",
    "user": "https://github.com/kcrisman"
}
```

There were some additional examples which still were platform-dependent.  This is really weird, I have to say!    In particular, the following

```
                try:
                    return(solve_ineq(self)) # trying solve_ineq_univar
                except:
                    pass
                try:
                    return(solve_ineq([self])) # trying solve_ineq_fourier
```

means that exp.solve(x) ignores the x.  However, I don't know that that is really worth changing since it still gives correct answers.

This patch should do it, hopefully it applies to alpha0.  The only changes were in doctests to ensure it passes, and to explain what is going on.  Perhaps it is in Maxima itself that this platform-dependence happens, but I don't have time to check this.

Also corrected two minor typos.



---

archive/issue_comments_061150.json:
```json
{
    "body": "Based on 4.3.1",
    "created_at": "2010-01-29T20:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61150",
    "user": "https://github.com/kcrisman"
}
```

Based on 4.3.1



---

archive/issue_comments_061151.json:
```json
{
    "body": "Attachment [trac_7325-final-for-real.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325-final-for-real.patch) by @kcrisman created at 2010-01-29 20:16:54\n\nAnd as always, \"apply only this patch\".  :)",
    "created_at": "2010-01-29T20:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61151",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_7325-final-for-real.patch](tarball://root/attachments/some-uuid/ticket7325/trac_7325-final-for-real.patch) by @kcrisman created at 2010-01-29 20:16:54

And as always, "apply only this patch".  :)



---

archive/issue_comments_061152.json:
```json
{
    "body": "Replying to [comment:32 kcrisman]:\n> There were some additional examples which still were platform-dependent.  This is really weird, I have to say!    In particular, the following\n> {{{\n>                 try:\n>                     return(solve_ineq(self)) # trying solve_ineq_univar\n>                 except:\n>                     pass\n>                 try:\n>                     return(solve_ineq([self])) # trying solve_ineq_fourier\n> }}}\n> means that exp.solve(x) ignores the x.  However, I don't know that that is really worth changing since it still gives correct answers.\n\nPerhaps to explain in more details what happens for ineq.solve(x):\n\n* ineq has not equality sign, the previous version of solve command raised error, the new version excutes the code above\n\n* we try solve_ineq(self), i.e. we use the Maxima's solve_rat_ineq. This raises error if there are more than one variable and if the solve_rat_ineq is not polynomial or quotient of two polynomial (after moving right hand side to the left and simplifying). Hence this function does not need the name of the variable on input. this is because solve_rat_ineq handles rational inequalities better than fourier_elim",
    "created_at": "2010-01-29T20:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61152",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:32 kcrisman]:
> There were some additional examples which still were platform-dependent.  This is really weird, I have to say!    In particular, the following
> {{{
>                 try:
>                     return(solve_ineq(self)) # trying solve_ineq_univar
>                 except:
>                     pass
>                 try:
>                     return(solve_ineq([self])) # trying solve_ineq_fourier
> }}}
> means that exp.solve(x) ignores the x.  However, I don't know that that is really worth changing since it still gives correct answers.

Perhaps to explain in more details what happens for ineq.solve(x):

* ineq has not equality sign, the previous version of solve command raised error, the new version excutes the code above

* we try solve_ineq(self), i.e. we use the Maxima's solve_rat_ineq. This raises error if there are more than one variable and if the solve_rat_ineq is not polynomial or quotient of two polynomial (after moving right hand side to the left and simplifying). Hence this function does not need the name of the variable on input. this is because solve_rat_ineq handles rational inequalities better than fourier_elim



---

archive/issue_comments_061153.json:
```json
{
    "body": "Replying to [comment:34 robert.marik]:\n> Replying to [comment:32 kcrisman]:\n> > There were some additional examples which still were platform-dependent.  This is really weird, I have to say!    In particular, the following\n> > {{{\n> >                 try:\n> >                     return(solve_ineq(self)) # trying solve_ineq_univar\n> >                 except:\n> >                     pass\n> >                 try:\n> >                     return(solve_ineq([self])) # trying solve_ineq_fourier\n> > }}}\n> > means that exp.solve(x) ignores the x.  However, I don't know that that is really worth changing since it still gives correct answers.\n> \n> Perhaps to explain in more details what happens for ineq.solve(x):\n> \n> * ineq has not equality sign, the previous version of solve command raised error, the new version excutes the code above\n\nOh, yes, I understand, I am just suggesting that in the future solve itself (not just solve_ineq) could take the variable given into account as well.\n\n> \n> * we try solve_ineq(self), i.e. we use the Maxima's solve_rat_ineq. This raises error if there are more than one variable and if the solve_rat_ineq is not polynomial or quotient of two polynomial (after moving right hand side to the left and simplifying). Hence this function does not need the name of the variable on input. this is because solve_rat_ineq handles rational inequalities better than fourier_elim\n> \n\nYes, of course.  Again, just suggesting that in the future (because the variable order matters for some reason) that the variables could fit in here in the future.  It's still great work!\n\nIncidentally, on Linux:\n\n```\nsage: set((x,y))\nset([y, x])\n```\n\nOn Mac:\n\n```\nsage: set((x,y))\nset([x, y])\n```\n\nSo that is why we are seeing these changes.  Probably something other than set could solve this issue, so I may open a new ticket for that.",
    "created_at": "2010-01-30T02:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61153",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:34 robert.marik]:
> Replying to [comment:32 kcrisman]:
> > There were some additional examples which still were platform-dependent.  This is really weird, I have to say!    In particular, the following
> > {{{
> >                 try:
> >                     return(solve_ineq(self)) # trying solve_ineq_univar
> >                 except:
> >                     pass
> >                 try:
> >                     return(solve_ineq([self])) # trying solve_ineq_fourier
> > }}}
> > means that exp.solve(x) ignores the x.  However, I don't know that that is really worth changing since it still gives correct answers.
> 
> Perhaps to explain in more details what happens for ineq.solve(x):
> 
> * ineq has not equality sign, the previous version of solve command raised error, the new version excutes the code above

Oh, yes, I understand, I am just suggesting that in the future solve itself (not just solve_ineq) could take the variable given into account as well.

> 
> * we try solve_ineq(self), i.e. we use the Maxima's solve_rat_ineq. This raises error if there are more than one variable and if the solve_rat_ineq is not polynomial or quotient of two polynomial (after moving right hand side to the left and simplifying). Hence this function does not need the name of the variable on input. this is because solve_rat_ineq handles rational inequalities better than fourier_elim
> 

Yes, of course.  Again, just suggesting that in the future (because the variable order matters for some reason) that the variables could fit in here in the future.  It's still great work!

Incidentally, on Linux:

```
sage: set((x,y))
set([y, x])
```

On Mac:

```
sage: set((x,y))
set([x, y])
```

So that is why we are seeing these changes.  Probably something other than set could solve this issue, so I may open a new ticket for that.



---

archive/issue_comments_061154.json:
```json
{
    "body": "Merged only [trac_7325-final-for-real.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7325/trac_7325-final-for-real.patch).",
    "created_at": "2010-01-30T23:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61154",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged only [trac_7325-final-for-real.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7325/trac_7325-final-for-real.patch).



---

archive/issue_events_007547.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-01-30T23:39:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7325#event-7547"
}
```



---

archive/issue_comments_061155.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7325#issuecomment-61155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
