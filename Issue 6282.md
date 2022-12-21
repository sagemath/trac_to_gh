# Issue 6282: document SAGE_CHECK

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-14 09:34:44

Assignee: tbd

Add the following to the SAGE_ROOT/README.txt, since right now the SAGE_CHECK flag is totally undocumented:


```
If you want to run the test suite for each individual spkg as it is installed, do

   export SAGE_CHECK="yes"

before starting the Sage build.  This will run each test suite, and will raise an error if any failures occur. 
```



---

Comment by was created at 2009-06-14 09:37:40

The "patch" is just the text in the description, which must be manually added to the README.txt by the release manager who closes this ticket.  Refereeing this means reading the text and making sure there are no typos and that it is not stupid.


---

Comment by jhpalmieri created at 2009-06-14 15:00:07

By the way, in this part:

```
If you have a machine with n processors, say, type  
             export MAKE="make -j4"
```

should "n" be changed to "4"?


---

Comment by ncalexan created at 2009-06-14 22:18:42

Resolution: fixed


---

Comment by ncalexan created at 2009-06-14 22:18:42

Done by ncalexan for 4.0.2.alpha0.
