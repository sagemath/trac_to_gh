# Issue 2936: notebook -- write a completely new use/data/security model backend for the notebook

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-15 22:17:16

Assignee: boothby

This sounds daunting but actually Brian Lauber already has mostly done this.  

I've attached a patch that *doesn't work* very well against sage-3.0.alpha5.  It's just for reference sake.  It has a lot of really good code in it, and does sort of work.  It probably *did* work fine against sage-10.4.   My hope is that he can update the page to work with
sage-3.0, then fix all issues, and we can get this into Sage. 

Brian Lauber describes the patch thus:

```
Okay, this version of the patch set is diffed against the current branch.  I believe there was only 1 merge conflict, and it was trivial to resolve.  Here is what you need to know about the redesign:


1. Authentication is handled by 3 separate interfaces:

  * PasswordChecker:  This checks a username/password pair on behalf of the Notebook

  * PasswordChanger:  This can change the password associated with a username.  A running Notebook instance does not need to have a PasswordChanger since some backends might not support it (for example: if the campus has a central sign-on service).

  * RegistrationManager: This is used to add and remove users from the notebook.  Once again, a Notebook does not need to define a RegistrationManager if the backend does not support adding or removing users.  Additionally, an administrator could simply choose to forgo a RegistrationManager for security reasons.


2. User information is maintained by UserInformation objects.  These break the user's information into three basic types:

  * PersonalInformation: Examples include first name, last name, e-mail, etc

  * Preferences: Information regarding the user's preferred notebook experience.  Enabling pretty print by default is once example.

  * Permissions: This actually controls how the user is allowed to interact w/ the Notebook's backend.  Currently, it only consists of an account_type field.  In the future, this should be broken into several finer-grained permissions, such as can_create_worksheets, can_create_groups, etc.


3. UserInformationManager is currently used to retrieve UserInformation objects from the backend.  I'm hoping to replace this aspect of the design and replace it with some general Backend object that can retrieve UserInformation, Worksheets, Groups, etc.

4. Password validation is handled by associating PasswordValidator objects with a PasswordChanger.  I created a function in password_validator.py called install_default_validators that installs what I believe to be a reasonable set of validators (minimum password length of 6, and the password much contain at least 1 letter, number, and symbol).


Personally, I still consider this code a prototype, but I do not believe it will cause any problems if it is integrated into the Notebook.  The next version of the code that I produce will probably have some major design changes based upon what I discovered this time through the code.  That's something for us to look forward to this summer, I suppose :-D
```



---

Attachment


---

Comment by boothby created at 2008-06-18 19:25:37

Resolution: invalid


---

Comment by boothby created at 2008-06-18 19:25:37

-1

Reasons for negative review:

  * Patch bomb.  This patch touches many files in the notebook directory, and many more outside the notebook directory: the bundle itself is trash.  This could be fixed by making a clean patch vs. a current version of the notebook.

  * Opaque.  I'm having a hard time understanding what's going on, since the bundle is so disorganized.  Any changes to the security system *MUST* be completely transparent.

  * Bad?  I don't like what I see.  But that might be because of the bundle, too.

  * Not ready.  I see a lot of TODOs.  Those would need to be resolved.

  * Security.  Frankly, I don't know who Brian Lauber is.  I don't know who he's affiliated with, or what his security experience is.  While he may be trustworthy, I do not trust him for now.  This is not a permanent decision against Brian; I just don't have enough info.
