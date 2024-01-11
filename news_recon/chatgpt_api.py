import requests

def query_chatgpt(article_content, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {
        "model": "gpt-4",  # Specify the model here
        "messages": [
            {"role": "system", "content": "Analyze the following article, thanks! Please reply succinctly, without explanations or prefixes, on a line by line basis, with the third and fourth just replying to the number."},
            {"role": "user", "content": article_content}  # Pass the article content directly
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response
