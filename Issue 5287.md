# Issue 5287: [with patch, needs review] improve mq.SR usability and performance

archive/issues_005287.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  rpw\n\nKeywords: aes, crypto, mq\n\nThe attached patch contains the following improvements for `mq.SR`:\n* faster polynomial_system generation by pre-computing S-Box polynomials\n* support for finite extension field elements in `mq.SBox` (needed by mq.SR)\n* more module level documentation for `mq.sr`\n* new `sbox()` function which returns AES (or SR) `SBox` object\n* `AllowZeroInversionsContext()` to handle table creation and such\n* more user friendly encryption, i.e. accept more inputs and make sense of them\n* `varstr()` function to return a specific string rather than a list of strings using `varstrs()`\n* `variable_dict()` function which gives fast access to string -> variable mappings\n* ring constructor accepts optional `reverse_variables` parameter now\n* `SR_gf2_2` class as example how to customize things\n* added `constant_coefficient()` function to `BooleanPolynomial`s (needed by `sbox()`)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5287\n\n",
    "created_at": "2009-02-16T16:33:44Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] improve mq.SR usability and performance",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5287",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  rpw

Keywords: aes, crypto, mq

The attached patch contains the following improvements for `mq.SR`:
* faster polynomial_system generation by pre-computing S-Box polynomials
* support for finite extension field elements in `mq.SBox` (needed by mq.SR)
* more module level documentation for `mq.sr`
* new `sbox()` function which returns AES (or SR) `SBox` object
* `AllowZeroInversionsContext()` to handle table creation and such
* more user friendly encryption, i.e. accept more inputs and make sense of them
* `varstr()` function to return a specific string rather than a list of strings using `varstrs()`
* `variable_dict()` function which gives fast access to string -> variable mappings
* ring constructor accepts optional `reverse_variables` parameter now
* `SR_gf2_2` class as example how to customize things
* added `constant_coefficient()` function to `BooleanPolynomial`s (needed by `sbox()`)


Issue created by migration from https://trac.sagemath.org/ticket/5287





---

