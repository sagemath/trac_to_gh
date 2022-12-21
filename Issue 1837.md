# Issue 1837: [with patch] pass through options from groebner_basis

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-18 19:53:57

Assignee: malb

Now this has an effect:

```
sage: sr = mq.SR()
sage: F,s = sr.polynomial_system()
sage: F.groebner_basis(redSB=False)
[(a)*k002 + (a^2)*k003 + 1, k001 + (a^2 + 1)*k002 + (a^3 + a + 1), k000 + (a^3 + a^2 + 1)*k003 + (a^3 + a^2 + a), (a^2)*s003 + (a^3 + a^2)*k003 + (a + 1), s002 + (a^2)*k002 + (a), s001 + (a)*k001 + (a^2 + 1), s000 + (a^2 + 1)*k000 + (a + 1), w103 + k003 + (a^3 + a^2 + 1), w102 + k002 + (a^3 + 1), w101 + k001 + (a^3 + a + 1), w100 + k000 + (a^3 + a^2 + a), (a^2)*x103 + (a^2)*s003 + (a + 1), x102 + s002 + (a), x101 + (a^3 + a + 1)*x102 + (a^3 + 1)*x103 + s001 + (a^3 + a + 1)*s002 + (a^3 + 1)*s003 + (a), x100 + (a^3)*x101 + (a + 1)*x102 + (a + 1)*x103 + s000 + (a^3)*s001 + (a + 1)*s002 + (a + 1)*s003 + (a^2 + a + 1), k103 + s000 + (a^3)*s001 + (a + 1)*s002 + (a + 1)*s003 + (a^2 + a), k102 + (a^3 + a)*s000 + (a^2)*s001 + (a^2)*s002 + s003 + (a^2 + a + 1), k101 + (a)*s000 + (a)*s001 + s002 + (a^3 + a^2 + a + 1)*s003 + (a^2 + a), k100 + (a^2 + 1)*s000 + s001 + (a^3 + a^2)*s002 + (a^2 + 1)*s003 + (a^2 + a + 1), k003^2 + k000]

sage: F.groebner_basis(redSB=True)
[(a)*k002 + (a^2)*k003 + 1, (a)*k001 + (a^2 + a + 1)*k003, k000 + (a^3 + a^2 + 1)*k003 + (a^3 + a^2 + a), (a^2)*s003 + (a^3 + a^2)*k003 + (a + 1), (a)*s002 + (a + 1)*k003, s001 + (a^2 + a + 1)*k003 + (a^2 + 1), s000 + (a^3 + a^2)*k003, w103 + k003 + (a^3 + a^2 + 1), w102 + (a)*k003, (a)*w101 + (a^2 + a + 1)*k003 + (a^2 + 1), w100 + (a^3 + a^2 + 1)*k003, x103 + (a + 1)*k003, (a)*x102 + (a + 1)*k003 + (a^2), (a^3)*x101 + (a^3 + a^2 + 1)*k003, (a^2)*x100 + (a^2 + 1)*k003 + (a^3 + a^2), (a^3)*k103 + k003 + (a^2 + a), (a^3)*k102 + (a^2 + a + 1)*k003 + (a^2 + a), (a^3)*k101 + k003 + (a^3 + a^2 + a), (a^3)*k100 + (a^2 + a + 1)*k003 + (a^3 + a^2 + a), k003^2 + (a^3 + a^2 + 1)*k003 + (a^3 + a^2 + a)]
```


This is not equivalent to #1396 because this isn't unified yet.


---

Attachment


---

Comment by mabshoff created at 2008-01-22 00:07:23

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-22 00:29:25

But there is some trouble applying it: 

hunk 1 has a reject, but that is easily fixed, see http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/groebner-kwds-hunk-1.patch

hunk 2 seems unrelated to the patch and I cannot find anything remotely similar that this part of the patch would apply against:

```
537	537	            singular = S.parent() 
538	538	            ov = singular.option("get") 
539	539	            singular.option("redSB") # make sure we always compute reduced bases 
 	540	 
 	541	            for o,v in kwds.iteritems(): 
 	542	                if v: 
 	543	                    singular.option(o) 
 	544	                     
 	545	                else: 
 	546	                    singular.option("no"+o) 
540	547	 
541	548	            if algorithm=="groebner": 
542	549	                S = S.groebner() 
```


hunk 3 & 4 work as expected, with slight fuzz. See http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/groebner-kwds.patch

I am doctesting the resulting merge at the moment. Please let me know if hunk #2 was a mistake in which case I will close this ticket, assuming the doctests pass.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-22 01:23:42

Doctests pass, so I am closing this.

malb: Please reopen the ticket if it turns out that the second hunk wasn't included by mistake. I will release 2.10.1.alpha1 very shortly, so you can use that as a base to patch things up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-22 01:24:18

Resolution: fixed


---

Comment by mabshoff created at 2008-01-22 01:24:18

Merged in Sage 2.10.1.alpha1


---

Comment by malb created at 2008-01-22 11:49:33

I'll check as soon as I get my hands on alpha1
