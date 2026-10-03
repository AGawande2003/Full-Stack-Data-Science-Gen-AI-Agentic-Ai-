import gradio as gr
import pandas as pd
import numpy as np
import random

df = pd.DataFrame({
    'height': np.random.randint(50, 70, 25),
    'weight': np.random.randint(120, 320, 25),
    'age': np.random.randint(18, 65, 25),
    'ethnicity': [random.choice(["white", "black", "asian"]) for _ in range(25)]
})

with gr.Blocks() as demo:
    gr.LinePlot(df, x="weight", y="height")

demo.launch()

# movies = pd.read_csv(r'C:\Users\adars\Full_stack_data _Science_with_Ai\Full_stack_data _Science_with_Ai\practice_Projects_&_Task\MovieLens_20M_Dataset_project\archive_dataset\movie.csv')