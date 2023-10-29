import shutil
import gradio as gr

def delt(text):
    txt = text
    shutil.rmtree("./output")
    return "Removed successfully..."

gr.Interface(delt, "text","text").launch(debug=True)