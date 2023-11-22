import datetime


class GuestTracker:
    def __init__(self, file_path, guest_list):
        self.file_path = file_path
        self.guest_list = guest_list

    def date_time(self):
        return datetime.datetime.now()

    def horizontal_line(self, line_length):
        return '___' * line_length

    def generate_guest_entry(self, user_id, user_name, entry_time):
        return f'User ID: {user_id}\nGuest Name: {user_name.title()}\nEntry Time: {str(entry_time)}\n'

    def guest_prompt(self):
        user_id = input('\nEnter your User ID or Quit: ')
        return user_id.lower()

    def reading_file(self):
        entry_time = self.date_time()
        while True:
            user_id = self.guest_prompt()

            if user_id == 'quit':
                print('Ending Program')
                break

            if user_id in self.guest_list:
                user_name = self.guest_list[user_id]
                with open(self.file_path, 'a') as file_obj:
                    guest_entry = self.generate_guest_entry(user_id, user_name, entry_time)
                    file_obj.write(guest_entry)

                # read file
                with open(self.file_path, 'r') as file_content:
                    guest_book_info = file_content.read()
                    print(guest_book_info)
                    print(self.horizontal_line(18))
            else:
                print('Access Denied. Try again!')


# Define guest list with user ID and name mappings
guest_list = {'001': 'Mike',
              '002': 'Bob',
              '003': 'Ruth',
              '004': 'James',
              '005': 'John',
              '006': 'Patric',
              '007': 'Stanley'
              }

file_path = 'text.txt'

# Create an instance of GuestTracker
guest_tracker = GuestTracker(file_path, guest_list)

# Start tracking guest entries
guest_tracker.reading_file()
