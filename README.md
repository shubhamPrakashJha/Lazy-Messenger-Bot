#Lazy-Messenger-Bot
An Automated Messenger Bot to control YouTube just by texting bot (integrated with  FACEBOOK MESSENGER ) using key terms like play ,pause, seek-to ,forward, resume, mute, unmute and many more.

#H2Dependencies

selenium - `pip install selenium`
Beautiful Soup - `pip install beautifulsoup4`
requests - `pip install requests`
subprocess - `pip install subprocess`

**Run the script once and..Bingo!!.. done..Bot will do the work for you**
Just fire up any Facebook Messenger(or any FB client ) on **any of your devices** and start chatting with the bot to control YouTube just by texting bot with the following terms
`play <search term>` : Returns top 5 videos from YouTube, waits for an integer response to play video
`play-now <search term>` : Plays first video from search results (I'm feeling lucky)
`forward <time in seconds>` : Seeks to the said time
`pause` : Pauses the video
`resume` : Resumes a paused the video
`mute` : Mutes the video
`unmute` : Unmutes the video

And also getting news updates  from TIMES OF INDIA  just by texting the bot key terms like show headlines, <topic> updates.
For automation we are using SELENIUM - A  PYTHON API to access all functionalities of the system WebDriver in an intuitive way.
          For news functionality we are using  beautiful soup library to scrap TOI news headlines Data. To automate the above tasks we are using selenium chrome drivers to interact our system with the fb messenger by parsing each command to make two way communication.
