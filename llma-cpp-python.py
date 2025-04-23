from huggingface_hub import hf_hub_download
from llama_cpp import Llama

model_path = hf_hub_download(
    repo_id="tharun66/mistral-sql-gguf",
    filename="mistral_sql_q4.gguf"
)
llm = Llama(
    model_path=model_path,
    n_ctx=512,
    n_threads=4,
    verbose=False
)

def clean_sql_response(response):
    sql = response.split('system')[0].strip()
    sql = sql.split('SQL:')[-1].strip() if 'SQL:' in sql else sql
    return sql

def generate_sql(llm, question):
    prompt = f"""### Task: Convert to SQL
### Question: {question}
### SQL:"""
    
    response = llm(
        prompt,
        max_tokens=128,
        temperature=0.7,
        stop=["system", "user", "assistant", "###"], 
        echo=False
    )
    
    return clean_sql_response(response['choices'][0]['text'])

# Test
test_questions = [
    "Show all active users",
    "List total sales by region"
]

print("SQL Query Generator")
print("-" * 50)

for question in test_questions:
    print(f"\nQuestion: {question}")
    sql = generate_sql(llm, question)
    print(f"SQL: {sql}")
