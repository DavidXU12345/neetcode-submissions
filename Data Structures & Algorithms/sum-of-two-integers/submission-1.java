public class Solution {
    public int getSum(int a, int b) {
        // java has 32-bit fixed length for integer, so no mask is needed like Python solution
        while (b != 0) {
            int carry = (a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
}