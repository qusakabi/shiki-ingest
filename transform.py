def transform_data(data):
    """
     Transforms raw anime data into a format suitable for saving to the database.

     Args:
         data (list): A list of dictionaries containing raw anime data.

     Returns:
         list: A list of dictionaries with transformed data.
     """
    transformed = []
    for item in data:
        transformed.append({
            "id": item.get("id"),
            "title": item.get("russian") or item.get("name", "Unknown"),
            "score": str(item.get("score", "0")),
            "episodes": item.get("episodes", 0),
            "status": item.get("status", "Unknown")
        })
    return transformed