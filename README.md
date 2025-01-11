# username_generator_fix
A Python script to generate usernames from a list of names with various transformations. Useful for penetration testing and brute force attack preparation (ethical purposes only).

# Username Generator Fix

A Python script to generate usernames from a list of names with various transformations. Useful for penetration testing and brute force attack preparation (ethical purposes only).

## Features

- Generate usernames from a list of names in various formats (lowercase and uppercase transformations).
- Handles common issues like empty or single-word lines in the input file.
- Command-line arguments for customization.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/username-generator-fix.git
    cd username-generator-fix
    ```

2. Ensure you have Python 3 installed:
    ```bash
    python3 --version
    ```

3. Install dependencies (if any).

## Usage

Run the script with a wordlist file as input:

```bash
python3 username_generator_fix.py -w wordlist.lst
