import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the website
url = "https://www.check4d.org/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define the letters to use: 'm', 'd', and 't'
    letters = ['m', 'd', 't']

    with open("results.txt", "w") as file:
        for letter in letters:


            if letter == 'm':
                word = "Magnum"
            elif letter == 'd':
                word = "Damacai"
            else:
                word = "Toto"


            file.write("\n"+ word +" Results\n\n")

            ## FIRST THREE PLACES

            # Define the prize places and their corresponding IDs
            prize_places = {
                "First Place": f"{letter}p1",
                "Second Place": f"{letter}p2",
                "Third Place": f"{letter}p3"
            }

            for place, id_value in prize_places.items():
                specific_number_element = soup.find('td', {'id': id_value})
                if specific_number_element:
                    specific_number = specific_number_element.get_text()

                    file.write(f"{specific_number}\n")


                else:
                    file.write(f"{place}: Element not found\n")

            ## SPECIAL PRICE
            
            ms_numbers = []  # Initialize a list to store the "ms" numbers

            # Define a range from 1 to 10 and loop through it
            for i in range(1, 11):
                specific_number_element = soup.find('td', {'id': f"{letter}s{i}"})
                if specific_number_element:
                    specific_number = specific_number_element.get_text()
                    if specific_number != '----' and specific_number != '****':
                        ms_numbers.append(specific_number)

            file.write( "    ".join(ms_numbers) + "\n")

            ## CONSOLATION PRICE
            
            mc_numbers = []  # Initialize a list to store the "ms" numbers

            # Define a range from 1 to 10 and loop through it
            for i in range(1, 11):
                specific_number_element = soup.find('td', {'id': f"{letter}c{i}"})
                if specific_number_element:
                    specific_number = specific_number_element.get_text()
                    if specific_number != '----' and specific_number != '****':
                        mc_numbers.append(specific_number)

            file.write( "    ".join(mc_numbers) + "\n")

else:
    print("Failed to fetch the page")
