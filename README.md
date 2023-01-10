# emailtools

A Python library for email suggestions and validations.

## Installation

Install from [PyPI](https://pypi.org/project/emailtools) with pip by typing in your favorite terminal:

This will install `persian-names` (for generating random names).

`pip install emailtools`

## Usage

Let's take a look at what an example test case would look like using `emailtools`.

### Generate Random Emails:

```python
from emailtools import generate

generate() # Generates a random Email
# Example: Reza.Mahmoudi_2023@yahoo.com

generate('gmail') # Generates a random Gmail
# Example: Jafari_Niloufar@gmail.com

generate('gmail.com', 'Arash', 'Amiri')
# Example: Amiri-Arash1@gmail.com

generate('Proton', 'Bita', 'Alipour', 1995)
# Example: BitaAlipour.1995@proton.me
```

### Email Suggestions:

```python
from emailtools import generate

for i in range(10):
    print(generate('gmail', 'Saman', 'Rezaei', 1980))

# SamanRezaei@gmail.com
# Rezaei_Saman_1980@gmail.com
# Rezaei_Saman@gmail.com
# RezaeiSaman_1980@gmail.com
# Saman_Rezaei_1980@gmail.com
# Rezaei.Saman@gmail.com
# SamanRezaei@gmail.com
# Saman-Rezaei_1980@gmail.com
# Rezaei_Saman@gmail.com
# Saman-Rezaei1980@gmail.com
```

### Email Validations:

```python
from emailtools import validate

validate('Anahita.Faramarzi@gmail.com') # True
validate('Fariborz_Jalali20.gmail.com') # False
validate('Mohammadrezaei-Samina@gmail') # False
```

