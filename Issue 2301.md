# Issue 2301: Bug in sage_flattened_str_list

archive/issues_002301.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @williamstein\n\nKeywords: ringlist, sage_structured_str_list\n\nWhen playing around with `ringlist`, i found a bug the method `sage_structured_str_list`:\n\n\n```\nsage: R=singular.ring(0,'(x1,x12,x2)','dp')\nsage: RL=R.ringlist()\nsage: RL\n\n[1]:\n   0\n[2]:\n   [1]:\n      x1\n   [2]:\n      x12\n   [3]:\n      x2\n[3]:\n   [1]:\n      [1]:\n         dp\n      [2]:\n         1,1,1\n   [2]:\n      [1]:\n         C\n      [2]:\n         0\n[4]:\n   _[1]=0\nsage: RL.sage_structured_str_list()\n[[], [], [], [], [], [], [], [], [], [], [], [], ['0']]\nsage: RL.sage_flattened_str_list()\n['0', 'x1', 'x12', 'x2', 'dp', '1,1,1', 'C', '0', '_[1]=0']\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2301\n\n",
    "created_at": "2008-02-25T11:19:35Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Bug in sage_flattened_str_list",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2301",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @malb

CC:  @williamstein

Keywords: ringlist, sage_structured_str_list

When playing around with `ringlist`, i found a bug the method `sage_structured_str_list`:


```
sage: R=singular.ring(0,'(x1,x12,x2)','dp')
sage: RL=R.ringlist()
sage: RL

[1]:
   0
[2]:
   [1]:
      x1
   [2]:
      x12
   [3]:
      x2
[3]:
   [1]:
      [1]:
         dp
      [2]:
         1,1,1
   [2]:
      [1]:
         C
      [2]:
         0
[4]:
   _[1]=0
