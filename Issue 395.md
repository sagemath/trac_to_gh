# Issue 395: flatten command for nested lists

archive/issues_000395.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: lists, flatten\n\nThe attached file has a candidate function for a flatten command. The default types to flatten are lists and tuples, but more can be added.\n\n\n```\ndef flatten(in_list, ltypes=(list, tuple)):\n    \"\"\"\n    Flattens a nested list.\n\n    INPUT:\n        in_list -- a list or tuple\n        ltypes -- optional list of particular types to flatten\n\n    OUTPUT:\n        a flat list of the entries of in_list\n\n    EXAMPLES:\n        sage: flatten([[1,1],[1],2])\n        [1, 1, 1, 2]\n        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))\n        ['Hi', 2, (1, 2, 3), 4, 5, 6]\n        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)),ltypes=(list, tuple, sage.modules.vector_rational_dense.Vector_rational_dense))\n        ['Hi', 2, 1, 2, 3, 4, 5, 6]\n    \"\"\"\n    index = 0\n    new_list = [x for x in in_list]\n    while index < len(new_list):\n        if not new_list[index]:\n            new_list.pop(index)\n            continue\n        while isinstance(new_list[index], ltypes):\n            new_list[index : index + 1] = list(new_list[index])\n        index += 1\n    return new_list\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/395\n\n",
    "created_at": "2007-06-28T16:06:22Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "title": "flatten command for nested lists",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/395",
    "user": "mhampton"
}
```
Assignee: mhampton

Keywords: lists, flatten

The attached file has a candidate function for a flatten command. The default types to flatten are lists and tuples, but more can be added.


```
def flatten(in_list, ltypes=(list, tuple)):
    """
    Flattens a nested list.

    INPUT:
        in_list -- a list or tuple
        ltypes -- optional list of particular types to flatten

    OUTPUT:
        a flat list of the entries of in_list

    EXAMPLES:
        sage: flatten([[1,1],[1],2])
        [1, 1, 1, 2]
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))
        ['Hi', 2, (1, 2, 3), 4, 5, 6]
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)),ltypes=(list, tuple, sage.modules.vector_rational_dense.Vector_rational_dense))
        ['Hi', 2, 1, 2, 3, 4, 5, 6]
    """
    index = 0
    new_list = [x for x in in_list]
    while index < len(new_list):
        if not new_list[index]:
            new_list.pop(index)
            continue
        while isinstance(new_list[index], ltypes):
            new_list[index : index + 1] = list(new_list[index])
        index += 1
    return new_list
```



Issue created by migration from https://trac.sagemath.org/ticket/395





---

archive/issue_comments_001932.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-06-28T16:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1932",
    "user": "mhampton"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001933.json:
```json
{
    "body": "New version:\n\ndef flatten(in_list, ltypes=(list, tuple)):\n    \"\"\"\n    Flattens a nested list.\n\n    INPUT:\n        in_list -- a list or tuple\n        ltypes -- optional list of particular types to flatten\n\n    OUTPUT:\n        a flat list of the entries of in_list\n\n    EXAMPLES:\n        sage: flatten([[1,1],[1],2])\n        [1, 1, 1, 2]\n        sage: flatten([[1,2,3], (4,5), [[[1],[2]]]])\n        [1, 2, 3, 4, 5, 1, 2]\n\n    In the following example, the vector isn't flattened because\n    it is not given in the ltypes input.\n        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))\n        ['Hi', 2, (1, 2, 3), 4, 5, 6]\n\n    We give the vector type and then even the vector gets flattened:\n        sage: flatten((['Hi',2,vector(QQ,[1,2,3])], (4,5,6)),\nltypes=(list,\ntuple,sage.modules.vector_rational_dense.Vector_rational_dense))\n        ['Hi', 2, 1, 2, 3, 4, 5, 6]\n\n    We flatten a finite field.\n        sage: flatten(GF(5))\n        [0, 1, 2, 3, 4]\n        sage: flatten([GF(5)])\n        [Finite Field of size 5]\n        sage: flatten([GF(5)], ltypes = (list, tuple,\nsage.rings.finite_field.FiniteField_prime_modn))\n        [0, 1, 2, 3, 4]\n\n    \"\"\"\n    index = 0\n    new_list = [x for x in in_list]\n    while index < len(new_list):\n        while isinstance(new_list[index], ltypes):\n            if len(new_list[index]) != 0:\n                new_list[index : index + 1] = list(new_list[index])\n            else:\n                new_list.pop(index)\n                break\n        index += 1\n    return new_list",
    "created_at": "2007-07-05T15:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1933",
    "user": "mhampton"
}
```

New version:

