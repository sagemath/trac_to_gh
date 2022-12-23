# Issue 3889: extend parameter for number field sqrt method

archive/issues_003889.json:
```json
{
    "body": "Assignee: was\n\nCC:  tscrim vdelecroix\n\nNumber field element sqrt should support the extend parameter in analogy with other sqrt functions.\n\n\n```\nsage: ZZ(4).sqrt(extend=False)\n2\nsage: CyclotomicField(4)(4).sqrt(extend=False)\n...\nTypeError: 'extend' is an invalid keyword argument for this function\n```\n\n\nIf it would even have the parameter and raise a NotImplementedError if extend==True, that would aid in writing generic code for the present.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3889\n\n",
    "created_at": "2008-08-18T13:50:47Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "extend parameter for number field sqrt method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3889",
    "user": "jbmohler"
}
```
Assignee: was

CC:  tscrim vdelecroix

Number field element sqrt should support the extend parameter in analogy with other sqrt functions.


```
sage: ZZ(4).sqrt(extend=False)
2
sage: CyclotomicField(4)(4).sqrt(extend=False)
...
TypeError: 'extend' is an invalid keyword argument for this function
```


If it would even have the parameter and raise a NotImplementedError if extend==True, that would aid in writing generic code for the present.

Issue created by migration from https://trac.sagemath.org/ticket/3889





---

archive/issue_comments_027751.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27751",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_027752.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-21T08:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27752",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_027753.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27753",
    "user": "davidloeffler"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_027754.json:
