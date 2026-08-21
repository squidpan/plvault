---
categories:
  - "[[Clippings]]"
title: "I Scanned My Own Wi-Fi Like a Hacker. Here’s What I Found."
source: "https://medium.com/@SatyamPathania/i-scanned-my-own-wi-fi-like-a-hacker-heres-what-i-found-9e20f90cefd1"
author:
  - "[[Satyam Pathania]]"
published: 2026-08-08
created: 2026-08-18
description: "I thought my home network was secure. Then I stopped looking at it like a normal user"
tags:
  - "clippings"
url: "https://medium.com/@SatyamPathania/i-scanned-my-own-wi-fi-like-a-hacker-heres-what-i-found-9e20f90cefd1"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*RREvERDgvDED9Vho6ty5tw.png)

credit — gemini

## I thought my home network was secure. Then I stopped looking at it like a normal user

[FREE ACCESS](https://medium.com/@SatyamPathania/i-scanned-my-own-wi-fi-like-a-hacker-heres-what-i-found-9e20f90cefd1?sk=4e1657ea6e7002de81e9790685e806b4)

I used to think securing a home network was pretty straightforward.

Get a decent router, set a strong Wi-Fi password, enable WPA2 or WPA3, and you’re probably fine.

At least, that’s what I thought.

Then I started learning cybersecurity properly and realized I had been looking at my network completely wrong. I was thinking about security from the perspective of someone using the network, while an attacker would be looking at something very different: devices, open ports, services, firmware, authentication, exposed interfaces and everything else that shouldn’t necessarily be there.

So one day, I decided to stop treating my home network like a normal person.

I opened my terminal.

And started looking.

**Before anyone gets creative:** everything in this article is about my own network and controlled testing. Don’t scan someone else’s network just because their Wi-Fi name looks suspicious. That’s not research. That’s just asking for problems.

## Who Am I?

I’m **Satyam Pathania**, a self-taught cybersecurity researcher, technical writer, builder and hardware nerd.

I’ve spent the last few years learning cybersecurity through labs, projects, offensive security, Linux, networking, hardware and a lot of breaking things that I was actually allowed to break.

I’ve also written extensively about cybersecurity and practical hacking because I learned a lot of this stuff the hard way.

I don’t really enjoy writing about security as if everything happens inside a perfect corporate lab.

Real systems are messy.

People forget passwords. Developers leave services running. Routers don’t get updated. Someone installs a random IoT device and forgets it exists six months later.

And that’s exactly why I wanted to look at my own network.

## The Wi-Fi Password Wasn’t the Problem

When most people hear “Wi-Fi security,” they immediately think about the password.

*Is it long enough?*

*Is it unique?*

*Does it contain someone’s birthday?*

Is it `password123`?

**We have all seen that one network.**

But your Wi-Fi password is only one part of your network security.

The router itself is a small computer. It has firmware, management interfaces, services, configuration options and, depending on the device, features such as UPnP, WPS, remote administration and port forwarding.

Then there are all the devices connected behind it.

> Your laptop.
> 
> Your phone.
> 
> Your television.
> 
> Your printer.
> 
> Your smart speaker.
> 
> Your Raspberry Pi.
> 
> Your IoT devices.

And that random development board you connected to the network three months ago and completely forgot about.

That last one is probably mine.

This is where the concept of an **attack surface** becomes important.

An attack surface isn’t simply “the thing an attacker can hack.” It’s the collection of systems, services, interfaces and entry points that could potentially be abused.

Once I started thinking about my home network that way, the question changed.

***I wasn’t asking:***

> *“Is my Wi-Fi password strong?”*

### I was asking:

> ***“What exactly have I connected to the internet?”***

And that’s a much better question

## First, I Wanted to Know What Was Actually Connected

Before looking for vulnerabilities, I wanted to understand the network itself.

This is one of those things beginners often skip because it doesn’t feel as exciting as running an exploit.

But reconnaissance is one of the most important parts of penetration testing.

You can’t properly secure something you don’t understand.

On a network you own, tools such as Nmap can help identify active hosts. For example, a basic host discovery scan might look like:

```c
nmap -sn 192.168.1.0/24
```

**Your actual subnet may be different, so don’t blindly copy the address above.**

> The important thing isn’t the command itself.
> 
> It’s what the command is trying to answer.

**Which devices appear to be alive on my network?**

Suddenly, the network stops being an abstract thing called “Wi-Fi.”

It becomes a list of actual machines.

And that list can be surprisingly long.

You might recognize everything immediately.

### Or you might see something and think:

***“Wait… what is that?”***

That moment is more valuable than it sounds.

**An unknown device isn’t automatically malicious. It could be a phone, printer, TV, access point or something else you simply forgot about.**

But from a security perspective, unknown assets deserve investigation.

## Then I Started Looking at Open Ports

Finding devices was only the first step.

Next came services.

A device can have different services listening on different network ports. You might encounter things such as SSH, HTTP, HTTPS, DNS or SMB depending on the system.

For example, you might see:

```c
22    SSH
80    HTTP
443   HTTPS
53    DNS
445   SMB
```

But here’s something important that I wish more beginners understood.

**An open port does not automatically mean you’ve found a vulnerability.**

It simply means something is listening.

That’s it.

Think about it like walking around a building and finding a door.

Finding the door doesn’t mean you’ve broken into the building.

You now have another question to answer.

> **Why is the door there?**
> 
> **Who is supposed to use it?**
> 
> **Is authentication enabled?**
> 
> **Is the software behind it updated?**
> 
> **Should the service be exposed at all?**

That’s the difference between randomly running tools and actually performing security reconnaissance.

The goal isn’t to collect screenshots of open ports.

The goal is to understand the system.

## Then I Looked at the Router

This was probably the part I found most interesting.

**People spend a lot of time worrying about their wireless password, but the router’s administrative interface often gets forgotten.**

**And that’s a completely different security boundary.**

**Your Wi-Fi credentials allow you to connect to the wireless network.**

**Your router’s administrator credentials allow someone to control the device managing that network.**

That distinction matters.

The router can control things like firewall rules, DNS settings, wireless configuration, port forwarding and other network-level settings.

So I started reviewing the router configuration with a different mindset.

> Was remote administration enabled?
> 
> Was WPS enabled?
> 
> Was UPnP enabled?
> 
> Were there unnecessary port-forwarding rules?
> 
> Was the firmware current?
> 
> Were the administrative credentials unique?

None of these settings automatically mean “your router is hacked.”

Security rarely works like that.

Instead, they represent decisions that affect the overall attack surface.

The problem is that many people configure their router once and never look at it again.

## The “Set It and Forget It” Problem

Your router is probably one of the most important devices in your house.

Yet most people treat it like an appliance.

You install it.

You configure the Wi-Fi.

Everything works.

Then you forget about it.

Meanwhile, security researchers continue discovering vulnerabilities, vendors release firmware updates, and old devices slowly become harder to maintain.

> Your laptop tells you when Windows needs an update.
> 
> Your browser tells you when Chrome needs an update.
> 
> Your phone practically begs you to install iOS or Android updates.

### Your router is sitting in the corner silently thinking:

***“Don’t worry, I’ll keep running this firmware from 2021.”***

That isn’t necessarily a joke.

Outdated firmware can leave known vulnerabilities unpatched, which is why firmware updates are an important part of basic router security.

It’s one of the least exciting security tasks you can do.

It’s also one of the easiest.

## Then There Was IoT

This is where my interest in hardware and IoT security really started making sense.

> **A laptop is obviously a computer.**
> 
> **An IoT device often doesn’t feel like one.**
> 
> **That’s the problem.**

A smart plug, camera, speaker, development board or other connected device can have firmware, network services, credentials, APIs and communication with other systems.

The fact that something costs $10 doesn’t mean it has no security implications.

If it connects to your network, it becomes part of your network’s security model.

This doesn’t mean you should throw every smart device in your house into the trash.

It means you should know what those devices are doing.

I like asking a simple question:

**“If this device were compromised, what could it reach?”**

That’s a much more useful security question than simply asking whether the device itself is secure.

## The Biggest Mistake Beginners Make

When people start learning ethical hacking, there’s a temptation to immediately search for exploits.

I understand it…..

You install Kali Linux, open Nmap, launch Burp Suite, watch a few videos and suddenly you’re ready to become the next legendary hacker who takes down the internet from a coffee shop.

Except real security research doesn’t work like that.

The boring part matters.

**Reconnaissance comes before exploitation.**

You need to understand the environment before you can meaningfully assess it.

On my own network, that meant identifying devices, understanding their purpose, reviewing exposed services, checking configurations and thinking about how those components interact.

Only after you understand the system does a vulnerability become meaningful.

A port isn’t interesting because it’s open.

It’s interesting because **something is listening behind it, and you now have a reason to ask why.**

## What I Would Check on My Own Network

After going through the network from an attacker’s perspective, there are several basic things I’d recommend checking on any home network you control.

Start by looking at the devices connected to your router and investigate anything you don’t recognize. Review the router’s administrator account separately from your Wi-Fi password and make sure both use strong, unique credentials.

Check whether your router has firmware updates available. Review settings such as remote administration, WPS, UPnP and port forwarding, and disable anything you don’t actually need.

If you have IoT devices, consider putting less-trusted devices on a separate guest or IoT network where practical. The goal is to reduce unnecessary communication between devices rather than assuming every device deserves unrestricted access to everything else.

And finally, don’t confuse “nothing bad has happened yet” with security.

That’s not security.

That’s luck.

## The Lesson Wasn’t Really About Wi-Fi

After spending time looking at my own network this way, I realized the biggest lesson wasn’t about Nmap or router configuration.

It was about perspective.

As a normal user, I saw a Wi-Fi network.

As a security researcher, I saw an attack surface.

I saw devices, services, trust relationships, configurations and potential entry points.

That shift in perspective is one of the most important things you can develop when learning cybersecurity.

> *Tools matter.*
> 
> *Commands matter.*
> 
> *Knowing how Nmap works matters.*

But eventually, you have to move beyond memorizing commands and start understanding **why you’re running them in the first place**.

Because knowing 200 security tools doesn’t automatically make you good at security.

Knowing what question you are trying to answer does.

## If You’re Learning Cybersecurity, Start With What You Own

You don’t need a $5,000 lab to start learning network security.

You can build a controlled home lab with virtual machines, a spare router, an old computer or inexpensive hardware. You can experiment with network discovery, traffic analysis, Linux, vulnerable applications and defensive configurations without touching systems that don’t belong to you.

That’s how I learned a lot of what I know.

I started with whatever hardware I could get my hands on, built things, broke things, fixed them and wrote about what I learned.

You don’t need to know everything before you start.

You just need something you’re allowed to test and enough curiosity to ask:

> ***“Okay, but what happens if I actually look?”***

That question has probably taught me more about cybersecurity than any single course ever did.

## Want Cybersecurity Content That Doesn’t Read Like a Corporate Brochure?

I’m **Satyam Pathania**, a self-taught cybersecurity researcher, technical writer and builder working across cybersecurity, hardware, IoT and emerging security technologies.

I work with cybersecurity startups, security platforms and technology brands on technical articles, product-led content, research-driven writing, educational content, security explainers and longer-term content partnerships.

If you’re building a cybersecurity product and have a great technical team but your content still sounds like it was written by a marketing committee, that’s exactly the kind of problem I like solving.

For collaborations and writing work:

**Email:** satyampathania14@gmail.com  
**Handle:** 0xdiddy

## Buy Me a Coffee

If this article helped you understand your home network a little differently, consider supporting my work.

**Buy Me a Coffee:**  
[*https://www.buymeacoffee.com/satyampathaniad*](https://buymeacoffee.com/satyampathania)

Your support helps me keep buying hardware, building security labs, testing weird devices and turning the results into free cybersecurity content.

And if coffee isn’t your thing, sharing the article with someone who still has `admin/admin` sitting somewhere on their network is also a pretty good contribution.

Wi-Fi security, home network security, network security, router security, ethical hacking, cybersecurity for beginners, Nmap tutorial, network scanning, penetration testing, wireless security, IoT security, cybersecurity home lab, Linux cybersecurity, network reconnaissance, router vulnerabilities.

## Medium Tags

**Cybersecurity · Hacking · Network Security · WiFi Hacking · Ethical Hacking**