def flatten(in_list, ltypes=(list, tuple)):
    """
    Flattens a nested list.

    INPUT:
        in_list -- a list or tuple
        ltypes -- optional list of particular types to flatten

    OUTPUT:
        a flat list of the entries of in_list

    EXAMPLES:
        sage: flatten([[1,1],[1],2])
        [1, 1, 1, 2]
        sage: flatten([[1,2,3], (4,5), [[[1],[2]]]])
        [1, 2, 3, 4, 5, 1, 2]

    In the following example, the vector isn't flattened because
    it is not given in the ltypes input.
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))
        ['Hi', 2, (1, 2, 3), 4, 5, 6]

    We give the vector type and then even the vector gets flattened:
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])], (4,5,6)),
ltypes=(list,
tuple,sage.modules.vector_rational_dense.Vector_rational_dense))
        ['Hi', 2, 1, 2, 3, 4, 5, 6]

    We flatten a finite field.
        sage: flatten(GF(5))
        [0, 1, 2, 3, 4]
        sage: flatten([GF(5)])
        [Finite Field of size 5]
        sage: flatten([GF(5)], ltypes = (list, tuple,
sage.rings.finite_field.FiniteField_prime_modn))
        [0, 1, 2, 3, 4]

    """
    index = 0
    new_list = [x for x in in_list]
    while index < len(new_list):
        while isinstance(new_list[index], ltypes):
            if len(new_list[index]) != 0:
                new_list[index : index + 1] = list(new_list[index])
            else:
                new_list.pop(index)
                break
        index += 1
    return new_list



---

archive/issue_comments_001934.json:
```json
{
    "body": "Sage 2.8.2 has a flatten command. It also seems to work on nested lists:\n\n```\nsage: L\n[[1, 2], [1, 2]]\nsage: flatten(L)\n[1, 2, 1, 2]\nsage: L=[L,[L,[L,[L]]]]\nsage: L\n[[[1, 2], [1, 2]], [[[1, 2], [1, 2]], [[[1, 2], [1, 2]], [[[1, 2], [1, 2]]]]]]\nsage: flatten(L)\n[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]\n```\n\nSo am I correct to assume that this ticket can be closed? \n\nCheers,\n\nMichael",
    "created_at": "2007-08-23T12:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1934",
    "user": "mabshoff"
}
```

Sage 2.8.2 has a flatten command. It also seems to work on nested lists:

```
sage: L
[[1, 2], [1, 2]]
sage: flatten(L)
[1, 2, 1, 2]
sage: L=[L,[L,[L,[L]]]]
sage: L
[[[1, 2], [1, 2]], [[[1, 2], [1, 2]], [[[1, 2], [1, 2]], [[[1, 2], [1, 2]]]]]]
sage: flatten(L)
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
```

So am I correct to assume that this ticket can be closed? 

Cheers,

Michael



---

archive/issue_comments_001935.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T02:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1935",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_001936.json:
```json
{
    "body": "Yep, this has been in SAGE a while.",
    "created_at": "2007-08-29T02:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1936",
    "user": "was"
}
```

Yep, this has been in SAGE a while.



---

archive/issue_comments_001937.json:
```json
{
    "body": "This still has some problems on empty lists, which I (Marshall Hampton) will try to fix soon.  the simplest example of the problem for the current (2.8.4.1) behavior is:\nflatten([[],[]])\n[[]]\n\nIt should return [].",
    "created_at": "2007-09-11T16:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1937",
    "user": "mhampton"
}
```

This still has some problems on empty lists, which I (Marshall Hampton) will try to fix soon.  the simplest example of the problem for the current (2.8.4.1) behavior is:
flatten([[],[]])
[[]]

It should return [].



---

