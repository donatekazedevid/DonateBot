<h1 align="center"><b>Donate Bot</b></h1>
<h4 align="center">A Telegram Bot to tell How to Donate you</h4>

# Help

### Deploy to Heroku :
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/KazeDevID/DonateBot)

### Local Deploy :
#### Configuration
- Edit the [Var.py](https://github.com/KazeDevID/DonateBot/blob/main/Var.py)  with your Own Values
- `API_ID` and `API_HASH` - Get API_ID and API_HASH from https://my.telegram.org
- `TOKEN` - Bot Token given by the [@BotFather](https://t.me/BotFather)
- `OWNER_ID` - Your Telegram ID, Get it from [@MissRose_bot](https://t.me/MissRose_bot) by sending `/start` and `/info`
- `DONATE_TEXT` - Your Donate Text or Message to be repeated, Basic Telegram Markdowns apply. For Markdown Help [click here](https://github.com/KazeDevID/DonateBot#markdown)

#### Running
- Install the Requirements by `pip3 install -r requirments.txt`
- Run the Bot by `python3 -m bot`

### Markdown
```
- To make your Text Bold use **Your Text Here**
- To make your Text Italic use __Your Text Here__
- To make your Text Mono use `Your Text Here`
- To make your Text Strikethrough use ~~Your Text Here~~ 
```