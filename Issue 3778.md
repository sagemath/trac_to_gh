# Issue 3778: [with patch, do not review] part 1 of new configuration system

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-08-05 23:27:01

Assignee: boothby

(1) Centralized dictionary of the configurable settings with object oriented interface
(2) CurrentConfig class will have process_runtime method taking the arguments at runtime and updating the current configuration
(3) run_notebook.py will use current_config.value(SETTING) to retrieve current configuration for each setting needed at run_time
(4) NotebookObject's __doc__ wil be dynamically created




---

Attachment


---

Comment by was created at 2009-11-19 23:31:34

This has bitrotted beyond repair.


---

Comment by was created at 2009-11-19 23:31:34

Resolution: invalid
