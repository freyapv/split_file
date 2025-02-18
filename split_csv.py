import csv
import sys

def split_csv(input_file):
    usernames_file = "usernames.txt"
    passwords_file = "passwords.txt"

    try:
        with open(input_file, "r") as csvfile, \
             open(usernames_file, "w") as user_file, \
             open(passwords_file, "w") as pass_file:

            reader = csv.reader(csvfile)

            for row in reader:
                if len(row) != 2:
                    print(f"Skipping invalid line: {row}")
                    continue
                
                username, password = row
                user_file.write(username.strip() + "\n")
                pass_file.write(password.strip() + "\n")

        print(f"✅ Usernames saved in {usernames_file}")
        print(f"✅ Passwords saved in {passwords_file}")

    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_csv.py <input_file.csv>")
    else:
        split_csv(sys.argv[1])
 
