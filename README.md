# Description

List data of trending projects on Github from your command line, including the security score

security score - The count of unused packages in the repo. calculated by the function find_extra_reqs in pip_check_reqs.

# Installation
```
pipenv install 
pipenv shell
```

# Usage 
```buildoutcfg
    python trending_repos.py 5
```

# Output Example
```buildoutcfg
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Name          ┃ Description                                                                         ┃ Stars and Forks  ┃ Security Score ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ UnicomTask    │ 联通手机营业厅自动做任务、签到、领流量、领积分等。                                          │ 1018 ⭐ 3159 ⎇   │ 3              │
│               │                                                                                     │                  │                │
│ oppia         │ A free, online learning platform to make quality education accessible for all.      │ 1816 ⭐ 1747 ⎇   │ 75             │
│               │                                                                                     │                  │                │
│ mslive_public │ Track live sentiment for stocks from Reddit and Twitter and identify growing stocks │ 70 ⭐ 29 ⎇       │ 0              │
│               │                                                                                     │                  │                │
│ consoleme     │ A Central Control Plane for AWS Permissions and Access                              │ 1611 ⭐ 82 ⎇     │ 150            │
│               │                                                                                     │                  │                │
│ wtfpython     │ What the f*ck Python? 😱                                                            │ 26226 ⭐ 2204 ⎇  │ 0              │
└───────────────┴─────────────────────────────────────────────────────────────────────────────────────┴──────────────────┴────────────────┘

```