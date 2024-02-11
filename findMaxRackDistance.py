"""
Problem Statement:

You have a row of bike racks, some of which are already occupied (denoted as "used"). You want to park your bike and maximize the distance between your bike and any other bikes. You can only park your bike between the first and last used racks, inclusive.

"""


def find_max_distance(used_racks):
    """
    Finds the maximum distance between a new bike rack and any existing bikes.

    Args:
        used_racks: A list of integers representing the positions of used bike racks.

    Returns:
        The maximum distance between the new bike rack and any existing bikes.
    """

    used_racks.sort()

    if len(used_racks) == 2:
        return (used_racks[1] - used_racks[0]) // 2  # Handle two-rack case

    max_distance = 0
    for i in range(len(used_racks) - 1):
        distance = used_racks[i + 1] - used_racks[i]
        if distance > 1:
            max_distance = max(max_distance, distance)

    return max_distance // 2  # Divide by 2 since bike can be placed anywhere in the gap


# Example usage:
used_racks = [1, 3, 6, 8, 11]
max_distance = find_max_distance(used_racks)
print(max_distance)  # Output: 1
