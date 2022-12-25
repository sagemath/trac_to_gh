# Issue 3999: [with patch, needs review] Wrapper class to treat additive groups as multiplicative goups

archive/issues_003999.json:
```json
{
    "body": "Assignee: somebody\n\nThis will greatly facilitate writing generic code. \n\n\n```\n        sage: from sage.groups.multiplicative_wrapper import MultiplicativeWrapper\n\n        sage: R.<x,y> = ZZ[]\n        sage: G = MultiplicativeWrapper(R)\n        sage: a, b = G(x), G(y)\n        sage: a^2 * b^5 * a\n        (3*x + 5*y)\n        sage: a/b\n        (x - y)\n\n        sage: E = EllipticCurve('37a')\n        sage: P = E([0,0])\n        sage: G = MultiplicativeWrapper(P.parent(), repr_format=None); G\n\n        sage: a = G(P); a\n        (0 : 0 : 1)\n        sage: b = G(5*P); b\n        (1/4 : -5/8 : 1)\n        sage: a^2 * b\n        (-5/9 : 8/27 : 1)\n        sage: 7*P\n        (-5/9 : 8/27 : 1)\n        sage: 10*P == a^10\n        True\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3999\n\n",
    "created_at": "2008-08-30T11:27:57Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "[with patch, needs review] Wrapper class to treat additive groups as multiplicative goups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3999",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

This will greatly facilitate writing generic code. 


```
        sage: from sage.groups.multiplicative_wrapper import MultiplicativeWrapper

        sage: R.<x,y> = ZZ[]
        sage: G = MultiplicativeWrapper(R)
        sage: a, b = G(x), G(y)
        sage: a^2 * b^5 * a
        (3*x + 5*y)
        sage: a/b
        (x - y)

        sage: E = EllipticCurve('37a')
        sage: P = E([0,0])
        sage: G = MultiplicativeWrapper(P.parent(), repr_format=None); G

        sage: a = G(P); a
        (0 : 0 : 1)
        sage: b = G(5*P); b
        (1/4 : -5/8 : 1)
        sage: a^2 * b
        (-5/9 : 8/27 : 1)
        sage: 7*P
        (-5/9 : 8/27 : 1)
        sage: 10*P == a^10
        True

```


Issue created by migration from https://trac.sagemath.org/ticket/3999





---

