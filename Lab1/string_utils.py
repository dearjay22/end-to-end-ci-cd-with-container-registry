def reverse_string(text: str) -> str:
    """Return the reverse of the input string."""
    return text[::-1]


if __name__ == "__main__":
    sample = "Hello"
    print(f"Original: {sample}")
    print(f"Reversed: {reverse_string(sample)}")