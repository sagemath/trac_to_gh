# Issue 2485: Complete docstrings and doctests for schemes/elliptic_curves

archive/issues_002485.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  ncalexan\n\nKeywords: elliptic curves\n\nFollowing Doc Days 2 on 2008-03-09 I am working on making the docstrings and tests for schemes/elliptic_curves as complete as I can.  A patch based on 2.10.3 will be posted here in time for 2.10.4, I hope.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2485\n\n",
    "created_at": "2008-03-12T09:25:54Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Complete docstrings and doctests for schemes/elliptic_curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2485",
    "user": "cremona"
}
```
Assignee: cremona

CC:  ncalexan

Keywords: elliptic curves

Following Doc Days 2 on 2008-03-09 I am working on making the docstrings and tests for schemes/elliptic_curves as complete as I can.  A patch based on 2.10.3 will be posted here in time for 2.10.4, I hope.


Issue created by migration from https://trac.sagemath.org/ticket/2485





---

archive/issue_comments_016834.json:
```json
{
    "body": "Hi John,\n\nI assume you're CCed on this.  I am actively using the hyperelliptic curve code and have lots of things to fix/upgrade.  Some of my work will touch schemes/elliptic_curves and I don't want to step on your toes.  I'm CCed on this; when your patch is done I'll gladly referee it.\n\nNick",
    "created_at": "2008-03-13T07:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2485#issuecomment-16834",
    "user": "ncalexan"
}
```

Hi John,

I assume you're CCed on this.  I am actively using the hyperelliptic curve code and have lots of things to fix/upgrade.  Some of my work will touch schemes/elliptic_curves and I don't want to step on your toes.  I'm CCed on this; when your patch is done I'll gladly referee it.

Nick



---

archive/issue_comments_016835.json:
```json
{
    "body": "Thanks Nick, that will be very helpful.  It's unlikely that we will conflict.  There is almost nothing I am planning to do except add to docstrings.  John",
    "created_at": "2008-03-13T09:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2485#issuecomment-16835",
    "user": "cremona"
}
```

Thanks Nick, that will be very helpful.  It's unlikely that we will conflict.  There is almost nothing I am planning to do except add to docstrings.  John



---

archive/issue_comments_016836.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-14T17:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2485#issuecomment-16836",
    "user": "cremona"
}
```

Attachment



---

archive/issue_comments_016837.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-14T17:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2485#issuecomment-16837",
    "user": "cremona"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016838.json:
```json
{
    "body": "The attached patch adds many docstrings to the following files (based on 2.10.3):\n\n* M sage/schemes/elliptic_curves/ell_finite_field.py\n* M sage/schemes/elliptic_curves/ell_generic.py\n* M sage/schemes/elliptic_curves/ell_modular_symbols.py\n* M sage/schemes/elliptic_curves/ell_number_field.py\n* M sage/schemes/elliptic_curves/ell_padic.py\n* M sage/schemes/elliptic_curves/ell_padic_field.py\n* M sage/schemes/elliptic_curves/ell_point.py\n* M sage/schemes/elliptic_curves/ell_rational_field.py\n* M sage/schemes/elliptic_curves/ell_tate_curve.py\n* M sage/schemes/elliptic_curves/gp_cremona.py\n* M sage/schemes/elliptic_curves/gp_simon.py\n\nIn addition there are a very few changes other than docstrings.\n* Some internal and local functions have had _ prepended to their names to explain why they may not have doctests\n* The output type of `modular_parametrization()` in ell_rational_field.py has been changed from a list of pari types to a list of Sage Laurent Series in the variable q\n* In addition to has_cm for elliptic curves over QQ, there is now a function cm_discriminant().  These two functions refer to a new global (to ell_rational_field.py) dict structure called CMJ.\n\nI hope all this will be found useful!  There is still more to do in this directory:\n\nOverall weighted coverage score:  66.1%\n\nbut a lot of that is explained by monsky_washnitzer.py: 23% (25 of 107) whci someone else will do, I hope.",
    "created_at": "2008-03-14T17:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2485#issuecomment-16838",
    "user": "cremona"
}
```

