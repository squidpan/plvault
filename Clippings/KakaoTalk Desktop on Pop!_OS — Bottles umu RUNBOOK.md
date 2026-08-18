---
categories:
  - "[[Clippings]]"
title: "income generation using laptop AI Kakaotalk etc"
source: "https://chatgpt.com/g/g-p-6a83487d47fc8191a629f148ceefa48a-income-generation-using-laptop-ai-kakaotalk-etc/c/6a83488c-429c-83ea-8b75-6b7a4c8f584a"
author:
published:
created: 2026-08-17
description: "Use ChatGPT to answer questions, write, create images, complete work, and code—all in one place. Get started for free or download the app."
tags:
  - "chatgpt/conversation"
---
Absolutely. Below is the version I'd put directly into Obsidian. It documents **what actually worked today**, including the failure/recovery behavior we observed rather than pretending this is a normal native Linux installation.

# KakaoTalk Desktop on Pop!_OS — Bottles/UMU Runbook

**Status:** Working and tested  
**Last tested:** 2026-08-17  
**Platform:** Pop!_OS 22.04 LTS  
**Application:** KakaoTalk for Windows  
**Compatibility environment:** Bottles + UMU/Proton  
**Purpose:** Run KakaoTalk Desktop on Linux and access Korean KakaoTalk Open Chat rooms and downloadable materials.

---

## 1. Working State

KakaoTalk Desktop is successfully running on Pop!_OS even though KakaoTalk does not provide a native Linux desktop client.

The working stack is:

**Pop!_OS → Bottles → UMU → Proton/Wine → Windows KakaoTalk**

The Bottles Library contains a launcher named:

**KakaoTalk**

with environment shown as:

**UMU / Game**

KakaoTalk authentication has been completed and persists between launches.

The desktop client successfully displays:

- Friends
    
- Chats
    
- Existing conversations
    
- KakaoTalk Open Chat rooms
    
- Open Chat announcements/messages
    
- Account/profile information
    

The Open Chat room tested successfully was:

**[무료 특강29] AI 블로그로 온라인 건물주 되기**

The room remained available after completely quitting KakaoTalk and launching it again.

---

# 2. Normal Startup Procedure

## Step 1 — Start Bottles

Open **Bottles** from Pop!_OS.

Select the **Library** tab.

The KakaoTalk launcher should appear as a card labeled:

**KakaoTalk — UMU / Game**

## Step 2 — Launch KakaoTalk

Click:

**Launch**

Wait for the KakaoTalk window to appear.

Do **not repeatedly click Launch** if KakaoTalk doesn't immediately appear.

UMU/Proton startup can take some time.

## Step 3 — Verify Login

The KakaoTalk **Friends** window should appear.

A new login should normally **not** be required.

The existing KakaoTalk account and authentication should persist inside the Bottles/UMU prefix.

## Step 4 — Open Chats

Click the **speech-bubble/chat icon** on the left side of KakaoTalk.

The Chats screen should appear.

The joined Open Chat should appear in the chat list.

For the initial test this included:

**[무료 특강29] AI 블로그로 온라인 건물주 되기**

Click the room to open it.

---

# 3. Important: Closing a Window Is NOT Necessarily Quitting KakaoTalk

This was the most important operational lesson discovered during testing.

Clicking the **X** on a KakaoTalk window can make the desktop interface disappear while the KakaoTalk/Proton/Wine environment remains alive.

Therefore:

> **A missing KakaoTalk window does not necessarily mean KakaoTalk has stopped.**

This caused confusion during testing because KakaoTalk appeared to be gone while its processes were still running.

Attempting to launch KakaoTalk again while the first instance was still alive also produced abnormal behavior.

---

# 4. Correct Shutdown Procedure

Whenever possible, quit KakaoTalk from KakaoTalk itself rather than simply closing its window.

From the main KakaoTalk window:

**Gear icon → Quit**

The gear icon is located near the lower-left corner.

The menu contains options including:

- Settings
    
- Lock
    
- Log out
    
- **Quit**
    

Choose:

**Quit**

Do **not** choose **Log out** for normal shutdown.

Logging out could require authentication again later.

---

# 5. Verify KakaoTalk Really Stopped

After choosing **Quit**, run this in a terminal:

