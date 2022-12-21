# Issue 3260: Make #optional usable at a higher level

Issue created by migration from Trac.

Original creator: broune

Original creation time: 2008-05-20 12:20:28

Assignee: failure

CC:  mmezzarobba

When adding optional spkgs to Sage, it is necessary to go through the Python interface file and put #optional on every single line of every single doctest, to indicate that those doctests should not be run.

It would be nice to be able to put #optional at, say, the top of the file, or in the docstring for the module or class, and then have that imply that every doctest within is optional.



---

Comment by was created at 2008-05-21 12:53:47

COMMENTS:
1. This is "already supported", but in an obscure way, which might very well be broken (?).  In local/bin/sage-doctest we have:

```
    if not optional and sl.find("optional") != -1 and \
               sl.find('package') != -1 and sl.find('installed'):
        return ''
```

Thus if you put anywhere in the docstring for a function (or the top of the file) all
three works optional, package, and installed, then everything is considered optional.


2. I don't really like your proposal, even though I once implemented it somewhat.  Generally speaking I think it's better that every example makes it crystal clear that the line of code being illustrated will NOT work without the user installing an optional package.    Users (like me) absolutely hate pasting in random lines and having them fail for no obvious reason.  It is, of course, good if error messages for optional code clearly indicate their optionality, but sometimes people don't read error messages.   This is a usability/psychology sort of thing.


---

Comment by broune created at 2008-05-21 13:44:14

If it already works, then one way to resolve this ticket is to document that in the appropriate places.

As for your number 2, I understand your objection to be that the docstring gotten when using Sage's built-in help-system should warn users that a particular doctest requires some optional package to work.

I can get behind that. It should not be hard to inject a notice of that into the docstring shown in the help system, without having them sprinkled all over the Python file. This notice could be much more helpful than a comment saying "#optional", since it is not obvious what a comment saying #optional means, if you do not already know. E.g. Sage could inject a string before each optional doctest saying "This example depends on an optional package being installed." Or it could preserve the status quo by injecting #optional on each line.


---

Comment by roed created at 2013-03-14 22:01:50

Wow, 5 years.  This ticket should be re-examined now that #12415 is finished.  Some solutions may be more tractable now.


---

Comment by roed created at 2013-03-28 23:15:47

Changing component from doctest to doctest framework.


---

Comment by jdemeyer created at 2016-08-12 09:14:44

Duplicate of #20427.


---

Comment by jdemeyer created at 2016-08-12 09:14:44

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-08-12 09:14:52

Changing status from needs_review to positive_review.


---

Comment by embray created at 2016-08-30 13:32:25

Resolution: wontfix


---

Comment by embray created at 2016-08-30 13:32:25

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).
