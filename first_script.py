import csv
import os
import sys
import traceback

def update_user_counter(csv_file, username):
    try:
        if not username.strip():
            raise ValueError("Username cannot be empty.")

        user_found = False
        rows = []
        count =1
        if os.path.exists(csv_file):
            try:
                with open(csv_file, mode='r', newline='') as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                    #print(f"Using CSV file: {csv_file}") #debugging line if csv doesnt "save"


                if rows and rows[0] != ['user', 'counter']:
                    rows.insert(0, ['user', 'counter'])
                for i, row in enumerate(rows):
                    if row[0] == username:
                        count = int(row[1]) + 1  # Increment the counter
                        rows[i][1] = str(count)
                        user_found = True
                        break

            except csv.Error as e:
                raise ValueError(f"Error reading the CSV file: {e}")
        
        if not user_found:
            rows.append([username, '1'])

        try:
            with open(csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
                print(f"{username} has been first for {count} times.")
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
        csv_file_path = 'user_data.csv'
        username = sys.argv[1]
        update_user_counter(csv_file_path, username)
