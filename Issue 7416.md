# Issue 7416: Create a 'man page'

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-11-09 13:26:38

Assignee: mvngu

CC:  david.kirkby@onetel.net

The title says it all really. 


---

Comment by kini created at 2013-07-15 19:59:01

IMO this man page should be written in reStructuredText for maintainability. `make` should generate the man page file using `rst2man.py` from Python's docutils, and `make install` should copy it to the appropriate place to register it into the system's man page database.
