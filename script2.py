import pandas as pd
import requests

def check_image_urls(input_csv, output_csv):
    # Read the input CSV file
    df = pd.read_csv(input_csv)
    
    # Prepare a list to hold results
    results = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        for col in df.columns:
            url = row[col]
            try:
                response = requests.head(url, timeout=10)  # Use HEAD request to check status
                status_code = response.status_code
            except requests.RequestException as e:
                status_code = None  # If there's an error, set status code to None
                print(f"Error for URL {url}: {e}")

            results.append({'URL': url, 'StatusCode': status_code})

    # Convert results to a DataFrame
    results_df = pd.DataFrame(results)
    
    # Write the results to the output CSV file
    results_df.to_csv(output_csv, index=False)

# Usage
input_csv = 'input_image_urls.csv'  # Replace with your input CSV file path
output_csv = 'output_image_status.csv'  # Replace with your output CSV file path

check_image_urls(input_csv, output_csv)
