from github_contributions import GithubUser
from datetime import datetime, date
import pytz
from quotes import *

tz_NY = pytz.timezone('Asia/Kolkata')
datetime_NY = str(datetime.now(tz_NY))

user = GithubUser('hdmtp')
contribs = user.contributions()

contribs_2021 = user.contributions(
    start_date=str(date.today()), end_date=str(date.today()))

sc = '''
<h2 align="center">Hello there<img src="https://user-images.githubusercontent.com/88626025/135751180-b3d128a5-ba6f-496d-a6d0-1503b568ee88.gif" width="30px"></h2>
<h3 align="center" margin=30px>
''' + f"\"{choice()}\"" + '''
</h3>

<br>

![Tests](https://github.com/hDmtP/hDmtP/actions/workflows/main.yml/badge.svg)

<br>
<br>



<hr>

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=hDmtP&langs_count=12)](https://github.com/hDmtP/github-readme-stats)

<h2> Visitor's count 👀</h2>

<p><img src="https://profile-counter.glitch.me/{nis130}/count.svg" alt="nis130 :: Visitor's Count" /></p>

<br>

![My GitHub stats](https://github-readme-stats.vercel.app/api?username=hdmtp&show_icons=true&theme=radical) 

<hr>


Today's Date | Time Last Updated      | Contributions Today
:--------------:|:----------------:|:-------------:
''' + f"**{datetime_NY[:10]}**| **{datetime_NY[11:26]}** | **{sum([day.count for day in contribs_2021.days])}**"

f = open("README.md", "w")
f.write(sc)
f.close()
