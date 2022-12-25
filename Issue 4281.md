# Issue 4281: [with patch,with positive review] elliptic curve doctest coverage (part 4)

archive/issues_004281.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is for the file ell_tate_curve.py. I was unable to doctest the _height function, which is used\nas a closure. Also, the missing loads(dumps(..)) test fails:\n\n```\nsage: e = EllipticCurve('130a1')\nsage: eq = e.tate_curve(5)\nsage: eq == loads(dumps(eq))\nFalse\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4281\n\n",
    "closed_at": "2008-10-20T14:01:54Z",
    "created_at": "2008-10-14T13:47:05Z",
    "labels": [
        "component: algebraic geometry",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch,with positive review] elliptic curve doctest coverage (part 4)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4281",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @williamstein

This is for the file ell_tate_curve.py. I was unable to doctest the _height function, which is used
as a closure. Also, the missing loads(dumps(..)) test fails:

```
sage: e = EllipticCurve('130a1')
sage: eq = e.tate_curve(5)
sage: eq == loads(dumps(eq))
False
```

Issue created by migration from https://trac.sagemath.org/ticket/4281





---

archive/issue_comments_031252.json:
```json
{
    "body": "Attachment [trac_4281.patch](tarball://root/attachments/some-uuid/ticket4281/trac_4281.patch) by @zimmermann6 created at 2008-10-14 13:49:50",
    "created_at": "2008-10-14T13:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31252",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_4281.patch](tarball://root/attachments/some-uuid/ticket4281/trac_4281.patch) by @zimmermann6 created at 2008-10-14 13:49:50



---

archive/issue_comments_031253.json:
```json
{
    "body": "Attachment [trac_4281.patch2](tarball://root/attachments/some-uuid/ticket4281/trac_4281.patch2) by @zimmermann6 created at 2008-10-14 14:00:49",
    "created_at": "2008-10-14T14:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31253",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_4281.patch2](tarball://root/attachments/some-uuid/ticket4281/trac_4281.patch2) by @zimmermann6 created at 2008-10-14 14:00:49



---

archive/issue_comments_031254.json:
```json
{
    "body": "The second patch fixed a few typos (to be applied after the 1st one).",
    "created_at": "2008-10-14T14:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31254",
    "user": "https://github.com/zimmermann6"
}
```

The second patch fixed a few typos (to be applied after the 1st one).



---

archive/issue_comments_031255.json:
```json
{
    "body": "The attached patch fixes the loads/dumps issue.",
    "created_at": "2008-10-14T21:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31255",
    "user": "https://github.com/robertwb"
}
```

The attached patch fixes the loads/dumps issue.



---

archive/issue_comments_031256.json:
```json
{
    "body": "The last patch does not for fix it for me. Do I do something wrong ?\n(This is the same patch as for #4289.)",
    "created_at": "2008-10-15T10:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31256",
    "user": "https://github.com/categorie"
}
```

The last patch does not for fix it for me. Do I do something wrong ?
(This is the same patch as for #4289.)



---

archive/issue_comments_031257.json:
```json
{
    "body": "I agree with Chris. Probably Robert attached the wrong patch. This one (4281-tate-pickle.patch)\nis already in 3.1.4 but the loads/dumps problem is still there:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.4, Release Date: 2008-10-16                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: e = EllipticCurve('130a1')\nsage: eq = e.tate_curve(5)\nsage: eq == loads(dumps(eq))\nFalse\n```",
    "created_at": "2008-10-18T11:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31257",
    "user": "https://github.com/zimmermann6"
}
```

I agree with Chris. Probably Robert attached the wrong patch. This one (4281-tate-pickle.patch)
is already in 3.1.4 but the loads/dumps problem is still there:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: e = EllipticCurve('130a1')
sage: eq = e.tate_curve(5)
sage: eq == loads(dumps(eq))
False
```



---

archive/issue_comments_031258.json:
```json
{
    "body": "Attachment [4281-tate-pickle.patch](tarball://root/attachments/some-uuid/ticket4281/4281-tate-pickle.patch) by @robertwb created at 2008-10-18 17:02:45\n\nYep, sorry, I posted the wrong patch. I've replaced it now.",
    "created_at": "2008-10-18T17:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31258",
    "user": "https://github.com/robertwb"
}
```

Attachment [4281-tate-pickle.patch](tarball://root/attachments/some-uuid/ticket4281/4281-tate-pickle.patch) by @robertwb created at 2008-10-18 17:02:45

Yep, sorry, I posted the wrong patch. I've replaced it now.



---

archive/issue_comments_031259.json:
```json
{
    "body": "Robert's new patch is ok, thus I give a positive review for it.\nHowever I cannot review my own patches...",
    "created_at": "2008-10-18T17:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31259",
    "user": "https://github.com/zimmermann6"
}
```

Robert's new patch is ok, thus I give a positive review for it.
However I cannot review my own patches...



---

archive/issue_comments_031260.json:
```json
{
    "body": "N.B. To apply the second patch properly I had to rename it to trac_4281_2.patch:  applying the patch failed when the suffix was patch2.\n\nApart from that, the sequence of patches applies fine and all tests in elliptic_curves pass.\n\nI also learnt from robertwb's patch one way in which loads(dumps(*)) can fail, so will return to the other ticket...",
    "created_at": "2008-10-19T20:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31260",
    "user": "https://github.com/JohnCremona"
}
```

N.B. To apply the second patch properly I had to rename it to trac_4281_2.patch:  applying the patch failed when the suffix was patch2.

Apart from that, the sequence of patches applies fine and all tests in elliptic_curves pass.

I also learnt from robertwb's patch one way in which loads(dumps(*)) can fail, so will return to the other ticket...



---

archive/issue_comments_031261.json:
```json
{
    "body": "Strictly speaking there is still something to do. It checks if E and p are equal. In a perfect implementation this should be an elliptic curve over a local field and we should check if they are isomorphic over this field, not over Q.\n\nBut I agree that the patch fixes this by now and the ticket should be closed.",
    "created_at": "2008-10-20T09:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31261",
    "user": "https://github.com/categorie"
}
```

Strictly speaking there is still something to do. It checks if E and p are equal. In a perfect implementation this should be an elliptic curve over a local field and we should check if they are isomorphic over this field, not over Q.

But I agree that the patch fixes this by now and the ticket should be closed.



---

archive/issue_comments_031262.json:
```json
{
    "body": "Replying to [comment:8 wuthrich]:\n> Strictly speaking there is still something to do. It checks if E and p are equal. In a perfect implementation this should be an elliptic curve over a local field and we should check if they are isomorphic over this field, not over Q.\n> \n\n\nWhen we have a type to hold elliptic curves over local fields then this can perhaps be changed.  I also did not bother to compare the (possibly) cached power series which are part of the class's data.  As I see it, this _cmp_ function is only there for technical Pythonic reasons, and serious mathematical functionality would not be implemented via the == operator.\n\n\n> But I agree that the patch fixes this by now and the ticket should be closed.\n\n\nGood!  Thanks.",
    "created_at": "2008-10-20T09:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31262",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:8 wuthrich]:
> Strictly speaking there is still something to do. It checks if E and p are equal. In a perfect implementation this should be an elliptic curve over a local field and we should check if they are isomorphic over this field, not over Q.
> 


When we have a type to hold elliptic curves over local fields then this can perhaps be changed.  I also did not bother to compare the (possibly) cached power series which are part of the class's data.  As I see it, this _cmp_ function is only there for technical Pythonic reasons, and serious mathematical functionality would not be implemented via the == operator.


> But I agree that the patch fixes this by now and the ticket should be closed.


Good!  Thanks.



---

archive/issue_comments_031263.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-20T14:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31263",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031264.json:
```json
{
    "body": "Merged all three patches in Sage 3.2.alpha0",
    "created_at": "2008-10-20T14:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4281#issuecomment-31264",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.2.alpha0



---

archive/issue_events_009669.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-20T14:01:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4281",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4281#event-9669"
}
```
