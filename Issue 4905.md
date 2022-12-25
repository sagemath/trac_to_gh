# Issue 4905: convert sage.coding.* docstrings to Sphinx

archive/issues_004905.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4905\n\n",
    "created_at": "2009-01-01T22:46:55Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "convert sage.coding.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4905",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4905





---

archive/issue_comments_037139.json:
```json
{
    "body": "Attachment [trac_4905.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905.patch) by @mwhansen created at 2009-01-02 02:57:18",
    "created_at": "2009-01-02T02:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37139",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4905.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905.patch) by @mwhansen created at 2009-01-02 02:57:18



---

archive/issue_comments_037140.json:
```json
{
    "body": "Will the table in sd_codes.py which the patch indicats is \n\n\n```\n \t166\t    n 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 B_n 1 1 1 2 2 3 4 7 9 \n \t167\t    16 25 55 103 261 731 \n```\n\nactually print in the docstring as\n\n\n```\n \tn  2 4 6 8 10 12 14 16 18 20 22 24  26  28  30 \n       B_n 1 1 1 2  2  3  4  7  9 16 25 55 103 261 731 \n```\n\n?",
    "created_at": "2009-01-02T03:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37140",
    "user": "https://github.com/wdjoyner"
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

archive/issue_comments_037141.json:
```json
{
    "body": "Nope, thanks for catching that.  I've attached a patch which fixes that.",
    "created_at": "2009-01-02T03:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37141",
    "user": "https://github.com/mwhansen"
}
```

Nope, thanks for catching that.  I've attached a patch which fixes that.



---

archive/issue_comments_037142.json:
```json
{
    "body": "Thanks. Can we read the html or pdf output somewhere or is it possible to generate it ourselves after applying the patch?",
    "created_at": "2009-01-02T10:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37142",
    "user": "https://github.com/wdjoyner"
}
```

Thanks. Can we read the html or pdf output somewhere or is it possible to generate it ourselves after applying the patch?



---

archive/issue_comments_037143.json:
```json
{
    "body": "You can read the html output at http://sage.math.washington.edu/home/mhansen/sage-3.2.3-sage.math-only-x86_64-Linux/devel/sage/doc/output/html/en/reference/index.html  There's a few things I need to do before the patch to build the docs is ready.",
    "created_at": "2009-01-02T10:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37143",
    "user": "https://github.com/mwhansen"
}
```

You can read the html output at http://sage.math.washington.edu/home/mhansen/sage-3.2.3-sage.math-only-x86_64-Linux/devel/sage/doc/output/html/en/reference/index.html  There's a few things I need to do before the patch to build the docs is ready.



---

archive/issue_comments_037144.json:
```json
{
    "body": "That helps a lot.\n\nHere are some more typos:\n\n* In the section on assmus_mattson_designs:\n\n\n```\ns = |{ i | A_i^* \\not= 0, 0<i\\leq n-t}|\n```\n\ndoes not output the math correctly. Maybe \n\n\n```\n$s = |\\{ i\\ |\\ A_i^* \\not= 0,\\ 0<i\\leq n-t\\}|$\n```\n\nwould be better?\n\nAlso,\n\n\n```\n \t771\t        (1) If `Ai\\not= 0` and \n \t772\t        `d\\leq i\\leq n then Ci = { c in C | wt(c) = i}` holds a \n \t773\t        simple t-design. \n\t774\t         \n \t775\t        (2) If `Ai*\\not= 0` and \n \t776\t        `d*\\leq i\\leq n-t then Ci* = { c in C* | wt(c) = i}` \n \t777\t        holds a simple t-design. \n```\n\nshould maybe be (maybe add a \"math::\" somewhere?)\n\n\n```\n \t771\t        (1) If `Ai\\not= 0` and \n \t772\t        `d\\leq i\\leq n` then `C_i = \\{ c \\in C\\ |\\ wt(c) = i\\}` holds a \n \t773\t        simple t-design. \n\t774\t         \n \t775\t        (2) If `Ai*\\not= 0` and \n \t776\t        `d*\\leq i\\leq n-t` then `C_i^* = \\{ c \\in C*\\ |\\ wt(c) = i\\}` \n \t777\t        holds a simple t-design. \n```\n\nand\n\n\n```\n \t793\t        `B = \\{supp(c) | c in C_i\\}` is the set of supports of the \n```\n\nshould be\n\n\n```\n \t793\t        `B = \\{supp(c)\\ |\\ c \\in C_i\\}` is the set of supports of the \n```\n\n\n* In automorphism_group_binary_code,\n\n\n```\n \t701\t                     \\{ g in S_n\\ |\\ g(c) \\in C, \\forall c\\in C\\},  \n```\n\nshould be\n\n```\n \t701\t                     \\{ g \\in S_n\\ |\\ g(c) \\in C, \\forall c\\in C\\},  \n```\n\n\nWhat else needs to be done to review this?",
    "created_at": "2009-01-02T11:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37144",
    "user": "https://github.com/wdjoyner"
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

archive/issue_comments_037145.json:
```json
{
    "body": "Attachment [trac_4905-2.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905-2.patch) by @mwhansen created at 2009-01-02 20:16:18\n\nI've updated the second patch to take care of these.",
    "created_at": "2009-01-02T20:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37145",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4905-2.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905-2.patch) by @mwhansen created at 2009-01-02 20:16:18

I've updated the second patch to take care of these.



---

archive/issue_comments_037146.json:
```json
{
    "body": "This happens a few times in the diff:\n\n```\nBEFORE:\n356\t \t    provided 0 < delta < 1-1/q. \nAFTER: \t \n \t416\t    provided 0 delta 1-1/q. \n```\n\n\nNotice that the < \"less than\" signs are just deleted.",
    "created_at": "2009-01-03T04:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37146",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_037147.json:
```json
{
    "body": "This is worrisome:\n\n```\nBEFORE:\n4\t4\tAUTHOR: \n5\t \t    -- David Joyner (2007-05): initial version \n6\t \t    --    \"         (2008-02): added cyclic codes, Hamming codes \n7\t \t    --    \"         (2008-03): added BCH code, LinearCodeFromCheckmatrix,   \n```\n\n\n\n```\nAFTER:\n \t6\t- David Joyner (2007-05): initial version \n \t7\t \n \t8\t- \" (2008-02): added cyclic codes, Hamming codes \n \t9\t \n \t10\t- \" (2008-03): added BCH code, LinearCodeFromCheckmatrix, ReedSolomonCode, WalshCode, \n \t11\t  DuadicCodeEvenPair, DuadicCodeOddPair, QR codes (even and odd) \n \t12\t \n```\n\n\nIt seems like AUTHOR: doesn't get changed to AUTHOR::.  Also, I'm worried about the -'s making a correct list, but maybe I shouldn't be.",
    "created_at": "2009-01-03T04:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37147",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_037148.json:
```json
{
    "body": "Attachment [trac_4905-2.2.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905-2.2.patch) by @wdjoyner created at 2009-01-09 00:41:11\n\nThese patches look good to me. \n\nI've forgotten now what exactly is involved in giving this a positive review beyond just looking them over, but this looks like it should go in to me.",
    "created_at": "2009-01-09T00:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37148",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4905-2.2.patch](tarball://root/attachments/some-uuid/ticket4905/trac_4905-2.2.patch) by @wdjoyner created at 2009-01-09 00:41:11

These patches look good to me. 

I've forgotten now what exactly is involved in giving this a positive review beyond just looking them over, but this looks like it should go in to me.



---

archive/issue_comments_037149.json:
```json
{
    "body": "Attachment [sage.coding-final.patch](tarball://root/attachments/some-uuid/ticket4905/sage.coding-final.patch) by @mwhansen created at 2009-02-21 19:15:51",
    "created_at": "2009-02-21T19:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37149",
    "user": "https://github.com/mwhansen"
}
```

Attachment [sage.coding-final.patch](tarball://root/attachments/some-uuid/ticket4905/sage.coding-final.patch) by @mwhansen created at 2009-02-21 19:15:51



---

archive/issue_events_011323.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-24T18:58:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4905#event-11323"
}
```



---

archive/issue_comments_037150.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37150",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037151.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4905#issuecomment-37151",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael
