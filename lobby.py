def lobby(v2degs):
    '''Return the Lobby index from a dictionary of vertices and degrees'''
    l = 0 # Lobby index
    # Sort the degree values
    degs = sorted(v2degs.values(), reverse=True)
    for deg in degs:
        l += 1
        if deg <= l: # Found Lobby index
            break
    return l

v2degs = {"b": 4, "c": 3, "d": 18, "e": 21 }
print("The lobby index is {}".format(lobby(v2degs)))
