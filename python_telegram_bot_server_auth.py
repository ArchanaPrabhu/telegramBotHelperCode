Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Vidya Prabhu/AppData/Local/Programs/Python/Python36/python_telegram_bot_2.py 
>>> 
 RESTART: C:/Users/Vidya Prabhu/AppData/Local/Programs/Python/Python36/python_telegram_bot.py 
2018-01-17 14:20:11,601 (apihelper.py:45 MainThread) DEBUG - TeleBot: "Request: method=post url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/sendMessage params={'chat_id': '415492693', 'text': 'Choose one letter:', 'reply_markup': '{"keyboard": [[{"text": "a"}, {"text": "v"}], [{"text": "c"}, {"text": "d"}, {"text": "e"}]]}'} files=None"
2018-01-17 14:20:13,265 (apihelper.py:55 MainThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":{"message_id":104,"from":{"id":491326980,"is_bot":true,"first_name":"Marauders","username":"Eleven011Bot"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179011,"text":"Choose one letter:"}}''"
2018-01-17 14:20:13,297 (__init__.py:269 MainThread) INFO - TeleBot: "Started polling."
2018-01-17 14:20:13,322 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:20:13,342 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 1, 'timeout': 20} files=None"
2018-01-17 14:20:27,602 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[{"update_id":252965517,\n"message":{"message_id":105,"from":{"id":415492693,"is_bot":false,"first_name":"Archana","last_name":"Prabhu","language_code":"en-IN"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179025,"text":"a"}}]}''"
2018-01-17 14:20:27,636 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 1 new updates"
2018-01-17 14:20:27,658 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:20:27,659 (util.py:55 WorkerThread1) DEBUG - TeleBot: "Received task"
2018-01-17 14:20:27,687 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:20:27,705 (apihelper.py:45 WorkerThread1) DEBUG - TeleBot: "Request: method=post url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/sendMessage params={'chat_id': '415492693', 'text': 'a', 'reply_to_message_id': 105} files=None"
2018-01-17 14:20:27,730 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965518, 'timeout': 20} files=None"
2018-01-17 14:20:28,794 (apihelper.py:55 WorkerThread1) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":{"message_id":106,"from":{"id":491326980,"is_bot":true,"first_name":"Marauders","username":"Eleven011Bot"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179027,"reply_to_message":{"message_id":105,"from":{"id":415492693,"is_bot":false,"first_name":"Archana","last_name":"Prabhu","language_code":"en-IN"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179025,"text":"a"},"text":"a"}}''"
2018-01-17 14:20:28,876 (util.py:59 WorkerThread1) DEBUG - TeleBot: "Task complete"
2018-01-17 14:20:31,931 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[{"update_id":252965518,\n"message":{"message_id":107,"from":{"id":415492693,"is_bot":false,"first_name":"Archana","last_name":"Prabhu","language_code":"en-IN"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179030,"text":"d"}}]}''"
2018-01-17 14:20:32,025 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 1 new updates"
2018-01-17 14:20:32,086 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:20:32,088 (util.py:55 WorkerThread2) DEBUG - TeleBot: "Received task"
2018-01-17 14:20:32,149 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:20:32,207 (apihelper.py:45 WorkerThread2) DEBUG - TeleBot: "Request: method=post url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/sendMessage params={'chat_id': '415492693', 'text': 'd', 'reply_to_message_id': 107} files=None"
2018-01-17 14:20:32,266 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965519, 'timeout': 20} files=None"
2018-01-17 14:20:33,272 (apihelper.py:55 WorkerThread2) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":{"message_id":108,"from":{"id":491326980,"is_bot":true,"first_name":"Marauders","username":"Eleven011Bot"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179031,"reply_to_message":{"message_id":107,"from":{"id":415492693,"is_bot":false,"first_name":"Archana","last_name":"Prabhu","language_code":"en-IN"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179030,"text":"d"},"text":"d"}}''"
2018-01-17 14:20:33,351 (util.py:59 WorkerThread2) DEBUG - TeleBot: "Task complete"
2018-01-17 14:20:40,352 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[{"update_id":252965519,\n"message":{"message_id":109,"from":{"id":415492693,"is_bot":false,"first_name":"Archana","last_name":"Prabhu","language_code":"en-IN"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179038,"text":"/help","entities":[{"offset":0,"length":5,"type":"bot_command"}]}}]}''"
2018-01-17 14:20:40,435 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 1 new updates"
2018-01-17 14:20:40,495 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:20:40,496 (util.py:55 WorkerThread2) DEBUG - TeleBot: "Received task"
2018-01-17 14:20:40,545 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:20:40,582 (apihelper.py:45 WorkerThread2) DEBUG - TeleBot: "Request: method=post url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/sendMessage params={'chat_id': '415492693', 'text': 'Howdy, how are you doing?', 'reply_to_message_id': 109} files=None"
2018-01-17 14:20:40,621 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965520, 'timeout': 20} files=None"
2018-01-17 14:20:41,045 (apihelper.py:55 WorkerThread2) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":{"message_id":110,"from":{"id":491326980,"is_bot":true,"first_name":"Marauders","username":"Eleven011Bot"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179039,"reply_to_message":{"message_id":109,"from":{"id":415492693,"is_bot":false,"first_name":"Archana","last_name":"Prabhu","language_code":"en-IN"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179038,"text":"/help","entities":[{"offset":0,"length":5,"type":"bot_command"}]},"text":"Howdy, how are you doing?"}}''"
2018-01-17 14:20:41,098 (util.py:59 WorkerThread2) DEBUG - TeleBot: "Task complete"
2018-01-17 14:20:46,288 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[{"update_id":252965520,\n"message":{"message_id":111,"from":{"id":415492693,"is_bot":false,"first_name":"Archana","last_name":"Prabhu","language_code":"en-IN"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179044,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}}]}''"
2018-01-17 14:20:46,351 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 1 new updates"
2018-01-17 14:20:46,412 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:20:46,413 (util.py:55 WorkerThread1) DEBUG - TeleBot: "Received task"
2018-01-17 14:20:46,537 (apihelper.py:45 WorkerThread1) DEBUG - TeleBot: "Request: method=post url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/sendMessage params={'chat_id': '415492693', 'text': 'Howdy, how are you doing?', 'reply_to_message_id': 111} files=None"
2018-01-17 14:20:46,479 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:20:46,663 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965521, 'timeout': 20} files=None"
2018-01-17 14:20:47,010 (apihelper.py:55 WorkerThread1) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":{"message_id":112,"from":{"id":491326980,"is_bot":true,"first_name":"Marauders","username":"Eleven011Bot"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179045,"reply_to_message":{"message_id":111,"from":{"id":415492693,"is_bot":false,"first_name":"Archana","last_name":"Prabhu","language_code":"en-IN"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179044,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]},"text":"Howdy, how are you doing?"}}''"
2018-01-17 14:20:47,079 (util.py:59 WorkerThread1) DEBUG - TeleBot: "Task complete"
2018-01-17 14:21:06,919 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:21:06,979 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:21:07,043 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:21:07,100 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:21:07,162 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965521, 'timeout': 20} files=None"
2018-01-17 14:21:27,426 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:21:27,482 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:21:27,528 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:21:27,565 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:21:27,600 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965521, 'timeout': 20} files=None"
2018-01-17 14:21:47,808 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:21:47,860 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:21:47,913 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:21:47,967 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:21:48,020 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965521, 'timeout': 20} files=None"
2018-01-17 14:22:05,703 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[{"update_id":252965521,\n"message":{"message_id":113,"from":{"id":415492693,"is_bot":false,"first_name":"Archana","last_name":"Prabhu","language_code":"en-US"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179124,"text":"https://github.com/eternnoir/pyTelegramBotAPI#edited-message-handlers","entities":[{"offset":0,"length":69,"type":"url"}]}}]}''"
2018-01-17 14:22:05,798 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 1 new updates"
2018-01-17 14:22:05,854 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:22:05,855 (util.py:55 WorkerThread1) DEBUG - TeleBot: "Received task"
2018-01-17 14:22:05,970 (apihelper.py:45 WorkerThread1) DEBUG - TeleBot: "Request: method=post url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/sendMessage params={'chat_id': '415492693', 'text': 'https://github.com/eternnoir/pyTelegramBotAPI#edited-message-handlers', 'reply_to_message_id': 113} files=None"
2018-01-17 14:22:05,915 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:22:06,104 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:22:06,437 (apihelper.py:55 WorkerThread1) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":{"message_id":114,"from":{"id":491326980,"is_bot":true,"first_name":"Marauders","username":"Eleven011Bot"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179124,"reply_to_message":{"message_id":113,"from":{"id":415492693,"is_bot":false,"first_name":"Archana","last_name":"Prabhu","language_code":"en-US"},"chat":{"id":415492693,"first_name":"Archana","last_name":"Prabhu","type":"private"},"date":1516179124,"text":"https://github.com/eternnoir/pyTelegramBotAPI#edited-message-handlers","entities":[{"offset":0,"length":69,"type":"url"}]},"text":"https://github.com/eternnoir/pyTelegramBotAPI#edited-message-handlers","entities":[{"offset":0,"length":69,"type":"url"}]}}''"
2018-01-17 14:22:06,540 (util.py:59 WorkerThread1) DEBUG - TeleBot: "Task complete"
2018-01-17 14:22:26,357 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:22:26,390 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:22:26,422 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:22:26,456 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:22:26,493 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:22:46,716 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:22:46,770 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:22:46,822 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:22:46,877 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:22:46,934 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:23:07,169 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:23:07,203 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:23:07,242 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:23:07,277 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:23:07,321 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:23:27,931 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:23:27,990 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:23:28,050 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:23:28,119 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:23:28,173 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:23:48,431 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:23:48,488 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:23:48,532 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:23:48,572 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:23:48,614 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:24:08,850 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:24:08,878 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:24:08,908 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:24:08,937 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:24:08,966 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:24:29,168 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:24:29,203 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:24:29,239 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:24:29,273 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:24:29,309 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:24:49,529 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:24:49,583 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:24:49,635 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:24:49,691 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:24:49,744 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:25:09,995 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:25:10,084 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:25:10,122 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:25:10,158 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:25:10,193 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:25:30,422 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:25:30,452 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:25:30,482 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:25:30,510 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:25:30,539 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:25:50,753 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:25:50,781 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:25:50,810 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:25:50,840 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:25:50,871 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:26:11,070 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:26:11,122 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:26:11,170 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:26:11,221 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:26:11,271 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:26:31,511 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:26:31,561 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:26:31,610 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:26:31,661 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:26:31,710 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:26:51,938 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:26:51,967 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:26:51,995 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:26:52,024 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:26:52,052 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:27:12,256 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:27:12,306 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:27:12,357 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:27:12,407 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:27:12,455 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:27:32,688 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:27:32,755 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:27:32,787 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:27:32,820 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:27:32,854 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"
2018-01-17 14:27:53,055 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:27:53,105 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:27:53,144 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:27:53,180 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:27:53,215 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 252965522, 'timeout': 20} files=None"

 RESTART: C:/Users/Vidya Prabhu/AppData/Local/Programs/Python/Python36/python_telegram_bot_2.py 
2018-01-17 14:28:04,934 (__init__.py:269 MainThread) INFO - TeleBot: "Started polling."
2018-01-17 14:28:04,971 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:28:05,004 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 1, 'timeout': 20} files=None"
2018-01-17 14:28:26,571 (apihelper.py:55 PollingThread) DEBUG - TeleBot: "The server returned: 'b'{"ok":true,"result":[]}''"
2018-01-17 14:28:26,669 (__init__.py:195 PollingThread) DEBUG - TeleBot: "Received 0 new updates"
2018-01-17 14:28:26,719 (util.py:59 PollingThread) DEBUG - TeleBot: "Task complete"
2018-01-17 14:28:26,770 (util.py:55 PollingThread) DEBUG - TeleBot: "Received task"
2018-01-17 14:28:26,822 (apihelper.py:45 PollingThread) DEBUG - TeleBot: "Request: method=get url=https://api.telegram.org/bot491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA/getUpdates params={'offset': 1, 'timeout': 20} files=None"

 RESTART: C:/Users/Vidya Prabhu/AppData/Local/Programs/Python/Python36/python_telegram_bot_2.py 