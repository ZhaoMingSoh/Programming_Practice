import java.math.BigInteger;

// Conver str a and str b into BigInteger objects, perform XOR and AND operations on them until the carry becomes 0.
class Solution {
    public static String addBinary(String a, String b) {
        BigInteger x = new BigInteger(a, 2);
        BigInteger y = new BigInteger(b, 2);
        BigInteger zero = new BigInteger("0", 2);
        BigInteger carry, answer;
        while (y.compareTo(zero) != 0) {
          answer = x.xor(y);
          carry = x.and(y).shiftLeft(1);
          x = answer;
          y = carry;
        }
        return x.toString(2);
    }

    public static void main(String []argv){
        String solution1 = addBinary("11","1");
        String solution2 = addBinary("1111","0010");
        System.out.println("The addition of "+"11"+" and "+"1"+" is "+solution1);
        System.out.println("The addition of "+"1111"+" and "+"0010"+" is "+solution2);
    }
}