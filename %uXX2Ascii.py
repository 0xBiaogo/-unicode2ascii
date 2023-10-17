encoded_text = "%u66%u6c%u61%u67%u7b%u77%u33%u5f%u68%u34%u76%u33%u5f%u74%u6f%u30%u5f%u6d%u34%u6e%u79%u5f%u77%u68%u31%u74%u33%u5f%u73%u70%u34%u63%u65%u5f%u32%u61%u35%u62%u34%u65%u30%u34%u7d"

encoded_parts = [int(part, 16) for part in encoded_text.split("%u")[1:] if part]
decoded_text = ''.join(chr(char) for char in encoded_parts)

print(decoded_text)
