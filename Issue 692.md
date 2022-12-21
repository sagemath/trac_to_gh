# Issue 692: add form capabilities to sage notebook

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-19 16:38:55

Assignee: boothby


```
On 9/19/07, PhantomDuck from Finland wrote:
> I am complete Sage newbie. The question is, that is it possible to add
> html-code to Sage web-browser interface?

You can click "edit", then paste arbitray HTML code anywhere in the notebook
body, and it will render as HTML.

> The goal would be insert some text-fields/checkboxes and radioboxes
> and wait for user input. After the input has been given the Sage would
> run some python programs and display the output. Does this approach
> require a submit button too?

You could create an HTML form easily enough by just pasting the HTML
into a worksheet in Edit mode.  *Unfortunately* nobody has actually 
implemented a feature in the notebook that would allow for submission
of the contents of the form and evaluation of the result.  I think this
would actually be pretty easy to implement for a developer. 

> e.g.
> We have equation 2x-1=0. There could be one html-text field where the
> user could input the root of the polynomial equation, namely 1/2. Then
> the Sage would check whether the root is correct and give some
> feedback to the user.
> 
> Thank you in advance (I know I might be asking silly things but please
> forgive me for being a total newbie).
> 
> 
> --~--~---------~--~----~------------~-------~--~----~
> You received this message because you are subscribed to the Google Groups "sage-newbie" group.
> To post to this group, send email to sage-newbie`@`googlegroups.com
> To unsubscribe from this group, send email to sage-newbie-unsubscribe`@`googlegroups.com
> For more options, visit this group at http://groups.google.com/group/sage-newbie?hl=en
> -~----------~----~----~----~------~----~------~--~---
> 
> 


-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org

```



---

Comment by jason created at 2007-11-29 16:32:05

Implementing ticket #1322 would enable variables that allow input in HTML forms as well as other sorts of javascript controls as well, so I'm marking this as a duplicate (am I allowed to mark things as duplicates?)


---

Comment by jason created at 2007-11-29 16:32:05

Resolution: duplicate
