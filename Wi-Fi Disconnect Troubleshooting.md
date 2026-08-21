---
categories:
  - "[[Processes]]"
type:
description:
source: chatgpt-manual
tags:
created: 2026-08-14
last: 2026-08-14
status:
origin:
run_id:
input_prompt:
---
# Pop!_OS 



**Date:** 2026-08-14  
**Machine:** System76 Pangolin 16  
**OS:** Pop!_OS 22.04 LTS  
**Kernel:** `7.0.11-76070011-generic`  
**Wi-Fi adapter:** MediaTek MT7922 `[14c3:7922]`  
**Kernel driver:** `mt7921e`

## Problem

Wi-Fi periodically disconnects on the Pangolin 16.

Important behavior:

- Problem occurs at home and on other Wi-Fi networks.
    
- On 2026-08-14 it also occurred on `FLPL-Public` at the Fort Lee Public Library.
    
- When the usual failure occurs, Wi-Fi normally **does not recover on its own**.
    
- A reboot or power cycle has normally been required to restore Wi-Fi.
    
- This suggests the problem should not be assumed to be specific to one router or access point.
    

---

# What We Did Today

## 1. Identified the Wi-Fi hardware

`lspci` showed:

```
01:00.0 Network controller: MEDIATEK Corp. Device [14c3:7922]
    Subsystem: AzureWave Device [1a3b:5141]
    Kernel driver in use: mt7921e
    Kernel modules: mt7921e
```

Therefore:

- Adapter = MediaTek MT7922
    
- Driver = `mt7921e`
    

The driver and firmware loaded during boot without an obvious fatal error.

---

## 2. Checked NetworkManager and radio state

NetworkManager was:

```
active (running)
```

Wi-Fi was:

```
connected
```

`rfkill` showed:

```
Wireless LAN
    Soft blocked: no
    Hard blocked: no
```

So Wi-Fi was not disabled by either a software or hardware radio block.

---

## 3. Found Wi-Fi power management enabled

Initial `iwconfig` output showed:

```
Power Management:on
```

NetworkManager configuration showed:

```
/etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
```

containing:

```
[connection]
wifi.powersave = 3
```

`wifi.powersave = 3` enables Wi-Fi power saving.

This became our first controlled troubleshooting change.

---

## 4. Backed up the original configuration

Before changing anything, we created:

```
/etc/NetworkManager/conf.d/default-wifi-powersave-on.conf.bak-20260814
```

The original configuration is therefore recoverable.

---

## 5. Disabled Wi-Fi power saving

Changed:

```
wifi.powersave = 3
```

to:

```
wifi.powersave = 2
```

Current file:

```
/etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
```

Current contents:

```
[connection]
wifi.powersave = 2
```

NetworkManager was restarted.

---

## 6. Verified the change survived reboot

After reboot:

```
Power Management:off
```

NetworkManager configuration still showed:

```
wifi.powersave = 2
```

Therefore the power-management change is active and persistent.

**Leave this setting unchanged for now.**

---

# Wi-Fi Failure Observed at Fort Lee Public Library

We captured a useful failure in the system journal.

The laptop was connected to one `FLPL-Public` access point:

```
5c:df:89:b3:d7:b0
```

It then attempted to authenticate against another access point:

```
5c:df:89:b3:d9:20
```

The kernel reported:

```
disconnect from AP ... for new auth
```

Authentication was attempted three times:

```
send auth ... (try 1/3)
send auth ... (try 2/3)
send auth ... (try 3/3)
```

and then:

```
authentication ... timed out
```

NetworkManager subsequently reported:

```
link timed out
Activation: failed for connection 'FLPL-Public'
```

The laptop later successfully authenticated to the second AP and recovered.

This particular event therefore looks like an **AP roaming/authentication failure**.

However, this does **not** explain the overall problem because similar Wi-Fi failures occur at home and elsewhere, and those failures normally require rebooting the computer.

The laptop remains the common factor.

---

# Current Working Hypotheses

We have **not established the root cause yet**.