archive/issue_comments_028665.json:
```json
{
    "body": "Virtually no overhead: \n\n```\nsage: from sage.groups.multiplicative_wrapper import MultiplicativeWrapper\nsage: R.<x,y> = ZZ[]\nsage: G = MultiplicativeWrapper(R)\nsage: f = R.random_element()\nsage: g = R.random_element()\nsage: timeit(\"2*f + 5*g\")\n625 loops, best of 3: 48.4 \u00b5s per loop\nsage: a = G(f)\nsage: b = G(g)\nsage: timeit(\"a^2 * b^5\")\n625 loops, best of 3: 49 \u00b5s per loop\n```\n",
    "created_at": "2008-08-30T11:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28665",
    "user": "https://github.com/robertwb"
}
```

Virtually no overhead: 

```
sage: from sage.groups.multiplicative_wrapper import MultiplicativeWrapper
sage: R.<x,y> = ZZ[]
sage: G = MultiplicativeWrapper(R)
sage: f = R.random_element()
sage: g = R.random_element()
sage: timeit("2*f + 5*g")
625 loops, best of 3: 48.4 µs per loop
sage: a = G(f)
sage: b = G(g)
sage: timeit("a^2 * b^5")
625 loops, best of 3: 49 µs per loop
```




---

archive/issue_comments_028666.json:
```json
{
    "body": "I am trying hard to see how this might actually be useful in practice.\n\nIf we had a whole implementation of additive abelian groups (as Z-modules, within the modules package) then this could be useful to allow for multiplicative abelian groups.\n\nBut in fact the whole abelian groups machinery is already multiplicative.  What I tried, and nearly succeeded doing, was to all additive notation for those.  Perhaps it would be possible to have a version of this patch which goes the other way.  But I have other things to do than learn how to do that.\n\nThis is not a negative review, just a non-review.",
    "created_at": "2008-09-02T19:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28666",
    "user": "https://github.com/JohnCremona"
}
```

I am trying hard to see how this might actually be useful in practice.

If we had a whole implementation of additive abelian groups (as Z-modules, within the modules package) then this could be useful to allow for multiplicative abelian groups.

But in fact the whole abelian groups machinery is already multiplicative.  What I tried, and nearly succeeded doing, was to all additive notation for those.  Perhaps it would be possible to have a version of this patch which goes the other way.  But I have other things to do than learn how to do that.

This is not a negative review, just a non-review.



---

archive/issue_comments_028667.json:
```json
{
    "body": "> I am trying hard to see how this might actually be useful in practice.\n\nThe first thing that comes to mind is the generic discrete log code that you wrote a while back. One then wouldn't have to use the cumbersome (and slower) op(x,y) notation for the group operations to be able to handle both additive (via the wrapper) and multiplicative groups. \n\nI had assumed the implementation of abelian groups was, at its core, additive using Z-modules and all (this seems more natural to me, as well as much more efficient). I'm not sure if this is part of the \"great abelian groups rewrite\" or not, but IMHO I think it should be. I also wrote the patch this direction because (in Sage) additive groups are all abelien (they inherit from modules), and there is a functor from them to generic non-abelien groups but not the other way around. It could also be handy in trying to (formally) implement Z[G] where G is initially presented as an additive group. \n\nTrying to add additive notation to these would be difficult, as they do not inherit from ModuleElement. Were you trying to make it so if I took elements of a multiplicative group (say, a permutation group) and did `a+b` it would instead do `a*b`. I would probably rather have it throw an error in this case. \n\nI could pretty easily write a patch going the other way if you would find it useful (though strange stuff might happen if one tries to use it on non-abelien groups, depending on the assumptions people make throughout the rest of the Sage library).",
    "created_at": "2008-09-02T23:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28667",
    "user": "https://github.com/robertwb"
}
```

> I am trying hard to see how this might actually be useful in practice.

The first thing that comes to mind is the generic discrete log code that you wrote a while back. One then wouldn't have to use the cumbersome (and slower) op(x,y) notation for the group operations to be able to handle both additive (via the wrapper) and multiplicative groups. 

I had assumed the implementation of abelian groups was, at its core, additive using Z-modules and all (this seems more natural to me, as well as much more efficient). I'm not sure if this is part of the "great abelian groups rewrite" or not, but IMHO I think it should be. I also wrote the patch this direction because (in Sage) additive groups are all abelien (they inherit from modules), and there is a functor from them to generic non-abelien groups but not the other way around. It could also be handy in trying to (formally) implement Z[G] where G is initially presented as an additive group. 

Trying to add additive notation to these would be difficult, as they do not inherit from ModuleElement. Were you trying to make it so if I took elements of a multiplicative group (say, a permutation group) and did `a+b` it would instead do `a*b`. I would probably rather have it throw an error in this case. 

I could pretty easily write a patch going the other way if you would find it useful (though strange stuff might happen if one tries to use it on non-abelien groups, depending on the assumptions people make throughout the rest of the Sage library).



---

archive/issue_comments_028668.json:
```json
{
    "body": "REFEREE REPORT:\n\nThis bitrotted.  I couldn't apply cleanly because of setup.py being refactored.  I fixed that by hand, but then this wouldn't compile:\n\n```\nwas@sage:~/build/sage-3.2.1.alpha1$ ./sage -br\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nBuilding modified file sage/groups/multiplicative_wrapper.pyx.\nExecute 1 commands (using 1 cpus)\npython2.5 `which cython` --embed-positions --incref-local-binop -I/home/was/build/sage-3.2.1.alpha1/devel/sage-main -o sage/groups/multiplicative_wrapper.c sage/groups/multiplicative_wrapper.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        except:\n            if x == 1:\n                return self.one\n            raise\n            \n    cpdef bint _has_coerce_map_from_(self, S) except -2:\n         ^\n------------------------------------------------------------\n\n/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/groups/multiplicative_wrapper.pyx:113:10: C method '_has_coerce_map_from_' not previously declared in definition part of extension type\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        cdef MultWrapperElement e = <MultWrapperElement>PY_NEW(MultWrapperElement)\n        e._parent = self._parent\n        e._elt = elt\n        return e\n\n    cdef MonoidElement _mul_c_impl(self, MonoidElement right):\n        ^\n------------------------------------------------------------\n\n/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/groups/multiplicative_wrapper.pyx:191:9: C method '_mul_c_impl' not previously declared in definition part of extension type\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        return e\n\n    cdef MonoidElement _mul_c_impl(self, MonoidElement right):\n        return self._new(self._elt._add_c((<MultWrapperElement>right)._elt))\n\n    cdef MultiplicativeGroupElement _div_c_impl(self, MultiplicativeGroupElement right):\n        ^\n------------------------------------------------------------\n\n/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/groups/multiplicative_wrapper.pyx:194:9: C method '_div_c_impl' not previously declared in definition part of extension type\nParallel build failed with status 256.\nsage: There was an error installing modified sage library code.\n```\n",
    "created_at": "2008-11-28T21:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28668",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

This bitrotted.  I couldn't apply cleanly because of setup.py being refactored.  I fixed that by hand, but then this wouldn't compile:

```
was@sage:~/build/sage-3.2.1.alpha1$ ./sage -br

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Building modified file sage/groups/multiplicative_wrapper.pyx.
Execute 1 commands (using 1 cpus)
python2.5 `which cython` --embed-positions --incref-local-binop -I/home/was/build/sage-3.2.1.alpha1/devel/sage-main -o sage/groups/multiplicative_wrapper.c sage/groups/multiplicative_wrapper.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
        except:
            if x == 1:
                return self.one
            raise
            
    cpdef bint _has_coerce_map_from_(self, S) except -2:
         ^
------------------------------------------------------------

/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/groups/multiplicative_wrapper.pyx:113:10: C method '_has_coerce_map_from_' not previously declared in definition part of extension type

Error converting Pyrex file to C:
------------------------------------------------------------
...
        cdef MultWrapperElement e = <MultWrapperElement>PY_NEW(MultWrapperElement)
        e._parent = self._parent
        e._elt = elt
        return e

    cdef MonoidElement _mul_c_impl(self, MonoidElement right):
        ^
------------------------------------------------------------

/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/groups/multiplicative_wrapper.pyx:191:9: C method '_mul_c_impl' not previously declared in definition part of extension type

Error converting Pyrex file to C:
------------------------------------------------------------
...
        return e

    cdef MonoidElement _mul_c_impl(self, MonoidElement right):
        return self._new(self._elt._add_c((<MultWrapperElement>right)._elt))

    cdef MultiplicativeGroupElement _div_c_impl(self, MultiplicativeGroupElement right):
        ^
------------------------------------------------------------

/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/groups/multiplicative_wrapper.pyx:194:9: C method '_div_c_impl' not previously declared in definition part of extension type
Parallel build failed with status 256.
sage: There was an error installing modified sage library code.
```




---

archive/issue_comments_028669.json:
```json
{
    "body": "I have made more progress in my adaptation of the existing Abelian Groups code (which uses additive representation internally, but multiplicative notation for input and output) work for additive group notation (for input and output).  I'll post a patch when I have finished doing doctests -- everything I wanted to be able to do now works, but for every single function I need to add additive examples as well as the existing multiplicative ones).\n\nFor my purposes, my patch will work fine, for example with elliptic curve groups which are naturally additive, and is preferable to what Robert has implemented here.  But it is a very different approach to the one here, which uses the coercion machinery which I am pretty sure I will never understand.",
    "created_at": "2008-12-03T20:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28669",
    "user": "https://github.com/JohnCremona"
}
```

I have made more progress in my adaptation of the existing Abelian Groups code (which uses additive representation internally, but multiplicative notation for input and output) work for additive group notation (for input and output).  I'll post a patch when I have finished doing doctests -- everything I wanted to be able to do now works, but for every single function I need to add additive examples as well as the existing multiplicative ones).

For my purposes, my patch will work fine, for example with elliptic curve groups which are naturally additive, and is preferable to what Robert has implemented here.  But it is a very different approach to the one here, which uses the coercion machinery which I am pretty sure I will never understand.



---

archive/issue_comments_028670.json:
```json
{
    "body": "The bitrot was due to #4310 and #4175, the patch has been updated. \n\nThre needs to be more doctests. \n\n\n```\nsage/groups/multiplicative_wrapper.pyx\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE sage/groups/multiplicative_wrapper.pyx: 20% (5 of 24)\n...\n```\n\n\nI'll hold off until I see John Cremona's patch. Could you post it, even if it's not done yet? I'm not sure I like the idea of `a+b` just working for any multiplicative group though. \n\nMost of my patch is not about coercion, but anyone doesn't understand how coercion is working I'm the one to blame until I at the very least put out some good documentation.",
    "created_at": "2008-12-07T10:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28670",
    "user": "https://github.com/robertwb"
}
```

The bitrot was due to #4310 and #4175, the patch has been updated. 

Thre needs to be more doctests. 


```
sage/groups/multiplicative_wrapper.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE sage/groups/multiplicative_wrapper.pyx: 20% (5 of 24)
...
```


I'll hold off until I see John Cremona's patch. Could you post it, even if it's not done yet? I'm not sure I like the idea of `a+b` just working for any multiplicative group though. 

Most of my patch is not about coercion, but anyone doesn't understand how coercion is working I'm the one to blame until I at the very least put out some good documentation.



---

archive/issue_comments_028671.json:
```json
{
    "body": "Attachment [3999-multwrap.patch](tarball://root/attachments/some-uuid/ticket3999/3999-multwrap.patch) by @robertwb created at 2008-12-07 10:44:07",
    "created_at": "2008-12-07T10:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28671",
    "user": "https://github.com/robertwb"
}
```

Attachment [3999-multwrap.patch](tarball://root/attachments/some-uuid/ticket3999/3999-multwrap.patch) by @robertwb created at 2008-12-07 10:44:07



---

archive/issue_comments_028672.json:
```json
{
    "body": "Replying to [comment:6 robertwb]:\n> The bitrot was due to #4310 and #4175, the patch has been updated. \n> \n> Thre needs to be more doctests. \n> \n> {{{\n> sage/groups/multiplicative_wrapper.pyx\n> ERROR: Please define a s == loads(dumps(s)) doctest.\n> SCORE sage/groups/multiplicative_wrapper.pyx: 20% (5 of 24)\n> ...\n> }}}\n> \n> I'll hold off until I see John Cremona's patch. Could you post it, even if it's not done yet? I'm not sure I like the idea of `a+b` just working for any multiplicative group though. \n\nOK, will do.  a+b will not work for multiplicative groups:  it will give a NotImplementedError, while a*b will work.  And vive versa if the group was created as multiplicative (which will be the old, default behaviour).\n\n> \n> Most of my patch is not about coercion, but anyone doesn't understand how coercion is working I'm the one to blame until I at the very least put out some good documentation.",
    "created_at": "2008-12-07T13:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28672",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:6 robertwb]:
> The bitrot was due to #4310 and #4175, the patch has been updated. 
> 
> Thre needs to be more doctests. 
> 
> {{{
> sage/groups/multiplicative_wrapper.pyx
> ERROR: Please define a s == loads(dumps(s)) doctest.
> SCORE sage/groups/multiplicative_wrapper.pyx: 20% (5 of 24)
> ...
> }}}
> 
> I'll hold off until I see John Cremona's patch. Could you post it, even if it's not done yet? I'm not sure I like the idea of `a+b` just working for any multiplicative group though. 

OK, will do.  a+b will not work for multiplicative groups:  it will give a NotImplementedError, while a*b will work.  And vive versa if the group was created as multiplicative (which will be the old, default behaviour).

> 
> Most of my patch is not about coercion, but anyone doesn't understand how coercion is working I'm the one to blame until I at the very least put out some good documentation.



---

archive/issue_comments_028673.json:
```json
{
    "body": "Attachment [3999-doctests.patch](tarball://root/attachments/some-uuid/ticket3999/3999-doctests.patch) by boothby created at 2009-01-23 09:00:49",
    "created_at": "2009-01-23T09:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28673",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [3999-doctests.patch](tarball://root/attachments/some-uuid/ticket3999/3999-doctests.patch) by boothby created at 2009-01-23 09:00:49



---

archive/issue_comments_028674.json:
```json
{
    "body": "Coverage at 100%.  Currently, some of the examples use Steenrod algebras, and expose some bugs in that code -- those will get fixed soon.",
    "created_at": "2009-01-23T09:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28674",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Coverage at 100%.  Currently, some of the examples use Steenrod algebras, and expose some bugs in that code -- those will get fixed soon.



---

archive/issue_comments_028675.json:
```json
{
    "body": "I have said enough on this ticket already.  None of the doctests give me a clue as to how I might ever find this useful (I don't know about Steenrod algebras), so the review should be done by someone who can appreciate that better.",
    "created_at": "2009-01-23T09:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28675",
    "user": "https://github.com/JohnCremona"
}
```

I have said enough on this ticket already.  None of the doctests give me a clue as to how I might ever find this useful (I don't know about Steenrod algebras), so the review should be done by someone who can appreciate that better.



---

archive/issue_comments_028676.json:
```json
{
    "body": "Thanks for the doctests. I don't know about Steenrod algebras either. \n\nThis would be useful, for example, if one wrote a blackbox group algorithm multiplicatively, then wanted to run it on an abelian group (such as points on an elliptic curve).",
    "created_at": "2009-01-23T10:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28676",
    "user": "https://github.com/robertwb"
}
```

Thanks for the doctests. I don't know about Steenrod algebras either. 

This would be useful, for example, if one wrote a blackbox group algorithm multiplicatively, then wanted to run it on an abelian group (such as points on an elliptic curve).



---

archive/issue_comments_028677.json:
```json
{
    "body": "Attachment [3999-fixtypo.patch](tarball://root/attachments/some-uuid/ticket3999/3999-fixtypo.patch) by boothby created at 2009-01-24 10:45:24\n\nDoctests fixed after #5064 is applied.",
    "created_at": "2009-01-24T10:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28677",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [3999-fixtypo.patch](tarball://root/attachments/some-uuid/ticket3999/3999-fixtypo.patch) by boothby created at 2009-01-24 10:45:24

Doctests fixed after #5064 is applied.



---

archive/issue_comments_028678.json:
```json
{
    "body": "Still doesn't work for me.",
    "created_at": "2009-01-24T11:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28678",
    "user": "https://trac.sagemath.org/admin/accounts/users/shumow"
}
```

Still doesn't work for me.



---

archive/issue_comments_028679.json:
```json
{
    "body": "Could you clarify what doesn't work?",
    "created_at": "2009-01-24T21:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3999#issuecomment-28679",
    "user": "https://github.com/robertwb"
}
```

Could you clarify what doesn't work?



---

archive/issue_events_009158.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3999#event-9158"
}
```



---

archive/issue_events_009159.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3999#event-9159"
}
```



---

archive/issue_events_009160.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3999#event-9160"
}
```



---

archive/issue_events_009161.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3999#event-9161"
}
```



---

archive/issue_events_009162.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3999#event-9162"
}
```



---

archive/issue_events_009163.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3999#event-9163"
}
```



---

archive/issue_events_009164.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3999",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3999#event-9164"
}
```
