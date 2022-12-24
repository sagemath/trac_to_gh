# Issue 8879: Bad indentation in hyperelliptic curve file

archive/issues_008879.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  mjo\n\nAs of 4.4, there is bad indentation in sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\n\n```\n    def is_in_weierstrass_disc(self,P):\n        \"\"\"\n        Checks if $P$ is in a Weierstrass disc\n\n        EXAMPLES:\n            sage: R.<x> = QQ['x']\n            sage: H = HyperellipticCurve(x^3-10*x+9)\n            sage: K = Qp(5,8)\n            sage: HK = H.change_ring(K)\n\t    sage: P = HK(0,3)\n\t    sage: HK.is_in_weierstrass_disc(P)\n\t    False\n\t    sage: Q = HK(0,1,0)\n\t    sage: HK.is_in_weierstrass_disc(Q)\n\t    True\n\t    sage: S = HK(1,0)\n            sage: HK.is_in_weierstrass_disc(S)\n            True\n\t    sage: T = HK.lift_x(1+3*5^2); T\n\t    (1 + 3*5^2 + O(5^8) : 2*5 + 4*5^3 + 3*5^4 + 5^5 + 3*5^6 + O(5^7) : 1 + O(5^8))\n\t    sage: HK.is_in_weierstrass_disc(T)\n\t    True\n\n\tAUTHOR:\n            - Jennifer Balakrishnan (2010-02)\n        \"\"\"\n```\n\nI don't know if it matters that much, but at the very least it's annoying.  It's not elliptic curves, of course, but that's the closest component I could find.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8879\n\n",
    "created_at": "2010-05-05T00:01:01Z",
    "labels": [
        "elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Bad indentation in hyperelliptic curve file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8879",
    "user": "kcrisman"
}
```
Assignee: cremona

CC:  mjo

As of 4.4, there is bad indentation in sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py

```
    def is_in_weierstrass_disc(self,P):
        """
        Checks if $P$ is in a Weierstrass disc

        EXAMPLES:
            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,8)
            sage: HK = H.change_ring(K)
	    sage: P = HK(0,3)
	    sage: HK.is_in_weierstrass_disc(P)
	    False
	    sage: Q = HK(0,1,0)
	    sage: HK.is_in_weierstrass_disc(Q)
	    True
	    sage: S = HK(1,0)
            sage: HK.is_in_weierstrass_disc(S)
            True
	    sage: T = HK.lift_x(1+3*5^2); T
	    (1 + 3*5^2 + O(5^8) : 2*5 + 4*5^3 + 3*5^4 + 5^5 + 3*5^6 + O(5^7) : 1 + O(5^8))
	    sage: HK.is_in_weierstrass_disc(T)
	    True

	AUTHOR:
            - Jennifer Balakrishnan (2010-02)
        """
