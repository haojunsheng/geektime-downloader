获取所有课程

geektime-dl login --phone xxxxxx --password xxxxxx

./geektime-dl column|awk '{print $4}'|grep -v ID

在使用geektime-downloader下载课程





```
./geektime-downloader --gcid "1046e15-314a477-4e2b98a-e8b1359"  --gcess "BgoEAAAAAAMEjHSGZwUEAAAAAAEIl_UeAAAAAAAEBACNJwAMAQEHBF.AP1kJAQEGBKJ1drIIAQMCBIx0hmcLAgYADQEB" --output 3
```

Main.py 可以获取所有的课程，以及本地已有的课程，下载没有的课程。
