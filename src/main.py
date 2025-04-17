import subprocess

def commandInput():
    while True: 
        print()  
        prompt = input("$  ")  

        
        if prompt == "exit":
            print("Exiting the Fortnite Shell...")
            break  # exit the program

        
        elif prompt == "cls":
            try:
                result = subprocess.run(["cls"], shell=True, capture_output=True, text=True, check=True)  # clear screen
                print(result.stdout)  
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")


        elif prompt == "dir":
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
        
        else:
            print(f"Unknown command: {prompt}")

def main():
    print("Welcome to the Fortnite Shell!")
    print("Type 'exit' to quit the program.")
    commandInput() 

if __name__ == "__main__":
    main()
