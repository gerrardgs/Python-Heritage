import pandas as pd

def read_data(filename):
    country_data = {}
    try:
        df = pd.read_excel(filename)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return country_data

    for index, row in df.iterrows():
        if pd.notna(row.iloc[0]):
            country = str(row.iloc[0]).strip()
            metrics = {}
            try:
                metrics['import_ton'] = float(row.iloc[1]) if pd.notna(row.iloc[1]) else 0
                metrics['export_ton'] = float(row.iloc[6]) if pd.notna(row.iloc[6]) else 0
                metrics['import_usd'] = float(row.iloc[13]) if pd.notna(row.iloc[13]) else 0
                metrics['export_usd'] = float(row.iloc[18]) if pd.notna(row.iloc[18]) else 0
                country_data[country] = metrics
            except ValueError as ve:
                print(f"Invalid value in row: {index + 2}, column causing error: {ve}")
                continue
    return country_data

def calculate_priority(country_data):
    # Define weights for each metric
    weights = {'import_ton': 1, 'export_ton': 2, 'import_usd': 3, 'export_usd': 4}
    for country, metrics in country_data.items():
        metrics['priority'] = (weights['import_ton'] * metrics['import_ton'] +
                               weights['export_ton'] * metrics['export_ton'] +
                               weights['import_usd'] * metrics['import_usd'] +
                               weights['export_usd'] * metrics['export_usd'])
    
    sorted_countries = sorted(country_data.items(), key=lambda x: x[1]['priority'], reverse=True)
    top_five = sorted_countries[:5]
    bottom_five = sorted_countries[-5:]
    return top_five, bottom_five

def main():
    filename = 'dataFIXmerges.xlsx'
    country_data = read_data(filename)
    top_five, bottom_five = calculate_priority(country_data)

    print("Top 5 Countries by Priority Score:")
    for country, data in top_five:
        print(f"{country}: Priority Score = {data['priority']}")

    print("\nBottom 5 Countries by Priority Score:")
    for country, data in bottom_five:
        print(f"{country}: Priority Score = {data['priority']}")

if __name__ == "__main__":
    main()