```
ps aux | grep -Ei 'KakaoTalk|umu|proton|wine' | grep -v grep
```

A successful complete shutdown should return **nothing**.

Example:

```
[PL] pl@pop-os:~ $ ps aux | grep -Ei 'KakaoTalk|umu|proton|wine' | grep -v grep
[PL] pl@pop-os:~ $
```

This is the known-good stopped state.

Bottles should also return to displaying:

**Launch**

instead of its running/stop control.

---

# 6. Known Hidden-Window Problem

During testing, KakaoTalk entered an unusual state:

- KakaoTalk processes were running.
    
- Bottles indicated that KakaoTalk was running.
    
- No usable KakaoTalk window could initially be found.
    
- KakaoTalk did **not appear in Alt+Tab**.
    
- Launching KakaoTalk again created another UMU/Proton launch attempt.
    
- Multiple related processes were visible.
    

The process list included items such as:

- `umu-run`
    
- `umu-shim`
    
- `proton`
    
- `wineserver`
    
- `winedevice.exe`
    
- `xalia.exe`
    
- `KakaoTalk.exe`
    

This is therefore a compatibility/window-management issue to remember.

It does **not** mean the KakaoTalk installation has been lost.

---

# 7. Diagnosing a Missing KakaoTalk Window

If KakaoTalk appears to disappear, **do not immediately launch another copy**.

First run:

```
ps aux | grep -Ei 'KakaoTalk|umu|proton|wine' | grep -v grep
```

### Result A — No output

KakaoTalk is actually stopped.

Return to Bottles and use:

**Library → KakaoTalk → Launch**

### Result B — Processes appear

KakaoTalk or its compatibility environment is still running.

Do **not** repeatedly press Launch.

First try locating the existing window through:

- Pop!_OS workspace overview
    
- Alt+Tab
    
- Other workspaces
    
- Windows hidden behind Chrome, Tilix or Bottles
    

Remember that during our testing KakaoTalk was once running **without appearing in Alt+Tab**.

---

# 8. Recovery From a Stuck/Hidden KakaoTalk Instance

During testing, we encountered an instance where the KakaoTalk process existed but its UI could not be found.

The KakaoTalk process was identified from:

```
ps aux | grep -Ei 'KakaoTalk|umu|proton|wine' | grep -v grep
```

The relevant process looked similar to:

```
C:\Program Files\Kakao\KakaoTalk\KakaoTalk.exe
```

Killing the problematic KakaoTalk process caused the existing KakaoTalk UI to become visible again.

This demonstrated that multiple/overlapping compatibility-process states can occur.

### Recovery rule

Prefer this sequence:

1. Determine whether KakaoTalk is already running.
    
2. Try to recover/find its existing window.
    
3. Avoid launching repeated copies.
    
4. Use KakaoTalk's own **Quit** command once the UI becomes available.
    
5. Verify that all related processes have stopped.
    
6. Only then launch KakaoTalk again from Bottles.
    

Direct process killing should be considered a **recovery procedure**, not the normal shutdown procedure.

---

# 9. Joining a KakaoTalk Open Chat From Linux

This required a workaround because the Kakao Open Chat website could not directly invoke the Windows KakaoTalk client running inside Bottles.

The Open Chat webpage offered four choices:

1. **Copy Link**
    
2. **Send Link to Mobile KakaoTalk**
    
3. **View QR Code**
    
4. **Install KakaoTalk for PC**
    

The original Open Chat URL was:

`https://open.kakao.com/o/gXYliFIi`

### What did NOT work

Clicking:

**Join Group Chat**

from Chrome caused Linux to invoke `xdg-open`.

Pop!_OS then displayed:

**No Apps available**

This happened because Linux did not have a registered native application capable of handling the KakaoTalk-specific link/protocol.

KakaoTalk exists inside Bottles/Proton rather than as a normal Linux KakaoTalk application.

Therefore the browser could not automatically hand the link to KakaoTalk Desktop.

This is expected with the current setup.

---

# 10. Working Method — QR Code + iPhone

The successful workaround was:

On the Kakao Open Chat webpage, click:

**View QR Code**

A QR code appears.

Use the iPhone to scan that QR code.

