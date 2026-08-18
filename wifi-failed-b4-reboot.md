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


[PL] pl@pop-os:~ $ date
Fri Aug 14 04:03:46 PM EDT 2026
[PL] pl@pop-os:~ $ nmcli device status
DEVICE          TYPE      STATE                   CONNECTION 
docker0         bridge    connected (externally)  docker0    
wlp1s0          wifi      disconnected            --         
p2p-dev-wlp1s0  wifi-p2p  disconnected            --         
lo              loopback  unmanaged               --         
[PL] pl@pop-os:~ $ iwconfig wlp1s0
wlp1s0    IEEE 802.11  ESSID:off/any  
          Mode:Managed  Access Point: Not-Associated   Tx-Power=3 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:off
          
[PL] pl@pop-os:~ $ sudo dmesg | tail -150
[sudo] password for pl: 
[  138.307585]  drm_ioctl_kernel+0xb0/0x110
[  138.307595]  drm_ioctl+0x2d3/0x5c0
[  138.307601]  ? __pfx_drm_connector_property_set_ioctl+0x10/0x10
[  138.307609]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.307620]  amdgpu_drm_ioctl+0x4b/0x90 [amdgpu]
[  138.307948]  __x64_sys_ioctl+0xa4/0x100
[  138.307956]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.307964]  x64_sys_call+0x140c/0x2790
[  138.307972]  do_syscall_64+0xd2/0x570
[  138.307983]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.307988]  ? drm_mode_object_put.part.0+0x26/0xa0
[  138.307994]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.307999]  ? drm_mode_obj_set_property_ioctl+0x212/0x440
[  138.308008]  ? __pfx_drm_connector_property_set_ioctl+0x10/0x10
[  138.308014]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308019]  ? drm_connector_property_set_ioctl+0x38/0x60
[  138.308025]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308030]  ? drm_ioctl_kernel+0xb0/0x110
[  138.308036]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308041]  ? __check_object_size+0x51/0x160
[  138.308050]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308055]  ? drm_ioctl+0x32b/0x5c0
[  138.308060]  ? __pfx_drm_connector_property_set_ioctl+0x10/0x10
[  138.308072]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308077]  ? ktime_get_mono_fast_ns+0x43/0xe0
[  138.308087]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308093]  ? amdgpu_drm_ioctl+0x6b/0x90 [amdgpu]
[  138.308402]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308408]  ? __x64_sys_ioctl+0xbe/0x100
[  138.308415]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308420]  ? arch_exit_to_user_mode_prepare.constprop.0+0xd/0xe0
[  138.308426]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308431]  ? do_syscall_64+0x10f/0x570
[  138.308436]  ? __x64_sys_epoll_ctl+0x65/0xa0
[  138.308445]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308450]  ? arch_exit_to_user_mode_prepare.constprop.0+0xd/0xe0
[  138.308457]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308462]  ? do_syscall_64+0x10f/0x570
[  138.308466]  ? srso_alias_return_thunk+0x5/0xfbef5
[  138.308471]  ? do_syscall_64+0x10f/0x570
[  138.308478]  entry_SYSCALL_64_after_hwframe+0x76/0x7e
[  138.308483] RIP: 0033:0x7624a5b1a98f
[  138.308490] Code: 00 48 89 44 24 18 31 c0 48 8d 44 24 60 c7 04 24 10 00 00 00 48 89 44 24 08 48 8d 44 24 20 48 89 44 24 10 b8 10 00 00 00 0f 05 <41> 89 c0 3d 00 f0 ff ff 77 1f 48 8b 44 24 18 64 48 2b 04 25 28 00
[  138.308495] RSP: 002b:00007ffe41629940 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[  138.308503] RAX: ffffffffffffffda RBX: 00007ffe416299d0 RCX: 00007624a5b1a98f
[  138.308507] RDX: 00007ffe416299d0 RSI: 00000000c01064ab RDI: 000000000000000f
[  138.308511] RBP: 00000000c01064ab R08: 0000000000000000 R09: 0000622cd7f8d540
[  138.308515] R10: 0000000000000000 R11: 0000000000000246 R12: 0000622cd7f89cb0
[  138.308519] R13: 000000000000000f R14: 0000622cd7f90b60 R15: 0000000000000000
[  138.308529]  </TASK>
[  138.308532] ---[ end trace 0000000000000000 ]---
[  142.193343] ACPI: button: The lid device is not compliant to SW_LID.
[  146.064993] logitech-hidpp-device 0003:046D:4091.0005: HID++ 4.5 device connected.
[  148.702284] warning: `ThreadPoolForeg' uses wireless extensions which will stop working for Wi-Fi 7 hardware; use nl80211
[ 5268.638380] wlp1s0: deauthenticating from 1e:6f:be:f6:9a:68 by local choice (Reason: 3=DEAUTH_LEAVING)
[ 5270.121566] PM: suspend entry (s2idle)
[ 5270.141390] Filesystems sync: 0.019 seconds
[ 5270.143761] Freezing user space processes
[ 5270.147526] Freezing user space processes completed (elapsed 0.003 seconds)
[ 5270.147533] OOM killer disabled.
[ 5270.147536] Freezing remaining freezable tasks
[ 5270.148803] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
[ 5270.148808] printk: Suspending console(s) (use no_console_suspend to debug)
[ 5270.431491] pcieport 0000:00:08.3: quirk: disabling D3cold for suspend
[ 5270.436540] ACPI: EC: interrupt blocked
[ 7178.212201] ACPI: EC: interrupt unblocked
[ 7178.245865] nvme nvme0: D3 entry latency set to 10 seconds
[ 7178.247882] nvme nvme0: 16/0/0 default/read/poll queues
[ 7178.250377] amdgpu 0000:c4:00.0: [drm] PCIE GART of 512M enabled (table at 0x000000807FD00000).
[ 7178.250472] amdgpu 0000:c4:00.0: SMU is resuming...
[ 7178.253546] amdgpu 0000:c4:00.0: SMU is resumed successfully!
[ 7178.663295] amdgpu 0000:c4:00.0: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[ 7178.663300] amdgpu 0000:c4:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[ 7178.663302] amdgpu 0000:c4:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[ 7178.663304] amdgpu 0000:c4:00.0: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[ 7178.663306] amdgpu 0000:c4:00.0: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[ 7178.663308] amdgpu 0000:c4:00.0: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[ 7178.663310] amdgpu 0000:c4:00.0: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[ 7178.663311] amdgpu 0000:c4:00.0: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[ 7178.663313] amdgpu 0000:c4:00.0: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[ 7178.663315] amdgpu 0000:c4:00.0: ring sdma0 uses VM inv eng 12 on hub 0
[ 7178.663317] amdgpu 0000:c4:00.0: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[ 7178.663319] amdgpu 0000:c4:00.0: ring jpeg_dec uses VM inv eng 1 on hub 8
[ 7178.663321] amdgpu 0000:c4:00.0: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[ 7178.820985] OOM killer enabled.
[ 7178.820987] Restarting tasks: Starting
[ 7178.824417] Restarting tasks: Done
[ 7178.824432] efivarfs: resyncing variable state
[ 7178.827845] efivarfs: finished resyncing variable state
[ 7178.827921] random: crng reseeded on system resumption
[ 7178.828537] PM: suspend exit
[ 7178.932617] usb 5-1: new full-speed USB device number 9 using xhci_hcd
[ 7179.160604] usb 5-1: new high-speed USB device number 10 using xhci_hcd
[ 7179.295816] usb 5-1: New USB device found, idVendor=0bda, idProduct=5409, bcdDevice= 1.30
[ 7179.295825] usb 5-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 7179.295829] usb 5-1: Product: USB2.1 Hub
[ 7179.295832] usb 5-1: Manufacturer: Generic
[ 7179.334254] hub 5-1:1.0: USB hub found
[ 7179.335654] hub 5-1:1.0: 5 ports detected
[ 7179.689152] usb 5-1.5: new high-speed USB device number 11 using xhci_hcd
[ 7179.794115] usb 5-1.5: New USB device found, idVendor=0bda, idProduct=1101, bcdDevice= 1.01
[ 7179.794131] usb 5-1.5: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 7179.794138] usb 5-1.5: Product: HID Device
[ 7179.794144] usb 5-1.5: Manufacturer: Realtek
[ 7179.834178] Bluetooth: hci0: HW/SW Version: 0x008a008a, Build Time: 20260106153735
[ 7179.850763] hid-generic 0003:0BDA:1101.0007: hiddev1,hidraw5: USB HID v1.11 Device [Realtek HID Device] on usb-0000:c6:00.3-1.5/input0
[ 7180.040635] Bluetooth: hci0: Device setup in 203267 usecs
[ 7180.040670] Bluetooth: hci0: HCI Enhanced Setup Synchronous Connection command is advertised, but not supported.
[ 7180.103315] Bluetooth: hci0: AOSP extensions version v1.00
[ 7180.103356] Bluetooth: hci0: AOSP quality report is supported
[ 9556.937279] PM: suspend entry (s2idle)
[ 9556.942437] Filesystems sync: 0.005 seconds
[ 9556.943778] Freezing user space processes
[ 9556.960100] Freezing user space processes completed (elapsed 0.016 seconds)
[ 9556.960112] OOM killer disabled.
[ 9556.960116] Freezing remaining freezable tasks
[ 9556.961533] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
[ 9556.961537] printk: Suspending console(s) (use no_console_suspend to debug)
[ 9557.095585] ACPI: EC: interrupt blocked
[14889.951198] ACPI: EC: interrupt unblocked
[14889.984812] nvme nvme0: D3 entry latency set to 10 seconds
[14889.987281] nvme nvme0: 16/0/0 default/read/poll queues
[14889.989457] amdgpu 0000:c4:00.0: [drm] PCIE GART of 512M enabled (table at 0x000000807FD00000).
[14889.989565] amdgpu 0000:c4:00.0: SMU is resuming...
[14889.993961] amdgpu 0000:c4:00.0: SMU is resumed successfully!
[14890.407380] amdgpu 0000:c4:00.0: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[14890.407385] amdgpu 0000:c4:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[14890.407388] amdgpu 0000:c4:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[14890.407389] amdgpu 0000:c4:00.0: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[14890.407391] amdgpu 0000:c4:00.0: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[14890.407393] amdgpu 0000:c4:00.0: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[14890.407395] amdgpu 0000:c4:00.0: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[14890.407396] amdgpu 0000:c4:00.0: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[14890.407398] amdgpu 0000:c4:00.0: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[14890.407400] amdgpu 0000:c4:00.0: ring sdma0 uses VM inv eng 12 on hub 0
[14890.407402] amdgpu 0000:c4:00.0: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[14890.407404] amdgpu 0000:c4:00.0: ring jpeg_dec uses VM inv eng 1 on hub 8
[14890.407405] amdgpu 0000:c4:00.0: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[14890.565037] OOM killer enabled.
[14890.565039] Restarting tasks: Starting
[14890.568821] Restarting tasks: Done
[14890.568836] efivarfs: resyncing variable state
[14890.572268] efivarfs: finished resyncing variable state
[14890.572341] random: crng reseeded on system resumption
[14890.573009] PM: suspend exit
[14891.579744] Bluetooth: hci0: HW/SW Version: 0x008a008a, Build Time: 20260106153735
[14891.808771] Bluetooth: hci0: Device setup in 225381 usecs
[14891.808810] Bluetooth: hci0: HCI Enhanced Setup Synchronous Connection command is advertised, but not supported.
[14891.869845] Bluetooth: hci0: AOSP extensions version v1.00
[14891.869852] Bluetooth: hci0: AOSP quality report is supported
[PL] pl@pop-os:~ $ sudo journalctl -b --since "15 minutes ago" --no-pager | \
  grep -iE 'mt7921|wlp1s0|firmware|MCU|timeout|reset|failed|disconnect|deauth|PCI'
Aug 14 15:59:55 pop-os kernel: amdgpu 0000:c4:00.0: [drm] PCIE GART of 512M enabled (table at 0x000000807FD00000).
Aug 14 15:59:56 pop-os gnome-shell[2401]: JS ERROR: Failed to initialize fprintd service: Gio.DBusError: GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown: The name is not activatable
Aug 14 15:59:56 pop-os NetworkManager[12638]: <info>  [1786737596.8699] manager[0x5946c4c20000]: monitoring kernel firmware directory '/lib/firmware'.
Aug 14 15:59:56 pop-os NetworkManager[12638]: <info>  [1786737596.9236] rfkill1: found Wi-Fi radio killswitch (at /sys/devices/pci0000:00/0000:00:02.2/0000:01:00.0/ieee80211/phy0/rfkill1) (driver mt7921e)
Aug 14 15:59:56 pop-os NetworkManager[12638]: <info>  [1786737596.9418] device (docker0): state change: unavailable -> disconnected (reason 'connection-assumed', sys-iface-state: 'external')
Aug 14 15:59:56 pop-os NetworkManager[12638]: <info>  [1786737596.9425] device (wlp1s0): driver supports Access Point (AP) mode
Aug 14 15:59:56 pop-os NetworkManager[12638]: <info>  [1786737596.9427] manager: (wlp1s0): new 802.11 Wi-Fi device (/org/freedesktop/NetworkManager/Devices/3)
Aug 14 15:59:56 pop-os NetworkManager[12638]: <info>  [1786737596.9429] device (wlp1s0): state change: unmanaged -> unavailable (reason 'managed', sys-iface-state: 'external')
Aug 14 15:59:57 pop-os NetworkManager[12638]: <info>  [1786737597.0187] device (docker0): state change: disconnected -> prepare (reason 'none', sys-iface-state: 'external')
Aug 14 15:59:57 pop-os NetworkManager[12638]: <info>  [1786737597.0623] device (wlp1s0): supplicant interface state: internal-starting -> disconnected
Aug 14 15:59:57 pop-os NetworkManager[12638]: <info>  [1786737597.0624] Wi-Fi P2P device controlled by interface wlp1s0 created
Aug 14 15:59:57 pop-os NetworkManager[12638]: <info>  [1786737597.0625] manager: (p2p-dev-wlp1s0): new 802.11 Wi-Fi P2P device (/org/freedesktop/NetworkManager/Devices/4)
Aug 14 15:59:57 pop-os NetworkManager[12638]: <info>  [1786737597.0625] device (p2p-dev-wlp1s0): state change: unmanaged -> unavailable (reason 'managed', sys-iface-state: 'external')
Aug 14 15:59:57 pop-os NetworkManager[12638]: <info>  [1786737597.0628] device (wlp1s0): state change: unavailable -> disconnected (reason 'supplicant-available', sys-iface-state: 'managed')
Aug 14 15:59:57 pop-os NetworkManager[12638]: <info>  [1786737597.0640] device (p2p-dev-wlp1s0): state change: unavailable -> disconnected (reason 'none', sys-iface-state: 'managed')
Aug 14 15:59:59 pop-os ModemManager[1013]: <info>  [base-manager] couldn't check support for device '/sys/devices/pci0000:00/0000:00:02.2/0000:01:00.0': not supported by any plugin
Aug 14 16:00:02 pop-os gnome-shell[2401]: clutter_actor_remove_child: assertion 'child->priv->parent != NULL' failed
Aug 14 16:00:02 pop-os gnome-shell[2401]: clutter_actor_remove_child: assertion 'child->priv->parent != NULL' failed
Aug 14 16:02:28 pop-os gnome-shell[2401]: Failed to get met.no forecast data: 2 Error resolving “aa037rv1tsaszxi6o.api.met.no”: Name or service not known
[PL] pl@pop-os:~ $ sudo journalctl -b --since "15 minutes ago" --no-pager > ~/wifi-failure.log
[PL] pl@pop-os:~ $ ls -lh ~/wifi-failure.log
-rw-rw-r-- 1 pl pl 33K Aug 14 16:04 /home/pl/wifi-failure.log
[PL] pl@pop-os:~ $ 
