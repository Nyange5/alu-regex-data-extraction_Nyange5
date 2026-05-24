import re
import json


#open and read the raw text file
with open("../input/raw-text.txt", "r") as file:
    raw_text = file.read()

# Safety check
if "<script>" in raw_text or "DROP TABLE" in raw_text:
    print("\nSecurity Alert: Unsafe content detected")

# Patterns

# 1. Email pattern
email_address_regex = r'[a-zA-Z0-9.]+@(?:(?:alumni|si)\.)?alueducation\.com'

# 2. Time pattern
time_regex = r'\d{2}:\d{2}:\d{2}'

# 3. Phone number pattern
phone_number_regex = r'\+2507[2389][0-9]{7}'

# 4. Credit card pattern
credit_card_regex = r'\b(?:\d{4}[- ]?){3}\d{4}\b'

# Hide credit card number
correct_cards = []
for card in re.findall(credit_card_regex, raw_text):
    last_four = card.replace(" ", "-")[-4:]  # This grabs the last 4 digits
    correct_cards.append("****-****-****-" + last_four)

# Extraction of accurate data
correct_email_address = re.findall(email_address_regex, raw_text)
correct_time = re.findall(time_regex, raw_text)
correct_number = re.findall(phone_number_regex, raw_text)

# Printing the results

print("\nValid ALU Email addresses:")
for email in correct_email_address:
    print(" -", email)

print("\nValid Time:")
for time in correct_time:
    print(" -", time)

print("\nValid Phone numbers:")
for number in correct_number:
    print(" -", number)

print("\nValid Credit cards:")
for card in correct_cards:
    print(" -", card)

# Saving everything to a json file
output = open("../output/sample-output.json", "w", encoding="utf-8")
json.dump({
    "emails": correct_email_address,
    "phone_numbers": correct_number,
    "times": correct_time,
    "credit_cards": correct_cards
}, output, indent=4)
output.close()

print("\nResults saved to output/sample-output.json")
