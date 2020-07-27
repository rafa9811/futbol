import xlrd
import os


def load_w():
    path_list = os.getcwd().split('/')
    generic_path = ""

    for elem in path_list[1:]:
        if not elem == 'futbol':
            generic_path += '/'
            generic_path += elem
        else:
            generic_path += '/'
            generic_path += elem
            break
    path = generic_path + '/excel/teams_data.xls'
    book = xlrd.open_workbook(path, formatting_info=True)
    sheet = book.sheet_by_index(0)
    return book, sheet


def load_coachs(team):
    path_list = os.getcwd().split('/')
    generic_path = ""

    for elem in path_list[1:]:
        if not elem == 'futbol':
            generic_path += '/'
            generic_path += elem
        else:
            generic_path += '/'
            generic_path += elem
            break
    path = generic_path + '/excel/' + team + '.xls'
    book = xlrd.open_workbook(path, formatting_info=True)
    sheet = book.sheet_by_index(0)
    return book, sheet


def get_teams():
    book, sheet = load_w()
    teamlist = []
    for i in range(4, 44):
        teamlist.append(sheet.cell(i, 0).value)
    return teamlist


def team_row(team):
    book, sheet = load_w()
    for i in range(4, 44):
        if sheet.cell(i, 0).value == team:
            return i
    return -1


def get_group(team):
    book, sheet = load_w()
    row = team_row(team)

    return str(sheet.cell(row, 1).value)


def get_coachs(team):
    book, sheet = load_coachs(team)
    list = []
    i = 2
    j = 8
    name = str(sheet.cell(i, j).value)
    job = str(sheet.cell(i, j+1).value)
    while name != "":
        list.append((job, name))
        i += 1
        name = str(sheet.cell(i, j).value)
        job = str(sheet.cell(i, j+1).value)
    return list


def get_player_first_kit(team):
    book, sheet = load_w()
    row = team_row(team)

    xfx = sheet.cell_xf_index(row, 6)
    shirt1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 7)
    shirt2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 8)
    shorts1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 9)
    shorts2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 10)
    shocks1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 11)
    shocks2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    return {'shirt1':shirt1, 'shirt2':shirt2, 'shorts1':shorts1, 'shorts2':shorts2, 'shocks1':shocks1, 'shocks2':shocks2}


def get_gk_first_kit(team):
    book, sheet = load_w()
    row = team_row(team)

    xfx = sheet.cell_xf_index(row, 12)
    shirt1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 13)
    shirt2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 14)
    shorts1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 15)
    shorts2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 16)
    shocks1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 17)
    shocks2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    return {'shirt1':shirt1, 'shirt2':shirt2, 'shorts1':shorts1, 'shorts2':shorts2, 'shocks1':shocks1, 'shocks2':shocks2}


def get_player_scnd_kit(team):
    book, sheet = load_w()
    row = team_row(team)

    xfx = sheet.cell_xf_index(row, 18)
    shirt1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 19)
    shirt2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 20)
    shorts1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 21)
    shorts2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 22)
    shocks1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 23)
    shocks2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    return {'shirt1':shirt1, 'shirt2':shirt2, 'shorts1':shorts1, 'shorts2':shorts2, 'shocks1':shocks1, 'shocks2':shocks2}


def get_gk_scnd_kit(team):
    book, sheet = load_w()
    row = team_row(team)

    xfx = sheet.cell_xf_index(row, 24)
    shirt1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 25)
    shirt2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 26)
    shorts1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 27)
    shorts2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 28)
    shocks1 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    xfx = sheet.cell_xf_index(row, 29)
    shocks2 = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]

    return {'shirt1':shirt1, 'shirt2':shirt2, 'shorts1':shorts1, 'shorts2':shorts2, 'shocks1':shocks1, 'shocks2':shocks2}


def get_bibs(team):
    book, sheet = load_w()
    row = team_row(team)
    xfx = sheet.cell_xf_index(row, 30)
    bibs = book.colour_map[book.xf_list[xfx].background.pattern_colour_index]
    return bibs
