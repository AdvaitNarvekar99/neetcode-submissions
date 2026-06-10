class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = "".join(str(len(s))+'#'+s for s in strs)
        return enc_str

    def decode(self, s: str) -> List[str]:
        dec_list = []
        i=0
        num = "0"
 
        while i<len(s):
            if s[i] == "#":
                dec_list.append(s[i+1:i+1+int(num)])
                i = i+1+int(num)
                num = "0"
            else:
                if (s[i]>='0' and s[i]<='9'):
                    num = num + s[i]
                i+=1

        return dec_list