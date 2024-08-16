import json

def handle_user(action):
    try:
        with open('user_data.json', 'r') as f:
            user_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        user_data = {}

    if action == 'signup':
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        mobile = input('Enter your mobile number: ')

        if username in user_data:
            print("Username already exists!")
        else:
            user_data[username] = {
                'password': password,
                'mobile': mobile
            }
            with open('user_data.json', 'w') as f:
                json.dump(user_data, f, indent=4)
            print("Signup successful!")

    elif action == 'signin':
        username = input('Enter your username: ')
        password = input('Enter your password: ')

        if username in user_data and user_data[username]['password'] == password:
            print('Login successful!')
            print(f"Welcome to the device! Your mobile number is: {user_data[username]['mobile']}")
        else:
            print('Incorrect credentials. Terminating program.')

def main():
    while True:
        print('1) Sign up')
        print('2) Sign in')
        print('3) Exit')
        
        choice = int(input('Enter your choice: '))
        
        if choice == 1:
            handle_user('signup')
        elif choice == 2:
            handle_user('signin')
        elif choice == 3:
            break
        else:
            print('Invalid choice!')

if __name__ == "__main__":
    main()