The iPhone opens the corresponding room through the native KakaoTalk mobile application.

KakaoTalk then displayed the Open Chat profile-selection interface.

An existing Kakao/Open Chat profile was selected.

The iPhone subsequently displayed:

**Welcome to '[무료 특강29] AI 블로그로 온라인 건물주 되기'**

This confirmed that the account had joined the room.

---

# 11. What Happens on the Desktop After Joining on iPhone

The QR code does **not** cause the webpage itself to transform into the desktop KakaoTalk room.

Instead, joining happens through the KakaoTalk account.

Once the account joins the room on the iPhone, the membership synchronizes through KakaoTalk.

On the desktop:

1. Open KakaoTalk.
    
2. Select **Chats**.
    
3. Locate the new Open Chat.
    
4. Click it.
    

The room then opens normally in KakaoTalk Desktop.

This was successfully tested.

---

# 12. QR Code Is Primarily Needed for Joining

Once the Open Chat has been joined successfully, it becomes part of the KakaoTalk account's chat list.

Therefore normal future use should be:

**Bottles → Launch KakaoTalk → Chats → Open Chat**

There should be no reason to:

- reopen the invitation webpage,
    
- rescan the QR code,
    
- reinstall KakaoTalk,
    
- or repeat the Open Chat joining procedure.
    

The QR/iPhone procedure is primarily a workaround for **joining a new Open Chat from Linux**.

---

# 13. Authentication

KakaoTalk Desktop authentication was successfully completed earlier using the mobile KakaoTalk account/device authorization process.

After quitting KakaoTalk completely and relaunching it:

**The account remained logged in.**

Therefore normal operation does not require repeating device authentication every time.

Avoid selecting:

**Log out**

unless intentionally removing the desktop login.

Use:

**Quit**

for normal shutdown.

---

# 14. Pop!_OS Window/Tiling Behavior

The workstation uses a Dell 34-inch ultrawide monitor.

Pop!_OS tiling is enabled and Chrome and Tilix behave normally when tiled side-by-side:

- resizing one changes the neighboring window,
    
- the two windows share the available tiled space.
    

KakaoTalk under Wine/Proton behaves differently.

KakaoTalk creates relatively narrow Windows-style windows, including separate windows for:

- main Friends/Chats interface,
    
- individual chat room,
    
- announcement/details view.
    

These do not integrate with Pop!_OS tiling as cleanly as native Linux applications.

The workspace overview confirmed that Chrome, Tilix and KakaoTalk can all exist in the same workspace even when KakaoTalk is obscured.

### Current decision

**Do not modify the tiling configuration just to accommodate KakaoTalk.**

The application is currently usable.

Window-layout optimization can be revisited later if it becomes a significant inconvenience.

---

# 15. Known-Good Functional Test

The following end-to-end test has been completed successfully.

|Test|Result|
|---|---|
|Launch KakaoTalk through Bottles|PASS|
|KakaoTalk desktop UI appears|PASS|
|Existing account remains authenticated|PASS|
|Friends list loads|PASS|
|Chats list loads|PASS|
|Joined Open Chat appears|PASS|
|Open Chat room opens|PASS|
|Room messages/announcements display|PASS|
|Administrator details/announcement opens|PASS|
|iPhone QR method joins new Open Chat|PASS|
|Mobile membership synchronizes to desktop|PASS|
|Quit through KakaoTalk menu|PASS|
|KakaoTalk processes terminate|PASS|
|UMU/Proton/Wine processes terminate|PASS|
|Relaunch after clean shutdown|PASS|
|Login persists after relaunch|PASS|
|Open Chat persists after relaunch|PASS|

**Overall result: PASS**

---

# 16. Daily Operating Procedure

For normal daily use:

### Start

**Bottles → Library → KakaoTalk → Launch**

Then:

**KakaoTalk → Chats**

### Use

Read/open KakaoTalk conversations and Open Chat rooms normally.

### Stop

**KakaoTalk gear icon → Quit**

If there is any doubt about whether it actually stopped:

```
ps aux | grep -Ei 'KakaoTalk|umu|proton|wine' | grep -v grep
```

No output means the environment has shut down.

---

# 17. Joining Future Open Chats

If another Kakao Open Chat web invitation fails to open directly from Chrome:

