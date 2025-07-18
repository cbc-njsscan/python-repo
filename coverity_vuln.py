import os

def run_command(user_input):
    # 🚨 Vulnerable: unsanitized input to os.system()
    os.system("ls " + user_input)

if __name__ == "__main__":
    user_input = input("Enter a directory name: ")
    run_command(user_input)
