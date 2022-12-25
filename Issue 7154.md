# Issue 7154: options for point/arrow thickness are inconsistently named

archive/issues_007154.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout @kcrisman\n\nKeywords: point arrow thickness\n\nThere should be a consistent naming scheme for the \"thickness\" of graphics objects. If I have a function my_plot(**kwds) that passes **kwds to all constructed graphics objects, then my_plot(thickness=5) should consistently scale the thickness. \n\nThe current status is:\n\n\n```\n  sage: point([0,0], pointsize = 5)\n  sage: point3d((0,0,0), thickness=5)                      \n  sage: line2d([[0,0],[1,1]], thickness=5)\n  sage: line3d([[0,0,0],[1,1,0]], thickness=5)\n  sage: arrow([0,0],[1,1], width=5)    \n  sage: arrow3d([0,0,0],[1,1,1], thickness=5)\n  sage: polygon([(0,0), (1,1), (0,1)], thickness=5)      \n  sage: polygon3d([(0,0,0), (1,1,0), (0,1,0)], thickness=5)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7154\n\n",
    "created_at": "2009-10-08T11:07:33Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "options for point/arrow thickness are inconsistently named",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7154",
    "user": "https://github.com/vbraun"
}
```
Assignee: @williamstein

CC:  @jasongrout @kcrisman

Keywords: point arrow thickness

There should be a consistent naming scheme for the "thickness" of graphics objects. If I have a function my_plot(**kwds) that passes **kwds to all constructed graphics objects, then my_plot(thickness=5) should consistently scale the thickness. 

The current status is:


```
  sage: point([0,0], pointsize = 5)
  sage: point3d((0,0,0), thickness=5)                      
  sage: line2d([[0,0],[1,1]], thickness=5)
  sage: line3d([[0,0,0],[1,1,0]], thickness=5)
  sage: arrow([0,0],[1,1], width=5)    
  sage: arrow3d([0,0,0],[1,1,1], thickness=5)
  sage: polygon([(0,0), (1,1), (0,1)], thickness=5)      
  sage: polygon3d([(0,0,0), (1,1,0), (0,1,0)], thickness=5)
```



Issue created by migration from https://trac.sagemath.org/ticket/7154





---

archive/issue_comments_059153.json:
```json
{
    "body": "Also, the arrow3d thickness behaves differently than the thickness of point3d and line3d: If you zoom in, the arrow becomes bigger and bigger like a physical object. The line3d and point3d stay the same apparent size, about thickness pixels wide on screen. Since the arrow3d is usually used to indicate a direction it would be nice if it would scale (or, rather, not scale) just like point3d and line3d.\n\n\n```\n  sage: scene = \\\n  ....: line3d([[1,0,0],[1,3,0]],thickness=5) + \\\n  ....: arrow3d([2,0,0],[2,3,0],thickness=5) + \\\n  ....: point3d([3,2,0],thickness=5)\n  sage: scene.show( aspect_ratio=[1,1,1])\n```\n\n\nand then zoom in/out in the Jmol viewer.",
    "created_at": "2009-10-09T09:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59153",
    "user": "https://github.com/vbraun"
}
```

Also, the arrow3d thickness behaves differently than the thickness of point3d and line3d: If you zoom in, the arrow becomes bigger and bigger like a physical object. The line3d and point3d stay the same apparent size, about thickness pixels wide on screen. Since the arrow3d is usually used to indicate a direction it would be nice if it would scale (or, rather, not scale) just like point3d and line3d.


```
  sage: scene = \
  ....: line3d([[1,0,0],[1,3,0]],thickness=5) + \
  ....: arrow3d([2,0,0],[2,3,0],thickness=5) + \
  ....: point3d([3,2,0],thickness=5)
  sage: scene.show( aspect_ratio=[1,1,1])
