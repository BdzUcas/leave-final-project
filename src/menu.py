from data import *
from gui import gui,gui_input
from MainGameGui import *
            
def choose_save_file(user_data):
    try:
        user_data['save_files']
    except:
        user_data['save_files'] = {gui_input('Name your first save file:'): {}}
    buttons = ['[' + i for i in user_data['save_files'].keys()]
    save_file = gui(['Choose save file:'] + buttons + ['[Create new save file'],15)
    if save_file == 'Create new save file':
        save_file = gui_input('Name your save file:')
        user_data['save_files'][save_file] = {}
    return user_data['save_files'][save_file]

def run_game(username,user_data):
    
    data = choose_save_file(user_data)
    print(data)
    if not data:
    #MAIN GAME FUNCTION GOES HERE
        game(1)
    else:
        game(data)
    json_dump(f'docs/{username}.json',user_data)
    launch_game()
def main():
    def get_users():
        users = csv_to_dictionary('docs/users.csv')
        #grab the username from each user and make them into a list
        return [user['username'] for user in users]
    def verify_account(username):
        return username in get_users()
    def login(user_data):
        while True:
            password = gui_input('Enter your password:')
            if encrypt(password) == user_data['password']:
                return True
            else:
                match gui(['Incorrect password!','[Try Again','[Back to Menu']):
                    case 'Try Again':
                        continue
                    case 'Back to Menu':
                        return False
    while True:
        match gui(['MAIN MENU','[Login','[Create Account','[Quit'],15):
            case 'Login':
                username = gui_input('Enter your username:')
                if verify_account(username):
                    user_data = json_pull(f'docs/{username}.json')
                    if not user_data:
                        gui([f'There was an error getting the data from this account!','Please make a new one.','[Back to Menu'])
                        continue
                    if not login(user_data):
                        continue
                    run_game(username,user_data)
                else:
                    gui([f'The username {username} is not associated with an account!','[Back to Menu'])
                    continue 

            case 'Create Account':
                username = gui_input('Enter your username:')
                if verify_account(username):
                    gui(['That username has been taken!','[Back to Menu'])
                    continue
                password = encrypt(gui_input('Enter a password:'))
                user_data = {'password':str(password)}
                create_json(f'docs/{username}.json')
                json_dump(f'docs/{username}.json',user_data)
                users = csv_to_dictionary('docs/users.csv')
                users.append({'username':username})
                save_csv(users,'docs/users.csv')
                run_game(username,user_data)
            case 'Quit':
                return

main()