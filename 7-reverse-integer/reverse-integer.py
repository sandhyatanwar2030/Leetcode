class Solution:

  def reverse(self, x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)

    # 32-bit integer limits
    limit = 2**31 - 1 if sign == 1 else 2**31
    rev = 0

    while x != 0:
      pop = x % 10
      x //= 10

      # Overflow check before multiplication
      if rev > (limit - pop) // 10:
        return 0

      rev = rev * 10 + pop

    return sign * rev