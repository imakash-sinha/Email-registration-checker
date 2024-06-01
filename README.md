
# Email Registration Checker

The **Email Registration Checker** is a Python tool designed to verify whether an email address is registered on a predefined set of websites. It offers a command-line interface for easy usage.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/imakash-sinha/email-registration-checker.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd email-registration-checker
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following command:
   ```bash
   python email_registration_checker.py <email_address> [--websites <website1> <website2> ...]
   ```

Replace `<email_address>` with the email address you want to check and `<website1> <website2> ...` with the optional list of websites to check against.

### Example

```bash
python email_registration_checker.py example@gmail.com --websites amazon.com github.com twitter.com
```

## Output

The tool will display the registration status for each specified website, indicating whether the email address is registered or not.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

