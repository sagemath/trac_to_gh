# Issue 6942: jordan_form with transformation=true returns non-invertible transformation

archive/issues_006942.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jasongrout\n\nKeywords: jordan_form, transformation\n\nThe following code returns an incorrect result:\n\n```\nmm=Matrix(GF(2),[[1,0,1,0,0,0,1],[1,0,0,1,1,1,0],[1,1,0,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,0,0,1,0],[1,1,1,0,1,0,0],[1,1,1,1,1,1,0]])\n_,S = mm.jordan_form(transformation=True)\nS.rank()\n```\n\nS should be invertible, so the rank should be 7, but the rank of the above is 5.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6942\n\n",
    "created_at": "2009-09-16T01:35:43Z",
    "labels": [
        "algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "jordan_form with transformation=true returns non-invertible transformation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6942",
    "user": "@syazdani77"
}
```
Assignee: tbd

CC:  @jasongrout

Keywords: jordan_form, transformation

The following code returns an incorrect result:

```
mm=Matrix(GF(2),[[1,0,1,0,0,0,1],[1,0,0,1,1,1,0],[1,1,0,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,0,0,1,0],[1,1,1,0,1,0,0],[1,1,1,1,1,1,0]])
_,S = mm.jordan_form(transformation=True)
S.rank()
```

S should be invertible, so the rank should be 7, but the rank of the above is 5.

Issue created by migration from https://trac.sagemath.org/ticket/6942





---

archive/issue_comments_057392.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2009-11-15T13:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57392",
    "user": "@aghitza"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_057393.json:
```json
{
    "body": "According to Magma:\n\n\n```\nu,v:=JordanForm(Matrix(GF(2),7,7,StringToIntegerSequence(\"1 0 1 0 0 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 0 1 0 1 1 1 0 1 0 0 1 1 1 1 1 1 0\")));\n\nprint \"jordan form:\";\nu;\nprint \"transformation\";\nv;\n\ngives\n\nMagma V2.15-14    Tue Nov 24 2009 10:36:58    [Seed = 4156006409]\n   -------------------------------------\n\njordan form:\n[1 0 0 0 0 0 0]\n[0 1 1 0 0 0 0]\n[0 0 1 0 0 0 0]\n[0 0 0 1 1 0 0]\n[0 0 0 0 1 0 0]\n[0 0 0 0 0 1 1]\n[0 0 0 0 0 0 1]\ntransformation\n[0 0 0 0 1 1 0]\n[0 0 0 0 0 0 1]\n[1 1 1 1 1 1 1]\n[0 0 0 0 0 1 0]\n[1 1 1 0 1 1 0]\n[1 0 1 0 0 0 0]\n[1 1 0 1 1 1 0]\n\nTotal time: 0.180 seconds, Total memory usage: 7.27MB\n```\n",
    "created_at": "2009-11-23T23:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57393",
    "user": "@jasongrout"
}
```

According to Magma:


```
u,v:=JordanForm(Matrix(GF(2),7,7,StringToIntegerSequence("1 0 1 0 0 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 0 1 0 1 1 1 0 1 0 0 1 1 1 1 1 1 0")));

print "jordan form:";
u;
print "transformation";
v;

gives

Magma V2.15-14    Tue Nov 24 2009 10:36:58    [Seed = 4156006409]
   -------------------------------------

jordan form:
[1 0 0 0 0 0 0]
[0 1 1 0 0 0 0]
[0 0 1 0 0 0 0]
[0 0 0 1 1 0 0]
[0 0 0 0 1 0 0]
[0 0 0 0 0 1 1]
[0 0 0 0 0 0 1]
transformation
[0 0 0 0 1 1 0]
[0 0 0 0 0 0 1]
[1 1 1 1 1 1 1]
[0 0 0 0 0 1 0]
[1 1 1 0 1 1 0]
[1 0 1 0 0 0 0]
[1 1 0 1 1 1 0]

