# Lazy-Messenger-Bot ( Build During DSCE-CSE HACKATHON 2017, TEAM Number 43 )

**Description Weblink: https://prk54.github.io/lazybotmessenger/ **

An Automated Messenger Bot with following cool **features**:
1. Control YouTube just by texting bot (integrated with  **Facebook Messenger** ) using key terms like play,pause,forward,resume,mute, unmute and many more.
2. Get news updates  from **Times of India**  just by texting the bot key terms like show headlines,show Tech and many more terms by topic.
3. Control your Terminal through Messenger.

## Dependencies and Usage

1. selenium - `pip install selenium`
2. Beautiful Soup - `pip install beautifulsoup4`
3. requests - `pip install requests`
4. subprocess - `pip install subprocess`

## Activate YouTube Automation (Implemented Demo Showed )

**Run the script once `python2 activateBot.py -e <BotId> -p <BotKey>` and..Bingo!!.. done..Now Bot will do the work for you**

Just Shot up Facebook Messenger(or any FB client ) on **any of your devices** and start chatting with the bot to control YouTube by **just texting bot** with the following terms
1. `play <search term>` : Returns top 5 videos from YouTube, waits for an integer response to play video
2. `play-now <search term>` : Plays first video from search results (I'm feeling lucky)
3. `forward <time in seconds>` : Seeks to the said time
4. `pause` : Pauses the video
5. `resume` : Resumes a paused the video
6. `mute` : Mutes the video
7. `unmute` : Unmutes the video

## Activate News Update Automation using Bot smartly (Implemented - Demo Showed )

**Run the script `python2 activateNews.py -e <BotId> -p <BotKey>` and Bot will show you the desired news feeds**

Get news updates from **Times of India** just by texting the Bot with key terms as follows
1. `show headlines`
2. `<topic> updates`

## Activate Terminal Control Automation ( Partialy Implemented  )

Allows user to take full control of the terminal of their computer through Facebook's messaging service.
run:`python teminal.py`
Wait till it sets up to start operation.

**Commands Supported**
`ls`  `help` `cd` `mkdir` `rm` `gedit <file-name>` `ps` 


# Technologies used and description

For automation we are using **Selenium**- An Automation Python API to access all functionalities of the system WebDriver in an intuitive way.For news functionality we are using **Beautiful soup** library to scrap **Times of India** news headlines feeds.To automate the above tasks we are using **Selenium Chrome Drivers** to interact our system with the FB messenger by parsing each command to make two way communication between the Bot and FB Messenger.
