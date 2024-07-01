from src.utils.data_load_ops import load_df_to_source_dataset
from src.assistants.data_generation_assistant import DataGenerationAssistant

def process_data(self, prompt):
    import pandas as pd
    data = assistant.generate_list(prompt=prompt)
    structured = []
    for i in range(0, len(data), 4):

        grouped = data[i:i+4]
        structured.append(grouped)

    return pd.DataFrame(data=structured[1:], columns=structured[0])



target_table = 'ai_load_test'
prompt = "10 beers"
assistant = DataGenerationAssistant()
df = process_data(prompt=prompt)


load_df_to_source_dataset(df=df, target_table=target_table)