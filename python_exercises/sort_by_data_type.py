# Accept a mixed list containing data of various data types, then return the data as three lists sorted by data type
def sort_by_data_type(data):
  int_list = []
  float_list = []
  str_list = []

  for item in data:
    if isinstance(item, int):
      int_list.append(item)
    elif isinstance(item, float):
      float_list.append(item)
    elif isinstance(item, str):
      str_list.append(item)

  return sorted(int_list), sorted(float_list), sorted(str_list)
