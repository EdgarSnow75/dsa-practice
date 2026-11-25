# LeetCode 271 (Require Premium) - Solved on NeetCode
def encode(strs: list[str]) -> str:
    encoded_string = ""
    for i in range(len(strs)):
        len_str = len(strs[i])
        encoded_string += f"{len_str}#{strs[i]}"
    return encoded_string


def decode(s: str) -> list[str]:
    decoded_str_lst = []
    i = 0
    while i < len(s) - 1:
        count = 0
        if s[i].isdigit():
            num_range = s[i]
            for k in range(i + 1, len(s)):
                if s[k].isdigit():
                    num_range += s[k]
                    count += 1
                elif s[k] == "#":
                    i += count
                    num_range = int(num_range)
                    len_str = i + num_range + 2
                    word = s[i + 2 : len_str]
                    decoded_str_lst.append(word)
                    i += num_range + 1
                    break
                else:
                    break
        i += 1
    return decoded_str_lst


# print(decode(encode(["edgar", "sno#w"])))
# print(decode(encode(["1,23", "45,6", "7,8,9"])))
# print(decode(encode(["we", "say", ":", "yes", "!@#$%^&*()"])))
# print(decode(encode(["12", "x"])))