sage: RL.sage_structured_str_list()
[[], [], [], [], [], [], [], [], [], [], [], [], ['0']]
sage: RL.sage_flattened_str_list()
['0', 'x1', 'x12', 'x2', 'dp', '1,1,1', 'C', '0', '_[1]=0']
```



Issue created by migration from https://trac.sagemath.org/ticket/2301





---

archive/issue_comments_015246.json:
```json
{
    "body": "Changing component from commutative algebra to interfaces.",
    "created_at": "2008-02-25T11:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15246",
    "user": "https://github.com/malb"
}
```

Changing component from commutative algebra to interfaces.



---

archive/issue_comments_015247.json:
```json
{
    "body": "Changing assignee from @malb to @williamstein.",
    "created_at": "2008-02-25T11:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15247",
    "user": "https://github.com/malb"
}
```

Changing assignee from @malb to @williamstein.



---

archive/issue_comments_015248.json:
```json
{
    "body": "Sorry, the bug is in sage_**structured**_str_list, rather than in ..._flattened_...",
    "created_at": "2008-02-26T07:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15248",
    "user": "https://github.com/simon-king-jena"
}
```

Sorry, the bug is in sage_**structured**_str_list, rather than in ..._flattened_...



---

archive/issue_comments_015249.json:
```json
{
    "body": "With the attached patch, the following works:\n\n```\nsage: R=singular.ring(0,'(x,y)','dp')\nsage: R.ringlist().sage_structured_str_list()\n['0', ['x', 'y'], [['dp', '1,\\n1 '], ['C', '0 ']], '0']\nsage: R.ringlist().sage_flattened_str_list()\n['0', 'x', 'y', 'dp', '1,1', 'C', '0', '_[1]=0']\n```\n\n\nThe suggested algorithm is recursive, and it is easy to see that if `L` is a singular list of (singular lists of (...)) then `L.sage_structured_list()` returns a sage list of lists mimicking `L`'s structure, so that any non-list component of `L` is represented as a string.\n\nThe following might be a disadvantage:\n* If `L` is very (i mean: **very**) deeply nested, there might be trouble with the recursion limit.\n* The example shows that `sage_flattened_str_list` and my suggestion for `sage_structured_str_list` are based on different string representations of the list components. E.g., in the example, the last component is a 0-ideal. Printing a 0-ideal yields the string `'0'` (see above in `sage_structured_str_list`), but if the 0-ideal is part of a list then printing the list would represent the 0-ideal in the form `'_[0]=0'` (see above in `sage_flattened_str_list`). Similarly, an `intvec` would be represented in two different ways.\n\nIt may be a matter of taste whether the first or second string representation is preferred, and i think it would not be difficult to achieve the other representation. Opinions?",
    "created_at": "2008-02-26T08:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15249",
    "user": "https://github.com/simon-king-jena"
}
```

With the attached patch, the following works:

```
sage: R=singular.ring(0,'(x,y)','dp')
sage: R.ringlist().sage_structured_str_list()
['0', ['x', 'y'], [['dp', '1,\n1 '], ['C', '0 ']], '0']
sage: R.ringlist().sage_flattened_str_list()
['0', 'x', 'y', 'dp', '1,1', 'C', '0', '_[1]=0']
```


The suggested algorithm is recursive, and it is easy to see that if `L` is a singular list of (singular lists of (...)) then `L.sage_structured_list()` returns a sage list of lists mimicking `L`'s structure, so that any non-list component of `L` is represented as a string.

The following might be a disadvantage:
* If `L` is very (i mean: **very**) deeply nested, there might be trouble with the recursion limit.
* The example shows that `sage_flattened_str_list` and my suggestion for `sage_structured_str_list` are based on different string representations of the list components. E.g., in the example, the last component is a 0-ideal. Printing a 0-ideal yields the string `'0'` (see above in `sage_structured_str_list`), but if the 0-ideal is part of a list then printing the list would represent the 0-ideal in the form `'_[0]=0'` (see above in `sage_flattened_str_list`). Similarly, an `intvec` would be represented in two different ways.

It may be a matter of taste whether the first or second string representation is preferred, and i think it would not be difficult to achieve the other representation. Opinions?



---

archive/issue_comments_015250.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n> It may be a matter of taste whether the first or second string representation is preferred, and i think it would not be difficult to achieve the other representation. \n\nHere is how to obtain the other representation: In the patch, replace `return str(self)` by `return '\\n'.join(x.strip() for x in self.list().__str__().split('\\n')[1:])`",
    "created_at": "2008-02-26T09:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15250",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:3 SimonKing]:
> It may be a matter of taste whether the first or second string representation is preferred, and i think it would not be difficult to achieve the other representation. 

Here is how to obtain the other representation: In the patch, replace `return str(self)` by `return '\n'.join(x.strip() for x in self.list().__str__().split('\n')[1:])`



---

archive/issue_comments_015251.json:
```json
{
    "body": "> The following might be a disadvantage:\n>  * If `L` is very (i mean: **very**) deeply nested, there might be trouble with the recursion limit.\n\nI don't think that this would be an issue in practice.\n\n>  * The example shows that `sage_flattened_str_list` and my suggestion for `sage_structured_str_list` are based on different string representations of the list components. E.g., in the example, the last component is a 0-ideal. Printing a 0-ideal yields the string `'0'` (see above in `sage_structured_str_list`), but if the 0-ideal is part of a list then printing the list would represent the 0-ideal in the form `'_[0]=0'` (see above in `sage_flattened_str_list`). Similarly, an `intvec` would be represented in two different ways.\n\nI don't like the second representation because it doesn't look like valid Singular outside a list? But if that is the format Singular accepts when we play the list of lists back to it then we should go for this representation.",
    "created_at": "2008-02-26T09:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15251",
    "user": "https://github.com/malb"
}
```

> The following might be a disadvantage:
>  * If `L` is very (i mean: **very**) deeply nested, there might be trouble with the recursion limit.

I don't think that this would be an issue in practice.

>  * The example shows that `sage_flattened_str_list` and my suggestion for `sage_structured_str_list` are based on different string representations of the list components. E.g., in the example, the last component is a 0-ideal. Printing a 0-ideal yields the string `'0'` (see above in `sage_structured_str_list`), but if the 0-ideal is part of a list then printing the list would represent the 0-ideal in the form `'_[0]=0'` (see above in `sage_flattened_str_list`). Similarly, an `intvec` would be represented in two different ways.

I don't like the second representation because it doesn't look like valid Singular outside a list? But if that is the format Singular accepts when we play the list of lists back to it then we should go for this representation.



---

archive/issue_comments_015252.json:
```json
{
    "body": "Replying to [comment:5 malb]:\n> >  * The example shows that `sage_flattened_str_list` and my suggestion for `sage_structured_str_list` are based on different string representations of the list components. E.g., in the example, the last component is a 0-ideal. Printing a 0-ideal yields the string `'0'` (see above in `sage_structured_str_list`), but if the 0-ideal is part of a list then printing the list would represent the 0-ideal in the form `'_[0]=0'` (see above in `sage_flattened_str_list`). Similarly, an `intvec` would be represented in two different ways.\n> \n> I don't like the second representation because it doesn't look like valid Singular outside a list? But if that is the format Singular accepts when we play the list of lists back to it then we should go for this representation.\n\n**Both** represantations can not be played back. \n\nExample 1: The first version of representing `intvec(1,1)` is `'1,\\n1'` -- but `singular('1,\\n1')` results in hanging up. The second version would represent `intvec(1,1)` as `'1,1'` -- but `singular('1,1')` is a list and not an intvec. \n\nExample 2: `singular.ideal('x','y')` would either be represented by `'x,\\ny'` (first version) or by `'_[1]=x\\n_[2]=y'` (second version). Both is not valid for `singular(...)`.\n\nSo i think it is really just a matter of taste. To return strings that can be used for defining the represented objects would involve much more work, unless there is a simple Singular command that provides such string. Do you know any?",
    "created_at": "2008-02-26T10:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15252",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:5 malb]:
