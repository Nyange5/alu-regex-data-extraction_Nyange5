# ALU Regex Data Extraction

a python script that reads a text file with support tickets and pulls out emails, phone numbers, times and credit cards. it also checks if the input has anything dangerous before doing anything.

---

## Project Structure

```
alu-regex-data-extraction/
├── input/
│   └── raw-text.txt        
├── src/
│   └── main.py             
├── output/
│   └── sample-output.json  
└── README.md
```

---

## How to run it

```bash
cd src
python3 main.py
```

---

## What it does

- pulls out ALU emails only (staff, alumni and SI)
- finds valid Rwanda phone numbers
- finds timestamps
- masks credit card numbers so only last 4 digits show
- warns you if the input has SQL injection or script attacks

---

## What you will see

```
Security Alert: Unsafe content detected

Valid ALU Email addresses:
 - amara.diallo@alueducation.com
 - fatima.nkosi@alumni.alueducation.com

Valid Time:
 - 14:35:00

Valid Phone numbers:
 - +250781234789

Valid Credit cards:
 - ****-****-****-1234

Results saved to output/sample-output.json
```

---

## Requirements

just Python 3, nothing else to install

