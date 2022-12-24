# Issue 4905: convert sage.coding.* docstrings to Sphinx

archive/issues_004905.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4905\n\n",
    "created_at": "2009-01-01T22:46:55Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "convert sage.coding.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4905",
    "user": "mhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4905





---

archive/issue_comments_037211.json:
```json
{
    "body": "Attachment [trac_4905.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905.patch) by mhansen created at 2009-01-02 02:57:18",
    "created_at": "2009-01-02T02:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37211",
    "user": "mhansen"
}
```

Attachment [trac_4905.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905.patch) by mhansen created at 2009-01-02 02:57:18



---

archive/issue_comments_037212.json:
```json
{
    "body": "Will the table in sd_codes.py which the patch indicats is \n\n\n```\n \t166\t    n 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 B_n 1 1 1 2 2 3 4 7 9 \n \t167\t    16 25 55 103 261 731 \n```\n\nactually print in the docstring as\n\n\n```\n \tn  2 4 6 8 10 12 14 16 18 20 22 24  26  28  30 \n       B_n 1 1 1 2  2  3  4  7  9 16 25 55 103 261 731 \n```\n\n?",
    "created_at": "2009-01-02T03:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37212",
    "user": "wdj"
}
```

Will the table in sd_codes.py which the patch indicats is 


```
 	166	    n 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 B_n 1 1 1 2 2 3 4 7 9 
 	167	    16 25 55 103 261 731 
```

actually print in the docstring as


```
 	n  2 4 6 8 10 12 14 16 18 20 22 24  26  28  30 
       B_n 1 1 1 2  2  3  4  7  9 16 25 55 103 261 731 
```

?



---

archive/issue_comments_037213.json:
```json
{
    "body": "Nope, thanks for catching that.  I've attached a patch which fixes that.",
    "created_at": "2009-01-02T03:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37213",
    "user": "mhansen"
}
```

Nope, thanks for catching that.  I've attached a patch which fixes that.



---

archive/issue_comments_037214.json:
```json
{
    "body": "Thanks. Can we read the html or pdf output somewhere or is it possible to generate it ourselves after applying the patch?",
    "created_at": "2009-01-02T10:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37214",
    "user": "wdj"
}
```

Thanks. Can we read the html or pdf output somewhere or is it possible to generate it ourselves after applying the patch?



---

archive/issue_comments_037215.json:
```json
{
    "body": "You can read the html output at http://sage.math.washington.edu/home/mhansen/sage-3.2.3-sage.math-only-x86_64-Linux/devel/sage/doc/output/html/en/reference/index.html  There's a few things I need to do before the patch to build the docs is ready.",
    "created_at": "2009-01-02T10:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37215",
    "user": "mhansen"
}
```

You can read the html output at http://sage.math.washington.edu/home/mhansen/sage-3.2.3-sage.math-only-x86_64-Linux/devel/sage/doc/output/html/en/reference/index.html  There's a few things I need to do before the patch to build the docs is ready.



---

archive/issue_comments_037216.json:
```json
{
    "body": "That helps a lot.\n\nHere are some more typos:\n\n* In the section on assmus_mattson_designs:\n\n\n```\ns = |{ i | A_i^* \\not= 0, 0<i\\leq n-t}|\n```\n\ndoes not output the math correctly. Maybe \n\n\n```\n$s = |\\{ i\\ |\\ A_i^* \\not= 0,\\ 0<i\\leq n-t\\}|$\n```\n\nwould be better?\n\nAlso,\n\n\n```\n \t771\t        (1) If `Ai\\not= 0` and \n \t772\t        `d\\leq i\\leq n then Ci = { c in C | wt(c) = i}` holds a \n \t773\t        simple t-design. \n\t774\t         \n \t775\t        (2) If `Ai*\\not= 0` and \n \t776\t        `d*\\leq i\\leq n-t then Ci* = { c in C* | wt(c) = i}` \n \t777\t        holds a simple t-design. \n```\n\nshould maybe be (maybe add a \"math::\" somewhere?)\n\n\n```\n \t771\t        (1) If `Ai\\not= 0` and \n \t772\t        `d\\leq i\\leq n` then `C_i = \\{ c \\in C\\ |\\ wt(c) = i\\}` holds a \n \t773\t        simple t-design. \n\t774\t         \n \t775\t        (2) If `Ai*\\not= 0` and \n \t776\t        `d*\\leq i\\leq n-t` then `C_i^* = \\{ c \\in C*\\ |\\ wt(c) = i\\}` \n \t777\t        holds a simple t-design. \n```\n\nand\n\n\n```\n \t793\t        `B = \\{supp(c) | c in C_i\\}` is the set of supports of the \n```\n\nshould be\n\n\n```\n \t793\t        `B = \\{supp(c)\\ |\\ c \\in C_i\\}` is the set of supports of the \n```\n\n\n* In automorphism_group_binary_code,\n\n\n```\n \t701\t                     \\{ g in S_n\\ |\\ g(c) \\in C, \\forall c\\in C\\},  \n```\n\nshould be\n\n```\n \t701\t                     \\{ g \\in S_n\\ |\\ g(c) \\in C, \\forall c\\in C\\},  \n```\n\n\nWhat else needs to be done to review this?",
    "created_at": "2009-01-02T11:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37216",
    "user": "wdj"
}
```

That helps a lot.

Here are some more typos:

* In the section on assmus_mattson_designs:


```
s = |{ i | A_i^* \not= 0, 0<i\leq n-t}|
```

does not output the math correctly. Maybe 


```
$s = |\{ i\ |\ A_i^* \not= 0,\ 0<i\leq n-t\}|$
```

would be better?

Also,


