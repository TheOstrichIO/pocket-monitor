import unittest
import webtest
import endpoints
from google.appengine.ext import testbed

import pocketmon as pm
import api

test_items_1 = {
    'test-user-1': {
        u'528495686': {u'status': u'1', u'is_index': u'0', u'time_updated': u'1393911087', u'time_favorited': u'0', u'time_read': u'1393911084', u'favorite': u'0', u'excerpt': u"If you read Lifehacker, you probably enjoy automating tasks to save both time and money. There's one more reason to add to that list of benefits: avoiding too many decisions.", u'has_video': u'0', u'word_count': u'230', u'sort_id': 10, u'resolved_url': u'http://lifehacker.com/automate-minor-tasks-to-fight-decision-fatigue-1505698868', u'has_image': u'1', u'item_id': u'528495686', u'time_added': u'1390588198', u'resolved_id': u'528483905', u'is_article': u'1', u'resolved_title': u'Automate Minor Tasks to Fight Decision Fatigue', u'given_url': u'http://feeds.gawker.com/~r/lifehacker/full/~3/Bv64mbjJzf8/automate-minor-tasks-to-fight-decision-fatigue-1505698868', u'given_title': u'Automate Minor Tasks to Fight Decision Fatigue'},
        u'143808646': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1369572786', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u"Planning a vacation doesn't necessarily mean you have to get someone to come and water your plants, especially if you only have a few that need a little care while you're out of town for a few days.", u'has_video': u'0', u'word_count': u'384', u'sort_id': 2, u'resolved_url': u'http://lifehacker.com/5891194/build-a-self+regulating-automatic-plant-watering-system-with-a-plastic-bottle-and-a-tray', u'has_image': u'1', u'item_id': u'143808646', u'time_added': u'1369572765', u'resolved_id': u'143808646', u'is_article': u'1', u'resolved_title': u'Build a Self-Regulating, Automatic Plant Watering System with a Plastic Bottle and a Tray', u'given_url': u'http://lifehacker.com/5891194/build-a-self+regulating-automatic-plant-watering-system-with-a-plastic-bottle-and-a-tray', u'given_title': u'Build a Self-Regulating, Automatic Plant Watering System with a Plastic Bot'},
        u'395590136': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1373738045', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'The dryer in our house is in an out-of-the-way corner where it\u2019s hard to hear the buzzer. When we miss it, the clothes sit in the dryer getting wrinkly, so we start the dryer again, don\u2019t hear the buzzer again \u2026 it\u2019s an endless cycle.', u'has_video': u'0', u'word_count': u'902', u'sort_id': 4, u'resolved_url': u'http://makezine.com/projects/make-34/the-dryer-messenger/', u'has_image': u'1', u'item_id': u'395590136', u'time_added': u'1373738030', u'resolved_id': u'395590136', u'is_article': u'0', u'resolved_title': u'The Dryer Messenger', u'given_url': u'http://makezine.com/projects/make-34/the-dryer-messenger/', u'given_title': u'MAKE | The Dryer Messenger'},
        u'250317486': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1393495378', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'Usually when someone speaks about the benefits of going paperless, they talk about reducing clutter, better organization, and the ability to find what you are looking for from anywhere. Those are powerful reasons for going paperless and I\u2019ve discussed many of them in these tips.', u'has_video': u'0', u'word_count': u'1632', u'sort_id': 11, u'resolved_url': u'http://www.jamierubin.net/2012/11/13/going-paperless-examples-of-paperless-automation-using-evernote/', u'has_image': u'1', u'item_id': u'250317486', u'time_added': u'1393495370', u'resolved_id': u'250317486', u'is_article': u'1', u'resolved_title': u'Going Paperless: Examples of Paperless Automation Using Evernote', u'given_url': u'http://www.jamierubin.net/2012/11/13/going-paperless-examples-of-paperless-automation-using-evernote/', u'given_title': u'Going Paperless: Examples of Paperless Automation Using Evernote | Jamie To'},
        u'348644794': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1395574862', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u"I've always found LIRC more unpleasant project to deal with than seems necessary, much like lm-sensors.", u'has_video': u'0', u'word_count': u'114', u'sort_id': 9, u'resolved_url': u'http://raspberrypi.stackexchange.com/questions/2062/using-raspberry-pi-to-control-my-ac-via-infrared', u'has_image': u'0', u'item_id': u'348644794', u'time_added': u'1373793073', u'resolved_id': u'348644794', u'is_article': u'1', u'resolved_title': u'Using Raspberry Pi to control my AC via infrared', u'given_url': u'http://raspberrypi.stackexchange.com/questions/2062/using-raspberry-pi-to-control-my-ac-via-infrared', u'given_title': u'python - Using Raspberry Pi to control my AC via infrared - Raspberry Pi St'},
        u'348635049': {u'status': u'1', u'is_index': u'0', u'time_updated': u'1367681502', u'time_favorited': u'0', u'time_read': u'1367681502', u'favorite': u'0', u'excerpt': u'', u'has_video': u'0', u'word_count': u'0', u'sort_id': 0, u'resolved_url': u'http://lifehacker.com/show-us-your-best-tasker-actions-487360630', u'has_image': u'1', u'item_id': u'348635049', u'time_added': u'1367586466', u'resolved_id': u'348616912', u'is_article': u'0', u'resolved_title': u'Show Us Your Best Tasker Actions', u'given_url': u'http://feeds.gawker.com/~r/lifehacker/full/~3/vnji9G8PhV4/show-us-your-best-tasker-actions-487360630', u'given_title': u'Show Us Your Best Tasker Actions'},
        u'395486567': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1393052596', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u"Some of the best DIY projects use microcontrollers or cheap single board computers to automate awesome stuff. But Between the Arduino, the Raspberry Pi, and the BeagleBone, it's hard to figure out which is best for a project.", u'has_video': u'0', u'word_count': u'1153', u'sort_id': 5, u'resolved_url': u'http://lifehacker.com/how-to-pick-the-right-electronics-board-for-your-diy-pr-742869540', u'has_image': u'1', u'item_id': u'395486567', u'time_added': u'1373782581', u'resolved_id': u'395486567', u'is_article': u'1', u'resolved_title': u'How to Pick the Right Electronics Board for Your DIY Project', u'given_url': u'http://lifehacker.com/how-to-pick-the-right-electronics-board-for-your-diy-pr-742869540', u'given_title': u'How to Pick the Right Electronics Board for Your DIY Project'},
        u'145985372': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1369572683', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u"Ever wished your house would greet you when you opened the front door, which unlocked automatically when you approached? Or your kitchen kept an inventory of everything inside it? The Jetsons may seem like they've got it all, but with a little patience and the right DIYs, the Jetson'll have nothi", u'has_video': u'1', u'word_count': u'2061', u'sort_id': 1, u'resolved_url': u'http://lifehacker.com/5893526/transform-your-digs-into-a-home-of-the-future-diy+style', u'has_image': u'1', u'item_id': u'145985372', u'time_added': u'1369572669', u'resolved_id': u'145985372', u'is_article': u'1', u'resolved_title': u'Transform Your Digs into a Home of the Future, DIY-Style', u'given_url': u'http://lifehacker.com/5893526/transform-your-digs-into-a-home-of-the-future-diy+style', u'given_title': u'Transform Your Digs into a Home of the Future, DIY-Style'},
        u'292449582': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1373782918', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'With Instructables you can share what you make with the world and tap into an ever-growing community of creative experts.  Of course that meant running network connections to all my rooms, as well as to the pool and the garage. I also wired my house for home automation and security.', u'has_video': u'1', u'word_count': u'2039', u'sort_id': 7, u'resolved_url': u'http://www.instructables.com/id/Home-9000-The-ULTIMATE-Doorbell/?ALLSTEPS', u'has_image': u'1', u'item_id': u'292449582', u'time_added': u'1373782884', u'resolved_id': u'292449582', u'is_article': u'0', u'resolved_title': u'Home 9000 - The ULTIMATE Doorbell', u'given_url': u'http://www.instructables.com/id/Home-9000-The-ULTIMATE-Doorbell/?ALLSTEPS', u'given_title': u'Home 9000 - The ULTIMATE Doorbell'},
        u'308895384': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1373723472', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'And The Final Product is Here!  This video below shows all the parts and how I\u2019ve connected the servo.', u'has_video': u'1', u'word_count': u'648', u'sort_id': 3, u'resolved_url': u'http://homeawesomation.wordpress.com/2013/02/26/automated-window-blinds-with-arduino/', u'has_image': u'1', u'item_id': u'308895384', u'time_added': u'1373723456', u'resolved_id': u'308895384', u'is_article': u'1', u'resolved_title': u'Automated Window Blinds with Arduino', u'given_url': u'http://homeawesomation.wordpress.com/2013/02/26/automated-window-blinds-with-arduino/', u'given_title': u'Automated Window Blinds with Arduino | Home Awesomation'},
        u'545333359': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1393694393', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'I promised that beginning this year, one of these posts each month would be a more advanced, in-depth post on how to use Evernote for automation. I mean to keep that promise, and thus, this post.', u'has_video': u'0', u'word_count': u'1905', u'sort_id': 12, u'resolved_url': u'http://www.jamierubin.net/2014/02/12/going-paperless-automating-repetitive-stuff-about-meetings/', u'has_image': u'1', u'item_id': u'545333359', u'time_added': u'1393498049', u'resolved_id': u'545333359', u'is_article': u'1', u'resolved_title': u'Going Paperless: Automating Repetitive Stuff about Meetings', u'given_url': u'http://www.jamierubin.net/2014/02/12/going-paperless-automating-repetitive-stuff-about-meetings/', u'given_title': u'Going Paperless: Automating Repetitive Stuff about Meetings | Jamie Todd Ru'},
        u'394219969': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1393052596', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'The Raspberry Pi was built as a cheap, educational computer platform for students. But it\u2019s exposed GPIO pins, linux support and prices comparable to an Arduino, have all contributed to it\u2019s meteoric rise as an \u2018internet of things\u2019 style embedded computer.', u'has_video': u'1', u'word_count': u'1442', u'sort_id': 6, u'resolved_url': u'http://falldeaf.com/2013/07/the-pi-control-script/', u'has_image': u'1', u'item_id': u'394219969', u'time_added': u'1373782635', u'resolved_id': u'394219969', u'is_article': u'1', u'resolved_title': u'The Pi Control Script', u'given_url': u'http://falldeaf.com/2013/07/the-pi-control-script/', u'given_title': u'The Pi Control Script'},
        u'117185160': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1373783222', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u"You don't need expensive software or a new camera to keep an eye on things at home. Whether you're looking after your dog or trying to catch burglars in the act, you can put together a home security system with a regular webcam and your PC.", u'has_video': u'1', u'word_count': u'657', u'sort_id': 8, u'resolved_url': u'http://lifehacker.com/5860538/how-to-turn-your-webcam-into-a-streaming-motion+detecting-surveillance-system', u'has_image': u'1', u'item_id': u'117185160', u'time_added': u'1373783206', u'resolved_id': u'117185160', u'is_article': u'1', u'resolved_title': u'How to Turn Your Webcam Into a Streaming, Motion-Detecting Surveillance System', u'given_url': u'http://lifehacker.com/5860538/how-to-turn-your-webcam-into-a-streaming-motion+detecting-surveillance-system', u'given_title': u'How to Turn Your Webcam Into a Streaming, Motion-Detecting Surveillance Sys'}
        },
    'test-user-2': {
        u'528495686': {u'status': u'1', u'is_index': u'0', u'time_updated': u'1393911087', u'time_favorited': u'0', u'time_read': u'1393911084', u'favorite': u'0', u'excerpt': u"If you read Lifehacker, you probably enjoy automating tasks to save both time and money. There's one more reason to add to that list of benefits: avoiding too many decisions.", u'has_video': u'0', u'word_count': u'230', u'sort_id': 10, u'resolved_url': u'http://lifehacker.com/automate-minor-tasks-to-fight-decision-fatigue-1505698868', u'has_image': u'1', u'item_id': u'528495686', u'time_added': u'1390588198', u'resolved_id': u'528483905', u'is_article': u'1', u'resolved_title': u'Automate Minor Tasks to Fight Decision Fatigue', u'given_url': u'http://feeds.gawker.com/~r/lifehacker/full/~3/Bv64mbjJzf8/automate-minor-tasks-to-fight-decision-fatigue-1505698868', u'given_title': u'Automate Minor Tasks to Fight Decision Fatigue'},
        u'143808646': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1369572786', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u"Planning a vacation doesn't necessarily mean you have to get someone to come and water your plants, especially if you only have a few that need a little care while you're out of town for a few days.", u'has_video': u'0', u'word_count': u'384', u'sort_id': 2, u'resolved_url': u'http://lifehacker.com/5891194/build-a-self+regulating-automatic-plant-watering-system-with-a-plastic-bottle-and-a-tray', u'has_image': u'1', u'item_id': u'143808646', u'time_added': u'1369572765', u'resolved_id': u'143808646', u'is_article': u'1', u'resolved_title': u'Build a Self-Regulating, Automatic Plant Watering System with a Plastic Bottle and a Tray', u'given_url': u'http://lifehacker.com/5891194/build-a-self+regulating-automatic-plant-watering-system-with-a-plastic-bottle-and-a-tray', u'given_title': u'Build a Self-Regulating, Automatic Plant Watering System with a Plastic Bot'},
        u'395590136': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1373738045', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'The dryer in our house is in an out-of-the-way corner where it\u2019s hard to hear the buzzer. When we miss it, the clothes sit in the dryer getting wrinkly, so we start the dryer again, don\u2019t hear the buzzer again \u2026 it\u2019s an endless cycle.', u'has_video': u'0', u'word_count': u'902', u'sort_id': 4, u'resolved_url': u'http://makezine.com/projects/make-34/the-dryer-messenger/', u'has_image': u'1', u'item_id': u'395590136', u'time_added': u'1373738030', u'resolved_id': u'395590136', u'is_article': u'0', u'resolved_title': u'The Dryer Messenger', u'given_url': u'http://makezine.com/projects/make-34/the-dryer-messenger/', u'given_title': u'MAKE | The Dryer Messenger'},
        u'250317486': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1393495378', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'Usually when someone speaks about the benefits of going paperless, they talk about reducing clutter, better organization, and the ability to find what you are looking for from anywhere. Those are powerful reasons for going paperless and I\u2019ve discussed many of them in these tips.', u'has_video': u'0', u'word_count': u'1632', u'sort_id': 11, u'resolved_url': u'http://www.jamierubin.net/2012/11/13/going-paperless-examples-of-paperless-automation-using-evernote/', u'has_image': u'1', u'item_id': u'250317486', u'time_added': u'1393495370', u'resolved_id': u'250317486', u'is_article': u'1', u'resolved_title': u'Going Paperless: Examples of Paperless Automation Using Evernote', u'given_url': u'http://www.jamierubin.net/2012/11/13/going-paperless-examples-of-paperless-automation-using-evernote/', u'given_title': u'Going Paperless: Examples of Paperless Automation Using Evernote | Jamie To'},
        u'348644794': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1395574862', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u"I've always found LIRC more unpleasant project to deal with than seems necessary, much like lm-sensors.", u'has_video': u'0', u'word_count': u'114', u'sort_id': 9, u'resolved_url': u'http://raspberrypi.stackexchange.com/questions/2062/using-raspberry-pi-to-control-my-ac-via-infrared', u'has_image': u'0', u'item_id': u'348644794', u'time_added': u'1373793073', u'resolved_id': u'348644794', u'is_article': u'1', u'resolved_title': u'Using Raspberry Pi to control my AC via infrared', u'given_url': u'http://raspberrypi.stackexchange.com/questions/2062/using-raspberry-pi-to-control-my-ac-via-infrared', u'given_title': u'python - Using Raspberry Pi to control my AC via infrared - Raspberry Pi St'},
        u'348635049': {u'status': u'1', u'is_index': u'0', u'time_updated': u'1367681502', u'time_favorited': u'0', u'time_read': u'1367681502', u'favorite': u'0', u'excerpt': u'', u'has_video': u'0', u'word_count': u'0', u'sort_id': 0, u'resolved_url': u'http://lifehacker.com/show-us-your-best-tasker-actions-487360630', u'has_image': u'1', u'item_id': u'348635049', u'time_added': u'1367586466', u'resolved_id': u'348616912', u'is_article': u'0', u'resolved_title': u'Show Us Your Best Tasker Actions', u'given_url': u'http://feeds.gawker.com/~r/lifehacker/full/~3/vnji9G8PhV4/show-us-your-best-tasker-actions-487360630', u'given_title': u'Show Us Your Best Tasker Actions'},
        u'395486567': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1393052596', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u"Some of the best DIY projects use microcontrollers or cheap single board computers to automate awesome stuff. But Between the Arduino, the Raspberry Pi, and the BeagleBone, it's hard to figure out which is best for a project.", u'has_video': u'0', u'word_count': u'1153', u'sort_id': 5, u'resolved_url': u'http://lifehacker.com/how-to-pick-the-right-electronics-board-for-your-diy-pr-742869540', u'has_image': u'1', u'item_id': u'395486567', u'time_added': u'1373782581', u'resolved_id': u'395486567', u'is_article': u'1', u'resolved_title': u'How to Pick the Right Electronics Board for Your DIY Project', u'given_url': u'http://lifehacker.com/how-to-pick-the-right-electronics-board-for-your-diy-pr-742869540', u'given_title': u'How to Pick the Right Electronics Board for Your DIY Project'},
        u'145985372': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1369572683', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u"Ever wished your house would greet you when you opened the front door, which unlocked automatically when you approached? Or your kitchen kept an inventory of everything inside it? The Jetsons may seem like they've got it all, but with a little patience and the right DIYs, the Jetson'll have nothi", u'has_video': u'1', u'word_count': u'2061', u'sort_id': 1, u'resolved_url': u'http://lifehacker.com/5893526/transform-your-digs-into-a-home-of-the-future-diy+style', u'has_image': u'1', u'item_id': u'145985372', u'time_added': u'1369572669', u'resolved_id': u'145985372', u'is_article': u'1', u'resolved_title': u'Transform Your Digs into a Home of the Future, DIY-Style', u'given_url': u'http://lifehacker.com/5893526/transform-your-digs-into-a-home-of-the-future-diy+style', u'given_title': u'Transform Your Digs into a Home of the Future, DIY-Style'},
        u'292449582': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1373782918', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'With Instructables you can share what you make with the world and tap into an ever-growing community of creative experts.  Of course that meant running network connections to all my rooms, as well as to the pool and the garage. I also wired my house for home automation and security.', u'has_video': u'1', u'word_count': u'2039', u'sort_id': 7, u'resolved_url': u'http://www.instructables.com/id/Home-9000-The-ULTIMATE-Doorbell/?ALLSTEPS', u'has_image': u'1', u'item_id': u'292449582', u'time_added': u'1373782884', u'resolved_id': u'292449582', u'is_article': u'0', u'resolved_title': u'Home 9000 - The ULTIMATE Doorbell', u'given_url': u'http://www.instructables.com/id/Home-9000-The-ULTIMATE-Doorbell/?ALLSTEPS', u'given_title': u'Home 9000 - The ULTIMATE Doorbell'},
        u'308895384': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1373723472', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'And The Final Product is Here!  This video below shows all the parts and how I\u2019ve connected the servo.', u'has_video': u'1', u'word_count': u'648', u'sort_id': 3, u'resolved_url': u'http://homeawesomation.wordpress.com/2013/02/26/automated-window-blinds-with-arduino/', u'has_image': u'1', u'item_id': u'308895384', u'time_added': u'1373723456', u'resolved_id': u'308895384', u'is_article': u'1', u'resolved_title': u'Automated Window Blinds with Arduino', u'given_url': u'http://homeawesomation.wordpress.com/2013/02/26/automated-window-blinds-with-arduino/', u'given_title': u'Automated Window Blinds with Arduino | Home Awesomation'},
        u'545333359': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1393694393', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'I promised that beginning this year, one of these posts each month would be a more advanced, in-depth post on how to use Evernote for automation. I mean to keep that promise, and thus, this post.', u'has_video': u'0', u'word_count': u'1905', u'sort_id': 12, u'resolved_url': u'http://www.jamierubin.net/2014/02/12/going-paperless-automating-repetitive-stuff-about-meetings/', u'has_image': u'1', u'item_id': u'545333359', u'time_added': u'1393498049', u'resolved_id': u'545333359', u'is_article': u'1', u'resolved_title': u'Going Paperless: Automating Repetitive Stuff about Meetings', u'given_url': u'http://www.jamierubin.net/2014/02/12/going-paperless-automating-repetitive-stuff-about-meetings/', u'given_title': u'Going Paperless: Automating Repetitive Stuff about Meetings | Jamie Todd Ru'},
        u'394219969': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1393052596', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u'The Raspberry Pi was built as a cheap, educational computer platform for students. But it\u2019s exposed GPIO pins, linux support and prices comparable to an Arduino, have all contributed to it\u2019s meteoric rise as an \u2018internet of things\u2019 style embedded computer.', u'has_video': u'1', u'word_count': u'1442', u'sort_id': 6, u'resolved_url': u'http://falldeaf.com/2013/07/the-pi-control-script/', u'has_image': u'1', u'item_id': u'394219969', u'time_added': u'1373782635', u'resolved_id': u'394219969', u'is_article': u'1', u'resolved_title': u'The Pi Control Script', u'given_url': u'http://falldeaf.com/2013/07/the-pi-control-script/', u'given_title': u'The Pi Control Script'},
        u'117185160': {u'status': u'0', u'is_index': u'0', u'time_updated': u'1373783222', u'time_favorited': u'0', u'time_read': u'0', u'favorite': u'0', u'excerpt': u"You don't need expensive software or a new camera to keep an eye on things at home. Whether you're looking after your dog or trying to catch burglars in the act, you can put together a home security system with a regular webcam and your PC.", u'has_video': u'1', u'word_count': u'657', u'sort_id': 8, u'resolved_url': u'http://lifehacker.com/5860538/how-to-turn-your-webcam-into-a-streaming-motion+detecting-surveillance-system', u'has_image': u'1', u'item_id': u'117185160', u'time_added': u'1373783206', u'resolved_id': u'117185160', u'is_article': u'1', u'resolved_title': u'How to Turn Your Webcam Into a Streaming, Motion-Detecting Surveillance System', u'given_url': u'http://lifehacker.com/5860538/how-to-turn-your-webcam-into-a-streaming-motion+detecting-surveillance-system', u'given_title': u'How to Turn Your Webcam Into a Streaming, Motion-Detecting Surveillance Sys'}
        },
    }

