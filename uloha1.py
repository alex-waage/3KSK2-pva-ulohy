def is_point_on_surface(point, room_size):
    """
    Check if the point is on one of the surfaces (walls, floor, ceiling) of the room.
    """
    return any(c in [0, room_size] for c in point)

def calculate_pipe_length(room_size, point1, point2):
    """
    Calculate the minimum required length of the pip.
    """
    # Validate room size and points
    if room_size <= 0 or not all(0 <= c <= room_size for p in [point1, point2] for c in p):
        return f"Nespravny vstup."

    # Check if both points are on the surfaces of the room
    if not (is_point_on_surface(point1, room_size) and is_point_on_surface(point2, room_size)):
        return f"Nespravny vstup."

    # Calculate the length of the pipe
    pipe_length = sum(abs(c1 - c2) for c1, c2 in zip(point1, point2))

    return f"Delka potrubi: {pipe_length}"

def main():
    try:
        room_size = float(input("Zadejte velikost místnosti (délku strany krychle): "))
        point1 = tuple(float(x) for x in input("Zadejte souřadnice prvního bodu (x, y, z) oddělené čárkou: ").split(','))
        point2 = tuple(float(x) for x in input("Zadejte souřadnice druhého bodu (x, y, z) oddělené čárkou: ").split(','))

        result = calculate_pipe_length(room_size, point1, point2)
        print(result)
        
    except ValueError:
        print("Nespravny vstup. Zadejte prosím číselné hodnoty.")

if __name__ == "__main__":
    main()
