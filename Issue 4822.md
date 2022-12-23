# Issue 4822: Tweak to the error message for EllipticCurve

archive/issues_004822.json:
```json
{
    "body": "Assignee: was\n\nI was using SAGE with the small version of the CremonaDatabase, and tried the following, which does not work because the conductor is too high:\n\n```\nEllipticCurve(\"10001a1\")\n```\n\n\nI think it would be useful if the error message not only said \"this curve is not in the database\" (which is indeed true) but also checked to see if one was using the small database of curves, and if so told the user how to access the larger version\nusing the incantation\n\n```\n!sage -i database_cremona_ellcurve-2005.11.03\n```\n\nor otherwise.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4822\n\n",
    "created_at": "2008-12-17T23:47:58Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "Tweak to the error message for EllipticCurve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4822",
    "user": "ljpk"
}
```
Assignee: was

I was using SAGE with the small version of the CremonaDatabase, and tried the following, which does not work because the conductor is too high:

```
EllipticCurve("10001a1")
```


I think it would be useful if the error message not only said "this curve is not in the database" (which is indeed true) but also checked to see if one was using the small database of curves, and if so told the user how to access the larger version
using the incantation

```
!sage -i database_cremona_ellcurve-2005.11.03
```

or otherwise.

Issue created by migration from https://trac.sagemath.org/ticket/4822





---

archive/issue_comments_036558.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4822#issuecomment-36558",
    "user": "rlm"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_036559.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4822#issuecomment-36559",
    "user": "davidloeffler"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_036560.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-20T19:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4822#issuecomment-36560",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_036561.json:
```json
{
    "body": "Attachment\n\nApplies to 4.1.1",
    "created_at": "2009-08-15T15:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4822#issuecomment-36561",
    "user": "cremona"
}
```

Attachment

Applies to 4.1.1



---

archive/issue_comments_036562.json:
```json
{
    "body": "Apply after previous",
    "created_at": "2009-08-15T15:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4822#issuecomment-36562",
    "user": "cremona"
}
```

Apply after previous



---

archive/issue_comments_036563.json:
```json
{
    "body": "Attachment\n\nThe patch deals with this in a more intelligent way.  I did not add doctests since it's hard to do that when the output message depends on whether or not the extra database is installed.  But I did test it before and after installing the optional database.  The message suggests installing the optional database iff the desired conductor is  betweem 10000 and 13000 and the optional db is not already installed;  I did not actually include the command-line to install it though.\n\nThe second patch fixes a doctest which otherwise fails when run after installing the optional database (but is otherwise independent of this ticket, except that I wrote it so was my fault anyway!)",
    "created_at": "2009-08-15T15:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4822#issuecomment-36563",
    "user": "cremona"
}
```

Attachment

The patch deals with this in a more intelligent way.  I did not add doctests since it's hard to do that when the output message depends on whether or not the extra database is installed.  But I did test it before and after installing the optional database.  The message suggests installing the optional database iff the desired conductor is  betweem 10000 and 13000 and the optional db is not already installed;  I did not actually include the command-line to install it though.

The second patch fixes a doctest which otherwise fails when run after installing the optional database (but is otherwise independent of this ticket, except that I wrote it so was my fault anyway!)



---

archive/issue_comments_036564.json:
```json
{
    "body": "The patch is ok (so far only tested without the optional package). I will test it with it later today.\n\nMaybe while we are at it I could suggest that the same change is done to `cremona_label()`.\nThis is without the optional package:\n\n\n```\nsage: E= EllipticCurve([3,10])\nsage: E.cremona_label()\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/home/chrigu/.sage/temp/linux_ljo8/12909/_home_chrigu__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in cremona_label(self, space)\n   3305                 X = self.database_curve()\n   3306             except RuntimeError:\n-> 3307                 raise RuntimeError, \"Cremona label not known for %s.\"%self\n   3308             self.__cremona_label = X.__cremona_label\n   3309             return self.cremona_label(space)\n\nRuntimeError: Cremona label not known for Elliptic Curve defined by y^2 = x^3 + 3*x + 10 over Rational Field.\nsage: E.conductor()\n44928\n```\n\n\nChris.\n\nps : 'I don't know if there is an official 'under review'.",
    "created_at": "2009-08-17T15:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4822#issuecomment-36564",
    "user": "wuthrich"
}
```

The patch is ok (so far only tested without the optional package). I will test it with it later today.

Maybe while we are at it I could suggest that the same change is done to `cremona_label()`.
This is without the optional package:


```
sage: E= EllipticCurve([3,10])
sage: E.cremona_label()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/chrigu/.sage/temp/linux_ljo8/12909/_home_chrigu__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in cremona_label(self, space)
   3305                 X = self.database_curve()
   3306             except RuntimeError:
-> 3307                 raise RuntimeError, "Cremona label not known for %s."%self
   3308             self.__cremona_label = X.__cremona_label
   3309             return self.cremona_label(space)

RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 = x^3 + 3*x + 10 over Rational Field.
sage: E.conductor()
44928
```


Chris.

ps : 'I don't know if there is an official 'under review'.



---

archive/issue_comments_036565.json:
```json
{
    "body": "This patch also works with the optional package. I give this ticket a positive review and I agree that the command-line to install the optional package should better not be included. It is very clear what to do as it is now.\n\n The second [independent] patch obtains also a positive review with this.\n\n I propose to address the issue that I raised on `cremona_label()` in a new ticket.\n\n Chris.",
    "created_at": "2009-08-17T16:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4822#issuecomment-36565",
    "user": "wuthrich"
}
```

This patch also works with the optional package. I give this ticket a positive review and I agree that the command-line to install the optional package should better not be included. It is very clear what to do as it is now.

 The second [independent] patch obtains also a positive review with this.

 I propose to address the issue that I raised on `cremona_label()` in a new ticket.

 Chris.



---

archive/issue_comments_036566.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-08-25T03:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4822#issuecomment-36566",
    "user": "mvngu"
}
```

Merged both patches.



---

archive/issue_comments_036567.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T03:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4822#issuecomment-36567",
    "user": "mvngu"
}
```

Resolution: fixed
