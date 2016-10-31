from pandocfilters import toJSONFilter, Para, Str, Space, RawBlock

def pauseFilter(key, value, format, meta):
  if key == 'RawBlock' and value[0] == "<!--pause-->":
    return Para([Str("."),Space(),Str("."),Space(),Str(".")])

if __name__ == "__main__":
  toJSONFilter(pauseFilter)