> >  * The example shows that `sage_flattened_str_list` and my suggestion for `sage_structured_str_list` are based on different string representations of the list components. E.g., in the example, the last component is a 0-ideal. Printing a 0-ideal yields the string `'0'` (see above in `sage_structured_str_list`), but if the 0-ideal is part of a list then printing the list would represent the 0-ideal in the form `'_[0]=0'` (see above in `sage_flattened_str_list`). Similarly, an `intvec` would be represented in two different ways.
> 
> I don't like the second representation because it doesn't look like valid Singular outside a list? But if that is the format Singular accepts when we play the list of lists back to it then we should go for this representation.

**Both** represantations can not be played back. 

Example 1: The first version of representing `intvec(1,1)` is `'1,\n1'` -- but `singular('1,\n1')` results in hanging up. The second version would represent `intvec(1,1)` as `'1,1'` -- but `singular('1,1')` is a list and not an intvec. 

Example 2: `singular.ideal('x','y')` would either be represented by `'x,\ny'` (first version) or by `'_[1]=x\n_[2]=y'` (second version). Both is not valid for `singular(...)`.

So i think it is really just a matter of taste. To return strings that can be used for defining the represented objects would involve much more work, unless there is a simple Singular command that provides such string. Do you know any?



---

archive/issue_comments_015253.json:
```json
{
    "body": "> **Both** represantations can not be played back. \n> \n> Example 1: The first version of representing `intvec(1,1)` is `'1,\\n1'` -- but `singular('1,\\n1')` results in hanging up. The second version would represent `intvec(1,1)` as `'1,1'` -- but `singular('1,1')` is a list and not an intvec. \n> \n> Example 2: `singular.ideal('x','y')` would either be represented by `'x,\\ny'` (first version) or by `'_[1]=x\\n_[2]=y'` (second version). Both is not valid for `singular(...)`.\n> \n> So i think it is really just a matter of taste. To return strings that can be used for defining the represented objects would involve much more work, unless there is a simple Singular command that provides such string. Do you know any?\n\nUnfortunately I don't know such a function. But I see the point that it is a matter of taste. However, I still prefer the first option because `_[1] = 0` depends on the index of the list ([1]) while just `0` doesn't.",
    "created_at": "2008-02-26T11:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15253",
    "user": "https://github.com/malb"
}
```

> **Both** represantations can not be played back. 
> 
> Example 1: The first version of representing `intvec(1,1)` is `'1,\n1'` -- but `singular('1,\n1')` results in hanging up. The second version would represent `intvec(1,1)` as `'1,1'` -- but `singular('1,1')` is a list and not an intvec. 
> 
> Example 2: `singular.ideal('x','y')` would either be represented by `'x,\ny'` (first version) or by `'_[1]=x\n_[2]=y'` (second version). Both is not valid for `singular(...)`.
> 
> So i think it is really just a matter of taste. To return strings that can be used for defining the represented objects would involve much more work, unless there is a simple Singular command that provides such string. Do you know any?

Unfortunately I don't know such a function. But I see the point that it is a matter of taste. However, I still prefer the first option because `_[1] = 0` depends on the index of the list ([1]) while just `0` doesn't.



---

archive/issue_comments_015254.json:
```json
{
    "body": "**Referee Report**:\n* Could you add doctests to `sage_structured_str_list` like the examples in the description of the ticket?\n* Does `make test` still pass after the change? In particular does `sage -t schemes/plane_curves/projective_curve.py` still pass? This seems to be the only place this method is called.",
    "created_at": "2008-02-26T11:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15254",
    "user": "https://github.com/malb"
}
```

**Referee Report**:
* Could you add doctests to `sage_structured_str_list` like the examples in the description of the ticket?
* Does `make test` still pass after the change? In particular does `sage -t schemes/plane_curves/projective_curve.py` still pass? This seems to be the only place this method is called.



---

