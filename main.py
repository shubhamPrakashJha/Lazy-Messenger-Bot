import re
import time
import argparse
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


def loginToFB(FBdriver, email, password):
    email_field = FBdriver.find_element_by_id('email')
    pass_field = FBdriver.find_element_by_id('pass')
    email_field.send_keys(email)
    pass_field.send_keys(password)
    email_field.submit()


def moveToMessages(FBdriver):
    profile_url = [a for a in FBdriver.find_elements_by_tag_name(
        'a') if a.get_attribute('title') == 'Profile'][0].get_attribute('href')
    re_search = re.search(r'(\?id=\d+)$', profile_url)

    FB_ID = ''

    if re_search:
        # Profiles with no username
        FB_ID = re_search.group(0)
        FB_ID = FB_ID.replace('?id=', '')
    else:
        # Profiles with username
        FB_ID = profile_url[profile_url.rfind('/') + 1:]

    FBdriver.get('https://www.facebook.com/messages/t/' + FB_ID)


def parseMessageAndExecute(message, FBdriver, YoutubeDriver):
    '''
    making the message input lowercase allows for a better user experice 
    on mobile devices with auto caps enabled
    '''

    message = message.lower()

    split_message = message.split()

    if re.search(r'^(play\s)', message):
        search_term = ' '.join(split_message[1:])
        search_box = YoutubeDriver.find_element_by_name('search_query')
        search_box.send_keys(search_term)
        search_box.submit()
        results = YoutubeDriver.find_elements_by_class_name(
            'item-section')[0].find_elements_by_class_name('yt-lockup-title')

        number_of_results = 5

        title_link_map = {}
        for result in results[:number_of_results]:
            anchor_tag = result.find_elements_by_tag_name('a')[0]
            title_link_map[anchor_tag.text.encode(
                'ascii', 'ignore')] = anchor_tag.get_attribute('href').encode('ascii', 'ignore')

        search_result_output = ''
        k = 1

        num_key_map = []

        for title in title_link_map.keys():
            search_result_output = (str(k) + '. ' + title + '\n\n')
            num_key_map.append(title)

            # sending user search results
            actions = ActionChains(FBdriver)
            actions.send_keys(search_result_output)
            actions.perform()

            k += 1

        FBdriver.implicitly_wait(10)
        time.sleep(1)

        previous_message_state = FBdriver.find_elements_by_css_selector(
            'span._3oh-._58nk')

        while True:

            FBdriver.implicitly_wait(5)

            current_message_state = FBdriver.find_elements_by_css_selector(
                'span._3oh-._58nk')

            if not current_message_state == previous_message_state:
                latest_message = current_message_state[
                    -1].text.encode('ascii', 'ignore')
                link = title_link_map[num_key_map[int(latest_message) - 1]]
                YoutubeDriver.get(link)
                break

            time.sleep(0.1)

    elif re.search(r'^(pause)$', message.strip()):
        YoutubeDriver.execute_script(
            "document.getElementById('movie_player').pauseVideo();")
    elif re.search(r'^(unpause)$', message.strip()):
        YoutubeDriver.execute_script(
            "document.getElementById('movie_player').playVideo();")
    elif re.search(r'^(mute)$', message.strip()):
        YoutubeDriver.execute_script(
            "document.getElementById('movie_player').mute();")
    elif re.search(r'^(unmute)$', message.strip()):
        YoutubeDriver.execute_script(
            "document.getElementById('movie_player').unMute();")
    elif re.search(r'^(seek-to)\s', message.strip()):
        time_value = split_message[1]
        YoutubeDriver.execute_script(
            "document.getElementById('movie_player').seekTo(" + time_value + ",true);")
    elif re.search(r'^(play-now)\s', message.strip()):
        search_term = ' '.join(split_message[1:])
        search_box = YoutubeDriver.find_element_by_name('search_query')
        search_box.send_keys(search_term)
        search_box.submit()
        link = YoutubeDriver.find_elements_by_class_name('item-section')[0].find_elements_by_class_name(
            'yt-lockup-title')[0].find_elements_by_tag_name('a')[0].get_attribute('href')
        YoutubeDriver.get(link)


def displayUsage():
    print'''
    >>> SETUP COMPLETE
    Usage:
    play <search term> : Returns top 5 videos from YouTube, waits for an integer response to play video
    play-now <search term> : Plays first video from search results (I\'m feeling lucky)
    seek-to <time in seconds> : Seeks to the said time
    pause : Pauses the video
    unpause : Unpauses the video
    mute : Mutes the video
    unmute : Unmutes the video\n\n
    '''


def readMessages(FBdriver, YoutubeDriver):
    previous_message_state = FBdriver.find_elements_by_css_selector(
        'span._3oh-._58nk')
    while True:
        FBdriver.implicitly_wait(5)
        current_message_state = FBdriver.find_elements_by_css_selector(
            'span._3oh-._58nk')
        if not current_message_state == previous_message_state:
            latest_message = current_message_state[-1].text
            print latest_message
            parseMessageAndExecute(latest_message, FBdriver, YoutubeDriver)
            previous_message_state = current_message_state
        time.sleep(0.1)


# required arguments

parser = argparse.ArgumentParser(
    description='A tool to control YouTube using Facebook messenger')
parser.add_argument(
    '-e', '--email', help='facebook / messenger login email', required=True)
parser.add_argument('-p', '--password',
                    help='facebook / messenger login password', required=True)
args = vars(parser.parse_args())

if __name__ == '__main__':
    email = args['email']
    password = args['password']

    print 'Setting Up ... Please Wait'

    chrome_opts = webdriver.ChromeOptions()
    chrome_opts.add_argument('--disable-notifications')

    FBdriver = webdriver.Chrome(chrome_options=chrome_opts)
    YoutubeDriver = webdriver.Chrome()
    FBdriver.get('https://www.facebook.com')
    YoutubeDriver.get('https://www.youtube.com')

    loginToFB(FBdriver, email, password)
    moveToMessages(FBdriver)
    displayUsage()
    print 'message log:'
    readMessages(FBdriver, YoutubeDriver)
