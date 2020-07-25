import xlrd
book = xlrd.open_workbook("teams_data.xls", formatting_info=True)

# for index, sh in enumerate(sheets):
sheet = book.sheet_by_index(0)
print(sheet.name)
# print "Sheet:", sheet.name
# rows, cols = sheet.nrows, sheet.ncols
# print "Number of rows: %s   Number of cols: %s" % (rows, cols)
# for row in range(rows):
# for col in range(cols):
# print "row, col is:", row+1, col+1,
thecell = sheet.cell(38, 0)
# # could get "dump", "value", "xf_index"
print (thecell.value)
xfx = sheet.cell_xf_index(18, 6)
xf = book.xf_list[xfx]
bgx = xf.background.pattern_colour_index
pattern_colour = book.colour_map[bgx]
print (pattern_colour[0])
