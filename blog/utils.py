# blog/utils.py

import re
import math

def calculate_reading_time(content):
    words = re.findall(r'\w+', content)
    word_count = len(words)
    words_per_minute = 200  # Adjust this value as needed for your content
    reading_time = math.ceil(word_count / words_per_minute)
    return reading_time
