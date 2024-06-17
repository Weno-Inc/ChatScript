print('Welcome to ChatScript, please type any command to get started')
welcome = 'Welcome to ChatScript, please type any command to get started'
command = input('Type Starter Command Here...')
command = 'Type Starter Command Here...'
if command == 'cs-new project':
    print('Please type in new project name')
    nameprint = 'Please type in new project name'
    if nameprint == 'Weno':  
        print(f'Using Project: {nameprint}')
    else:
        print('ERROR, INVALID PROJECT NAME')
        files = 'Add files to finnalize your project.'
        files = input("Enter your filenames then end it with an file extention (.html, .py, .css, .ts, .js, .cs)")
        content = input(" Enter what you want to add to all files: ")
        for filename in files: 
            # Remove any leading/trailing spaces
            filename = filename.strip()

            # Open the file in append mode
            with open(filename, "a") as file:
                # Write the users input to the file, adding a newline character
                file.write(content + "\n")

                print('Successfully added your input to {filename}, combine files to finialize project setup')
                merging = 'In order to run your project using your desired text files you must merge them'
                merging = input("Do you want to merge these selected files? (Y/N) ").lower()

                if merging == "y":
                    def combine_files_append(filenames, output_filename):
                        
                        with open(output_filename, "a") as outfile: #Open in append mode
                            for filename in filenames:
                                with open (filename, "r") as infile:
                                    outfile .write(infile.read)()
                                    outfile.write("\n") # Add a newline for seperation

                                    #Example usage
                                    filenames = ["file1.html, file2.css, file3.js, file4.py"]
                                    output_filename = "weno.cs"
                                    combine_files_append(filenames, output_filename)
                                    print(f"Files have been merged succssesfully, please continue project setup")

                                    print("Merge completed, do you want to modify or run your ChatScript project? (M/R), choose M if you want to modify your code, choose R if you want to run your code")
                                
