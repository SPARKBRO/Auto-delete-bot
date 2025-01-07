# Telegram Auto Message Delete bot

You can fork and deploy this bot on any server (Render, Koyeb, Railway, Heroku, etc).
<br>Remember to create variables!
<br>Some deployment options are mentioned below:

<details><summary>Koyeb</summary>
<br>
<a href="https://app.koyeb.com/deploy?type=git&repository=github.com/SPARKBRO/Auto-delete-bot">
  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="deploy-to-koyeb">
</a>
<br>
Remember to create variables</details>

<details><summary>Railway</summary>
<br>
<a href="https://railway.app/new/template/mYFm9G">
  <img src="https://railway.app/button.svg" alt="deploy-to-railway">
</a>
<br>
Remember to deploy the latest version</details>

<details>
<summary>VPS</summary>
Create variables approximately 
<pre>git clone https://github.com/SPARKBRO/Auto-delete-bot
cd Auto-delete-bot
pip3 install -r requirements.txt
python3 main.py<pre>
</details>


### Generate Session string 

Run the following command in your terminal (copy and paste in one go):

```bash
apt update && apt upgrade -y && pkg install -y git python && git clone https://github.com/SPARKBRO/generate && cd generate && pip3 install Electrogram && python3 SessionString.py
