# Issue 7855: offline sage notebook

Issue created by migration from https://trac.sagemath.org/ticket/7855

Original creator: was

Original creation time: 2010-01-06 14:50:27

Assignee: was

CC:  jhpalmieri


```
On Jan 6, 1:03 am, William Stein <wst...@gmail.com> wrote:
> Does anybody know how Google Gears or whatever does things like
> offline gmail?

First, skip Gears - that project fades out and will be html5. Chrome,
Firefox and Safari are afaik nearly capable of providing these
features, or already do. Gears is just an early example that is
similar to html5.

One feature is to have a database. Then, you can access tables and
entries with (probably a bit limited?) SQL.  For the implementation,
there could be a table for each worksheet, or one table holding all
cells and a n:m relationship table for worksheet:cell or something
like that.

Another html5 feature is to define offline resources. These are html
(or other) files which are stored locally. They will be used for the
starting page and the static javascript code. Maybe it's also possible
for this feature to save everything as such an offline resource and no
need for the database mentioned above.

http://www.w3.org/TR/offline-webapps/
http://www.w3.org/TR/2009/WD-webdatabase-20091222/
http://www.w3.org/TR/html5/offline.html

and here i found examples:
http://html5demos.com/
especially this file is interesting:
http://html5demos.com/tweets.js
and
http://html5demos.com/offlineapp

```



---

Comment by chapoton created at 2017-07-25 07:45:56

Changing status from new to needs_review.


---

Comment by chapoton created at 2017-07-25 07:45:56

I think this is very outdated.


---

Comment by jhpalmieri created at 2017-07-25 15:01:13

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2017-07-25 15:01:19

Agreed.


---

Comment by embray created at 2017-12-12 08:23:33

Resolution: wontfix