Total time: 0.180 seconds, Total memory usage: 7.27MB
```




---

archive/issue_comments_057394.json:
```json
{
    "body": "Or more verbosely:\n\n\n```\nm:=Matrix(GF(2),7,7,StringToIntegerSequence(\"1 0 1 0 0 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 0 1 0 1 1 1 0 1 0 0 1 1 1 1 1 1 0\"));\njor,trans:=JordanForm(m);\n\nprint \"jordan form:\";\njor;\nprint \"transformation\";\ntrans;\nprint \"m*transformation\";\ntrans*m;\nprint \"transformation*jordan form\";\njor*trans; \n\ngives\n\nMagma V2.15-14    Tue Nov 24 2009 10:41:01    [Seed = 3482294566]\n   -------------------------------------\n\njordan form:\n[1 0 0 0 0 0 0]\n[0 1 1 0 0 0 0]\n[0 0 1 0 0 0 0]\n[0 0 0 1 1 0 0]\n[0 0 0 0 1 0 0]\n[0 0 0 0 0 1 1]\n[0 0 0 0 0 0 1]\ntransformation\n[0 0 0 0 1 1 0]\n[0 0 0 0 0 0 1]\n[1 1 1 1 1 1 1]\n[0 0 0 0 0 1 0]\n[1 1 1 0 1 1 0]\n[1 0 1 0 0 0 0]\n[1 1 0 1 1 1 0]\nm*transformation\n[0 0 0 0 1 1 0]\n[1 1 1 1 1 1 0]\n[1 1 1 1 1 1 1]\n[1 1 1 0 1 0 0]\n[1 1 1 0 1 1 0]\n[0 1 1 1 1 1 0]\n[1 1 0 1 1 1 0]\ntransformation*jordan form\n[0 0 0 0 1 1 0]\n[1 1 1 1 1 1 0]\n[1 1 1 1 1 1 1]\n[1 1 1 0 1 0 0]\n[1 1 1 0 1 1 0]\n[0 1 1 1 1 1 0]\n[1 1 0 1 1 1 0]\n\nTotal time: 0.170 seconds, Total memory usage: 7.27MB\n\n```\n",
    "created_at": "2009-11-23T23:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57394",
    "user": "@jasongrout"
}
```

Or more verbosely:


```
m:=Matrix(GF(2),7,7,StringToIntegerSequence("1 0 1 0 0 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 0 1 0 1 1 1 0 1 0 0 1 1 1 1 1 1 0"));
jor,trans:=JordanForm(m);

print "jordan form:";
jor;
print "transformation";
trans;
print "m*transformation";
trans*m;
print "transformation*jordan form";
jor*trans; 

gives

Magma V2.15-14    Tue Nov 24 2009 10:41:01    [Seed = 3482294566]
   -------------------------------------

jordan form:
[1 0 0 0 0 0 0]
[0 1 1 0 0 0 0]
[0 0 1 0 0 0 0]
[0 0 0 1 1 0 0]
[0 0 0 0 1 0 0]
[0 0 0 0 0 1 1]
[0 0 0 0 0 0 1]
transformation
[0 0 0 0 1 1 0]
[0 0 0 0 0 0 1]
[1 1 1 1 1 1 1]
[0 0 0 0 0 1 0]
[1 1 1 0 1 1 0]
[1 0 1 0 0 0 0]
[1 1 0 1 1 1 0]
m*transformation
[0 0 0 0 1 1 0]
[1 1 1 1 1 1 0]
[1 1 1 1 1 1 1]
[1 1 1 0 1 0 0]
[1 1 1 0 1 1 0]
[0 1 1 1 1 1 0]
[1 1 0 1 1 1 0]
transformation*jordan form
[0 0 0 0 1 1 0]
[1 1 1 1 1 1 0]
[1 1 1 1 1 1 1]
[1 1 1 0 1 0 0]
[1 1 1 0 1 1 0]
[0 1 1 1 1 1 0]
[1 1 0 1 1 1 0]

Total time: 0.170 seconds, Total memory usage: 7.27MB

