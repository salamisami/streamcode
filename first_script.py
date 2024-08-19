"""_summary_

    Raises:
        ValueError: _description_
        ValueError: _description_
        IOError: _description_
"""
import csv
import os
import sys
import traceback

def update_user_counter(csv_file, _username):
    """_summary_

    Args:
        csv_file (_type_): username, counter;
        _username (_type_): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_
        IOError: _description_
    """
    try:
        if not _username.strip():
            raise ValueError("Username cannot be empty.")

        user_found = False
        rows = []
        count =1
        if os.path.exists(csv_file):
            try:
                with open(csv_file, encoding='ascii', mode='r', newline='') as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                    #print(f"Using CSV file: {csv_file}") #debugging line if csv doesnt "save"


                if rows and rows[0] != ['user', 'counter']:
                    rows.insert(0, ['user', 'counter'])
                for i, row in enumerate(rows):
                    if row[0] == _username:
                        count = int(row[1]) + 1  # Increment the counter
                        rows[i][1] = str(count)
                        user_found = True
                        break

            except csv.Error as e:
                raise ValueError(f"Error reading the CSV file: {e}")
        if not user_found:
            rows.append([_username, '1'])

        try:
            with open(csv_file, encoding='ascii', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
                print(f"{_username} has been first for {count} times.")
        except IOError as e:
            raise IOError(f"Error writing to the CSV file: {e}")

    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{csv_file}'.")
    except ValueError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print(traceback.format_exc())

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python script.py <username>")
    else:
        CSV_FILE_PATH = 'user_data.csv'
        username = sys.argv[1]
        update_user_counter(CSV_FILE_PATH, username)
