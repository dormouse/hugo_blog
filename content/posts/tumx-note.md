---
title: "Tmux Note"
date: 2017-02-08 18:35:00
lastmod: 2017-02-08 18:35:00
tags: ["tmux","note"]
categories: ["software"]
slug: "tmux-note"
description: "Note for tmux."
---



Official site: <https://github.com/tmux/tmux>

cheat-sheet
-----------

tmux use prefix key (default: `C-b`)

### General

  Key                            |Description
  ------------------------------ |----------------------------
  :                              |interactive dialog (promt)
  d                              |detach session
  tmux restore                   |restore session
  : source -file \~/.tmux.conf   |reload .tmux.conf
  t                              |big clock
  ?                              |list bindings

### Pane Handling

  Key             |Description
  --------------- |-----------------------------------------
  %               |split vertically
  "               |split horizontally
  o               |go to next pane (down- pane)
  q               |show pane number, press number to go to
  {               |move current pane left
  }               |move current pane right
  x               |kill pane
  &lt;space&gt;   |toggle through layouts
  ;               |last pane
  z               |resize pane
  M-Up            |resize pane up 5 row
  C-Up            |resize pane up 1 row

### Window Handling

  Key                 |Description
  ------------------- |-------------------------------
  c                   |new window
  ,                   |rename window
  n                   |next window
  p                   |previous window
  l                   |previously selected window
  w                   |list all windows
  \[0-9\]             |move to window number \[0-9\]
  f \[window name\]   |find window
  :                   |list-windows list windows
  &                   |kill window
  .                   |move window

### Session handling

  Key                            |Description
  ------------------------------ |-------------------------------------
  tmux                           |start new
  tmux new -s myname             |start new with name
  tmux a -t                      |reattach session (or at, or attach)
  tmux a -t myname               |reattach named session
  tmux ls                        |list sessions
  tmux kill-s ession -t myname   |kill named session
  :new                           |new session
  s                              |list sessions
  \$                             |name session
  tmux kill-s erver              |kill server and all sessions

### customizing tmux

  Key                       |Description
  ------------------------- |----------------------------------------
  set-option -g prefix C-a  |rebind the Ctrl-b prefix to Ctrl-a ; -g |for global =&gt; every window
  bind-key C-a last-window  |switch to last active window; To use hit Ctrl-a twice
  unbind %                  |Remove default split binding
  bind | split-window -h    |bind vertical splitting to |
  bind - split-window -v    |bind vertical splitting to -
  set -g status-bg black    |set status bar bg color to black
  set -g status-fg white    |set status bar fg color to white
  set -g status-left '\#\[fg=green\]\#H'|beginning of statusbar hostname in green
  set -g status-right '\#\[fg=yellow\]\#(uptime | cut -d "," -f 2-)'|number of users and load average for computer
  set-window-o ption -g window-status-current-bg red|current window shown in red
  setw -g monito r-a ctivity on |highlight window with new activity
  set -g visual -ac tivity on   |show info on new activity
  setw -g automatic -rename on  |set window title to current command

Default key bindings
--------------------

The default command key bindings are:

    C-b Send the prefix key (C-b) through to the application.
    C-o Rotate the panes in the current window forwards.
    C-z Suspend the tmux client.
    !  Break the current pane out of the window.
    " Split the current pane into two, top and bottom.
    # List all paste buffers.
    $ Rename the current session.
    % Split the current pane into two, left and right.
    & Kill the current window.
    ' Prompt for a window index to select.
    ( Switch the attached client to the previous session.
    ) Switch the attached client to the next session.
    , Rename the current window.
    - Delete the most recently copied buffer of text.
    .  Prompt for an index to move the current window.
    0 to 9 Select windows 0 to 9.
    : Enter the tmux command prompt.
    ; Move to the previously active pane.
    = Choose which buffer to paste interactively from a list.
    ?  List all key bindings.
    D Choose a client to detach.
    L Switch the attached client back to the last session.
    [ Enter copy mode to copy text or view the history.
    ] Paste the most recently copied buffer of text.
    c Create a new window.
    d Detach the current client.
    f Prompt to search for text in open windows.
    i Display some information about the current window.
    l Move to the previously selected window.
    n Change to the next window.
    o Select the next pane in the current window.
    p Change to the previous window.
    q Briefly display pane indexes.
    r Force redraw of the attached client.
    m Mark the current pane (see select-pane -m).
    M Clear the marked pane.
    s Select a new session for the attached client interactively.
    t Show the time.
    w Choose the current window interactively.
    x Kill the current pane.
    z Toggle zoom state of the current pane.
    { Swap the current pane with the previous pane.
    } Swap the current pane with the next pane.
    ~ Show previous messages from tmux, if any.
    Page Up Enter copy mode and scroll one page up.
    Up, Down Left, Right Change to the pane above, below, to the left, or to the right of the current pane.
    M-1 to M-5 Arrange panes in one of the five preset layouts: even-horizontal, even-vertical, main-horizontal, main-vertical, or tiled.
    Space Arrange the current window in the next preset layout.
    M-n Move to the next window with a bell or activity marker.
    M-o Rotate the panes in the current window backwards.
    M-p Move to the previous window with a bell or activity marker.
    C-Up, C-Down C-Left, C-Right Resize the current pane in steps of one cell.
    M-Up, M-Down M-Left, M-Right Resize the current pane in steps of five cells.

References
----------

-   <https://www.cheatography.com/bechtold/cheat-sheets/tmux-the-terminal-multiplexer/>
-   <http://harttle.com/2015/11/06/tmux-startup.html>

