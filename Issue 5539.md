# Issue 5539: "sage -docbuild" could use a better error message

Issue created by migration from https://trac.sagemath.org/ticket/5539

Original creator: robertwb

Original creation time: 2009-03-17 00:21:15

Assignee: tba


```
$ sage -docbuild
You must specify the document name and the output format
```


It would be nice if it at least gave a list of available documents to build. 


---

Comment by AlexGhitza created at 2009-03-17 00:29:32

It would also be nice if it gave a list of available output formats.


---

Comment by jhpalmieri created at 2009-06-10 21:57:51

Here's a patch which doesn't do what you're asking, but tells you how to get the list.


---

Attachment


---

Comment by mvngu created at 2009-06-13 11:46:29

Yes, I agree that the command

```
sage -docbuild -help
```

provides more help on building the documentation. The error message of 

```
sage -docbuild
}}} 
now informs the user about that command. Positive review.


---

Comment by ncalexan created at 2009-06-13 22:57:14

Resolution: fixed
