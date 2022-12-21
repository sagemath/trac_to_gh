# Issue 4245: notebook -- error clicking editing when there is a < in the html.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-05 18:46:04

Assignee: boothby


```

On Sun, Oct 5, 2008 at 3:56 AM, Joël Duet <joel.duet`@`gmail.com> wrote:
> Hi,
> Here is my problem :
> I want to write "a<b" in the HTML part of my worksheet (notebook() style).
>
> 1) I click "Edit"
> 2) After a }}} and before a {{{, I type (without quotes) : " <p> Let
> <i>a&lt;b</i>.</p>"
> 3) I click "Save Changes"
>
> And it's done but if I click again at "Edit", I get (without quotes) : "<p>
> Let <i>a<b</i>.</p>" and it's bad.
>
> What can I do if I want to Edit several times ?
>

This is definitely a bug, which could be fixed.  In the meantime, as a workround 
you might just do

"<p>Let  $a < b$.</p>"

since that will look better anyways. 
```



---

Comment by jhpalmieri created at 2008-10-17 23:22:05

I can't tell if I'm seeing the same problem or not, so I have a new ticket which might be related: #4316.


---

Attachment


---

Comment by mhansen created at 2009-01-24 07:34:31

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-24 07:34:31

Changing assignee from boothby to mhansen.


---

Comment by jhpalmieri created at 2009-01-24 16:18:46

When testing the problem in #4316:

```
%html 
some math: $x<y$.
```

I get the message 

```
NameError: global name 'cgi' is not defined
```

More importantly, when testing the problem reported here, I don't see a change in behavior: after editing the worksheet and typing 

```
<p> Let <i>a&lt;b</i>.</p>
```

in between cells and saving, it looks fine, but when I click "Edit" again, the `&lt;` has turned into `<`, and it is printed wrong.


---

Comment by jason created at 2009-02-06 08:57:00

Mike's patch above breaks %html mode since it assumes you literally want "<" every time you write it.  That means you can't type `<b>hello</b>`.  I like it better the other way (before), that demanded that you type &lt; instead of <.

This is somewhat of a moot point now that TinyMCE is in.


---

Comment by jason created at 2009-02-06 08:58:01

Changing priority from minor to critical.


---

Comment by jason created at 2009-02-06 08:58:01

I've attached a patch which fixes the quoting issue for the Edit button.  Basically, we need to escape ampersands as well as less thans.


---

Attachment


---

Comment by jason created at 2009-02-06 08:58:46

Apply only trac_4245-html-escape.patch


---

Comment by jason created at 2009-02-06 08:59:00

Changing assignee from mhansen to jason.


---

Comment by jason created at 2009-02-06 08:59:00

Changing status from assigned to new.


---

Comment by kcrisman created at 2009-02-06 14:09:01

Positive review, fixes the problem for me.  Explanation makes sense too, although interestingly I never saw e.g. &lt anywhere, whether in TinyMCE or in the Edit button, or even in "View Source", when this problem occurred.


---

Comment by jhpalmieri created at 2009-02-06 15:35:15

Looks good to me, too.


---

Comment by jason created at 2009-02-06 16:03:34

kcrisman: that was the problem.  There should have &lt; things in the Edit view.


---

Comment by mabshoff created at 2009-02-06 21:53:21

Resolution: fixed


---

Comment by mabshoff created at 2009-02-06 21:53:21

Merged trac_4245-html-escape.patch only in Sage 3.3.alpha6.

Cheers,

Michael