archive/issue_comments_040550.json:
```json
{
    "body": "Attachment [better_sr.patch](tarball://root/attachments/some-uuid/ticket5287/better_sr.patch) by mabshoff created at 2009-02-17 21:55:46\n\nThis patch applied to my 3.3.rc2 merge tree does pass long doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T21:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5287#issuecomment-40550",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [better_sr.patch](tarball://root/attachments/some-uuid/ticket5287/better_sr.patch) by mabshoff created at 2009-02-17 21:55:46

This patch applied to my 3.3.rc2 merge tree does pass long doctests.

Cheers,

Michael



---

archive/issue_comments_040551.json:
```json
{
    "body": "REVIEW:\n\n# In the file sbox.py\n\nI don't like this:\n\n```\nsage: S = mq.SBox([7,6,0,4,2,5,1,3])\nsage: S(long(7))\nTypeError: object of type 'long' has no len()\n```\n\n\nI don't like this:\n\n```\nfrom sage.all import vector \n```\n\nCould you import it a little more precisely?\n\nI *really* don't like this:\n\n```\nsage: S = mq.SBox([7,6,0,4,2,5,1,3])\nsage: S([1]*10^6)\noutputs a *million page* exception!\n```\n\n\n# sr.py\n\n* I'm glad you're fixing your email address. However, even after this patch there are at least 30 other places in the sage core library with your old address:\n\n```\nsage: search_src('malb@informatik.uni-bremen.de')\nover 30 lines output\n```\n\n\n* Regarding\n\n```\nsage: I.variety() # order is random-ish \n```\n\nYou could make the output into a sorted list (instead of a dict) so the output can be checked exactly.\n\n* Here is a backslash without r\"\"\":\n\n```\n \t1451\t        \"\"\" \n \t1452\t        Return a dictionary to access variables in \\code{self.R} by \n \t1453\t        their names. \n```\n\n\n* I wish this function had more tests, which at a minimum illustrated all the options:\n\n```\ndef inversion_polynomials_single_sbox(self, x=None, w=None, biaffine_only=None, correct_only=None, groebner=False):\n```\n\nRight now many of the options aren't tested at all.",
    "created_at": "2009-02-18T00:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5287#issuecomment-40551",
    "user": "https://github.com/williamstein"
}
```

REVIEW:

# In the file sbox.py

I don't like this:

```
sage: S = mq.SBox([7,6,0,4,2,5,1,3])
sage: S(long(7))
TypeError: object of type 'long' has no len()
```


I don't like this:

```
from sage.all import vector 
```

Could you import it a little more precisely?

I *really* don't like this:

```
sage: S = mq.SBox([7,6,0,4,2,5,1,3])
sage: S([1]*10^6)
outputs a *million page* exception!
```


# sr.py

* I'm glad you're fixing your email address. However, even after this patch there are at least 30 other places in the sage core library with your old address:

```
sage: search_src('malb@informatik.uni-bremen.de')
over 30 lines output
```


* Regarding

```
sage: I.variety() # order is random-ish 
```

You could make the output into a sorted list (instead of a dict) so the output can be checked exactly.

* Here is a backslash without r""":

```
 	1451	        """ 
 	1452	        Return a dictionary to access variables in \code{self.R} by 
 	1453	        their names. 
```


* I wish this function had more tests, which at a minimum illustrated all the options:

```
def inversion_polynomials_single_sbox(self, x=None, w=None, biaffine_only=None, correct_only=None, groebner=False):
```

Right now many of the options aren't tested at all.



---

archive/issue_comments_040552.json:
```json
{
    "body": "Attachment [trac_5287_corrections.patch](tarball://root/attachments/some-uuid/ticket5287/trac_5287_corrections.patch) by @malb created at 2009-02-18 11:16:37\n\naddresses referee's concerns",
    "created_at": "2009-02-18T11:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5287#issuecomment-40552",
    "user": "https://github.com/malb"
}
```

Attachment [trac_5287_corrections.patch](tarball://root/attachments/some-uuid/ticket5287/trac_5287_corrections.patch) by @malb created at 2009-02-18 11:16:37

addresses referee's concerns



---

archive/issue_comments_040553.json:
```json
{
    "body": "Replying to [comment:2 was]:\n> I don't like this:\n\n```\nsage: S = mq.SBox([7,6,0,4,2,5,1,3])\nsage: S(long(7))\nTypeError: object of type 'long' has no len()\n```\n\n\n*fixed*\n\n> I don't like this:\n\n```\nfrom sage.all import vector \n```\n\n\n*fixed*\n\n> I *really* don't like this:\n\n```\nsage: S = mq.SBox([7,6,0,4,2,5,1,3])\nsage: S([1]*10^6)\noutputs a *million page* exception!\n```\n\n\nThe string of the TypeError depends on the length of the string of X now. I assume this might be controversial?\n \n> I'm glad you're fixing your email address. However, even after this patch there are at least \n> 30 other places in the sage core library with your old address:\n\n`@`informatik.uni-bremen.de still works so I see no rush fixing all those. Also, it seems Uni-Bremen is more generous when it comes to old e-mail addresses, you get to keep them forever. On the other hand, I'm not so sure about RHUL. The main reason I'm adding `M.R.Albrecht` to `sr.py` is to indicate that someone from RHUL worked on this. Since a team from RHUL defined SR in the first place, some people might consider this relevant.\n\n> Regarding\n\n```\nsage: I.variety() # order is random-ish \n```\n\n\nIt is printed sorted now, but I didn't change what variety() returns, just the doctest.\n\n> Here is a backslash without `r\"\"\"`\n\n*fixed*\n\n>  I wish this function had more tests, which at a minimum illustrated all the options:\n\n```\ndef inversion_polynomials_single_sbox(self, x=None, w=None, biaffine_only=None, correct_only=None, groebner=False):\n```\n\n\nI added one more doctest. Note that most options are ignored anyway (as documented in the docstring).",
    "created_at": "2009-02-18T11:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5287#issuecomment-40553",
    "user": "https://github.com/malb"
}
```

Replying to [comment:2 was]:
> I don't like this:

```
sage: S = mq.SBox([7,6,0,4,2,5,1,3])
sage: S(long(7))
TypeError: object of type 'long' has no len()
```


*fixed*

> I don't like this:

```
from sage.all import vector 
```


*fixed*

> I *really* don't like this:

```
sage: S = mq.SBox([7,6,0,4,2,5,1,3])
sage: S([1]*10^6)
outputs a *million page* exception!
```


The string of the TypeError depends on the length of the string of X now. I assume this might be controversial?
 
> I'm glad you're fixing your email address. However, even after this patch there are at least 
> 30 other places in the sage core library with your old address:

`@`informatik.uni-bremen.de still works so I see no rush fixing all those. Also, it seems Uni-Bremen is more generous when it comes to old e-mail addresses, you get to keep them forever. On the other hand, I'm not so sure about RHUL. The main reason I'm adding `M.R.Albrecht` to `sr.py` is to indicate that someone from RHUL worked on this. Since a team from RHUL defined SR in the first place, some people might consider this relevant.

> Regarding

```
sage: I.variety() # order is random-ish 
```


It is printed sorted now, but I didn't change what variety() returns, just the doctest.

> Here is a backslash without `r"""`

*fixed*

>  I wish this function had more tests, which at a minimum illustrated all the options:

```
def inversion_polynomials_single_sbox(self, x=None, w=None, biaffine_only=None, correct_only=None, groebner=False):
```


I added one more doctest. Note that most options are ignored anyway (as documented in the docstring).



---

archive/issue_comments_040554.json:
```json
{
    "body": "* \n> The string of the TypeError? depends on the length of the string \n> of X now. I assume this might be controversial? \n\nThat's not much better, since computing len(str(X)) can take a very long time:\n\n```\nsage: S = mq.SBox([7,6,0,4,2,5,1,3])\nsage: S([1]*10^9)\n[wait 15 minutes]\nTypeError: Cannot apply SBox to provided element.\n```\n\n\n* \"The main reason I'm adding M.R.Albrecht to sr.py is to indicate that someone from RHUL worked on this. Since a team from RHUL defined SR in the first place, some people might consider this relevant.\"\n\nWouldnt it then be better to explicitly somehow emphasize that this module is authored by a student at RHUL working with the group that defined SR originally, and maybe give a reference to where it originally appeared (?).  It just seems that you are being perhaps more subtle than necessary. \n\n* \n\n```\nsage: I.variety() # order is random-ish \n```\n\n\"It is printed sorted now, but I didn't change what variety() returns, just the doctest.\"\n\nThat doesn't help at all, since in sage-3.4 variety could suddenly return some wrong points, and this doctest would never catch that. \n\n* \"Note that most options are ignored anyway (as documented in the docstring).\"\n\nThere could be a test that illustrates the options all being ignored, which is in the TESTS: section. \n\nI'm going to give this a positive review, since perhaps I'm being overly picky.  I don't feel all my referee remarks were addressed.   I'll leave Martin doing the other changes or not up to his conscious.",
    "created_at": "2009-02-20T05:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5287#issuecomment-40554",
    "user": "https://github.com/williamstein"
}
```

* 
> The string of the TypeError? depends on the length of the string 
> of X now. I assume this might be controversial? 

That's not much better, since computing len(str(X)) can take a very long time:

```
sage: S = mq.SBox([7,6,0,4,2,5,1,3])
sage: S([1]*10^9)
[wait 15 minutes]
TypeError: Cannot apply SBox to provided element.
```


* "The main reason I'm adding M.R.Albrecht to sr.py is to indicate that someone from RHUL worked on this. Since a team from RHUL defined SR in the first place, some people might consider this relevant."

Wouldnt it then be better to explicitly somehow emphasize that this module is authored by a student at RHUL working with the group that defined SR originally, and maybe give a reference to where it originally appeared (?).  It just seems that you are being perhaps more subtle than necessary. 

* 

```
sage: I.variety() # order is random-ish 
```

"It is printed sorted now, but I didn't change what variety() returns, just the doctest."

That doesn't help at all, since in sage-3.4 variety could suddenly return some wrong points, and this doctest would never catch that. 

* "Note that most options are ignored anyway (as documented in the docstring)."

There could be a test that illustrates the options all being ignored, which is in the TESTS: section. 

I'm going to give this a positive review, since perhaps I'm being overly picky.  I don't feel all my referee remarks were addressed.   I'll leave Martin doing the other changes or not up to his conscious.



---

archive/issue_comments_040555.json:
```json
{
    "body": "I just want to add that I'm ok with this being merged since there are a 1000 other places in sage with similar but worse issues.  And probably 50% are my fault.",
    "created_at": "2009-02-20T05:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5287#issuecomment-40555",
    "user": "https://github.com/williamstein"
}
```

I just want to add that I'm ok with this being merged since there are a 1000 other places in sage with similar but worse issues.  And probably 50% are my fault.



---

archive/issue_events_012289.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-20T06:40:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5287#event-12289"
}
```



