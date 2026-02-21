"""ETL module: placeholder batch job."""
import os
import csv


def run_spark_etl():
    """Run a simple ETL job that reads CSVs from /data/raw and writes processed files to /data/processed.
    This is a lightweight example — expand with real transformations.
    """
    raw_dir = "/data/raw"
    out_dir = "/data/processed"
    os.makedirs(out_dir, exist_ok=True)

    if not os.path.exists(raw_dir):
        return

    # Simple CSV processing
    for filename in os.listdir(raw_dir):
        if filename.endswith('.csv'):
            input_path = os.path.join(raw_dir, filename)
            output_path = os.path.join(out_dir, f"processed_{filename}")
            
            try:
                with open(input_path, 'r') as infile, open(output_path, 'w', newline='') as outfile:
                    reader = csv.DictReader(infile)
                    if reader.fieldnames:
                        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
                        writer.writeheader()
                        for row in reader:
                            writer.writerow(row)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
