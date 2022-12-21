# Issue 191: prime table / database

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-13 20:51:51

Assignee: was

CC:  mvngu

It would be very nice if SAGE had a large table/database of prime numbers.

For example, on the number theory list:


```
Look in the file
 
http://homes.cerias.purdue.edu/~ssw/bell/r1
 
for the factorizations of p^p - 1 for most p < 180.
 
(If you change "r1" to "r2", you get the factors of p^p + 1.)
 
For the meaning of the "L" and "M" notation, see the papers at
 
http://homes.cerias.purdue.edu/~ssw/bell/index.html
```

So a person really wanted to factor some numbers p^p -1, but couldn't
with PARI.  If SAGE had tables of the factorizations of those numbers,
it could have done it via a lookup, and the verbose message could have
given the above reference.  Something similar would be good for a huge
range of classes of prime numbers.   This would be an excellent student
project.


---

Comment by was created at 2007-01-13 20:51:56

Changing priority from major to minor.


---

Comment by mvngu created at 2009-06-27 00:52:05

CC'ing myself.


---

Comment by davidloeffler created at 2009-07-20 19:54:59

Changing component from number theory to factorization.


---

Comment by davidloeffler created at 2009-07-20 19:54:59

Changing assignee from was to tbd.


---

Comment by jdemeyer created at 2010-07-08 14:17:36

Resolution: duplicate


---

Comment by jdemeyer created at 2010-07-08 14:17:36

See #7239


---

Comment by davidloeffler created at 2010-07-08 19:20:26

Resolution changed from duplicate to 


---

Comment by davidloeffler created at 2010-07-08 19:20:26

Changing status from closed to new.


---

Comment by davidloeffler created at 2010-07-08 19:20:26

Please do not close tickets yourself. Only release managers have the authority to do this.


---

Comment by davidloeffler created at 2010-07-08 19:20:48

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-07-08 19:23:39

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-07-08 19:23:39

What I usually do in this situation is to set the ticket to "needs review" with a message saying I think it ought to be closed. Then if someone else agrees, we can set it to "positive review", and then it'll show up in the list of tickets to be merged in the next release. Then the release manager will close it. In this case, I've put it at "positive review", since I agree with your claim that it should be fixed. 

BTW, I'm not sure "duplicate" is fair; this ticket has been open for years, so #7239 was a duplicate of this one rather than the other way round. Perhaps "fixed" is the most appropriate resolution. But that is for the release manager to decide.


---

Comment by mpatel created at 2010-07-20 09:40:24

I'm resolving this as a "duplicate," simply because the only relevant milestone is "sage-duplicate/invalid/wontfix."


---

Comment by mpatel created at 2010-07-20 09:40:24

Resolution: duplicate
