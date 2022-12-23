# Issue 8996: @ character is usernames is problematic

Issue created by migration from https://trac.sagemath.org/ticket/8996

Original creator: ddrake

Original creation time: 2010-05-19 23:58:30

Assignee: jason, was

In http://groups.google.com/group/sage-support/t/2acd499a566efce1 a user had troubles because his username is his email address and the `@` character messed things up. 

We should either allow `@` (and similar non-alphanumeric) characters and make things work properly with them, or explicitly disallow them. Note that right now (4.4.1), http://sagenb.org/register says that `@` is allowed in usernames!


---

Comment by robertwb created at 2010-05-20 00:10:31

Dupe of #8995 (though this description is slightly more informative). If it's not to hard, I have a strong preference for allowing `@` in usernames, as I often use my email address as a username because it's both easy to remember and likely to be unique.


---

Comment by ddrake created at 2010-05-20 02:47:57

Resolution: duplicate


---

Comment by ddrake created at 2010-05-20 02:48:50

Replying to [comment:1 robertwb]:
> Dupe of #8995 (though this description is slightly more informative). If it's not to hard, I have a strong preference for allowing `@` in usernames, as I often use my email address as a username because it's both easy to remember and likely to be unique. 

I agree. I use my email address as a username for the same reasons.