```

I don't know if it matters that much, but at the very least it's annoying.  It's not elliptic curves, of course, but that's the closest component I could find.

Issue created by migration from https://trac.sagemath.org/ticket/8879





---

archive/issue_comments_081586.json:
```json
{
    "body": "There is also a tab in the following doctest which causes Mac OS X 10.4 to have problems while doctesting, I think.\n\n```\n    def residue_disc(self,P):\n        \"\"\"\n        Gives the residue disc of $P$\n        \n        EXAMPLES:\n\t    sage: R.<x> = QQ['x']\t\n```\n\nNote that tab character (not visible, but there!) in the last line.",
    "created_at": "2010-05-05T00:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8879#issuecomment-81586",
    "user": "kcrisman"
}
```

There is also a tab in the following doctest which causes Mac OS X 10.4 to have problems while doctesting, I think.

```
    def residue_disc(self,P):
        """
        Gives the residue disc of $P$
        
        EXAMPLES:
	    sage: R.<x> = QQ['x']	
```

Note that tab character (not visible, but there!) in the last line.



---

archive/issue_comments_081587.json:
```json
{
    "body": "Also, the tests at lines 465 ff. take 12-15 seconds EACH on a pretty new computer.  Shouldn't these be marked # long time?  In general quite a few of the doctests take very long, and there are so many that it seems reasonable that some don't have to be run in a normal make check.\n\nThere is a further tab character in line 752:\n\n```\n            sage: T = HK(0,1,0)\t\n```\n\nand line 757\n\n```\n            sage: HK.coleman_integral(w*x^3,T,S)\t\n```\n",
    "created_at": "2010-05-05T00:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8879#issuecomment-81587",
    "user": "kcrisman"
}
```

Also, the tests at lines 465 ff. take 12-15 seconds EACH on a pretty new computer.  Shouldn't these be marked # long time?  In general quite a few of the doctests take very long, and there are so many that it seems reasonable that some don't have to be run in a normal make check.

There is a further tab character in line 752:

```
            sage: T = HK(0,1,0)	
```

and line 757

```
            sage: HK.coleman_integral(w*x^3,T,S)	
```




---

archive/issue_comments_081588.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-16T03:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8879#issuecomment-81588",
    "user": "mjo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081589.json:
```json
{
    "body": "* All tabs were fixed in #8680.\n  * The coleman_integral stuff was marked long time in #10712.\n  * The bad indentation was fixed somewhere along the line.\n\nI've cleaned up some trailing whitespace, so that there isn't nothing to do here.",
    "created_at": "2012-01-16T03:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8879#issuecomment-81589",
    "user": "mjo"
}
```

* All tabs were fixed in #8680.
  * The coleman_integral stuff was marked long time in #10712.
  * The bad indentation was fixed somewhere along the line.

I've cleaned up some trailing whitespace, so that there isn't nothing to do here.



---

archive/issue_comments_081590.json:
```json
{
    "body": "Attachment [sage-trac_8879.patch](tarball://root/attachments/some-uuid/ticket8879/sage-trac_8879.patch) by mjo created at 2012-01-16 03:46:19\n\nRemove trailing whitespace.",
    "created_at": "2012-01-16T03:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8879#issuecomment-81590",
    "user": "mjo"
}
```

Attachment [sage-trac_8879.patch](tarball://root/attachments/some-uuid/ticket8879/sage-trac_8879.patch) by mjo created at 2012-01-16 03:46:19

Remove trailing whitespace.



---

archive/issue_comments_081591.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-03T03:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8879#issuecomment-81591",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081592.json:
```json
{
    "body": "Replying to [comment:3 mjo]:\n>  * All tabs were fixed in #8680.\n>  * The coleman_integral stuff was marked long time in #10712.\n>  * The bad indentation was fixed somewhere along the line.\n> \n> I've cleaned up some trailing whitespace, so that there isn't nothing to do here.\nNot much to review either.  You could have just positively reviewed this as a duplicate too, you know!  But I suppose someone has to remove trailing whitespace!",
    "created_at": "2012-02-03T03:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8879#issuecomment-81592",
    "user": "kcrisman"
}
```

Replying to [comment:3 mjo]:
>  * All tabs were fixed in #8680.
>  * The coleman_integral stuff was marked long time in #10712.
>  * The bad indentation was fixed somewhere along the line.
> 
> I've cleaned up some trailing whitespace, so that there isn't nothing to do here.
Not much to review either.  You could have just positively reviewed this as a duplicate too, you know!  But I suppose someone has to remove trailing whitespace!



---

archive/issue_comments_081593.json:
```json
{
    "body": "I had already cleaned up the whitespace in the process of investigating the fixed issues, so it felt wrong throw out a perfectly good patch.",
    "created_at": "2012-02-03T03:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8879#issuecomment-81593",
    "user": "mjo"
}
```

I had already cleaned up the whitespace in the process of investigating the fixed issues, so it felt wrong throw out a perfectly good patch.



---

archive/issue_comments_081594.json:
```json
{
    "body": "Agreed.  Changing the summary, though :)",
    "created_at": "2012-02-03T15:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8879#issuecomment-81594",
    "user": "kcrisman"
}
```

Agreed.  Changing the summary, though :)



---

archive/issue_comments_081595.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-06T21:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8879#issuecomment-81595",
    "user": "jdemeyer"
}
```

Resolution: fixed