```




---

archive/issue_comments_057395.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T12:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57395",
    "user": "spancratz"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057396.json:
```json
{
    "body": "Attachment [trac6942_jordan.patch](tarball://root/attachments/some-uuid/ticket6942/trac6942_jordan.patch) by spancratz created at 2010-01-19 12:28:03\n\nThe above patch fixes this problem, and also resolves ticket #6932.",
    "created_at": "2010-01-19T12:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57396",
    "user": "spancratz"
}
```

Attachment [trac6942_jordan.patch](tarball://root/attachments/some-uuid/ticket6942/trac6942_jordan.patch) by spancratz created at 2010-01-19 12:28:03

The above patch fixes this problem, and also resolves ticket #6932.



---

archive/issue_comments_057397.json:
```json
{
    "body": "Additional doctests",
    "created_at": "2010-01-20T02:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57397",
    "user": "spancratz"
}
```

Additional doctests



---

archive/issue_comments_057398.json:
```json
{
    "body": "Attachment [trac6942_jordan_tests.patch](tarball://root/attachments/some-uuid/ticket6942/trac6942_jordan_tests.patch) by spancratz created at 2010-01-20 02:19:12\n\nThe second patch adds additional doctests.  There are three of them, all for 10 by 10 matrices over the rationals and with only one eigenvalue.  The Jordan blocks are of sizes (a) 3,3,3,1, (b) 3,3,2,2, and (c) 3,2,2,2,1.\n\nSebastian",
    "created_at": "2010-01-20T02:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57398",
    "user": "spancratz"
}
```

Attachment [trac6942_jordan_tests.patch](tarball://root/attachments/some-uuid/ticket6942/trac6942_jordan_tests.patch) by spancratz created at 2010-01-20 02:19:12

The second patch adds additional doctests.  There are three of them, all for 10 by 10 matrices over the rationals and with only one eigenvalue.  The Jordan blocks are of sizes (a) 3,3,3,1, (b) 3,3,2,2, and (c) 3,2,2,2,1.

Sebastian



---

archive/issue_comments_057399.json:
```json
{
    "body": "This is looking pretty good.  But I'll have to spend some more time with it.  Until then, here's another 10x10 matrix with a nice Jordan form and nearly no fractions in the transformation matrix.\n\n\n```\nmatrix(QQ, [\n[-6,  9,  -7,  -5,  5,  12,  -22,  14,  8,  21 ],\n[ -3,  5,  -3,  -1,  2,  7,  -12,  9,  1,  12 ],\n[8,  -9,  8,  6,  0,  -14,  25,  -13,  -4,  -26 ],\n[-7,  9,  -7,  -5,  0,  13,  -23,  13,  2,  24 ],\n[0,  -1,  0,  -1,  -3,  -2,  3,  -4,  -2,  -3 ],\n[3,  2,  1,  2,  9,  -1,  1,  5,  5,  -5 ],\n[-1,  3,  -3,  -2,  4,  3,  -6,  4,  4,  3 ],\n[3,  -4,  3,  2,  1,  -5,  9,  -5,  1,  -9 ],\n[0,  2,  0,  0,  2,  2,  -4,  4,  2,  4 ],\n[-4,  4,  -5,  -4,  -1,  6,  -11,  4,  1, 10]\n])\n```\n",
    "created_at": "2010-01-24T08:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57399",
    "user": "@rbeezer"
}
```

This is looking pretty good.  But I'll have to spend some more time with it.  Until then, here's another 10x10 matrix with a nice Jordan form and nearly no fractions in the transformation matrix.


```
matrix(QQ, [
[-6,  9,  -7,  -5,  5,  12,  -22,  14,  8,  21 ],
[ -3,  5,  -3,  -1,  2,  7,  -12,  9,  1,  12 ],
[8,  -9,  8,  6,  0,  -14,  25,  -13,  -4,  -26 ],
[-7,  9,  -7,  -5,  0,  13,  -23,  13,  2,  24 ],
[0,  -1,  0,  -1,  -3,  -2,  3,  -4,  -2,  -3 ],
[3,  2,  1,  2,  9,  -1,  1,  5,  5,  -5 ],
[-1,  3,  -3,  -2,  4,  3,  -6,  4,  4,  3 ],
[3,  -4,  3,  2,  1,  -5,  9,  -5,  1,  -9 ],
[0,  2,  0,  0,  2,  2,  -4,  4,  2,  4 ],
[-4,  4,  -5,  -4,  -1,  6,  -11,  4,  1, 10]
])
```




---

archive/issue_comments_057400.json:
```json
{
    "body": "Attachment [trac_6942-reviewer.patch](tarball://root/attachments/some-uuid/ticket6942/trac_6942-reviewer.patch) by @rbeezer created at 2010-01-31 07:04:22\n\nOne-character reviewer doctest fix",
    "created_at": "2010-01-31T07:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57400",
    "user": "@rbeezer"
}
```

Attachment [trac_6942-reviewer.patch](tarball://root/attachments/some-uuid/ticket6942/trac_6942-reviewer.patch) by @rbeezer created at 2010-01-31 07:04:22

One-character reviewer doctest fix



---

archive/issue_comments_057401.json:
```json
{
    "body": "Hi Sebastian,\n\nVery nice!\n\n1.  One line in a list indented one-too-many characters.  Fix in reviewer patch for your convenience.  Accept or not.\n\n2.  Most of the linear algebra matrix decompositions return all the pieces, all the time.  I've always thought it inconsistent Jordan form has this `transformation` switch, sometimes returning one matrix, other times two.  Now would be a good time to change this behavior.  But I see that the form is almost a combinatorial routine (once you have the spectrum), while the basis vectors require a whole lot more work, so maybe best not to compute it unless it is asked for?\n\n3.  The list `Vsmall+Y` ends up in a `span()` in the \"vector_in_difference\" routine.  The span has an `already_echelonized` switch, so I spent a lot of time trying to decide how (or if it was possible) to somehow \"keep\" `Vsmall+Y` echelonized, since `Vsmall` will start that way.  Couldn't see a reasonable way to do anything too clever, though.\n\n4.  Do you want the 10x10 matrix above for the doctests?  I'd be happy to package it up with the one-character patch.  ;-)\n\nOther than the doctest fix, this is ready to go.  If you want to accept the doctest fix, then go ahead and mark this as \"positive review\" - everything else is just for your consideration.\n\nGreat to see all your good work since the summer, including this.\n\nRob",
    "created_at": "2010-01-31T07:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57401",
    "user": "@rbeezer"
}
```

Hi Sebastian,

Very nice!

1.  One line in a list indented one-too-many characters.  Fix in reviewer patch for your convenience.  Accept or not.

2.  Most of the linear algebra matrix decompositions return all the pieces, all the time.  I've always thought it inconsistent Jordan form has this `transformation` switch, sometimes returning one matrix, other times two.  Now would be a good time to change this behavior.  But I see that the form is almost a combinatorial routine (once you have the spectrum), while the basis vectors require a whole lot more work, so maybe best not to compute it unless it is asked for?

3.  The list `Vsmall+Y` ends up in a `span()` in the "vector_in_difference" routine.  The span has an `already_echelonized` switch, so I spent a lot of time trying to decide how (or if it was possible) to somehow "keep" `Vsmall+Y` echelonized, since `Vsmall` will start that way.  Couldn't see a reasonable way to do anything too clever, though.

4.  Do you want the 10x10 matrix above for the doctests?  I'd be happy to package it up with the one-character patch.  ;-)

Other than the doctest fix, this is ready to go.  If you want to accept the doctest fix, then go ahead and mark this as "positive review" - everything else is just for your consideration.

Great to see all your good work since the summer, including this.

Rob



---

archive/issue_comments_057402.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-01-31T07:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57402",
    "user": "@rbeezer"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_057403.json:
```json
{
    "body": "I've marked this as \"needs review\"  in hopes it will get merged soon.  The questions above could be addressed on a new ticket.",
    "created_at": "2010-02-03T19:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57403",
    "user": "@rbeezer"
}
```

I've marked this as "needs review"  in hopes it will get merged soon.  The questions above could be addressed on a new ticket.



---

archive/issue_comments_057404.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-03T19:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57404",
    "user": "@rbeezer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_057405.json:
```json
{
    "body": "The reviewer patch [trac_6942-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6942/trac_6942-reviewer.patch) looks good to me.",
    "created_at": "2010-02-03T22:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57405",
    "user": "mvngu"
}
```

The reviewer patch [trac_6942-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6942/trac_6942-reviewer.patch) looks good to me.



---

archive/issue_comments_057406.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-03T22:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57406",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057407.json:
```json
{
    "body": "Dear Rob,\n\nI am sorry that I am only looking at this again now.  Of course, the reviewer patch looks fine.  Thanks again for reviewing this!  About your other points...\n\n3) Yes, that is a good observation.  I am almost sure that if one looked closer at the linear algebra operations then this code could easily be improved.  There are currently two reasons why I won't look at this, though.  (a) The previous code was broken, so I think it's important to first have something that \"obviously\" works, in the sense that it is moderately easy to review since the code only uses \"high-level\" operations.  (b) I've got my first year interview this coming Monday.\n\n4) This is completely up to you.  The matrix looks quite intriguing and more examples certainly couldn't hurt.  Since this ticket will probably be closed soon, if you decide to include this new example, feel free to let me know (via email or sage-devel) and I'll review it right away.\n\nAlso, Minh, thank you for picking up the slack and completing the review process!\n\nKind regards,\n\nSebastian",
    "created_at": "2010-02-06T02:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57407",
    "user": "spancratz"
}
```

Dear Rob,

I am sorry that I am only looking at this again now.  Of course, the reviewer patch looks fine.  Thanks again for reviewing this!  About your other points...

3) Yes, that is a good observation.  I am almost sure that if one looked closer at the linear algebra operations then this code could easily be improved.  There are currently two reasons why I won't look at this, though.  (a) The previous code was broken, so I think it's important to first have something that "obviously" works, in the sense that it is moderately easy to review since the code only uses "high-level" operations.  (b) I've got my first year interview this coming Monday.

4) This is completely up to you.  The matrix looks quite intriguing and more examples certainly couldn't hurt.  Since this ticket will probably be closed soon, if you decide to include this new example, feel free to let me know (via email or sage-devel) and I'll review it right away.

Also, Minh, thank you for picking up the slack and completing the review process!

Kind regards,

Sebastian



---

archive/issue_comments_057408.json:
```json
{
    "body": "Replying to [comment:11 spancratz]:\n\n> \n> Also, Minh, thank you for picking up the slack and completing the review process!\n\n\nMinh and Rob---thank you both of you for reviewing this!",
    "created_at": "2010-02-06T03:10:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57408",
    "user": "@jasongrout"
}
```

Replying to [comment:11 spancratz]:

> 
> Also, Minh, thank you for picking up the slack and completing the review process!


Minh and Rob---thank you both of you for reviewing this!



---

archive/issue_comments_057409.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6942#issuecomment-57409",
    "user": "@qed777"
}
```

Resolution: fixed
