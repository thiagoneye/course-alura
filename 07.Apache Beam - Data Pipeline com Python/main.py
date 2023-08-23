import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.options.pipeline_options import PipelineOptions

from functions import string_to_list, list_to_dict, create_feature_from_date_string, create_tuple_from_dict_and_feature

# Set initial settings
pipeline_options = PipelineOptions(argv=None)
pipeline = beam.Pipeline(options=pipeline_options)

# Constants
columns_name = ['id', 'data_iniSE', 'casos', 'ibge_code', 'cidade', 'uf', 'cep', 'latitude', 'longitude']

# Define pipeline
dengue = (
    pipeline
    | "Dataset reading" >> ReadFromText("dataset/dengue.txt", skip_header_lines=1)
    | "String to list" >> beam.Map(string_to_list)
    | "List to dict" >> beam.Map(list_to_dict, columns_name=columns_name)
    | "Create key year_month" >> beam.Map(create_feature_from_date_string, key_of_date='data_iniSE')
    | "Create tuple from state" >> beam.Map(create_tuple_from_dict_and_feature, feature='uf')
    | "Group by state" >> beam.GroupByKey()
    | "Show results" >> beam.Map(print)
)

# Run pipeline 
pipeline.run()
