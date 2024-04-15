#q1
def main():
    num_cities = int(input("Enter the number of cities: "))

    with open("cities.txt", "w") as file:
        for _ in range(num_cities):
            city_name = input("Enter city name: ")
            population = input("Enter population: ")
            mayor = input("Enter mayor's name: ")

            file.write(f"{city_name},{population},{mayor}\n")

    print("Data has been successfully stored in cities.txt")

if __name__ == "__main__":
    main()


#q2:
def main():
    with open("student.txt", "a") as file:
        file.write("Now we are AI students\n")
    print("Message appended to student.txt")

if __name__ == "__main__":
    main()