```


and then zoom in/out in the Jmol viewer.



---

archive/issue_comments_059154.json:
```json
{
    "body": "I agree with the first comment; the arguments should distinguish between \"width\", which is in data coordinates and changes as you zoom, and \"thickness\", which is in screen coordinates, and does not change as you zoom.  Figure out which is which for the cases above, and probably use the `@`rename_keyword decorator from the plotting code to change instances with deprecation.",
    "created_at": "2010-05-26T15:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59154",
    "user": "https://github.com/jasongrout"
}
```

I agree with the first comment; the arguments should distinguish between "width", which is in data coordinates and changes as you zoom, and "thickness", which is in screen coordinates, and does not change as you zoom.  Figure out which is which for the cases above, and probably use the `@`rename_keyword decorator from the plotting code to change instances with deprecation.



---

archive/issue_comments_059155.json:
```json
{
    "body": "Changing keywords from \"point arrow thickness\" to \"point arrow thickness, beginner\".",
    "created_at": "2010-05-26T15:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59155",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "point arrow thickness" to "point arrow thickness, beginner".



---

archive/issue_comments_059156.json:
```json
{
    "body": "Rename arrow 'width' option to 'thickness'",
    "created_at": "2010-08-21T14:13:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59156",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Rename arrow 'width' option to 'thickness'



---

archive/issue_comments_059157.json:
```json
{
    "body": "Attachment [trac_7154_arrow_thickness.patch](tarball://root/attachments/some-uuid/ticket7154/trac_7154_arrow_thickness.patch) by ryan created at 2010-08-21 14:20:29\n\nlooking at the arrow3d thickness now.",
    "created_at": "2010-08-21T14:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59157",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_7154_arrow_thickness.patch](tarball://root/attachments/some-uuid/ticket7154/trac_7154_arrow_thickness.patch) by ryan created at 2010-08-21 14:20:29

looking at the arrow3d thickness now.



---

archive/issue_comments_059158.json:
```json
{
    "body": "Attachment [trac_7154_arrow3d_width.patch](tarball://root/attachments/some-uuid/ticket7154/trac_7154_arrow3d_width.patch) by ryan created at 2010-08-21 22:33:40",
    "created_at": "2010-08-21T22:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59158",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_7154_arrow3d_width.patch](tarball://root/attachments/some-uuid/ticket7154/trac_7154_arrow3d_width.patch) by ryan created at 2010-08-21 22:33:40



---

archive/issue_comments_059159.json:
```json
{
    "body": "In response to jason's comment, I submit a patch that renames the thickness keyword of arrow3d to width.  The reason is that the width of the arrow3d are not screen coordinates.  Why? Because arrow3d is constructed of a cylinder and the thickness controls the radius of this cylinder.\n\nIf someone is looking for an alternative to arrow3d that does not scale when zoomed, you can use line3d with arrow_head=True.",
    "created_at": "2010-08-21T22:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59159",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

In response to jason's comment, I submit a patch that renames the thickness keyword of arrow3d to width.  The reason is that the width of the arrow3d are not screen coordinates.  Why? Because arrow3d is constructed of a cylinder and the thickness controls the radius of this cylinder.

If someone is looking for an alternative to arrow3d that does not scale when zoomed, you can use line3d with arrow_head=True.



---

archive/issue_comments_059160.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-21T22:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59160",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059161.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-21T23:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59161",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059162.json:
```json
{
    "body": "Thanks!  Fixing things like this really add to the polish and ease-of-use of Sage, and make it much more user-friendly.\n\nThree comments:\n\n1. I think the rename_keyword works the other way.  See this example from the docs:\n\n\n```\nrename_keyword(deprecated='Sage version 4.2', deprecated_option='new_option')\n```\n\n\nDon't you want it to be thickness='width'?  Also, the actual keyword in the function should be changed in the function declaration (you can probably then search and replace in the function definition to replace 'thickness' with 'width'.\n\n2. Could you add a deprecation by using the deprecation feature of rename_keyword?\n\n3. Could you add a short doctest showing the deprecation warning and the new option?  The deprecation warning should probably be in a TESTS: section, while the new option should definitely be in the EXAMPLES section.\n\nThanks for working on this!",
    "created_at": "2010-08-21T23:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59162",
    "user": "https://github.com/jasongrout"
}
```

Thanks!  Fixing things like this really add to the polish and ease-of-use of Sage, and make it much more user-friendly.

Three comments:

1. I think the rename_keyword works the other way.  See this example from the docs:


```
rename_keyword(deprecated='Sage version 4.2', deprecated_option='new_option')
```


Don't you want it to be thickness='width'?  Also, the actual keyword in the function should be changed in the function declaration (you can probably then search and replace in the function definition to replace 'thickness' with 'width'.

2. Could you add a deprecation by using the deprecation feature of rename_keyword?

3. Could you add a short doctest showing the deprecation warning and the new option?  The deprecation warning should probably be in a TESTS: section, while the new option should definitely be in the EXAMPLES section.

Thanks for working on this!



---

archive/issue_comments_059163.json:
```json
{
    "body": "oops. The rename_keyword in the *arrow3d_width.patch is backwards.  I'll update it as soon as I can (with the other changes as well).\n\nAlso, is there really a need for arrow3d to scale when zoomed?  I can't think of any instance where that would be genuinely useful.  Maybe arrow3d should be changed to match the behavior of line3d if that is what people are expecting.",
    "created_at": "2010-08-22T02:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59163",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

oops. The rename_keyword in the *arrow3d_width.patch is backwards.  I'll update it as soon as I can (with the other changes as well).

Also, is there really a need for arrow3d to scale when zoomed?  I can't think of any instance where that would be genuinely useful.  Maybe arrow3d should be changed to match the behavior of line3d if that is what people are expecting.



---

archive/issue_comments_059164.json:
```json
{
    "body": "updated - added doctests and deprecation warning",
    "created_at": "2010-08-28T18:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59164",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

updated - added doctests and deprecation warning



---

archive/issue_comments_059165.json:
```json
{
    "body": "Attachment [trac_7154_arrow_thickness.2.patch](tarball://root/attachments/some-uuid/ticket7154/trac_7154_arrow_thickness.2.patch) by ryan created at 2010-08-28 18:18:18\n\nthe real update :)  added doctest and deprecation warning",
    "created_at": "2010-08-28T18:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59165",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_7154_arrow_thickness.2.patch](tarball://root/attachments/some-uuid/ticket7154/trac_7154_arrow_thickness.2.patch) by ryan created at 2010-08-28 18:18:18

the real update :)  added doctest and deprecation warning



---

archive/issue_comments_059166.json:
```json
{
    "body": "sorry accidentally uploaded the wrong patch.",
    "created_at": "2010-08-28T18:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59166",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

sorry accidentally uploaded the wrong patch.



---

archive/issue_comments_059167.json:
```json
{
    "body": "Wow, that is a huge patch.  It looks like a lot of whitespace changes.  Is that right?",
    "created_at": "2010-08-29T02:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59167",
    "user": "https://github.com/jasongrout"
}
```

Wow, that is a huge patch.  It looks like a lot of whitespace changes.  Is that right?



---

archive/issue_comments_059168.json:
```json
{
    "body": "Replying to [comment:10 jason]:\n> Wow, that is a huge patch.  It looks like a lot of whitespace changes.  Is that right?\n\nI was also puzzled at why it was so big.  Most likely it has something to do with my python editor removing trailing spaces on save.",
    "created_at": "2010-08-29T04:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59168",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Replying to [comment:10 jason]:
> Wow, that is a huge patch.  It looks like a lot of whitespace changes.  Is that right?

I was also puzzled at why it was so big.  Most likely it has something to do with my python editor removing trailing spaces on save.



---

archive/issue_comments_059169.json:
```json
{
    "body": "Updated patch (with Sage 4.5.3)",
    "created_at": "2010-09-11T05:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59169",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Updated patch (with Sage 4.5.3)



---

archive/issue_comments_059170.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-11T05:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59170",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059171.json:
```json
{
    "body": "Attachment [trac_7154_arrow3d_width.3.patch](tarball://root/attachments/some-uuid/ticket7154/trac_7154_arrow3d_width.3.patch) by ryan created at 2010-09-11 05:24:36",
    "created_at": "2010-09-11T05:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59171",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_7154_arrow3d_width.3.patch](tarball://root/attachments/some-uuid/ticket7154/trac_7154_arrow3d_width.3.patch) by ryan created at 2010-09-11 05:24:36



---

archive/issue_comments_059172.json:
```json
{
    "body": "apply instead of previous patch",
    "created_at": "2010-09-11T16:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59172",
    "user": "https://github.com/jasongrout"
}
```

apply instead of previous patch



---

archive/issue_comments_059173.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-11T16:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59173",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059174.json:
```json
{
    "body": "Attachment [trac_7154_arrow3d_width.4.patch](tarball://root/attachments/some-uuid/ticket7154/trac_7154_arrow3d_width.4.patch) by @jasongrout created at 2010-09-11 16:56:33\n\nLooks good.  I updated the version number in trac_7154_arrow3d_width.4.patch; apply only that patch.  \n\nThanks!\n\nThis is Ryan's first contribution, along with #8838 and #9199.",
    "created_at": "2010-09-11T16:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59174",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_7154_arrow3d_width.4.patch](tarball://root/attachments/some-uuid/ticket7154/trac_7154_arrow3d_width.4.patch) by @jasongrout created at 2010-09-11 16:56:33

Looks good.  I updated the version number in trac_7154_arrow3d_width.4.patch; apply only that patch.  

Thanks!

This is Ryan's first contribution, along with #8838 and #9199.



---

archive/issue_events_007374.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-15T10:40:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7154#event-7374"
}
```



---

archive/issue_comments_059175.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7154#issuecomment-59175",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