The attached patch adds many docstrings to the following files (based on 2.10.3):

* M sage/schemes/elliptic_curves/ell_finite_field.py
* M sage/schemes/elliptic_curves/ell_generic.py
* M sage/schemes/elliptic_curves/ell_modular_symbols.py
* M sage/schemes/elliptic_curves/ell_number_field.py
* M sage/schemes/elliptic_curves/ell_padic.py
* M sage/schemes/elliptic_curves/ell_padic_field.py
* M sage/schemes/elliptic_curves/ell_point.py
* M sage/schemes/elliptic_curves/ell_rational_field.py
* M sage/schemes/elliptic_curves/ell_tate_curve.py
* M sage/schemes/elliptic_curves/gp_cremona.py
* M sage/schemes/elliptic_curves/gp_simon.py

In addition there are a very few changes other than docstrings.
* Some internal and local functions have had _ prepended to their names to explain why they may not have doctests
* The output type of `modular_parametrization()` in ell_rational_field.py has been changed from a list of pari types to a list of Sage Laurent Series in the variable q
* In addition to has_cm for elliptic curves over QQ, there is now a function cm_discriminant().  These two functions refer to a new global (to ell_rational_field.py) dict structure called CMJ.

I hope all this will be found useful!  There is still more to do in this directory:

Overall weighted coverage score:  66.1%

but a lot of that is explained by monsky_washnitzer.py: 23% (25 of 107) whci someone else will do, I hope.



---

archive/issue_comments_016839.json:
```json
{
    "body": "I think this patch should be applied, because it is mostly good, but it's not perfect.  I've noted a few nits below, only one of which (the KeyError) should be addressed before application.\n\nThanks for your effort, John!\n\nThis is probably not your bug, John, but it doesn't look right.\n\n\n```\n606\t        EXAMPLES: \n607\t            sage: E=EllipticCurve(GF(5),[1,1]) \n608\t            sage: E._homset_class(GF(5^10,'a'),GF(5)) \n609\t            Abelian group of points on Finite Field in a of size 5^10\n```\n\n\nAlso, I really worry about double underscore functions at all -- I say replace with single underscore; then doctesting isn't so strange.\n\n\n```\n \t632\t            sage: E=EllipticCurve(QQ,[1,1]) \n \t633\t            sage: E._EllipticCurve_generic__is_over_RationalField() \n \t634\t            True \n```\n\n\nThis comment looks outdated, and should be removed:\n\n```\n \t521\t        def _pval(x):   # cannot be used for x=0 \n \t522\t            \"\"\" \n \t523\t            Local function returning the valuation of x at P \n \t524\t            \"\"\" \n522\t525\t            if x==0: return Infinity \n```\n\n\nI think things like\n\n```\n1809\t2264\t    def label(self): \n1810\t2265\t        r\"\"\" \n1811\t2266\t        Exactly the same as the \\code{cremona_label()} command. \n \t2267\t \n \t2268\t        EXAMPLES: \n \t2269\t            sage: E=EllipticCurve('389a1') \n \t2270\t            sage: E.label() \n \t2271\t            '389a1' \n \t2272\t \n1812\t2273\t        \"\"\" \n1813\t2274\t        return self.cremona_label() \n```\n\n\nshould be replaced with `label = cremona_label`.\n\nThis is not very helpful -- I would prefer, \"A ValueError is raised...\"\n\n```\n        2390\t        An error is raised if the curve does not have CM (see the \n \t2391\t        function has_cm()) \n```\n\nand change the code to raise ValueError; it seems more appropriate than KeyError.",
    "created_at": "2008-03-14T18:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2485#issuecomment-16839",
    "user": "ncalexan"
}
```

I think this patch should be applied, because it is mostly good, but it's not perfect.  I've noted a few nits below, only one of which (the KeyError) should be addressed before application.

Thanks for your effort, John!

This is probably not your bug, John, but it doesn't look right.


```
606	        EXAMPLES: 
607	            sage: E=EllipticCurve(GF(5),[1,1]) 
608	            sage: E._homset_class(GF(5^10,'a'),GF(5)) 
609	            Abelian group of points on Finite Field in a of size 5^10
```


Also, I really worry about double underscore functions at all -- I say replace with single underscore; then doctesting isn't so strange.


```
 	632	            sage: E=EllipticCurve(QQ,[1,1]) 
 	633	            sage: E._EllipticCurve_generic__is_over_RationalField() 
 	634	            True 
