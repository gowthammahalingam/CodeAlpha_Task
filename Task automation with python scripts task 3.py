import os
import re

def extract_emails_from_file():
    print("--- Task Automation: Extract Email Addresses ---")
    input_filename = input("Enter the name of the text file to read emails from (e.g., input.txt): ")
    output_filename = input("Enter the name of the file to save extracted emails to (e.g., emails.txt): ")

    # Check if the input file exists
    if not os.path.exists(input_filename):
        print(f"Error: The file '{input_filename}' does not exist.")
        print("-" * 20)
        return

    try:
        # Read the entire content of the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
    except IOError as e:
        print(f"Error reading input file: {e}")
        print("-" * 20)
        return

    # Regular expression to find email addresses:
    # \b          - Word boundary
    # [A-Za-z0-9._%+-]+ - One or more letters, numbers, and specific symbols before @
    # @           - The '@' symbol
    # [A-Za-z0-9.-]+ - One or more letters, numbers, hyphens, or dots after @
    # \.          - A literal dot (escaped with backslash)
    # [A-Z|a-z]{2,} - Two or more letters for the domain extension (e.g., com, org, net)
    # \b          - Word boundary
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all matches in the content
    extracted_emails = re.findall(email_pattern, content)

    if not extracted_emails:
        print("No email addresses found in the file.")
    else:
        print(f"Found {len(extracted_emails)} email address(es).")
        try:
            # Write the extracted emails to the output file, one per line
            with open(output_filename, 'w') as outfile:
                for email in extracted_emails:
                    outfile.write(email + '\n')
            print(f"Extracted emails saved to {output_filename}")
        except IOError as e:
            print(f"Error writing output file: {e}")
    print("-" * 20)

# --- How to test this task: ---
# 1. Create a text file named, for example, 'test_emails.txt' in the same directory
#    as your Python script.
# 2. Put some text in 'test_emails.txt', including a few email addresses:
#    Example content for 'test_emails.txt':
#    My email is user@example.com. Please send inquiries to info-support@company.org.
#    Contact John at john.doe123@mail.co.uk. No email here. another.one@domain.net
#
# To run the Email Extractor:
if __name__ == "__main__":
    # Optional: Create a dummy file for quick testing.
    # You can comment out the following lines if you prefer to create the file manually.
    dummy_input_filename = "dummy_input_emails.txt"
    with open(dummy_input_filename, "w") as f:
        f.write("Contact us at test@example.com or support@company.org. My personal email is user.name@domain.co.uk.\n")
        f.write("No email here. Just some text.\n")
        f.write("Another email: info@web.net\n")
    print(f"\nNote: A dummy file '{dummy_input_filename}' has been created for quick testing.")
    print("When prompted, enter 'dummy_input_emails.txt' for the input file.")

    extract_emails_from_file()