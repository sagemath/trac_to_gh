# Issue 4637: bug/stupid design of padic_printing.sep print mode stuff

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-27 06:58:30

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





---

Comment by roed created at 2009-03-18 06:13:21

Requires the #5499 patch.


---

Attachment

I know there are still problems.  But all doctests currently pass, I don't know of remaining bugs, and I wanted to keep this manageable (rather than continuing the tradition of patch-bombs).  I'm going to keep working on adding more documentation.


---

Comment by ncalexan created at 2009-03-18 18:41:22

First comment: your choice of ... for eliding terms in printing conflicts with the doctest framework; could that be .. or something different?  For example, in factory.py around line 150,


```
        sage: T = Qp(5, print_mode='series', print_max_terms=4); b = R(-70700); repr(b)                                                  
        '2*5^2 + 4*5^3 + 5^4 + 2*5^5 + ... + O(5^22)'
```


is *not* testing what you think it is -- the doctester matches ... inside of strings!  (You've typoed, and you meant `T(-70700)`.)


---

Comment by ncalexan created at 2009-03-18 19:16:40

I'll be honest, this is ugly beyond belief.

Why isn't this printing functionality factored out into a separate printing object which is then part of the data for the ring?  For example, we now have a boatload of printing parameters... sounds like an object to me.  We have, for example, a `name` and a `ram_name`; for something like `Zq(5^2, 'a')` `name` is 'a' and one could make 5 print as `ram_name`, often 'p'.  But what happens when we have two level extensions, rather than just one level?

Why aren't we constructing `Zp` first, setting its printing, and then constructing `Zq` on top of that `Zp`?

I am reviewing this positive because:

 * it passes doctests;
 * it appears to fix at least one of the bugs at hand;
 * it adds valuable documentation and tests;
 * and, most importantly, is a step in the direction the maintainer, David Roe, wants the code to progress.


---

Comment by roed created at 2009-03-23 02:26:00

Fair criticisms.  The current model of passing in parameters hasn't really stood up well as I've added features.  Now that someone else has read the code, I'd be happy to discuss better options.


---

Comment by was created at 2009-04-10 17:04:03

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

Comment by was created at 2009-04-10 17:05:52

(That said, the patch does add a _lot_ of very good new examples and documentation.)


---

Comment by mabshoff created at 2009-04-13 03:13:24

With the latest patch at #5499 all doctests pass.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 08:47:15

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 08:47:15

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-15 02:35:11

David: This patch is also a diff, so next time you might want to export. I have committed this patch in your name.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-15 03:28:37

This is the version of the patch I merged with credit given to David.
