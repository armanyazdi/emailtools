# emailtools

[![PyPI](https://img.shields.io/pypi/v/emailtools?style=for-the-badge&color=ee999f&labelColor=302d41)](https://pypi.org/project/emailtools)
[![GitHub](https://img.shields.io/github/license/armanyazdi/emailtools?style=for-the-badge&color=8cd5ca&labelColor=302d41)](https://pypi.org/project/emailtools)

A Python library for email suggestions and validations.

## Installation

Install from [PyPI](https://pypi.org/project/emailtools) with pip by typing in your favorite terminal:

This will install `persian-names` (for generating random names).

`pip install emailtools`

## Usage

Let's take a look at what an example test case would look like using `emailtools`.

### Generate Random Emails:

Note: You can use the name of email providers or their domains for the first argument.

```python
from emailtools import generate

# generate('EmailProvider', 'FirstName', 'LastName', BirthYear)

generate() # Generates a random email
# Example: Reza.Mahmoudi_2023@yahoo.com

generate('gmail') # Generates a random Gmail
# Example: Jafari_Niloufar@gmail.com

generate('gmail.com', 'Arash', 'Amiri')
# Example: Amiri-Arash1@gmail.com

generate('Outlook', 'Bita', 'Alipour', 1995)
# Example: BitaAlipour.1995@outlook.com
```

### Suggest Email Usernames:

```python
from emailtools import generate

for i in range(10):
    print(generate('Gmail', 'Saman', 'Rezaei', 1980))

# SamanRezaei@gmail.com
# Rezaei_Saman_1980@gmail.com
# Rezaei_Saman@gmail.com
# RezaeiSaman_5@gmail.com
# Saman_Rezaei_1980@gmail.com
# Rezaei.Saman@gmail.com
# RezaeiSaman7@gmail.com
# Saman-Rezaei_1@gmail.com
# Rezaei_Saman@gmail.com
# Saman.Rezaei1980@gmail.com
```

### Validate Emails:

```python
from emailtools import validate

validate('Anahita.Faramarzi@gmail.com') # True
validate('Fariborz_Jalali20.gmail.com') # False
validate('Mohammadrezaei-Arash7@gmail') # False
```