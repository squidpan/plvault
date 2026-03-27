---
categories:
  - "[[Installs]]"
rating:
created: 2026-03-26
last: 2026-03-26
topics:
apps: "[[Google Chrome]]"
title: clean uninstall of flatpak google chrome and reinstall using .deb package using apt for ubuntu
tags:
  - install
---
# Summary

Google Chrome extension, HoverNotes, fails to save file in the designated folder.
Flatpak version of Google Chrome is a sandbox that restricts its access to your personal files. I tried to terminal command to grant permissions but did not work:

>[!Info]
>flatpak override --user --filesystem=home com.google.Chrome

I will reinstall Chrome using .deb package downloaded from Chrome website

# Prerequisites

# Steps

1. Uninstall Google Chrome initially that was initially installed using flatpak

```code
#Uninstall application
flatpak uninstall com.google.Chrome

#(Optional) Remove Application Data
flatpak uninstall --delete-data com.google.Chrome

#Cleanup unused dependencies
flatpak uninstall --unused

```

2. Download Google Chrome for Linux (e.g google-chrome-stable_current_amd64.deb)
3. move it to /home/pl/pjs/software so I can keep track of sw I installed
4. install the package:
```code
sudo apt install ./google-chrome-stable_current_amd64.deb
```





