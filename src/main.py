import subprocess
command_history = []
def commandInput():
    while True:
        print()
        prompt = input("$  ")

        command_history.append(prompt)

        if prompt.strip() == "exit":
            print("Exiting the Fortnite Shell...")
            break

        if prompt == "cls":
            try:
                result = subprocess.run(["cls"], shell=True, capture_output=True, text=True, check=True)  # clear screen
                print(result.stdout)  
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
        if prompt == "dir":
            try:
                result = subprocess.run(["dir"], shell=True, capture_output=True, text=True, check=True)  # list directory
                print(result.stdout)  
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
        
        
        elif prompt == "Fortnite Version":
            try:
                result = subprocess.run(["python", "--version"], capture_output=True, text=True)  # check Python version
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
        
        
        elif prompt == "Fortnite Battlepass":
            try:
                result = subprocess.run(["python", "src\fortniteBattlepass.py"], capture_output=True, text=True)  # run the script
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
        elif prompt == "History":
            print("Command History:")
            for i, command in enumerate(command_history, start=1):
                print(f"{i}: {command}")
            
        else:
            try:
                # Run everything through PowerShell
                result = subprocess.run(["powershell", "-Command", prompt], capture_output=True, text=True)
                if result.stdout:
                    print(result.stdout.strip())
                if result.stderr:
                    print(result.stderr.strip())
            except Exception as e:
                print(f"Error: {e}")

def main():
    print("Welcome to the Fortnite Shell!")
    print("Type 'exit' to quit the program.")
    commandInput() 

if __name__ == "__main__":
    main()
