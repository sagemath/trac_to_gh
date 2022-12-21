# Issue 1556: [with patch] improve readability of unknown username error page

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2007-12-18 02:06:13

Assignee: boothby

Keywords: notebook

The current page you get when you try to login to the notebook with an unknown username is incredibly hard to read since it does not even alphabetize usernames.  This patch will alphabetize the list and put each username on a single line. 


---

Attachment


---

Comment by rlm created at 2007-12-21 01:20:28

Resolution: fixed


---

Comment by rlm created at 2007-12-21 01:20:28

Merged in 2.9.1 alpha2


---

Comment by was created at 2007-12-21 06:08:36


```
- Hide quoted text -
On Dec 20, 2007 10:57 PM, William Stein <wstein`@`gmail.com> wrote:
> On Dec 20, 2007 6:24 PM, Robert Miller <rlmillster`@`gmail.com> wrote:
> >
> > As pointed out by Michael Abshoff, it seems like an information leak
> > to list all the usernames on a notebook when you fail to use a valid
> > one to log in. Thoughts?
>
> This exact question comes up about every other week.   Are you talking
> about a public notebook like sagenb.org or sagenb.com?  If so, then
> note that *anybody* can make a new account, and once they login
> with that account, it is trivial for them -- in several different ways -- to get
> a list of all user names.  If you're talking about a server that you personally
> run but with no user accounts, then there is just one name, i.e., "admin".
> In both cases, security by obscuring the existing usernames is no security
> at all.
>
> So maybe you are talking about semi-private servers that have a fixed list
> of accounts and users, like a normal UNIX system say, where potential
> users cannot sign up for a new account -- only an admin can create accounts.
> In this case getting a list of users would be a security issue.  But
> you probably
> don't mean this since it isn't implemented in sage (yet!).

I should have finished by adding that there is no point at all in
not listing usernames in the scenarios in the first paragraph above -- that
would just be security by obscurity.  There is a point in not listing
user names in paragraph two above.  When Sage actually supports
what is described in paragraph two, then when the notebook is in
that mode it shouldn't list usernames.

```

