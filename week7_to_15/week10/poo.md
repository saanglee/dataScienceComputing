def save_to_csv(data): # csv title = year+month+day+hour+minute.csv
fieldnames = ['', 'stock_name', 'current_price', 'previous_day_price', 'fluctuation_rate', 'face_value', 'market_cap', 'listed_shares', 'foreigner_ratio', 'volume', 'PER', 'ROE']

    current = datetime.datetime.now().strftime('%Y%m%d%H%M')

    with open(f'{current}.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