Areas still under investigation include:

1. MediaTek MT7922 behavior
    
2. `mt7921e` kernel driver
    
3. MediaTek firmware
    
4. Kernel/driver/firmware interaction
    
5. Authentication or association failures
    
6. Wi-Fi power management
    
7. AP roaming behavior
    
8. DHCP/DNS/routing, if Wi-Fi remains associated during a future failure
    

The library log did **not** show an obvious firmware crash, MCU crash, PCIe failure, or driver reset.

A failure at home that does not recover is therefore particularly important to capture.

---

# IMPORTANT — What To Do When Wi-Fi Fails Again

**DO NOT REBOOT IMMEDIATELY.**

Even without Internet access, the terminal and local filesystem still work.

Open a terminal and run the following commands.

## 1. Record the time

```
date
```

## 2. Check NetworkManager device state

```
nmcli device status
```

## 3. Check Wi-Fi state

```
iwconfig wlp1s0
```

## 4. Capture recent kernel messages

```
sudo dmesg | tail -150
```

## 5. Capture relevant Wi-Fi/driver events

```
sudo journalctl -b --since "15 minutes ago" --no-pager | \
  grep -iE 'mt7921|wlp1s0|firmware|MCU|timeout|reset|failed|disconnect|deauth|PCI'
```

## 6. Save the journal BEFORE rebooting

This is important because the saved file can be examined after Internet access returns.

```
sudo journalctl -b --since "15 minutes ago" --no-pager > ~/wifi-failure.log
```

Verify that the file exists:

```
ls -lh ~/wifi-failure.log
```

## 7. Reboot

After the diagnostic information has been saved:

```
sudo reboot
```

---
results here
[[wifi-failed-b4-reboot]]


# After Reboot

Once Wi-Fi returns, inspect the saved log:

```
less ~/wifi-failure.log
```

The file can then be copied/pasted into ChatGPT for analysis.

Also report:

- Where the failure occurred
    
- Wi-Fi network name
    
- Whether the laptop was stationary
    
- Whether Wi-Fi disappeared completely or merely lost Internet connectivity
    
- Whether turning Wi-Fi off/on was attempted
    
- Whether it recovered without rebooting
    

---

# Pop!_OS Updates

**Temporarily hold off on the currently offered Pop!_OS update.**

This is not because Pop!_OS updates should generally be avoided.

An update may actually contain a newer:

- Linux kernel
    
- `linux-firmware`
    
- MediaTek firmware
    
- System76 package
    
- NetworkManager component
    

that fixes the problem.

However, installing the update now would change the environment before we capture the persistent failure.

The goal is to obtain a **before-update failure baseline** first.

After capturing a hard failure, inspect exactly which packages Pop!_OS wants to update before installing them.

Do **not** indefinitely avoid system updates.

---

# Things NOT To Do Yet

Until another failure has been captured:

- Do not reinstall Pop!_OS.
    
- Do not install random MediaTek drivers.
    
- Do not manually replace firmware.
    
- Do not downgrade the kernel.
    
- Do not change multiple NetworkManager settings.
    
- Do not start changing home router settings.
    
- Do not restore Wi-Fi power saving yet.
    
- Do not install the pending Pop!_OS update yet.
    

The objective is to change **one variable at a time**.

---

# Current System State

At the end of today's troubleshooting:

```
Adapter:          MediaTek MT7922
Driver:           mt7921e
Kernel:           7.0.11-76070011-generic
Wi-Fi power save: OFF
NetworkManager:   Running
rfkill:           Not blocked
```

Persistent NetworkManager configuration:

```
[connection]
wifi.powersave = 2
```

Backup of original configuration:

```
/etc/NetworkManager/conf.d/default-wifi-powersave-on.conf.bak-20260814
```

---

# Next Milestone

The next milestone is **not another configuration change**.

It is:

> Capture the diagnostic state of the Pangolin while Wi-Fi is in its normal unrecoverable failed condition, before rebooting.

That evidence should tell us whether the next investigation should focus on the MT7922 firmware/driver, association/authentication, NetworkManager, or IP networking.


