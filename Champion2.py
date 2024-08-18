# ****************************************************************************************************
#
# File name:   Champion2.py
# Description:  This program will create a dictionary for the world series winners.
# other fle:    WorldSeriesWinners.txt
#
# ****************************************************************************************************

def get_dict(team_list):
    team_dict = {}
    try:
        with open(team_list, 'r') as file:
            years = 1903
            for line in file:
                team_name = line.strip()
                if team_name != "none":
                    if team_name in team_dict:
                        team_dict[team_name].add(years)
                    else:
                        team_dict[team_name] = {years}
                years += 1
    except FileNotFoundError:
        print(f"Error: {team_list} not found.")
    except Exception as e:
        print(f"An error occurred while reading the file")

    return team_dict


# ****************************************************************************************************

def display(team_dict):
    for team, years in team_dict.items():
        if team != "none":
            print(f"Team name: {team}:")
            years_list = sorted(list(years))
            for i in range(0, len(years_list), 8):
                year_chunk = years_list[i:i + 8]
                for year in year_chunk:
                    print(year, end=' ')
                print()
                print()


# ****************************************************************************************************

def main():
    team_list = "WorldSeriesWinners.txt"
    team_dict = get_dict(team_list)

    while True:
        print('-' * 50)
        print("1. View a team info")
        print("2. View all team info")
        print("3. Delete a team info")
        print("4. Change team info")
        print("5. Quit")

        choice = input("please chose an option: ")

        if choice == "1":
            team_name = input("Enter the team name: ")
            if team_name in team_dict:
                print(f"Winning years for {team_name}:")
                years_list = sorted(list(team_dict[team_name]))
                for year in years_list:
                    print(year, end=' ')
                print()
            else:
                print(f"{team_name} not found in the records.")

        elif choice == "2":
            display(team_dict)

        elif choice == "3":
            team_name = input("Enter the team name: ")
            if team_name in team_dict:
                del team_dict[team_name]
                print(f"{team_name} deleted.")
            else:
                print(f"{team_name} not found in the records.")

        elif choice == "4":
            team_name = input("Enter a team name to change: ")
            if team_name in team_dict:
                new_years = set(map(int, input("Enter the new set of winning year(s): ").split(' ')))
                team_dict[team_name] = new_years
                print(f"{team_name}'s changed.")
            else:
                print(f"{team_name} not found in the records.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# ****************************************************************************************************

if __name__ == '__main__':
    main()

# ****************************************************************************************************