```
 	771	        (1) If `Ai\not= 0` and 
 	772	        `d\leq i\leq n then Ci = { c in C | wt(c) = i}` holds a 
 	773	        simple t-design. 
	774	         
 	775	        (2) If `Ai*\not= 0` and 
 	776	        `d*\leq i\leq n-t then Ci* = { c in C* | wt(c) = i}` 
 	777	        holds a simple t-design. 
```

should maybe be (maybe add a "math::" somewhere?)


```
 	771	        (1) If `Ai\not= 0` and 
 	772	        `d\leq i\leq n` then `C_i = \{ c \in C\ |\ wt(c) = i\}` holds a 
 	773	        simple t-design. 
	774	         
 	775	        (2) If `Ai*\not= 0` and 
 	776	        `d*\leq i\leq n-t` then `C_i^* = \{ c \in C*\ |\ wt(c) = i\}` 
 	777	        holds a simple t-design. 
```

and


```
 	793	        `B = \{supp(c) | c in C_i\}` is the set of supports of the 
```

should be


```
 	793	        `B = \{supp(c)\ |\ c \in C_i\}` is the set of supports of the 
```


* In automorphism_group_binary_code,


```
 	701	                     \{ g in S_n\ |\ g(c) \in C, \forall c\in C\},  
```

should be

```
 	701	                     \{ g \in S_n\ |\ g(c) \in C, \forall c\in C\},  
```


What else needs to be done to review this?



---

archive/issue_comments_037217.json:
```json
{
    "body": "Attachment [trac_4905-2.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905-2.patch) by mhansen created at 2009-01-02 20:16:18\n\nI've updated the second patch to take care of these.",
    "created_at": "2009-01-02T20:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37217",
    "user": "mhansen"
}
```

Attachment [trac_4905-2.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905-2.patch) by mhansen created at 2009-01-02 20:16:18

I've updated the second patch to take care of these.



---

archive/issue_comments_037218.json:
```json
{
    "body": "This happens a few times in the diff:\n\n```\nBEFORE:\n356\t \t    provided 0 < delta < 1-1/q. \nAFTER: \t \n \t416\t    provided 0 delta 1-1/q. \n```\n\n\nNotice that the < \"less than\" signs are just deleted.",
    "created_at": "2009-01-03T04:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37218",
    "user": "was"
}
```

This happens a few times in the diff:

```
BEFORE:
356	 	    provided 0 < delta < 1-1/q. 
AFTER: 	 
 	416	    provided 0 delta 1-1/q. 
```


Notice that the < "less than" signs are just deleted.



---

archive/issue_comments_037219.json:
```json
{
    "body": "This is worrisome:\n\n```\nBEFORE:\n4\t4\tAUTHOR: \n5\t \t    -- David Joyner (2007-05): initial version \n6\t \t    --    \"         (2008-02): added cyclic codes, Hamming codes \n7\t \t    --    \"         (2008-03): added BCH code, LinearCodeFromCheckmatrix,   \n```\n\n\n\n```\nAFTER:\n \t6\t- David Joyner (2007-05): initial version \n \t7\t \n \t8\t- \" (2008-02): added cyclic codes, Hamming codes \n \t9\t \n \t10\t- \" (2008-03): added BCH code, LinearCodeFromCheckmatrix, ReedSolomonCode, WalshCode, \n \t11\t  DuadicCodeEvenPair, DuadicCodeOddPair, QR codes (even and odd) \n \t12\t \n```\n\n\nIt seems like AUTHOR: doesn't get changed to AUTHOR::.  Also, I'm worried about the -'s making a correct list, but maybe I shouldn't be.",
    "created_at": "2009-01-03T04:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37219",
    "user": "was"
}
```

This is worrisome:

```
BEFORE:
4	4	AUTHOR: 
5	 	    -- David Joyner (2007-05): initial version 
6	 	    --    "         (2008-02): added cyclic codes, Hamming codes 
7	 	    --    "         (2008-03): added BCH code, LinearCodeFromCheckmatrix,   
```



```
AFTER:
 	6	- David Joyner (2007-05): initial version 
 	7	 
 	8	- " (2008-02): added cyclic codes, Hamming codes 
 	9	 
 	10	- " (2008-03): added BCH code, LinearCodeFromCheckmatrix, ReedSolomonCode, WalshCode, 
 	11	  DuadicCodeEvenPair, DuadicCodeOddPair, QR codes (even and odd) 
 	12	 
```


It seems like AUTHOR: doesn't get changed to AUTHOR::.  Also, I'm worried about the -'s making a correct list, but maybe I shouldn't be.



---

archive/issue_comments_037220.json:
```json
{
    "body": "Attachment [trac_4905-2.2.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905-2.2.patch) by wdj created at 2009-01-09 00:41:11\n\nThese patches look good to me. \n\nI've forgotten now what exactly is involved in giving this a positive review beyond just looking them over, but this looks like it should go in to me.",
    "created_at": "2009-01-09T00:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37220",
    "user": "wdj"
}
```

Attachment [trac_4905-2.2.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905-2.2.patch) by wdj created at 2009-01-09 00:41:11

These patches look good to me. 

I've forgotten now what exactly is involved in giving this a positive review beyond just looking them over, but this looks like it should go in to me.



---

archive/issue_comments_037221.json:
```json
{
    "body": "Attachment [sage.coding-final.patch](tarball://root/attachments/some-uuid/ticket4905/sage.coding-final.patch) by mhansen created at 2009-02-21 19:15:51",
    "created_at": "2009-02-21T19:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37221",
    "user": "mhansen"
}
```

Attachment [sage.coding-final.patch](tarball://root/attachments/some-uuid/ticket4905/sage.coding-final.patch) by mhansen created at 2009-02-21 19:15:51



---

archive/issue_comments_037222.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37222",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037223.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37223",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael
