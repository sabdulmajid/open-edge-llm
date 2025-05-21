import dask.dataframe as dd

def process_parquet(input_path, output_path):
    df = dd.read_parquet(input_path)
    # Example: filter and save
    filtered = df[df['sensor'] == 'temperature']
    filtered.to_parquet(output_path)

if __name__ == "__main__":
    process_parquet('input.parquet', 'filtered.parquet')
