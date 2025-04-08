# Random-Username-Generator
Random Username Generator with GUI


 Project Title:
Random Username Generator (GUI-based Python Application)

🔹 Objective:
The goal of this project is to create a simple, interactive application that generates unique and creative usernames. The user can customize the output by choosing whether to include numbers, special characters, and even set a maximum username length. The program is equipped with a graphical user interface (GUI) for ease of use and saves generated usernames to a file.

🔹 Technologies Used:
Programming Language: Python 3

Libraries:

tkinter – for building the graphical user interface (GUI)

random – for generating random selections

datetime – for adding the current date to saved files

🔹 Features:
Generates random usernames by combining adjectives and nouns.

Option to add random numbers (e.g., EpicNinja23).

Option to add special characters (e.g., HappyTiger@).

Users can specify the number of usernames to generate.

Users can set a maximum username length.

GUI-based – no need for command-line input.

Saves usernames to a text file named using the current date (e.g., usernames_2025-04-08.txt).

Automatically avoids duplicate usernames using a Python set.

🔹 How It Works:
User Input (via GUI):

Number of usernames to generate.

Whether to include numbers or special characters.

Optional max length of the usernames.

Username Generation:

Randomly selects one adjective and one noun.

Optionally appends numbers and/or special characters.

Trims the username if it exceeds the user-defined length.

Output Display:

The generated usernames are displayed in a text box inside the GUI.

Saving to File:

When the user clicks “Save to File,” the usernames are written to a text file with the current date.

🔹 Sample Output:
If the user selects to generate 5 usernames, including numbers, and sets a maximum length of 14 characters, sample results might be:

Copy
Edit
👉 WittyTiger93  
👉 FunkyNinja87  
👉 ChillWizard25  
👉 SwiftPanda19  
👉 EpicShadow42
🔹 Use Cases:
Quick creation of usernames for websites or apps.

Game nickname generator.

Identity masking or placeholder usernames in UI/UX design.

🔹 Possible Improvements:
Add multilingual support for adjectives/nouns.

Integrate with APIs for real-time name suggestions.

Export to CSV or Excel format.

Web-based version using Flask or Streamlit.

Add themes or categories (e.g., funny, professional, gamer, etc.).
