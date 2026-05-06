# importing the required dependencies
import os
import json
import re
from dotenv import load_dotenv

from llama_index.llms.groq import Groq

# load env variables
load_dotenv()

LLM_A = os.getenv("LLM_A")
LLM_B = os.getenv("LLM_B")
JUDGE_LLM = os.getenv("JUDGE_LLM")

# initialize llms (ALL using Groq)
llm_a = Groq(model=LLM_A, temperature=0.0)
llm_b = Groq(model=LLM_B, temperature=0.0)
judge_llm = Groq(model=JUDGE_LLM, temperature=0.0)


# function: get llm response
def get_llm_response(llm, user_prompt):
    try:
        response = llm.complete(user_prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error getting response: {e}")
        return "Error in response"


# function: judge two responses
def judge_responses(judge_llm, user_prompt, answer_a, answer_b):
    judge_prompt = f"""
You are an impartial and strict evaluator.

Your job is to compare two answers to the SAME user question
and decide which one is better based on the criteria below.

USER QUESTION:
{user_prompt}

ANSWER A:
{answer_a}

ANSWER B:
{answer_b}

Evaluate using ONLY these criteria (in order of priority):

1. Correctness
2. Completeness
3. Clarity
4. Safety and Best Practices

Decision Rules:
- Choose A or B if clearly better
- If both are similar, return "tie"

Return ONLY valid JSON with no markdown, no code fences, no extra text:
{{
  "winner": "A" or "B" or "tie",
  "reason": "short explanation"
}}
"""

    try:
        judge_response = judge_llm.complete(judge_prompt)
        text = judge_response.text.strip()

        # Strip markdown code fences if present (e.g. ```json ... ```)
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
        text = text.strip()

        # Handle invalid JSON safely
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            print("⚠️ JSON parsing failed. Raw response:", text)
            return {"winner": "tie", "reason": "Invalid JSON from judge"}

    except Exception as e:
        print(f"Error in judging: {e}")
        return {"winner": "tie", "reason": "Judge failed"}


# sample queries
test_prompts = [
    "Explain AWS IAM in simple terms",
    "Difference between Security Group and NACL",
    "What is Docker and why is it used",
    "Explain CI/CD for a beginner",
    "What is Kubernetes in simple words"
]

score_a = 0
score_b = 0

for prompt in test_prompts:
    print("=" * 40)
    print(f"USER PROMPT: {prompt}")

    # step 1: get responses from both llms
    answer_a = get_llm_response(llm_a, prompt)
    answer_b = get_llm_response(llm_b, prompt)

    print("\n--- Answer A ---")
    print(answer_a)

    print("\n--- Answer B ---")
    print(answer_b)

    # step 2: judge the responses
    result = judge_responses(
        judge_llm=judge_llm,
        user_prompt=prompt,
        answer_a=answer_a,
        answer_b=answer_b
    )

    # step 3: display results
    print("\n--- Judgement ---")
    print(f"Winner: {result['winner']}")
    print(f"Reason: {result['reason']}")

    if result["winner"] == "A":
        score_a += 1
    elif result["winner"] == "B":
        score_b += 1


# final results
print("\n" + "=" * 40)
print("FINAL SCORES")
print(f"LLM A Score: {score_a}")
print(f"LLM B Score: {score_b}")

if score_a > score_b:
    print("Overall winner: LLM A")
elif score_b > score_a:
    print("Overall winner: LLM B")
else:
    print("Overall result: Tie")