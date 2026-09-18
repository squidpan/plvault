---
categories:
  - "[[Topics]]"
  - "[[Jobs]]"
url:
created:
last:
type:
tags:
  - nutshell
---
give me examples of using sftp commands to login to remote sftp server, list remote files, show list of local files and put command to place local files on remote server and download remote files locally. Also is there a command to check disk space on remote sftp server.

Great—this is very practical and exactly the kind of thing they might expect you to **know at a working level**.

I’ll walk you through **real SFTP usage step-by-step**, with commands + what to say in an SRE context.

---

# 🔐 1. Login to a remote SFTP server

sftp username@remote_host

### Example:

sftp john@192.168.1.10

👉 You’ll be prompted for a password (or use SSH key)

### After login, you’ll see:

sftp>

---

# 📂 2. List remote files (on server)

ls

### Example:

sftp> ls  
logs/   data.csv   config.json

👉 Shows files on the **remote server**

---

# 💻 3. Show local files (your machine)

lls

### Example:

sftp> lls  
app.log   test.txt

👉 “l” = local

---

# 📤 4. Upload file (local → remote)

put local_file

### Example:

sftp> put app.log

👉 Uploads `app.log` to remote server

---

## Upload to specific remote directory

put app.log /remote/logs/

---

# 📥 5. Download file (remote → local)

get remote_file

### Example:

sftp> get data.csv

👉 Downloads file to your local machine

---

## Download to specific local directory

get data.csv /local/downloads/

---

# 📁 6. Change directories

## Remote:

cd /remote/path

## Local:

lcd /local/path

---

# 💾 7. Check disk space on remote server

👉 **Yes—but not directly with `df` inside SFTP**

### Option 1 (inside SFTP — limited)

df -h

⚠️ Not always supported depending on server

---

### Option 2 (BEST PRACTICE — use SSH)

ssh username@remote_host  
df -h

👉 This is the **correct SRE answer**

---

# 🎯 How to say this in interview

## 💬 Example answer

> I’ve used SFTP for secure file transfers during troubleshooting, such as uploading logs or downloading data files from remote systems.
> 
> I’m comfortable logging into remote servers, listing files, and using commands like put and get to transfer files.
> 
> For example, I might upload log files to a server for analysis or download data to investigate issues locally.
> 
> If I need to check disk space, I would typically SSH into the server and use commands like df -h.

---

# 🔥 Real SRE use case (THIS is what impresses them)

> “If a client reports an issue, I might use SFTP to retrieve logs from the remote system, analyze them locally, and correlate with monitoring data.”

👉 That’s exactly how SREs use it.

---

# ⚡ Quick command summary (memorize this)

| Action      | Command          |
| ----------- | ---------------- |
| Login       | `sftp user@host` |
| List remote | `ls`             |
| List local  | `lls`            |
| Upload      | `put file`       |
| Download    | `get file`       |
| Remote dir  | `cd`             |
| Local dir   | `lcd`            |

---

# 💥 Pro tip (small but powerful)

Mention this if you can:

> “I prefer SFTP over FTP because it’s secure and uses SSH.”

---

# 🚀 If you want next level

I can:

- Give you **common Linux + networking command combos they ask together**
- Or simulate a **hands-on troubleshooting interview (they give scenario, you respond live)**
