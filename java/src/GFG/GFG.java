/******
 *
 * Minimum flips to make all 1s in the left and 0s in the right | set 1 (using bitmask)
 *
 * Given a binary array, we can flip all the 1 are in the left part and all the 0 to the right part. Calculate the
 * minimum flips required to make 1s in the left and 0s in right.
 *
 * Examples:
 *
 * input: 1011000
 * output: 1
 * i flip is required to make it 1111000
 *
 *
 * input: 00001
 * output: 2
 * 2 flips required to make it 10000
 *
 * For solving this problem we use bit masking. Firs, we convert this array to string, then we find the equivalent
 * decimal number of that binary string. We try all mask with all possibilities of 1s in the left and 0s in the right.
 * We iterate a loop till decimal number becomes zero. Each time we will do bitwise XOR of the number with mask and
 * number of ones in XOR value will be the number of flips required. We decrease n by 1 and update the mask.
 *
 * 1. Take binary array as input
 * 2. Convert array to string and then equivalent decimal number (num)
 * 3. Take initial mask value and iterate till num <= 0
 * 4. Find required flips using (num XOR mask)
 * 5. Find minimum flips and decrease num and update mask
 * 6. Return the minimum count
 *
 *****/

// Java program to find minimum flips to make all 1s in left
import java.io.*;


class GFG {

    // function to count minimum number of flips
    public static int findMiniFlip(int[] nums)
    {
        int n = nums.length;
        String s = "";
        for (int i = 0; i < n; i++)
        {
            s += nums[i];
        }

        // this is converting string s into integer of base 2
        long num = Integer.parseInt(s, 2);

        // initialize minXor with n that can be maximum number of flips
        int minXor = n;

        // left shift 1 by (n-1) bits
        long mask = (1 << (n-1));
        while (n-1 > 0){

            // calculate bitwise Xor of num and mask
            long temp = (num ^ mask);

            //Math.min(a, b) returns minimum of a and b return minimum number of flips till that digit
            minXor = Math.min(minXor, countones(temp));
            n--;

            mask = (mask | (1 << n));
        }
        return minXor;
    }


    // function to count number of 1s
    public static int countones(long n)
    {
        int c = 0;
        while (n > 0)
        {
            n = n & (n-1);
            c++;
        }
        return c;
    }


    public static void main(String[] args)
    {
        int[] nums = {1, 0, 1, 1, 0, 0, 0};
        int n = findMiniFlip(nums);
        System.out.println(n);
    }
}