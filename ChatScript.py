class Weno:
    def __init__(self):
        self.welcome = 'Welcome to ChatScript, type any command to get started'
        self.command_process()

    def command_process(self):
        self.command = input('Type Starter Command Here...')
        if self.command == 'cs-new project':
            self.new_project()

    def new_project(self):
        print('Please type in new project name')
        self.project_name = input()
        if self.project_name:
            print(f'Using Project: {self.project_name}')
            self.manage_project()
        else:
            print('ERROR, INVALID PROJECT NAME')

    def manage_project(self):
        files = input("Enter filenames (end with .html, .py, .css, .ts, .js, .chat): ")
        files = files.split(',')
        self.files = [f.strip() for f in files]
        content = input(" Enter content to add to all files: ")
        self.add_content_to_files(content)

    def add_content_to_files(self, content):
        for filename in self.files: 
            with open(filename, "a") as file:
                file.write(content + "\n")
            print(f'Successfully added your input to {filename}')
        self.check_merge()

    def check_merge(self):
        merging = input("Do you want to merge these selected files? (Y/N) ").lower()
        if merging == "y":
            self.merge_files()

    def merge_files(self):
        output_filename = f'{self.project_name}.chat'
        with open(output_filename, "a") as outfile: 
            for filename in self.files:
                with open(filename, "r") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")
            print(f"Files have been merged successfully, project setup complete")

Weno()