---

Yes — this capture changes the picture in a useful way.

The key event is **suspend/resume**, not ordinary Wi-Fi roaming. Your log shows the machine entering `s2idle`, later resuming, and then the Wi-Fi interface remaining present but disconnected. The interface was still recognized by NetworkManager and the `mt7921e` driver, but it did not reconnect.

Even more interesting, immediately after one resume the Dell USB-C path re-enumerated a USB hub and a Realtek HID device:

```
USB2.1 Hub
Realtek HID Device
```

That strongly supports treating the Dell USB-C monitor connection as part of the suspend/resume scenario we need to test, although it does **not yet prove the monitor causes the Wi-Fi failure**.

Your failure state itself was clear:

```
wlp1s0 wifi disconnected
ESSID:off/any
Access Point: Not-Associated
Power Management:off
```

So disabling Wi-Fi power saving did **not** prevent this failure.

The other significant result is that restarting NetworkManager did not cure it. After the restart, NetworkManager rediscovered `wlp1s0`, identified `mt7921e`, brought the interface from unavailable to disconnected, but it still never associated with your home network. That makes a simple NetworkManager problem less likely.

And your real-world recovery test adds another important clue: **rebooting with the Dell still attached did not restore Wi-Fi, while unplugging USB-C and rebooting did.** I would treat that as a strong correlation worth reproducing before we declare causation.

There is also prior history of MT7922 Linux connectivity problems with the `mt7921e` driver, including Pop!_OS reports involving authentication problems, although the older issue I found focused on 5 GHz rather than your exact suspend/USB-C scenario. ([GitHub](https://github.com/pop-os/linux-firmware/issues/47?utm_source=chatgpt.com "Mediatek MT7922 wireless adapter 5GHz connectivity issue")) Your MT7922 is indeed a device supported by the Linux `mt7921e` driver. ([Cateee](https://cateee.net/lkddb/web-lkddb/MT7921E.html?utm_source=chatgpt.com "CONFIG_MT7921E: MediaTek MT7921E (PCIe) support"))

### What I want to do next if wifi is dead again

For now, **do not install the pending OS update yet**. We finally have a reproducible-looking pre-update failure mode, so this is a good point to run one controlled experiment.

Use the machine normally with the Dell attached. Before walking away long enough for it to sleep, confirm:

```
nmcli device status
```

When you return, if Wi-Fi is dead again, **do not reboot initially**. Run:

```
date

nmcli device status

iwconfig wlp1s0
```

Then try the driver reload that we didn't get to test during this failure:

```
sudo modprobe -r mt7921e
sudo modprobe mt7921e
```

Wait about 15 seconds, then:

```
nmcli device status
```

If that restores Wi-Fi, that strongly implicates the MT7922/`mt7921e` suspend-resume state.

If it **does not** restore Wi-Fi, then unplug only the Dell USB-C cable — **without rebooting** — wait about 30 seconds and run:

```
nmcli device status
```

That is the experiment I most want now. We need to distinguish:

- driver reload fixes it;
    
- unplugging Dell fixes it;
    
- neither fixes it and only a reboot with Dell unplugged fixes it.
    

Those are three substantially different diagnoses.

One thing I would **not** do yet is replace drivers, change kernel parameters, or start disabling PCIe power management. We now have evidence that the failure lines up with suspend/resume, and possibly USB-C state, so we can test that directly instead of making speculative system changes.

Also, keep the `wifi.powersave = 2` setting. It didn't solve this failure, but there's no reason yet to undo it.

I would update your Obsidian note with one new headline finding:

> **2026-08-14 home failure:** Wi-Fi failed after `s2idle` suspend/resume while Dell S3425DW was attached by USB-C. NetworkManager restart did not restore association. Reboot with Dell attached still had no Wi-Fi; unplugging Dell and rebooting restored Wi-Fi. Root cause not yet proven; next test is `mt7921e` reload followed by USB-C unplug without reboot.

This is considerably better evidence than where we were this morning.