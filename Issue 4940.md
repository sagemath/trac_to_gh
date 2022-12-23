# Issue 4940: dokchitser L-series at least for number fields claims a pole at zero, though the zeta function has a zero there

archive/issues_004940.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: K.<a> = NumberField(x^2-2)\nsage: z = K.zeta_function()\nsage: z(0)\nTraceback (most recent call last):\n...\nArithmeticError:   ###   user error: L*(s) has a pole at s=0\nsage: z(0.0000001)\n-4.40686861437826e-8\n```\n\n\nNotice that there is in fact a zero at s=0, not a pole as the ArithmeticError claims.\n\nIn fact, it's a theorem that there is a zero at s=0 of order the unit rank of the number field.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4940\n\n",
    "created_at": "2009-01-05T08:01:29Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "dokchitser L-series at least for number fields claims a pole at zero, though the zeta function has a zero there",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4940",
    "user": "was"
}
```
Assignee: was


```
sage: K.<a> = NumberField(x^2-2)
sage: z = K.zeta_function()
sage: z(0)
Traceback (most recent call last):
...
ArithmeticError:   ###   user error: L*(s) has a pole at s=0
sage: z(0.0000001)
-4.40686861437826e-8
```


Notice that there is in fact a zero at s=0, not a pole as the ArithmeticError claims.

In fact, it's a theorem that there is a zero at s=0 of order the unit rank of the number field.

Issue created by migration from https://trac.sagemath.org/ticket/4940





---

archive/issue_comments_037494.json:
```json
{
    "body": "The function ` L*(s) = sqrt(8)<sup>s/pi</sup>s * gamma(s/2)^2 ` does have a pole at s=0, even though L(s) doesn't. That being said, it shouldn't raise this error. \n\nI have made some progress on the re-implementation of dokchitser the last couple of days.",
    "created_at": "2009-01-23T04:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4940#issuecomment-37494",
    "user": "robertwb"
}
```

The function ` L*(s) = sqrt(8)<sup>s/pi</sup>s * gamma(s/2)^2 ` does have a pole at s=0, even though L(s) doesn't. That being said, it shouldn't raise this error. 

I have made some progress on the re-implementation of dokchitser the last couple of days.



---

archive/issue_comments_037495.json:
```json
{
    "body": "Changing keywords from \"\" to \"dokchitser\".",
    "created_at": "2013-09-21T11:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4940#issuecomment-37495",
    "user": "chapoton"
}
```

Changing keywords from "" to "dokchitser".