```


This comment looks outdated, and should be removed:

```
 	521	        def _pval(x):   # cannot be used for x=0 
 	522	            """ 
 	523	            Local function returning the valuation of x at P 
 	524	            """ 
522	525	            if x==0: return Infinity 
```


I think things like

```
1809	2264	    def label(self): 
1810	2265	        r""" 
1811	2266	        Exactly the same as the \code{cremona_label()} command. 
 	2267	 
 	2268	        EXAMPLES: 
 	2269	            sage: E=EllipticCurve('389a1') 
 	2270	            sage: E.label() 
 	2271	            '389a1' 
 	2272	 
1812	2273	        """ 
1813	2274	        return self.cremona_label() 
```


should be replaced with `label = cremona_label`.

This is not very helpful -- I would prefer, "A ValueError is raised..."

```
        2390	        An error is raised if the curve does not have CM (see the 
 	2391	        function has_cm()) 
```

and change the code to raise ValueError; it seems more appropriate than KeyError.



---

archive/issue_comments_016840.json:
```json
{
    "body": "Attachment\n\nApply after 8866.patch",
    "created_at": "2008-03-14T19:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2485#issuecomment-16840",
    "user": "cremona"
}
```

Attachment

Apply after 8866.patch



---

archive/issue_comments_016841.json:
```json
{
    "body": "Thanks a lot for the fast review, Nick.\n\n* I left the _homset_class test as it was.  That was one where I had a hard time working out what the function did and what was the point of it.  I still do not know.\n\n* Doctesting double-underscore functions is indeed very hard.  For things like __init__() the test does not mention __init__() and \"sage -t\" complains.  For ones like `_EllipticCurve_generic__is_over_RationalField()` (where in the code the function is simply `__is_over_RationalField()` there's no way the user will ever get to use them, and putting in tests will hardly help developers.\n\n* I fixed the others as you suggested, including changing the KeyError to ValueError -- it's just that the error is first raised as a KeyError (the value of j is not a key in the dict CMJ), but the user need not know that.",
    "created_at": "2008-03-14T19:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2485#issuecomment-16841",
    "user": "cremona"
}
```

Thanks a lot for the fast review, Nick.

* I left the _homset_class test as it was.  That was one where I had a hard time working out what the function did and what was the point of it.  I still do not know.

* Doctesting double-underscore functions is indeed very hard.  For things like __init__() the test does not mention __init__() and "sage -t" complains.  For ones like `_EllipticCurve_generic__is_over_RationalField()` (where in the code the function is simply `__is_over_RationalField()` there's no way the user will ever get to use them, and putting in tests will hardly help developers.

* I fixed the others as you suggested, including changing the KeyError to ValueError -- it's just that the error is first raised as a KeyError (the value of j is not a key in the dict CMJ), but the user need not know that.



---

archive/issue_comments_016842.json:
```json
{
    "body": "Both patches apply cleanly against 2.10.3, and all doctests pass in sage/schemes/elliptic_curves/\n\nThe second patch appears to fix the issues brought up by the first reviewer, so I say \"thumbs up\".",
    "created_at": "2008-03-15T18:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2485#issuecomment-16842",
    "user": "AlexGhitza"
}
```

Both patches apply cleanly against 2.10.3, and all doctests pass in sage/schemes/elliptic_curves/

The second patch appears to fix the issues brought up by the first reviewer, so I say "thumbs up".



---

archive/issue_comments_016843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T19:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2485#issuecomment-16843",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016844.json:
```json
{
    "body": "Merged both patches in Sage 2.10.4.rc0",
    "created_at": "2008-03-15T19:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2485#issuecomment-16844",
    "user": "mabshoff"
}
```

Merged both patches in Sage 2.10.4.rc0
