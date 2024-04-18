def check_answer(ans: str):
    """
    This function returns "Yes" if a person has passed 42 or forty two or forty-two as an argument, otherwise it returns "No"

    Argument: 
        - ans (str)

    Returns:
        - result (str)
    """
    if ans.strip() == "42":
        return"Yes"
    elif ans.strip().lower() == "forty-two":
        return "Yes"
    elif ans.strip().lower() == "forty two":
        return "Yes"
    else:
        return "No"


