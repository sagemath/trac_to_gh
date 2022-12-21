# Issue 4551: notebook -- implement Notebook Settings page with email system on/off setting

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-11-19 17:35:01

Assignee: boothby

CC:  wjp timdumol was

Depends on #4550


---

Attachment


---

Attachment

Depends on #4135


---

Attachment

first two patches folded into one, rebased on 4.1.2.alpha0 + #4550


---

Attachment

Rebased for sagenb #6983 + #7110 (including #5447) + #7158 + #4550.


---

Comment by mpatel created at 2009-10-10 07:28:20

I'm working on adding other server settings to the "Notebook Settings" page.


---

Attachment

SageNB: settings page for all server options.  Depends on #7110, #7158.  Apply only this patch.


---

Comment by mpatel created at 2009-10-10 13:29:40

The [attachment:trac_4551-settings_page_v2.patch new version], based on #6983's revision 72, #7110, and #7158, can display and update all server settings.

With some extra work, we can do the same for user settings, including custom key bindings, for example.

Feel free to suggest changes.  Potential "To do" list items:

 * Use templates.
 * Check for errors.
 * "Reset to defaults" option.
 * "Revert to earlier configuration" option.  This should be straightforward to implement, if we use a versioning system for the `.conf` files.
 * Combine the `defaults` and `defaults_descriptions` dictionaries.
 * Remove unused settings.
 * Use a color picker for color settings.
 * User settings, including key bindings, CSS, etc.


---

Comment by mpatel created at 2009-10-12 18:41:39

Reminder: Rebase against the outcomes of #7196, #7158, if the new changes are worthwhile.


---

Attachment

Now uses Farbtastic as a color chooser.  Rebased against #7196 + #7158 v2.  Apply only this patch.


---

Comment by mpatel created at 2009-10-14 11:06:25

Patch v3:

 * Uses [Farbtastic](http://acko.net/dev/farbtastic) for color settings.
 * Updates the `descriptions_defaults` dictionary.
 * Adds a `T_LIST` type.
 * Changes `'email'`'s type back to `T_BOOL`.

Remarks:

 * It would be simpler (and more consistent?) to use `[]` instead of `None` for an empty `server_poll` setting.
 * Install the more compact [jPicker](http://www.digitalmagicpro.com/jPicker/).  Use it for `interact`s, too?


---

Comment by was created at 2009-10-17 07:01:34

Looks AWESOME!  Strong positive review (despite some missing doctests, which is OK at this stage since this isn't part of the Sage library).   Very very good.  This adds a huge amount of much needed functionality!


---

Comment by was created at 2009-10-17 07:01:34

Resolution: fixed
