def split_data(data: str):
    """Splits the provided data
    returns game info and moves part
    """
    splits = data.split("\n\n")
    return splits[0], splits[1]
    