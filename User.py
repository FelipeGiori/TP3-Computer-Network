import pandas as pd

class User:
    def __init__(self):
        self.users = pd.DataFrame(columns = ["username", "password", "message"])


    def register_user(self, username, password):
        # Check if there is a user with the same username
        if(sum(self.users.username == username) > 0):
            return "N -1"
        else:
            self.users.loc[self.users.shape[0]] = [username, password, None]
            return "N 0"


    def auth_user(self, username, password):
        '''
            Error Code:
            -1: User does not exist
            -2: Incorrect password
        '''
        # Retrieve all the information from a user. If no such information exists, then the user doesn't exist
        # If a user with that username exists, then the passwords are compared.
        user = self.users[self.users.username == username]
        if(user.shape[0] == 0):
            return -1
        elif(user.password[user.index[0]] == password):
            return True
        else:
            return -2


    def store_message(self, rcv_msg):
        # Message info
        username = rcv_msg[1]
        password = rcv_msg[2]
        filename = rcv_msg[3]
        file_content = " ".join(rcv_msg[4: ])

        signal = self.auth_user(username, password)

        # Account auth related signals
        if(signal == -1):
            return "S -1"
        elif(signal == -2):
            return "S -2"
        else:
            # filename related signals
            signal = self.check_file_exists(username, filename)
            user_id = self.users.index[self.users.username == username][0]

            # Python dictionaries are being used as file structure: {(key)filename: (content)file_content}
            # If no files exist, creates a dictionary structure and adds a file to it
            if(signal == 2):
                content = {filename: file_content}
                self.users.at[user_id, 'message'] = content
                return "S 0"
            
            # Replaces the content related to a key
            elif(signal == 1):
                files = self.users.message[self.users.username == username]
                files = files[files.index[0]]
                files[filename] = file_content
                self.users.at[user_id, 'message'] = files
                return "S 1"

            # Creates a new key and assigns content to it
            elif(signal == 0):
                files = self.users.message[self.users.username == username]
                files = files[files.index[0]]
                files[filename] = file_content
                self.users.at[user_id, 'message'] = files
                return "S 0"


    def check_file_exists(self, username, filename):
        '''
            Error code:
            2: No files associated with user
            1: There is a file with the same name
            0: There is files, but not with the same name
        '''
        # Get all files associated with the username
        files = self.users.message[self.users.username == username]
        if(files[files.index[0]] == None):
            return 2
        
        list_files = list(files[files.index[0]].keys())
        if(filename in str(list_files)):
            return 1
        else:
            return 0


    def retrieve_message(self, rcv_msg):
        # Message info
        username = rcv_msg[1]
        password = rcv_msg[2]
        filename = rcv_msg[3]

        signal = self.auth_user(username, password)

        # Account auth related signals
        if(signal == -1):
            return "R -1"
        elif(signal == -2):
            return "R -2"
        else:
            # filename related signals
            signal = self.check_file_exists(username, filename)
            if((signal == 2) or (signal == 0)):
                return "R -3"
            else:
                files = self.users.message[self.users.username == username]
                files = files[files.index[0]]
                return "R 0 " + files[filename]


    def retrieve_filenames(self, username, password):
        signal = self.auth_user(username, password)

        # Account auth related signals
        if(signal == -1):
            return "L -1"
        elif(signal == -2):
            return "L -2"
        else:
            # Get all files associated with the username
            files = self.users.message[self.users.username == username]
            files = files[files.index[0]]
            if(files == None):
                return "L 0"
            else:
                # Retrieve the keys (filenames)
                filenames = list(files.keys())
                filenames = " ".join(filenames)
                return "L 0 " + filenames