

def create_tile_map():    # map_size1, map_size2
    tile_map = [['empty'] * 1000 for i in range(1000)]

    for i in range(1000):
        tile_map[i][0] = 'Water'
        tile_map[i][0] = 'testura_peska'
        tile_map[i][0] = 'testura_peska'
        tile_map[i][1] = 'textura_dorogi'
        tile_map[i][2] = 'textura_dorogi'
        tile_map[i][3] = 'textura_travy'
        tile_map[i][4] = 'textura_travy'
        tile_map[i][5] = 'textura_vody'
        tile_map[i][6] = 'textura_vody'
        tile_map[i][7] = 'textura_travy'
        tile_map[i][8] = 'textura_travy'
        tile_map[i][9] = 'textura_travy'
        tile_map[i][10] = 'textura_travy'
        tile_map[i][11] = 'Water'
        tile_map[i][12] = 'testura_peska'
        tile_map[i][13] = 'testura_peska'
        tile_map[i][14] = 'textura_dorogi'
        tile_map[i][15] = 'textura_dorogi'
        tile_map[i][16] = 'textura_travy'
        tile_map[i][17] = 'textura_travy'
        tile_map[i][18] = 'textura_vody'
        tile_map[i][19] = 'textura_vody'
        tile_map[i][20] = 'Water'
        tile_map[i][21] = 'Water'
        tile_map[i][22] = 'Water'
        tile_map[i][23] = 'Water'

    return tile_map


def create_fight_map():   # map_size1, map_size2
    tile_map = [['empty'] * 30 for i in range(30)]

    for i in range(30):
        tile_map[i][0] = 'textura_dorogi'
        tile_map[i][0] = 'textura_dorogi'
        tile_map[i][0] = 'textura_dorogi'
        tile_map[i][1] = 'textura_dorogi'
        tile_map[i][2] = 'Water'
        tile_map[i][3] = 'textura_dorogi'
        tile_map[i][4] = 'textura_dorogi'
        tile_map[i][5] = 'textura_dorogi'
        tile_map[i][6] = 'textura_dorogi'
        tile_map[i][7] = 'textura_dorogi'
        tile_map[i][8] = 'Water'
        tile_map[i][9] = 'textura_dorogi'
        tile_map[i][10] = 'textura_dorogi'
        tile_map[i][11] = 'textura_dorogi'
        tile_map[i][12] = 'textura_dorogi'
        tile_map[i][13] = 'Water'
        tile_map[i][14] = 'textura_dorogi'
        tile_map[i][15] = 'textura_dorogi'
        tile_map[i][16] = 'textura_dorogi'
        tile_map[i][17] = 'textura_dorogi'
        tile_map[i][18] = 'textura_dorogi'
        tile_map[i][19] = 'textura_dorogi'
        tile_map[i][20] = 'textura_dorogi'
        tile_map[i][21] = 'textura_dorogi'
        tile_map[i][22] = 'textura_dorogi'
        tile_map[i][23] = 'textura_dorogi'

    for i in range(30):
        tile_map[1][i] = 'Water'
        tile_map[19][i] = 'Water'

    return tile_map

