import re
import logging

def find_errors_in_log(log_file_path, error_log_path):
    # Define error patterns
    error_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in ['ERROR', 'WARNING', 'CRITICAL']]

    # Set up logging
    logging.basicConfig(filename=error_log_path, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Read log file and search for errors
    try:
        with open(log_file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                for pattern in error_patterns:
                    if pattern.search(line):
                        error_message = f"Line {line_number}: {line.strip()}"
                        print(error_message)

                        # Log error to file
                        logging.error(error_message)
    except FileNotFoundError:
        print(f"File not found: {log_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Get file paths from user
    log_file_path = input("Please enter the path to your log file: ")
    error_log_path = input("Please enter the path to save the error log: ")
    
    find_errors_in_log(log_file_path, error_log_path)

if __name__ == "__main__":
    main()

