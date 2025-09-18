def write_author_data(filename="Auther.txt"):
    """Writes author information to a text file."""

    try:
        athrnm = input("Name of author: ")
        no = int(input("No. of Books: "))  # Convert to integer
        nmOfPub = input("Name of Publication House: ")
        Title = input("Title of Book: ")

        with open(filename, 'w') as f:  # 'with' ensures the file is closed
            f.write(f"Name of author: {athrnm}\n")
            f.write(f"No. of Books: {no}\n")
            f.write(f"Name of Publication House: {nmOfPub}\n")
            f.write(f"Title of Book: {Title}\n")

        print(f"Author data written to {filename} successfully.")

    except ValueError:
        print("Error: Invalid input for 'No. of Books'. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_author_data(filename="Auther.txt"):
    """Reads and prints author information from a text file."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


# Example usage:
write_author_data()  # Write the data
read_author_data()   # Read and print the data
