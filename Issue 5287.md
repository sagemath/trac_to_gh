# Issue 5287: [with patch, needs review] improve mq.SR usability and performance

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-02-16 16:33:44

Assignee: malb

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



---

Attachment

This patch applied to my 3.3.rc2 merge tree does pass long doctests.

Cheers,

Michael


---

Comment by was created at 2009-02-18 00:38:00

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
sage: search_src('malb`@`informatik.uni-bremen.de')
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

Attachment

addresses referee's concerns


---

Comment by malb created at 2009-02-18 11:22:16

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

Comment by was created at 2009-02-20 05:50:58

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

Comment by was created at 2009-02-20 05:55:06

I just want to add that I'm ok with this being merged since there are a 1000 other places in sage with similar but worse issues.  And probably 50% are my fault.


---

Comment by mabshoff created at 2009-02-20 06:40:22

Merged both patches in Sage 3.3.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 06:40:22

Resolution: fixed


---

Comment by malb created at 2009-02-20 11:21:24

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

Comment by malb created at 2009-02-20 11:52:26

See #5321


---

Comment by malb created at 2009-02-21 03:07:56

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