---

archive/issue_comments_040556.json:
```json
{
    "body": "Merged both patches in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T06:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5287#issuecomment-40556",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_comments_040557.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T06:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5287#issuecomment-40557",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040558.json:
```json
{
    "body": "Replying to [comment:4 was]:\n> That's not much better, since computing len(str(X)) can take a very long time:\n {{{\nsage: S = mq.SBox([7,6,0,4,2,5,1,3])\nsage: S([1]*10^9)\n[wait 15 minutes]\nTypeError: Cannot apply SBox to provided element.\n }}}\n\nNote that the above example does not show what you mean to show:\n\n\n```\nsage: %time l = [1]*10^9\nCPU times: user 11.19 s, sys: 5.13 s, total: 16.32 s\nWall time: 16.31 s\nsage: %time len(l)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n1000000000\n```\n\n\ni.e. you're timing the creation of the list --- which is outside of the `SBox` class.\n\n> * \"The main reason I'm adding M.R.Albrecht to sr.py is to indicate that someone from RHUL worked on this. Since a team from RHUL defined SR in the first place, some people might consider this relevant.\"\n> \n> Wouldnt it then be better to explicitly somehow emphasize that this module is authored by a student at RHUL working with the group that defined SR originally, and maybe give a reference to where it originally appeared (?).  It just seems that you are being perhaps more subtle than necessary. \n\nA reference is already given in the module documentation. I don't think adding an explicit statement about authorship is necessary. It's just when people look explicitly they see it. I have no strong feelings about this either way though so if you feel it would improve things, I can address that.\n\n> >\n> > \"It is printed sorted now, but I didn't change what variety() returns, just the doctest.\"\n> \n> That doesn't help at all, since in sage-3.4 variety could suddenly return some wrong points, and this doctest would never catch that. \n\nI don't understand, the doctest is now:\n\n\n```\n   sage: I = F.ideal()\n   sage: for V in I.variety():\n   ...    for k,v in sorted(V.iteritems()):\n   ...       print k,v\n   ...    print \n```\n\n\nhow does that allow the addition of wrong points? Do you mean I should evaluate the ideal members on all points to show that the result is correct ... hmmm, I could add that.\n\n> * \"Note that most options are ignored anyway (as documented in the docstring).\"\n> \n> There could be a test that illustrates the options all being ignored, which is in the TESTS: section. \n\nI'll open a new ticket addressing that.",
    "created_at": "2009-02-20T11:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5287#issuecomment-40558",
    "user": "https://github.com/malb"
}
```

Replying to [comment:4 was]:
> That's not much better, since computing len(str(X)) can take a very long time:
 {{{
sage: S = mq.SBox([7,6,0,4,2,5,1,3])
sage: S([1]*10^9)
[wait 15 minutes]
TypeError: Cannot apply SBox to provided element.
 }}}

Note that the above example does not show what you mean to show:


```
sage: %time l = [1]*10^9
CPU times: user 11.19 s, sys: 5.13 s, total: 16.32 s
Wall time: 16.31 s
sage: %time len(l)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
1000000000
```


i.e. you're timing the creation of the list --- which is outside of the `SBox` class.

> * "The main reason I'm adding M.R.Albrecht to sr.py is to indicate that someone from RHUL worked on this. Since a team from RHUL defined SR in the first place, some people might consider this relevant."
> 
> Wouldnt it then be better to explicitly somehow emphasize that this module is authored by a student at RHUL working with the group that defined SR originally, and maybe give a reference to where it originally appeared (?).  It just seems that you are being perhaps more subtle than necessary. 

A reference is already given in the module documentation. I don't think adding an explicit statement about authorship is necessary. It's just when people look explicitly they see it. I have no strong feelings about this either way though so if you feel it would improve things, I can address that.

> >
> > "It is printed sorted now, but I didn't change what variety() returns, just the doctest."
> 
> That doesn't help at all, since in sage-3.4 variety could suddenly return some wrong points, and this doctest would never catch that. 

I don't understand, the doctest is now:


```
   sage: I = F.ideal()
   sage: for V in I.variety():
   ...    for k,v in sorted(V.iteritems()):
   ...       print k,v
   ...    print 
