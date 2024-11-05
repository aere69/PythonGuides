# ----------------  CONSTANT DEFINITIONS -------------------------------

PLACEHOLDER = "[name]"
PATH_TO_PROJECT = "./Projects/Intermediate/SimpleMailMerge"
filename = PATH_TO_PROJECT + "/Input/Names/invited_names.txt"

# ---------------- FUNCTION DEFINITIONS --------------------------------

def clean_name(name):
    """Returns a clean name. No leading or trailing spaces or new line"""
    clean_name = name.strip()
    clean_name = clean_name.strip("\n")
    return clean_name

def load_doc_template(file_name):
    """Returns the content of the file."""
    with open(file_name) as file:
        doc = file.read()
    return doc

def create_invitation(to, document):
    """Takes a name (to) and a document template and creates a new file with PLACEHODER replaced in the document template"""
    doc = document.replace(PLACEHOLDER, to)
    to = to.replace(" ", "_")
    filename = PATH_TO_PROJECT+"/Output/ReadyToSend/"+to+"_invitation_letter.txt"
    with open(filename, "w") as file:
        file.write(doc)

# ------------------- MAIN CODE --------------------------------

try:
    # f = open(filename, "r")
    with open(filename) as file:
        f = file.readlines()
    
    template = load_doc_template(PATH_TO_PROJECT+"/Input/Letters/starting_letter.txt")

    for invited_name in f:
        create_invitation(clean_name(invited_name),template)

except FileNotFoundError:
    print(f"Error - File not found.")
    exit()
except:
    print(f"Something went wrong.")
    exit()
else:
    # There were no exceptions
    pass
finally:
    # This will always happen
    pass

