# Issue 8447: Detect when Sage is old and issue warning

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-05 16:59:00

Assignee: tbd

CC:  leif mpatel was

Various threads - e.g

http://groups.google.co.uk/group/sage-devel/browse_thread/thread/29ee9e1d4efdeda2

indicate that it is problematic when very old distributions of Sage are used in distributions of Debian, Ubunta etc. 

Whilst this is "shutting the gate afte the horse has bolted", it would be useful if future versions of Sage indicated when they are very old. 

Perhaps one message should be generated if the date on the computer is more than 4 months in advance of the Sage release date, and a stronger message is isssues if it is more than 12 months old. The exact wording and periods would have to be discussed in sage-devel. 

Whatever method is used, it should be portable, and non rely on GNU-specific options to the 'date' command, or any other GNUism. 

See 

http://www.opengroup.org/onlinepubs/9699919799/utilities/date.html


for POSIX options to the _date_ command. 



---

Comment by drkirkby created at 2010-08-07 07:44:48

I'm increasing the priority of this, in the hope someone will notice it. I think it would be quite easy to do for someone familiar with python, and very useful, though personally I don't know how to do it. 

Dave


---

Comment by drkirkby created at 2010-08-07 07:44:48

Changing priority from major to critical.


---

Comment by leif created at 2010-08-07 08:40:10

Well, at least the Sage banner shows the release date... ;-)

Perhaps something for our NagBot writer?

From the ticket's title I first guessed you meant detecting "dead" Sage 3.x (Debian/Ubuntu) packages installed on the user's system, like this one:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
```

A few times there have been "bug reports" and questions (not explicitly) referring to _that_ version... :)
| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
Another issue is the "frozen" `#sage-devel` banner nobody has the power to update:

```
Logs of this channel are posted online | Sage - free open-source mathematics software |
Ask questions here and wait, or post to sage-support list | www.sagemath.org |
stable: 4.3.1 | dev: 4.3.2.alpha1
```


I'm not sure if it is desirable to continually check for recent Sage versions (e.g. at start-up); at least such a feature should be disableable.


---

Comment by drkirkby created at 2010-08-07 09:43:17

Replying to [comment:2 leif]:
> Well, at least the Sage banner shows the release date... ;-)

True, but many users will probably assume its the latest version available when they go to the Debian site. If there was a warning like 


```
---------------------------------------------------------------------
----------------------------------------------------------------------
```

| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
|                                                                    |
| WARNING You are using a VERY old version of Sage. We suggest you   |
| to http://www.sagemath.org/ and download the latest version.       |
| The latest version has a lot more features                         |

> I'm not sure if it is desirable to continually check for recent Sage versions (e.g. at start-up); at least such a feature should be disableable.

I was thinking just on date. That should be very easy to do - just a bit of Python, that issues one warning when Sage is say 3 months old, and a stronger one when its a year old. Assuming the date in Sage is right, and the persons computer has the right date, that should work. 

Checking online for version updates is a more tricky issue - some people have privacy concerns over that. If that was implemented, I think the default should be off. It's also a lot more work to do. 

My python skills are next to useless, otherwise I'd tackle this myself. (Not that having poor python skills seems to put some others off writing code for Sage!) 

Dave


---

Comment by jdemeyer created at 2013-02-08 14:29:01

Changing priority from critical to minor.


---

Comment by jdemeyer created at 2013-02-08 14:29:01

I wouldn't mind closing this as wontfix... what's the point anyway, people see the release date every time they start Sage.


---

Comment by jdemeyer created at 2013-06-21 09:40:16

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-06-21 09:40:27

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-13 08:32:28

Resolution: wontfix
