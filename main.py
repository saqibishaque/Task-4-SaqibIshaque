def run_quiz():
    # State Initialization: Integer vault to enforce cumulative math
    score = 0
    total_questions = 3

    print("=== Welcome to The General Knowledge Quiz ===")
    print("Answer each question to test your knowledge.\n")

    # --- Question 1 ---
    # Step 1 & 2: Ask, Capture, and Sanitize (Whitespace + Case Normalization)
    q1 = input("1. What is the capital of France? ").strip().lower()

    # Step 3 & 4: Evaluate logic gate & execute feedback
    if q1 == "paris":
        print("Correct! +1 point.\n")
        score += 1
    else:
        print("Incorrect. The correct answer is Paris.\n")

    # --- Question 2 ---
    q2 = input("2. Which planet is known as the Red Planet? ").strip().lower()

    if q2 == "mars":
        print("Correct! +1 point.\n")
        score += 1
    else:
        print("Incorrect. The correct answer is Mars.\n")

    # --- Question 3 ---
    q3 = input("3. What is the largest ocean on Earth? ").strip().lower()

    if q3 in ["pacific", "pacific ocean"]:
        print("Correct! +1 point.\n")
        score += 1
    else:
        print("Incorrect. The correct answer is the Pacific Ocean.\n")

    # --- Final Output ---
    # Delivered via formatted f-string runtime interpolation
    print("-" * 35)
    print(f"Quiz Complete! Your Final Score: {score:>2}/{total_questions}")
    print("-" * 35)


if __name__ == "__main__":
    run_quiz()
