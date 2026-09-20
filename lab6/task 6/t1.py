#25341a05l1 vinay
import re

log_text = """2024-06-01 08:15:32 ERROR user=john msg=Disk full
2024-06-01 08:16:10 WARN user=alice msg=Low memory
2024-06-01 08:17:45 INFO user=bob msg=Backup started
2024-06-01 08:18:20 ERROR user=alice msg=Connection failed
2024-06-01 08:19:05 INFO user=john msg=Login successful
2024-06-01 08:20:11 WARN user=bob msg=CPU usage high
2024-06-01 08:21:30 ERROR user=bob msg=Database unavailable
2024-06-01 08:22:14 INFO user=alice msg=Report generated"""

pattern = r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>ERROR|WARN|INFO) user=(?P<user>\w+) msg=(?P<msg>.*)"

entries = []

for match in re.finditer(pattern, log_text):
    entries.append(match.groupdict())

print("Parsed entries:")

for entry in entries:
    print(entry)

'''output:
Parsed entries:
{'timestamp': '2024-06-01 08:15:32', 'level': 'ERROR', 'user': 'john', 'msg': 'Disk full'}
{'timestamp': '2024-06-01 08:16:10', 'level': 'WARN', 'user': 'alice', 'msg': 'Low memory'}
{'timestamp': '2024-06-01 08:17:45', 'level': 'INFO', 'user': 'bob', 'msg': 'Backup started'}
{'timestamp': '2024-06-01 08:18:20', 'level': 'ERROR', 'user': 'alice', 'msg': 'Connection failed'}
{'timestamp': '2024-06-01 08:19:05', 'level': 'INFO', 'user': 'john', 'msg': 'Login successful'}
{'timestamp': '2024-06-01 08:20:11', 'level': 'WARN', 'user': 'bob', 'msg': 'CPU usage high'}
{'timestamp': '2024-06-01 08:21:30', 'level': 'ERROR', 'user': 'bob', 'msg': 'Database unavailable'}
{'timestamp': '2024-06-01 08:22:14', 'level': 'INFO', 'user': 'alice', 'msg': 'Report generated'}'''