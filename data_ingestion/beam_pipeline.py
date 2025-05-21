import apache_beam as beam
import json

class ParseJson(beam.DoFn):
    def process(self, element):
        yield json.loads(element)

def run_pipeline(input_path, output_path):
    with beam.Pipeline() as p:
        (
            p
            | 'ReadInput' >> beam.io.ReadFromText(input_path)
            | 'ParseJson' >> beam.ParDo(ParseJson())
            | 'WriteParquet' >> beam.io.WriteToParquet(output_path, schema=None)  # Placeholder schema
        )

if __name__ == "__main__":
    run_pipeline('input.json', 'output.parquet')
