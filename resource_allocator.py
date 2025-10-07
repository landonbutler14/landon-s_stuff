#This program allocates resources giving extra to Mira and Tov. Mira receives 13% of the remainder and Tov receives 11%.
num_colonists = input("Enter number of colonists: ")

while not num_colonists.isdigit():
        print("Invalid input, please enter integers only.")
        num_colonists = input("Enter number of colonists: ")
num_colonists = int(num_colonists)

total_units = input("Enter total resource units available: ")

while not total_units.isdigit():
         print("Invalid input, please enter integers only.")
         total_units = input("Enter total resource units available: ")
total_units = int(total_units)


remainder_after_shoreleave = total_units - ((num_colonists - 2) * 3)
mira_extra_share = remainder_after_shoreleave * 0.13
tov_extra_share = (remainder_after_shoreleave - mira_extra_share) * 0.11
remainder_to_be_split = remainder_after_shoreleave - (mira_extra_share + tov_extra_share)
share_per_colonist = remainder_to_be_split / (num_colonists)
mira_share = mira_extra_share + share_per_colonist
tov_share = tov_extra_share + share_per_colonist

print(f"Each colonist's share: {share_per_colonist:.2f} ")
print(f"Mira's share: {mira_share:.2f} ")
print(f"Tov's share: {tov_share:.2f} ")
input("Press Enter to exit")