**Do not troubleshoot `xdg-open` immediately.**

Use the proven method:

**Open Chat webpage → View QR Code → scan with iPhone → join in mobile KakaoTalk → return to desktop KakaoTalk → Chats**

This bypasses the Linux-to-Windows protocol-handler problem entirely.

---

# 18. Configuration Change Policy

The current installation is **working**.

Therefore:

> **Do not upgrade, reconfigure, change runners, change Proton versions, reinstall KakaoTalk, or modify Bottles settings merely to improve something that is already functional.**

In particular, don't attempt to "fix" the browser's inability to launch KakaoTalk links unless that capability later becomes genuinely important.

The QR/mobile workaround is simple and proven.

If something breaks later, first determine whether the failure is:

**KakaoTalk → Wine/Proton → UMU → Bottles → Pop!_OS/window manager → network**

before changing the working configuration.

---

# 19. Current Bottles/Compatibility Information Observed

The working process paths showed the Bottles environment using:

**Runner:**

`protosoda-11.0-1`

**KakaoTalk executable:**

`C:\Program Files\Kakao\KakaoTalk\KakaoTalk.exe`

The underlying prefix observed during troubleshooting was under:

`~/.var/app/com.usebottles.bottles/data/bottles/umu/prefixes/`

with KakaoTalk installed inside its Windows `drive_c`.

These details are worth retaining because they can help identify the correct environment if Bottles configuration or recovery is needed later.

---

# 20. Troubleshooting Quick Reference

|Symptom|First action|
|---|---|
|KakaoTalk won't appear|Check processes before launching again|
|KakaoTalk missing from Alt+Tab|Check workspace overview and process list|
|Bottles indicates KakaoTalk is running|Do not repeatedly click Launch|
|Browser says “No Apps available”|Use Open Chat QR code + iPhone|
|Open Chat isn't on desktop|Confirm it was joined on iPhone, then check Chats|
|KakaoTalk window was closed accidentally|Determine whether process is still running|
|Want to shut down normally|Gear → Quit|
|Want to confirm shutdown|Run `ps` diagnostic|
|Strange behavior after multiple launches|Cleanly terminate existing instance before relaunching|
|Everything works|**Don't change anything**|

---

# 21. Why This Setup Exists

The purpose of installing KakaoTalk Desktop was not simply to experiment with running Windows applications on Linux.

It was needed to access Korean KakaoTalk material related to an online income/business course.

The first Open Chat under investigation is:

**[무료 특강29] AI 블로그로 온라인 건물주 되기**

Roughly:

**"[Free Special Lecture 29] Become an Online Landlord with an AI Blog"**

The visible course announcement references topics including:

- AdSense
    
- AI-generated content
    
- online building/project concept
    
- approximately 10 minutes per day
    
- beginner AdSense setup
    
- using AI to automate content creation
    
- SEO/search exposure
    
- external traffic
    
- monetization
    
- examples of actual earnings
    
- a free starter/secret PDF or related material
    

These are **claims/topics from the promotional material**, not conclusions about whether the business model works.

The next phase is therefore to collect and analyze the actual starter materials rather than relying on the promotional claims.

---

# 22. Next Phase — Income Model Investigation

The KakaoTalk/Linux installation is now infrastructure.

The actual investigation should answer five questions:

1. **What exactly is this person doing to make money?**
    
2. **Is the business model legitimate?**
    
3. **Does the evidence suggest that it is realistically promising rather than merely promotional?**
    
4. **Can the model be operated from New Jersey/the United States, or does it depend upon Korean platforms, audiences, advertisers, payment systems, residency, language, or market conditions?**
    
5. **If the Korean implementation does not transfer directly, what equivalent U.S. model could be built using a laptop, AI and the user's existing technical/business-analysis skills?**
    

The evaluation should distinguish carefully between:

**the underlying business model**

and

**the course being sold to teach the business model.**

A legitimate underlying activity—such as content publishing and advertising—does not automatically mean the instructor's income claims, course, automation strategy, or promised returns are sound.

Likewise, a Korea-specific implementation may contain techniques that can be adapted to a U.S. market even if the exact Korean workflow cannot.

**KakaoTalk setup phase: COMPLETE.**