import pandas as pd

def clean_data(data):
    """Clean and transform the scraped data."""
    try:
        df = pd.DataFrame(data)
        if df.empty:
            print("Warning: Empty DataFrame received")
            return df

        try:
            df['Rating'] = (df['Rating']
                        .str.extract(r'(\d+\.?\d*)', expand=False)
                        .fillna(0)
                        .astype(float))
        except Exception as e:
            print(f"Error processing Rating column: {e}")
            df['Rating'] = 0
        try:
            df['Colors'] = (df['Colors']
                        .str.extract(r'(\d+\.?\d*)', expand=False)
                        .fillna(0)
                        .astype(int))
        except Exception as e:
            print(f"Error processing Colors column: {e}")
            df['Colors'] = 0

        try:
            df['Size'] = (df['Size']
                        .str.replace(r'Size:\s*', '', regex=True)
                        .str.replace(r'[^a-zA-Z0-9]', '', regex=True)
                        .str.strip())
        except Exception as e:
            print(f"Error processing Size column: {e}")
            df['Size'] = 'Unknown'

        try:
            df['Gender'] = (df['Gender']
                        .str.replace(r'Gender:\s*', '', regex=True)
                        .str.strip())
        except Exception as e:
            print(f"Error processing Gender column: {e}")
            df['Gender'] = 'Unknown'

        try:
            df['Price'] = (df['Price']
                        .str.extract(r'(\d+\.?\d*)', expand=False)
                        .fillna(0)
                        .astype(float))
            df = df.loc[df['Price'] > 0]
            df = df.loc[df['Title'] != 'Unknown Product']
        except Exception as e:
            print(f"Error processing Price column: {e}")
            return pd.DataFrame()

        return df

    except Exception as e:
        print(f"Error in clean_data function: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

def convert_currency(df, exchange_rate):
    """Convert prices to local currency using the specified exchange rate."""
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        
        if not isinstance(exchange_rate, (int, float)) or exchange_rate <= 0:
            raise ValueError("Exchange rate must be a positive number")

        df = df.copy()
        df['Price'] = df['Price'] * exchange_rate
        return df

    except Exception as e:
        print(f"Error in convert_currency function: {e}")
        return pd.DataFrame()