```json
{
    "body": "New commits:",
    "created_at": "2020-10-18T08:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27754",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_027755.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-10-18T08:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27755",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_027756.json:
```json
{
    "body": "green bot, please review",
    "created_at": "2020-10-18T12:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27756",
    "user": "chapoton"
}
```

green bot, please review



---

archive/issue_comments_027757.json:
```json
{
    "body": "It might be good to allow `extend` to take a string input to set the extension's variable name. Otherwise, LGTM.",
    "created_at": "2020-10-19T23:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27757",
    "user": "tscrim"
}
```

It might be good to allow `extend` to take a string input to set the extension's variable name. Otherwise, LGTM.



---

archive/issue_comments_027758.json:
```json
{
    "body": "I can see 2 places where a parameter \"name\" is used:\n\n```\nsrc/sage/rings/power_series_ring_element.pyx:    def sqrt(self, prec=None, extend=False, all=False, name=None):\nsrc/sage/rings/ring_extension_element.pyx:    def sqrt(self, extend=True, all=False, name=None):\n```\n",
    "created_at": "2020-10-20T07:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27758",
    "user": "chapoton"
}
```

I can see 2 places where a parameter "name" is used:

```
src/sage/rings/power_series_ring_element.pyx:    def sqrt(self, prec=None, extend=False, all=False, name=None):
src/sage/rings/ring_extension_element.pyx:    def sqrt(self, extend=True, all=False, name=None):
```




---

archive/issue_comments_027759.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-10-20T07:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27759",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027760.json:
```json
{
    "body": "I have added an optional parameter for the name.",
    "created_at": "2020-10-20T08:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27760",
    "user": "chapoton"
}
```

I have added an optional parameter for the name.



---

archive/issue_comments_027761.json:
```json
{
    "body": "The specicifications does not match the following behavior\n\n```\nsage: CyclotomicField(4)(2).sqrt(extend=False)\nsqrt(2)\n```\n\nOf course, this is no due to your changes, but this function is just wrong in returning symbolic ring stuff without notice.",
    "created_at": "2020-10-20T09:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27761",
    "user": "vdelecroix"
}
```

The specicifications does not match the following behavior

```
sage: CyclotomicField(4)(2).sqrt(extend=False)
sqrt(2)
```

Of course, this is no due to your changes, but this function is just wrong in returning symbolic ring stuff without notice.



---

archive/issue_comments_027762.json:
```json
{
    "body": "Et donc ? que faire ?",
    "created_at": "2020-10-20T09:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27762",
    "user": "chapoton"
}
```

Et donc ? que faire ?



---

archive/issue_comments_027763.json:
```json
{
    "body": "Replying to [comment:16 chapoton]:\n> Et donc ? que faire ?\n\nMany ways to solve it\n\n1. Do not return symbolic as one can do `SR(my_stuff).sqrt()`\n\n2. Add a `symbolic` argument\n\n3. Make `extend` a three fold alternative\n   - `extend=None`: old behavior\n   - `extend=False`: return in the current number field or raise an error\n   - `extend=True`: return in the current number field or an extended one if needed",
    "created_at": "2020-10-20T09:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27763",
    "user": "vdelecroix"
}
```

Replying to [comment:16 chapoton]:
> Et donc ? que faire ?

Many ways to solve it

1. Do not return symbolic as one can do `SR(my_stuff).sqrt()`

2. Add a `symbolic` argument

3. Make `extend` a three fold alternative
   - `extend=None`: old behavior
   - `extend=False`: return in the current number field or raise an error
   - `extend=True`: return in the current number field or an extended one if needed



---

archive/issue_comments_027764.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-10-20T11:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27764",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027765.json:
```json
{
    "body": "alors, j'ai vir\u00e9 SR (option 1)",
    "created_at": "2020-10-20T11:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27765",
    "user": "chapoton"
}
```

alors, j'ai viré SR (option 1)



---

archive/issue_comments_027766.json:
```json
{
    "body": "Tu noteras qu'il y a un probl\u00e8me de retrocompatibilit\u00e9.",
    "created_at": "2020-10-20T12:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27766",
    "user": "vdelecroix"
}
```

Tu noteras qu'il y a un problème de retrocompatibilité.



---

archive/issue_comments_027767.json:
```json
{
    "body": "alors je remets le bloc SR ?",
    "created_at": "2020-10-20T13:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27767",
    "user": "chapoton"
}
```

alors je remets le bloc SR ?



---

archive/issue_comments_027768.json:
```json
{
    "body": "Oui avec un `DeprecationWarning` disant de faire `SR(my_number_field_element).sqrt()`.",
    "created_at": "2020-10-21T16:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27768",
    "user": "vdelecroix"
}
```

Oui avec un `DeprecationWarning` disant de faire `SR(my_number_field_element).sqrt()`.



---

archive/issue_comments_027769.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-10-21T18:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27769",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027770.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-10-21T18:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27770",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027771.json:
```json
{
    "body": "Je ne comprends pas pourquoi la deprecation n'est pas d\u00e9clench\u00e9e par le doctest.",
    "created_at": "2020-10-21T18:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27771",
    "user": "chapoton"
}
```

Je ne comprends pas pourquoi la deprecation n'est pas déclenchée par le doctest.



---

archive/issue_comments_027772.json:
```json
{
    "body": "Replying to [comment:25 chapoton]:\n> Je ne comprends pas pourquoi la deprecation n'est pas d\u00e9clench\u00e9e par le doctest.\n\nhttps://trac.sagemath.org/ticket/28500",
    "created_at": "2020-10-21T19:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27772",
    "user": "vdelecroix"
}
```

Replying to [comment:25 chapoton]:
> Je ne comprends pas pourquoi la deprecation n'est pas déclenchée par le doctest.

https://trac.sagemath.org/ticket/28500



---

archive/issue_comments_027773.json:
```json
{
    "body": "ca pose de gros problemes dans src/sage/geometry/polyhedron/base.py",
    "created_at": "2020-10-25T08:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27773",
    "user": "chapoton"
}
```

ca pose de gros problemes dans src/sage/geometry/polyhedron/base.py



---

archive/issue_comments_027774.json:
```json
{
    "body": "The problem I'm having with `src/sage/geometry/polyhedron.base.py` is the following:\n\nGiven a number field `K` with specified embedding into `AA`. How do I obtain a positive square root (i.e. the parent has a specified embedding as well).\n\nIt is very unnatural if it isn't well-defined if the volume is positive or negative.",
    "created_at": "2020-10-26T08:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27774",
    "user": "@kliem"
}
```

The problem I'm having with `src/sage/geometry/polyhedron.base.py` is the following:

Given a number field `K` with specified embedding into `AA`. How do I obtain a positive square root (i.e. the parent has a specified embedding as well).

It is very unnatural if it isn't well-defined if the volume is positive or negative.



---

archive/issue_comments_027775.json:
```json
{
    "body": "Replying to [comment:28 gh-kliem]:\n> The problem I'm having with `src/sage/geometry/polyhedron.base.py` is the following:\n> \n> Given a number field `K` with specified embedding into `AA`. How do I obtain a positive square root (i.e. the parent has a specified embedding as well).\n> \n> It is very unnatural if it isn't well-defined if the volume is positive or negative.\n\nJust move the volume answer to `AA`. A number field version can easily be reconstructed\n\n```\nsage: K.<sqrt2> = QuadraticField(2, embedding=AA(2).sqrt())                                                                                                                                    \nsage: v = AA(12*sqrt2 - 15).sqrt()                                                                                                                                                             \nsage: L, vL, phi = v.as_number_field_element(minimal=True, embedded=True)                                                                                                                      \nsage: vL                                                                                                                                                                                       \n-a^3 + a^2 + 4*a + 3\nsage: vL.n()                                                                                                                                                                                   \n1.40376734129169\n```\n",
    "created_at": "2020-10-26T09:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27775",
    "user": "vdelecroix"
}
```

Replying to [comment:28 gh-kliem]:
> The problem I'm having with `src/sage/geometry/polyhedron.base.py` is the following:
> 
> Given a number field `K` with specified embedding into `AA`. How do I obtain a positive square root (i.e. the parent has a specified embedding as well).
> 
> It is very unnatural if it isn't well-defined if the volume is positive or negative.

Just move the volume answer to `AA`. A number field version can easily be reconstructed

```
sage: K.<sqrt2> = QuadraticField(2, embedding=AA(2).sqrt())                                                                                                                                    
sage: v = AA(12*sqrt2 - 15).sqrt()                                                                                                                                                             
sage: L, vL, phi = v.as_number_field_element(minimal=True, embedded=True)                                                                                                                      
sage: vL                                                                                                                                                                                       
-a^3 + a^2 + 4*a + 3
sage: vL.n()                                                                                                                                                                                   
1.40376734129169
```




---

archive/issue_comments_027776.json:
```json
{
    "body": "This works for the volume of polyhedra now.\n\nI did change the behaviour. The new default `None` is deprecated now and `extend=False` raises a `ValueError` to be consistent with other rings. The new default should then be `extend=True` once we remove the deprecation warning.\n\nThe `QR` method of method of matrices does not raise correctly a `TypeError`, if the base ring does not support the required roots. (Before it would sometimes implicitly extend even though the documentation tells us that the base ring must support roots.)\n----\nNew commits:",
    "created_at": "2020-10-26T11:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27776",
    "user": "@kliem"
}
```

This works for the volume of polyhedra now.

I did change the behaviour. The new default `None` is deprecated now and `extend=False` raises a `ValueError` to be consistent with other rings. The new default should then be `extend=True` once we remove the deprecation warning.

The `QR` method of method of matrices does not raise correctly a `TypeError`, if the base ring does not support the required roots. (Before it would sometimes implicitly extend even though the documentation tells us that the base ring must support roots.)
----
New commits:



---

archive/issue_comments_027777.json:
```json
{
    "body": "The doctest testing the deprecation warning still does not work.",
    "created_at": "2020-10-26T11:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27777",
    "user": "@kliem"
}
```

The doctest testing the deprecation warning still does not work.



---

archive/issue_comments_027778.json:
```json
{
    "body": "Having a deprecated default is the worse that can be!",
    "created_at": "2020-10-26T11:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27778",
    "user": "vdelecroix"
}
```

Having a deprecated default is the worse that can be!



---

archive/issue_comments_027779.json:
```json
{
    "body": "How else can you tell users that they should think about what they really want?",
    "created_at": "2020-10-26T11:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27779",
    "user": "@kliem"
}
```

How else can you tell users that they should think about what they really want?



---

archive/issue_comments_027780.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-10-26T11:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27780",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027781.json:
```json
{
    "body": "`extend=False` should just throw an error (if extension is needed) and don't do something weird like changing to symbolic ring.\n\nTo do `elt.sqrt(extend=False)` is correct behaviour and it should just raise and error, like with other rings. Also `extend=False` is a bad default, because it is not the default for `functions.other.sqrt`.\n\nThe idea of this default deprecation message is that users code needs to be updated and this is how you notify them, isn't it?",
    "created_at": "2020-10-26T11:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27781",
    "user": "@kliem"
}
```

`extend=False` should just throw an error (if extension is needed) and don't do something weird like changing to symbolic ring.

To do `elt.sqrt(extend=False)` is correct behaviour and it should just raise and error, like with other rings. Also `extend=False` is a bad default, because it is not the default for `functions.other.sqrt`.

The idea of this default deprecation message is that users code needs to be updated and this is how you notify them, isn't it?



---

archive/issue_comments_027782.json:
```json
{
    "body": "Then again we could just not do a deprecation warning at all and change the default to `extend=True`.\n\nThis is what it boils down to for `functions.other.sqrt` anyway.",
    "created_at": "2020-10-26T12:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27782",
    "user": "@kliem"
}
```

Then again we could just not do a deprecation warning at all and change the default to `extend=True`.

This is what it boils down to for `functions.other.sqrt` anyway.



---

archive/issue_comments_027783.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-10-26T12:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27783",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027784.json:
```json
{
    "body": "I removed the deprecation warning. The main problem is that `functions.other.sqrt` calls the method `sqrt` without optional arguments and claims that the default is to extend.\n\nIn this way it requires:\n- that any `sqrt` method must extend by default without deprecation warning etc,\n- any `sqrt` method does have an `extend` argument.\n\nIf we want to keep the deprecation message we need to alter `functions.other.sqrt`.\n\nFeel free to reject my changes alltogether or change anything you like. I just joined in because there was trouble with polyhedra.",
    "created_at": "2020-10-26T12:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27784",
    "user": "@kliem"
}
```

I removed the deprecation warning. The main problem is that `functions.other.sqrt` calls the method `sqrt` without optional arguments and claims that the default is to extend.

In this way it requires:
- that any `sqrt` method must extend by default without deprecation warning etc,
- any `sqrt` method does have an `extend` argument.

If we want to keep the deprecation message we need to alter `functions.other.sqrt`.

Feel free to reject my changes alltogether or change anything you like. I just joined in because there was trouble with polyhedra.



---

archive/issue_comments_027785.json:
```json
{
    "body": "There is still one failing doctest, see patchbot report",
    "created_at": "2020-10-27T17:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27785",
    "user": "chapoton"
}
```

There is still one failing doctest, see patchbot report



---

archive/issue_comments_027786.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-10-27T22:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27786",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027787.json:
```json
{
    "body": "I am not sure what this `sqrt` method is trying to achieve. Giving an answer is not a necessity. Especially if the answer is \"the square root of your number\". Currently, I find that only the `extend=False` looks reasonable.\n\nI see several problems\n- `QQ` is a particular case of number fields, and `ZZ` is a particular case of `QQ`. For both `ZZ` and `QQ` the behavior of `sqrt` should be compatible with what is proposed for number fields.\n- The proposal is not compatible with embeddings. Many users would expect `K(2).sqrt() + K(3).sqrt()` to work. Especially with `K=QQ`.",
    "created_at": "2020-10-28T07:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27787",
    "user": "vdelecroix"
}
```

I am not sure what this `sqrt` method is trying to achieve. Giving an answer is not a necessity. Especially if the answer is "the square root of your number". Currently, I find that only the `extend=False` looks reasonable.

I see several problems
- `QQ` is a particular case of number fields, and `ZZ` is a particular case of `QQ`. For both `ZZ` and `QQ` the behavior of `sqrt` should be compatible with what is proposed for number fields.
- The proposal is not compatible with embeddings. Many users would expect `K(2).sqrt() + K(3).sqrt()` to work. Especially with `K=QQ`.



---

archive/issue_comments_027788.json:
```json
{
    "body": "I tried to make the behavior consistent, this is why I changed the default to `extend=True`.\n\nBut I see the problem that `ZZ` and `QQ` still choose symbolic expressions instead. Should we change them all or just leave it at symbolic expressions? (The polyhedron problem is still solved by this, because by the `extend=False` option, you can stabely raise an error.)\n\nCompatibily of embeddings can be achieved, at least when `all=False`: If `K` has a specified complex embedding, we just use this to specify an ambedding of the extension. In case `K` is `QQ` we just go with `AA`. This way `K(2).sqrt() + K(3).sqrt()` would still work, at least when `K` has a specified complex embedding that contains both `K(2).sqrt()` and `K(3).sqrt()`.",
    "created_at": "2020-10-28T08:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27788",
    "user": "@kliem"
}
```

I tried to make the behavior consistent, this is why I changed the default to `extend=True`.

But I see the problem that `ZZ` and `QQ` still choose symbolic expressions instead. Should we change them all or just leave it at symbolic expressions? (The polyhedron problem is still solved by this, because by the `extend=False` option, you can stabely raise an error.)

Compatibily of embeddings can be achieved, at least when `all=False`: If `K` has a specified complex embedding, we just use this to specify an ambedding of the extension. In case `K` is `QQ` we just go with `AA`. This way `K(2).sqrt() + K(3).sqrt()` would still work, at least when `K` has a specified complex embedding that contains both `K(2).sqrt()` and `K(3).sqrt()`.



---

archive/issue_comments_027789.json:
```json
{
    "body": "So I agree that it should be consistent. However, there will be a backwards incompatibility issue to deal with if we make this change. At least with the current change, there is at least a type distinction that can be employed to justify the difference. If we do make a change for `ZZ` and `QQ`, then we should only do it once as it will likely be a bit painful for users expecting it in `SR`. That is my 2 cents.",
    "created_at": "2020-11-01T23:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27789",
    "user": "tscrim"
}
```

So I agree that it should be consistent. However, there will be a backwards incompatibility issue to deal with if we make this change. At least with the current change, there is at least a type distinction that can be employed to justify the difference. If we do make a change for `ZZ` and `QQ`, then we should only do it once as it will likely be a bit painful for users expecting it in `SR`. That is my 2 cents.



---

archive/issue_comments_027790.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2021-01-11T09:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27790",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027791.json:
```json
{
    "body": "Ok. This should now behave consistenly with `ZZ` and `QQ`.\nIf `self` is a square, just return the root.\nIf `self` is not a square, raise an error if `extend=False` and use symbolic ring if `extend=True` (default).\n\nOf course one could argue, that this behavior isn't optimal and there are better choices for a square root construction (e.g. extend the number field), but it is really hard to guess what the user wants precisely (e.g. for polytopes volume, if we need to extend anyway, we might as well go to `AA`).",
    "created_at": "2021-01-11T09:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27791",
    "user": "@kliem"
}
```

Ok. This should now behave consistenly with `ZZ` and `QQ`.
If `self` is a square, just return the root.
If `self` is not a square, raise an error if `extend=False` and use symbolic ring if `extend=True` (default).

Of course one could argue, that this behavior isn't optimal and there are better choices for a square root construction (e.g. extend the number field), but it is really hard to guess what the user wants precisely (e.g. for polytopes volume, if we need to extend anyway, we might as well go to `AA`).



---

archive/issue_comments_027792.json:
```json
{
    "body": "I am a little worried about this change:\n\n```diff\ndiff --git a/src/sage/matrix/matrix2.pyx b/src/sage/matrix/matrix2.pyx\nindex 5e190ea..7ce4196 100644\n--- a/src/sage/matrix/matrix2.pyx\n+++ b/src/sage/matrix/matrix2.pyx\n@@ -10136,7 +10136,7 @@ cdef class Matrix(Matrix1):\n             hip = v.hermitian_inner_product(v)\n             if hip != 0:\n                 try:\n-                    scale = sqrt(hip)\n+                    scale = sqrt(hip, extend=False)\n                     q = (1/scale)*v\n                     Q.append(q)\n                     R[row,i] = scale\n```\n\nSince this can take in general rings, such as one whose elements could have a `sqrt` that does not take `extend` as a parameter, this could behave differently than before. How would you classify this behavior? A bug in the `sqrt` implementation? Or am I just being paranoid about this?",
    "created_at": "2021-01-12T00:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27792",
    "user": "tscrim"
}
```

I am a little worried about this change:

```diff
diff --git a/src/sage/matrix/matrix2.pyx b/src/sage/matrix/matrix2.pyx
index 5e190ea..7ce4196 100644
--- a/src/sage/matrix/matrix2.pyx
+++ b/src/sage/matrix/matrix2.pyx
@@ -10136,7 +10136,7 @@ cdef class Matrix(Matrix1):
             hip = v.hermitian_inner_product(v)
             if hip != 0:
                 try:
