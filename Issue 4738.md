# Issue 4738: base_ring of orders in relative number fields is wrong

archive/issues_004738.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein\n\nKeywords: base ring relative number field order\n\nI think that the last ring should be the ring of integers of the relative number field.\n\n```\nsage: K = NumberField([x^2 + 2, x^2 + 3], 'a')\nsage: K.base_ring()\nNumber Field in a1 with defining polynomial x^2 + 3\nsage: K.maximal_order()\nRelative Order in Number Field in a0 with defining polynomial x^2 + 2 over its base field\nsage: K.maximal_order().base_ring()\nInteger Ring\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4738\n\n",
    "created_at": "2008-12-07T20:03:53Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "base_ring of orders in relative number fields is wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4738",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @williamstein

Keywords: base ring relative number field order

I think that the last ring should be the ring of integers of the relative number field.

```
sage: K = NumberField([x^2 + 2, x^2 + 3], 'a')
sage: K.base_ring()
Number Field in a1 with defining polynomial x^2 + 3
sage: K.maximal_order()
Relative Order in Number Field in a0 with defining polynomial x^2 + 2 over its base field
sage: K.maximal_order().base_ring()
Integer Ring
```

Issue created by migration from https://trac.sagemath.org/ticket/4738





---

archive/issue_comments_035697.json:
```json
{
    "body": "Sorry, the ring of integesr of the base field of the relative number field.",
    "created_at": "2008-12-07T20:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35697",
    "user": "https://github.com/ncalexan"
}
```

Sorry, the ring of integesr of the base field of the relative number field.



---

archive/issue_comments_035698.json:
```json
{
    "body": "While trying to fix this, I discovered that finding orders in relative number fields is ridiculously slow.  I think pari probably will help here, either but computing it directly or by computing a basis for the absolute order and then constructing a basis for the relative order from it.\n\n```\nsage: K.<a,b> = NumberField([x^4 + 1, x^4 - 3])\nsage: K.base_field().maximal_order()\nMaximal Order in Number Field in b with defining polynomial x^4 - 3\nsage: K.absolute_field('c').maximal_order()\nMaximal Order in Number Field in c with defining polynomial x^16 - 8*x^12 + 432*x^8 + 640*x^4 + 256\nsage: K.absolute_field('c').maximal_order().basis()\n[3/512*c^14 + 3/352*c^12 + 3/128*c^10 + 3/704*c^8 + 1/32*c^6 + 15/176*c^4 + 1/44, 7/1024*c^15 + 1/512*c^14 + 3/704*c^13 + 1/256*c^12 + 3/256*c^11 + 1/128*c^10 + 3/1408*c^9 + 3/64*c^8 + 1/64*c^7 + 1/32*c^6 + 15/352*c^5 + 1/16*c^4 + 1/88*c, 35/5632*c^14 + 3/256*c^12 + 7/704*c^10 + 3/64*c^8 + 1/88*c^6 + 1/16*c^4 + 1/88*c^2, 79/11264*c^15 + 3/512*c^14 + 7/512*c^13 + 1/128*c^12 + 7/1408*c^11 + 1/128*c^10 + 3/128*c^9 + 1/32*c^8 + 1/176*c^7 + 1/32*c^6 + 1/32*c^5 + 1/176*c^3, 1/128*c^12 + 1/32*c^8 + 1/8*c^4, 1/256*c^15 + 3/256*c^13 + 1/64*c^9 + 1/16*c^5, 1/256*c^14 + 1/64*c^10 + 1/16*c^6, 1/512*c^15 + 1/128*c^13 + 1/128*c^11 + 1/32*c^7, 1/16*c^8, 1/256*c^15 + 1/32*c^9, 1/32*c^10, 1/256*c^15 + 1/128*c^13 + 1/64*c^11, 1/64*c^12, 1/64*c^13, 1/128*c^14, 1/128*c^15]\nsage: K.maximal_order()\n  C-c C-c---------------------------------------------------------------------------\nKeyboardInterrupt                         Traceback (most recent call last)\n\n/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/47346/_Users_ncalexan__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in maximal_order(self)\n   4894         O = K.maximal_order()\n   4895         B = [from_K(z) for z in O.basis()]\n-> 4896         OK = self.order(B, check_is_integral=False, check_rank=False)\n   4897         self.__maximal_order = OK\n   4898         return OK\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in order(self, *gens, **kwds)\n   5630             gens = gens[0]\n   5631         gens = [self(x) for x in gens]\n-> 5632         return order.relative_order_from_ring_generators(gens, **kwds)\n   5633         \n   5634 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc in relative_order_from_ring_generators(gens, check_is_integral, check_rank, is_maximal, allow_subfield)\n   1640     module_gens = [to_Kabs(a) for a in gens]\n   1641     n = [a.absolute_minpoly().degree() for a in gens]\n-> 1642     absolute_order_module_gens = monomials(module_gens, n)\n   1643 \n   1644     abs_order =  absolute_order_from_module_generators(absolute_order_module_gens,\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     15         nn = list(n)\n     16         del nn[i]\n---> 17         v = monomials(w, nn)\n     18         k = len(v)\n     19         for _ in range(n[i]-1):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     15         nn = list(n)\n     16         del nn[i]\n---> 17         v = monomials(w, nn)\n     18         k = len(v)\n     19         for _ in range(n[i]-1):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     15         nn = list(n)\n     16         del nn[i]\n---> 17         v = monomials(w, nn)\n     18         k = len(v)\n     19         for _ in range(n[i]-1):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     15         nn = list(n)\n     16         del nn[i]\n---> 17         v = monomials(w, nn)\n     18         k = len(v)\n     19         for _ in range(n[i]-1):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     15         nn = list(n)\n     16         del nn[i]\n---> 17         v = monomials(w, nn)\n     18         k = len(v)\n     19         for _ in range(n[i]-1):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     15         nn = list(n)\n     16         del nn[i]\n---> 17         v = monomials(w, nn)\n     18         k = len(v)\n     19         for _ in range(n[i]-1):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     15         nn = list(n)\n     16         del nn[i]\n---> 17         v = monomials(w, nn)\n     18         k = len(v)\n     19         for _ in range(n[i]-1):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     15         nn = list(n)\n     16         del nn[i]\n---> 17         v = monomials(w, nn)\n     18         k = len(v)\n     19         for _ in range(n[i]-1):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     15         nn = list(n)\n     16         del nn[i]\n---> 17         v = monomials(w, nn)\n     18         k = len(v)\n     19         for _ in range(n[i]-1):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     15         nn = list(n)\n     16         del nn[i]\n---> 17         v = monomials(w, nn)\n     18         k = len(v)\n     19         for _ in range(n[i]-1):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     15         nn = list(n)\n     16         del nn[i]\n---> 17         v = monomials(w, nn)\n     18         k = len(v)\n     19         for _ in range(n[i]-1):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)\n     52     v = Sequence(v)\n     53     R = v.universe()\n---> 54     return _monomials(v, R, n, 0)\n     55 \n     56 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)\n     19         for _ in range(n[i]-1):\n     20             for j in range(k):\n---> 21                 v.append(v[j]*z)\n     22             z *= gens[i]\n     23         return v\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)\n      7 \n      8 def my_sigint(x, n):\n----> 9     raise KeyboardInterrupt\n     10 \n     11 def my_sigfpe(x, n):\n\nKeyboardInterrupt:\n```",
    "created_at": "2008-12-07T20:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35698",
    "user": "https://github.com/ncalexan"
}
```

While trying to fix this, I discovered that finding orders in relative number fields is ridiculously slow.  I think pari probably will help here, either but computing it directly or by computing a basis for the absolute order and then constructing a basis for the relative order from it.

```
sage: K.<a,b> = NumberField([x^4 + 1, x^4 - 3])
sage: K.base_field().maximal_order()
Maximal Order in Number Field in b with defining polynomial x^4 - 3
sage: K.absolute_field('c').maximal_order()
Maximal Order in Number Field in c with defining polynomial x^16 - 8*x^12 + 432*x^8 + 640*x^4 + 256
sage: K.absolute_field('c').maximal_order().basis()
[3/512*c^14 + 3/352*c^12 + 3/128*c^10 + 3/704*c^8 + 1/32*c^6 + 15/176*c^4 + 1/44, 7/1024*c^15 + 1/512*c^14 + 3/704*c^13 + 1/256*c^12 + 3/256*c^11 + 1/128*c^10 + 3/1408*c^9 + 3/64*c^8 + 1/64*c^7 + 1/32*c^6 + 15/352*c^5 + 1/16*c^4 + 1/88*c, 35/5632*c^14 + 3/256*c^12 + 7/704*c^10 + 3/64*c^8 + 1/88*c^6 + 1/16*c^4 + 1/88*c^2, 79/11264*c^15 + 3/512*c^14 + 7/512*c^13 + 1/128*c^12 + 7/1408*c^11 + 1/128*c^10 + 3/128*c^9 + 1/32*c^8 + 1/176*c^7 + 1/32*c^6 + 1/32*c^5 + 1/176*c^3, 1/128*c^12 + 1/32*c^8 + 1/8*c^4, 1/256*c^15 + 3/256*c^13 + 1/64*c^9 + 1/16*c^5, 1/256*c^14 + 1/64*c^10 + 1/16*c^6, 1/512*c^15 + 1/128*c^13 + 1/128*c^11 + 1/32*c^7, 1/16*c^8, 1/256*c^15 + 1/32*c^9, 1/32*c^10, 1/256*c^15 + 1/128*c^13 + 1/64*c^11, 1/64*c^12, 1/64*c^13, 1/128*c^14, 1/128*c^15]
sage: K.maximal_order()
  C-c C-c---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/47346/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in maximal_order(self)
   4894         O = K.maximal_order()
   4895         B = [from_K(z) for z in O.basis()]
