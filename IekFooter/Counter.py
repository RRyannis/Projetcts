import os

html_file = "Iek_Project.html"

def update_counter():
    if os.path.exists(html_file):
        with open(html_file, "r", encoding="utf-8") as file:
            content = file.read()

        start_tag = "<div class=\"counter\">"
        end_tag = "</div class=\"counter\">"
        start_index = content.find(start_tag)
        end_index = content.find(end_tag)
        

        if start_index != -1 and end_index != -1:
            current_counter = int(content[start_index + len(start_tag):end_index])


            new_counter = current_counter + 1
            new_content = content[:start_index] + start_tag + str(new_counter) + end_tag + content[end_index + len(end_tag):]

            with open(html_file, "w", encoding="utf-8") as wfile:
                wfile.write(new_content)
                wfile.close()

            print("Visitors counter updated successfully.")
        else :
            print("Error: Visitors counter tags not found in HTML file")
    
    else:
        print("Error: HTML file '{html_file}' not found.")

update_counter()

