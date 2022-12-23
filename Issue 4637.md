# Issue 4637: bug/stupid design of padic_printing.sep print mode stuff

archive/issues_004637.json:
```json
{
    "body": "Assignee: was\n\nCC:  ncalexan\n\nConsider this session:\n\n```\nbsd:padics was$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: Qp(7, print_mode=\"digits\")(1/3)\n...44444444444444444445\nsage: padic_printing.sep('][')\nsage: Qp(7, print_mode=\"digits\")(1/3)\n...44444444444444444445\nsage: Qp(11, print_mode=\"digits\")(1/3)\n...73737373737373737374\nsage: Qp(17, print_mode=\"digits\")(1/3)\n...B5B5B5B5B5B5B5B5B5B6\nsage: Qp(97, print_mode=\"digits\")(1/3)\n...64][64][64][64][64][64][64][64][64][64][64][64][64][64][64][64][64][64][64][65\nsage: Qp(7, print_mode=\"digits\")(1/3)\n...44444444444444444445\nsage: Qp(389, print_mode=\"digits\")(1/3)\n...259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][130\nsage: padic_printing.sep('|')\nsage: Qp(389, print_mode=\"digits\")(1/3)\n...259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][130\nsage: Qp(997, print_mode=\"digits\")(1/3)\n...664|664|664|664|664|664|664|664|664|664|664|664|664|664|664|664|664|664|664|665\nsage: Qp(7, print_mode=\"digits\")(1/3)\n...44444444444444444445\nsage: Qp(3, print_mode=\"digits\")(1/3)\n....1\nsage: Qp(5, print_mode=\"digits\")(1/3)\n...31313131313131313132\n```\n\n| Sage Version 3.2.1.alpha2, Release Date: 2008-11-26                |\n| Type notebook() for the GUI, and license() for information.        |\nBasically the print separator for p-adic fields depends on what the global padic_printing.sep(...) thing happens to have been set at when that field was first created.  There seems to be absolutely no way to change it later.  The dependence is also totally baffling?  Why the hell does it change for 97 but not 17, 11, 7?  WTF!?!\n\nSolution -- make the frickin' separator a property of the field that must be passed in.  Notice now that isn't even possible.  totally get rid of this stupid padic_printing object. \n\n\n```\nsage: Qp(5, print_mode=\"digits\", sep='|')\nTypeError: Qp() got an unexpected keyword argument 'sep'\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4637\n\n",
    "created_at": "2008-11-27T06:58:30Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "bug/stupid design of padic_printing.sep print mode stuff",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4637",
    "user": "was"
}
```
Assignee: was

CC:  ncalexan

Consider this session:

```
bsd:padics was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Qp(7, print_mode="digits")(1/3)
...44444444444444444445
sage: padic_printing.sep('][')
sage: Qp(7, print_mode="digits")(1/3)
...44444444444444444445
sage: Qp(11, print_mode="digits")(1/3)
...73737373737373737374
sage: Qp(17, print_mode="digits")(1/3)
...B5B5B5B5B5B5B5B5B5B6
sage: Qp(97, print_mode="digits")(1/3)
...64][64][64][64][64][64][64][64][64][64][64][64][64][64][64][64][64][64][64][65
sage: Qp(7, print_mode="digits")(1/3)
...44444444444444444445
sage: Qp(389, print_mode="digits")(1/3)
...259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][130
sage: padic_printing.sep('|')
sage: Qp(389, print_mode="digits")(1/3)
...259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][129][259][130
sage: Qp(997, print_mode="digits")(1/3)
...664|664|664|664|664|664|664|664|664|664|664|664|664|664|664|664|664|664|664|665
sage: Qp(7, print_mode="digits")(1/3)
...44444444444444444445
sage: Qp(3, print_mode="digits")(1/3)
....1
sage: Qp(5, print_mode="digits")(1/3)
...31313131313131313132
```

| Sage Version 3.2.1.alpha2, Release Date: 2008-11-26                |
| Type notebook() for the GUI, and license() for information.        |
Basically the print separator for p-adic fields depends on what the global padic_printing.sep(...) thing happens to have been set at when that field was first created.  There seems to be absolutely no way to change it later.  The dependence is also totally baffling?  Why the hell does it change for 97 but not 17, 11, 7?  WTF!?!

Solution -- make the frickin' separator a property of the field that must be passed in.  Notice now that isn't even possible.  totally get rid of this stupid padic_printing object. 


```
sage: Qp(5, print_mode="digits", sep='|')
TypeError: Qp() got an unexpected keyword argument 'sep'
```




Issue created by migration from https://trac.sagemath.org/ticket/4637





---

archive/issue_comments_034877.json:
```json
{
    "body": "Requires the #5499 patch.",
    "created_at": "2009-03-18T06:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34877",
    "user": "roed"
}
```

Requires the #5499 patch.



---

archive/issue_comments_034878.json:
```json
{
    "body": "Attachment\n\nI know there are still problems.  But all doctests currently pass, I don't know of remaining bugs, and I wanted to keep this manageable (rather than continuing the tradition of patch-bombs).  I'm going to keep working on adding more documentation.",
    "created_at": "2009-03-18T06:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34878",
    "user": "roed"
}
```

Attachment

I know there are still problems.  But all doctests currently pass, I don't know of remaining bugs, and I wanted to keep this manageable (rather than continuing the tradition of patch-bombs).  I'm going to keep working on adding more documentation.



---

archive/issue_comments_034879.json:
```json
{
    "body": "First comment: your choice of ... for eliding terms in printing conflicts with the doctest framework; could that be .. or something different?  For example, in factory.py around line 150,\n\n\n```\n        sage: T = Qp(5, print_mode='series', print_max_terms=4); b = R(-70700); repr(b)                                                  \n        '2*5^2 + 4*5^3 + 5^4 + 2*5^5 + ... + O(5^22)'\n```\n\n\nis *not* testing what you think it is -- the doctester matches ... inside of strings!  (You've typoed, and you meant `T(-70700)`.)",
    "created_at": "2009-03-18T18:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34879",
    "user": "ncalexan"
}
```

First comment: your choice of ... for eliding terms in printing conflicts with the doctest framework; could that be .. or something different?  For example, in factory.py around line 150,


```
        sage: T = Qp(5, print_mode='series', print_max_terms=4); b = R(-70700); repr(b)                                                  
        '2*5^2 + 4*5^3 + 5^4 + 2*5^5 + ... + O(5^22)'
```


is *not* testing what you think it is -- the doctester matches ... inside of strings!  (You've typoed, and you meant `T(-70700)`.)



---

archive/issue_comments_034880.json:
```json
{
    "body": "I'll be honest, this is ugly beyond belief.\n\nWhy isn't this printing functionality factored out into a separate printing object which is then part of the data for the ring?  For example, we now have a boatload of printing parameters... sounds like an object to me.  We have, for example, a `name` and a `ram_name`; for something like `Zq(5^2, 'a')` `name` is 'a' and one could make 5 print as `ram_name`, often 'p'.  But what happens when we have two level extensions, rather than just one level?\n\nWhy aren't we constructing `Zp` first, setting its printing, and then constructing `Zq` on top of that `Zp`?\n\nI am reviewing this positive because:\n\n* it passes doctests;\n* it appears to fix at least one of the bugs at hand;\n* it adds valuable documentation and tests;\n* and, most importantly, is a step in the direction the maintainer, David Roe, wants the code to progress.",
    "created_at": "2009-03-18T19:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34880",
    "user": "ncalexan"
}
```

I'll be honest, this is ugly beyond belief.

Why isn't this printing functionality factored out into a separate printing object which is then part of the data for the ring?  For example, we now have a boatload of printing parameters... sounds like an object to me.  We have, for example, a `name` and a `ram_name`; for something like `Zq(5^2, 'a')` `name` is 'a' and one could make 5 print as `ram_name`, often 'p'.  But what happens when we have two level extensions, rather than just one level?

Why aren't we constructing `Zp` first, setting its printing, and then constructing `Zq` on top of that `Zp`?

I am reviewing this positive because:

* it passes doctests;
* it appears to fix at least one of the bugs at hand;
* it adds valuable documentation and tests;
* and, most importantly, is a step in the direction the maintainer, David Roe, wants the code to progress.



---

archive/issue_comments_034881.json:
```json
{
    "body": "Fair criticisms.  The current model of passing in parameters hasn't really stood up well as I've added features.  Now that someone else has read the code, I'd be happy to discuss better options.",
    "created_at": "2009-03-23T02:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34881",
    "user": "roed"
}
```

Fair criticisms.  The current model of passing in parameters hasn't really stood up well as I've added features.  Now that someone else has read the code, I'd be happy to discuss better options.



---

archive/issue_comments_034882.json:
```json
{
    "body": "REMARK: \n\nThis patch introduces 5 new functions with no doctests, hence fails what I consider *the most basic* review criterion:\n\n```\n\t360\t    def _sep(self): \n \t361\t        return self.sep \n \t362\t \n \t363\t    def _alphabet(self): \n \t364\t        return self.alphabet \n \t365\t \n \t366\t    def _max_ram_terms(self): \n \t367\t        return self.max_ram_terms \n \t368\t \n \t369\t    def _max_unram_terms(self): \n \t370\t        return self.max_unram_terms \n \t371\t \n \t372\t    def _max_terse_terms(self): \n \t373\t        return self.max_terse_terms  \n```\n",
    "created_at": "2009-04-10T17:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34882",
    "user": "was"
}
```

REMARK: 

This patch introduces 5 new functions with no doctests, hence fails what I consider *the most basic* review criterion:

```
	360	    def _sep(self): 
 	361	        return self.sep 
 	362	 
 	363	    def _alphabet(self): 
 	364	        return self.alphabet 
 	365	 
 	366	    def _max_ram_terms(self): 
 	367	        return self.max_ram_terms 
 	368	 
 	369	    def _max_unram_terms(self): 
 	370	        return self.max_unram_terms 
 	371	 
 	372	    def _max_terse_terms(self): 
 	373	        return self.max_terse_terms  
```




---

archive/issue_comments_034883.json:
```json
{
    "body": "(That said, the patch does add a *lot* of very good new examples and documentation.)",
    "created_at": "2009-04-10T17:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34883",
    "user": "was"
}
```

(That said, the patch does add a *lot* of very good new examples and documentation.)



---

archive/issue_comments_034884.json:
```json
{
    "body": "With the latest patch at #5499 all doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T03:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34884",
    "user": "mabshoff"
}
```

With the latest patch at #5499 all doctests pass.

Cheers,

Michael



---

archive/issue_comments_034885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T08:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34885",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034886.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T08:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34886",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_034887.json:
```json
{
    "body": "David: This patch is also a diff, so next time you might want to export. I have committed this patch in your name.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T02:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34887",
    "user": "mabshoff"
}
```

David: This patch is also a diff, so next time you might want to export. I have committed this patch in your name.

Cheers,

Michael



---

archive/issue_comments_034888.json:
```json
{
    "body": "This is the version of the patch I merged with credit given to David.",
    "created_at": "2009-04-15T03:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4637#issuecomment-34888",
    "user": "mabshoff"
}
```

This is the version of the patch I merged with credit given to David.