-> 4896         OK = self.order(B, check_is_integral=False, check_rank=False)
   4897         self.__maximal_order = OK
   4898         return OK

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in order(self, *gens, **kwds)
   5630             gens = gens[0]
   5631         gens = [self(x) for x in gens]
-> 5632         return order.relative_order_from_ring_generators(gens, **kwds)
   5633         
   5634 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc in relative_order_from_ring_generators(gens, check_is_integral, check_rank, is_maximal, allow_subfield)
   1640     module_gens = [to_Kabs(a) for a in gens]
   1641     n = [a.absolute_minpoly().degree() for a in gens]
-> 1642     absolute_order_module_gens = monomials(module_gens, n)
   1643 
   1644     abs_order =  absolute_order_from_module_generators(absolute_order_module_gens,

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     19         for _ in range(n[i]-1):
     20             for j in range(k):
---> 21                 v.append(v[j]*z)
     22             z *= gens[i]
     23         return v

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)
      7 
      8 def my_sigint(x, n):
----> 9     raise KeyboardInterrupt
     10 
     11 def my_sigfpe(x, n):

KeyboardInterrupt:
```



---

archive/issue_comments_035699.json:
```json
{
    "body": "The problem of the slowness of computing relative maximal orders is solved\nby the patch in #5842.  A doctest is included at line 532 of the patched\n`number_field_rel.py`",
    "created_at": "2009-04-21T08:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35699",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

The problem of the slowness of computing relative maximal orders is solved
by the patch in #5842.  A doctest is included at line 532 of the patched
`number_field_rel.py`



---

archive/issue_comments_035700.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35700",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_035701.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-21T08:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35701",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_events_010820.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4738#event-10820"
}
```



---

archive/issue_events_010821.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4738#event-10821"
}
```



---

archive/issue_events_010822.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4738#event-10822"
}
```



---

archive/issue_comments_035702.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-04-18T01:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35702",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_035703.json:
```json
{
    "body": "Do we really want the *maximal* order of the base field?  I would say the base ring should be the intersection of the relative order with the base field.  In the following example, the order *R* in *L* does not contain the maximal order of *K*:\n\n```\nsage: K.<s> = QuadraticField(5)\nsage: O = K.order(s)  # of index 2 in the maximal order of K\nsage: L.<t> = K.extension(x^2 + 1)\nsage: R = L.order((s, t))\nsage: a = (1 + s)/2\nsage: a.is_integral()\nTrue\nsage: L(a) in R  # check that R does not contain the maximal order of K\nFalse\n```\nNote the `L(a)` in the last line; this is because there is also the following bug:\n\n```\nsage: s in R\nFalse  # clearly wrong because R = ZZ[s, t] as a subring of L\n```\n\n---\nNew commits:",
    "created_at": "2014-04-18T10:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35703",
    "user": "https://github.com/pjbruin"
}
```

Do we really want the *maximal* order of the base field?  I would say the base ring should be the intersection of the relative order with the base field.  In the following example, the order *R* in *L* does not contain the maximal order of *K*:

```
sage: K.<s> = QuadraticField(5)
sage: O = K.order(s)  # of index 2 in the maximal order of K
sage: L.<t> = K.extension(x^2 + 1)
sage: R = L.order((s, t))
sage: a = (1 + s)/2
sage: a.is_integral()
True
sage: L(a) in R  # check that R does not contain the maximal order of K
False
```
Note the `L(a)` in the last line; this is because there is also the following bug:

```
sage: s in R
False  # clearly wrong because R = ZZ[s, t] as a subring of L
```

---
New commits:



---

archive/issue_comments_035704.json:
```json
{
    "body": "> Note the `L(a)` in the last line; this is because there is also the following bug:\n> \n> ```\n> sage: s in R\n> False  # clearly wrong because R = ZZ[s, t] as a subring of L\n> ```\n\nThis would probably be fixed by implementing a coercion morphism from the base order to the relative order.  However, we currently cannot construct this morphism at all:\n\n```\nsage: O.hom((R(s),))\n...\nTypeError: images do not define a valid homomorphism\n```\nThe error probably arises because `Order._is_valid_homomorphism_()` is not implemented.",
    "created_at": "2014-04-18T10:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35704",
    "user": "https://github.com/pjbruin"
}
```

> Note the `L(a)` in the last line; this is because there is also the following bug:
> 
> ```
> sage: s in R
> False  # clearly wrong because R = ZZ[s, t] as a subring of L
> ```

This would probably be fixed by implementing a coercion morphism from the base order to the relative order.  However, we currently cannot construct this morphism at all:

```
sage: O.hom((R(s),))
...
TypeError: images do not define a valid homomorphism
```
The error probably arises because `Order._is_valid_homomorphism_()` is not implemented.



---

archive/issue_comments_035705.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2014-05-03T15:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35705",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_035706.json:
```json
{
    "body": "The base ring should be either **Z** or the order intersected with the base field (which is in general not the maximal order of the base field).  We have to decide which is better.",
    "created_at": "2014-05-03T15:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35706",
    "user": "https://github.com/pjbruin"
}
```

The base ring should be either **Z** or the order intersected with the base field (which is in general not the maximal order of the base field).  We have to decide which is better.



---

archive/issue_events_010823.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4738#event-10823"
}
```



---

archive/issue_events_010824.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4738#event-10824"
}
```



---

archive/issue_events_010825.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4738#event-10825"
}
```



---

archive/issue_events_010826.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4738#event-10826"
}
```



---

archive/issue_comments_035707.json:
```json
{
    "body": "Doctest failures.",
    "created_at": "2017-03-01T11:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35707",
    "user": "https://github.com/jdemeyer"
}
```

Doctest failures.



---

archive/issue_comments_035708.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2017-03-01T11:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4738#issuecomment-35708",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_info to needs_work.
