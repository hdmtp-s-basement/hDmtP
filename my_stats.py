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
<br>
<br>
<p align="center">
<img src="https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif" align="center">
<hr>
![Movement - Imgur](https://user-images.githubusercontent.com/65482473/145084467-c34802cd-5684-425a-9ed3-ba09d4baa9cd.gif)
</p>
<hr>
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=hDmtP&langs_count=12)](https://github.com/hDmtP/github-readme-stats)
![My GitHub stats](https://github-readme-stats.vercel.app/api?username=hdmtp&show_icons=true&theme=radical) 
<hr>
Today's Date | Time Last Updated      | Contributions Today
:--------------:|:----------------:|:-------------:
''' + f"**{datetime_NY[:10]}**| **{datetime_NY[10:26]}** | **{sum([day.count for day in contribs_2021.days])}**"

f = open("README.md", "w")
f.write(sc)
f.close()
