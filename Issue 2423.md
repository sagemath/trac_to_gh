# Issue 2423: notebook() opens up to the entire world by default

Issue created by migration from https://trac.sagemath.org/ticket/2423

Original creator: jason

Original creation time: 2008-03-07 22:41:35

Assignee: boothby

See http://groups.google.com/group/sage-support/browse_thread/thread/3aeb27037554491b

The meat of the issue is that notebook() by default allows connections from anyone to the local computer.  This patch fixes it by calling the "interface" option of twisted to only allow connections from a specific interface.

Quoting Yi Qiang in the email discussion:


```
The problem is that the notebook is never launched to bound to a specific
interface. Could you please file a trac# against this?

The specific issue is that in twistedconf.tac, we start the server like so:

strports.service('tls:8000:privateKey=/Users/yqiang/.sage/notebook/private.pem:certKey=/Users/yqiang/.sage/notebook/public.pem',
factory)

It should read something like

strports.service('tls:8000:interface=
127.0.0.1:privateKey=/Users/yqiang/.sage/notebook/private.pem:certKey=/Users/yqiang/.sage/notebook/public.pem',
factory)

to only listen on localhost.

```



---

Attachment


---

Comment by yi created at 2008-03-07 23:15:27

This patch looks good to me. 

The only question I have is what happens when a user specifies an invalid address, but this was not handled previously so it's not a regression.

+1


---

Comment by was created at 2008-03-07 23:18:02

Looks good to me.  Thanks!


---

Comment by mabshoff created at 2008-03-07 23:22:25

Resolution: fixed


---

Comment by mabshoff created at 2008-03-07 23:22:25

Merged in Sage 2.10.3.rc3
