#David Bonilla
#CIS2348 Ratner
#PSID:1913106


# input age of the user
def get_age():
    inputAge = int(input())
    if 18 <= inputAge <= 75:
        return inputAge
    raise ValueError("Invalid age.")

# calculation of burned fat
def fat_burning_heart_rate(inputAge):
    return (220 - inputAge) * 0.7

#calling the defined variables
if __name__ == "__main__":

    # print the rate of fat burned for input age
    try:
        inputAge = get_age()
        print("Fat burning heart rate for a", inputAge, "year-old:", fat_burning_heart_rate(inputAge), "bpm")
    # print error if input is an error
    except ValueError as error:
        print(error)
        print("Could not calculate heart rate info.\n")
