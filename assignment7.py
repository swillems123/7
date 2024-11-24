def sort_animes_by_popularity(input_file: str, output_file: str):
    """
    Reads an anime list from a CSV, sorts it by popularity, and writes the name and rating to a new CSV.
    
    :param input_file: Path to the input CSV file containing anime data.
    :param output_file: Path to the output CSV file for sorted results.
    """
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            lines = file.readlines()

        if not lines:
            print("Error: Input file is empty.")
            return

        # Extract headers and data rows
        headers = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]

        # Check for required columns
        if 'Name' not in headers or 'Popularity' not in headers or 'Rating' not in headers:
            print("Error: Input file must contain 'Name', 'Popularity', and 'Rating' columns.")
            return

        # Get the indices of required columns
        name_idx = headers.index('Name')
        popularity_idx = headers.index('Popularity')
        rating_idx = headers.index('Rating')

        # Convert popularity to integers for sorting
        data.sort(key=lambda x: int(x[popularity_idx]))

        # Prepare the output data with name and rating columns
        output_data = [['Name', 'Rating']] + [[row[name_idx], row[rating_idx]] for row in data]

        # Write to the output file
        with open(output_file, 'w') as file:
            for row in output_data:
                file.write(','.join(row) + '\n')

        print(f"Sorted animes by popularity and saved to {output_file}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except ValueError as e:
        print(f"Error: {e}. Ensure the 'Popularity' column contains valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage example with the correct file paths
input_csv = r'C:\Users\sethw\OneDrive\Documents\Projects\assignement\toprankedanime.csv'
output_csv = r'C:\Users\sethw\OneDrive\Documents\Projects\sorted_animes.csv'

sort_animes_by_popularity(input_csv, output_csv)
