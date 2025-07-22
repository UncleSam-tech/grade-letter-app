def is_valid_score(score):
    if score < 0  or score > 100:
        raise ValueError ("Score should be between 0 and 100")
    return True
    """
    Returns True if score is 0-100 inclusive.
    """
def grade_letter(score: int) -> str:
    is_valid_score (score)
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >=70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
   try:
    s = int(input("Enter your score: "))
    result =  grade_letter(s)
    print(f"Your Grade is: {result}")
   except ValueError as e:
    print(f"Error: {e}") 
