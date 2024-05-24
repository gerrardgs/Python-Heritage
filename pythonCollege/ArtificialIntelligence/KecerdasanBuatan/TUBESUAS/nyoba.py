import pandas as pd

def read_data(filename):
    country_data = {}
    try:
        df = pd.read_excel(filename)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return country_data
    
    for index, row in df.iterrows():
        if pd.notna(row[0]):  
            country = str(row[0]).strip() 
            try:
                import_ton = float(row[1]) if pd.notna(row[1]) else 0
                export_ton = float(row[6]) if pd.notna(row[6]) else 0
                import_usd = float(row[13]) if pd.notna(row[13]) else 0
                export_usd = float(row[18]) if pd.notna(row[18]) else 0
                
            except ValueError:
                print(f"Invalid tonnage value in row: {index + 2}")
                continue
            
            country_data[country] = {
                'import_ton': import_ton,
                'export_ton': export_ton,
                'import_usd': import_usd,
                'export_usd': export_usd
            }
    return country_data

def top_countries_by_metric(country_data, metric, top_n=5):
    return sorted(country_data.items(), key=lambda x: x[1][metric], reverse=True)[:top_n]

def main():
    filename = 'dataFIXmerges.xlsx'
    country_data = read_data(filename)

    top_exporters_ton = top_countries_by_metric(country_data, 'export_ton')
    top_importers_ton = top_countries_by_metric(country_data, 'import_ton')
    top_exporters_usd = top_countries_by_metric(country_data, 'export_usd')
    top_importers_usd = top_countries_by_metric(country_data, 'import_usd')

    print("Top Exporters by Heavy (TON):")
    for country, data in top_exporters_ton:
        print(f"{country}: {data['export_ton']}")

    print("\nTop Importers by Heavy (TON):")
    for country, data in top_importers_ton:
        print(f"{country}: {data['import_ton']}")

    print("\nTop Exporters by Value (USD):")
    for country, data in top_exporters_usd:
        print(f"{country}: {data['export_usd']}")

    print("\nTop Importers by Value (USD):")
    for country, data in top_importers_usd:
        print(f"{country}: {data['import_usd']}")

if __name__ == "__main__":
    main()
