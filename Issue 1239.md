# Issue 1239: Wrap Simon's new gp two descent code

archive/issues_001239.json:
```json
{
    "body": "Assignee: was\n\nScripts were recently updated http://www.math.unicaen.fr/~simon/\n\nIt now handles two-torsion more uniformly, works on more curves, and actually returns points on the curve given. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1239\n\n",
    "created_at": "2007-11-21T19:43:50Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "Wrap Simon's new gp two descent code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1239",
    "user": "robertwb"
}
```
Assignee: was

Scripts were recently updated http://www.math.unicaen.fr/~simon/

It now handles two-torsion more uniformly, works on more curves, and actually returns points on the curve given. 

Issue created by migration from https://trac.sagemath.org/ticket/1239





---

archive/issue_comments_007742.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-21T19:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7742",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_007743.json:
```json
{
    "body": "Attachment\n\nJohn Cremona and I worked on this during Sage Days 6. \n\nThe attached patches have the new version of the code (to be applied to extcode) and a revised interface. \n\nThis also includes an implementation of transformations between different Weierstrass models.",
    "created_at": "2007-11-21T19:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7743",
    "user": "robertwb"
}
```

Attachment

John Cremona and I worked on this during Sage Days 6. 

The attached patches have the new version of the code (to be applied to extcode) and a revised interface. 

This also includes an implementation of transformations between different Weierstrass models.



---

archive/issue_comments_007744.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2007-11-21T19:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7744",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_007745.json:
```json
{
    "body": "WARNING: This is full of bugs and issues.  \n\nE.g.,             \n\n```\nsage: E = EllipticCurve([0, 0, 1/216, -7/1296, 1/7776])\nsage: F = E.global_integral_model(); F\noutputs a non-integral model!\n```\n\n\nDO NOT apply this until further patche(s) are posted.\n\nI'm working on some now.\n\nALSO -- there are many new functions with no doctets.",
    "created_at": "2007-12-15T07:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7745",
    "user": "was"
}
```

WARNING: This is full of bugs and issues.  

E.g.,             

```
sage: E = EllipticCurve([0, 0, 1/216, -7/1296, 1/7776])
sage: F = E.global_integral_model(); F
outputs a non-integral model!
```


DO NOT apply this until further patche(s) are posted.

I'm working on some now.

ALSO -- there are many new functions with no doctets.



---

archive/issue_comments_007746.json:
```json
{
    "body": "Some missing doctests or things that will cause latex problems:\n\n```\na/sage/schemes/elliptic_curves/ell_generic.py\nintegral_model\nchange_weierstrass_model\n\na/sage/rings/complex_double.pyx\nargument\n\n* number_field_element.pyx -- nth_root has \\ but no r\"\"\"\n* same prob in WeierstrassIsomorphism\n* no doctest in init method for WeierstrassIsomorphism\n* no doctest in init method for WeierstrassIsomorphism _call_\n```\n",
    "created_at": "2007-12-15T07:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7746",
    "user": "was"
}
```

Some missing doctests or things that will cause latex problems:

```
a/sage/schemes/elliptic_curves/ell_generic.py
integral_model
change_weierstrass_model

a/sage/rings/complex_double.pyx
argument

* number_field_element.pyx -- nth_root has \ but no r"""
* same prob in WeierstrassIsomorphism
* no doctest in init method for WeierstrassIsomorphism
* no doctest in init method for WeierstrassIsomorphism _call_
```




---

archive/issue_comments_007747.json:
```json
{
    "body": "\n```\n[11:14pm] wstein-rvw-1239: It might be easy for you to fix the problems.\n[11:14pm] wstein-rvw-1239: E.g.,            sage: E = EllipticCurve([0, 0, 1/216, -7/1296, 1/7776])\n[11:14pm] wstein-rvw-1239:             sage: F = E.global_integral_model(); F\n[11:14pm] wstein-rvw-1239: doesn't return an integral model.\n[11:14pm] wstein-rvw-1239: E = EllipticCurve([1/3, 5]); E\n[11:14pm] wstein-rvw-1239: E.integral_model()\n[11:14pm] wstein-rvw-1239: returns a non-integral model\n```\n",
    "created_at": "2007-12-15T07:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7747",
    "user": "was"
}
```


```
[11:14pm] wstein-rvw-1239: It might be easy for you to fix the problems.
[11:14pm] wstein-rvw-1239: E.g.,            sage: E = EllipticCurve([0, 0, 1/216, -7/1296, 1/7776])
[11:14pm] wstein-rvw-1239:             sage: F = E.global_integral_model(); F
[11:14pm] wstein-rvw-1239: doesn't return an integral model.
[11:14pm] wstein-rvw-1239: E = EllipticCurve([1/3, 5]); E
[11:14pm] wstein-rvw-1239: E.integral_model()
[11:14pm] wstein-rvw-1239: returns a non-integral model
```




---

archive/issue_comments_007748.json:
```json
{
    "body": "Attachment\n\ntentative_trac-1239.patch",
    "created_at": "2007-12-15T07:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7748",
    "user": "was"
}
```

Attachment

tentative_trac-1239.patch



---

archive/issue_comments_007749.json:
```json
{
    "body": "[good review -- on extcode] The extcode bundle is *OK* -- no problems.",
    "created_at": "2007-12-15T07:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7749",
    "user": "was"
}
```

[good review -- on extcode] The extcode bundle is *OK* -- no problems.



---

archive/issue_comments_007750.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-15T07:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7750",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_007751.json:
```json
{
    "body": "The global_integral_model / integral_model code in question is John Cremona's. I'll look into it more. \n\nWARNING: The extcode patch can't go in without this one (due to interface changes).",
    "created_at": "2007-12-15T07:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7751",
    "user": "robertwb"
}
```

The global_integral_model / integral_model code in question is John Cremona's. I'll look into it more. 

WARNING: The extcode patch can't go in without this one (due to interface changes).



---

archive/issue_comments_007752.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-15T07:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7752",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007753.json:
```json
{
    "body": "Attachment\n\nTurned out to be an indentation issue. Also added another doctest. \n\nShould be ready to go in now.",
    "created_at": "2007-12-15T08:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7753",
    "user": "robertwb"
}
```

Attachment

Turned out to be an indentation issue. Also added another doctest. 

Should be ready to go in now.



---

archive/issue_comments_007754.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T08:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7754",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_007755.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T08:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1239#issuecomment-7755",
    "user": "mabshoff"
}
```

Resolution: fixed