archive/issue_comments_015255.json:
```json
{
    "body": "Attachment [sage_structured_str_list.patch](tarball://root/attachments/some-uuid/ticket2301/sage_structured_str_list.patch) by @simon-king-jena created at 2008-02-26 23:55:39\n\nReplying to [comment:8 malb]:\n> **Referee Report**:\n>  * Could you add doctests to `sage_structured_str_list` like the examples in the description of the ticket?\n\nDone.\n\n>  * Does `make test` still pass after the change? In particular does `sage -t schemes/plane_curves/projective_curve.py` still pass? This seems to be the only place this method is called.\n\nI'm afraid this test fails.\n\nBut i believe the function `riemann_roch_basis` only works because it expects a behaviour of `sage_structured_str_list` *that does not fit to its specification*.\n\nTo be precise: Taking the example of `riemann_roch_basis`, the function internally computes `LG = G.BrillNoether(X2)`, which is printed as\n\n```\n[1]:\n   _[1]=x\n   _[2]=y\n[2]:\n   _[1]=1\n   _[2]=1\n[3]:\n   _[1]=z\n   _[2]=y\n[4]:\n   _[1]=z^2\n   _[2]=y^2\n[5]:\n   _[1]=z\n   _[2]=x\n[6]:\n   _[1]=z^2\n   _[2]=x*y\n```\n\n\nThen, `sage_structured_str_list` is applied to this thing, and yields\n\n```\n[['x', 'y'], ['1', '1'], ['z', 'y'], ['z^2', 'y^2'], ['z', 'x'], ['z^2', 'x*y']]\n```\n\n\nI believe this output is wrong, since `LG[1]` is not a singular list, hence, must be represented as a string and not as a sage list.\n\nI see two ways to resolve it:\n\n1. Change `riemann_roch_basis`, since it relies on getting a *wrong* answer from `sage_structured_str_list`\n\n2. Change `sage_structured_str_list` so that not only singular lists are turned into a sage list, but also singular ideals and intvecs are turned into lists.\n\nI prefer the first option, since the second option clearly violates the specification of `sage_structured_str_list`.\n\nAnyway, i think we will only be able to fix the bug later.",
    "created_at": "2008-02-26T23:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15255",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [sage_structured_str_list.patch](tarball://root/attachments/some-uuid/ticket2301/sage_structured_str_list.patch) by @simon-king-jena created at 2008-02-26 23:55:39

Replying to [comment:8 malb]:
> **Referee Report**:
>  * Could you add doctests to `sage_structured_str_list` like the examples in the description of the ticket?

Done.

>  * Does `make test` still pass after the change? In particular does `sage -t schemes/plane_curves/projective_curve.py` still pass? This seems to be the only place this method is called.

I'm afraid this test fails.

But i believe the function `riemann_roch_basis` only works because it expects a behaviour of `sage_structured_str_list` *that does not fit to its specification*.

To be precise: Taking the example of `riemann_roch_basis`, the function internally computes `LG = G.BrillNoether(X2)`, which is printed as

```
[1]:
   _[1]=x
   _[2]=y
[2]:
   _[1]=1
   _[2]=1
[3]:
   _[1]=z
   _[2]=y
[4]:
   _[1]=z^2
   _[2]=y^2
[5]:
   _[1]=z
   _[2]=x
[6]:
   _[1]=z^2
   _[2]=x*y
