Template OS Linux - IOPS
=======================

Zabbix template for collecting IO statistics

With this template you can collect different disk statistics.


Installation
------------
1) Copy text from "userparameter_diskstats.conf" to end of file "/etc/zabbix/zabbix-agentd.conf"/userparameter_diskstats.conf"
2) Copy "lld-disks.py" to "/etc/zabbix/scripts/lld-disks.py" and make it executable "chmod a+x /etc/zabbix/scripts/lld-disks.py"
3) Add Template "Template OS Linux - IOPS - Python.xml" to ZABBIX server and 
4) After that restart zabbix-agent

- userparameter_diskstats.conf - user parameters
- lld-disks.py1 is low level discovery script for enumerating disks of your system. (JSON)
- lld-disks.py2 is low level discovery script for enumerating disks of your system. (NEW JSON)
- lld-disks.py3 is low level discovery script for enumerating disks of your system. (NO JSON - EMULATOR WITH PRINT)

Using without User Parameters
-----------------------------
Zabbix have [standard parameters](https://www.zabbix.com/documentation/2.0/manual/appendix/items/supported_by_platform) for monitoring disk io: `vfs.dev.read` and `vfs.dev.write` with several types:
* sectors
* operations
* sps
* ops

Template have this values configured, but disabled by default.


Testing
-------
To test that everything work use `zabbix_get` (from some time this is in it's own package, so do `apt-get/yum install zabbix-get`):
```bash
# view result of low level discovery
zabbix_get -s "ip_client" -k "custom.vfs.discover_disks"
# view statistics for 'sda' disk
zabbix_get -s "ip_client" -k "custom.vfs.dev.write.sectors[sda]"