test_update_1 = {
    'test-user-1': {
        u'545333359': {u'status': u'1', u'is_index': u'0', u'time_updated': u'1393694393', u'time_favorited': u'0', u'time_read': u'1395911084', u'favorite': u'0', u'excerpt': u'I promised that beginning this year, one of these posts each month would be a more advanced, in-depth post on how to use Evernote for automation. I mean to keep that promise, and thus, this post.', u'has_video': u'0', u'word_count': u'1905', u'sort_id': 12, u'resolved_url': u'http://www.jamierubin.net/2014/02/12/going-paperless-automating-repetitive-stuff-about-meetings/', u'has_image': u'1', u'item_id': u'545333359', u'time_added': u'1393498049', u'resolved_id': u'545333359', u'is_article': u'1', u'resolved_title': u'Going Paperless: Automating Repetitive Stuff about Meetings', u'given_url': u'http://www.jamierubin.net/2014/02/12/going-paperless-automating-repetitive-stuff-about-meetings/', u'given_title': u'Going Paperless: Automating Repetitive Stuff about Meetings | Jamie Todd Ru'},
        },
    }

class TestFetchItems(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
    
    def tearDown(self):
        self.testbed.deactivate()
    
    def testUpdateItemsFromPocketApiDict(self):
        for username, items_dict in test_items_1.iteritems():
            pm.update_items_from_pocket(items_dict, username)
        self.assertEqual(13,
                         len(pm.PocketItem.queryUser('test-user-1').fetch(20)))
    
    def testGetAddedtStats(self):
        pm.update_items_from_pocket(test_items_1['test-user-1'], 'test-user-1')
        items, words = pm.PocketItem.getAddedStats('test-user-1',
                                                   1390586000.3,
                                                   1393495600.5)
        self.assertEqual(2, items)
        self.assertEqual(1862, words)
    
    def testGetReadtStats(self):
        pm.update_items_from_pocket(test_items_1['test-user-1'], 'test-user-1')
        items, words = pm.PocketItem.getReadStats('test-user-1',
                                                   1390586000.3,
                                                   1393995600.5)
        self.assertEqual(1, items)
        self.assertEqual(230, words)
    
    def testGetReadStatusAfterUpdate(self):
        pm.update_items_from_pocket(test_items_1['test-user-1'],
                                    'test-user-1')
        pm.update_items_from_pocket(test_update_1['test-user-1'],
                                    'test-user-1')
        self.assertEqual(13, len(pm.PocketItem.query().fetch(20)))
        items, words = pm.PocketItem.getReadStats('test-user-1',
                                                   1390586000.3,
                                                   1395995600.5)
        self.assertEqual(2, items)
        self.assertEqual(2135, words)
    
    def testGetAllStats(self):
        pm.update_items_from_pocket(test_items_1['test-user-1'],
                                    'test-user-1')
        all_stats = pm.PocketItem.getAllStats('test-user-1', 1393912000)
        self.assertDictEqual(all_stats,
                             {
                            'unread_items': 11,
                            'unread_words': 12937,
                            'added_items_delta': 0,
                            'added_words_delta': 0,
                            'read_items_delta': 1,
                            'read_words_delta': 230,
                            })

class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.setup_env(
                current_version_id='testbed.version',
                USER_EMAIL='test-user-1',
                overwrite=True)
        #needed because endpoints expects a . in this value
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.app = endpoints.api_server([api.PocketMonApi], restricted=False)
        self.testapp = webtest.TestApp(self.app)
    
    def tearDown(self):
        self.testbed.deactivate()
    
    def testApiGetStatsEmpty(self):
        resp = self.testapp.post_json('/_ah/spi/PocketMonApi.get_stats')
        self.assertDictEqual(resp.json,
                             {
                            'unread_items': '0',
                            'unread_words': '0',
                            'added_items_delta': '0',
                            'added_words_delta': '0',
                            'read_items_delta': '0',
                            'read_words_delta': '0',
                            })
    
    def testApiGetStatsData(self):
        pm.update_items_from_pocket(test_items_1['test-user-1'], 'test-user-1')
        resp = self.testapp.post_json(
                           '/_ah/spi/PocketMonApi.get_stats',
                           {'timestamp': 1393912000,})
        self.assertDictEqual(resp.json,
                             {
                            'unread_items': '11',
                            'unread_words': '12937',
                            'added_items_delta': '0',
                            'added_words_delta': '0',
                            'read_items_delta': '1',
                            'read_words_delta': '230',
                            })

if __name__ == '__main__':
    unittest.main()
