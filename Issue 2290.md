# Issue 2290: [with easy patch] typo in calculus.py

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2008-02-24 09:48:13

Assignee: tba




---

Attachment


---

Comment by mabshoff created at 2008-02-24 17:40:19

Hmm, I am not convinced that the result is correct:

```
88	88	    We can also make \class{CallableSymbolicExpressions}, which is a \class{SymbolicExpression} 
89	 	    that are functions of variables in a fixed order. Each 
 	89	    that is function of variables in a fixed order. Each 
90	90	    \class{SymbolicExpression} has a function() method used to create a 
91	91	    \class{CallableSymbolicExpression}.
```

While I agree that it should be singular, I think an article is missing. I guess in British English the above without the article would be correct, but with my American English I would like to see an article there.

Thoughts?

Cheers,

Michael


---

Attachment

my attempt, as a native english speaker


---

Comment by zimmerma created at 2008-02-25 14:31:59

I am neither an american nor a british english speaker, but the new patch seems definitively better
to me (it also fixes the extra 's' in CallableSymbolicExpressions which I did not spot).


---

Comment by mabshoff created at 2008-02-25 15:14:04

Resolution: fixed


---

Comment by mabshoff created at 2008-02-25 15:14:04

Merged sage-2290-english.patch in Sage 2.10.3.alpha0
