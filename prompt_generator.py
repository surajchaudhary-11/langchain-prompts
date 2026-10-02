from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Explain the research paper "{paper_input}" with these settings:

Explanation style: {style_input}
Explanation length: {length_input}

Rules:
1. Explain the main idea and why the paper is important.
2. Use simple examples where they help.
3. If you are not sure about a detail, say "I am not sure" instead of guessing.
""",
    input_variables=['paper_input', 'style_input', 'length_input'],
)

template.save('template.json')