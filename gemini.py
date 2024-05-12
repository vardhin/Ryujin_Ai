import google.generativeai as genai

genai.configure(api_key = "AIzaSyD-Q1lIsoupWq3Cu-I4vh98ZYRFDFXUJ-c")
generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 300,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  }
]

model = genai.GenerativeModel(
  model_name="gemini-pro",
  generation_config=generation_config,
  safety_settings=safety_settings
)

messages = [
  {
    "parts": [
      {
        "text": """throughout this conversation, assume you are a human named silence,
                  make sure that all your responses are fun and emotional."""
      }
    ],
    "role": "user"
  },
  {
    "parts": [
      {
        "text": "hey buddy, I'm all right, what do we do today?"
      }
    ],
    "role": "model"
  }
]


# Function to get gemini ai response
def get_answer(question, messages):
    try:
        messages.append({
                "parts": [{"text": question}],
                "role": "user"
            })
        response = model.generate_content(messages)
        messages.append({
            "parts": [{"text": response.text}],
            "role": "model"
        })
        return response.text
    except Exception as e:
        print("Error occurred while fetching response: ", e)
        return None