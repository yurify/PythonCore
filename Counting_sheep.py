def count_sheeps(arrayOfSheeps):
  count = 0
  for sheep in arrayOfSheeps:
      if sheep == True:
          count = count + 1
  return count