```


how does that allow the addition of wrong points? Do you mean I should evaluate the ideal members on all points to show that the result is correct ... hmmm, I could add that.

> * "Note that most options are ignored anyway (as documented in the docstring)."
> 
> There could be a test that illustrates the options all being ignored, which is in the TESTS: section. 

I'll open a new ticket addressing that.



---

archive/issue_comments_040559.json:
```json
{
    "body": "See #5321",
    "created_at": "2009-02-20T11:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5287#issuecomment-40559",
    "user": "https://github.com/malb"
}
```

See #5321



---

archive/issue_comments_040560.json:
```json
{
    "body": "> Note that the above example does not show what you mean to show:\n> \n\n```\nsage: %time l = [1]*10^9\nCPU times: user 11.19 s, sys: 5.13 s, total: 16.32 s\nWall time: 16.31 s\nsage: %time len(l)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n1000000000\n```\n\n>\n> i.e. you're timing the creation of the list --- which is outside of the `SBox` class.\n\nArgh, I am an idiot. Strike that comment I fully get your point.",
    "created_at": "2009-02-21T03:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5287#issuecomment-40560",
    "user": "https://github.com/malb"
}
```

> Note that the above example does not show what you mean to show:
> 

```
sage: %time l = [1]*10^9
CPU times: user 11.19 s, sys: 5.13 s, total: 16.32 s
Wall time: 16.31 s
sage: %time len(l)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
1000000000
```

>
> i.e. you're timing the creation of the list --- which is outside of the `SBox` class.

Argh, I am an idiot. Strike that comment I fully get your point.