archive/issue_comments_001938.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2007-09-11T16:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1938",
    "user": "mhampton"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_001939.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-11T16:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1939",
    "user": "mhampton"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_001940.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-11T16:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1940",
    "user": "mhampton"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_001941.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2007-09-11T16:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1941",
    "user": "mhampton"
}
```

Changing status from reopened to new.



---

archive/issue_comments_001942.json:
```json
{
    "body": "Replying to [comment:6 mhampton]:\n\nSorry, I am not used to this formatting.  My example should be:\n\nflatten([[],[]])\n\n[[]]\n",
    "created_at": "2007-09-11T16:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1942",
    "user": "mhampton"
}
```

Replying to [comment:6 mhampton]:

Sorry, I am not used to this formatting.  My example should be:

flatten([[],[]])

[[]]




---

archive/issue_comments_001943.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-11T20:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1943",
    "user": "mhampton"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001944.json:
```json
{
    "body": "Here is a new version that I believe fixes the problem.\n\n\n```\ndef flatten(in_list, ltypes=(list, tuple)):\n   \"\"\"\n   Flattens a nested list.\n\n   INPUT:\n       in_list -- a list or tuple\n       ltypes -- optional list of particular types to flatten\n\n   OUTPUT:\n       a flat list of the entries of in_list\n\n   EXAMPLES:\n       sage: flatten([[1,1],[1],2])\n       [1, 1, 1, 2]\n       sage: flatten([[1,2,3], (4,5), [[[1],[2]]]])\n       [1, 2, 3, 4, 5, 1, 2]\n\n   In the following example, the vector isn't flattened because\n   it is not given in the ltypes input. \n       sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))\n       ['Hi', 2, (1, 2, 3), 4, 5, 6]\n\n   We give the vector type and then even the vector gets flattened:\n       sage: flatten((['Hi',2,vector(QQ,[1,2,3])], (4,5,6)), ltypes=(list, tuple,sage.modules.vector_rational_dense.Vector_rational_dense))\n       ['Hi', 2, 1, 2, 3, 4, 5, 6]\n\n   We flatten a finite field. \n       sage: flatten(GF(5))\n       [0, 1, 2, 3, 4]\n       sage: flatten([GF(5)])\n       [Finite Field of size 5]\n       sage: flatten([GF(5)], ltypes = (list, tuple, sage.rings.finite_field.FiniteField_prime_modn))\n       [0, 1, 2, 3, 4]\n\n   Degenerate cases:\n      sage: flatten([[],[]])\n      []\n      sage: flatten([[[]]])\n      []\n   \"\"\"\n   index = 0\n   new_list = [x for x in in_list]\n   while index < len(new_list):\n      while isinstance(new_list[index], ltypes):\n         v = list(new_list[index])\n         if len(v) != 0:\n            new_list[index : index + 1] = v\n         else:\n            new_list.pop(index)\n            index += -1\n            break\n      index += 1\n   return new_list\n\n```\n",
    "created_at": "2007-09-11T20:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1944",
    "user": "mhampton"
}
```

Here is a new version that I believe fixes the problem.


```
def flatten(in_list, ltypes=(list, tuple)):
   """
   Flattens a nested list.

   INPUT:
       in_list -- a list or tuple
       ltypes -- optional list of particular types to flatten

   OUTPUT:
       a flat list of the entries of in_list

   EXAMPLES:
       sage: flatten([[1,1],[1],2])
       [1, 1, 1, 2]
       sage: flatten([[1,2,3], (4,5), [[[1],[2]]]])
       [1, 2, 3, 4, 5, 1, 2]

   In the following example, the vector isn't flattened because
   it is not given in the ltypes input. 
       sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))
       ['Hi', 2, (1, 2, 3), 4, 5, 6]

   We give the vector type and then even the vector gets flattened:
       sage: flatten((['Hi',2,vector(QQ,[1,2,3])], (4,5,6)), ltypes=(list, tuple,sage.modules.vector_rational_dense.Vector_rational_dense))
       ['Hi', 2, 1, 2, 3, 4, 5, 6]

   We flatten a finite field. 
       sage: flatten(GF(5))
       [0, 1, 2, 3, 4]
       sage: flatten([GF(5)])
       [Finite Field of size 5]
       sage: flatten([GF(5)], ltypes = (list, tuple, sage.rings.finite_field.FiniteField_prime_modn))
       [0, 1, 2, 3, 4]

   Degenerate cases:
      sage: flatten([[],[]])
      []
      sage: flatten([[[]]])
      []
   """
   index = 0
   new_list = [x for x in in_list]
   while index < len(new_list):
      while isinstance(new_list[index], ltypes):
         v = list(new_list[index])
         if len(v) != 0:
            new_list[index : index + 1] = v
         else:
            new_list.pop(index)
            index += -1
            break
      index += 1
   return new_list

```




---

archive/issue_comments_001945.json:
```json
{
    "body": "Changing type from defect to task.",
    "created_at": "2007-09-11T20:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1945",
    "user": "mhampton"
}
```

Changing type from defect to task.



---

archive/issue_comments_001946.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2007-09-11T23:00:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1946",
    "user": "was"
}
```

Changing priority from minor to major.



---

archive/issue_comments_001947.json:
```json
{
    "body": "applied for sage-2.8.4.2.",
    "created_at": "2007-09-13T15:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1947",
    "user": "was"
}
```

applied for sage-2.8.4.2.



---

archive/issue_comments_001948.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-13T15:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/395#issuecomment-1948",
    "user": "was"
}
```

Resolution: fixed
