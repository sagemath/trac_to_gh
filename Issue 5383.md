# Issue 5383: isinstance(PrincipalIdealDomain) should be replaced with a method .is_principal_ideal_domain()

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-02-26 04:41:00

Assignee: was

Keywords: principal ideal domain span free module isinstance

This is the cause of things like:


```
sage: R.<x, y> = QQ[]
sage: M = R^2
sage: span(R, vector([1, 0]))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/dhcp_v009_038.mobile.uci.edu/301/_Users_ncalexan_Documents_School_rumely_polynomial_ring_as_module2_sage_142.py in <module>()

/Users/ncalexan/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in span(gens, base_ring, check, already_echelonized)
    408 
    409     if not isinstance(R, principal_ideal_domain.PrincipalIdealDomain):
--> 410         raise TypeError, "The base_ring (= %s) must be a principal ideal domain."%R
    411     if len(gens) == 0:
    412         return FreeModule(R, 0)

TypeError: The base_ring (= Multivariate Polynomial Ring in x, y over Rational Field) must be a principal ideal domain.
```


Surprisingly few places where this bites us:


```
sage: search_src('PrincipalIdealDomain')
modules/free_module.py:        elif isinstance(base_ring, principal_ideal_domain.PrincipalIdealDomain):
modules/free_module.py:    if not isinstance(R, principal_ideal_domain.PrincipalIdealDomain):
modules/free_module.py:        if not isinstance(base_ring, principal_ideal_domain.PrincipalIdealDomain):
modules/free_quadratic_module.py:    elif isinstance(base_ring, principal_ideal_domain.PrincipalIdealDomain):
rings/all.py:from principal_ideal_domain import PrincipalIdealDomain, is_PrincipalIdealDomain
rings/all.py:from principal_ideal_domain_element import PrincipalIdealDomainElement, is_PrincipalIdealDomainElement
rings/ideal.py:    if isinstance(R, sage.rings.principal_ideal_domain.PrincipalIdealDomain):
<snip>
```



---

Comment by ncalexan created at 2009-02-26 17:46:18

I realize now, of course, that QQ['x', 'y'] is not a PID... but I still think our type dependent implementation is not good :)


---

Comment by mabshoff created at 2009-03-01 02:27:26

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by mhansen created at 2013-07-23 14:26:46

This should do it.


---

Comment by mhansen created at 2013-07-23 14:26:46

Changing status from new to needs_review.


---

Attachment


---

Comment by rws created at 2014-02-18 07:32:14

Changing status from needs_review to positive_review.


---

Comment by rws created at 2014-02-18 07:32:14

Easy ticket.
----
New commits:


---

Comment by git created at 2014-02-20 17:27:49

Changing status from positive_review to needs_review.


---

Comment by git created at 2014-02-20 17:27:49

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by rws created at 2014-02-20 17:46:28

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-23 07:46:34

Resolution: fixed