-                    scale = sqrt(hip)
+                    scale = sqrt(hip, extend=False)
                     q = (1/scale)*v
                     Q.append(q)
                     R[row,i] = scale
```

Since this can take in general rings, such as one whose elements could have a `sqrt` that does not take `extend` as a parameter, this could behave differently than before. How would you classify this behavior? A bug in the `sqrt` implementation? Or am I just being paranoid about this?



---

archive/issue_comments_027793.json:
```json
{
    "body": "Yes, I agree, there is a number of rings that don't have this keyword.",
    "created_at": "2021-01-12T08:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27793",
    "user": "@kliem"
}
```

Yes, I agree, there is a number of rings that don't have this keyword.



---

archive/issue_comments_027794.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2021-01-12T08:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27794",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027795.json:
```json
{
    "body": "Reading closely, the documentation of `QR` does not claim that the base ring is preserved. In particular it mentions that it is not preserved, when the base ring is not a field. It just mentions that the base ring must have have roots. In that way, I guess that `QQ` has roots in sage (just not preserving the ring).\n\nThe change in `QR` was required, because of some design decision that I reverted already.",
    "created_at": "2021-01-12T08:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27795",
    "user": "@kliem"
}
```

Reading closely, the documentation of `QR` does not claim that the base ring is preserved. In particular it mentions that it is not preserved, when the base ring is not a field. It just mentions that the base ring must have have roots. In that way, I guess that `QQ` has roots in sage (just not preserving the ring).

The change in `QR` was required, because of some design decision that I reverted already.



---

archive/issue_comments_027796.json:
```json
{
    "body": "I am ready to set a positive review. Vincent, any additional comments or things to address before I do so?",
    "created_at": "2021-01-14T05:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27796",
    "user": "tscrim"
}
```

I am ready to set a positive review. Vincent, any additional comments or things to address before I do so?



---

archive/issue_comments_027797.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-01-14T10:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27797",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_027798.json:
```json
{
    "body": "Nothing to add. Thanks.",
    "created_at": "2021-01-14T10:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27798",
    "user": "vdelecroix"
}
```

Nothing to add. Thanks.



---

archive/issue_comments_027799.json:
```json
{
    "body": "Thank you.",
    "created_at": "2021-01-14T10:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27799",
    "user": "@kliem"
}
```

Thank you.



---

archive/issue_comments_027800.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2021-01-24T10:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3889#issuecomment-27800",
    "user": "vbraun"
}
```

Resolution: fixed
