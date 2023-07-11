def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res

def ConvertToStr(n):
  res = ""
  while n > 0:
    res += chr(n % 256)
    n //= 256
  return res[::-1]