```


Then, `sage_structured_str_list` is applied to this thing, and yields

```
[['x', 'y'], ['1', '1'], ['z', 'y'], ['z^2', 'y^2'], ['z', 'x'], ['z^2', 'x*y']]
```


I believe this output is wrong, since `LG[1]` is not a singular list, hence, must be represented as a string and not as a sage list.

I see two ways to resolve it:

1. Change `riemann_roch_basis`, since it relies on getting a *wrong* answer from `sage_structured_str_list`

2. Change `sage_structured_str_list` so that not only singular lists are turned into a sage list, but also singular ideals and intvecs are turned into lists.

I prefer the first option, since the second option clearly violates the specification of `sage_structured_str_list`.

Anyway, i think we will only be able to fix the bug later.



---

archive/issue_comments_015256.json:
```json
{
    "body": "> 1. Change `riemann_roch_basis`, since it relies on getting a *wrong* answer from `sage_structured_str_list`\n> \n> 2. Change `sage_structured_str_list` so that not only singular lists are turned into a sage list, but also singular ideals and intvecs are turned into lists.\n> \n> I prefer the first option, since the second option clearly violates the specification of `sage_structured_str_list`.\n\nThis seems reasonable, however we should contact the original author (I don't know this area of the code). I assume it is William whom I hereby CC.\n \n> Anyway, i think we will only be able to fix the bug later.\n\nUntil we have figured this one out I think we shouldn't merge the patch. However, this seems to be something that can be resolved quickly.",
    "created_at": "2008-02-27T00:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15256",
    "user": "https://github.com/malb"
}
```

> 1. Change `riemann_roch_basis`, since it relies on getting a *wrong* answer from `sage_structured_str_list`
> 
> 2. Change `sage_structured_str_list` so that not only singular lists are turned into a sage list, but also singular ideals and intvecs are turned into lists.
> 
> I prefer the first option, since the second option clearly violates the specification of `sage_structured_str_list`.

This seems reasonable, however we should contact the original author (I don't know this area of the code). I assume it is William whom I hereby CC.
 
> Anyway, i think we will only be able to fix the bug later.

Until we have figured this one out I think we shouldn't merge the patch. However, this seems to be something that can be resolved quickly.



---

archive/issue_comments_015257.json:
```json
{
    "body": "Attachment [sage_structured_str_list.2.patch](tarball://root/attachments/some-uuid/ticket2301/sage_structured_str_list.2.patch) by @simon-king-jena created at 2008-02-27 08:54:20",
    "created_at": "2008-02-27T08:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15257",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [sage_structured_str_list.2.patch](tarball://root/attachments/some-uuid/ticket2301/sage_structured_str_list.2.patch) by @simon-king-jena created at 2008-02-27 08:54:20



---

archive/issue_comments_015258.json:
```json
{
    "body": "Attachment [riemann_roch_basis.2.patch](tarball://root/attachments/some-uuid/ticket2301/riemann_roch_basis.2.patch) by @simon-king-jena created at 2008-02-27 08:55:03",
    "created_at": "2008-02-27T08:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15258",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [riemann_roch_basis.2.patch](tarball://root/attachments/some-uuid/ticket2301/riemann_roch_basis.2.patch) by @simon-king-jena created at 2008-02-27 08:55:03



---

archive/issue_comments_015259.json:
```json
{
    "body": "Replying to [comment:10 malb]:\n> > Anyway, i think we will only be able to fix the bug later.\n> \n> Until we have figured this one out I think we shouldn't merge the patch. However, this seems to be something that can be resolved quickly.\n\nI think i did fix it.\n\nFirst of all, the patch for `sage_structured_str_list` should be replaced by patch number 2, because in the first patch i had a mistake in the doctest.\n\nThen, i attached a patch for `riemann_roch_basis`. The point is that internally `riemann_roch_basis` computes something that apparently is known to be a list of ideals with two generators. We know how these are dealt with by the new version of `sage_structured_str_list`. Hence, changing one line of `riemann_roch_basis` suffices.\n\nOops, i just see that i attached the patch twice...\n\nAnyway. With the patches `sage_structured_str_list2.patch` and with either patch for `riemann_roch_basis`, all doc tests for `singular.py` and for `projective_curve.py` pass.\n\nMoreover, i can not find any other place where `sage_structured_str_list` or `riemann_roch_basis` are used.",
    "created_at": "2008-02-27T09:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15259",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:10 malb]:
> > Anyway, i think we will only be able to fix the bug later.
> 
> Until we have figured this one out I think we shouldn't merge the patch. However, this seems to be something that can be resolved quickly.

I think i did fix it.

First of all, the patch for `sage_structured_str_list` should be replaced by patch number 2, because in the first patch i had a mistake in the doctest.

Then, i attached a patch for `riemann_roch_basis`. The point is that internally `riemann_roch_basis` computes something that apparently is known to be a list of ideals with two generators. We know how these are dealt with by the new version of `sage_structured_str_list`. Hence, changing one line of `riemann_roch_basis` suffices.

Oops, i just see that i attached the patch twice...

Anyway. With the patches `sage_structured_str_list2.patch` and with either patch for `riemann_roch_basis`, all doc tests for `singular.py` and for `projective_curve.py` pass.

Moreover, i can not find any other place where `sage_structured_str_list` or `riemann_roch_basis` are used.



---

archive/issue_comments_015260.json:
```json
{
    "body": "Replying to [comment:7 malb]:\n> Unfortunately I don't know such a function. But I see the point that it is a matter of taste. However, I still prefer the first option because `_[1] = 0` depends on the index of the list ([1]) while just `0` doesn't.\n\nAnd, by the way, i prefer the first option as well, and the patches work accordingly.",
    "created_at": "2008-02-27T09:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15260",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:7 malb]:
> Unfortunately I don't know such a function. But I see the point that it is a matter of taste. However, I still prefer the first option because `_[1] = 0` depends on the index of the list ([1]) while just `0` doesn't.

And, by the way, i prefer the first option as well, and the patches work accordingly.



---

archive/issue_comments_015261.json:
```json
{
    "body": "Patches look good. Positive review.",
    "created_at": "2008-02-27T11:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15261",
    "user": "https://github.com/malb"
}
```

Patches look good. Positive review.



---

archive/issue_comments_015262.json:
```json
{
    "body": "No dice:\n\n```\nsage$ hg import sage_structured_str_list.2.patch\napplying sage_structured_str_list.2.patch\nabort: malformed patch sage/interfaces/singular.py @@ -1089,20 +1089,39 @@ class SingularElement(ExpectElement):\n```\n\nCan you repost the patches and delete all the old ones?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-27T11:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15262",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

No dice:

```
sage$ hg import sage_structured_str_list.2.patch
applying sage_structured_str_list.2.patch
abort: malformed patch sage/interfaces/singular.py @@ -1089,20 +1089,39 @@ class SingularElement(ExpectElement):
```

Can you repost the patches and delete all the old ones?

Cheers,

Michael



---

archive/issue_comments_015263.json:
```json
{
    "body": "Replying to [comment:14 mabshoff]:\n> No dice:\n> {{{\n> sage$ hg import sage_structured_str_list.2.patch\n> applying sage_structured_str_list.2.patch\n> abort: malformed patch sage/interfaces/singular.py `@``@` -1089,20 +1089,39 `@``@` class SingularElement(ExpectElement):\n> }}}\n\nI guess this is since i made the mistake to manually edit the patch.\n\n> Can you repost the patches and delete all the old ones?\n\nI don't know how i can delete an attachment.\n\nNor do i understand what happens. I did `hg_sage.pull()` followed by `hg_sage.update()`, and i expected to get `singular.py` so that `sage_structured_str_list` is in its old state.\n\nBut what i pulled from the official repository did already contain my patch for `sage_structured_str_list`, with the corrected doc test.\n\nCould you verify whether in the official repository the lines 1117-1151 look like that:\n\n```\n    def sage_structured_str_list(self):\n        \"\"\"\n        If self is a Singular list of lists of Singular elements,\n        returns corresponding SAGE list of lists of strings.\n\n        EXAMPLES:\n            sage: R=singular.ring(0,'(x,y)','dp')\n            sage: RL=R.ringlist()\n            sage: RL\n            [1]:\n               0\n            [2]:\n               [1]:\n                  x\n               [2]:\n                  y\n            [3]:\n               [1]:\n                  [1]:\n                     dp\n                  [2]:\n                     1,1\n               [2]:\n                  [1]:\n                     C\n                  [2]:\n                     0\n            [4]:\n               _[1]=0\n            sage: RL.sage_structured_str_list()\n            ['0', ['x', 'y'], [['dp', '1,\\n1 '], ['C', '0 ']], '0']\n        \"\"\"\n        if not (self.type()=='list'):\n            return str(self)\n        return [X.sage_structured_str_list() for X in self]\n```\n\nThis is how they should be **after** applying my patch. \n\nAnyway, i think i need an advice how to make a clean patch.",
    "created_at": "2008-02-27T11:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15263",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:14 mabshoff]:
> No dice:
> {{{
> sage$ hg import sage_structured_str_list.2.patch
> applying sage_structured_str_list.2.patch
> abort: malformed patch sage/interfaces/singular.py `@``@` -1089,20 +1089,39 `@``@` class SingularElement(ExpectElement):
> }}}

I guess this is since i made the mistake to manually edit the patch.

> Can you repost the patches and delete all the old ones?

I don't know how i can delete an attachment.

Nor do i understand what happens. I did `hg_sage.pull()` followed by `hg_sage.update()`, and i expected to get `singular.py` so that `sage_structured_str_list` is in its old state.

But what i pulled from the official repository did already contain my patch for `sage_structured_str_list`, with the corrected doc test.

Could you verify whether in the official repository the lines 1117-1151 look like that:

```
    def sage_structured_str_list(self):
        """
        If self is a Singular list of lists of Singular elements,
        returns corresponding SAGE list of lists of strings.

        EXAMPLES:
            sage: R=singular.ring(0,'(x,y)','dp')
            sage: RL=R.ringlist()
            sage: RL
            [1]:
               0
            [2]:
               [1]:
                  x
               [2]:
                  y
            [3]:
               [1]:
                  [1]:
                     dp
                  [2]:
                     1,1
               [2]:
                  [1]:
                     C
                  [2]:
                     0
            [4]:
               _[1]=0
            sage: RL.sage_structured_str_list()
            ['0', ['x', 'y'], [['dp', '1,\n1 '], ['C', '0 ']], '0']
        """
        if not (self.type()=='list'):
            return str(self)
        return [X.sage_structured_str_list() for X in self]
```

This is how they should be **after** applying my patch. 

Anyway, i think i need an advice how to make a clean patch.



---

archive/issue_comments_015264.json:
```json
{
    "body": "* I just wrote a new patch, waiting for `make test` to finish, so don't bother with this one Simon\n  * to make a new patch you have to remove the patch you already checked in locally. `pull()` will not help since it only adds the patches found upstream but does not remove the ones you already have. \n  * I usually work with branches and if one goes FUBAR I just start with a clean main branche and clone that\n  * or you could use the HG queues, don't know how those work though.",
    "created_at": "2008-02-27T11:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15264",
    "user": "https://github.com/malb"
}
```

* I just wrote a new patch, waiting for `make test` to finish, so don't bother with this one Simon
  * to make a new patch you have to remove the patch you already checked in locally. `pull()` will not help since it only adds the patches found upstream but does not remove the ones you already have. 
  * I usually work with branches and if one goes FUBAR I just start with a clean main branche and clone that
  * or you could use the HG queues, don't know how those work though.



---

archive/issue_comments_015265.json:
```json
{
    "body": "There is a riemann_roch_basis function in both schemes/plane_curves/affine_curve.py\nand schemes/plane_curves/projective_curve.py. I think William Stein and I wrote them.\n(I need it for AG codes, coding/ag_code.py.) As of a few years ago, riemann_roch_basis\nwas unreliable in the sense that Singular would not return the same (and consistent)\nanswers to the same input. I don't remember the counterexamples but could try to dig them\nup in old emails. These were reported to the Singular authors. Maybe it's fixed now?\nAnyway, I strongly hope that this gets fixed if it hasn't been and thanks *very much* \nfor working on this.",
    "created_at": "2008-02-27T12:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15265",
    "user": "https://github.com/wdjoyner"
}
```

There is a riemann_roch_basis function in both schemes/plane_curves/affine_curve.py
and schemes/plane_curves/projective_curve.py. I think William Stein and I wrote them.
(I need it for AG codes, coding/ag_code.py.) As of a few years ago, riemann_roch_basis
was unreliable in the sense that Singular would not return the same (and consistent)
answers to the same input. I don't remember the counterexamples but could try to dig them
up in old emails. These were reported to the Singular authors. Maybe it's fixed now?
Anyway, I strongly hope that this gets fixed if it hasn't been and thanks *very much* 
for working on this.



---

archive/issue_comments_015266.json:
```json
{
    "body": "replaces all other patches attached to this ticket",
    "created_at": "2008-02-27T13:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15266",
    "user": "https://github.com/malb"
}
```

replaces all other patches attached to this ticket



---

archive/issue_comments_015267.json:
```json
{
    "body": "Attachment [trac_2301_superpatch.patch](tarball://root/attachments/some-uuid/ticket2301/trac_2301_superpatch.patch) by @malb created at 2008-02-27 13:02:31\n\nmabshoff, please apply `trac_2301_superpatch.patch` it contains **exactly** the same code as Simon's patches. Credits go to Simon King. `make test` passes.",
    "created_at": "2008-02-27T13:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15267",
    "user": "https://github.com/malb"
}
```

Attachment [trac_2301_superpatch.patch](tarball://root/attachments/some-uuid/ticket2301/trac_2301_superpatch.patch) by @malb created at 2008-02-27 13:02:31

mabshoff, please apply `trac_2301_superpatch.patch` it contains **exactly** the same code as Simon's patches. Credits go to Simon King. `make test` passes.



---

archive/issue_comments_015268.json:
```json
{
    "body": "Replying to [comment:18 malb]:\n> mabshoff, please apply `trac_2301_superpatch.patch` it contains **exactly** the same code as Simon's patches. Credits go to Simon King. `make test` passes.\n\nThank you for your help!",
    "created_at": "2008-02-27T13:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15268",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:18 malb]:
> mabshoff, please apply `trac_2301_superpatch.patch` it contains **exactly** the same code as Simon's patches. Credits go to Simon King. `make test` passes.

Thank you for your help!



---

archive/issue_comments_015269.json:
```json
{
    "body": "Replying to [comment:17 wdj]:\n> As of a few years ago, riemann_roch_basis\n> was unreliable in the sense that Singular would not return the same (and consistent)\n> answers to the same input. \n\nStill the second doctest example has random result. Or do you mean something else?\n\n> Maybe it's fixed now?\n> Anyway, I strongly hope that this gets fixed if it hasn't been and thanks *very much* \n> for working on this.\n\nI don't know if it is fixed on the Singular side. I can only say: If Singular returns a list of ideals with two generators then I believe my patch for the `riemann_roch_basis` in `projective_curve.py` works.\n\nCould you review the Riemann-Roch part of `trac_2301_superpatch.patch`? The positive review of malb refers to the bug in `sage_structured_str_list`, but a review for the other part is still missing, as far as i understand.",
    "created_at": "2008-02-27T14:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15269",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:17 wdj]:
> As of a few years ago, riemann_roch_basis
> was unreliable in the sense that Singular would not return the same (and consistent)
> answers to the same input. 

Still the second doctest example has random result. Or do you mean something else?

> Maybe it's fixed now?
> Anyway, I strongly hope that this gets fixed if it hasn't been and thanks *very much* 
> for working on this.

I don't know if it is fixed on the Singular side. I can only say: If Singular returns a list of ideals with two generators then I believe my patch for the `riemann_roch_basis` in `projective_curve.py` works.

Could you review the Riemann-Roch part of `trac_2301_superpatch.patch`? The positive review of malb refers to the bug in `sage_structured_str_list`, but a review for the other part is still missing, as far as i understand.



---

archive/issue_comments_015270.json:
```json
{
    "body": "Merged trac_2301_superpatch.patch in Sage 2.10.3.rc0",
    "created_at": "2008-02-27T21:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15270",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_2301_superpatch.patch in Sage 2.10.3.rc0



---

archive/issue_events_002478.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-27T21:28:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2301#event-2478"
}
```



---

archive/issue_comments_015271.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-27T21:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15271",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015272.json:
```json
{
    "body": "Simon,\n\nplease open another ticker for \"Follow-up bug in riemann_roch_basis\" - if it is a separate issue we prefer to do it that way. Otherwise tickets get too complicated and we can only close them when all issues have been resolved.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-27T21:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15272",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Simon,

please open another ticker for "Follow-up bug in riemann_roch_basis" - if it is a separate issue we prefer to do it that way. Otherwise tickets get too complicated and we can only close them when all issues have been resolved.

Cheers,

Michael



---

archive/issue_comments_015273.json:
```json
{
    "body": "This appears to cause a failure in another module:\n\nsage -t  devel/sage-rrspace/sage/interfaces/singular.py\n**********************************************************************\nFile \"singular.py\", line 1117:\n   sage: RL.sage_structured_str_list()\nExpected:\n   ['0', ['x', 'y'], [['dp', '1,\\n1 '], ['C', '0 ']], '0']\nGot:\n   [[], [], [], [], [], [], [], [], [], [], [], ['0']]\n**********************************************************************",
    "created_at": "2008-02-28T02:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15273",
    "user": "https://github.com/wdjoyner"
}
```

This appears to cause a failure in another module:

sage -t  devel/sage-rrspace/sage/interfaces/singular.py
**********************************************************************
File "singular.py", line 1117:
   sage: RL.sage_structured_str_list()
Expected:
   ['0', ['x', 'y'], [['dp', '1,\n1 '], ['C', '0 ']], '0']
Got:
   [[], [], [], [], [], [], [], [], [], [], [], ['0']]
**********************************************************************



---

archive/issue_comments_015274.json:
```json
{
    "body": "Ignore my last comment. (I ran the test incorrectly.)",
    "created_at": "2008-02-28T11:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15274",
    "user": "https://github.com/wdjoyner"
}
```

Ignore my last comment. (I ran the test incorrectly.)



---

archive/issue_comments_015275.json:
```json
{
    "body": "Replying to [comment:23 mabshoff]:\n> please open another ticker for \"Follow-up bug in riemann_roch_basis\" - if it is a separate issue we prefer to do it that way. \n\nNext time i will do so. \nI did not open a new ticket because it was the new version of `sage_structured_str_list` that made `riemann_roch_basis` fail, and so i thought that this follow-up still belongs to the same ticket.\n\nAnyway. The doctests for both `singular.py` and `projective_curve.py` pass in `sage-2.10.3.rc0`, so i think it is ok to leave the ticket closed. \n\nSince the problem seems solved, i also think it is not needed to open a new ticket for `riemann_roch_basis`, or am i mistaken?",
    "created_at": "2008-02-28T12:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15275",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:23 mabshoff]:
> please open another ticker for "Follow-up bug in riemann_roch_basis" - if it is a separate issue we prefer to do it that way. 

Next time i will do so. 
I did not open a new ticket because it was the new version of `sage_structured_str_list` that made `riemann_roch_basis` fail, and so i thought that this follow-up still belongs to the same ticket.

Anyway. The doctests for both `singular.py` and `projective_curve.py` pass in `sage-2.10.3.rc0`, so i think it is ok to leave the ticket closed. 

Since the problem seems solved, i also think it is not needed to open a new ticket for `riemann_roch_basis`, or am i mistaken?



---

archive/issue_comments_015276.json:
```json
{
    "body": "Replying to [comment:26 SimonKing]:\n \n> Since the problem seems solved, i also think it is not needed to open a new ticket for `riemann_roch_basis`, or am i mistaken?\n\nI am under the impression that malb's patch merged all your patches, but please verify with 2.10.3.rc0. If some code didn't make it in please open another ticket and post the new patch(es) there and mention in the description that it is a merge leftover from this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-29T16:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15276",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:26 SimonKing]:
 
> Since the problem seems solved, i also think it is not needed to open a new ticket for `riemann_roch_basis`, or am i mistaken?

I am under the impression that malb's patch merged all your patches, but please verify with 2.10.3.rc0. If some code didn't make it in please open another ticket and post the new patch(es) there and mention in the description that it is a merge leftover from this ticket.

Cheers,

Michael



---

archive/issue_comments_015277.json:
```json
{
    "body": "Replying to [comment:27 mabshoff]:\n> I am under the impression that malb's patch merged all your patches, but please verify with 2.10.3.rc0. \n\nYes, everything is in.",
    "created_at": "2008-02-29T22:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2301#issuecomment-15277",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:27 mabshoff]:
> I am under the impression that malb's patch merged all your patches, but please verify with 2.10.3.rc0. 

Yes, everything is in.
