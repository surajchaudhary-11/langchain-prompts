from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    'Explain {topic} in {length} words.'
)

prompt = template.invoke({'topic': 'machine learning', 'length': '50'})

print(prompt)