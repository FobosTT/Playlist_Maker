def split_and_append(b, s, k, bachata, salsa, kizomba, playlist):
    # Initialize variables to keep track of the current index in each list
    first_index = 0
    second_index = 0
    third_index = 0

    # Loop until we have processed all of the segments
    while first_index < len(bachata) or second_index < len(salsa) or third_index < len(kizomba):
        # Append b segments from the first list
        for i in range(b):
            if first_index >= len(bachata):
                break
            playlist.append(bachata[first_index])
            first_index += 1

        # Append s segments from the second list
        for i in range(s):
            if second_index >= len(salsa):
                break
            playlist.append(salsa[second_index])
            second_index += 1

        # Append k segments from the third list
        for i in range(k):
            if third_index >= len(kizomba):
                break
            playlist.append(kizomba[third_index])
            third_index += 1


# Example usage
# playlist = []
# split_and_append(2, 1, 3, bachata, salsa, kizomba, playlist)
# print(playlist)  # Output: [1, 2, 'a', 3, 4, 'b', 5, 'c', 'x', 'y', 'z']
