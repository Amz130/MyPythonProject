import csv  # To read the CSV file

# Class representing a political party
class Party:
    def __init__(self, name):
        self.name = name  # Name of the party
        self.members = 0  # Count of MPs in the party
        self.votes = 0  # Total votes received by the party

    def increment_member_count(self):
        """Increases the member count by one."""
        self.members += 1

    def increment_votes(self, votes):
        """Adds votes to the party's total."""
        self.votes += int(votes)

    def __str__(self):
        """Returns a summary of the party's members and votes."""
        return f"{self.name} has {self.members} members and {self.votes} total votes."


# Class representing a Member of Parliament
class MP:
    def __init__(self, name, constituency, party):
        self.name = name  # Full name of the MP
        self.constituency = constituency  # Constituency the MP represents
        self.party = party  # The MP's political party
        self.votes = 0  # Votes received by the MP

    def add_votes(self, votes):
        """Assigns votes to the MP."""
        self.votes = int(votes)

    def __str__(self):
        """Returns a summary of the MP's details."""
        return f"{self.name}, MP for {self.constituency}, belongs to {self.party} and received {self.votes} votes."


# Function to read and process the CSV file
def read_file(file_name):
    """Reads the CSV file, processes MPs and parties, and prints party statistics."""
    mp_list = []  # List to store MP objects
    party_list = {}  # Dictionary to store Party objects

    # Open and read the CSV file
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Extract MP details from the row
            mp_name = f"{row['Member first name']} {row['Member surname']}"
            constituency = row['Constituency name']
            party_name = row['First party']

            # Determine the votes based on party type
            if party_name in ["Ind", "TUV", "Spk"]:
                votes = int(row['Of which other winner'])
            else:
                votes = int(row[party_name])

            # Create an MP object
            mp = MP(mp_name, constituency, party_name)
            mp.add_votes(votes)
            mp_list.append(mp)

            # Update or create the Party object
            if party_name not in party_list:
                party_list[party_name] = Party(party_name)
            party_list[party_name].increment_member_count()
            party_list[party_name].increment_votes(votes)

    # Print all MPs (Optional - Comment out if not needed)
    print("MP Details:")
    for mp in mp_list:
        print(mp)

    # Print party statistics
    print("\nParty Statistics:")
    for party in party_list.values():
        print(party)


# Test the function with a CSV file
read_file('Data.csv')

